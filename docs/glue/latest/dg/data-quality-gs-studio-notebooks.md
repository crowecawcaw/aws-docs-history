# Data Quality for ETL jobs in AWS Glue Studio notebooks

In
this tutorial, you learn how to use AWS Glue Data Quality for extract,
transform, and load (ETL) jobs in AWS Glue Studio notebooks.

You
can
use
notebooks in
AWS Glue Studio
to
edit job scripts and view the output without having to run a full job. You can also add
markdown and save notebooks as `.ipynb` files and job scripts.
Note
that
you can start a notebook without installing software locally or managing
servers. When
you're
satisfied with your code,
you can use
AWS Glue Studio
to
easily
convert your notebook to an
AWS Glue
job.

The dataset
that
you
use
in this example consists of Medicare Provider payment data that was downloaded from two
_Data.CMS.gov_
datasets:
"Inpatient Prospective Payment System Provider Summary for the Top 100 Diagnosis-Related
Groups - FY2011" and "Inpatient Charge Data FY 2011".

After downloading the data, we modified the dataset to introduce a
couple of erroneous records at the end of the file. This modified file is located in a
public Amazon S3 bucket at
`s3://awsglue-datasets/examples/medicare/Medicare_Hospital_Provider.csv`.

## Prerequisites

- AWS Glue role with Amazon S3 permission to write to your destination Amazon S3
  bucket
- A new
  notebook
  (see
  [Getting started with
  notebooks in
  AWS Glue Studio](../ug/notebook-getting-started.md "../ug/notebook-getting-started.md"))

## Creating an ETL job in

AWS Glue Studio

###### To

create an ETL
job

1. Change the session version to AWS Glue 3.0.

To do this, remove all boilerplate code cells
with
the following magic and run the cell.
Note that
this boilerplate code is automatically provided in the first cell when a new
notebook is created.

```
%glue_version 3.0
```

2. Copy the
   following
   code and run it in the cell.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

```

3. In the next cell, import the `EvaluateDataQuality`
   class
   that
   evaluatesAWS Glue
   Data
   Quality.

```
from awsgluedq.transforms import EvaluateDataQuality
```

4. In
   the next cell, read in the source data
   by
   using the .csv file
   that's
   stored in the public Amazon S3 bucket.

```
medicare = spark.read.format(
"csv").option(
"header", "true").option(
"inferSchema", "true").load(
's3://awsglue-datasets/examples/medicare/Medicare_Hospital_Provider.csv')
medicare.printSchema()

```

5. Convert the data to
   an
   AWS Glue
   DynamicFrame.

```
from awsglue.dynamicframe import DynamicFrame
medicare_dyf = DynamicFrame.fromDF(medicare,glueContext,"medicare_dyf")

```

6. Create the ruleset using
   Data
   Quality Definition Language
   (DQDL).

```
EvaluateDataQuality_ruleset = """
    Rules = [
        ColumnExists "Provider Id",
        IsComplete "Provider Id",
        ColumnValues  " Total Discharges " > 15
]
    ]
"""

```

7. Validate the dataset against the
   ruleset.

```
EvaluateDataQualityMultiframe = EvaluateDataQuality().process_rows(
    frame=medicare_dyf,
    ruleset=EvaluateDataQuality_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQualityMultiframe",
        "enableDataQualityCloudWatchMetrics": False,
        "enableDataQualityResultsPublishing": False,
    },
    additional_options={"performanceTuning.caching": "CACHE_NOTHING"},
)

```

8. Review the
   results.

```
ruleOutcomes = SelectFromCollection.apply(
    dfc=EvaluateDataQualityMultiframe,
    key="ruleOutcomes",
    transformation_ctx="ruleOutcomes",
)

ruleOutcomes.toDF().show(truncate=False)

