import pandas as pd
import kaggle
kaggle.api.authenticate()
print("API REQUESTS BEGINNING")
datasets = []
try:
    for i in range(1, 501):
        for dataset in kaggle.api.dataset_list(page = i, sort_by="votes"):
            datasets.append(dataset)
except kaggle.rest.ApiException:
    print(len(datasets)//20)
fields = [
            'ref', 'title', 'size', 'lastUpdated', 'downloadCount',
            'voteCount', 'usabilityRating'
        ]
print("API REQUESTS COMPLETE")
print("DATAFRAME CREATION")
dataset_fp = pd.DataFrame([[getattr(i, f) for f in fields] for i in datasets], columns=fields)
print("DATAFRAME CREATED")
print("WRITE OUT")
dataset_fp.to_csv("kaggle.csv.zip", index=None, compression="zip")
print("WRITE COMPLETE")
print("Goodbye!")
