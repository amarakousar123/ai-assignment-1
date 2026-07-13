response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=payload,
    timeout=30
)
print("STATUS:", response.status_code)
print("RESPONSE:", response.text)
result = response.json()
if "choices" in result:
    reply = result["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})
else:
    return jsonify({"reply": str(result)})
