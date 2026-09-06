

# Building a profile job configuration programmatically in AWS Glue DataBrew
<a name="profile.configuration"></a>

In this section, you can find descriptions of profile job steps and functions that you can use programmatically. You can use them either from the AWS Command Line Interface (AWS CLI) or by using one of the AWS SDKs.

In a profile job, you can customize a configuration to control how DataBrew evaluates your dataset. You can apply the configuration to a dataset or apply it to particular columns. You can build the configuration when creating a profile job, and then update it anytime.

A profile configuration structure includes four parts:
+ [ProfileColumns section](#profile-columns.statistics)
+ [DatasetStatisticsConfiguration section](#profile-dataset-stats-config)
+ [ColumnStatisticsConfigurations section](#profile-column-stats-config)
+ [EntityDetectorConfiguration section for configuring PII](#entity-detector-configuration)

Following is an example.

```
{
    "ProfileColumns": [
        {
            "Name": "example"
        },
        {
            "Regex": "example.*"
        }
    ],
    "DatasetStatisticsConfiguration": {
        "IncludedStatistics": [
            "CORRELATION"
        ],
        "Overrides": [
            {
                "Statistic": "CORRELATION",
                "Parameters": {
                    "columnSelectors": "[{\"name\":\"example\"}, {\"regex\":\"example.*\"}]"
                }
            }
        ]
    },
    "ColumnStatisticsConfigurations": [
        {
            "Selectors": [
                {
                    "Name": "example"
                }
            ],
            "Statistics": {
                "IncludedStatistics": [
                    "CORRELATION",
                    "DUPLICATE_ROWS_COUNT"
                ],
                "Overrides": [
                    {
                        "Statistic": "VALUE_DISTRIBUTION",
                        "Parameters": {
                            "binNumber": "10"
                        }
                    }
                ]
            }
        }
    ]
}
```

## ProfileColumns section
<a name="profile-columns.statistics"></a>

In the `ProfileColumns` section of your structure, set the columns from your dataset that you want to evaluate in your profile job. `ProfileColumns` is a list of column selectors (`Selectors`). You can specify either a column name or a regular expression in a column selector. An example follows.

```
"ProfileColumns": [{"Name": "example"}, {"Regex": "example.*"}]
```

When `ProfileColumns` is specified, only columns whose names match a name or regular expression in `ProfileColumns` are included in the profile job. If the profile job doesn't support a selected column's data type, DataBrew skips the selected column during the job run.

If ProfileColumns is undefined, the profile job evaluates all supported columns. Supported columns are columns containing data of a supported data type: `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`, `String`, or `Boolean`.

## DatasetStatisticsConfiguration section
<a name="profile-dataset-stats-config"></a>

In the `DatasetStatisticsConfiguration` section of your structure, you can build a configuration for intercolumn evaluations. The configuration includes `IncludedStatistics` and `Overrides`. An example follows.

```
"DatasetStatisticsConfiguration": {
    "IncludedStatistics": ["CORRELATION"],
    "Overrides": [
        {
            "Statistic": "CORRELATION",
            "Parameters": {
                "columnSelectors": "[{\"name\":\"example\"}, {\"regex\":\"example.*\"}]"
            }
        }
    ]
}
```

You can select evaluations that you want to have by adding evaluation names to `IncludedStatistics`. An example follows.

```
"IncludedStatistics": ["CORRELATION", "DUPLICATE_ROWS_COUNT"]
```

When you specify `IncludedStatistics`, only evaluations in the list are included in the profile job. If `IncludedStatistics` is undefined, the profile job runs all supported evaluations with default settings. You can exclude all evaluations by adding NONE to `IncludedStatistics`. An example follows.

```
"IncludedStatistics": ["NONE"]
```

### Configurable statistics at the dataset level
<a name="statistics.table01"></a>

In the `DatasetStatisticsConfiguration` section of your structure, a profile job supports the evaluations shown in the table following.


| **Statistic name** | **Description** | **Supported data types** | **Default status** | **Attributes of profile result** | **Type of profile result** | 
| --- | --- | --- | --- | --- | --- | 
| DUPLICATE\_ROWS\_COUNT | Count of duplicate rows in the dataset | all | Enable | duplicateRowsCount | Int | 
| CORRELATION | Pearson Correlation Coefficient between two columns | number | Enable | correlations (in each selected column) | Object | 

In `IncludedStatistics`, you can override each evaluation's default settings by adding an override. Each override includes the name of a particular evaluation and a parameter map.

In `DatasetStatisticsConfiguration`, a profile job supports the `CORRELATION` override. This override calculates the Pearson Correlation Coefficient between two columns from a list of selected columns. The default setting is selecting the first 10 numeric columns. You can specify either a number of columns or a list of column selectors to override the default setting.

`CORRELATION` takes these parameters:
+ `columnNumber` – The number of numeric columns. The profile job selects the first *n* columns from the dataset. This value should be greater than 1. Use `"ALL"` to select all numeric columns.
+ `columnSelectors:` – List of column selectors. Each selector can have either a column name or a regular expression.

An example follows.

```
{
    "Statistic": "CORRELATION",
    "Parameters": {
        "columnSelectors": "[{\"name\":\"example\"}, {\"regex\":\"example.*\"}]"
    }
}
```

## ColumnStatisticsConfigurations section
<a name="profile-column-stats-config"></a>

In the `ColumnStatisticsConfigurations` section of your structure, you can build configurations for particular columns. `ColumnStatisticsConfigurations` is a list of `ColumnStatisticsConfiguration` settings. In `ColumnStatisticsConfiguration`, there are `Selectors`, a list of column selectors, and `Statistics` for the configuration of statistics. An example follows.

```
{ 
    "Selectors": [{"Name": "example"}
    ],
    "Statistics": {
       "IncludedStatistics": ["CORRELATION", "DUPLICATE_ROWS_COUNT"]
        "Overrides": [
            {
                "Statistic": "VALUE_DISTRIBUTION",
                "Parameters": {
                    "binNumber": "10"
                }
            }
        ]
    }
}
```

`Selectors` is a list of column selectors. As with `ProfileColumns`, you can specify either a column name or a regular expression in each column selector. When you specify `Selectors`, the column configuration is applied to columns that match any column selector in `Selectors`. Otherwise, the configuration is applied to all supported columns.

In `Statistics`, you can override settings of selected columns. As with `DatasetStatisticsConfiguration`, `Statistics` has `IncludedStatistics` and `Overrides`.

To select the evaluations that you want, add evaluation names to `IncludedStatistics`. 

```
"IncludedStatistics": ["CORRELATION", "DUPLICATE_ROWS_COUNT"]                    
```

When you specify `IncludedStatistics`, only evaluations in the list are included in the profile job. Otherwise, the profile job runs all supported evaluations with default settings.

You can exclude all evaluations by adding `NONE` to `IncludedStatistics`.

```
"IncludedStatistics": ["NONE"]                    
```

 In some cases, there might be multiple configurations in `ColumnStatisticsConfigurations` that have different `IncludedStatistics` that you can apply to the same column. In these cases, the profile job picks the last configuration in `ColumnStatisticsConfigurations` and applies its `IncludedStatistics` to the selected column. A new configuration overrides older configurations.

### Configurable statistics at the column level
<a name="statistics.table02"></a>

In `ColumnStatisticsConfigurations`, a profile job supports the evaluations shown in the table following.

A supported data type of `number` in this table means that the attribute's data type is one of the following: `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, or `DoubleType`.


| **Statistic name** | **Description** | **Supported data types** | **Default status** | **Attributes of profile result** | **Type of profile result** | 
| --- | --- | --- | --- | --- | --- | 
| – | Name of the column. | all | – | name | string | 
| – | Data type of the column. | all | – | type | string | 
| DISTINCT\_VALUES\_COUNT | Number of distinct values. A *distinct value* is value that appears at least once. | number/boolean/string | Enabled | distinctValuesCount | Int | 
| ENTROPY | Entropy (information theory). | number/boolean/string | Enabled | entropy | Double | 
| INTER\_QUARTILE\_RANGE | Range between the 25th percent and 75th percent of numbers. | number | Enabled | interquartileRange | Double | 
| KURTOSIS | Kurtosis of the column. | number | Enabled | kurtosis | Double | 
| MAX | Maximum value in the column. | number/string length | Enabled | max | Int/Double | 
| MAXIMUM\_VALUES | List of the maximum values in the column and their counts. | number | Enabled | maximumValues | List | 
| MEAN | Mean value of values in the column. | number/string length | Enabled | mean | Double | 
| MEDIAN | Median of values in the column. | number/string length | Enabled | median | Double | 
| MEDIAN\_ABSOLUTE\_DEVIATION | The median of the absolute differences between each data point and the median of a numeric column. | number | Enabled | medianAbsoluteDeviation | Double | 
| MIN | Minimum value in the column. | number/string length | Enabled | min | Int/Double | 
| MINIMUM\_VALUES | List of the minimum values in the column and their counts. | number | Enabled | minimumValues | List | 
| MISSING\_VALUES\_COUNT | Number of missing values in the column. Null and empty strings are considered as missing. | all | Enabled | missingValuesCount | Int | 
| MODE | The most frequently occurring value in the column. If several values appear that often, the mode is one of those values. | number/string length | Enabled | mode | Int/Double | 
| MOST\_COMMON\_VALUES | List of the most common values in the column. | number/boolean/string | Enabled | mostCommonValues | List | 
| OUTLIER\_DETECTION | Detect outliers in the column by Z\_score algorithm. Count the number of outliers and extract a list of samples from detected outliers. | number/string length | Enabled | zScoreOutliersCount, zScoreOutliersSample | Int/List | 
| PERCENTILES | Percentile values of numeric column (5%, 25%, 75%, 95%). | number | Enabled | percentile5, percentile25, percentile75, percentile95 | Double | 
| RANGE | Range of values in the column. | number | Enabled | range | Int/Double | 
| SKEWNESS | Skewness of values in the column. | number | Enabled | skewness | Double | 
| STANDARD\_DEVIATION | Unbiased sample standard deviation of values in the column. | number/string length | Enabled | standardDeviation | Double | 
| SUM | Sum of values in the column. | number | Enabled | sum | Int/Double | 
| UNIQUE\_VALUES\_COUNT | Number of unique values. A unique value means that the value appears only once. | number/boolean/string | Enabled | uniqueValuesCount | Int | 
| VALUE\_DISTRIBUTION | Measure of the distribution of values in the column by range. | number/string length | Enabled | valueDistribution | List | 
| VARIANCE | Variance of values in the column. | number | Enabled | variance | Double | 
| Z\_SCORE\_DISTRIBUTION | Measure of the distribution of data points' z-score values by range. | number | Enabled | zScoreDistribution | List | 
| ZEROS\_COUNT | Number of zeroes (0s) in the column. | number | Enabled | zerosCount | Int | 

In `IncludedStatistics`, you can override each evaluation's default parameters by adding an override. Each override includes the name of a particular evaluation and a parameter map.

## Parameters for ColumnStatisticsConfigurations columns
<a name="profile-column-parameters"></a>

In `ColumnStatisticsConfigurations`, a profile job supports the following parameters. 

In some cases, there might be multiple configurations in `ColumnStatisticsConfigurations` that have different `IncludedStatistics` that you can apply to the same column. In these cases, the profile job picks the last configuration in `ColumnStatisticsConfigurations` and applies its `IncludedStatistics` to the selected column. A new configuration overrides older configurations.

### MAXIMUM\_VALUES
<a name="profile-column-parameter-MAXIMUM-VALUES"></a>

Lists the maximum values in the numeric column and their counts. The default list size is 5. You can override the list size by specifying a value for `sampleSize`.

**Settings**

`sampleSize` – The size of list that includes the maximum number and count of values in the numeric column. This value should be greater than 0. Use `"ALL"` to list all values. 

**Example**

```
{ 
    "Statistic": "MAXIMUM_VALUES",
    "Parameters": {
        "sampleSize": "5"
    }
}
```

### MINIMUM\_VALUES
<a name="profile-column-parameter-MINIMUM-VALUES"></a>

Lists the minimum values in the numeric column and their counts. The default list size is 5. You can override the list size by specifying a value for `sampleSize`.

**Settings**

`sampleSize` – The size of list that includes the maximum number and count of values in the numeric column. This value should be greater than 0. Use `"ALL"` to list all values. 

**Example**

```
{
    "Statistic": "MINIMUM_VALUES",
    "Parameters": {
        "sampleSize": "5"
    }
}
```

### MOST\_COMMON\_VALUES
<a name="profile-column-parameter-MOST-COMMON-VALUES"></a>

Lists the most common values in the column and their counts. The default list size is 50. You can override the list size by specifying a value for `sampleSize`.

**Settings**

`sampleSize` – The size of list that includes the maximum number and count of values in the numeric column. This value should be greater than 0. Use `"ALL"` to list all values.

**Example**

```
{
    "Statistic": "MOST_COMMON_VALUES",
    "Parameters": {
        "sampleSize": "50"
    }
}
```

### OUTLIER\_DETECTION
<a name="profile-column-parameter-OUTLIER-DETECTION"></a>

Detects outliers in the numeric column or string column (based on string length) by Z\_score algorithm. 

Your profile job counts the number of outliers and generates a sample list of outliers and their z-scores. The sample list is ordered by the z-score's absolute value. The default list size is 50.

The Z\_Score algorithm identifies a value as an outlier when it deviates from the mean by more than the standard deviation threshold. The default outlier threshold is 3.

You can provide one more threshold, a mild threshold, to get more information. Your mild threshold should be less than your threshold. This feature is turned off by default. When a mild threshold is specified, your profile job returns one more count, `zScoreMildOutliersCount`. Also, `zScoreOutliersSample` can include a sample of mild threshold outliers in this case.

**Settings**
+ `threshold` – The threshold value to use when detecting outliers. This value should be greater or equal to 0. 
+ `mildThreshold` – The mild threshold value to use when detecting outliers. This value should be greater or equal to 0 and less than `threshold`.
+ `sampleSize` – The size of list that includes outliers in the column. Use `"ALL"` to list all values.

**Example**

```
{
    "Statistic": "OUTLIER_DETECTION",
    "Parameters": {
        "threshold": "5",
        "mildThreshold": "3.5",
        "sampleSize": "20"
    }
}
```

### VALUE\_DISTRIBUTION
<a name="profile-column-parameter-VALUE-DISTRIBUTION"></a>

Measures the distribution of values in the column by the values' ranges. A profile job groups values from a numeric column or string column (based on string length) into bins by numeric ranges, and generates a list of bins. Bins are consecutive, and the upper bound for a bucket is the lower bound for the next bucket.

**Settings**

` binNumber` – Number of bins. This value should be greater than 0. 

**Example**

```
{
    "Statistic": "VALUE_DISTRIBUTION",
    "Parameters": {
        "binNumber": "5"
    }
}
```

### Z\_SCORE\_DISTRIBUTION
<a name="profile-column-parameter-Z-SCORE-DISTRIBUTION"></a>

Measures the distribution of values’ z-scores in numeric column. A profile job groups z-scores of values into bins by numeric ranges, and generates a list of bins. Bins are consecutive, and the upper bound for a bucket is the lower bound for the next bucket.

**Settings**

` binNumber` – Number of bins. This value should be greater than 0. 

**Example**

```
{
    "Statistic": "Z_SCORE_DISTRIBUTION",
    "Parameters": {
        "binNumber": "5"
    }
}
```

## EntityDetectorConfiguration section for configuring PII
<a name="entity-detector-configuration"></a>

In the `EntityDetectorConfiguration` section of your structure, you can configure the entity types in your dataset that you want DataBrew to detect as **personally identifiable information** (PII) for a profile job.

### EntityTypes
<a name="w2aac19c15c13c23b5"></a>

You configure the entity types you want DataBrew to detect as PII for your profile job. When `EntityDetectorConfiguration` is undefined, entity detection is disabled. The following entity types can be detected in your dataset:
+ USA\_SSN
+ EMAIL
+ USA\_ITIN
+ USA\_PASSPORT\_NUMBER
+ PHONE\_NUMBER
+ USA\_DRIVING\_LICENSE
+ BANK\_ACCOUNT
+ CREDIT\_CARD
+ IP\_ADDRESS
+ MAC\_ADDRESS
+ USA\_DEA\_NUMBER
+ USA\_HCPCS\_CODE
+ USA\_NATIONAL\_PROVIDER\_IDENTIFIER
+ USA\_NATIONAL\_DRUG\_CODE
+ USA\_HEALTH\_INSURANCE\_CLAIM\_NUMBER
+ USA\_MEDICARE\_BENEFICIARY\_IDENTIFIER
+ USA\_CPT\_CODE
+ PERSON\_NAME
+ DATE

The entity type group `USA_ALL` is also supported, and includes all of the above entity types except `PERSON_NAME` and `DATE`.

The type of `EntityTypes` is an array of strings.

### AllowedStatistics
<a name="w2aac19c15c13c23b7"></a>

Configure the statistics that are allowed to be run on columns that contain detected entities. If `AllowedStatistics` is undefined, no statistics will be computed on columns that contain detected entities. See [Configurable statistics at the column level](#statistics.table02) for a list of valid values for the `AllowedStatistics` parameter.

The type of `AllowedStatistics` is an array of `AllowedStatistics` objects.