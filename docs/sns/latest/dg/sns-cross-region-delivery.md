# Sending Amazon SNS messages to an Amazon SQS queue or

AWS Lambda function in a different Region

Amazon SNS supports cross-region deliveries, both for Regions that are enabled by default and
for [opt-in Regions](#opt-in-regions "#opt-in-regions"). For the current list of AWS
Regions that Amazon SNS supports, including opt-in Regions, see [Amazon Simple Notification Service endpoints and quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") in the
_Amazon Web Services General Reference._

Amazon SNS supports the cross-region delivery of notifications to Amazon SQS queues and to AWS Lambda
functions. When one of the Regions is an opt-in Region, you must specify a different Amazon SNS
service principal in the subscribed resource's policy.

The Amazon SNS subscription command must be executed in the region where Amazon SNS is hosted, in
the corresponding region. For example, if Amazon SNS is in account "A" in the us-east-1
region, and the Lambda function is in account "B" in the us-east-2 region, the
subscription CLI command must be executed in account "A" in the us-east-1
region.

## Opt-in Regions

Amazon SNS supports the following opt-in Regions:

| Region name                             | Region                                                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ----------------------- |
| Africa (Cape Town) Region               | af-south-1                                                                                                    |
| Asia Pacific (Hong Kong) Region         | ap-east-1                                                                                                     |
| Asia Pacific (Hyderabad) Region         | ap-south-2                                                                                                    |
| Asia Pacific (Jakarta) Region           | ap-southeast-3                                                                                                |
| Asia Pacific (Melbourne) Region         | ap-southeast-4                                                                                                |
| Europe (Milan) Region                   | eu-south-1                                                                                                    |
| Europe (Spain) Region                   | eu-south-2                                                                                                    |
| Europe (Zurich) Region                  | eu-central-2                                                                                                  |
| Israel (Tel Aviv) Region                | il-central-1                                                                                                  |
| Middle East (Bahrain) Region            | me-south-1                                                                                                    |
| Middle East (UAE) Region                | me-central-1                                                                                                  | For information on enabling an opt-in Region, see [Managing AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the _Amazon Web Services General Reference._ When you use Amazon SNS to deliver messages from opt-in Regions to Regions that are enabled by default, you must alter the resource policy created for the queue. Replace the principal `sns.amazonaws.com` with `sns.<opt-in-region>.amazonaws.com`. For example: <br>• To subscribe an Amazon SQS queue in US East (N. Virginia) to an Amazon SNS topic in Asia Pacific (Hong Kong), change the principal in the queue policy to `sns.ap-east-1.amazonaws.com`. Opt-in regions include any regions launched after March 20, 2019, which includes Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Middle East (Bahrain), Europe (Milan), and Africa (Cape Town). Regions launched prior to March 20, 2019 are enabled by default. Cross-region delivery support to Amazon SQS                                                                                                                                                                                                                                                                                                                                   | Cross-region delivery type | Supported/Not supported |
| ---                                     | ---                                                                                                           |
| Default-enabled Region to opt-in Region | Supported using `sns.`queue-region`.amazonaws.com` in the service principal for the queue                     |
| Opt-in Region to default-enabled Region | Supported using `sns.`topic-region`.amazonaws.com` in the service principal for the queue                     |
| Opt-in Region to opt-in Region          | Supported using `sns.`queue-region`.amazonaws.com` in the service principal for the queue                     | The following is an example of an access policy statement that allows an Amazon SNS topic in an opt-in Region (af-south-1) to deliver to an Amazon SQS queue in an enabled-by-default Region (us-east-1). It contains the necessary regionalized service principal configuration under the path `Statement`/`Principal`/`Service`. JSON `` `{ "Version":"2012-10-17", "Id": "__default_policy_ID", "Statement": [ { "Sid": "allow_sns_arn:aws:sns:af-south-1:111111111111:source_topic_name", "Effect": "Allow", "Principal": { "Service": "sns.af-south-1.amazonaws.com" }, "Action": "SQS:SendMessage", "Resource": "arn:aws:sqs:us-west-1:111111111111:destination_queue_name", "Condition": { "ArnLike": { "aws:SourceArn": "arn:aws:sns:af-south-1:111111111111:source_topic_name" } } } ] }` `` <br>• To subscribe an AWS Lambda function in US East (N. Virginia) to an Amazon SNS topic in Asia Pacific (Hong Kong), change the principal in the AWS Lambda function policy to `sns.ap-east-1.amazonaws.com`. Opt-in regions include any regions launched after March 20, 2019, which includes Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Middle East (Bahrain), Europe (Milan), and Africa (Cape Town). Regions launched prior to March 20, 2019 are enabled by default. Cross-region delivery support to AWS Lambda | Cross-region delivery type | Supported/Not supported |
| ---                                     | ---                                                                                                           |
| Default-enabled Region to opt-in Region | Supported using `sns.`lambda-function-region`.amazonaws.com` in the service principal for the Lambda function |
| Opt-in Region to default-enabled Region | Supported using `sns.`topic-region`.amazonaws.com` in the service principal for the Lambda function           |
| Opt-in Region to opt-in Region          | Supported using `sns.`lambda-function-region`.amazonaws.com` in the service principal for the Lambda function |
