import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Create dummy dataset
data = pd.DataFrame({
    "study_hours": [1,2,3,4,5,6,7,8],
    "sleep_hours": [4,5,6,6,7,7,8,8],
    "attendance": [50,60,65,70,75,80,85,90],
    "result": [0,0,0,1,1,1,1,1]
})

X = data[["study_hours", "sleep_hours", "attendance"]]
y = data["result"]

model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!") 