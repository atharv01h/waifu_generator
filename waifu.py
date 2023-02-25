import requests
import json

def generate_waifu():
    response = requests.post('https://api.waifulabs.com/generate', data={'step': '2'})
    if response.status_code == 200:
        result = json.loads(response.text)
        return result['image']
    else:
        print(f"Error {response.status_code}: {response.reason}")
        return None

waifu_image = generate_waifu()
if waifu_image:
    with open('waifu.png', 'wb') as f:
        f.write(requests.get(waifu_image).content)
    print("Waifu image saved as waifu.png")
else:
    print("Failed to generate waifu")
