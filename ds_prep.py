#Here the plan is to load and prepare the dataset loading the stanfordnlp/sst2 dataset
import torch
from datasets import load_dataset
dataset = load_dataset("Stanfordnlp/sst")
print(dataset)