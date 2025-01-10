import matplotlib.pyplot as plt
import numpy as np
import json

# Reload the data from the uploaded files
file_paths = {
    "CIRR": "./CIRRthreshold.json",
    "FIQ": "./FIQthreshold.json",
    "CIRCO": "./CIRCOthreshold.json"
}

data = {}
for dataset, path in file_paths.items():
    with open(path, 'r') as file:
        data[dataset] = json.load(file)

# Function to extract and sort data
def extract_plot_data(dataset_key, metric_key):
    dataset = sorted(data[dataset_key], key=lambda x: x["Threshold"])  # Sort by Threshold
    alpha = [entry["Threshold"] for entry in dataset]
    metric = list(zip(*[entry[metric_key] for entry in dataset]))  # Transpose for K values
    return np.array(alpha), np.array(metric)

# Extracting sorted data
alpha_CIRR, recall_CIRR = extract_plot_data("CIRR", "Recall")
alpha_FIQ, recall_FIQ = extract_plot_data("FIQ", "Recall")
alpha_CIRCO, map_CIRCO = extract_plot_data("CIRCO", "mAP")

# Names for each K value
K_labels_CIRR = ["R@1", "R@5", "R@10", "R@50"]
K_labels_CIRCO = ["mAP@5", "mAP@10", "mAP@25", "mAP@50"]

# Creating subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Subplot 1: CIRR Dataset
plt.figure(figsize=(6, 4))
for i, label in enumerate(K_labels_CIRR):
    plt.plot(alpha_CIRR, recall_CIRR[i], marker='o', label=label)
plt.title("CIRR Dataset")
plt.xlabel("Threshold")
plt.ylabel("Recall")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("./Threshold_CIRR_Dataset.png")

# Subplot 2: FIQ Dataset
plt.figure(figsize=(6, 4))
for i, label in enumerate(K_labels_CIRR):  # Same K-labels as CIRR
    plt.plot(alpha_FIQ, recall_FIQ[i], marker='s', label=label)
plt.title("FashionIQ Dataset")
plt.xlabel("Threshold")
plt.ylabel("Recall")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("./Threshold_FashionIQ_Dataset.png")

# Subplot 3: CIRCO Dataset
plt.figure(figsize=(6, 4))
for i, label in enumerate(K_labels_CIRCO):
    plt.plot(alpha_CIRCO, map_CIRCO[i], marker='^', label=label)
plt.title("CIRCO Dataset")
plt.xlabel("Threshold")
plt.ylabel("mAP")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig("./Threshold_CIRCO_Dataset.png")
