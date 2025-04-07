curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo -E bash -
yum install -y nodejs
playwright install chromium
uvicorn application:app --host 0.0.0.0 --port 8000
