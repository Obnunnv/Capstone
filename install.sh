#!/bin/bash

set -e

echo "[+] Installing dependencies..."
sudo apt update
sudo apt install -y nmap python3 git

echo "[+] Cloning repository..."
TMP_DIR=$(mktemp -d)

git clone https://github.com/Obnunnv/Capstone.git "$TMP_DIR/Capstone"

echo "[+] Installing secscan command..."

sudo bash -c "cat > /usr/local/bin/secscan" <<EOF
#!/bin/bash
cd $TMP_DIR/Capstone/scan
python3 main.py
EOF

sudo chmod +x /usr/local/bin/secscan

echo "[+] Installation complete!"
echo "Run with: secscan"
