# csv-join

## Requirements

- Python 3.6+
- Python packages: 
  - `pandas`
  - `pyyaml`

## Instructions for Running

Clone the repository locally and install the required packages.

```bash
pip install -r requirements.txt
```

or 

```bash
python -m pip install -r requirements.txt
```

Update the `info.yaml` file with the list of CSV files to be joined together.

```yaml
files:
  - path/to/file-1.csv
  - path/to/file-2.csv
  - path/to/file-3.csv
```

Then run the file:

```bash
python main.py
```

The final CSV will be at the following path: `out.csv`



