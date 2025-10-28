# Examples: Set up an AWS Control Tower landing zone with APIs only

This walkthrough of examples is a companion document. For explanations, caveats, and more information, see [Getting started with AWS Control Tower using APIs](getting-started-apis.md "getting-started-apis.md").

**Prerequisites**

Before creating an AWS Control Tower landing zone, you must create an organization, two shared accounts, and some IAM roles. This walkthrough tutorial includes these steps, with example CLI commands and output.

**Step 1. Create the organization and two required accounts.**

```

aws organizations create-organization --feature-set ALL
aws organizations create-account --email example+log@example.com --account-name "Log archive account"
aws organizations create-account --email example+aud@example.com --account-name "Audit account"

```

**Step 2. Create the required IAM roles.**

`AWSControlTowerAdmin`

```
cat <<EOF >controltower_trust.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "controltower.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
aws iam create-role --role-name AWSControlTowerAdmin --path /service-role/ --assume-role-policy-document file://controltower_trust.json
cat <<EOF >ct_admin_role_policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeAvailabilityZones",
            "Resource": "*"
        }
    ]
}
EOF
aws iam put-role-policy --role-name AWSControlTowerAdmin --policy-name AWSControlTowerAdminPolicy --policy-document file://ct_admin_role_policy.json
aws iam attach-role-policy --role-name AWSControlTowerAdmin --policy-arn arn:aws:iam::aws:policy/service-role/AWSControlTowerServiceRolePolicy
```

`AWSControlTowerCloudTrailRole`

```
cat <<EOF >cloudtrail_trust.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudtrail.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
aws iam create-role --role-name AWSControlTowerCloudTrailRole --path /service-role/ --assume-role-policy-document file://cloudtrail_trust.json
cat <<EOF >cloudtrail_role_policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "logs:CreateLogStream",
            "Resource": "arn:aws:logs:*:*:log-group:aws-controltower/CloudTrailLogs:*",
            "Effect": "Allow"
        },
        {
            "Action": "logs:PutLogEvents",
            "Resource": "arn:aws:logs:*:*:log-group:aws-controltower/CloudTrailLogs:*",
            "Effect": "Allow"
        }
    ]
}
EOF
aws iam put-role-policy --role-name AWSControlTowerCloudTrailRole --policy-name AWSControlTowerCloudTrailRolePolicy --policy-document file://cloudtrail_role_policy.json
```

`AWSControlTowerStackSetRole`

```
cat <<EOF >cloudformation_trust.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudformation.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
aws iam create-role --role-name AWSControlTowerStackSetRole --path /service-role/ --assume-role-policy-document file://cloudformation_trust.json
cat <<EOF >stackset_role_policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/AWSControlTowerExecution"
            ],
            "Effect": "Allow"
        }
    ]
}
EOF
aws iam put-role-policy --role-name AWSControlTowerStackSetRole --policy-name AWSControlTowerStackSetRolePolicy --policy-document file://stackset_role_policy.json
```

`AWSControlTowerConfigAggregatorRoleForOrganizations`

```
cat <<EOF >config_trust.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "config.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
aws iam create-role --role-name AWSControlTowerConfigAggregatorRoleForOrganizations --path /service-role/ --assume-role-policy-document file://config_trust.json
aws iam attach-role-policy --role-name AWSControlTowerConfigAggregatorRoleForOrganizations --policy-arn arn:aws:iam::aws:policy/service-role/AWSConfigRoleForOrganizations
```

**Step 3. Get account IDs and generate the landing zone manifest file.**

The first two commands in the following example store the account IDs for the accounts you created in **Step 1** into variables. These variables then help generate the landing zone manifest file.

