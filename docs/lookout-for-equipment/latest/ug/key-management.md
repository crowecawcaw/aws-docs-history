On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Key management

Amazon Lookout for Equipment encrypts your data using one of the following types of keys:

- An AWS owned key. This is the default.
- A customer managed key. You can create the key when you create an
  Amazon Lookout for Equipment dataset, model, or inference, or you can create the key using
  the AWS Key Management Service (AWS KMS) console. Choose a symmetric customer managed key,
  Amazon Lookout for Equipment doesn't support asymmetric customer managed keys. For more information, see
  [Using symmetric and asymmetric keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the _AWS Key Management Service
  Developer Guide_.
  When you create a key using the AWS KMS console, you can give the key the following
  policy, which enables users or roles to use the key with Amazon Lookout for Equipment. For more
  information, see [Using key policies
  in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

```

{
    "Effect": "Allow",
    "Sid": "Allow to use the key with Amazon Lookout for Equipment",
    "Principal": {
        "AWS": "IAM USER OR ROLE ARN"
    },
    "Action": [
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:RetireGrant"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "lookoutequipment.`Region`.amazonaws.com"
            ]
        }
    }
},
{
    "Effect": "Allow",
    "Sid": "Allow to view the key in the console"
    "Principal": {
        "AWS": "IAM USER OR ROLE ARN"
    },
    "Action": [
        "kms:DescribeKey"
    ],
    "Resource": "*"
},
{
    "Effect": "Allow",
    "Sid": "Allow inference scheduler pass-in role to encrypt output data"
    "Principal": {
        "AWS": "INFERENCE SCHEDULER PASS-IN ROLE ARN"
    },
    "Action": [
        "kms:GenerateDataKey"
    ],
    "Resource": "*"
}

```
