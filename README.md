# Flask Splash Docker 🐳🔥

A minimal Dockerized Flask app that serves a centered splash screen with TailwindCSS.

---

## 📦 Quick Start (Local)

```bash
git clone https://github.com/FullBoreStudios/flask-splash-docker.git
cd flask-splash-docker
docker build -t flask-splash .
docker run -d --name flask-splash -p 5000:5000 flask-splash
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🧠 For `fbcli` Users (Deploy to Server)

```bash
fb redeploy fb-web-1 flask-splash-docker
```

This assumes:

- Your server is defined in `fbcli` under `fb-web-1`
- The repo is cloned at `~/flask-splash-docker` on the server
- Docker is installed and your app listens on port `5000`

---

## 🌐 Nginx Reverse Proxy Setup (on reverse proxy box)

1. SSH into your reverse proxy server:

```bash
ssh fbadmin@your.reverse.proxy.ip
```

2. Create a new nginx config:

```bash
sudo nano /etc/nginx/sites-available/yourdomain.com
```

Paste this:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location / {
        proxy_pass http://192.168.22.112:5000;  # Update with internal IP of your app host
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

3. Enable the site and reload nginx:

```bash
sudo ln -s /etc/nginx/sites-available/yourdomain.com /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

---

## 🔐 Enable HTTPS with Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Choose the redirect option when prompted to force HTTPS.

---

## 🛠 Notes

- Flask app runs on port `5000` by default
- Static assets (like `logo.png`) live in `/static`
- Uses TailwindCSS via CDN (no local Node required)
- Great for splash pages, landing pages, and placeholder apps

---

## 📄 License

MIT – free to use, fork, deploy, or strip for parts.
