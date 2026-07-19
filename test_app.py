import pandas as pd
import numpy as np
from app import transform

def test_salary():

    df = pd.DataFrame({
        "salary":[100]
    })

    result = transform(df)

    #assert result["salary"][0] == 110
    #pd.testing.assert_series_equal(result["salary"], pd.Series([110.0], name="salary"), check_less_precise=True)
    np.testing.assert_allclose(result["salary"][0], 110.0)
