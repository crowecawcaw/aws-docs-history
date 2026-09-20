

# Sending Amazon SNS messages to an Amazon SQS queue or AWS Lambda function in a different Region
<a name="sns-cross-region-delivery"></a>

Amazon SNS supports cross-Region deliveries, both for Regions that are enabled by default and for [opt-in Regions](#opt-in-regions). For the current list of AWS Regions that Amazon SNS supports, including opt-in Regions, see [Amazon Simple Notification Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html) in the *Amazon Web Services General Reference.* 

Amazon SNS supports the cross-Region delivery of notifications to Amazon SQS queues and to AWS Lambda functions. When one of the Regions is an opt-in Region, you must specify a different Amazon SNS service principal in the subscribed resource's policy.

The Amazon SNS subscription command must be executed in the Region where Amazon SNS is hosted, in the corresponding Region. For example, if Amazon SNS is in account "A" in the us-east-1 Region, and the Lambda function is in account "B" in the us-east-2 Region, the subscription CLI command must be executed in account "A" in the us-east-1 Region.

## Opt-in Regions
<a name="opt-in-regions"></a>

Amazon SNS supports the following opt-in Regions: 


| Region name | Region | 
| --- | --- | 
| Africa (Cape Town) Region | af-south-1 | 
| Asia Pacific (Hong Kong) Region | ap-east-1 | 
| Asia Pacific (Hyderabad) Region | ap-south-2 | 
| Asia Pacific (Jakarta) Region | ap-southeast-3 | 
| Asia Pacific (Melbourne) Region | ap-southeast-4 | 
| Europe (Milan) Region | eu-south-1 | 
| Europe (Spain) Region | eu-south-2 | 
| Europe (Zurich) Region | eu-central-2 | 
| Israel (Tel Aviv) Region | il-central-1 | 
| Middle East (Bahrain) Region | me-south-1 | 
| Middle East (UAE) Region | me-central-1 | 

For information on enabling an opt-in Region, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *Amazon Web Services General Reference.*

When you use Amazon SNS to deliver messages from opt-in Regions to Regions that are enabled by default, you must alter the resource policy created for the queue. Replace the principal `sns.amazonaws.com` with `sns.<opt-in-region>.amazonaws.com`. For example:
+  To subscribe an Amazon SQS queue in US East (N. Virginia) to an Amazon SNS topic in Asia Pacific (Hong Kong), change the principal in the queue policy to `sns.ap-east-1.amazonaws.com`. Opt-in regions include any regions launched after March 20, 2019, which includes Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Middle East (Bahrain), Europe (Milan), and Africa (Cape Town). Regions launched before March 20, 2019 are enabled by default. 


**Cross-region delivery support to Amazon SQS**  

<table>
<thead>
  <tr><th>Cross-region delivery type</th><th>Supported/Not supported</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Default-enabled Region to opt-in Region</td><td>Supported using <code>sns.queue-region.amazonaws.com</code> in the service principal for the queue</td><td></td></tr>
  <tr><td>Opt-in Region to default-enabled Region</td><td>Supported using <code>sns.topic-region.amazonaws.com</code> in the service principal for the queue</td><td></td></tr>
  <tr><td>Opt-in Region to opt-in Region</td><td>Supported using <code>sns.queue-region.amazonaws.com</code> in the service principal for the queue</td><td></td></tr>
</tbody>
</table>


  The following is an example of an access policy statement that allows an Amazon SNS topic in an opt-in Region (af-south-1) to deliver to an Amazon SQS queue in an enabled-by-default Region (us-east-1). It contains the necessary regionalized service principal configuration under the path `Statement`/`Principal`/`Service`. 

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Id": "__default_policy_ID",
      "Statement": [
          {
              "Sid": "allow_sns_arn:aws:sns:af-south-1:111111111111:source_topic_name",
              "Effect": "Allow",
              "Principal": {
                  "Service": "sns.af-south-1.amazonaws.com"
              },
              "Action": "SQS:SendMessage",
              "Resource": "arn:aws:sqs:us-west-1:111111111111:destination_queue_name",
              "Condition": {
                  "ArnLike": {
                      "aws:SourceArn": "arn:aws:sns:af-south-1:111111111111:source_topic_name"
                  }
              }
          }
      ]
  }
  ```

------
+  To subscribe an AWS Lambda function in US East (N. Virginia) to an Amazon SNS topic in Asia Pacific (Hong Kong), change the principal in the AWS Lambda function policy to `sns.ap-east-1.amazonaws.com`. Opt-in regions include any regions launched after March 20, 2019, which includes Asia Pacific (Hong Kong), Asia Pacific (Jakarta), Middle East (Bahrain), Europe (Milan), and Africa (Cape Town). Regions launched before March 20, 2019 are enabled by default. 


**Cross-region delivery support to AWS Lambda**  

<table>
<thead>
  <tr><th>Cross-region delivery type</th><th>Supported/Not supported</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Default-enabled Region to opt-in Region </td><td>Supported using <code>sns.lambda-function-region.amazonaws.com</code> in the service principal for the Lambda function</td><td></td></tr>
  <tr><td>Opt-in Region to default-enabled Region</td><td>Supported using <code>sns.topic-region.amazonaws.com</code> in the service principal for the Lambda function</td><td></td></tr>
  <tr><td>Opt-in Region to opt-in Region</td><td>Supported using <code>sns.lambda-function-region.amazonaws.com</code> in the service principal for the Lambda function</td><td></td></tr>
</tbody>
</table>
