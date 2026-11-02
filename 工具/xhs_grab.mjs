// 只抓 JSON 接口响应，找 doc_id / download_url
const PORT = 9333;
const TARGET = process.argv[2];
const WAIT = Number(process.argv[3] || 10000);

const r = await fetch(`http://127.0.0.1:${PORT}/json/new?${encodeURIComponent(TARGET)}`, { method: 'PUT' });
const tab = await r.json();
const ws = new WebSocket(tab.webSocketDebuggerUrl);
let id = 0;
const pending = new Map();
const send = (method, params = {}) => new Promise((res) => {
  const i = ++id; pending.set(i, res);
  ws.send(JSON.stringify({ id: i, method, params }));
});
const reqs = [];
ws.addEventListener('message', (ev) => {
  const msg = JSON.parse(ev.data);
  if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg.result); pending.delete(msg.id); return; }
  if (msg.method === 'Network.responseReceived') {
    const { url, status, mimeType } = msg.params.response;
    if (/\/api\//.test(url) && /json/.test(mimeType || '')) reqs.push({ url, rid: msg.params.requestId, status });
  }
});
await new Promise((res) => ws.addEventListener('open', res));
await send('Network.enable');
await send('Page.enable');
await send('Emulation.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' });
await send('Page.navigate', { url: TARGET });
await new Promise((r) => setTimeout(r, WAIT));

const out = [];
for (const q of reqs) {
  let b = null;
  try { b = await send('Network.getResponseBody', { requestId: q.rid }); } catch (e) { }
  if (!b || !b.body) continue;
  const body = b.body;
  if (/doc_id|download_url|preview_pdf_url|\.docx/.test(body)) out.push({ url: q.url, body: body.slice(0, 6000) });
}
console.log(JSON.stringify({ apiCount: reqs.length, hits: out.length, out }, null, 1));
ws.close();
