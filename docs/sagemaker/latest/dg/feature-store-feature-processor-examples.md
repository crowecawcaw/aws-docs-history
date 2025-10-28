# Example Feature Processing code

for common use cases

The following examples provide sample Feature Processing code for common use cases. For a
more detailed example notebook showcasing specific use cases, see [Amazon SageMaker Feature Store Feature Processing notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-featurestore/feature_store_feature_processor.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-featurestore/feature_store_feature_processor.ipynb").

In the following examples, `us-east-1` is
the region of the resource, `111122223333`
is the resource owner account ID, and
`your-feature-group-name` is the feature group
name.

The `transactions` data set used in the following examples has the following
schema:

```
'FeatureDefinitions': [
  {'FeatureName': 'txn_id', 'FeatureType': 'String'},
  {'FeatureName': 'txn_time', 'FeatureType': 'String'},
  {'FeatureName': 'credit_card_num', 'FeatureType': 'String'},
  {'FeatureName': 'txn_amount', 'FeatureType': 'Fractional'}
]
```

###### Topics

- [Joining data from multiple data sources](#feature-store-feature-processor-examples-joining-multiple-sources "#feature-store-feature-processor-examples-joining-multiple-sources")
- [Sliding window aggregates](#feature-store-feature-processor-examples-sliding-window-aggregates "#feature-store-feature-processor-examples-sliding-window-aggregates")
- [Tumbling window aggregates](#feature-store-feature-processor-examples-tumbling-window-aggregates "#feature-store-feature-processor-examples-tumbling-window-aggregates")
- [Promotion from the offline store to online store](#feature-store-feature-processor-examples-promotion-offline-to-online-store "#feature-store-feature-processor-examples-promotion-offline-to-online-store")
- [Transformations with the Pandas library](#feature-store-feature-processor-examples-transforms-with-pandas-library "#feature-store-feature-processor-examples-transforms-with-pandas-library")
- [Continuous executions and automatic retries using event based triggers](#feature-store-feature-processor-examples-continuous-execution-automatic-retries "#feature-store-feature-processor-examples-continuous-execution-automatic-retries")

## Joining data from multiple data sources

```
@feature_processor(
    inputs=[
        CSVDataSource('s3://bucket/customer'),
        FeatureGroupDataSource('transactions')
    ],
    output='arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/`your-feature-group-name`'
)
def join(transactions_df, customer_df):
  '''Combine two data sources with an inner join on a common column'''

  return transactions_df.join(
    customer_df, transactions_df.customer_id == customer_df.customer_id, "inner"
  )
```

## Sliding window aggregates

```
@feature_processor(
    inputs=[FeatureGroupDataSource('transactions')],
    output='arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/`your-feature-group-name`'
)
def sliding_window_aggregates(transactions_df):
    '''Aggregates over 1-week windows, across 1-day sliding windows.'''
    from pyspark.sql.functions import window, avg, count

    return (
        transactions_df
            .groupBy("credit_card_num", window("txn_time", "1 week", "1 day"))
            .agg(avg("txn_amount").alias("avg_week"), count("*").alias("count_week"))
            .orderBy("window.start")
            .select("credit_card_num", "window.start", "avg_week", "count_week")
    )
```

## Tumbling window aggregates

```
@feature_processor(
    inputs=[FeatureGroupDataSource('transactions')],
    output='arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/`your-feature-group-name`'
)
def tumbling_window_aggregates(transactions_df, spark):
    '''Aggregates over 1-week windows, across 1-day tumbling windows, as a SQL query.'''

    transactions_df.createOrReplaceTempView('transactions')
    return spark.sql(f'''
        SELECT credit_card_num, window.start, AVG(amount) AS avg, COUNT(*) AS count
        FROM transactions
        GROUP BY credit_card_num, window(txn_time, "1 week")
        ORDER BY window.start
    ''')
```

## Promotion from the offline store to online store

```
@feature_processor(
    inputs=[FeatureGroupDataSource('transactions')],
    target_stores=['OnlineStore'],
    output='arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/transactions'
)
def offline_to_online():
    '''Move data from the offline store to the online store of the same feature group.'''

    transactions_df.createOrReplaceTempView('transactions')
    return spark.sql(f'''
        SELECT txn_id, txn_time, credit_card_num, amount
        FROM
            (SELECT *,
            row_number()
            OVER
                (PARTITION BY txn_id
                ORDER BY "txn_time" DESC, Api_Invocation_Time DESC, write_time DESC)
            AS row_number
            FROM transactions)
        WHERE row_number = 1
    ''')

```

## Transformations with the Pandas library

**Transformations with the Pandas library**

```
@feature_processor(
    inputs=[FeatureGroupDataSource('transactions')],
    target_stores=['OnlineStore'],
    output='arn:aws:sagemaker:`us-east-1`:`111122223333`:feature-group/transactions'
)
def pandas(transactions_df):
    '''Author transformations using the Pandas interface.

    Requires PyArrow to be installed via pip.
    For more details: https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark
    '''
    import pyspark.pandas as ps

    # PySpark DF to Pandas-On-Spark DF (Distributed DF with Pandas interface).
    pandas_on_spark_df = transactions_df.pandas_api()
    # Pandas-On-Spark DF to Pandas DF (Single Machine Only).
    pandas_df = pandas_on_spark_df.to_pandas()

    # Reverse: Pandas DF to Pandas-On-Spark DF
    pandas_on_spark_df = ps.from_pandas(pandas_df)
    # Reverse: Pandas-On-Spark DF to PySpark DF
    spark_df = pandas_on_spark_df.to_spark()

    return spark_df

```

## Continuous executions and automatic retries using event based triggers

```
from sagemaker.feature_store.feature_processor import put_trigger, to_pipeline, FeatureProcessorPipelineEvent
from sagemaker.feature_store.feature_processor import FeatureProcessorPipelineExecutionStatus

streaming_pipeline_name = "`target-pipeline`"

to_pipeline(
    pipeline_name=streaming_pipeline_name,
    step=transform
)

put_trigger(
    source_pipeline_events=[
        FeatureProcessorPipelineEvent(
            pipeline_name=streaming_pipeline_name,
            pipeline_execution_status=[
            FeatureProcessorPipelineExecutionStatus.STOPPED,
            FeatureProcessorPipelineExecutionStatus.FAILED]
        )
    ],
    target_pipeline=streaming_pipeline_name
)
```
