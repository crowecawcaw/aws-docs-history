# Common error messages in Amazon Personalize

The following sections list and explain some of the messages that you might encounter when
using Amazon Personalize.

###### Topics

- [Data import and management](#data-import-troubleshooting "#data-import-troubleshooting")
- [Creating a solution and solution version
  (custom resources)](#training-troubleshooting "#training-troubleshooting")
- [Model deployment (custom
  campaigns)](#deployment-troubleshooting "#deployment-troubleshooting")
- [Recommenders (Domain dataset groups)](#recommender-errors "#recommender-errors")
- [Recommendations](#recommendations-troubleshooting "#recommendations-troubleshooting")
- [Filtering recommendations](#filters-troubleshooting "#filters-troubleshooting")

## Data import and management

**Error message:**
_Invalid Data location._

Make sure you used the correct syntax for your Amazon S3 bucket location. For dataset import
jobs, use the following syntax for the location of your data in Amazon S3:

`s3://amzn-s3-demo-bucket/<folder
 path>/<CSVfilename>`

If your CSV files are in a folder and you want to upload multiple files with one dataset
import job, use this syntax without the CSV file name.

**Error message:**
_An error occurred (LimitExceededException) when calling the
CreateDatasetImportJob operation: More than 5 resources with PENDING or IN_PROGRESS
status._

You can have a total of 5 pending or in progress dataset import jobs
per region. This quota is not adjustable. For a complete list of quotas for Amazon Personalize, see [Amazon Personalize endpoints and quotas](limits.md "limits.md").

**Error message:**
_Failed to create a data import job for <dataset type>
dataset....Insufficient privileges for accessing data in Amazon S3._

Give Amazon Personalize access to your Amazon S3 resources by attaching access policies to your Amazon S3
bucket and your Amazon Personalize service role. See [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").

**Error message:**
_Failed to create a data import job <dataset type>
dataset...Input CSV is missing the following columns:[COLUMN\_NAME,
COLUMN\_NAME]._

The data that you import into Amazon Personalize, including attribute names and data types, must
match the destination dataset's schema. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

**Error message:**
_Length cannot be more than <character limit> characters for <COLLUMN_NAME>. If no values
exceed the character limit, make sure your data follows the formatting guidelines listed in https://docs.aws.amazon.com/personalize/latest/dg/data-prep-formatting.html._

Check to make sure all values in this column don't exceed the character limit. If no values exceed the character limit, check
any preceding textual fields for the following:

- Make sure any textual data is wrapped in double quotes. Use the `\` character to escape any double quotes or `\` characters in your data.
- Makes sure each record in your CSV file is on a single line.

## Creating a solution and solution version

(custom resources)

**Error message:**
_Create failed. Dataset has fewer than 25 users with at least 2
interactions each._

You must import more data before you can train the model. The minimum data requirements
to train a model are:

- At minimum 1000 item interactions records from users interacting with items in your catalog.
  These interactions can be from bulk imports, or streamed events, or both.
- At minimum 25 unique user IDs with at least two item interactions for each.

For real-time recommendations, import more data with a dataset import job or record more interaction _[events](../../../glossary/latest/reference/glos-chap.md#event "../../../glossary/latest/reference/glos-chap.md#event")_ for your users with an event
tracker and the [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md")
operation. For more information on recording real-time events, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").

For batch recommendations, import your data with a dataset import job when you have more
data. For more information, about importing bulk
data see [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md").

## Model deployment (custom

campaigns)

**Error:**
_Cannot create a campaign. More than 5 resources in ACTIVE state.
Please delete some and try again._

You can have a total of 5 active Amazon Personalize campaigns per dataset group. This quota
is adjustable and you can request a quota increase using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For a complete list of limits and
quotas for Amazon Personalize, see [Amazon Personalize endpoints and quotas](limits.md "limits.md").

## Recommenders (Domain dataset groups)

**Error:**
_Dataset has fewer than 1000 interactions after filtering by event
type: <event type>_

Different use cases require different event types. Your data must have at minimum
1000 events with the required type for your use case. For more information, see
[Choosing a use case](domain-use-cases.md "domain-use-cases.md")

## Recommendations

**Batch inference job error message:**
_Invalid S3 input path_ or _Invalid
S3 output path_

Make sure you use the correct syntax for your Amazon S3 input or output locations. Also make
sure that your output location is different from your input data. It should be a folder in the
same Amazon S3 bucket or a different bucket.

Use the following syntax for the _input_ file location in Amazon S3:
`s3://amzn-s3-demo-bucket/<folder name>/<input JSON file
 name>`

Use the following syntax for the _output_ folder in Amazon S3:
`s3://amzn-s3-demo-bucket/<output folder name>/`

## Filtering recommendations

**Error message:**
_Could not create filter. Invalid input symbol: $parameterName. Placeholders are not allowed
with NOT_IN operator._

You can't use placeholder parameters in a filter expression that uses the NOT_IN operator. Instead,
use the IN operator and use the opposite Action: use Include instead of Exclude (or the reverse).

For example, if you want to use `INCLUDE ItemID WHERE Items.GENRE NOT IN ($GENRE)`,
you can use `EXCLUDE ItemID WHERE Items.GENRE IN ($GENRE)` and get the same results.

For more information about filters, see [Filter expression elements](creating-filter-expressions.md#filter-expression-elements "creating-filter-expressions.md#filter-expression-elements").

**Error message:**
_Could not create filter. Invalid Expression..._ when
filtering on Boolean type fields

You can't create filter expressions that filter using values with a Boolean type in your
schema. To filter based on Boolean values, use a schema with a field of type
`String` and use the values `True` and `False` in your
data. Or you can use type `int` or `long` and values `0` and
`1`.

For more information about filters, see [Filter expression elements](creating-filter-expressions.md#filter-expression-elements "creating-filter-expressions.md#filter-expression-elements").
