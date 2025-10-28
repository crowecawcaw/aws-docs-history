# Example SCPs for Amazon Elastic Compute Cloud

(Amazon EC2)

###### Topics

- [Require Amazon EC2 instances to use a specific type](#example-ec2-1 "#example-ec2-1")
- [Prevent launching EC2 instances without IMDSv2](#example-ec2-2 "#example-ec2-2")
- [Prevent disabling of default Amazon EBS encryption](#example-ec2-3 "#example-ec2-3")
- [Prevent creating and attaching non-gp3 volumes](#example-ec2-4 "#example-ec2-4")

## Require Amazon EC2 instances to use a specific type

With this SCP, any instance launches not using the `t2.micro` instance type
are denied.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RequireMicroInstanceType",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:*:*:instance/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "ec2:InstanceType": "t2.micro"
        }
      }
    }
  ]
}
```

## Prevent launching EC2 instances without IMDSv2

The following policy restricts all users from launching EC2 instances without
IMDSv2.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringNotEquals": {
          "ec2:MetadataHttpTokens": "required"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "NumericGreaterThan": {
          "ec2:MetadataHttpPutResponseHopLimit": "2"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "NumericLessThan": {
          "ec2:RoleDelivery": "2.0"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "ec2:ModifyInstanceMetadataOptions",
      "Resource": "*"
    }
  ]
}

```

The following policy restricts all users from launching EC2 instances without IMDSv2
but allows specific IAM identities to modify instance metadata options.

```
[
  {
    "Effect": "Deny",
    "Action": "ec2:RunInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*",
    "Condition": {
      "StringNotEquals": {
        "ec2:MetadataHttpTokens": "required"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": "ec2:RunInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*",
    "Condition": {
      "NumericGreaterThan": {
        "ec2:MetadataHttpPutResponseHopLimit": "2"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
      "NumericLessThan": {
        "ec2:RoleDelivery": "2.0"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": "ec2:ModifyInstanceMetadataOptions",
    "Resource": "*",
    "Condition": {
      "ArnNotLike": {
        "aws:PrincipalARN": [
          "arn:aws:iam::{ACCOUNT_ID}:{RESOURCE_TYPE}/{RESOURCE_NAME}"
        ]
      }
    }
  }
]
```

## Prevent disabling of default Amazon EBS encryption

The following policy restricts all users from disabling the default Amazon EBS Encryption.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:DisableEbsEncryptionByDefault"
      ],
      "Resource": "*"
    }
  ]
}

```

## Prevent creating and attaching non-gp3 volumes

The following policy restricts all users from creating or attaching any Amazon EBS volumes that are not of the gp3 volume type.
For more information, see [Amazon EBS volume types](../../../ebs/latest/userguide/ebs-volume-types.md "../../../ebs/latest/userguide/ebs-volume-types.md").

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyCreationAndAttachmentOfNonGP3Volumes",
      "Effect": "Deny",
      "Action": [
        "ec2:AttachVolume",
        "ec2:CreateVolume",
        "ec2:RunInstances"
      ],
      "Resource": "arn:aws:ec2:*:*:volume/*",
      "Condition": {
        "StringNotEquals": {
          "ec2:VolumeType": "gp3"
        }
      }
    }
  ]
}
```

This can help enforce a standardized volume configuration across an organization.

###### Volume type modifications are not prevented

You cannot restrict the action of modifying an existing gp3 volume to an Amazon EBS volume of another type using SCPs.
For example, this SCP would not prevent you from modifying an existing gp3 volume to a gp2 volume.
This is because the condition key `ec2:VolumeType`
checks the volume type before it is modified.
