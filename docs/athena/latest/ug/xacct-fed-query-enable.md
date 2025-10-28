# Enable cross-account federated queries

Federated query allows you to query data sources other than Amazon S3 using data source
connectors deployed on AWS Lambda. The cross-account federated query feature allows the Lambda
function and the data sources that are to be queried to be located in different
accounts.

###### Note

Use this method only if you have not registered your federated data source with the
AWS Glue Data Catalog. If you have registered your data source with the AWS Glue Data Catalog, use the
AWS Glue Data Catalog cross account features and permissions model. For more information, see
[Granting
cross-account access](../../../glue/latest/dg/cross-account-access.md "../../../glue/latest/dg/cross-account-access.md") in the _AWS Glue User Guide_.

As a data administrator, you can enable cross-account federated queries by sharing your
data connector with a data analyst's account or, as a data analyst, by using a shared Lambda
ARN from a data administrator to add to your account. When configuration changes are made to
a connector in the originating account, the updated configuration is automatically applied
to the shared instances of the connector in other user's accounts.

## Considerations

and limitations

- The cross-account federated query feature is available for non-Hive metastore
  data connectors that use a Lambda-based data source.
- The feature is not available for the AWS Glue Data Catalog data source type. For
  information about cross-account access to AWS Glue Data Catalogs, see [Configure cross-account
  access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md").
- If the response from your connector's Lambda function exceeds the Lambda
  response size limit of 6MB, Athena automatically encrypts, batches, and spills
  the response to an Amazon S3 bucket that you configure. The entity running the Athena
  query must have access to the spill location in order for Athena to read the
  spilled data. We recommend that you set an Amazon S3 lifecycle policy to delete
  objects from the spill location since the data is not needed after the query
  completes.
- Using federated queries across AWS Regions is not supported.

## Required

permissions

To set up the required permissions, actions must be taken in both Account A (`444455556666`) and
Account B (`111122223333`).

### Actions for

Account A

For data administrator Account A to share a Lambda function with data analyst
Account B, Account B requires Lambda invoke function and spill bucket access.
Accordingly, Account A should add a [resource-based
policy](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") to the Lambda function and [principal](../../../AmazonS3/latest/userguide/access-policy-language-overview.md "../../../AmazonS3/latest/userguide/access-policy-language-overview.md") access to its spill bucket in Amazon S3.

1. The following policy grants Lambda invoke function permissions to Account B
   on a Lambda function in Account A.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CrossAccountInvocationStatement",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:user/`username`"
 ]
 },
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:`us-east-1`:`444455556666`:function:`lambda-function-name`"
 }
 ]
}`

```

2. The following policy allows spill bucket access to the principal in
   Account B.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": ["arn:aws:iam::`111122223333`:user/`username`"]
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`spill-bucket`",
 "arn:aws:s3:::`spill-bucket`/*"
 ]
 }
 ]
 }`

```

3. If the Lambda function is encrypting the spill bucket with a AWS KMS key
   instead of the default encryption offered by the federation SDK, the AWS KMS
   key policy in Account A must grant access to the user in Account B, as in
   the following example.

```
{
    "Sid": "Allow use of the key",
    "Effect": "Allow",
    "Principal":
    {
       "AWS": ["arn:aws:iam::`account-B-id`:user/`username`"]
    },
    "Action": [ "kms:Decrypt" ],
    "Resource": "*" // Resource policy that gets placed on the KMS key.
 }
```

### Actions for

Account B

For Account A to share its connector with Account B, Account B must create a role
called `AthenaCrossAccountCreate-`account-A-id``
that Account A assumes by calling the AWS Security Token Service [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API action.

1. Use the IAM console or the AWS CLI to create the
   `AthenaCrossAccountCreate-`account-A-id``
   role in as a custom trust policy role. A custom trust policy delegates
   access and allows others to perform actions in your AWS account. For
   steps, see [Create a role
   using custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _IAM User Guide_.

The trust relationship should have a principal object in which the key is
`AWS` and the value is the ARN of Account A, as in the
following example.

```
...
"Principal":
{
   "AWS": ["arn:aws:iam::`account-A-id`:user/`username`"]
},
...
```

2. Also in Account B, create a policy like the following that allows the
   `CreateDataCatalog` action.

```
{
 "Effect": "Allow",
 "Action": "athena:CreateDataCatalog",
 "Resource": "arn:aws:athena:*:`account-B-id`:datacatalog/*"
}

```

3. Add the policy that allows the `CreateDataCatalog` action to
   the
   `AthenaCrossAccountCreate-`account-A-id``
   role that you created using Account B.

## Sharing a data source in Account A with Account B

After permissions are in place, you can use the **Data sources and catalogs** page
in the Athena console to share a data connector in your account (Account A) with another
account (Account B). Account A retains full control and ownership of the connector. When
Account A makes configuration changes to the connector, the updated configuration
applies to the shared connector in Account B.

###### Note

You can only share a Lambda type data source and cannot share data sources that use
AWS Glue connections. For more information, see [Available data source connectors](connectors-available.md "connectors-available.md").

###### To share a Lambda data source in Account A with Account B

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 3. Choose **Data sources and catalogs**. 4. On the **Data sources and catalogs** page, choose the link of the
connector that you want to share. 5. On the details page for a Lambda data source, from the
**Actions** menu in the top right corner, choose
**Share**. 6. In the **Share `Lambda-name` with another
account?** dialog box, enter the required information.

    * For **Data source name**, enter the name of the
     copied data source as you want it to appear in the other account.
    * For **Account ID**, enter the ID of the account with
     which you want to share your data source (in this case, Account
     B).

7. Choose **Share**. The shared data connector that you
   specified is created in Account B. Configuration changes to the connector in
   Account A apply to the connector in Account B.

## Adding a shared data source from Account A to Account B

As a data analyst, you may be given the ARN of a connector to add to your account from
a data administrator. You can use the **Data sources and catalogs** page of the
Athena console to add the Lambda ARN provided by your administrator to your
account.

###### To add the Lambda ARN of a shared data connector to your account

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. If the navigation pane is not visible, choose the expansion menu on the
   left.
3. Choose **Data sources and catalogs**.
4. On the **Data sources and catalogs** page, choose **Create data
   source**.
5. On the **Choose a data source** page, choose **Custom
   or shared connector**.
6. Choose **Next**.
7. On the **Enter data source details** page, in the
   **Connection details** section, for **Select or
   enter a Lambda function**, enter the Lambda ARN of Account A.
8. Choose **Next**.
9. On the **Review and create** page, choose **Create
   data source**.

## Troubleshooting

If you receive an error message that Account A does not have the permissions to assume
a role in Account B, make sure that the name of the role created in Account B is spelled
correctly and that it has the proper policy attached.
