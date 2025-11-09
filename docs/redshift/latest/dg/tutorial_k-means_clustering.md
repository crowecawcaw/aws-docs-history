Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tutorial: Building K-means clustering

models

In this tutorial, you use Amazon Redshift ML to create, train, and deploy a machine
learning model based on the [K-means
algorithm](url-sm-dev.md "url-sm-dev.md"). This algorithm solves clustering problems where you want to
discover groupings in the data. K-means helps in grouping data that has not been
labeled yet. To learn more about K-means clustering, see [How K-means Clustering Works](../../../sagemaker/latest/dg/algo-kmeans-tech-notes.md "../../../sagemaker/latest/dg/algo-kmeans-tech-notes.md")in the Amazon SageMaker AI Developer Guide.

You will use a CREATE MODEL operation to create a K-means model from a Amazon Redshift
cluster. You can use a CREATE MODEL command to export training data, train a model,
import the model, and prepare an Amazon Redshift prediction function. Use the CREATE MODEL
operation to specify training data either as a table or a SELECT statement.

In this tutorial, you use K-means on the [Global Database of Events,
Language, and Tone (GDELT)](https://aws.amazon.com/public-datasets/gdelt/ "https://aws.amazon.com/public-datasets/gdelt/") dataset, which monitors world news across the
world, and the data is stored for every second of every day. K-means will group
events that have similar tone, actors, or locations. The data is stored as multiple
files on Amazon Simple Storage Service, in two different folders. The folders are historical, which cover
the years 1979–2013, and daily updates, which cover the years 2013 and later. For
this example, we use the historical format and bring in 1979 data.

## Use case examples

You can solve other clustering problems with Amazon Redshift ML, such as grouping customers
who have similar viewing habits on a streaming service. You could also use Redshift ML to predict
the optimal number of shipping centers for a delivery service.

**Tasks**

- Prerequisites
- Step 1: Load the data from Amazon S3 to Amazon Redshift
- Step 2: Create the machine learning model
- Step 3: Perform predictions with the model

## Prerequisites

To complete this tutorial, you must complete the
[Administrative setup](admin-setup.md "admin-setup.md") for Amazon Redshift ML.

## Step 1: Load the data from Amazon S3 to Amazon Redshift

1. Use the [Amazon Redshift query editor v2](../mgmt/query-editor-v2-using.md "../mgmt/query-editor-v2-using.md") to run the following query. The query
   drops the `gdelt_data` table in the public schema if it exists and
   creates a table of the same name in the public schema.

```
DROP TABLE IF EXISTS gdelt_data CASCADE;

CREATE TABLE gdelt_data (
    GlobalEventId bigint,
    SqlDate bigint,
    MonthYear bigint,
    Year bigint,
    FractionDate double precision,
    Actor1Code varchar(256),
    Actor1Name varchar(256),
    Actor1CountryCode varchar(256),
    Actor1KnownGroupCode varchar(256),
    Actor1EthnicCode varchar(256),
    Actor1Religion1Code varchar(256),
    Actor1Religion2Code varchar(256),
    Actor1Type1Code varchar(256),
    Actor1Type2Code varchar(256),
    Actor1Type3Code varchar(256),
    Actor2Code varchar(256),
    Actor2Name varchar(256),
    Actor2CountryCode varchar(256),
    Actor2KnownGroupCode varchar(256),
    Actor2EthnicCode varchar(256),
    Actor2Religion1Code varchar(256),
    Actor2Religion2Code varchar(256),
    Actor2Type1Code varchar(256),
    Actor2Type2Code varchar(256),
    Actor2Type3Code varchar(256),
    IsRootEvent bigint,
    EventCode bigint,
    EventBaseCode bigint,
    EventRootCode bigint,
    QuadClass bigint,
    GoldsteinScale double precision,
    NumMentions bigint,
    NumSources bigint,
    NumArticles bigint,
    AvgTone double precision,
    Actor1Geo_Type bigint,
    Actor1Geo_FullName varchar(256),
    Actor1Geo_CountryCode varchar(256),
    Actor1Geo_ADM1Code varchar(256),
    Actor1Geo_Lat double precision,
    Actor1Geo_Long double precision,
    Actor1Geo_FeatureID bigint,
    Actor2Geo_Type bigint,
    Actor2Geo_FullName varchar(256),
    Actor2Geo_CountryCode varchar(256),
    Actor2Geo_ADM1Code varchar(256),
    Actor2Geo_Lat double precision,
    Actor2Geo_Long double precision,
    Actor2Geo_FeatureID bigint,
    ActionGeo_Type bigint,
    ActionGeo_FullName varchar(256),
    ActionGeo_CountryCode varchar(256),
    ActionGeo_ADM1Code varchar(256),
    ActionGeo_Lat double precision,
    ActionGeo_Long double precision,
    ActionGeo_FeatureID bigint,
    DATEADDED bigint
);
```

2. The following query loads the sample data into the
   `gdelt_data` table.

```
COPY gdelt_data
FROM 's3://gdelt-open-data/events/1979.csv'
REGION 'us-east-1'
IAM_ROLE default
CSV
DELIMITER '\t';
```

### Examine the training data (optional)

To see what data your model will be trained on, use the following
query.

```
SELECT
    AvgTone,
    EventCode,
    NumArticles,
    Actor1Geo_Lat,
    Actor1Geo_Long,
    Actor2Geo_Lat,
    Actor2Geo_Long
FROM
    gdelt_data LIMIT 100;
```

## Step 2: Create the machine learning model

The following example uses the CREATE MODEL command to create a model that
groups the data into seven clusters. The K value is the number of clusters that
your data points are divided into. The model classifies your data points into
clusters where data points are more similar to each other. By clustering the data
points into groups, the K-Means algorithm iteratively determines the best cluster
center. The algorithm then assigns each data point to the closest cluster center.
Members nearest the same cluster center belong to the same group. Members of a
group are as similar as possible to other members in the same group, and as
different as possible from members of other groups. The K value is subjective and
depends on methods that measure the similarities among data points. You can change
the K value to smooth out cluster sizes if the clusters are unevenly
distributed.

In the following example, replace amzn-s3-demo-bucket with your own
Amazon S3 bucket.

```
CREATE MODEL news_data_clusters
FROM
    (
        SELECT
            AvgTone,
            EventCode,
            NumArticles,
            Actor1Geo_Lat,
            Actor1Geo_Long,
            Actor2Geo_Lat,
            Actor2Geo_Long
        FROM
            gdelt_data
    ) FUNCTION news_monitoring_cluster
    IAM_ROLE default
    AUTO OFF
    MODEL_TYPE KMEANS
    PREPROCESSORS 'none'
    HYPERPARAMETERS DEFAULT
    EXCEPT
    (K '7')
    SETTINGS (S3_BUCKET 'amzn-s3-demo-bucket');
```

### Check the status of model training (optional)

You can use the SHOW MODEL command to know when your model is ready.

To check the model status, use the following SHOW MODEL operation and find
if the `Model State` is `Ready`.

```
SHOW MODEL NEWS_DATA_CLUSTERS;
```

When the model is ready, the output of the previous operation should show
that the `Model State` is `Ready`. The following is an
example of the output of the SHOW MODEL operation.

```
+--------------------------+------------------------------------------------------------------------------------------------------+
|        Model Name        |                                          news_data_clusters                                          |
+--------------------------+------------------------------------------------------------------------------------------------------+
|       Schema Name        |                                                public                                                |
|          Owner           |                                               awsuser                                                |
|      Creation Time       |                                       Fri, 17.06.2022 16:32:19                                       |
|       Model State        |                                                READY                                                 |
|        train:msd         |                                             2973.822754                                              |
|      train:progress      |                                              100.000000                                              |
|     train:throughput     |                                            237114.875000                                             |
|      Estimated Cost      |                                               0.004983                                               |
|                          |                                                                                                      |
|      TRAINING DATA:      |                                                                                                      |
|          Query           | SELECT AVGTONE, EVENTCODE, NUMARTICLES, ACTOR1GEO_LAT, ACTOR1GEO_LONG, ACTOR2GEO_LAT, ACTOR2GEO_LONG |
|                          |                                           FROM GDELT_DATA                                            |
|                          |                                                                                                      |
|       PARAMETERS:        |                                                                                                      |
|        Model Type        |                                                kmeans                                                |
|    Training Job Name     |                                redshiftml-20220617163219978978-kmeans                                |
|      Function Name       |                                       news_monitoring_cluster                                        |
|   Function Parameters    |       avgtone eventcode numarticles actor1geo_lat actor1geo_long actor2geo_lat actor2geo_long        |
| Function Parameter Types |                             float8 int8 int8 float8 float8 float8 float8                             |
|         IAM Role         |                                         default-aws-iam-role                                         |
|        S3 Bucket         |                                            amzn-s3-demo-bucket                                       |
|       Max Runtime        |                                                 5400                                                 |
|                          |                                                                                                      |
|     HYPERPARAMETERS:     |                                                                                                      |
|       feature_dim        |                                                  7                                                   |
|            k             |                                                  7                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------+
```

## Step 3: Perform predictions with the model

### Identify the clusters

You can find discrete groupings identified in the data by your model,
otherwise known as clusters. A cluster is the set of data points that is closer
to its cluster center than any other cluster center. Since the K value
represents the number of clusters in the model, it also represents the number
of cluster centers. The following query identifies the clusters by showing the
cluster associated with each `globaleventid`.

```
SELECT
    globaleventid,
    news_monitoring_cluster (
        AvgTone,
        EventCode,
        NumArticles,
        Actor1Geo_Lat,
        Actor1Geo_Long,
        Actor2Geo_Lat,
        Actor2Geo_Long
    ) AS cluster
FROM
    gdelt_data;
```

### Check the distribution of data

You can check the distribution of data across clusters to see if the K value
that you chose caused the data to be somewhat evenly distributed. Use the
following query to determine if the data is evenly distributed across your
clusters.

```
SELECT
    events_cluster,
    COUNT(*) AS nbr_events
FROM
    (
        SELECT
            globaleventid,
            news_monitoring_cluster(
                AvgTone,
                EventCode,
                NumArticles,
                Actor1Geo_Lat,
                Actor1Geo_Long,
                Actor2Geo_Lat,
                Actor2Geo_Long
            ) AS events_cluster
        FROM
            gdelt_data
    )
GROUP BY
    1;
```

Note that you can change the K value to smooth out cluster sizes if the
clusters are unevenly distributed.

### Determine the cluster centers

A data point is closer to its cluster center than it is to any other cluster
center. Thus, finding the cluster centers helps you define the clusters.

Run the following query to determine the centers of the clusters based on
the number of articles by event code.

```
SELECT
    news_monitoring_cluster (
        AvgTone,
        EventCode,
        NumArticles,
        Actor1Geo_Lat,
        Actor1Geo_Long,
        Actor2Geo_Lat,
        Actor2Geo_Long
    ) AS events_cluster,
    eventcode,
    SUM(numArticles) AS numArticles
FROM
    gdelt_data
GROUP BY
    1,
    2;
```

### Show information about data points in a cluster

Use the following query to return the data for the points assigned to the
fifth cluster. The selected articles must have two actors.

```
SELECT
    news_monitoring_cluster (
        AvgTone,
        EventCode,
        NumArticles,
        Actor1Geo_Lat,
        Actor1Geo_Long,
        Actor2Geo_Lat,
        Actor2Geo_Long
    ) AS events_cluster,
    eventcode,
    actor1name,
    actor2name,
    SUM(numarticles) AS totalarticles
FROM
    gdelt_data
WHERE
    events_cluster = 5
    AND actor1name <> ' '
    AND actor2name <> ' '
GROUP BY
    1,
    2,
    3,
    4
ORDER BY
    5 desc;
```

### Show data about events with actors of the same ethnic code

The following query counts the number of articles written about events with
a positive tone. The query also requires that the two actors have the same
ethnic code and it returns which cluster each event is assigned to.

```
SELECT
    news_monitoring_cluster (
        AvgTone,
        EventCode,
        NumArticles,
        Actor1Geo_Lat,
        Actor1Geo_Long,
        Actor2Geo_Lat,
        Actor2Geo_Long
    ) AS events_cluster,
    SUM(numarticles) AS total_articles,
    eventcode AS event_code,
    Actor1EthnicCode AS ethnic_code
FROM
    gdelt_data
WHERE
    Actor1EthnicCode = Actor2EthnicCode
    AND Actor1EthnicCode <> ' '
    AND Actor2EthnicCode <> ' '
    AND AvgTone > 0
GROUP BY
    1,
    3,
    4
HAVING
    (total_articles) > 4
ORDER BY
    1,
    2 ASC;
```

## Related topics

For more information about Amazon Redshift ML, see the following documentation:

- [Costs for using Amazon Redshift ML](cost.md "cost.md")
- [CREATE MODEL operation](r_CREATE_MODEL.md "r_CREATE_MODEL.md")
- [EXPLAIN_MODEL function](r_explain_model_function.md "r_explain_model_function.md")

For more information about machine learning, see the following documentation:

- [Machine learning overview](machine_learning_overview.md "machine_learning_overview.md")
- [Machine learning for novices and experts](novice_expert.md "novice_expert.md")
- [What Is Fairness and Model Explainability for Machine Learning
  Predictions?](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md")
