#!/bin/bash
clear
set -e

echo "[+] Installing dependencies..."
sudo apt update
sudo apt install -y git nmap python3

echo "[+] Installing to /opt/secscan..."

sudo rm -rf /opt/secscan
sudo git clone https://github.com/Obnunnv/Capstone.git /opt/secscan

echo "[+] Creating global command..."

sudo bash -c 'cat > /usr/local/bin/secscan' <<'EOF'
#!/bin/bash
cd /opt/secscan/scan
exec python3 main.py
EOF

sudo chmod +x /usr/local/bin/secscan

clear
echo "[+] Installation complete!"
echo "Run with: secscan"
