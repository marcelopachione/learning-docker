import os
import urllib.request
import json
import pandas as pd

# Persistencia de dados
# Bind Mount

output_dir = "/app/data"
output_file = os.path.join(output_dir, "issPosition.csv")

with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as resp:

    if resp.status == 200:
        print("Status Code: 200")

        data = resp.read()
        obj = json.loads(data)

        timestamp = obj['timestamp']
        latitude = obj['iss_position']['latitude']
        longitude = obj['iss_position']['longitude']

        df = pd.DataFrame({

            'Timestamp': [timestamp],
            'Latitude': [latitude],
            'Longitude' : [longitude]
        })

        df.to_csv(output_file, index=False)
        print(f"Dados salvos em: {output_file} ")

        print(pd.read_csv(output_file))

    else:
        print("Error: ", resp.status)