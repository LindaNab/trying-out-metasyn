# Generating dummy data using metasyn without using an input dataset
# input: ./config-dummy-data.toml
# output: ./dummy-data.csv

import os
from metasyn import MetaFrame

# Create subdir "output" where output is saved
os.mkdir("output")

# Create MetaFrame from config file 
config = MetaFrame.from_config("input/config-dummy-data.toml")

# Export config file to json for reference
config.to_json("output/gmf-dummy-data.json")

# Generate a new DataFrame from the MetaFrame
df_synth = config.synthesize()

# Export DataFrame to csv
df_synth.write_csv("output/dummy-data.csv")
