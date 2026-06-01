const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const PORT = 8080;

// Discover the local network IP address (e.g. 192.168.x.x)
function getLocalIpAddress() {
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      // Look for IPv4 and non-loopback addresses
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address;
      }
    }
  }
  return 'localhost';
}

const localIp = getLocalIpAddress();

// Create HTTP server
const server = http.createServer((req, res) => {
  // Normalize path and prevent directory traversal
  let filePath = '.' + req.url;
  if (filePath === './') {
    filePath = './index.html';
  }

  // Resolve absolute path
  const absolutePath = path.resolve(__dirname, filePath);
  
  // Ensure the requested file is inside this directory (security check)
  if (!absolutePath.startsWith(path.resolve(__dirname))) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('Forbidden');
    return;
  }

  // Get file extension for MIME type mapping
  const extname = String(path.extname(absolutePath)).toLowerCase();
  const mimeTypes = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
  };

  const contentType = mimeTypes[extname] || 'application/octet-stream';

  // Read and serve the file
  fs.readFile(absolutePath, (error, content) => {
    if (error) {
      if (error.code === 'ENOENT') {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 File Not Found');
      } else {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Sorry, check with the site admin for error: ' + error.code + ' ..\n');
      }
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
});

// Start listening on all network interfaces (0.0.0.0)
server.listen(PORT, '0.0.0.0', () => {
  console.log('\n=============================================================');
  console.log('                 JAPANEX - SERVEUR LOCAL RUNNING             ');
  console.log('=============================================================');
  console.log(`\n  👉 Sur votre Mac : http://localhost:${PORT}`);
  console.log(`  👉 Sur votre Téléphone (même WiFi) : http://${localIp}:${PORT}`);
  console.log('\n-------------------------------------------------------------');
  console.log('   Pressez [Ctrl + C] dans ce terminal pour arrêter le serveur');
  console.log('=============================================================\n');
});
