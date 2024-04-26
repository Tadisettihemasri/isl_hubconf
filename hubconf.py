import torch
import torchvision.models as models
from sklearn.datasets import make_blobs

# def fun_print():
# 	print("Hello World!")
# 	return "Hey"

# model=models.vgg16(weights='IMAGENET1K_V1')
# torch.save(model.state_dict(), 'model_weights.pth')

# def get_model():
# 	print("model")
# 	return model
def make_blobs:
	X, y = make_blobs(n_samples=10, centers=3, n_features=2, random_state=0)
	print(X, y)
