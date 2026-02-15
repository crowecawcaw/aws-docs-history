# Assign resources with AWS CLI

## Filter by services or resource types

Resource selection is based on service names and resource types. The method of
resource selection determines whether a resource is included in the backup. This inclusion
depends on service names, resource types, and opt-in settings.

###### Selection by service name

When you specify only a service name in the resource selection, the backup inclusion
depends on the opt-in setting for the underlying resource types. For example, with
`arn:aws:ec2:*`, EC2 instances will be included in the backup only if the
opt-in setting for the EC2 resource type is enabled.

###### Selection by resource type

If you specify the resource selection directly with the resource type, it will be
included in the backup regardless of the opt-in setting for that particular service. For
example, with `arn:aws:ec2:::instance/*`, EC2 instances will be backed up
regardless of the opt-in setting.

###### Shared resource types

When multiple resources share the same resource type, you need to enable opt-in
settings for specific resource types to initiate backups.

###### Example

Aurora and RDS Clusters share the ARN format: `arn:aws:rds:::cluster:*`.
To backup Aurora databases, you must enable the opt-in setting for Aurora.

FSx and FSx for OpenZFS share the ARN format
`arn:aws:fsx:::file-system/*`. Enable the respective opt-in settings to
backup these file systems.

## Use a JSON to define backup plan resource assignment

You can define a resource assignment in a JSON document.

You can specify conditions, tags, or resources to define what will be included in your
backup plan. For more information to help you determine which parameters to include, see
[`BackupSelection`](API_BackupSelection.md#Backup-Type-BackupSelection-ListOfTags "API_BackupSelection.md#Backup-Type-BackupSelection-ListOfTags").

This sample resource assignment assigns all Amazon EC2 instances to the backup plan
`BACKUP-PLAN-ID`:

```
{
  "BackupPlanId":"`BACKUP-PLAN-ID`",
  "BackupSelection":{
    "SelectionName":"resources-list-selection",
    "IamRoleArn":"arn:aws:iam::`ACCOUNT-ID`:role/`IAM-ROLE-ARN`",
    "Resources":[
      "arn:aws:ec2:*:*:instance/*"
    ]
  }
}
```

Assuming this JSON is stored as `backup-selection.json`, you can assign
these resources to your backup plan using the following CLI command:

```
aws backup create-backup-selection --cli-input-json file://`PATH-TO-FILE`/`backup-selection`.json
```

The following are example resource assignments, along with the corresponding JSON
document. To make this table easier for you to read, the examples omit the fields
`"BackupPlanId"`, `"SelectionName"`, and
`"IamRoleArn"`. The wildcard `*` represents zero or more
non-whitespace characters.

###### Example: Select all resources in my account

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ]
  }
}
```

###### Example: Select all resources in my account, but exclude EBS volumes

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ],
    "NotResources":[
      "arn:aws:ec2:*:*:volume/*"
    ]
  }
}
```

###### Example: Select all resources tagged with "backup":"true", but exclude EBS volumes

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ],
    "NotResources":[
      "arn:aws:ec2:*:*:volume/*"
    ],
    "Conditions":{
      "StringEquals":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"true"
        }
      ]
    }
  }
}
```

###### Important

RDS, Aurora, Neptune, and DocumentDB ARNs start with `arn:aws:rds:`.
Refine your selection with tags and conditional operators if you don't intend to include
all those types.

###### Example: Select all EBS volumes and RDS DB instances tagged with both "backup":"true" and "stage":"prod"

The Boolean arithmetic is similar to that in IAM policies, with those in
"Resources" combined using a Boolean OR and those in
`"Conditions"` combined with a Boolean AND.

The `"Resources"` expression `"arn:aws:rds:*:*:db:*"` only
selects RDS DB instances because there are no corresponding Aurora, Neptune, or
DocumentDB resources.

```
{
  "BackupSelection":{
    "Resources":[
      "arn:aws:ec2:*:*:volume/*",
      "arn:aws:rds:*:*:db:*"
    ],
    "Conditions":{
      "StringEquals":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"true"
        },
        {
          "ConditionKey":"aws:ResourceTag/stage",
          "ConditionValue":"prod"
        }
      ]
    }
  }
}
```

###### Example: Select all EBS volumes and RDS instances tagged with "backup":"true" but not "stage":"test"

```
{
  "BackupSelection":{
    "Resources":[
      "arn:aws:ec2:*:*:volume/*",
      "arn:aws:rds:*:*:db:*"
    ],
    "Conditions":{
      "StringEquals":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"true"
        }
      ],
      "StringNotEquals":[
        {
          "ConditionKey":"aws:ResourceTag/stage",
          "ConditionValue":"test"
        }
      ]
    }
  }
}
```

###### Example: Select all resources tagged with "key1" and a value which begins with "include" but not with "key2" and value that contains the word "exclude"

You can use the wildcard character at the start, end, and middle of a string. Note
the use of the wildcard character (\*) in `include*` and
`*exclude*` in the example above. You can also use the wildcard character
in the middle of a string as shown in the previous example,
`arn:aws:rds:*:*:db:*`.

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ],
    "Conditions":{
      "StringLike":[
        {
          "ConditionKey":"aws:ResourceTag/key1",
          "ConditionValue":"include*"
        }
      ],
      "StringNotLike":[
        {
          "ConditionKey":"aws:ResourceTag/key2",
          "ConditionValue":"*exclude*"
        }
      ]
    }
  }
}
```

###### Example: Select all resources tagged with "backup":"true" except FSx file systems and RDS, Aurora, Neptune, and DocumentDB resources

Items in `NotResources` are combined using the Boolean OR.

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ],
    "NotResources":[
      "arn:aws:fsx:*",
      "arn:aws:rds:*"
    ],
    "Conditions":{
      "StringEquals":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"true"
        }
      ]
    }
  }
}
```

###### Example: Select all resources tagged with a tag "backup" and any value

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ],
    "Conditions":{
      "StringLike":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"*"
        }
      ]
    }
  }
}
```

###### Example: Select all FSx file systems, the Aurora cluster "my-aurora-cluster", and all resources tagged with "backup":"true", except for resources tagged with "stage":"test"

```
{
  "BackupSelection":{
    "Resources":[
      "arn:aws:fsx:*",
      "arn:aws:rds:*:*:cluster:my-aurora-cluster"
    ],
    "ListOfTags":[
      {
        "ConditionType":"StringEquals",
        "ConditionKey":"backup",
        "ConditionValue":"true"
      }
    ],
    "Conditions":{
      "StringNotEquals":[
        {
          "ConditionKey":"aws:ResourceTag/stage",
          "ConditionValue":"test"
        }
      ]
    }
  }
}
```

###### Example: Select all resources tagged with tag "backup":"true" except for EBS volumes tagged with "stage":"test"

Use two CLI commands to create two selections to select this group of resources. The
first selection applies to all resources except for EBS volumes. The second selection
applies to EBS volumes.

```
{
  "BackupSelection":{
    "Resources":[
      "*"
    ],
    "NotResources":[
      "arn:aws:ec2:*:*:volume/*"
    ],
    "Conditions":{
      "StringEquals":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"true"
        }
      ]
    }
  }
}
```

```
{
  "BackupSelection":{
    "Resources":[
      "arn:aws:ec2:*:*:volume/*"
    ],
    "Conditions":{
      "StringEquals":[
        {
          "ConditionKey":"aws:ResourceTag/backup",
          "ConditionValue":"true"
        }
      ],
      "StringNotEquals":[
        {
          "ConditionKey":"aws:ResourceTag/stage",
          "ConditionValue":"test"
        }
      ]
    }
  }
}
```
