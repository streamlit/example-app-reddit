import base64
import toml

output_file = ".streamlit/secrets.toml"

with open("firestore-key.json") as json_file:
    json_text = json_file.read()
    json_bytes = base64.b64encode(str.encode(json_text))

config = {"key": json_bytes.decode("utf-8"), "textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)
