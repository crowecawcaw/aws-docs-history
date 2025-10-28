We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Data Rearrangement

The data rearrangement functionality enables you to create a
datasource that is based on only a portion of the input data that
it points to. For example, when you create an ML Model using the
**Create ML Model** wizard in the
Amazon ML console, and choose the default evaluation option,
Amazon ML automatically reserves 30% of your data for ML model
evaluation, and uses the other 70% for training. This
functionality is enabled by the Data Rearrangement feature of
Amazon ML.

If you are using the Amazon ML API to create datasources, you can
specify which part of the input data a new datasource will be
based. You do this by passing instructions in the
`DataRearrangement` parameter to the `CreateDataSourceFromS3`,
`CreateDataSourceFromRedshift` or `CreateDataSourceFromRDS` APIs.
The contents of the DataRearrangement string are a JSON string containing the
beginning and end locations of your data, expressed as
percentages, a complement flag, and a splitting strategy. For example, the following DataRearrangement string
specifies that the first 70% of the data will be used to create
the datasource:

```
{
    "splitting": {
        "percentBegin": 0,
        "percentEnd": 70,
        "complement": false,
        "strategy": "sequential"
    }
}
```

## DataRearrangement Parameters

To change how Amazon ML creates a datasource, use the follow parameters.

**PercentBegin (Optional)**

Use `percentBegin` to indicate where the data for the datasource starts.
If you do not include `percentBegin` and `percentEnd`, Amazon ML
includes all of the data when creating the datasource.

Valid values are `0` to `100`, inclusive.

**PercentEnd (Optional)**

Use `percentEnd` to indicate where the data for the datasource ends. If you do not
include `percentBegin` and `percentEnd`, Amazon ML includes all of the data
when creating the datasource.

Valid values are `0` to `100`, inclusive.

**Complement (Optional)**

The `complement` parameter tells Amazon ML to use the data that is
not included in the range of `percentBegin` to `percentEnd` to create a
datasource. The `complement` parameter is useful if you need to create
complementary datasources for training and evaluation.
To create a complementary datasource, use the same
values for `percentBegin` and `percentEnd`, along with the
`complement` parameter.

For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first
datasource has 25 percent of the data, and the second one has 75 percent of the data.

Datasource for evaluation:

```
{
    "splitting":{
        "percentBegin":0,
        "percentEnd":25
    }
}
```

Datasource for training:

```
{
    "splitting":{
        "percentBegin":0,
        "percentEnd":25,
        "complement":"true"
    }
}
```

Valid values are `true` and `false`.

**Strategy (Optional)**

To change how Amazon ML splits the data for a datasource, use the `strategy` parameter.

The default value for the `strategy` parameter
is `sequential`, meaning that Amazon ML takes all of the data records between the `percentBegin`
and `percentEnd` parameters for the datasource, in the order that the records appear in the input data

The following two `DataRearrangement` lines are examples of sequentially ordered
training and evaluation datasources:

Datasource for evaluation: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}`

Datasource for training: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential", "complement":"true"}}`

To create a datasource from a random selection of the data, set the `strategy` parameter to
`random` and provide a string that is used as the seed value for the random data splitting (for
example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy,
Amazon ML assigns each row of data a pseudo-random number, and then selects the rows that have an assigned
number between `percentBegin` and `percentEnd`. Pseudo-random numbers are assigned
using the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved.
The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly.
It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in
training and evaluation datasources containing non-similar data records.

The following two `DataRearrangement` lines are examples of non-sequentially ordered
training and evaluation datasources:

Datasource for evaluation:

```
{
    "splitting":{
        "percentBegin":70,
        "percentEnd":100,
        "strategy":"random",
        "strategyParams": {
            "randomSeed":"RANDOMSEED"
        }
    }
}
```

Datasource for training:

```
{
    "splitting":{
        "percentBegin":70,
        "percentEnd":100,
        "strategy":"random",
        "strategyParams": {
            "randomSeed":"RANDOMSEED"
        }
        "complement":"true"
    }
}
```

Valid values are `sequential` and `random`.

**(Optional) Strategy:RandomSeed**

Amazon ML uses the **randomSeed** to split the data. The default seed
for the API is an empty string. To specify a seed for the random split
strategy, pass in a string. For more information about random seeds, see
[Randomly Splitting Your Data](splitting-types.md#random-splitting "splitting-types.md#random-splitting") in the
_Amazon Machine Learning Developer Guide_.

For sample code that demonstrates how to use cross-validation with Amazon ML, go to [Github Machine Learning Samples](https://github.com/awslabs/machine-learning-samples "https://github.com/awslabs/machine-learning-samples").
