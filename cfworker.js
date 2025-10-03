export default {
  async fetch(request) {
    try {
      const id = new URL(request.url).searchParams.get("id");
      if (!id) return new Response("Missing 'id' parameter", { status: 400 });
      const hmacBytes = new Uint8Array(await crypto.subtle.sign(
        "HMAC",
        await crypto.subtle.importKey(
          "raw",new Uint8Array([3,85,15,247,247,2,96,1,81,213,104,110,184,228,121,54]),
          { name: "HMAC", hash: "SHA-512" },false,["sign"]
        ),
        new TextEncoder().encode(id)
      ));
      const t = Math.floor(Date.now() / 10000000);
      const aesOut = new Uint8Array([(t >> 12) & 0xff, (t >> 4) & 0xff, ((t & 0xf) << 4) | 3]);
      const aesIn = new Uint8Array(await crypto.subtle.encrypt(
        { name: "AES-CTR", counter: hmacBytes.slice(32, 48), length: 128 },
        await crypto.subtle.importKey("raw", hmacBytes.slice(0, 32), { name: "AES-CTR" }, false, ["encrypt"]),
        aesOut
      ));
      const unpacked = aesIn.reduce((n, b) => (n << 8) | b, 0) & 0xffffff;
      return new Response(`*#${(aesOut[2] & 0xf).toString().padStart(2, "0")}*${unpacked.toString().padStart(8, "0")}#*`);
    } catch {
      return new Response("FUCK YOU", { status: 500 });
    }
  }
};