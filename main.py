import sys
import yaml
import pandas as pd
from pathlib import Path


INFO_FILE = "./info.yaml" # YAML file with files to join
OUTPUT_FILE = "out.csv"   # Output CSV to save result file


print("Info file:  ", INFO_FILE)
print("Output file:", OUTPUT_FILE)


# Read in the data from the info file with the lists
# of files to be joined together
print("Loading info file...")
try:
    data = yaml.safe_load(Path(INFO_FILE).read_text())
except Exception as e:
    print("Failed to read info file", e)
    sys.exit()

# Create a list to hold all of the output files
full = []

# Iterate through the files
files = data.get("files")

# Validate the list of file paths
if files is None:
    print("Error: Didn't find the key 'files' in the info file")
    sys.exit()
if not isinstance(files, list) or not all(isinstance(p, str) for p in files):
    print("Error: Expected 'files' in the info file to be a list of strings")
    sys.exit()

print(f"Found {len(files)} file paths in the info file")
for p in files:
    # Confirm that the path exists
    if not Path(p).exists():
        print(f"Path '{p}' does not exist")
        sys.exit()

    # Read in the file
    df = pd.read_csv(p)

    # Convert the table to a list of recrods
    records = df.to_dict("records")

    # Add the records to the full list
    full.extend(records)

print("Finished iterating through files")
print("Joining into a single file and saving.")

# Convert the full list to a dataframe
pd.DataFrame(full).to_csv(OUTPUT_FILE, index=False)
print("Done.")

