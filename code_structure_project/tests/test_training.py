
import os
from src.code_structure.train import train
import pytest


@pytest.mark.parametrize("lr", [1e-3, 1e-2])
def test_training(lr):
    last_modified_time = os.path.getmtime("reports/figures/training_statistics.png")
    train(lr, epochs=1)
    new_modified_time = os.path.getmtime("reports/figures/training_statistics.png")

    assert(last_modified_time != new_modified_time), "the figure was not changed"