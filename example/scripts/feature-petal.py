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

# Generates petal features.

import pandas as pd

# + tags=["parameters"]
upstream = ['get']
product = None
# -


df = pd.read_csv(upstream['get']['data'])

df.head()

df['pulse*waist'] = df['Pulse'] * df['Waist']

df[['pulse*waist']].to_csv(product['data'], index=False)


