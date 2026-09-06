

# View the details of your landing zone manifest file
<a name="lz-manifest-file"></a>

The AWS Control Tower landing zone manifest file is a text file that describes your AWS Control Tower resources. The following sections show detailed definitions of entries in the landing zone manifest file.

To see a full landing zone schema example, see [Landing zone schemas](https://docs.aws.amazon.com/controltower/latest/userguide/landing-zone-schemas.html).

**governedRegions** – Regions to place under governance 
+  **Type:** List of strings
+ **Required:** No
+ **Example:**

  ```
  "governedRegions": ["us-west-2","us-west-1"]
  ```

**organizationStructure** – Select the names of security and sandbox OUs to be created in your organization
+  **Type:** Object
+ **Required:** Yes
+ **Properties:**
+ **Example:**
  + `security` - an object with one required property, `name`, which takes a `String`
  + `sandbox` - an object with one required property, `name`, which takes a `String`

  ```
  "organizationStructure": {
         "security": {
             "name": "CORE"
         },
         "sandbox": {
             "name": "Sandbox"
         }
     }
  ```

**Note**  
The `organizationStructure` field is not present in landing zone version 4.0 and later.

**centralizedLogging** – Configuration for AWS CloudTrail
+  **Type:** Object
+ **Required:** No (version 4.0 and later). Yes (version 3.3 and earlier).
+ **Properties:**
  + *accountId* - a `String` the represents the AWS account into which the logging resource should be deployed
  + *configurations* - an `Object` with three properties
    + `loggingBucket` - an object with one property, `retentionDays`, which takes a `Number`
    + `accessLoggingBucket` - an object with one property, `retentionDays`, which takes a `Number`
    + `kmsKeyArn` - an optional `String`
  + *enabled* - a `Boolean` (required in version 4.0 and later, optional in version 3.3 and earlier) 
+ **Example:**

  ```
  "centralizedLogging": {
          "accountId": "222222222222",
          "configurations": {
              "loggingBucket": {
                  "retentionDays": 60
              },
              "accessLoggingBucket": {
                  "retentionDays": 60
              },
              "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
          },
          "enabled": true
     }
  ```

**Note**  
In landing zone version 4.0 and later, `accountId` is only required when `enabled` is set to `true`. The `enabled` field is required.

**securityRoles** – Choose where to deploy central resources for security monitoring within your organization
+  **Type:** Object
+ **Required:** No (version 4.0 and later). Yes (version 3.3 and earlier).
+ **Properties:**
  + *accountId* - a `String` that represents the AWS account into which the central security monitoring resources should be deployed. Required when `enabled` is `true`.
  + *enabled* - a `Boolean` (required in version 4.0 and later)
+ **Example:**

  ```
  "securityRoles": {
          "accountId": "333333333333",
          "enabled": true
     }
  ```

**Note**  
In landing zone version 4.0 and later, `securityRoles` includes a required `enabled` Boolean property. The `accountId` is only required when `enabled` is set to `true`.

**accessManagement** – Choose whether to enable access management
+  **Type:** Object
+ **Required:** No
+ **Properties:** *enabled* - a Boolean
+ **Example:**

  ```
  "accessManagement": {
          "enabled": true
     }
  ```

**backup** – Configuration for AWS Backup with AWS Control Tower
+  **Type:** Object
+ **Required:** No
+ **Properties:**
  + *configurations* - an `Object` with three properties
    + `centralBackup` - an object with one property, `accountId`, which takes a `String`
    + `backupAdmin` - an object with one property, `accountId`, which takes a `String`
    + `kmsKeyArn` - an optional `String`
  + *enabled* - a `Boolean` 
+ **Example:**

  ```
  "backup": {
      "configurations": {
          "centralBackup": {
              "accountId": "{{CENTRAL BACKUP ACCOUNT ID}}"
          },
          "backupAdmin": {
              "accountId": "{{BACKUP MANAGER ACCOUNT ID}}"
          },
          "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
      },
      "enabled": true
  }
  ```

**config** – Configuration for AWS Config with AWS Control Tower
+  **Type:** Object
+ **Required:** No
+ **Properties:**
  + *accountId* - a `String` that represents the AWS account into which the AWS Config resources should be deployed. Required when `enabled` is `true`.
  + *configurations* - an optional `Object` with three properties
    + `loggingBucket` - an object with one property, `retentionDays`, which takes a `Number`
    + `accessLoggingBucket` - an object with one property, `retentionDays`, which takes a `Number`
    + `kmsKeyArn` - an optional `String`
  + *enabled* - a required `Boolean`
+ **Example:**

  ```
  "config": {
      "accountId": "444444444444",
      "configurations": {
          "loggingBucket": {
              "retentionDays": 60
          },
          "accessLoggingBucket": {
              "retentionDays": 60
          },
          "kmsKeyArn": "arn:aws:kms:us-west-1:123456789123:key/e84XXXXX-6bXX-49XX-9eXX-ecfXXXXXXXXX"
      },
      "enabled": true
  }
  ```

**Note**  
The `config` field is only available in landing zone version 4.0 and later.