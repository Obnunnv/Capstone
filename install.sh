#!/bin/bash

set -e

echo "[+] Installing dependencies..."
sudo apt update
sudo apt install -y nmap python3 git

echo "[+] Installing Capstone into /opt/secscan..."

sudo rm -rf /opt/secscan
sudo git clone https://github.com/Obnunnv/Capstone.git /opt/secscan

echo "[+] Creating command..."

sudo bash -c 'cat > /usr/local/bin/secscan' <<'EOF'
#!/bin/bash
cd /opt/secscan/scan
python3 main.py
EOF

sudo chmod +x /usr/local/bin/secscan

echo "[+] Done!"
echo "Run with: secscan"
