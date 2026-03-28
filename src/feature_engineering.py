def add_features(df):
    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["0-1 Year", "1-2 Years", "2-4 Years", "4-6 Years"]
    )

    df["MonthlyCharges_group"] = pd.cut(
        df["MonthlyCharges"],
        bins=[0, 35, 70, 120],
        labels=["Low", "Medium", "High"]
    )

    df["Churn_numeric"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df