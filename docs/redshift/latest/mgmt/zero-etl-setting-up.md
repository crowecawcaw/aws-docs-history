Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create a zero-ETL integration for

DynamoDB

Before creating a zero-ETL integration, review the considerations and requirements outlined in
[Considerations when using zero-ETL integrations with Amazon Redshift](zero-etl.md "zero-etl.md"). Follow this
general flow to create a zero-ETL integration from DynamoDB to Amazon Redshift

###### To replicate DynamoDB data to Amazon Redshift with zero-ETL integration

1. Confirm your sign in credentials allow permissions to work with zero-ETL integrations with
   Amazon Redshift and DynamoDB. See [IAM policy to work with DynamoDB
   zero-ETL integrations](#zero-etl-signin-iam-policy "#zero-etl-signin-iam-policy") for an example IAM policy.
2. From the DynamoDB console, [configure your DynamoDB table](../../../amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.md#RedshiftforDynamoDB-zero-etl-prereqs "../../../amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.md#RedshiftforDynamoDB-zero-etl-prereqs") to have point-in-time recovery (PITR), resource
   policies, identity-based policies, and encryption key permissions as described in the
   _Amazon DynamoDB Developer Guide_.
3. From the Amazon Redshift console: [Create and configure a target
   Amazon Redshift data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
   - From the AWS CLI or Amazon Redshift console: [Turn on case sensitivity for your
     data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
   - From the Amazon Redshift console: [Configure authorization for your Amazon Redshift data
     warehouse](zero-etl-using.md "zero-etl-using.md").

4. From the Amazon Redshift console, create the zero-ETL integration integration as described later in
   this topic.
5. From the Amazon Redshift console, create the destination database in your Amazon Redshift data
   warehouse. For more information, see [Creating destination databases in
   Amazon Redshift](zero-etl-using.md "zero-etl-using.md").
6. From the Amazon Redshift console, query your replicated data in the Amazon Redshift data warehouse. For
   more information, see [Querying replicated
   data in Amazon Redshift](zero-etl-using.md "zero-etl-using.md").
   In this step, you create an Amazon DynamoDB zero-ETL integration with Amazon Redshift.

Amazon Redshift console

###### To create an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the Amazon Redshift console

1. From the Amazon Redshift console, choose **Zero-ETL integrations**. On
   the pane with the list of zero-ETL integrations, choose **Create
   zero-ETL integration**, **Create DynamoDB integration**.
2. On the pages to create an integration, enter information about the
   integration as follows:
   - Enter an **Integration name** – Which is a
     unique name that can be used to reference your integration.
   - Enter a **Description** – That describes the
     data that is to be replicated from source to target.
   - Choose the DynamoDB **Source table** – One DynamoDB
     table can be chosen. Point-in-time recovery (PITR) must be enabled on the
     table. Only tables with a table size up to 100 tebibytes (TiB) are shown.
     The source DynamoDB table must be encrypted. The source must also have a
     resource policy with authorized principals and integration sources. If these
     the policy is not correct, you are presented with the option **Fix
     it for me**.
   - Choose the target **Amazon Redshift data warehouse** – The
     data warehouse can be an Amazon Redshift provisioned cluster or Redshift Serverless workgroup. If
     your target Amazon Redshift is in the same account, you are able to select the target.
     If the target is in a different account, you specify the **Redshift
     data warehouse ARN**. The target must have a resource policy with
     authorized principals and integration source and the
     `enable_case_sensitive_identifier` parameter set to true. If
     you do not have the correct resource policies on the target and your target
     is in the same account, you can select the **Fix it for
     me** option to automatically apply the resource policies during
     the create integration process. If your target is in a different
     AWS account, you need to apply the resource policy on the Amazon Redshift warehouse
     manually. If your target Amazon Redshift data warehouse does not have the correct
     parameter group option `enable_case_sensitive_identifier`
     configured as `true`, you can select the **Fix it for
     me** option to automatically update this parameter group and
     reboot the warehouse during the create integration process.
   - Enter up to 50 tag **Keys** and with an optional
     **Value** – To provide additional metadata about
     the integration. For more information, see [Tag resources in Amazon Redshift](amazon-redshift-tagging.md "amazon-redshift-tagging.md").
   - Choose **Encryption** options – To encrypt the
     integration. For more information, see [Encrypting DynamoDB integrations with a
     customer managed key](#zero-etl.create-encrypt "#zero-etl.create-encrypt").

   When you encrypt the integration, you can also add **Additional
   encryption contexts**. For more information, see [Encryption context](#zero-etl.add-encryption-context "#zero-etl.add-encryption-context").

3. A review page is shown where you can choose **Create DynamoDB
   integration**.
4. A progress page is shown where you can view the progress of the various
   tasks to create the zero-ETL integration.
5. After the integration is created and active, on the details page of the
   integration, choose **Connect to database**. When your Amazon Redshift
   data warehouse was first created, a database was also created. You need to
   connect to any database in your target data warehouse to create another database
   for the integration. In the **Connect to database** page,
   determine whether you can use a recent connection and choose an
   **Authentication** method. Depending on your authentication
   method, enter information to connect to an existing database in your target.
   This authentication information can include the existing **Database
   name** (typically, `dev`) and the **Database
   user** specified when the database was created with the Amazon Redshift data
   warehouse.
6. After you are connected to a database, choose **Create database from
   integration** to create the database that receives the data from the
   source. When you create the database you provide the **Integration
   ID**, **Data warehouse name**, and
   **Database name**.
7. After the integration status and destination database is
   `Active`, data begins to replicate from your DynamoDB table to the
   target table. As you add data to the source it replicates automatically to the
   target Amazon Redshift data warehouse.

AWS CLI
To create an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the AWS CLI, use the
`create-integration` command with the following options:

- `integration-name` – Specify a name for the
  integration.
- `source-arn` – Specify the ARN of the DynamoDB source.
- `target-arn` – Specify the namespace ARN of the Amazon Redshift
  provisioned cluster or Redshift Serverless workgroup target.

The following example creates an integration by providing the integration name,
source ARN, and target ARN. The integration is not encrypted.

```
`aws redshift create-integration \
--integration-name ddb-integration \
--source-arn arn:aws:dynamodb:us-east-1:123456789012:table/books \
--target-arn arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`
          `{
 "Status": "creating",
 "IntegrationArn": "arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "Errors": [],
 "ResponseMetadata": {
 "RetryAttempts": 0,
 "HTTPStatusCode": 200,
 "RequestId": "132cbe27-fd10-4f0a-aacb-b68f10bb2bfb",
 "HTTPHeaders": {
 "x-amzn-requestid": "132cbe27-fd10-4f0a-aacb-b68f10bb2bfb",
 "date": "Sat, 24 Aug 2024 05:44:08 GMT",
 "content-length": "934",
 "content-type": "text/xml"
 }
 },
 "Tags": [],
 "CreateTime": "2024-08-24T05:44:08.573Z",
 "KMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
 "AdditionalEncryptionContext": {},
 "TargetArn": "arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "IntegrationName": "ddb-integration",
 "SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/books"
}`

```

The following example creates an integration using a customer managed key for encryption.
Before creating the integration:

- Create a customer managed key (called “CMCMK” in the example) in the same account
  (called “AccountA” in the example) at the source DynamoDB table.
- Ensure that the user/role (called “RoleA” in the example) is being used to
  create the integration has `kms:CreateGrant` and
  `kms:DescribeKey` permissions on this KMS key.
- Add the following to the key policy.

```
{
    "Sid": "Enable RoleA to create grants with key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "`RoleA-ARN`"
    },
    "Action": "kms:CreateGrant",
    "Resource": "*",
    "Condition": {
        // Add "StringEquals" condition if you plan to provide additional encryption context
        // for the zero-ETL integration. Ensure that the key-value pairs added here match
        // the key-value pair you plan to use while creating the integration.
        // Remove this if you don't plan to use additional encryption context
        "StringEquals": {
            "kms:EncryptionContext:`context-key1`": "`context-value1`"
        },
        "ForAllValues:StringEquals": {
            "kms:GrantOperations": [
                "Decrypt",
                "GenerateDataKey",
                "CreateGrant"
            ]
        }
    }
},
{
    "Sid": "Enable RoleA to describe key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "`RoleA-ARN`"
    },
    "Action": "kms:DescribeKey",
    "Resource": "*"
},
{
    "Sid": "Allow use by RS SP",
    "Effect": "Allow",
    "Principal": {
        "Service": "redshift.amazonaws.com"
           },
    "Action": "kms:CreateGrant",
    "Resource": "*"
}
```

```
`aws redshift create-integration \
--integration-name ddb-integration \
--source-arn arn:aws:dynamodb:us-east-1:123456789012:table/books \
--target-arn arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
--kms-key-id arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333 \
--additional-encryption-context key33=value33 // This matches the condition in the key policy.`
          `{
 "IntegrationArn": "arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "IntegrationName": "ddb-integration",
 "SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/books",
 "SourceType": "dynamodb",
 "TargetArn": "arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "Status": "creating",
 "Errors": [],
 "CreateTime": "2024-10-02T18:29:26.710Z",
 "KMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
 "AdditionalEncryptionContext": {
 "key33": "value33"
 },
 "Tags": []
}`

```

## IAM policy to work with DynamoDB

zero-ETL integrations

When creating zero-ETL integrations, your sign in credentials must have permission to on both
DynamoDB and Amazon Redshift actions and also on the resources involved as sources and targets of the
integration. Following is a example that demonstrates the minimum permissions
required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:ListTables"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetResourcePolicy",
 "dynamodb:PutResourcePolicy",
 "dynamodb:UpdateContinuousBackups"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/my-ddb-table"
 ]
 },
 {
 "Sid": "AllowRedshiftDescribeIntegration",
 "Effect": "Allow",
 "Action": [
 "redshift:DescribeIntegrations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowRedshiftCreateIntegration",
 "Effect": "Allow",
 "Action": "redshift:CreateIntegration",
 "Resource": "arn:aws:redshift:`us-east-1`:`111122223333`:integration:*"
 },
 {
 "Sid": "AllowRedshiftModifyDeleteIntegration",
 "Effect": "Allow",
 "Action": [
 "redshift:ModifyIntegration",
 "redshift:DeleteIntegration"
 ],
 "Resource": "arn:aws:redshift:`us-east-1`:`111122223333`:integration:`<uuid>`"
 },
 {
 "Sid": "AllowRedshiftCreateInboundIntegration",
 "Effect": "Allow",
 "Action": "redshift:CreateInboundIntegration",
 "Resource": "arn:aws:redshift:`us-east-1`:`111122223333`:namespace:`<uuid>`"
 }
 ]
}`

```

## Encrypting DynamoDB integrations with a

customer managed key

If you specify a custom KMS key rather than an AWS owned key when you create a
DynamoDB zero-ETL integration, the key policy must provide the Amazon Redshift service principal access to
the `CreateGrant` action. In addition, it must allow the requester account or
role permission to run the `DescribeKey` and `CreateGrant`
actions.

The following sample key policy statements demonstrate the permissions required in
your policy. Some examples include context keys to further reduce the scope of
permissions.

The following policy statement allows the requester account or role to retrieve
information about a KMS key.

```
{
   "Effect":"Allow",
   "Principal":{
      "AWS":"arn:aws:iam::`{account-ID}`:role/`{role-name}`"
   },
   "Action":"kms:DescribeKey",
   "Resource":"*"
}
```

The following policy statement allows the requester account or role to add a
grant to a KMS key. The [`kms:ViaService`](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service") condition key limits use of the KMS key
to requests from Amazon Redshift.

```
{
   "Effect":"Allow",
   "Principal":{
      "AWS":"arn:aws:iam::`{account-ID}`:role/`{role-name}`"
   },
   "Action":"kms:CreateGrant",
   "Resource":"*",
   "Condition":{
      "StringEquals":{
         "kms:EncryptionContext:`{context-key}`":"`{context-value}`",
         "kms:ViaService":"redshift.`{region}`.amazonaws.com"
      },
      "ForAllValues:StringEquals":{
         "kms:GrantOperations":[
            "Decrypt",
            "GenerateDataKey",
            "CreateGrant"
         ]
      }
   }
}
```

The following policy statement allows the Amazon Redshift service principal to add a grant
to a KMS key.

```
{
   "Effect":"Allow",
   "Principal":{
      "Service":"redshift.amazonaws.com"
   },
   "Action":"kms:CreateGrant",
   "Resource":"*",
   "Condition":{
      "StringEquals":{
         "kms:EncryptionContext:`{context-key}`":"`{context-value}`",
         "aws:SourceAccount":"`{account-ID}`"
      },
      "ForAllValues:StringEquals":{
         "kms:GrantOperations":[
            "Decrypt",
            "GenerateDataKey",
            "CreateGrant"
         ]
      },
      "ArnLike":{
         "aws:SourceArn":"arn:aws:*:`{region}`:`{account-ID}`:integration:*"
      }
   }
}
```

For more information, see [Creating a key policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") in the _AWS Key Management Service Developer
Guide_.

## Encryption context

When you encryption a zero-ETL integration, you can add key-value pairs as an
**Additional encryption context**. You might want to add these
key-value pairs to add additional contextual information about the data being
replicated. For more information, see [Encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md") in
the _AWS Key Management Service Developer Guide_.

Amazon Redshift adds the following encryption context pairs in addition to any that you
add:

- `aws:redshift:integration:arn` - `IntegrationArn`
- `aws:servicename:id` - `Redshift`

This reduces the overall number of pairs that you can add from 8 to 6, and
contributes to the overall character limit of the grant constraint. For more
information, see [Using grant constraints](../../../kms/latest/developerguide/create-grant-overview.md#grant-constraints "../../../kms/latest/developerguide/create-grant-overview.md#grant-constraints") in the _AWS Key Management Service Developer
Guide_.
