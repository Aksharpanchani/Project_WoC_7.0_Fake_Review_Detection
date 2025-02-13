import joblib

# Load the model
model = joblib.load('model.pkl')

# Check the model type
print("Model type:", type(model))

# Print available methods to see if it has 'predict'
print("Model methods:", dir(model))
