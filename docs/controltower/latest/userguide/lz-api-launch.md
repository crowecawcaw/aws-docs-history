

# Step 2: Launch your landing zone using the AWS Control Tower APIs

 You can use AWS Control Tower APIs to launch your landing zone. This section describes how to create the required *landing zone manifest file* and use it with the `CreateLandingZone` API operation. 

## Creating the manifest file
<a name="w2aac15c17c17b5"></a>

 The manifest file is a JSON document that specifies your landing zone configuration. With landing zone version 4.0, many components are now optional, allowing for a more flexible deployment. 

### Manifest Structure
<a name="w2aac15c17c17b5b5"></a>

Below is the complete structure of the manifest file with all available configurations:

```json
{
    "accessManagement": {
        "enabled": true    // Required - Controls IAM Identity Center integration
    },
    "backup": {
        "enabled": true,   // Required - Controls AWS Backup integration
        "configurations": {
            "backupAdmin": {
                "accountId": {{"111122223333"}}    // Backup administrator account
            },
            "centralBackup": {
                "accountId": {{"111122224444"}}    // Central backup account
            },
            "kmsKeyArn": {{"arn:aws:kms:region:account-id:key/key-id"}}
        }
    },
    "centralizedLogging": {
        "accountId": {{"111122225555"}},    // Log archive account
        "enabled": true,                // Required - Controls centralized logging
        "configurations": {
            "accessLoggingBucket": {
                "retentionDays": 365    // Minimum value: 1
            },
            "loggingBucket": {
                "retentionDays": 365    // Minimum value: 1
            },
            "kmsKeyArn": {{"arn:aws:kms:region:account-id:key/key-id"}}
        }
    },
    "config": {
        "accountId": {{"111122226666"}},    // Config aggregator account
        "enabled": true,                // Required - Controls AWS Config integration
        "configurations": {
            "accessLoggingBucket": {
                "retentionDays": 365    // Minimum value: 1
            },
            "loggingBucket": {
                "retentionDays": 365    // Minimum value: 1
            },
            "kmsKeyArn": {{"arn:aws:kms:region:account-id:key/key-id"}}
        }
    },
    "governedRegions": [               // Optional - List of regions to govern
        "us-east-1",
        "us-west-2"
    ],
    "securityRoles": {
        "enabled": true,               // Required - Controls security roles creation
        "accountId": "{{"111122226666"}}    // Security/Audit account
    }
}
```

### Important Notes
<a name="w2aac15c17c17b5b7"></a>
+ All `enabled` flags are required in the manifest.
+ If you disable AWS Config integration (`"config.enabled": false`), you must also disable the following integrations:
  + Security Roles (`"securityRoles.enabled": false`)
  + Access Management (`"accessManagement.enabled": false`)
  + Backup (`"backup.enabled": false`)
+ Account IDs must be valid 12-digit AWS account IDs.
+ KMS key ARNs must be valid AWS KMS key ARNs.
+ Retention days must be at least 1.

### Example: Using a custom logging bucket
<a name="lz-api-custom-logging-bucket"></a>

To send logs to an existing Amazon S3 bucket instead of a bucket that AWS Control Tower creates and manages, replace the `loggingBucket` and `accessLoggingBucket` objects with a `customLoggingBucket` object in the `centralizedLogging` integration, the `config` integration, or both. The `bucketArn` identifies the bucket, and the `bucketAccountId` identifies the account that owns it. The `kmsKeyArn` fields identify the AWS KMS keys used for encryption. The following example uses a custom logging bucket for both integrations:

```json
{
    "accessManagement": {
        "enabled": true
    },
    "backup": {
        "enabled": true,
        "configurations": {
            "backupAdmin": {
                "accountId": {{"444455556666"}}
            },
            "centralBackup": {
                "accountId": {{"555555555555"}}
            },
            "kmsKeyArn": {{"arn:aws:kms:region:account-id:key/key-id"}}
        }
    },
    "centralizedLogging": {
        "accountId": {{"111122223333"}},
        "enabled": true,
        "configurations": {
            "customLoggingBucket": {
                "bucketArn": {{"arn:aws:s3:::amzn-s3-demo-logging-bucket"}},
                "bucketAccountId": {{"111122223333"}}
            },
            "kmsKeyArn": {{"arn:aws:kms:region:account-id:key/key-id"}}
        }
    },
    "config": {
        "accountId": {{"777788889999"}},
        "enabled": true,
        "configurations": {
            "customLoggingBucket": {
                "bucketArn": {{"arn:aws:s3:::amzn-s3-demo-config-bucket"}},
                "bucketAccountId": {{"111122223333"}}
            },
            "kmsKeyArn": {{"arn:aws:kms:region:account-id:key/key-id"}}
        }
    },
    "governedRegions": [
        "us-east-1",
        "us-west-2"
    ],
    "securityRoles": {
        "enabled": true,
        "accountId": {{"777788889999"}}
    }
}
```

You can't use `customLoggingBucket` together with `loggingBucket` or `accessLoggingBucket` in the same integration. For more information, see [Bring your own Amazon S3 bucket for log delivery](custom-logging-bucket.md).

## Using the CreateLandingZone API
<a name="w2aac15c17c17b7"></a>

To create your landing zone using the API:

```bash
aws controltower create-landing-zone --landing-zone-version 4.0 --manifest file://manifest.json
```

The API will return a landing zone operation ID that you can use to track the progress of your landing zone creation. Sample response:

```json
{
    "arn": "arn:aws:controltower:us-west-2:123456789012:landingzone/1A2B3C4D5E6F7G8H",
    "operationIdentifier": "55XXXXXX-e2XX-41XX-a7XX-446XXXXXXXXX"
}
```

You can monitor the operation status using `GetLandingZoneOperation` API which returns a **status** of `SUCCEEDED`, `FAILED`, or `IN_PROGRESS`:

```bash
aws controltower get-landing-zone-operation --operation-identifier "55XXXXXX-eXXX-4XXX-aXXX-44XXXXXXXXXX"
```

## What's Changed in landing zone version 4.0
<a name="w2aac15c17c17b9"></a>

Important changes to the manifest structure and requirements:
+ Organization Structure
  + `organizationStructure` definition has been removed from the manifest
  + Customers can now define their own organizational structure
  + Only requirement: Service integration accounts must be in the same OU directly under root
+ Enabled Flags
  + All service integration configurations have an `enabled` flag which is now a required field.
  + Customers need to always provide a boolean value. No default values are provided.
  + Customers need to explicitly enable/disable each service integration configuration in the manifest:
    + `accessManagement`
    + `backup`
    + `centralizedLogging`
    + `config`
    + `securityRoles`
+ Security Roles
  + Security Roles integration is now optional
  + New `enabled` flag introduced to manage `securityRoles` deployment
  + When disabled, related security features will not be implemented
+ AWS Config Integration
  + New AWS Config service integration section added to manifest as `config` with the following fields:
    + `enabled`: Required boolean flag to manage AWS Config integration deployment
    + `accountId`: AWS account ID for AWS Config aggregator
    + configurations:
      + `accessLoggingBucket.retentionDays`: Retention period for access logs
      + `loggingBucket.retentionDays`: Retention period for AWS Config logs
      + `kmsKeyArn`: KMS key for encryption