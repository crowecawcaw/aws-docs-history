# Amazon DocumentDB controls

###### Topics

- [[CT.DOCUMENTDB.PR.1] Require an Amazon DocumentDB cluster to be encrypted at rest](#ct-documentdb-pr-1-description "#ct-documentdb-pr-1-description")
- [[CT.DOCUMENTDB.PR.2] Require an Amazon DocumentDB cluster to have a backup retention period greater than or equal to seven days](#ct-documentdb-pr-2-description "#ct-documentdb-pr-2-description")

## [CT.DOCUMENTDB.PR.1] Require an Amazon DocumentDB cluster to be encrypted at rest

This control checks whether storage encryption is enabled for an Amazon DocumentDB (with MongoDB compatibility) cluster.

- **Control objective:** Encrypt data at rest
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DocDB::DBCluster`
- **CloudFormation guard rule:**
  [CT.DOCUMENTDB.PR.1 rule specification](#ct-documentdb-pr-1-rule "#ct-documentdb-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DOCUMENTDB.PR.1 rule specification](#ct-documentdb-pr-1-rule "#ct-documentdb-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.DOCUMENTDB.PR.1 example templates](#ct-documentdb-pr-1-templates "#ct-documentdb-pr-1-templates")

**Explanation**

You encrypt data at rest in your Amazon DocumentDB cluster by specifying the storage encryption option when you create your cluster. Storage encryption is enabled cluster-wide, and it is applied to all instances, including the primary instance and any replicas. It also is applied to your cluster's storage volume, data, indexes, logs, automated backups, and snapshots.

Clusters that you create using AWS CloudFormation have encryption at rest turned off by default. Therefore, you must explicitly enable encryption at rest using the `StorageEncrypted` property.

### Remediation for rule failure

Set the value of the `StorageEncrypted` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon DocumentDB Cluster - Example

An Amazon DocumentDB cluster configured with storage encryption enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DocumentDBCluster": {
        "Type": "AWS::DocDB::DBCluster",
        "Properties": {
            "MasterUsername": {
                "Fn::Sub": "{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}"
            },
            "MasterUserPassword": {
                "Fn::Sub": "{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}"
            },
            "StorageEncrypted": true
        }
    }
}

```

**YAML example**

```

DocumentDBCluster:
  Type: AWS::DocDB::DBCluster
  Properties:
    MasterUsername: !Sub '{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}'
    MasterUserPassword: !Sub '{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}'
    StorageEncrypted: true


```

### CT.DOCUMENTDB.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   docdb_cluster_encrypted_check
#
# Description:
#   This control checks whether storage encryption is enabled for an Amazon DocumentDB (with MongoDB compatibility) cluster.
#
# Reports on:
#   AWS::DocDB::DBCluster
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Document DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Document DB cluster resource
#       And: 'StorageEncrypted' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Document DB cluster resource
#       And: 'StorageEncrypted' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Document DB cluster resource
#       And: 'StorageEncrypted' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let DOCUMENT_DB_CLUSTER_TYPE = "AWS::DocDB::DBCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let document_db_clusters = Resources.*[ Type == %DOCUMENT_DB_CLUSTER_TYPE ]

#
# Primary Rules
#
rule docdb_cluster_encrypted_check when is_cfn_template(%INPUT_DOCUMENT)
                                        %document_db_clusters not empty {
    check(%document_db_clusters.Properties)
        <<
        [CT.DOCUMENTDB.PR.1]: Require an Amazon DocumentDB cluster to be encrypted at rest
        [FIX]: Set the value of the 'StorageEncrypted' parameter to true.
        >>
}

rule docdb_cluster_encrypted_check when is_cfn_hook(%INPUT_DOCUMENT, %DOCUMENT_DB_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%DOCUMENT_DB_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.DOCUMENTDB.PR.1]: Require an Amazon DocumentDB cluster to be encrypted at rest
        [FIX]: Set the value of the 'StorageEncrypted' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(document_db_cluster) {
    %document_db_cluster {
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

### CT.DOCUMENTDB.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DocumentDBClusterSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        SecretStringTemplate: '{"username": "exampleuser"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: \"@/\\
  DocumentDBCluster:
    Type: AWS::DocDB::DBCluster
    Properties:
      MasterUsername:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}'
      MasterUserPassword:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}'
      StorageEncrypted: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DocumentDBClusterSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        SecretStringTemplate: '{"username": "exampleuser"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: \"@/\\
  DocumentDBCluster:
    Type: AWS::DocDB::DBCluster
    Properties:
      MasterUsername:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}'
      MasterUserPassword:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}'
      StorageEncrypted: false


