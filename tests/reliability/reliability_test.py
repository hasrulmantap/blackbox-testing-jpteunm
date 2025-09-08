import requests

url = "https://jpteunm.com"
success_count = 0

for i in range(5):
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            success_count += 1
    except Exception as e:
        print("Request error:", e)

if success_count == 5:
    print("Reliability test passed!")
else:
    print(f"Reliability test failed! {success_count}/5 requests succeeded")
    raise SystemExit(1)

