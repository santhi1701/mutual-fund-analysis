import requests

schemes = {
    "HDFC Top 100":125497,
    "SBI Bluechip":119551,
    "ICICI Bluechip":120503,
    "Nippon Large Cap":118632,
    "Axis Bluechip":119092,
    "Kotak Bluechip":120841
}

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        print(f"✓ {code} ({name}) : Valid")

    else:

        print(f"✗ {code} ({name}) : Invalid")