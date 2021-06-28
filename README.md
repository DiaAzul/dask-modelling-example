# Healthcare systems modelling using Dask/Pandas

This project is an example implementation of a business model using Dask and Pandas DataFrames. The model is greatly simplified for training purposes - the original model was significantly more complex and replaced a Microsoft Excel model which had become unmanageable.

```python
@delayed
def _business_transform(
    self,
    acute_forecast: pd.DataFrame,
    community_forecast: pd.DataFrame,
    assumptions_data: pd.DataFrame,
) -> pd.DataFrame:
```