```
sec_account_id=$(aws organizations list-accounts | jq -r '.Accounts[] | select(.Name == "Audit account") | .Id')
log_account_id=$(aws organizations list-accounts | jq -r '.Accounts[] | select(.Name == "Log archive account") | .Id')

cat <<EOF >landing_zone_manifest.json
{
   "governedRegions": ["us-west-1", "us-west-2"],
   "organizationStructure": {
       "security": {
           "name": "Security"
       },
       "sandbox": {
           "name": "Sandbox"
       }
   },
   "centralizedLogging": {
        "accountId": "$log_account_id",
        "configurations": {
            "loggingBucket": {
                "retentionDays": 60
            },
            "accessLoggingBucket": {
                "retentionDays": 60
            }
        },
        "enabled": true
   },
   "securityRoles": {
        "accountId": "$sec_account_id"
   },
   "accessManagement": {
        "enabled": true
   }
}
EOF
```

**Step 4. Create the landing zone with the latest version.**

You must set up the landing zone with the manifest file and the latest version. This example shows version 3.3.

```
aws --region us-west-1 controltower create-landing-zone --manifest file://landing_zone_manifest.json --landing-zone-version 3.3
```

The output will contain an **arn** and an **operationIdentifier**, as shown in the example that follows.

```
{
    "arn": "arn:aws:controltower:us-west-1:0123456789012:landingzone/4B3H0ULNUOL2AXXX",
    "operationIdentifier": "16bb47f7-b7a2-4d90-bc71-7df4ca1201xx"
}
```

**Step 5. (Optional) Track the status of your landing zone creation operation, by setting up a loop.**

To track status, use the **operationIdentifier** from the previous `create-landing-zone` command's output.

```
aws --region us-west-1 controltower get-landing-zone-operation --operation-identifier 16bb47f7-b7a2-4d90-bc71-7df4ca1201xx
```

Sample status output:

```
{
    "operationDetails": {
        "operationType": "CREATE",
        "startTime": "2024-02-28T21:49:31Z",
        "status": "IN_PROGRESS"
    }
}
```

You can use the following example script to help you set up a loop, which reports the operation's status over and over, like a log file. Then you don't need to keep entering the command.

```
while true; do echo "$(date) $(aws --region us-west-1 controltower get-landing-zone-operation --operation-identifier 16bb47f7-b7a2-4d90-bc71-7df4ca1201xx | jq -r .operationDetails.status)"; sleep 15; done
```

**To show detailed information about your landing zone**

_Step 1. Find the ARN of the landing zone_

```
aws --region us-west-1 controltower list-landing-zones
```

Output will include the identifier of the landing zone, as shown in the following example of output.

```
{
    "landingZones": [
        {
            "arn": "arn:aws:controltower:us-west-1:123456789012:landingzone/4B3H0ULNUOL2AXXX"
        }
    ]
}
```

_Step 2. Get the information_

```
aws --region us-west-1 controltower get-landing-zone --landing-zone-identifier arn:aws:controltower:us-west-1:123456789012:landingzone/4B3H0ULNUOL2AXXX
```

Here's an example of the kind of output you may see:

```
{
    "landingZone": {
        "arn": "arn:aws:controltower:us-west-1:123456789012:landingzone/4B3H0ULNUOL2AXXX",
        "driftStatus": {
            "status": "IN_SYNC"
        },
        "latestAvailableVersion": "3.3",
        "manifest": {
            "accessManagement": {
                "enabled": true
            },
            "securityRoles": {
                "accountId": "9750XXXX4444"
            },
            "governedRegions": [
                "us-west-1",
                "us-west-2"
            ],
            "organizationStructure": {
                "sandbox": {
                    "name": "Sandbox"
                },
                "security": {
                    "name": "Security"
                }
            },
            "centralizedLogging": {
                "accountId": "012345678901",
                "configurations": {
                    "loggingBucket": {
                        "retentionDays": 60
                    },
                    "accessLoggingBucket": {
                        "retentionDays": 60
                    }
                },
                "enabled": true
            }
        },
        "status": "ACTIVE",
        "version": "3.3"
    }
}
```

**Step 6. (Optional) Call the `ListLandingZoneOperations` API to view the status of any operations that change your landing zone.**

To track the status of any landing zone operation, you can call the [ListLandingZoneOperations](lz-api-examples-short.md#list-lz-operations-api-examples "lz-api-examples-short.md#list-lz-operations-api-examples") API.
