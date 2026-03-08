# Creating a new Neptune Analytics notebook using the AWS Management Console

You can create a new notebook for Neptune Analytics by following the instructions mentioned in
[Using the Neptune workbench to host Neptune notebooks](../../../neptune/latest/userguide/graph-notebooks.md#graph-notebooks-workbench "../../../neptune/latest/userguide/graph-notebooks.md#graph-notebooks-workbench") with a few changes:

- While selecting the Neptune service, please choose **Analytics**.
- The console can create an AWS AWS Identity and Access Management role for your notebooks, or you can create one yourself by following
  [Create an IAM role for a Neptune Analytics notebook](create-notebook-console.md#create-notebook-iam-role "create-notebook-console.md#create-notebook-iam-role").

## Create an IAM role for a Neptune Analytics notebook

###### To create an IAM role for a Neptune Analytics notebook

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, expand **Access management**,
   then choose **Roles**.
3. Select **Create role**.
4. Under **Trusted entity type**, select **Custom
   trust policy** and copy in the following trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

5. Choose **Next**, and then **Next** again.
6. Enter a name and description for the role, and select **Create role**.
7. Go back to the **Roles** page, search for the
   name of the role you just created, and open it.
8. On the **Permissions** tab Under **Permissions policies**,
   select **Add permissions** and choose **Create inline policy**.
9. In the **Policy editor**, switch to the **JSON**
   option, and copy in the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowS3",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::aws-neptune-notebook-`us-east-1`",
 "arn:aws:s3:::aws-neptune-notebook-`us-east-1`/*",
 "arn:aws:s3:::aws-neptune-customer-samples-`us-east-1`",
 "arn:aws:s3:::aws-neptune-customer-samples-`us-east-1`/*"
 ]
 },
 {
 "Sid": "AllowNeptuneGraph",
 "Effect": "Allow",
 "Action": "neptune-graph:*",
 "Resource": [
 "arn:aws:neptune-graph:`us-east-1`:`111122223333`:graph/`resource-id`"
 ]
 },
 {
 "Sid": "AllowLogs",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/sagemaker/*"
 ]
 },
 {
 "Sid": "AllowSagemaker",
 "Effect": "Allow",
 "Action": "sagemaker:DescribeNotebookInstance",
 "Resource": [
 "arn:aws:sagemaker:`us-east-1`:`111122223333`:notebook-instance/*"
 ]
 }
 ]
}`

```

10. Choose **Next**.
11. Give a name to the inline policy.
12. Select **Create policy**. Make note of the name
    of the policy you just created.
