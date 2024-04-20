import pandas as pd

df = pd.DataFrame().from_records([
    {"estoque": 1},
    {"estoque": 4},
    {"estoque": 5},
    {"estoque": 2}
])
df["cores"] = df.apply(lambda x: "red" if x > 5 else "yellow")