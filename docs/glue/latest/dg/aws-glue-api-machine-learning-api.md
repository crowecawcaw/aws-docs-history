# Machine learning API

The Machine learning API describes the machine learning data types, and
includes the API for creating, deleting, or updating a transform, or starting
a machine learning task run.

## Data types

- [TransformParameters structure](#aws-glue-api-machine-learning-api-TransformParameters "#aws-glue-api-machine-learning-api-TransformParameters")
- [EvaluationMetrics structure](#aws-glue-api-machine-learning-api-EvaluationMetrics "#aws-glue-api-machine-learning-api-EvaluationMetrics")
- [MLTransform structure](#aws-glue-api-machine-learning-api-MLTransform "#aws-glue-api-machine-learning-api-MLTransform")
- [FindMatchesParameters structure](#aws-glue-api-machine-learning-api-FindMatchesParameters "#aws-glue-api-machine-learning-api-FindMatchesParameters")
- [FindMatchesMetrics structure](#aws-glue-api-machine-learning-api-FindMatchesMetrics "#aws-glue-api-machine-learning-api-FindMatchesMetrics")
- [ConfusionMatrix structure](#aws-glue-api-machine-learning-api-ConfusionMatrix "#aws-glue-api-machine-learning-api-ConfusionMatrix")
- [GlueTable structure](#aws-glue-api-machine-learning-api-GlueTable "#aws-glue-api-machine-learning-api-GlueTable")
- [TaskRun structure](#aws-glue-api-machine-learning-api-TaskRun "#aws-glue-api-machine-learning-api-TaskRun")
- [TransformFilterCriteria structure](#aws-glue-api-machine-learning-api-TransformFilterCriteria "#aws-glue-api-machine-learning-api-TransformFilterCriteria")
- [TransformSortCriteria structure](#aws-glue-api-machine-learning-api-TransformSortCriteria "#aws-glue-api-machine-learning-api-TransformSortCriteria")
- [TaskRunFilterCriteria structure](#aws-glue-api-machine-learning-api-TaskRunFilterCriteria "#aws-glue-api-machine-learning-api-TaskRunFilterCriteria")
- [TaskRunSortCriteria structure](#aws-glue-api-machine-learning-api-TaskRunSortCriteria "#aws-glue-api-machine-learning-api-TaskRunSortCriteria")
- [TaskRunProperties structure](#aws-glue-api-machine-learning-api-TaskRunProperties "#aws-glue-api-machine-learning-api-TaskRunProperties")
- [FindMatchesTaskRunProperties structure](#aws-glue-api-machine-learning-api-FindMatchesTaskRunProperties "#aws-glue-api-machine-learning-api-FindMatchesTaskRunProperties")
- [ImportLabelsTaskRunProperties structure](#aws-glue-api-machine-learning-api-ImportLabelsTaskRunProperties "#aws-glue-api-machine-learning-api-ImportLabelsTaskRunProperties")
- [ExportLabelsTaskRunProperties structure](#aws-glue-api-machine-learning-api-ExportLabelsTaskRunProperties "#aws-glue-api-machine-learning-api-ExportLabelsTaskRunProperties")
- [LabelingSetGenerationTaskRunProperties structure](#aws-glue-api-machine-learning-api-LabelingSetGenerationTaskRunProperties "#aws-glue-api-machine-learning-api-LabelingSetGenerationTaskRunProperties")
- [SchemaColumn structure](#aws-glue-api-machine-learning-api-SchemaColumn "#aws-glue-api-machine-learning-api-SchemaColumn")
- [TransformEncryption structure](#aws-glue-api-machine-learning-api-TransformEncryption "#aws-glue-api-machine-learning-api-TransformEncryption")
- [MLUserDataEncryption structure](#aws-glue-api-machine-learning-api-MLUserDataEncryption "#aws-glue-api-machine-learning-api-MLUserDataEncryption")
- [ColumnImportance structure](#aws-glue-api-machine-learning-api-ColumnImportance "#aws-glue-api-machine-learning-api-ColumnImportance")

## TransformParameters structure

The algorithm-specific parameters that are associated with the machine
learning transform.

###### Fields

- `TransformType` – _Required:_ UTF-8 string (valid values: `FIND_MATCHES`).

The type of machine learning transform.

For information about the types of machine learning transforms, see [Creating
Machine Learning Transforms](add-job-machine-learning-transform.md "add-job-machine-learning-transform.md").

- `FindMatchesParameters` – A [FindMatchesParameters](#aws-glue-api-machine-learning-api-FindMatchesParameters "#aws-glue-api-machine-learning-api-FindMatchesParameters") object.

The parameters for the find matches algorithm.

## EvaluationMetrics structure

Evaluation metrics provide an estimate of the quality of your machine
learning transform.

###### Fields

- `TransformType` – _Required:_ UTF-8 string (valid values: `FIND_MATCHES`).

The type of machine learning transform.

- `FindMatchesMetrics` – A [FindMatchesMetrics](#aws-glue-api-machine-learning-api-FindMatchesMetrics "#aws-glue-api-machine-learning-api-FindMatchesMetrics") object.

The evaluation metrics for the find matches algorithm.

## MLTransform structure

A structure for a machine learning transform.

###### Fields

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique transform ID that is generated for the machine learning transform.
The ID is guaranteed to be unique and does not change.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A user-defined name for the machine learning transform. Names are not
guaranteed unique and can be changed at any time.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A user-defined, long-form description text for the machine learning
transform. Descriptions are not guaranteed to be unique and can be changed at
any time.

- `Status` – UTF-8 string (valid values: `NOT_READY` | `READY` | `DELETING`).

The current status of the machine learning transform.

- `CreatedOn` – Timestamp.

A timestamp. The time and date that this machine learning transform was
created.

- `LastModifiedOn` – Timestamp.

A timestamp. The last point in time when this machine learning transform
was modified.

- `InputRecordTables` – An array of [GlueTable](#aws-glue-api-machine-learning-api-GlueTable "#aws-glue-api-machine-learning-api-GlueTable") objects, not more than 10 structures.

A list of AWS Glue table definitions used by the transform.

- `Parameters` – A [TransformParameters](#aws-glue-api-machine-learning-api-TransformParameters "#aws-glue-api-machine-learning-api-TransformParameters") object.

A `TransformParameters` object. You can use parameters
to tune (customize) the behavior of the machine learning transform by specifying
what data it learns from and your preference on various tradeoffs (such as precious
vs. recall, or accuracy vs. cost).

- `EvaluationMetrics` – An [EvaluationMetrics](#aws-glue-api-machine-learning-api-EvaluationMetrics "#aws-glue-api-machine-learning-api-EvaluationMetrics") object.

An `EvaluationMetrics` object. Evaluation metrics provide
an estimate of the quality of your machine learning transform.

- `LabelCount` – Number (integer).

A count identifier for the labeling files generated by AWS Glue for this transform. As you create a better transform, you can iteratively download,
label, and upload the labeling file.

- `Schema` – An array of [SchemaColumn](#aws-glue-api-machine-learning-api-SchemaColumn "#aws-glue-api-machine-learning-api-SchemaColumn") objects, not more than 100 structures.

A map of key-value pairs representing the columns and data types that this
transform can run against. Has an upper bound of 100 columns.

- `Role` – UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role with the required
permissions. The required permissions include both AWS Glue service
role permissions to AWS Glue resources, and Amazon S3 permissions
required by the transform.

    + This role needs AWS Glue service role permissions to allow
     access to resources in AWS Glue. See [Attach a Policy to IAM
     Users That Access AWS Glue](attach-policy-iam-user.md "attach-policy-iam-user.md").
    + This role needs permission to your Amazon Simple Storage Service (Amazon
     S3) sources, targets, temporary directory, scripts, and any libraries used
     by the task run for this transform.

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

This value determines which version of AWS Glue this machine
learning transform is compatible with. Glue 1.0 is recommended for most customers.
If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information,
see [AWS Glue Versions](release-notes.md#release-notes-versions "release-notes.md#release-notes-versions") in the developer guide.

- `MaxCapacity` – Number (double).

The number of AWS Glue data processing units (DPUs) that are
allocated to task runs for this transform. You can allocate from 2 to 100 DPUs;
the default is 10. A DPU is a relative measure of processing power that consists
of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
[AWS Glue pricing
page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

`MaxCapacity` is a mutually exclusive option with `NumberOfWorkers`
and `WorkerType`.

    + If either `NumberOfWorkers` or `WorkerType`
     is set, then `MaxCapacity` cannot be set.
    + If `MaxCapacity` is set then neither `NumberOfWorkers`
     or `WorkerType` can be set.
    + If `WorkerType` is set, then `NumberOfWorkers`
     is required (and vice versa).
    + `MaxCapacity` and `NumberOfWorkers` must
     both be at least 1.

When the `WorkerType` field is set to a value other than `Standard`,
the `MaxCapacity` field is set automatically and becomes read-only.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when a task of this transform
runs. Accepts a value of Standard, G.1X, or G.2X.

    + For the `Standard` worker type, each worker provides 4 vCPU,
     16 GB of memory and a 50GB disk, and 2 executors per worker.
    + For the `G.1X` worker type, each worker provides 4 vCPU, 16
     GB of memory and a 64GB disk, and 1 executor per worker.
    + For the `G.2X` worker type, each worker provides 8 vCPU, 32
     GB of memory and a 128GB disk, and 1 executor per worker.

`MaxCapacity` is a mutually exclusive option with `NumberOfWorkers`
and `WorkerType`.

    + If either `NumberOfWorkers` or `WorkerType`
     is set, then `MaxCapacity` cannot be set.
    + If `MaxCapacity` is set then neither `NumberOfWorkers`
     or `WorkerType` can be set.
    + If `WorkerType` is set, then `NumberOfWorkers`
     is required (and vice versa).
    + `MaxCapacity` and `NumberOfWorkers` must
     both be at least 1.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when a task of the transform runs.

If `WorkerType` is set, then `NumberOfWorkers`
is required (and vice versa).

- `Timeout` – Number (integer), at least 1.

The timeout in minutes of the machine learning transform.

- `MaxRetries` – Number (integer).

The maximum number of times to retry after an `MLTaskRun`
of the machine learning transform fails.

- `TransformEncryption` – A [TransformEncryption](#aws-glue-api-machine-learning-api-TransformEncryption "#aws-glue-api-machine-learning-api-TransformEncryption") object.

The encryption-at-rest settings of the transform that apply to accessing
user data. Machine learning transforms can access user data encrypted in Amazon
S3 using KMS.

## FindMatchesParameters structure

The parameters to configure the find matches transform.

###### Fields

- `PrimaryKeyColumnName` – UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of a column that uniquely identifies rows in the source table.
Used to help identify matching records.

- `PrecisionRecallTradeoff` – Number (double), not more than 1.0.

The value selected when tuning your transform for a balance between precision
and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely
for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff,
choosing values close to 1.0 means very low recall, and choosing values close
to 0.0 results in very low precision.

The precision metric indicates how often your model is correct when it
predicts a match.

The recall metric indicates that for an actual match, how often your model
predicts the match.

- `AccuracyCostTradeoff` – Number (double), not more than 1.0.

The value that is selected when tuning your transform for a balance between
accuracy and cost. A value of 0.5 means that the system balances accuracy and cost
concerns. A value of 1.0 means a bias purely for accuracy, which typically results
in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely
for cost, which results in a less accurate `FindMatches` transform,
sometimes with unacceptable accuracy.

Accuracy measures how well the transform finds true positives and true
negatives. Increasing accuracy requires more machine resources and cost. But
it also results in increased recall.

Cost measures how many compute resources, and thus money, are consumed
to run the transform.

- `EnforceProvidedLabels` – Boolean.

The value to switch on or off to force the output to match the provided labels
from users. If the value is `True`, the `find matches`
transform forces the output to match the provided labels. The results override
the normal conflation results. If the value is `False`, the `find
 matches` transform does not ensure all the labels provided are respected,
and the results rely on the trained model.

Note that setting this value to true may increase the conflation execution
time.

## FindMatchesMetrics structure

The evaluation metrics for the find matches algorithm. The quality of
your machine learning transform is measured by getting your transform to predict
some matches and comparing the results to known matches from the same dataset.
The quality metrics are based on a subset of your data, so they are not precise.

###### Fields

- `AreaUnderPRCurve` – Number (double), not more than 1.0.

The area under the precision/recall curve (AUPRC) is a single number measuring
the overall quality of the transform, that is independent of the choice made for
precision vs. recall. Higher values indicate that you have a more attractive
precision vs. recall tradeoff.

For more information, see [Precision
and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall") in Wikipedia.

- `Precision` – Number (double), not more than 1.0.

The precision metric indicates when often your transform is correct when
it predicts a match. Specifically, it measures how well the transform finds true
positives from the total true positives possible.

For more information, see [Precision
and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall") in Wikipedia.

- `Recall` – Number (double), not more than 1.0.

The recall metric indicates that for an actual match, how often your transform
predicts the match. Specifically, it measures how well the transform finds true
positives from the total records in the source data.

For more information, see [Precision
and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall") in Wikipedia.

- `F1` – Number (double), not more than 1.0.

The maximum F1 metric indicates the transform's accuracy between 0 and
1, where 1 is the best accuracy.

For more information, see [F1
score](https://en.wikipedia.org/wiki/F1_score "https://en.wikipedia.org/wiki/F1_score") in Wikipedia.

- `ConfusionMatrix` – A [ConfusionMatrix](#aws-glue-api-machine-learning-api-ConfusionMatrix "#aws-glue-api-machine-learning-api-ConfusionMatrix") object.

The confusion matrix shows you what your transform is predicting accurately
and what types of errors it is making.

For more information, see [Confusion
matrix](https://en.wikipedia.org/wiki/Confusion_matrix "https://en.wikipedia.org/wiki/Confusion_matrix") in Wikipedia.

- `ColumnImportances` – An array of [ColumnImportance](#aws-glue-api-machine-learning-api-ColumnImportance "#aws-glue-api-machine-learning-api-ColumnImportance") objects, not more than 100 structures.

A list of `ColumnImportance` structures containing column
importance metrics, sorted in order of descending importance.

## ConfusionMatrix structure

The confusion matrix shows you what your transform is predicting accurately
and what types of errors it is making.

For more information, see [Confusion
matrix](https://en.wikipedia.org/wiki/Confusion_matrix "https://en.wikipedia.org/wiki/Confusion_matrix") in Wikipedia.

###### Fields

- `NumTruePositives` – Number (long).

The number of matches in the data that the transform correctly found, in
the confusion matrix for your transform.

- `NumFalsePositives` – Number (long).

The number of nonmatches in the data that the transform incorrectly classified
as a match, in the confusion matrix for your transform.

- `NumTrueNegatives` – Number (long).

The number of nonmatches in the data that the transform correctly rejected,
in the confusion matrix for your transform.

- `NumFalseNegatives` – Number (long).

The number of matches in the data that the transform didn't find, in the
confusion matrix for your transform.

## GlueTable structure

The database and table in the AWS Glue Data Catalog that is used for
input or output data.

###### Fields

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A database name in the AWS Glue Data Catalog.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A table name in the AWS Glue Data Catalog.

- `CatalogId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the AWS Glue Data Catalog.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to the AWS Glue Data Catalog.

- `AdditionalOptions` – A map array of key-value pairs, not less than 1 or more than 10 pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Additional options for the table. Currently there are two keys supported:

    + `pushDownPredicate`: to filter on partitions without having
     to list and read all the files in your dataset.
    + `catalogPartitionPredicate`: to use server-side partition
     pruning using partition indexes in the AWS Glue Data Catalog.

## TaskRun structure

The sampling parameters that are associated with the machine learning
transform.

###### Fields

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the transform.

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for this task run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The current status of the requested task run.

- `LogGroupName` – UTF-8 string.

The names of the log group for secure logging, associated with this task
run.

- `Properties` – A [TaskRunProperties](#aws-glue-api-machine-learning-api-TaskRunProperties "#aws-glue-api-machine-learning-api-TaskRunProperties") object.

Specifies configuration properties associated with this task run.

- `ErrorString` – UTF-8 string.

The list of error strings associated with this task run.

- `StartedOn` – Timestamp.

The date and time that this task run started.

- `LastModifiedOn` – Timestamp.

The last point in time that the requested task run was updated.

- `CompletedOn` – Timestamp.

The last point in time that the requested task run was completed.

- `ExecutionTime` – Number (integer).

The amount of time (in seconds) that the task run consumed resources.

## TransformFilterCriteria structure

The criteria used to filter the machine learning transforms.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique transform name that is used to filter the machine learning transforms.

- `TransformType` – UTF-8 string (valid values: `FIND_MATCHES`).

The type of machine learning transform that is used to filter the machine
learning transforms.

- `Status` – UTF-8 string (valid values: `NOT_READY` | `READY` | `DELETING`).

Filters the list of machine learning transforms by the last known status
of the transforms (to indicate whether a transform can be used or not). One of "NOT_READY",
"READY", or "DELETING".

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

This value determines which version of AWS Glue this machine
learning transform is compatible with. Glue 1.0 is recommended for most customers.
If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information,
see [AWS Glue Versions](release-notes.md#release-notes-versions "release-notes.md#release-notes-versions") in the developer guide.

- `CreatedBefore` – Timestamp.

The time and date before which the transforms were created.

- `CreatedAfter` – Timestamp.

The time and date after which the transforms were created.

- `LastModifiedBefore` – Timestamp.

Filter on transforms last modified before this date.

- `LastModifiedAfter` – Timestamp.

Filter on transforms last modified after this date.

- `Schema` – An array of [SchemaColumn](#aws-glue-api-machine-learning-api-SchemaColumn "#aws-glue-api-machine-learning-api-SchemaColumn") objects, not more than 100 structures.

Filters on datasets with a specific schema. The `Map<Column,
 Type>` object is an array of key-value pairs representing the schema
this transform accepts, where `Column` is the name of a column, and
`Type` is the type of the data such as an integer or string. Has an upper
bound of 100 columns.

## TransformSortCriteria structure

The sorting criteria that are associated with the machine learning transform.

###### Fields

- `Column` – _Required:_ UTF-8 string (valid values: `NAME` | `TRANSFORM_TYPE` | `STATUS` | `CREATED` | `LAST_MODIFIED`).

The column to be used in the sorting criteria that are associated with the
machine learning transform.

- `SortDirection` – _Required:_ UTF-8 string (valid values: `DESCENDING` | `ASCENDING`).

The sort direction to be used in the sorting criteria that are associated
with the machine learning transform.

## TaskRunFilterCriteria structure

The criteria that are used to filter the task runs for the machine learning
transform.

###### Fields

- `TaskRunType` – UTF-8 string (valid values: `EVALUATION` | `LABELING_SET_GENERATION` | `IMPORT_LABELS` | `EXPORT_LABELS` | `FIND_MATCHES`).

The type of task run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The current status of the task run.

- `StartedBefore` – Timestamp.

Filter on task runs started before this date.

- `StartedAfter` – Timestamp.

Filter on task runs started after this date.

## TaskRunSortCriteria structure

The sorting criteria that are used to sort the list of task runs for the machine
learning transform.

###### Fields

- `Column` – _Required:_ UTF-8 string (valid values: `TASK_RUN_TYPE` | `STATUS` | `STARTED`).

The column to be used to sort the list of task runs for the machine learning
transform.

- `SortDirection` – _Required:_ UTF-8 string (valid values: `DESCENDING` | `ASCENDING`).

The sort direction to be used to sort the list of task runs for the machine
learning transform.

## TaskRunProperties structure

The configuration properties for the task run.

###### Fields

- `TaskType` – UTF-8 string (valid values: `EVALUATION` | `LABELING_SET_GENERATION` | `IMPORT_LABELS` | `EXPORT_LABELS` | `FIND_MATCHES`).

The type of task run.

- `ImportLabelsTaskRunProperties` – An [ImportLabelsTaskRunProperties](#aws-glue-api-machine-learning-api-ImportLabelsTaskRunProperties "#aws-glue-api-machine-learning-api-ImportLabelsTaskRunProperties") object.

The configuration properties for an importing labels task run.

- `ExportLabelsTaskRunProperties` – An [ExportLabelsTaskRunProperties](#aws-glue-api-machine-learning-api-ExportLabelsTaskRunProperties "#aws-glue-api-machine-learning-api-ExportLabelsTaskRunProperties") object.

The configuration properties for an exporting labels task run.

- `LabelingSetGenerationTaskRunProperties` – A [LabelingSetGenerationTaskRunProperties](#aws-glue-api-machine-learning-api-LabelingSetGenerationTaskRunProperties "#aws-glue-api-machine-learning-api-LabelingSetGenerationTaskRunProperties") object.

The configuration properties for a labeling set generation task run.

- `FindMatchesTaskRunProperties` – A [FindMatchesTaskRunProperties](#aws-glue-api-machine-learning-api-FindMatchesTaskRunProperties "#aws-glue-api-machine-learning-api-FindMatchesTaskRunProperties") object.

The configuration properties for a find matches task run.

## FindMatchesTaskRunProperties structure

Specifies configuration properties for a Find Matches task run.

###### Fields

- `JobId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job ID for the Find Matches task run.

- `JobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name assigned to the job for the Find Matches task run.

- `JobRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The job run ID for the Find Matches task run.

## ImportLabelsTaskRunProperties structure

Specifies configuration properties for an importing labels task run.

###### Fields

- `InputS3Path` – UTF-8 string.

The Amazon Simple Storage Service (Amazon S3) path from where you will
import the labels.

- `Replace` – Boolean.

Indicates whether to overwrite your existing labels.

## ExportLabelsTaskRunProperties structure

Specifies configuration properties for an exporting labels task run.

###### Fields

- `OutputS3Path` – UTF-8 string.

The Amazon Simple Storage Service (Amazon S3) path where you will export
the labels.

## LabelingSetGenerationTaskRunProperties structure

Specifies configuration properties for a labeling set generation task
run.

###### Fields

- `OutputS3Path` – UTF-8 string.

The Amazon Simple Storage Service (Amazon S3) path where you will generate
the labeling set.

## SchemaColumn structure

A key-value pair representing a column and data type that this transform
can run against. The `Schema` parameter of the `MLTransform`
may contain up to 100 of these structures.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the column.

- `DataType` – UTF-8 string, not more than 131072 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The type of data in the column.

## TransformEncryption structure

The encryption-at-rest settings of the transform that apply to accessing
user data. Machine learning transforms can access user data encrypted in Amazon
S3 using KMS.

Additionally, imported labels and trained transforms can now be encrypted
using a customer provided KMS key.

###### Fields

- `MlUserDataEncryption` – A [MLUserDataEncryption](#aws-glue-api-machine-learning-api-MLUserDataEncryption "#aws-glue-api-machine-learning-api-MLUserDataEncryption") object.

An `MLUserDataEncryption` object containing the encryption
mode and customer-provided KMS key ID.

- `TaskRunSecurityConfigurationName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the security configuration.

## MLUserDataEncryption structure

The encryption-at-rest settings of the transform that apply to accessing
user data.

###### Fields

- `MlUserDataEncryptionMode` – _Required:_ UTF-8 string (valid values: `DISABLED` | `SSE-KMS="SSEKMS"`).

The encryption mode applied to user data. Valid values are:

    + DISABLED: encryption is disabled
    + SSEKMS: use of server-side encryption with AWS Key Management Service (SSE-KMS)
     for user data stored in Amazon S3.

- `KmsKeyId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID for the customer-provided KMS key.

## ColumnImportance structure

A structure containing the column name and column importance score for
a column.

Column importance helps you understand how columns contribute to your
model, by identifying which columns in your records are more important than others.

###### Fields

- `ColumnName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of a column.

- `Importance` – Number (double), not more than 1.0.

The column importance score for the column, as a decimal.

## Operations

- [CreateMLTransform action (Python: create_ml_transform)](#aws-glue-api-machine-learning-api-CreateMLTransform "#aws-glue-api-machine-learning-api-CreateMLTransform")
- [UpdateMLTransform action (Python: update_ml_transform)](#aws-glue-api-machine-learning-api-UpdateMLTransform "#aws-glue-api-machine-learning-api-UpdateMLTransform")
- [DeleteMLTransform action (Python: delete_ml_transform)](#aws-glue-api-machine-learning-api-DeleteMLTransform "#aws-glue-api-machine-learning-api-DeleteMLTransform")
- [GetMLTransform action (Python: get_ml_transform)](#aws-glue-api-machine-learning-api-GetMLTransform "#aws-glue-api-machine-learning-api-GetMLTransform")
- [GetMLTransforms action (Python: get_ml_transforms)](#aws-glue-api-machine-learning-api-GetMLTransforms "#aws-glue-api-machine-learning-api-GetMLTransforms")
- [ListMLTransforms action (Python: list_ml_transforms)](#aws-glue-api-machine-learning-api-ListMLTransforms "#aws-glue-api-machine-learning-api-ListMLTransforms")
- [StartMLEvaluationTaskRun action (Python: start_ml_evaluation_task_run)](#aws-glue-api-machine-learning-api-StartMLEvaluationTaskRun "#aws-glue-api-machine-learning-api-StartMLEvaluationTaskRun")
- [StartMLLabelingSetGenerationTaskRun action (Python: start_ml_labeling_set_generation_task_run)](#aws-glue-api-machine-learning-api-StartMLLabelingSetGenerationTaskRun "#aws-glue-api-machine-learning-api-StartMLLabelingSetGenerationTaskRun")
- [GetMLTaskRun action (Python: get_ml_task_run)](#aws-glue-api-machine-learning-api-GetMLTaskRun "#aws-glue-api-machine-learning-api-GetMLTaskRun")
- [GetMLTaskRuns action (Python: get_ml_task_runs)](#aws-glue-api-machine-learning-api-GetMLTaskRuns "#aws-glue-api-machine-learning-api-GetMLTaskRuns")
- [CancelMLTaskRun action (Python: cancel_ml_task_run)](#aws-glue-api-machine-learning-api-CancelMLTaskRun "#aws-glue-api-machine-learning-api-CancelMLTaskRun")
- [StartExportLabelsTaskRun action (Python: start_export_labels_task_run)](#aws-glue-api-machine-learning-api-StartExportLabelsTaskRun "#aws-glue-api-machine-learning-api-StartExportLabelsTaskRun")
- [StartImportLabelsTaskRun action (Python: start_import_labels_task_run)](#aws-glue-api-machine-learning-api-StartImportLabelsTaskRun "#aws-glue-api-machine-learning-api-StartImportLabelsTaskRun")

## CreateMLTransform action (Python: create_ml_transform)

Creates an AWS Glue machine learning transform. This operation
creates the transform and all the necessary parameters to train it.

Call this operation as the first step in the process of using a machine learning
transform (such as the `FindMatches` transform) for deduplicating
data. You can provide an optional `Description`, in addition to
the parameters that you want to use for your algorithm.

You must also specify certain parameters for the tasks that AWS Glue runs on your behalf as part of learning from your data and creating a high-quality
machine learning transform. These parameters include `Role`,
and optionally, `AllocatedCapacity`, `Timeout`,
and `MaxRetries`. For more information, see [Jobs](aws-glue-api-jobs-job.md "aws-glue-api-jobs-job.md").

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique name that you give the transform when you create it.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the machine learning transform that is being defined.
The default is an empty string.

- `InputRecordTables` – _Required:_ An array of [GlueTable](#aws-glue-api-machine-learning-api-GlueTable "#aws-glue-api-machine-learning-api-GlueTable") objects, not more than 10 structures.

A list of AWS Glue table definitions used by the transform.

- `Parameters` – _Required:_ A [TransformParameters](#aws-glue-api-machine-learning-api-TransformParameters "#aws-glue-api-machine-learning-api-TransformParameters") object.

The algorithmic parameters that are specific to the transform type used.
Conditionally dependent on the transform type.

- `Role` – _Required:_ UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role with the required
permissions. The required permissions include both AWS Glue service
role permissions to AWS Glue resources, and Amazon S3 permissions
required by the transform.

    + This role needs AWS Glue service role permissions to allow
     access to resources in AWS Glue. See [Attach a Policy to IAM
     Users That Access AWS Glue](attach-policy-iam-user.md "attach-policy-iam-user.md").
    + This role needs permission to your Amazon Simple Storage Service (Amazon
     S3) sources, targets, temporary directory, scripts, and any libraries used
     by the task run for this transform.

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

This value determines which version of AWS Glue this machine
learning transform is compatible with. Glue 1.0 is recommended for most customers.
If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information,
see [AWS Glue Versions](release-notes.md#release-notes-versions "release-notes.md#release-notes-versions") in the developer guide.

- `MaxCapacity` – Number (double).

The number of AWS Glue data processing units (DPUs) that are
allocated to task runs for this transform. You can allocate from 2 to 100 DPUs;
the default is 10. A DPU is a relative measure of processing power that consists
of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
[AWS Glue pricing
page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

`MaxCapacity` is a mutually exclusive option with `NumberOfWorkers`
and `WorkerType`.

    + If either `NumberOfWorkers` or `WorkerType`
     is set, then `MaxCapacity` cannot be set.
    + If `MaxCapacity` is set then neither `NumberOfWorkers`
     or `WorkerType` can be set.
    + If `WorkerType` is set, then `NumberOfWorkers`
     is required (and vice versa).
    + `MaxCapacity` and `NumberOfWorkers` must
     both be at least 1.

When the `WorkerType` field is set to a value other than `Standard`,
the `MaxCapacity` field is set automatically and becomes read-only.

When the `WorkerType` field is set to a value other than `Standard`,
the `MaxCapacity` field is set automatically and becomes read-only.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when this task runs. Accepts
a value of Standard, G.1X, or G.2X.

    + For the `Standard` worker type, each worker provides 4 vCPU,
     16 GB of memory and a 50GB disk, and 2 executors per worker.
    + For the `G.1X` worker type, each worker provides 4 vCPU, 16
     GB of memory and a 64GB disk, and 1 executor per worker.
    + For the `G.2X` worker type, each worker provides 8 vCPU, 32
     GB of memory and a 128GB disk, and 1 executor per worker.

`MaxCapacity` is a mutually exclusive option with `NumberOfWorkers`
and `WorkerType`.

    + If either `NumberOfWorkers` or `WorkerType`
     is set, then `MaxCapacity` cannot be set.
    + If `MaxCapacity` is set then neither `NumberOfWorkers`
     or `WorkerType` can be set.
    + If `WorkerType` is set, then `NumberOfWorkers`
     is required (and vice versa).
    + `MaxCapacity` and `NumberOfWorkers` must
     both be at least 1.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when this task runs.

If `WorkerType` is set, then `NumberOfWorkers`
is required (and vice versa).

- `Timeout` – Number (integer), at least 1.

The timeout of the task run for this transform in minutes. This is the maximum
time that a task run for this transform can consume resources before it is terminated
and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).

- `MaxRetries` – Number (integer).

The maximum number of times to retry a task for this transform after a task
run fails.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags to use with this machine learning transform. You may use tags to
limit access to the machine learning transform. For more information about tags
in AWS Glue, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md") in the developer guide.

- `TransformEncryption` – A [TransformEncryption](#aws-glue-api-machine-learning-api-TransformEncryption "#aws-glue-api-machine-learning-api-TransformEncryption") object.

The encryption-at-rest settings of the transform that apply to accessing
user data. Machine learning transforms can access user data encrypted in Amazon
S3 using KMS.

###### Response

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier that is generated for the transform.

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `AccessDeniedException`
- `ResourceNumberLimitExceededException`
- `IdempotentParameterMismatchException`

## UpdateMLTransform action (Python: update_ml_transform)

Updates an existing machine learning transform. Call this operation
to tune the algorithm parameters to achieve better results.

After calling this operation, you can call the `StartMLEvaluationTaskRun`
operation to assess how well your new parameters achieved your goals (such as
improving the quality of your machine learning transform, or making it more cost-effective).

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier that was generated when the transform was created.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique name that you gave the transform when you created it.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the transform. The default is an empty string.

- `Parameters` – A [TransformParameters](#aws-glue-api-machine-learning-api-TransformParameters "#aws-glue-api-machine-learning-api-TransformParameters") object.

The configuration parameters that are specific to the transform type
(algorithm) used. Conditionally dependent on the transform type.

- `Role` – UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role with the required
permissions.

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

This value determines which version of AWS Glue this machine
learning transform is compatible with. Glue 1.0 is recommended for most customers.
If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information,
see [AWS Glue Versions](release-notes.md#release-notes-versions "release-notes.md#release-notes-versions") in the developer guide.

- `MaxCapacity` – Number (double).

The number of AWS Glue data processing units (DPUs) that are
allocated to task runs for this transform. You can allocate from 2 to 100 DPUs;
the default is 10. A DPU is a relative measure of processing power that consists
of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
[AWS Glue pricing
page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

When the `WorkerType` field is set to a value other than `Standard`,
the `MaxCapacity` field is set automatically and becomes read-only.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when this task runs. Accepts
a value of Standard, G.1X, or G.2X.

    + For the `Standard` worker type, each worker provides 4 vCPU,
     16 GB of memory and a 50GB disk, and 2 executors per worker.
    + For the `G.1X` worker type, each worker provides 4 vCPU, 16
     GB of memory and a 64GB disk, and 1 executor per worker.
    + For the `G.2X` worker type, each worker provides 8 vCPU, 32
     GB of memory and a 128GB disk, and 1 executor per worker.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when this task runs.

- `Timeout` – Number (integer), at least 1.

The timeout for a task run for this transform in minutes. This is the maximum
time that a task run for this transform can consume resources before it is terminated
and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).

- `MaxRetries` – Number (integer).

The maximum number of times to retry a task for this transform after a task
run fails.

###### Response

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the transform that was updated.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `AccessDeniedException`

## DeleteMLTransform action (Python: delete_ml_transform)

Deletes an AWS Glue machine learning transform. Machine learning
transforms are a special type of transform that use machine learning to learn
the details of the transformation to be performed by learning from examples provided
by humans. These transformations are then saved by AWS Glue. If you
no longer need a transform, you can delete it by calling `DeleteMLTransforms`.
However, any AWS Glue jobs that still reference the deleted transform
will no longer succeed.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the transform to delete.

###### Response

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the transform that was deleted.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetMLTransform action (Python: get_ml_transform)

Gets an AWS Glue machine learning transform artifact and all
its corresponding metadata. Machine learning transforms are a special type
of transform that use machine learning to learn the details of the transformation
to be performed by learning from examples provided by humans. These transformations
are then saved by AWS Glue. You can retrieve their metadata by calling
`GetMLTransform`.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the transform, generated at the time that the
transform was created.

###### Response

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the transform, generated at the time that the
transform was created.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique name given to the transform when it was created.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the transform.

- `Status` – UTF-8 string (valid values: `NOT_READY` | `READY` | `DELETING`).

The last known status of the transform (to indicate whether it can be used
or not). One of "NOT_READY", "READY", or "DELETING".

- `CreatedOn` – Timestamp.

The date and time when the transform was created.

- `LastModifiedOn` – Timestamp.

The date and time when the transform was last modified.

- `InputRecordTables` – An array of [GlueTable](#aws-glue-api-machine-learning-api-GlueTable "#aws-glue-api-machine-learning-api-GlueTable") objects, not more than 10 structures.

A list of AWS Glue table definitions used by the transform.

- `Parameters` – A [TransformParameters](#aws-glue-api-machine-learning-api-TransformParameters "#aws-glue-api-machine-learning-api-TransformParameters") object.

The configuration parameters that are specific to the algorithm used.

- `EvaluationMetrics` – An [EvaluationMetrics](#aws-glue-api-machine-learning-api-EvaluationMetrics "#aws-glue-api-machine-learning-api-EvaluationMetrics") object.

The latest evaluation metrics.

- `LabelCount` – Number (integer).

The number of labels available for this transform.

- `Schema` – An array of [SchemaColumn](#aws-glue-api-machine-learning-api-SchemaColumn "#aws-glue-api-machine-learning-api-SchemaColumn") objects, not more than 100 structures.

The `Map<Column, Type>` object that represents the
schema that this transform accepts. Has an upper bound of 100 columns.

- `Role` – UTF-8 string.

The name or Amazon Resource Name (ARN) of the IAM role with the required
permissions.

- `GlueVersion` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #48](aws-glue-api-common.md#regex_48 "aws-glue-api-common.md#regex_48").

This value determines which version of AWS Glue this machine
learning transform is compatible with. Glue 1.0 is recommended for most customers.
If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information,
see [AWS Glue Versions](release-notes.md#release-notes-versions "release-notes.md#release-notes-versions") in the developer guide.

- `MaxCapacity` – Number (double).

The number of AWS Glue data processing units (DPUs) that are
allocated to task runs for this transform. You can allocate from 2 to 100 DPUs;
the default is 10. A DPU is a relative measure of processing power that consists
of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the
[AWS Glue pricing
page](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

When the `WorkerType` field is set to a value other than `Standard`,
the `MaxCapacity` field is set automatically and becomes read-only.

- `WorkerType` – UTF-8 string (valid values: `Standard=""` | `G.1X=""` | `G.2X=""` | `G.025X=""` | `G.4X=""` | `G.8X=""` | `Z.2X=""`).

The type of predefined worker that is allocated when this task runs. Accepts
a value of Standard, G.1X, or G.2X.

    + For the `Standard` worker type, each worker provides 4 vCPU,
     16 GB of memory and a 50GB disk, and 2 executors per worker.
    + For the `G.1X` worker type, each worker provides 4 vCPU, 16
     GB of memory and a 64GB disk, and 1 executor per worker.
    + For the `G.2X` worker type, each worker provides 8 vCPU, 32
     GB of memory and a 128GB disk, and 1 executor per worker.

- `NumberOfWorkers` – Number (integer).

The number of workers of a defined `workerType` that are allocated
when this task runs.

- `Timeout` – Number (integer), at least 1.

The timeout for a task run for this transform in minutes. This is the maximum
time that a task run for this transform can consume resources before it is terminated
and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).

- `MaxRetries` – Number (integer).

The maximum number of times to retry a task for this transform after a task
run fails.

- `TransformEncryption` – A [TransformEncryption](#aws-glue-api-machine-learning-api-TransformEncryption "#aws-glue-api-machine-learning-api-TransformEncryption") object.

The encryption-at-rest settings of the transform that apply to accessing
user data. Machine learning transforms can access user data encrypted in Amazon
S3 using KMS.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetMLTransforms action (Python: get_ml_transforms)

Gets a sortable, filterable list of existing AWS Glue machine
learning transforms. Machine learning transforms are a special type of transform
that use machine learning to learn the details of the transformation to be performed
by learning from examples provided by humans. These transformations are then
saved by AWS Glue, and you can retrieve their metadata by calling `GetMLTransforms`.

###### Request

- `NextToken` – UTF-8 string.

A paginated token to offset the results.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

- `Filter` – A [TransformFilterCriteria](#aws-glue-api-machine-learning-api-TransformFilterCriteria "#aws-glue-api-machine-learning-api-TransformFilterCriteria") object.

The filter transformation criteria.

- `Sort` – A [TransformSortCriteria](#aws-glue-api-machine-learning-api-TransformSortCriteria "#aws-glue-api-machine-learning-api-TransformSortCriteria") object.

The sorting criteria.

###### Response

- `Transforms` – _Required:_ An array of [MLTransform](#aws-glue-api-machine-learning-api-MLTransform "#aws-glue-api-machine-learning-api-MLTransform") objects.

A list of machine learning transforms.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListMLTransforms action (Python: list_ml_transforms)

Retrieves a sortable, filterable list of existing AWS Glue
machine learning transforms in this AWS account, or the resources
with the specified tag. This operation takes the optional `Tags`
field, which you can use as a filter of the responses so that tagged resources can
be retrieved as a group. If you choose to use tag filtering, only resources with
the tags are retrieved.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of a list to return.

- `Filter` – A [TransformFilterCriteria](#aws-glue-api-machine-learning-api-TransformFilterCriteria "#aws-glue-api-machine-learning-api-TransformFilterCriteria") object.

A `TransformFilterCriteria` used to filter the machine
learning transforms.

- `Sort` – A [TransformSortCriteria](#aws-glue-api-machine-learning-api-TransformSortCriteria "#aws-glue-api-machine-learning-api-TransformSortCriteria") object.

A `TransformSortCriteria` used to sort the machine learning
transforms.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Specifies to return only these tagged resources.

###### Response

- `TransformIds` – _Required:_ An array of UTF-8 strings.

The identifiers of all the machine learning transforms in the account,
or the machine learning transforms with the specified tags.

- `NextToken` – UTF-8 string.

A continuation token, if the returned list does not contain the last metric
available.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## StartMLEvaluationTaskRun action (Python: start_ml_evaluation_task_run)

Starts a task to estimate the quality of the transform.

When you provide label sets as examples of truth, AWS Glue machine
learning uses some of those examples to learn from them. The rest of the labels
are used as a test to estimate quality.

Returns a unique identifier for the run. You can call `GetMLTaskRun`
to get more information about the stats of the `EvaluationTaskRun`.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

###### Response

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier associated with this run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ConcurrentRunsExceededException`
- `MLTransformNotReadyException`

## StartMLLabelingSetGenerationTaskRun action (Python: start_ml_labeling_set_generation_task_run)

Starts the active learning workflow for your machine learning transform
to improve the transform's quality by generating label sets and adding labels.

When the `StartMLLabelingSetGenerationTaskRun` finishes,
AWS Glue will have generated a "labeling set" or a set of questions
for humans to answer.

In the case of the `FindMatches` transform, these questions
are of the form, "What is the correct way to group these rows together into groups
composed entirely of matching records?"

After the labeling process is finished, you can upload your labels with
a call to `StartImportLabelsTaskRun`. After `StartImportLabelsTaskRun`
finishes, all future runs of the machine learning transform will use the new and
improved labels and perform a higher-quality transformation.

Note: The role used to write the generated labeling set to the `OutputS3Path`
is the role associated with the Machine Learning Transform, specified in the
`CreateMLTransform` API.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `OutputS3Path` – _Required:_ UTF-8 string.

The Amazon Simple Storage Service (Amazon S3) path where you generate
the labeling set.

###### Response

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier that is associated with this task run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ConcurrentRunsExceededException`

## GetMLTaskRun action (Python: get_ml_task_run)

Gets details for a specific task run on a machine learning transform. Machine
learning task runs are asynchronous tasks that AWS Glue runs on your
behalf as part of various machine learning workflows. You can check the stats
of any task run by calling `GetMLTaskRun` with the `TaskRunID`
and its parent transform's `TransformID`.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `TaskRunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the task run.

###### Response

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the task run.

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique run identifier associated with this run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this task run.

- `LogGroupName` – UTF-8 string.

The names of the log groups that are associated with the task run.

- `Properties` – A [TaskRunProperties](#aws-glue-api-machine-learning-api-TaskRunProperties "#aws-glue-api-machine-learning-api-TaskRunProperties") object.

The list of properties that are associated with the task run.

- `ErrorString` – UTF-8 string.

The error strings that are associated with the task run.

- `StartedOn` – Timestamp.

The date and time when this task run started.

- `LastModifiedOn` – Timestamp.

The date and time when this task run was last modified.

- `CompletedOn` – Timestamp.

The date and time when this task run was completed.

- `ExecutionTime` – Number (integer).

The amount of time (in seconds) that the task run consumed resources.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## GetMLTaskRuns action (Python: get_ml_task_runs)

Gets a list of runs for a machine learning transform. Machine learning
task runs are asynchronous tasks that AWS Glue runs on your behalf
as part of various machine learning workflows. You can get a sortable, filterable
list of machine learning task runs by calling `GetMLTaskRuns` with
their parent transform's `TransformID` and other optional parameters
as documented in this section.

This operation returns a list of historic runs and must be paginated.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `NextToken` – UTF-8 string.

A token for pagination of the results. The default is empty.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

- `Filter` – A [TaskRunFilterCriteria](#aws-glue-api-machine-learning-api-TaskRunFilterCriteria "#aws-glue-api-machine-learning-api-TaskRunFilterCriteria") object.

The filter criteria, in the `TaskRunFilterCriteria` structure,
for the task run.

- `Sort` – A [TaskRunSortCriteria](#aws-glue-api-machine-learning-api-TaskRunSortCriteria "#aws-glue-api-machine-learning-api-TaskRunSortCriteria") object.

The sorting criteria, in the `TaskRunSortCriteria` structure,
for the task run.

###### Response

- `TaskRuns` – An array of [TaskRun](#aws-glue-api-machine-learning-api-TaskRun "#aws-glue-api-machine-learning-api-TaskRun") objects.

A list of task runs that are associated with the transform.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## CancelMLTaskRun action (Python: cancel_ml_task_run)

Cancels (stops) a task run. Machine learning task runs are asynchronous
tasks that AWS Glue runs on your behalf as part of various machine learning
workflows. You can cancel a machine learning task run at any time by calling `CancelMLTaskRun`
with a task run's parent transform's `TransformID` and the task
run's `TaskRunId`.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `TaskRunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the task run.

###### Response

- `TransformId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the task run.

- `Status` – UTF-8 string (valid values: `RUNNING` | `FINISHED` | `FAILED` | `PENDING_EXECUTION` | `TIMED_OUT` | `CANCELING` | `CANCELED` | `RECEIVED_BY_TASKRUNNER`).

The status for this run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## StartExportLabelsTaskRun action (Python: start_export_labels_task_run)

Begins an asynchronous task to export all labeled data for a particular
transform. This task is the only label-related API call that is not part of the
typical active learning workflow. You typically use `StartExportLabelsTaskRun`
when you want to work with all of your existing labels at the same time, such as when
you want to remove or change labels that were previously submitted as truth. This
API operation accepts the `TransformId` whose labels you want to
export and an Amazon Simple Storage Service (Amazon S3) path to export the labels
to. The operation returns a `TaskRunId`. You can check on the status
of your task run by calling the `GetMLTaskRun` API.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `OutputS3Path` – _Required:_ UTF-8 string.

The Amazon S3 path where you export the labels.

###### Response

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the task run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## StartImportLabelsTaskRun action (Python: start_import_labels_task_run)

Enables you to provide additional labels (examples of truth) to be used
to teach the machine learning transform and improve its quality. This API operation
is generally used as part of the active learning workflow that starts with the
`StartMLLabelingSetGenerationTaskRun` call and that ultimately
results in improving the quality of your machine learning transform.

After the `StartMLLabelingSetGenerationTaskRun` finishes,
AWS Glue machine learning will have generated a series of questions
for humans to answer. (Answering these questions is often called 'labeling'
in the machine learning workflows). In the case of the `FindMatches`
transform, these questions are of the form, "What is the correct way to group these
rows together into groups composed entirely of matching records?" After the
labeling process is finished, users upload their answers/labels with a call
to `StartImportLabelsTaskRun`. After `StartImportLabelsTaskRun`
finishes, all future runs of the machine learning transform use the new and improved
labels and perform a higher-quality transformation.

By default, `StartMLLabelingSetGenerationTaskRun` continually
learns from and combines all labels that you upload unless you set `Replace`
to true. If you set `Replace` to true, `StartImportLabelsTaskRun`
deletes and forgets all previously uploaded labels and learns only from the exact
set that you upload. Replacing labels can be helpful if you realize that you previously
uploaded incorrect labels, and you believe that they are having a negative effect
on your transform quality.

You can check on the status of your task run by calling the `GetMLTaskRun`
operation.

###### Request

- `TransformId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier of the machine learning transform.

- `InputS3Path` – _Required:_ UTF-8 string.

The Amazon Simple Storage Service (Amazon S3) path from where you import
the labels.

- `ReplaceAllLabels` – Boolean.

Indicates whether to overwrite your existing labels.

###### Response

- `TaskRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the task run.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `InternalServiceException`