```

Output:

````
--------------------------------------+-------+-----------------------------------------------------+-------------------------------------------+
|Rule                                  |Outcome|FailureReason                                        |EvaluatedMetrics                           | +--------------------------------------+-------+-----------------------------------------------------+-------------------------------------------+
|ColumnExists "Provider Id"            |Passed |null                                                 |{}                                         |
|IsComplete "Provider Id"              |Passed |null                                                 |{Column.Provider Id.Completeness -> 1.0}   |
|ColumnValues " Total Discharges " > 15|Failed |Value: 11.0 does not meet the constraint requirement!|{Column. Total Discharges .Minimum -> 11.0}| +--------------------------------------+-------+-----------------------------------------------------+-------------------------------------------+ ``` 9. Filter passed rows and review the failed rows from the Data Quality row-level results. ``` owLevelOutcomes = SelectFromCollection.apply( dfc=EvaluateDataQualityMultiframe, key="rowLevelOutcomes", transformation_ctx="rowLevelOutcomes", ) rowLevelOutcomes_df = rowLevelOutcomes.toDF() # Convert Glue DynamicFrame to SparkSQL DataFrame rowLevelOutcomes_df_passed = rowLevelOutcomes_df.filter(rowLevelOutcomes_df.DataQualityEvaluationResult == "Passed") # Filter only the Passed records. rowLevelOutcomes_df.filter(rowLevelOutcomes_df.DataQualityEvaluationResult == "Failed").show(5, truncate=False) # Review the Failed records ``` Output: ``` +----------------------------------------+-----------+-------------------------------------+--------------------------+-------------+--------------+-----------------+------------------------------------+------------------+-------------------------+------------------------+-------------------------+--------------------------+----------------------------------------+----------------------------+---------------------------+
|DRG Definition                          |Provider Id|Provider Name                        |Provider Street Address   |Provider City|Provider State|Provider Zip Code|Hospital Referral Region Description| Total Discharges | Average Covered Charges | Average Total Payments |Average Medicare Payments|DataQualityRulesPass      |DataQualityRulesFail                    |DataQualityRulesSkip        |DataQualityEvaluationResult| +----------------------------------------+-----------+-------------------------------------+--------------------------+-------------+--------------+-----------------+------------------------------------+------------------+-------------------------+------------------------+-------------------------+--------------------------+----------------------------------------+----------------------------+---------------------------+
|039 - EXTRACRANIAL PROCEDURES W/O CC/MCC|10005      |MARSHALL MEDICAL CENTER SOUTH        |2505 U S HIGHWAY 431 NORTH|BOAZ         |AL            |35957            |AL - Birmingham                     |14                |$15131.85                |$5787.57                |$4976.71                 |[IsComplete "Provider Id"]|[ColumnValues " Total Discharges " > 15]|[ColumnExists "Provider Id"]|Failed                     |
|039 - EXTRACRANIAL PROCEDURES W/O CC/MCC|10046      |RIVERVIEW REGIONAL MEDICAL CENTER    |600 SOUTH THIRD STREET    |GADSDEN      |AL            |35901            |AL - Birmingham                     |14                |$67327.92                |$5461.57                |$4493.57                 |[IsComplete "Provider Id"]|[ColumnValues " Total Discharges " > 15]|[ColumnExists "Provider Id"]|Failed                     |
|039 - EXTRACRANIAL PROCEDURES W/O CC/MCC|10083      |SOUTH BALDWIN REGIONAL MEDICAL CENTER|1613 NORTH MCKENZIE STREET|FOLEY        |AL            |36535            |AL - Mobile                         |15                |$25411.33                |$5282.93                |$4383.73                 |[IsComplete "Provider Id"]|[ColumnValues " Total Discharges " > 15]|[ColumnExists "Provider Id"]|Failed                     |
|039 - EXTRACRANIAL PROCEDURES W/O CC/MCC|30002      |BANNER GOOD SAMARITAN MEDICAL CENTER |1111 EAST MCDOWELL ROAD   |PHOENIX      |AZ            |85006            |AZ - Phoenix                        |11                |$34803.81                |$7768.90                |$6951.45                 |[IsComplete "Provider Id"]|[ColumnValues " Total Discharges " > 15]|[ColumnExists "Provider Id"]|Failed                     |
|039 - EXTRACRANIAL PROCEDURES W/O CC/MCC|30010      |CARONDELET ST  MARYS HOSPITAL        |1601 WEST ST MARY'S ROAD  |TUCSON       |AZ            |85745            |AZ - Tucson                         |12                |$35968.50                |$6506.50                |$5379.83                 |[IsComplete "Provider Id"]|[ColumnValues " Total Discharges " > 15]|[ColumnExists "Provider Id"]|Failed                     | +----------------------------------------+-----------+-------------------------------------+--------------------------+-------------+--------------+-----------------+------------------------------------+------------------+-------------------------+------------------------+-------------------------+--------------------------+----------------------------------------+----------------------------+---------------------------+ only showing top 5 rows ``` Note that AWS Glue Data Quality added four new columns (DataQualityRulesPass, DataQualityRulesFail, DataQualityRulesSkip, and DataQualityEvaluationResult). This indicates the records that passed, the records that failed, rules skipped for row-level evaluation, and the overall row-level results. 10. Write the output to an Amazon S3 bucket to analyze the data and visualize the results. ``` #Write the Passed records to the destination. glueContext.write_dynamic_frame.from_options( frame = rowLevelOutcomes_df_passed, connection_type = "s3", connection_options = {"path": "s3://glue-sample-target/output-dir/medicare_parquet"}, format = "parquet") ```
````
