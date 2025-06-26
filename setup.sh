#!/bin/bash

# Thiết lập để không bị hỏi tương tác khi cài đặt
export DEBIAN_FRONTEND=noninteractive

# Cài đặt các dependency cần thiết (ca-certificates, curl, gnupg)
apt-get update && apt-get install -y ca-certificates curl gnupg

# Thêm kho lưu trữ (repository) của NodeSource cho Node.js phiên bản 18.x
# Kho lưu trữ này chứa các phiên bản Node.js mới nhất
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -

# Bây giờ, cài đặt Node.js phiên bản 18 từ kho lưu trữ vừa thêm
apt-get install -y nodejs

# In ra phiên bản Node.js và npm để kiểm tra trong log
echo "--- Node.js version after install ---"
node -v
echo "--- npm version after install ---"
npm -v

# Cuối cùng, cài đặt gemini-cli bằng npm
echo "--- Installing @google/gemini-cli ---"
npm install -g @google/gemini-cli
echo "--- Installation finished ---"
