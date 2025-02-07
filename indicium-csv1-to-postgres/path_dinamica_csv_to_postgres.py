import os
import yaml
from datetime import datetime
import subprocess

base_folder = "/home/denise/code-challenge/files-github-indicium/data/csv/"
today_date = datetime.today().strftime("%Y-%m-%d")
data_folder = os.path.join(base_folder, today_date)
csv_filepath = os.path.join(data_folder, "order_details.csv")

if os.path.exists(csv_filepath):
    meltano_file = "meltano.yml"

    with open(meltano_file, "r") as file:
        config = yaml.safe_load(file)

    for extractor in config["plugins"]["extractors"]:
        if extractor["name"] == "tap-csv":
            extractor["config"]["files"][0]["path"] = csv_filepath

    with open(meltano_file, "w") as file:
        yaml.dump(config, file, default_flow_style=False)

    subprocess.run(["meltano", "run", "tap-csv", "target-postgres"])
