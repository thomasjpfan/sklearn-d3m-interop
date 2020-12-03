import pytest
from pathlib import Path


@pytest.fixture
def sklearn_wrap_path():
    sklearn_wrap = Path(".") / "sklearn-wrap"

    if not sklearn_wrap.exists():
        pytest.fail(
            "sklearn-wrap submodule does not exist, run "
            "git submodule init && git submodule update"
        )
