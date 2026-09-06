

# Use encrypted data sources with CMKs
<a name="encrypted-data-cmk"></a>

This topic contains information about setting up and connecting App Studio to data sources that are encrypted using a [AWS KMS Customer Managed Key (CMK)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk).

**Contents**
+ [Using encrypted managed data storage tables](#encrypted-data-cmk-managed-data)
+ [Using encrypted DynamoDB tables](#encrypted-data-cmk-ddb)

## Using encrypted managed data storage tables
<a name="encrypted-data-cmk-managed-data"></a>

Use the following procedure to encrypt the DynamoDB tables used by managed storage entities in your App Studio apps. For more information about managed data entities, see [Managed data entities in AWS App Studio](managed-data-entities.md).

**To use encrypted managed data storage tables**

1. If necessary, create the managed data entities in an application in App Studio. For more information, see [Creating an entity with an App Studio managed data source](data-entities-create.md#data-entities-create-managed-data-source).

1. Add a policy statement with permissions to encrypt and decrypt table data with your CMK to the `AppStudioManagedStorageDDBAccess` IAM role by performing the following steps:

   1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
**Important**  
You must use the same account used to create your App Studio instance.

   1. In the navigation pane of the IAM console, choose **Roles**.

   1. Choose `AppStudioManagedStorageDDBAccess`.

   1. In **Permissions policies**, choose **Add permissions** and then choose **Create inline policy**.

   1. Choose **JSON** and replace the contents with the following policy, replacing the following:
      + Replace {{111122223333}} with the AWS account number of the account used to set up the App Studio instance, listed as **AWS account ID** in the account settings in your App Studio instance.
      + Replace {{CMK\_id}} with CMK ID. To find it, see [Find the key ID and key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html).

1. Encrypt the DynamoDB tables that are used by your App Studio managed data entities by performing the following steps:

   1. Open the Amazon DynamoDB console at [https://console.aws.amazon.com/dynamodbv2/](https://console.aws.amazon.com/dynamodbv2/).

   1. Choose the table you want to encrypt. You can find the table name in the **Connection** tab of the corresponding entity in App Studio.

   1. Choose **Additional settings**.

   1. In **Encryption**, choose **Manage encryption**.

   1. Choose **Stored in your account, and owned and managed by you** and select your CMK.

1. Test your changes by republishing your app and ensuring that reading and writing data works in both the Testing and Production environments, and using this table in another entity works as expected.
**Note**  
Any newly added managed data entities use the DynamoDB managed key by default, and must be updated to using the CMK by following the previous steps.

## Using encrypted DynamoDB tables
<a name="encrypted-data-cmk-ddb"></a>

Use the following procedure to configure encrypted DynamoDB tables to be used in your App Studio apps.

**To use encrypted DynamoDB tables**

1. Follow the instructions in [Step 1: Create and configure DynamoDB resources](connectors-dynamodb.md#connectors-dynamodb-create-resources) with the following changes:

   1. Configure your tables to be encrypted. For more information, see [Specifying the encryption key for a new table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html#encryption.tutorial-creating) in the *Amazon DynamoDB Developer Guide*.

1. Follow the instructions in [Step 2: Create an IAM policy and role with appropriate DynamoDB permissions](connectors-dynamodb.md#connectors-dynamodb-iam), and then update the permission policy on the new role by adding a new policy statement with permits it to encrypt and decrypt table data using your CMK by performing the following steps:

   1. If necessary, navigate to your role in the IAM console.

   1. In **Permissions policies**, choose **Add permissions** and then choose **Create inline policy**.

   1. Choose **JSON** and replace the contents with the following policy, replacing the following:
      + Replace {{team\_account\_id}} with your App Studio team ID, which can be found in your account settings.
      + Replace {{CMK\_id}} with CMK ID. To find it, see [Find the key ID and key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html).

1. Create the connector by following the instructions in [Create DynamoDB connector](connectors-dynamodb.md#connectors-dynamodb-create-connector) and using the role you created earlier.

1. Test the configuration by publishing an app that uses the DynamoDB connector and table to Testing or Production. Ensure that reading and writing data works, and using this table to create another entity works as well.
**Note**  
When any new DynamoDB tables are created, you must configure them to be encrypted using a CMK by following the previous steps.