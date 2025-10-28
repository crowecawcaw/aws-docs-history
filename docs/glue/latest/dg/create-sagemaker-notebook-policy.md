# Step 6: Create an IAM policy for SageMaker AI

notebooks

If you plan to use SageMaker AI notebooks with development endpoints, you must specify permissions when
you create the notebook. You provide those permissions by using AWS Identity and Access Management
(IAM).

###### To create an IAM policy for SageMaker AI notebooks

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policies**.
3. Choose **Create Policy**.
4. On the **Create Policy** page, navigate to a tab to edit the
   JSON. Create a policy document with the following JSON statements. Edit
   `bucket-name`,
   `region-code`, and `account-id` for your environment.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`*"
 ]
 },
 {
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents",
 "logs:CreateLogGroup"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/sagemaker/*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/sagemaker/*:log-stream:aws-glue-*"
 ]
 },
 {
 "Action": [
 "glue:UpdateDevEndpoint",
 "glue:GetDevEndpoint",
 "glue:GetDevEndpoints"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:devEndpoint/*"
 ]
 },
 {
 "Action": [
 "sagemaker:ListTags"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:notebook-instance/*"
 ]
 }
 ]
}`

```

Then choose **Review policy**.

The following table describes the permissions granted by this policy.

| **Action**                                                                                      | **Resource**                                                                                                                                                       | **Description**                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"s3:ListBucket*"`                                                                              | `"arn:aws:s3:::`bucket-name`"`                                                                                                                                     | Grants permission to list Amazon S3 buckets.                                                                                                                                                   |
| `"s3:GetObject"`                                                                                | `"arn:aws:s3:::`bucket-name`*"`                                                                                                                                    | Grants permission to get Amazon S3 objects that are used by SageMaker AI notebooks.                                                                                                            |
| `"logs:CreateLogStream", "logs:DescribeLogStreams", "logs:PutLogEvents", "logs:CreateLogGroup"` | `"arn:aws:logs:`region-code`:`account-id`:log-group:/aws/sagemaker/*", "arn:aws:logs:`region-code`:`account-id`:log-group:/aws/sagemaker/*:log-stream:aws-glue-*"` | Grants permission to write logs to Amazon CloudWatch Logs from notebooks. Naming convention: Writes to log groups whose names begin with **aws-glue**.                                         |
| `"glue:UpdateDevEndpoint", "glue:GetDevEndpoint", "glue:GetDevEndpoints"`                       | `"arn:aws:glue:`region-code`:`account-id`:devEndpoint/*"`                                                                                                          | Grants permission to use a development endpoint from SageMaker AI notebooks.                                                                                                                   |
| `"sagemaker:ListTags"`                                                                          | `"arn:aws:sagemaker:`region-code`:`account-id`:notebook-instance/*"`                                                                                               | Grants permission to return tags for an SageMaker AI resource. The `aws-glue-dev-endpoint` tag is required on the SageMaker AI notebook for connecting the notebook to a development endpoint. | 5. On the **Review Policy** screen, enter your **Policy Name**, for example `AWSGlueSageMakerNotebook`. Enter an optional description, and when you're satisfied with the policy, choose **Create policy**. |
