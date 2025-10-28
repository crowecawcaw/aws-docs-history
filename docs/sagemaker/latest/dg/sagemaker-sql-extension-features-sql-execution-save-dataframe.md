# Save SQL

query results in a pandas DataFrame

You can store the results of your SQL query in a pandas DataFrame. The easiest way to
output query results to a DataFrame is to use the [SQL editor features of the
JupyterLab SQL extension](sagemaker-sql-extension-features-editor.md "sagemaker-sql-extension-features-editor.md") query-result dropdown and choose the
**Pandas dataframe** option.

Alternatively, you can add the parameter `--output '{"format": "DATAFRAME",
 "dataframe_name": "`dataframe_name`"}'` to your connection
string.

For example, the following query extracts details of customers with the highest balance
from the `Customer` table in Snowflake's `TPCH_SF1` database, using
both pandas and SQL:

- In this example, we extract all the data from the customer table and save then in a
  DataFrame named `all_customer_data`.

```
%%sm_sql --output '{"format": "DATAFRAME", "dataframe_name": "all_customer_data"}' --metastore-id `snowflake-connection-name` --metastore-type GLUE_CONNECTION
SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
```

```
Saved results to all_customer_data
```

- Next, we extract the details of the highest account balance from the
  DataFrame.

```
all_customer_data.loc[all_customer_data['C_ACCTBAL'].idxmax()].values
```

```
array([61453, 'Customer#000061453', 'RxNgWcyl5RZD4qOYnyT3', 15,
'25-819-925-1077', Decimal('9999.99'), 'BUILDING','es. carefully regular requests among the blithely pending requests boost slyly alo'],
dtype=object)
```
