import pandas as pd

def transform(df):
    df["salary"] = df["salary"] * 1.1
    return df

if __name__ == "__main__":

    df = pd.DataFrame({
        "name":["Ali","Sara"],
        "salary":[1000,2000]
    })

    result = transform(df)

    result.to_csv("output/result.csv",index=False)

    print("ETL Finished")
