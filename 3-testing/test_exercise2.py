import os
import pytest
import tempfile

@pytest.fixture
def temp_file():
	with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
		f.write("Hello, world!")
		f.flush()
		yield f.name
	os.remove(f.name)

@pytest.fixture(scope="module")
def example():
	# work that happens before the test
	yield "value"
	# work that happens after the test

def test_temp_file_contents(temp_file):
    # Open the temporary file and read its contents
    with open(temp_file, 'r') as f:
        contents = f.read()
    # Check if the contents are correct
    assert contents == 'Hello, world!'