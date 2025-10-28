# Amazon Neptune controls

###### Topics

- [[CT.NEPTUNE.PR.1] Require an Amazon Neptune DB cluster to have AWS Identity and Access Management (IAM) database authentication enabled](#ct-neptune-pr-1-description "#ct-neptune-pr-1-description")
- [[CT.NEPTUNE.PR.2] Require an Amazon Neptune DB cluster to have deletion protection enabled](#ct-neptune-pr-2-description "#ct-neptune-pr-2-description")
- [[CT.NEPTUNE.PR.3] Require an Amazon Neptune DB cluster to have storage encryption enabled](#ct-neptune-pr-3-description "#ct-neptune-pr-3-description")
- [[CT.NEPTUNE.PR.4] Require an Amazon Neptune DB cluster to
  enable Amazon CloudWatch Logs export for audit logs](#ct-neptune-pr-4-description "#ct-neptune-pr-4-description")
- [[CT.NEPTUNE.PR.5] Require an Amazon Neptune DB cluster to set a
  backup retention period greater than or equal to seven days](#ct-neptune-pr-5-description "#ct-neptune-pr-5-description")

## [CT.NEPTUNE.PR.1] Require an Amazon Neptune DB cluster to have AWS Identity and Access Management (IAM) database authentication enabled

This control checks whether an Amazon Neptune cluster has AWS Identity and Access Management (IAM) database authentication enabled.

- **Control objective:** Enforce least privilege, Use strong authentication
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Neptune::DBCluster`
- **AWS CloudFormation guard rule:**
  [CT.NEPTUNE.PR.1 rule specification](#ct-neptune-pr-1-rule "#ct-neptune-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.NEPTUNE.PR.1 rule specification](#ct-neptune-pr-1-rule "#ct-neptune-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.NEPTUNE.PR.1 example templates](#ct-neptune-pr-1-templates "#ct-neptune-pr-1-templates")

**Explanation**

You can use AWS Identity and Access Management (IAM) to authenticate to your Neptune DB instance or DB cluster. IAM allows you to manage access to your database resources centrally, instead of managing access individually on each DB instance or cluster.

### Remediation for rule failure

Set the value of the `IamAuthEnabled` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon Neptune Cluster - Example

Neptune Cluster configured with AWS IAM database authentication enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "NeptuneDBCluster": {
        "Type": "AWS::Neptune::DBCluster",
        "Properties": {
            "IamAuthEnabled": true
        }
    }
}

```

**YAML example**

```

NeptuneDBCluster:
  Type: AWS::Neptune::DBCluster
  Properties:
    IamAuthEnabled: true


```

### CT.NEPTUNE.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   neptune_cluster_iam_database_authentication_check
#
# Description:
#   This control checks whether an Amazon Neptune cluster has AWS Identity and Access Management (IAM) database authentication enabled.
#
# Reports on:
#   AWS::Neptune::DBCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any Neptune DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'IamAuthEnabled' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'IamAuthEnabled' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'IamAuthEnabled' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let NEPTUNE_CLUSTER_TYPE = "AWS::Neptune::DBCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let neptune_db_clusters = Resources.*[ Type == %NEPTUNE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule neptune_cluster_iam_database_authentication_check when is_cfn_template(%INPUT_DOCUMENT)
                                                            %neptune_db_clusters not empty {
    check(%neptune_db_clusters.Properties)
        <<
        [CT.NEPTUNE.PR.1]: Require an Amazon Neptune DB cluster to have AWS Identity and Access Management (IAM) database authentication enabled
        [FIX]: Set the value of the 'IamAuthEnabled' parameter to true.
        >>
}

rule neptune_cluster_iam_database_authentication_check when is_cfn_hook(%INPUT_DOCUMENT, %NEPTUNE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%NEPTUNE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.NEPTUNE.PR.1]: Require an Amazon Neptune DB cluster to have AWS Identity and Access Management (IAM) database authentication enabled
        [FIX]: Set the value of the 'IamAuthEnabled' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(neptune_cluster) {
    %neptune_cluster {
        # Scenario 2
        IamAuthEnabled exists
        # Scenarios 3 and 4
        IamAuthEnabled == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.NEPTUNE.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      IamAuthEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      IamAuthEnabled: false


```

## [CT.NEPTUNE.PR.2] Require an Amazon Neptune DB cluster to have deletion protection enabled

This control checks whether an Amazon Neptune cluster has deletion protection enabled.

- **Control objective:** Improve availability, Protect configurations
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Neptune::DBCluster`
- **AWS CloudFormation guard rule:**
  [CT.NEPTUNE.PR.2 rule specification](#ct-neptune-pr-2-rule "#ct-neptune-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.NEPTUNE.PR.2 rule specification](#ct-neptune-pr-2-rule "#ct-neptune-pr-2-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.NEPTUNE.PR.2 example templates](#ct-neptune-pr-2-templates "#ct-neptune-pr-2-templates")

**Explanation**

Cluster deletion protection adds an additional layer of protection against accidental database deletion, or deletion by an unauthorized entity. A Neptune cluster cannot be deleted while deletion protection is enabled. Deletion protection must be disabled first, before a delete request can succeed.

### Remediation for rule failure

Set the value of the `DeletionProtection` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon Neptune Cluster - Example

An Amazon Neptune Cluster configured with deletion protection enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "NeptuneDBCluster": {
        "Type": "AWS::Neptune::DBCluster",
        "Properties": {
            "DeletionProtection": true
        }
    }
}

```

**YAML example**

```

NeptuneDBCluster:
  Type: AWS::Neptune::DBCluster
  Properties:
    DeletionProtection: true


```

### CT.NEPTUNE.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   neptune_cluster_deletion_protection_enabled_check
#
# Description:
#   This control checks whether an Amazon Neptune cluster has deletion protection enabled.
#
# Reports on:
#   AWS::Neptune::DBCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any Neptune DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'DeletionProtection' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'DeletionProtection' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'DeletionProtection' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let NEPTUNE_CLUSTER_TYPE = "AWS::Neptune::DBCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let neptune_db_clusters = Resources.*[ Type == %NEPTUNE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule neptune_cluster_deletion_protection_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                            %neptune_db_clusters not empty {
    check(%neptune_db_clusters.Properties)
        <<
        [CT.NEPTUNE.PR.2]: Require an Amazon Neptune DB cluster to have deletion protection enabled
        [FIX]: Set the value of the 'DeletionProtection' parameter to true.
        >>
}

rule neptune_cluster_deletion_protection_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %NEPTUNE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%NEPTUNE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.NEPTUNE.PR.2]: Require an Amazon Neptune DB cluster to have deletion protection enabled
        [FIX]: Set the value of the 'DeletionProtection' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(neptune_cluster) {
    %neptune_cluster {
        # Scenario 2
        DeletionProtection exists
        # Scenarios 3 and 4
        DeletionProtection == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.NEPTUNE.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DeletionProtection: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DeletionProtection: false


```

## [CT.NEPTUNE.PR.3] Require an Amazon Neptune DB cluster to have storage encryption enabled

This control checks whether an Amazon Neptune cluster has storage encryption enabled.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Neptune::DBCluster`
- **AWS CloudFormation guard rule:**
  [CT.NEPTUNE.PR.3 rule specification](#ct-neptune-pr-3-rule "#ct-neptune-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.NEPTUNE.PR.3 rule specification](#ct-neptune-pr-3-rule "#ct-neptune-pr-3-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.NEPTUNE.PR.3 example templates](#ct-neptune-pr-3-templates "#ct-neptune-pr-3-templates")

**Explanation**

Neptune encrypted instances provide an additional layer of data protection, because they help to secure your data from unauthorized access to the underlying storage. Neptune encryption helps increase data protection of your applications that are deployed in the cloud. You also can use it to fulfill compliance requirements for data-at-rest encryption.

###### Usage considerations

- This control checks only whether the `StorageEncrypted` property is provided and set to `true.` When you create an encrypted Neptune DB instance, you also can supply the AWS KMS key identifier for your encryption key by means of the `KmsKeyId` property. If you don't specify an AWS KMS key identifier, Neptune uses your default Amazon RDS encryption key (aws/rds) for your new Neptune DB instance.

### Remediation for rule failure

Set `StorageEncrypted` to `true`.

The examples that follow show how to implement this remediation.

#### Amazon Neptune Cluster - Example

An Amazon Neptune Cluster configured with storage encryption enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "NeptuneDBCluster": {
        "Type": "AWS::Neptune::DBCluster",
        "Properties": {
            "StorageEncrypted": true
        }
    }
}

```

**YAML example**

```

NeptuneDBCluster:
  Type: AWS::Neptune::DBCluster
  Properties:
    StorageEncrypted: true


```

### CT.NEPTUNE.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   neptune_cluster_encrypted_check
#
# Description:
#   This control checks whether an Amazon Neptune cluster has storage encryption enabled.
#
# Reports on:
#   AWS::Neptune::DBCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any Neptune DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'StorageEncrypted' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'StorageEncrypted' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'StorageEncrypted' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let NEPTUNE_CLUSTER_TYPE = "AWS::Neptune::DBCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let neptune_db_clusters = Resources.*[ Type == %NEPTUNE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule neptune_cluster_encrypted_check when is_cfn_template(%INPUT_DOCUMENT)
                                          %neptune_db_clusters not empty {
    check(%neptune_db_clusters.Properties)
        <<
        [CT.NEPTUNE.PR.3]: Require an Amazon Neptune DB cluster to have storage encryption enabled
        [FIX]: Set 'StorageEncrypted' to 'true'.
        >>
}

rule neptune_cluster_encrypted_check when is_cfn_hook(%INPUT_DOCUMENT, %NEPTUNE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%NEPTUNE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.NEPTUNE.PR.3]: Require an Amazon Neptune DB cluster to have storage encryption enabled
        [FIX]: Set 'StorageEncrypted' to 'true'.
        >>
}

#
# Parameterized Rules
#
rule check(neptune_cluster) {
    %neptune_cluster {
        # Scenario 2
        StorageEncrypted exists
        # Scenarios 3 and 4
        StorageEncrypted == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.NEPTUNE.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      StorageEncrypted: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      StorageEncrypted: false


```

## [CT.NEPTUNE.PR.4] Require an Amazon Neptune DB cluster to

enable Amazon CloudWatch Logs export for audit logs

This control checks whether an Amazon Neptune cluster is configured to send audit logs to
Amazon CloudWatch Logs.

- **Control objective:** Establish logging and monitoring
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Neptune::DBCluster`
- **AWS CloudFormation guard rule:**
  [CT.NEPTUNE.PR.4 rule specification](#ct-neptune-pr-4-rule "#ct-neptune-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.NEPTUNE.PR.4 rule specification](#ct-neptune-pr-4-rule "#ct-neptune-pr-4-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.NEPTUNE.PR.4 example templates](#ct-neptune-pr-4-templates "#ct-neptune-pr-4-templates")

**Explanation**

You can configure an Amazon Neptune DB cluster to publish audit log data to a log group in
Amazon CloudWatch Logs. Storing your Neptune DB cluster audit log data in Amazon CloudWatch Logs allows you to perform
real-time analysis of the log data, and also to use Amazon CloudWatch to create alarms and view metrics.

### Remediation for rule failure

In the `EnableCloudwatchLogsExports` parameter, set an entry to the value audit.

The examples that follow show how to implement this remediation.

#### Amazon Neptune cluster - Example

An Amazon Neptune Cluster configured to export audit logs to Amazon CloudWatch Logs. The example is
shown in JSON and in YAML.

**JSON example**

```

{
    "NeptuneDBCluster": {
        "Type": "AWS::Neptune::DBCluster",
        "Properties": {
            "EnableCloudwatchLogsExports": [
                "audit"
            ]
        }
    }
}

```

**YAML example**

```

NeptuneDBCluster:
  Type: AWS::Neptune::DBCluster
  Properties:
    EnableCloudwatchLogsExports:
      - audit


```

### CT.NEPTUNE.PR.4 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   neptune_cluster_cloudwatch_audit_log_export_enabled
#
# Description:
#   This control checks whether an Amazon Neptune cluster is configured to send audit logs to Amazon CloudWatch Logs.
#
# Reports on:
#   AWS::Neptune::DBCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any Neptune DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'EnableCloudwatchLogsExports' has not been provided or has been provided as an
#            empty list
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'EnableCloudwatchLogsExports' has been provided as a non-empty list
#       And: 'EnableCloudwatchLogsExports' does not contain an entry with the value 'audit'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'EnableCloudwatchLogsExports' has been provided as a non-empty list
#       And: 'EnableCloudwatchLogsExports' contains an entry with the value 'audit'
#      Then: PASS

#
# Constants
#
let NEPTUNE_CLUSTER_TYPE = "AWS::Neptune::DBCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let neptune_db_clusters = Resources.*[ Type == %NEPTUNE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule neptune_cluster_cloudwatch_audit_log_export_enabled when is_cfn_template(%INPUT_DOCUMENT)
                                                              %neptune_db_clusters not empty {
    check(%neptune_db_clusters.Properties)
        <<
        [CT.NEPTUNE.PR.4]: Require an Amazon Neptune DB cluster to enable Amazon CloudWatch log export for audit logs
        [FIX]: In the 'EnableCloudwatchLogsExports' parameter, set an entry to the value audit.
        >>
}

rule neptune_cluster_cloudwatch_audit_log_export_enabled when is_cfn_hook(%INPUT_DOCUMENT, %NEPTUNE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%NEPTUNE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.NEPTUNE.PR.4]: Require an Amazon Neptune DB cluster to enable Amazon CloudWatch log export for audit logs
        [FIX]: In the 'EnableCloudwatchLogsExports' parameter, set an entry to the value audit.
        >>
}

#
# Parameterized Rules
#
rule check(neptune_cluster) {
    %neptune_cluster {
        # Scenario 2
        EnableCloudwatchLogsExports exists
        EnableCloudwatchLogsExports is_list
        EnableCloudwatchLogsExports not empty

        # Scenarios 3 and 4
        some EnableCloudwatchLogsExports[*] == "audit"
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.NEPTUNE.PR.4 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      EnableCloudwatchLogsExports:
      - audit
      - slowquery


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      EnableCloudwatchLogsExports:
      - slowquery


```

## [CT.NEPTUNE.PR.5] Require an Amazon Neptune DB cluster to set a

backup retention period greater than or equal to seven days

This control checks whether Amazon Neptune DB clusters have configured automatic backups with a retention period set to
7 or more days (>=7). The default retention period is one day.

- **Control objective:** Improve resiliency
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::Neptune::DBCluster`
- **AWS CloudFormation guard rule:**
  [CT.NEPTUNE.PR.5 rule specification](#ct-neptune-pr-5-rule "#ct-neptune-pr-5-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.NEPTUNE.PR.5 rule specification](#ct-neptune-pr-5-rule "#ct-neptune-pr-5-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.NEPTUNE.PR.5 example templates](#ct-neptune-pr-5-templates "#ct-neptune-pr-5-templates")

**Explanation**

Amazon Neptune backs up your cluster volume automatically, and it retains restore data for the length of the backup
retention period. Backups are continuous and incremental. You can restore to any point within the backup
retention period, quickly. No performance impact or interruption of database service occurs as backup data is
being written.

### Remediation for rule failure

Set the `BackupRetentionPeriod` parameter to an integer value between 7 and 35 days (inclusive).

The examples that follow show how to implement this remediation.

#### Amazon Neptune cluster - Example

An Amazon Neptune Cluster configured with a backup retention period of seven (7) days. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "NeptuneDBCluster": {
        "Type": "AWS::Neptune::DBCluster",
        "Properties": {
            "BackupRetentionPeriod": 7
        }
    }
}

```

**YAML example**

```

NeptuneDBCluster:
  Type: AWS::Neptune::DBCluster
  Properties:
    BackupRetentionPeriod: 7


```

### CT.NEPTUNE.PR.5 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   neptune_cluster_backup_retention_check
#
# Description:
#   This control checks whether Amazon Neptune DB clusters have configured automatic backups with a retention period set to 7 or more days (>=7). The default retention period is one day.
#
# Reports on:
#   AWS::Neptune::DBCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any Neptune DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'BackupRetentionPeriod' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'BackupRetentionPeriod' has been provided and set to an integer value
#            less than seven (< 7)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a Neptune DB cluster resource
#       And: 'BackupRetentionPeriod' has been provided and set to an integer value
#            greater than or equal to seven (>=7)
#      Then: PASS

#
# Constants
#
let NEPTUNE_CLUSTER_TYPE = "AWS::Neptune::DBCluster"
let MINIMUM_BACKUP_RETENTION_PERIOD = 7
let INPUT_DOCUMENT = this

#
# Assignments
#
let neptune_db_clusters = Resources.*[ Type == %NEPTUNE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule neptune_cluster_backup_retention_check when is_cfn_template(%INPUT_DOCUMENT)
                                                 %neptune_db_clusters not empty {
    check(%neptune_db_clusters.Properties)
        <<
        [CT.NEPTUNE.PR.5]: Require an Amazon Neptune DB cluster to set a backup retention period greater than or equal to seven days
        [FIX]: Set the 'BackupRetentionPeriod' parameter to an integer value between 7 and 35 days (inclusive).
        >>
}

rule neptune_cluster_backup_retention_check when is_cfn_hook(%INPUT_DOCUMENT, %NEPTUNE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%NEPTUNE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.NEPTUNE.PR.5]: Require an Amazon Neptune DB cluster to set a backup retention period greater than or equal to seven days
        [FIX]: Set the 'BackupRetentionPeriod' parameter to an integer value between 7 and 35 days (inclusive).
        >>
}

#
# Parameterized Rules
#
rule check(neptune_cluster) {
    %neptune_cluster {
        # Scenario 2
        BackupRetentionPeriod exists
        # Scenarios 3 and 4
        BackupRetentionPeriod >= %MINIMUM_BACKUP_RETENTION_PERIOD
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.NEPTUNE.PR.5 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      BackupRetentionPeriod: 7


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource
creation.

```

Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      BackupRetentionPeriod: 1


```
