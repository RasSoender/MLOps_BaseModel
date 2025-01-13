from torch.utils.data import Dataset
import torch
from src.code_structure.data import corrupt_mnist
import pytest

import os.path
@pytest.mark.skipif(not os.path.exists("data/"), reason="Data files not found")
def test_data():
    """Test the MyDataset class."""
    training, testing = corrupt_mnist() 
    assert len(training) == 30000, "not enough training data"
    assert len(testing) == 5000, "not enough testing data"
    for dataset in [training, testing]:
        for x, y in dataset:
            assert x.shape == (1, 28, 28)
            assert y in range(10)

    train_targets = torch.unique(training.tensors[1])
    assert (train_targets == torch.arange(0,10)).all(), "missing labels in the training"
    test_targets = torch.unique(testing.tensors[1])
    assert (test_targets == torch.arange(0,10)).all(), "missing labels in the testing"