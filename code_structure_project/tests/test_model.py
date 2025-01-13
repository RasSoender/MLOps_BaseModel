
from src.code_structure.model import MyAwesomeModel
import torch
import pytest

def test_model():
    network = MyAwesomeModel()
    x = torch.randn(1,1,28,28)
    y = network(x)
    assert(y.shape == (1,10)), "the output of the forward method do not have the right shape "


def test_error_on_wrong_shape():
    model = MyAwesomeModel()
    with pytest.raises(ValueError, match='Expected input to a 4D tensor'):
        model(torch.randn(1,2,3))
