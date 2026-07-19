import pandas as pd
from app import transform

def test_salary():

    df = pd.DataFrame({
        "salary":[100]
    })

    result = transform(df)

    assert result["salary"][0] == 110