```

## [CT.DOCUMENTDB.PR.2] Require an Amazon DocumentDB cluster to have a backup retention period greater than or equal to seven days

This control checks whether an Amazon DocumentDB cluster retention period is set to seven or more days (>=7). The default retention period is one day.

- **Control objective:** Improve resiliency
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DocDB::DBCluster`
- **CloudFormation guard rule:**
  [CT.DOCUMENTDB.PR.2 rule specification](#ct-documentdb-pr-2-rule "#ct-documentdb-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DOCUMENTDB.PR.2 rule specification](#ct-documentdb-pr-2-rule "#ct-documentdb-pr-2-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.DOCUMENTDB.PR.2 example templates](#ct-documentdb-pr-2-templates "#ct-documentdb-pr-2-templates")

**Explanation**

Amazon DocumentDB creates daily automatic snapshots of your cluster during your cluster's backup window. Amazon DocumentDB saves the automatic snapshots of your cluster according to the backup retention period that you specify, allowing you to restore to any point within the backup retention period. This daily snapshot strengthens the resilience of your systems, and it can help you recover quickly from a security incident.

### Remediation for rule failure

Set the value of the `BackupRetentionPeriod` parameter to an integer value between 7 and 35 days (inclusive).

The examples that follow show how to implement this remediation.

#### Amazon DocumentDB Cluster - Example

An Amazon DocumentDB cluster configured with a backup retention period of seven (7) days. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DocumentDBCluster": {
        "Type": "AWS::DocDB::DBCluster",
        "Properties": {
            "MasterUsername": {
                "Fn::Sub": "{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}"
            },
            "MasterUserPassword": {
                "Fn::Sub": "{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}"
            },
            "BackupRetentionPeriod": 7
        }
    }
}

```

**YAML example**

```

DocumentDBCluster:
  Type: AWS::DocDB::DBCluster
  Properties:
    MasterUsername: !Sub '{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}'
    MasterUserPassword: !Sub '{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}'
    BackupRetentionPeriod: 7


```

### CT.DOCUMENTDB.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   docdb_cluster_backup_retention_check
#
# Description:
#   This control checks whether an Amazon DocumentDB cluster retention period is set to seven or more days (>=7).
#
# Reports on:
#   AWS::DocDB::DBCluster
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any Document DB cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Document DB cluster resource
#       And: 'BackupRetentionPeriod' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Document DB cluster resource
#       And: 'BackupRetentionPeriod' has been provided and set to an integer value less than seven (<7)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a Document DB cluster resource
#       And: 'BackupRetentionPeriod' has been provided and set to an integer value greater than or equal to seven (>=7)
#      Then: PASS

#
# Constants
#
let DOCUMENT_DB_CLUSTER_TYPE = "AWS::DocDB::DBCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let document_db_clusters = Resources.*[ Type == %DOCUMENT_DB_CLUSTER_TYPE ]

#
# Primary Rules
#
rule docdb_cluster_backup_retention_check when is_cfn_template(%INPUT_DOCUMENT)
                                               %document_db_clusters not empty {
    check(%document_db_clusters.Properties)
        <<
        [CT.DOCUMENTDB.PR.2]: Require an Amazon DocumentDB cluster to have automatic backups enabled
        [FIX]: Set the value of the 'BackupRetentionPeriod' parameter to an integer value between 7 and 35 days (inclusive).
        >>
}

rule docdb_cluster_backup_retention_check when is_cfn_hook(%INPUT_DOCUMENT, %DOCUMENT_DB_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%DOCUMENT_DB_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.DOCUMENTDB.PR.2]: Require an Amazon DocumentDB cluster to have automatic backups enabled
        [FIX]: Set the value of the 'BackupRetentionPeriod' parameter to an integer value between 7 and 35 days (inclusive).
        >>
}

#
# Parameterized Rules
#
rule check(document_db_cluster) {
    %document_db_cluster {
        # Scenario 2
        BackupRetentionPeriod exists
        # Scenarios 3 and 4
        BackupRetentionPeriod >= 7
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

### CT.DOCUMENTDB.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DocumentDBClusterSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        SecretStringTemplate: '{"username": "exampleuser"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: '\"@/\\'
  DocumentDBCluster:
    Type: AWS::DocDB::DBCluster
    Properties:
      MasterUsername:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}'
      MasterUserPassword:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}'
      BackupRetentionPeriod: 7


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DocumentDBClusterSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      GenerateSecretString:
        SecretStringTemplate: '{"username": "exampleuser"}'
        GenerateStringKey: password
        PasswordLength: 16
        ExcludeCharacters: '\"@/\\'
  DocumentDBCluster:
    Type: AWS::DocDB::DBCluster
    Properties:
      MasterUsername:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::username}}'
      MasterUserPassword:
        Fn::Sub: '{{resolve:secretsmanager:${DocumentDBClusterSecret}::password}}'
      BackupRetentionPeriod: 1


```
