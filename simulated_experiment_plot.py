import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/simulated_experiment_results.csv")

data= data[["num_items", "item_code_bytes",	"mRT"]]
markers = [".", "^", "x", "d", "D"]
plt.figure(figsize=(5,3))

for i, codel_length in enumerate(data["item_code_bytes"].unique()):
    df_cl = data[data.item_code_bytes == codel_length]
    plt.plot(df_cl["num_items"], df_cl["mRT"], label=f"Code Length: {codel_length}", marker = markers[i])

plt.xlabel("Number of Items")
plt.ylabel("Median Running Time (ms)")
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("figures/simulated_figure.pdf")
