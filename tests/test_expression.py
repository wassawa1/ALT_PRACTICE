import os
import sys
import pandas as pd
import pytest
import logging
import math

# Configure logging to write to a file
log_file_path = os.path.join(os.path.dirname(__file__), r'.\debug.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from main import Expression, execute

# CSVファイルからテストベクトルを読み込む関数
def load_test_vectors(filepath):
    logger.debug(f"Loading test vectors from {filepath}")
    df = pd.read_csv(filepath, dtype={'expected': str, 'error': bool})
    logger.debug(f"Loaded {len(df)} test cases")
    return df.to_dict(orient='records')

# テストベクトルを使用したパラメータ化テスト
@pytest.mark.parametrize("params", load_test_vectors(os.path.join(os.path.dirname(__file__), 'test_patterns.csv')))
def test_expression_evaluation(params):
    input_value = params['input']
    expected = params['expected']

    try:
        result = execute(input_value)
        logger.info(f"Result for input: {input_value} is {result}")
        
        if expected == '' or (isinstance(expected, float) and math.isnan(float(expected))):
            # If expected is NaN, result should be empty string ''
            assert result == '', f"Expected {expected}, got {result}"
        else:
            assert result == expected, f"Expected {expected}, got {result}"

        # Log success message if the test passes
        logger.info(f"Test succeeded for input: {input_value}")

    except Exception as e:
        logger.error(f"Test failed for input: {input_value} with error: {e}")
        raise

if __name__ == "__main__":
    pytest.main()