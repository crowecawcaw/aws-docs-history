Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# AWS KMS and data encryption in

Amazon Monitron

Amazon Monitron encrypts your data and project information using one of two types
of keys through AWS Key Management Service (AWS KMS). You can choose one of the following:

- An AWS owned key. This is the default encryption key and is used if you
  do not choose **Custom encryption settings** when setting
  up your project.
- A customer managed CMK. You can use an existing key in your AWS account
  or create a key in the AWS KMS console or using the API. If you're using an
  existing key, you choose **Choose an AWS KMS key** and then
  either choose a key from the list of AWS KMS keys, or enter the Amazon
  Resource Name (ARN) of another key. If you want to create a new key, you
  choose **Create an AWS KMS key**. For more information, see
  [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer
  Guide_.
  When using AWS KMS to encrypt your data, keep the following in mind:

- Your data is encrypted at rest in the Cloud in Amazon S3 and Amazon DynamoDB.
- When data is encrypted using an AWS owned CMK, Amazon Monitron uses a
  separate CMK for each customer.
- IAM users must have the required permissions to call the AWS KMS API
  operations connected with Amazon Monitron. Amazon Monitron includes the following permissions in
  its managed policy for console use.

```
{
                 "Effect": "Allow",
                 "Action": [
                         "kms:ListKeys",
                         "kms:DescribeKey",
                         "kms:ListAliases",
                         "kms:CreateGrant"
                 ],
                 "Resource": "*"
         },

```

For more information, see [Using IAM Policies with AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md") in the _AWS Key Management Service
Developer Guide_.

- If you delete or disable your CMK, you won't be able to access the data.
  For more information, see [Deleting AWS KMS keys](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md") in the _AWS Key Management Service Developer
  Guide_.
