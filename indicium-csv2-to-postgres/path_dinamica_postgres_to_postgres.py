import os
import yaml
import csv
from datetime import datetime
import subprocess


base_folder = "/home/denise/code-challenge/files-github-indicium/data/postgres/"
today_date = datetime.today().strftime("%Y-%m-%d")
data_folder = os.path.join(base_folder, today_date)


files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

if not files:
    exit(1)

meltano_file = "meltano.yml"

for file in files:
    csv_filepath = os.path.join(data_folder, file)
    entity_name = os.path.splitext(file)[0]  

    
    with open(csv_filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader) 

    primary_key = header[0]  

    with open(meltano_file, "r") as f:
        config = yaml.safe_load(f)

    
    for extractor in config["plugins"]["extractors"]:
        if extractor["name"] == "tap-csv":
            extractor["config"]["files"][0]["path"] = csv_filepath
            extractor["config"]["files"][0]["entity"] = entity_name
            extractor["config"]["files"][0]["keys"] = [primary_key]  

    with open(meltano_file, "w") as f:
        yaml.dump(config, f, default_flow_style=False)

    print(f" `meltano.yml` atualizado para {csv_filepath} (entity: {entity_name}, key: {primary_key})")

    # Executa 11 vezes
    subprocess.run(["meltano", "run", "tap-csv", "target-postgres"])

print("Processamento finalizado para todos os arquivos!")
