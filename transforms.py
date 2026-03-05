import base64, json

def format_json(text: str) -> str:
    obj=json.loads(text)
    return json.dumps(obj, indent=2, sort_keys=True) + '\n'

def b64_encode(text: str) -> str:
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def b64_decode(text: str) -> str:
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

def normalize(text: str) -> str:
    return ' '.join(text.split())
