#!/usr/bin/env python3
import urllib.request
import urllib.error

endpoints = [
    "https://api.example.com/healthz",
    "https://api.example.com/v1/status"
]

for url in endpoints:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            print(f"✅ {url} - Status: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"❌ {e.code} Error on {url}!")
    except Exception as e:
        print(f"💥 Critical: Connection failed to {url}: {e}")
