# Healthcare systems modelling using Dask/Pandas

Forecasting activity and finances is a tasks frequently undertaken using spreadsheets and, for simple models, this works well. However, as models become more complex developing and maintaining models in spreadsheets becomes harder - particularly when the models have more than two dimensions such as age, sex, disease group, hospital, region, year, and so on. For larger models alternative approaches are required, in this case the proposed approach uses Python, Pandas DataFrames and Dask. The benefits of this approach are:

+ **Separation of code, data and presentation** - Spreadsheets provide an integrated environment for storing data, code and presenting results; however, this makes larger models less flexible and harder to manage. Separating the modelling into the three domains provides greater flexibility, at the loss of an all-in-one packaging of the model.

+ **Documentation** - One of the most challenging features of modelling in spreadsheets is documenting the model. Coding in Python has a strong culture of documentation which increases code maintainability if used appropriately.

+ **Unit testing** - Testing in spreadsheets is limited, often to control totals. Separation of the code from the data provides greater opportunities to introducing unit testing using established testing frameworks.

This example project provides an implementation of a simple forecasting model using Dask and Pandas DataFrames. The model is greatly simplified for demonstration purposes, however, covers the main principles of importing data, performing calculations and outputting the results.

## Case study example

The model case study.

```mermaid
Acute hospital data -> acute forecast
Population growth -> acute forecast
Community data -> community forecast
Population growth -> community forecast
acute forecast -> business transform
community forecast -> business transform
assumption -> business transform
business transform -> output
```

```python
@delayed
def _business_transform(
    self,
    acute_forecast: pd.DataFrame,
    community_forecast: pd.DataFrame,
    assumptions_data: pd.DataFrame,
) -> pd.DataFrame:
```
