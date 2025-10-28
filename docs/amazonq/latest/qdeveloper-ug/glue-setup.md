# Using Amazon Q Developer with AWS Glue Studio

This page describes how to set up and activate Amazon Q Developer for [AWS Glue Studio Notebook](../../../glue/latest/ug/notebooks-chapter.md "../../../glue/latest/ug/notebooks-chapter.md"). Once
activated, Amazon Q can make code recommendations automatically as you write your ETL
code.

###### Note

Amazon Q supports both Python and Scala, the two languages used for coding ETL scripts for Spark jobs in AWS Glue Studio.

In the following procedure, you will set up AWS Glue to work with Amazon Q.

1. [Set up AWS Glue Studio Notebook](../../../glue/latest/ug/notebook-getting-started.md "../../../glue/latest/ug/notebook-getting-started.md").
2. Attach the following policy to your IAM role for Glue Studio notebook

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonQDeveloperPermissions",
 "Effect": "Allow",
 "Action": [
 "codewhisperer:GenerateRecommendations"
 ],
 "Resource": "*"
 }
 ]
}`

```

3. Open the [Glue console](https://console.aws.amazon.com/glue "https://console.aws.amazon.com/glue")
4. Under **ETL jobs**, choose **Notebooks**.
5. Verify that **Jupyter Notebook** is selected. Choose **Create**.
6. Enter a **Job name**.
7. For IAM role, select the role that you configured to interact with Amazon Q
8. Choose **Start notebook**.
