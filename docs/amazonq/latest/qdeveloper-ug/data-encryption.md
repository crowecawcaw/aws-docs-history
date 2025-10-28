# Data encryption in Amazon Q Developer

This topic provides information specific to Amazon Q Developer about encryption in transit and
encryption at rest.

## Encryption in transit

All communication between customers and Amazon Q and between Amazon Q and its downstream
dependencies is protected using TLS 1.2 or higher connections.

## Encryption at rest

Amazon Q stores data at rest using Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3). The data at rest is
encrypted using AWS encryption solutions by default. Amazon Q encrypts your data using
AWS owned encryption keys from AWS Key Management Service (AWS KMS). You don’t have to take any
action to protect the AWS managed keys that encrypt your data. For more information,
see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk")
in the _AWS Key Management Service Developer Guide_.

For IAM Identity Center workforce users subscribed to Amazon Q Developer Pro, administrators can set up encryption with customer
managed KMS keys for data at rest for the following features:

- Chat in the AWS console
- Diagnosing AWS console errors
- Customizations
- Agents in the IDE

You can only encrypt data with a customer managed key for the listed features of
Amazon Q in the AWS console and the IDE. Your conversations with Amazon Q on the AWS
website, AWS Documentation pages, and in chat applications are only
encrypted with AWS-owned keys.

Customer managed keys are KMS keys in your AWS account that you create, own, and
manage to directly control access to your data by controlling access to the KMS key.
Only symmetric keys are supported. For information on creating your own KMS key, see
[Creating
keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer
Guide_.

When you use a customer managed key, Amazon Q Developer makes use of KMS grants, allowing
authorized users, roles, or applications to use a KMS key. When an Amazon Q Developer
administrator chooses to use a customer managed key for encryption during configuration,
a grant is created for them. This grant is what allows the end user to use the
encryption key for data encryption at rest. For more information on grants, see [Grants in
AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md").

If you change the KMS key used to encrypt chats with Amazon Q in the AWS console, you
must start a new conversation to begin using the new key to encrypt your data. Any
conversations that were encrypted with the previous key won’t be retained, and
only future conversations will be encrypted with the updated key. If you want to
maintain your conversations from a previous encryption method, you can revert to
the key you were using during those conversations. If you change the KMS key used to
encrypt diagnosing console error sessions, you must start a new diagnose session to
being using the new key to encrypt your data.

## Using customer managed KMS keys

After creating a customer managed KMS key, an Amazon Q Developer administrator must provide
the key in the Amazon Q Developer console to use it to encrypt data. For information on adding
the key in the Amazon Q Developer console, see [Managing the encryption method in Amazon Q Developer](manage-encryption.md "manage-encryption.md").

To set up a customer managed key to encrypt data in Amazon Q Developer, administrators need
permissions to use AWS KMS. The required KMS permissions are included in the example IAM
policy, [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").

To use features that are encrypted with a customer managed key, users need
permissions to allow Amazon Q to access the customer managed key. For a policy that grants
the needed permissions, see [Allow Amazon Q access to
customer managed keys](id-based-policy-examples-users.md#id-based-policy-examples-allow-q-access-encryption "id-based-policy-examples-users.md#id-based-policy-examples-allow-q-access-encryption").

If you see an error related to KMS grants while using Amazon Q Developer, you likely need to
update your permissions to allow Amazon Q to create grants. To automatically configure the
needed permissions, go to the Amazon Q Developer console and choose **Update
permissions** in the banner at the top of the page.
