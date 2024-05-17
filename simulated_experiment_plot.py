import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/simulated_experiment_results.csv")

data= data[["num_items", "item_code_bytes",	"mRT", "method"]]
mm_data = data[data.method == "Matrix Multiplication"]
print(mm_data)

markers = ["o", "^"]
linesize=2
markersize=5
for item_code_bytes in data.item_code_bytes.unique():
    code_data = data[data.item_code_bytes == item_code_bytes]
    fig, ax = plt.subplots(1, 1, figsize=(2.8, 1.8))
    for i, method in enumerate(["PQTopK", "RecJPQ"]):
        method_code_data = code_data[code_data.method == method]
        ax.plot(method_code_data["num_items"], method_code_data["mRT"], label=method, marker = markers[i], linewidth=linesize, markersize=markersize)
        pass
    ax.plot(mm_data["num_items"], mm_data["mRT"], label="Default", linestyle="solid", linewidth=linesize, markersize=markersize, marker = "x")
    ax.set_xlabel("Number of Items")
    ax.set_ylabel("mRT (ms)")
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_yticks([1e0, 1e1, 1e2, 1e3, 1e4])
    ax.set_xticks([1e4, 1e5, 1e6, 1e7, 1e8, 1e9])
    ax.grid()
    ax.legend(prop={'size': 8})
    fig.tight_layout()
    fig.savefig(f"figures/simulated_figure_{item_code_bytes}.pdf")




exit()
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
