# Step 2: Launch your landing zone

The AWS Control Tower `CreateLandingZone` API requires a landing zone version and a _landing zone manifest file_ as input parameters.
You can use the AWS Control Tower landing zone manifest file to configure the
following features:

- [Optionally configure log retention](configure-log-retention.md "configure-log-retention.md")
- [Optionally self-manage AWS account access](select-idp.md "select-idp.md")
- [Optionally configure AWS CloudTrail trails](configure-org-trails.md "configure-org-trails.md")
- [Optionally configure
  AWS KMS keys](configure-kms-keys.md "configure-kms-keys.md")
  After compiling your manifest file, you're ready to create a new landing zone.

For more information about what's in the manifest file, see [View the details of your landing zone manifest file](lz-manifest-file.md "lz-manifest-file.md").

For more information about landing zone schemas that apply to the landing zone
manifest file, see [Landing zone
schemas](landing-zone-schemas.md "landing-zone-schemas.md").

###### Note

AWS Control Tower does not support the Region deny control when using APIs to configure and launch a landing zone. After
successfully launching your landing zone using APIs, you can use the AWS Control Tower console to [Configure the Region deny control](region-deny.md "region-deny.md").

1. Call the AWS Control Tower `CreateLandingZone` API. This API requires a
   landing zone version and a landing zone manifest file as input.

```
aws controltower create-landing-zone --landing-zone-version 3.3 --manifest "file://LandingZoneManifest.json"
```

For more detail about the contents of the _landing zone manifest file_, see [View the details of your landing zone manifest file](lz-manifest-file.md "lz-manifest-file.md").

The following example shows a **LandingZoneManifest.json** manifest, which includes settings for
governed Regions and centralized logging:

```
{
   "governedRegions": ["us-west-2","us-west-1"],
   "organizationStructure": {
       "security": {
           "name": "`CORE`"
       },
       "sandbox": {
           "name": "`Sandbox`"
       }
   },
   "centralizedLogging": {
        "accountId": "`222222222222`",
        "configurations": {
            "loggingBucket": {
                "retentionDays": 60
            },
            "accessLoggingBucket": {
                "retentionDays": 60
            },
            "kmsKeyArn": "`arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX`"
        },
        "enabled": true
   },
   "securityRoles": {
        "accountId": "`333333333333`"
   },
   "accessManagement": {
        "enabled": true
   }
}
```

###### Note

As shown in the example, the **AccountId**
for the `CentralizedLogging` and `SecurityRoles`
accounts must be different.

The following example shows a **LandingZoneManifest.json** manifest file, which includes settings
for backup and centralized logging:

```
{
        "landingZoneIdentifier": "`LANDING ZONE ARN`",
        "manifest": {
            "accessManagement": {
                "enabled": true
            },
            "securityRoles": {
                "accountId": "`333333333333`"
            },
            "backup": {
                "configurations": {
                    "centralBackup": {
                        "accountId": "`CENTRAL BACKUP ACCOUNT ID`"
                    },
                    "backupAdmin": {
                        "accountId": "`BACKUP MANAGER ACCOUNT ID`"
                    },
                    "kmsKeyArn": "`arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX`"
                },
                "enabled": true
            },
            "governedRegions": [
                "us-west-1"
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
                "accountId": "`222222222222`",
                "configurations": {
                    "loggingBucket": {
                        "retentionDays": 365
                    },
                    "accessLoggingBucket": {
                        "retentionDays": 3650
                    }
                },
                "enabled": true
            }
        },
        "version": "3.3"
}
```

**Output**:

```
{
   "arn": "arn:aws:controltower:us-west-2:123456789012:landingzone/1A2B3C4D5E6F7G8H",
   "operationIdentifier": "55XXXXXX-e2XX-41XX-a7XX-446XXXXXXXXX"
}
```

2. Call the `GetLandingZoneOperation` API to check the status of the `CreateLandingZone`
   operation. The `GetLandingZoneOperation` API returns a **status** of `SUCCEEDED`,
   `FAILED`, or `IN_PROGRESS`.

```
aws controltower get-landing-zone-operation --operation-identifier "55XXXXXX-eXXX-4XXX-aXXX-44XXXXXXXXXX"
```

**Output**:

```
{
    "operationDetails": {
        "operationType": "CREATE",
        "startTime": "Thu Nov 09 20:39:19 UTC 2023",
        "endTime": "Thu Nov 09 21:02:01 UTC 2023",
        "status": "SUCCEEDED"
    }
}
```

3. When the status returns as `SUCCEEDED`, you can call the `GetLandingZone`
   API to review the landing zone configuration.

```
aws controltower get-landing-zone --landing-zone-identifier "arn:aws:controltower:us-west-2:123456789123:landingzone/1A2B3C4D5E6F7G8H"
```

**Output**:

```
{
    "landingZone": {
        "arn": "arn:aws:controltower:us-west-2:123456789012:landingzone/1A2B3C4D5E6F7G8H",
        "driftStatus": {
            "status": "IN_SYNC"
        },
        "latestAvailableVersion": "3.3",
        "manifest": {
            "accessManagement": {
                "enabled": true
            },
            "securityRoles": {
                "accountId": "333333333333"
            },
            "governedRegions": [
                "us-west-1",
                "eu-west-3",
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
                "accountId": "222222222222",
                "configurations": {
                    "loggingBucket": {
                        "retentionDays": 60
                    },
                    "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX",
                    "accessLoggingBucket": {
                        "retentionDays": 60
                    }
                },
                "enabled": true
            }
        },
        "status": "PROCESSING",
        "version": "3.3"
    }
}
```
