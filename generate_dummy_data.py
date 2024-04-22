# Generating dummy data using metasyn without using an input dataset
# input: ./config-dummy-data.toml
# output: ./dummy-data.csv

from metasyn import MetaFrame

# Create MetaFrame from config file 
config = MetaFrame.from_config("config-dummy-data.toml")

# Export config file to json for reference
config.to_json("gmf-dummy-data.json")

# Generate a new DataFrame from the MetaFrame
df_synth = config.synthesize()

# Export DataFrame to csv
df_synth.write_csv("dummy-data.csv")
