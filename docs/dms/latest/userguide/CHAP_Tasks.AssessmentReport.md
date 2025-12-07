# Creating prerequisites for premigration assessments

This section describes the Amazon S3 and IAM resources you need to create a premigration assessment.

###### Important

The following prerequisites are only required if you supply your own Amazon S3 bucket and IAM role.

## Create an S3 bucket

AWS DMS stores premigration assessment reports in an S3 bucket. To create the S3 bucket, do the following:

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. On the **Create bucket** page,
   enter a globally unique name that includes your sign-in name for the bucket, such as dms-bucket-`yoursignin`.
4. Choose the AWS Region for the DMS migration task.
5. Leave the remaining settings as they are, and choose **Create bucket**.

##

Create IAM resources

DMS uses an IAM role and policy to access the S3 bucket to store premigration assessment results.

To create the IAM policy, do the following:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. In the **Create policy** page, choose the **JSON** tab.
5. Paste the following JSON code into the editor, replacing the example code.
   Replace `amzn-s3-demo-bucket` with the name of the Amazon S3 bucket that you created in the previous section.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:PutObjectTagging"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 }
 ]
}`

```

6. Choose **Next: Tags**, then choose and **Next: Review**.
7. Enter `DMSPremigrationAssessmentS3Policy` for **Name\***, and
   then choose **Create policy**.

To create the IAM role, do the following:

1. In the IAM console, in the navigation pane, choose **Roles**.
2. Choose **Create role**.
3. On the **Select trusted entity** page, for **Trusted entity type**,
   choose **AWS Service**. For
   **Use cases for other AWS services**, choose **DMS.**
4. Check the **DMS** check box, and then choose **Next.**
5. On the **Add permissions** page, choose **DMSPremigrationAssessmentS3Policy**.
   Choose **Next**.
6. On the **Name, review, and create** page, enter
   `DMSPremigrationAssessmentS3Role` for **Role name**,
   then choose **Create role**.
7. On the **Roles** page, enter `DMSPremigrationAssessmentS3Role`
   for **Role name**. Choose
   **DMSPremigrationAssessmentS3Role**.
8. On the **DMSPremigrationAssessmentS3Role** page, choose the
   **Trust relationships** tab. Choose **Edit trust policy**.
9. On the **Edit trust policy** page, paste the following JSON into the editor,
   replacing the existing text.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"",
 "Effect":"Allow",
 "Principal":{
 "Service":"dms.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

This policy grants the `sts:AssumeRole` permission to DMS to put the
premigration assessment run results into the S3 bucket. 10. Choose **Update policy**.
