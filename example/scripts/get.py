# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Get raw data

import pandas as pd
from sklearn.datasets import load_linnerud

# + tags=["parameters"]
upstream = None
product = None
# -


raw = load_linnerud(as_frame=True)
df = raw['data']

df.head()

df['Pulse'] = raw['target']['Pulse']

df['Waist'] = raw['target']['Waist']

df['Weight'] = raw['target']['Weight']

df.to_csv(product['data'], index=False)


