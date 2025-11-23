# AWS Database Migration Service (AWS DMS) controls

###### Topics

- [[CT.DMS.PR.1] Require that a public AWS DMS replication instance is not public](#ct-dms-pr-1-description "#ct-dms-pr-1-description")
- [[CT.DMS.PR.2] Require an AWS Database Migration Service (DMS) Endpoint to encrypt connections for source and target endpoints](#ct-dms-pr-2-description "#ct-dms-pr-2-description")

## [CT.DMS.PR.1] Require that a public AWS DMS replication instance is not public

This control checks whether your AWS DMS replication instance is public.

- **Control objective:** Limit network access, Enforce least privilege
- **Implementation:** CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DMS::ReplicationInstance`
- **CloudFormation guard rule:**
  [CT.DMS.PR.1 rule specification](#ct-dms-pr-1-rule "#ct-dms-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DMS.PR.1 rule specification](#ct-dms-pr-1-rule "#ct-dms-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.DMS.PR.1 example templates](#ct-dms-pr-1-templates "#ct-dms-pr-1-templates")

**Explanation**

A private replication instance has a private IP address that you cannot access outside of the replication network. You use a private instance when both source and target databases are in the same network that is connected to the replication instance's VPC. The network can be connected to the VPC by using a VPN, AWS Direct Connect, or VPC peering.

### Remediation for rule failure

Set `PubliclyAccessible` to `false`.

The examples that follow show how to implement this remediation.

#### AWS DMS Replication Instance - Example

AWS DMS replication instance configured with public access disabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DMSReplicationInstance": {
        "Type": "AWS::DMS::ReplicationInstance",
        "Properties": {
            "ReplicationInstanceClass": "dms.t3.micro",
            "PubliclyAccessible": false
        }
    }
}

```

**YAML example**

```

DMSReplicationInstance:
  Type: AWS::DMS::ReplicationInstance
  Properties:
    ReplicationInstanceClass: dms.t3.micro
    PubliclyAccessible: false


```

### CT.DMS.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
# Rule Identifier:
#   dms_replication_instance_not_public_check
#
# Description:
#   This control checks whether your AWS DMS replication instance is public.
#
# Reports on:
#   AWS::DMS::ReplicationInstance
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
#       And: The input document does not contain any AWS DMS replication instance resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS replication instance resource
#       And: 'PubliclyAccessible' is not present on the AWS DMS replication instance
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS replication instance resource
#       And: 'PubliclyAccessible' is present on the AWS DMS replication instance
#            and is set to bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS replication instance resource
#       And: 'PubliclyAccessible' is present on the AWS DMS replication instance
#            and is set to bool(false)
#      Then: PASS

#
# Constants
#
let DMS_REPLICATION_INSTANCE_TYPE = "AWS::DMS::ReplicationInstance"
let INPUT_DOCUMENT = this

#
# Assignments
#
let dms_replication_instances = Resources.*[ Type == %DMS_REPLICATION_INSTANCE_TYPE ]

#
# Primary Rules
#
rule dms_replication_instance_not_public_check when is_cfn_template(%INPUT_DOCUMENT)
                                                    %dms_replication_instances not empty {
    check(%dms_replication_instances.Properties)
        <<
        [CT.DMS.PR.1]: Require that a public AWS DMS replication instance is not public
        [FIX]: Set 'PubliclyAccessible' to 'false'.
        >>
}

rule dms_replication_instance_not_public_check when is_cfn_hook(%INPUT_DOCUMENT, %DMS_REPLICATION_INSTANCE_TYPE) {
    check(%INPUT_DOCUMENT.%DMS_REPLICATION_INSTANCE_TYPE.resourceProperties)
        <<
        [CT.DMS.PR.1]: Require that a public AWS DMS replication instance is not public
        [FIX]: Set 'PubliclyAccessible' to 'false'.
        >>
}

#
# Parameterized Rules
#
rule check(dms_replication_instances) {
    %dms_replication_instances {
        # Scenario 2
        PubliclyAccessible exists
        # Scenario 3 and 4
        PubliclyAccessible == false
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

### CT.DMS.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DMSReplicationInstance:
    Type: AWS::DMS::ReplicationInstance
    Properties:
      ReplicationInstanceClass: dms.t3.micro
      PubliclyAccessible: false


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DMSReplicationInstance:
    Type: AWS::DMS::ReplicationInstance
    Properties:
      ReplicationInstanceClass: dms.t3.micro
      PubliclyAccessible: true


```

## [CT.DMS.PR.2] Require an AWS Database Migration Service (DMS) Endpoint to encrypt connections for source and target endpoints

This control checks whether an AWS Database Migration Service (AWS DMS) Endpoint is configured to encrypt connections for source and target endpoints by
using Secure Sockets Layer (SSL).

- **Control objective:** Encrypt data in transit
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DMS::Endpoint`
- **CloudFormation guard rule:**
  [CT.DMS.PR.2 rule specification](#ct-dms-pr-2-rule "#ct-dms-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DMS.PR.2 rule specification](#ct-dms-pr-2-rule "#ct-dms-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.DMS.PR.2 example templates](#ct-dms-pr-2-templates "#ct-dms-pr-2-templates")

**Explanation**

You can encrypt connections for source and target endpoints by using Secure Sockets Layer (SSL). By enabling encryption
in-transit with SSL, you can protect the confidentiality of data during AWS DMS data migrations.

###### Usage considerations

- This control applies only to AWS DMS endpoints with an EngineName property of `mysql`, `oracle`, `postgres`, `mariadb`, `aurora`, `aurora-postgresql`, `db2,` sybase`,` mongodb`,` docdb`, or` sqlserver'.
- Not all SSL modes work with all database endpoints. See [Using SSL with AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Security.md "../../../dms/latest/userguide/CHAP_Security.md") in the
  _AWS Database Migration Service User Guide_ for information on which SSL modes are supported for each database engine, and limitations of using SSL with AWS DMS.

### Remediation for rule failure

Set the value of the SslMode property to a supported encryption mode for the endpoint engine (one of require, verify-ca, or verify-full).

The examples that follow show how to implement this remediation.

#### AWS DMS Endpoint - Example

An AWS DMS endpoint configured with a `postgres` database target and connection encryption using SSL (TLS). The example is shown in JSON and in YAML.

**JSON example**

```

{
    "Endpoint": {
        "Type": "AWS::DMS::Endpoint",
        "Properties": {
            "DatabaseName": "sample-db",
            "EndpointType": "target",
            "Username": {
                "Fn::Sub": "{{resolve:secretsmanager:${DMSEndpointSecret}::username}}"
            },
            "Password": {
                "Fn::Sub": "{{resolve:secretsmanager:${DMSEndpointSecret}::password}}"
            },
            "Port": 1234,
            "ServerName": "server.db.example.com",
            "EngineName": "postgres",
            "SslMode": "require"
        }
    }
}

```

**YAML example**

```

Endpoint:
  Type: AWS::DMS::Endpoint
  Properties:
    DatabaseName: sample-db
    EndpointType: target
    Username: !Sub '{{resolve:secretsmanager:${DMSEndpointSecret}::username}}'
    Password: !Sub '{{resolve:secretsmanager:${DMSEndpointSecret}::password}}'
    Port: 1234
    ServerName: server.db.example.com
    EngineName: postgres
    SslMode: require


```

### CT.DMS.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   dms_endpoint_ssl_configured_check
#
# Description:
#   This control checks whether an AWS Database Migration Service (AWS DMS) Endpoint is configured to encrypt connections for source and target endpoints by using
Secure Sockets Layer (SSL).
#
# Reports on:
#   AWS::DMS::Endpoint
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
#       And: The input document does not contain any AWS DMS endpoint resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS endpoint resource
#       And: 'EngineName' has been set to an engine other than an engine that supports configuration
#            of SSL connections via 'SslMode' (values other than 'mysql', 'oracle', 'postgres', 'mariadb',
#            'aurora', 'aurora-postgresql', 'db2, 'sybase', 'mongodb', 'docdb', 'sqlserver')
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS endpoint resource
#       And: 'EngineName' has been set to an engine that supports configuration of SSL connections via 'SslMode'
#            ('mysql', 'oracle', 'postgres', 'mariadb', 'aurora', 'aurora-postgresql',
#            'db2, 'sybase', 'mongodb', 'docdb', 'sqlserver')
#       And: 'SslMode' has not been provided
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS endpoint resource
#       And: 'EngineName' has been set to an engine that supports configuration of SSL connections via 'SslMode'
#            ('mysql', 'oracle', 'postgres', 'mariadb', 'aurora', 'aurora-postgresql',
#            'db2, 'sybase', 'mongodb', 'docdb', 'sqlserver')
#       And: 'SslMode' has been provided and set to a value other than 'require', 'verify-ca' or 'verify-full'
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains a AWS DMS endpoint resource
#       And: 'EngineName' has been set to an engine that supports configuration of SSL connections via 'SslMode'
#            ('mysql', 'oracle', 'postgres', 'mariadb', 'aurora', 'aurora-postgresql',
#            'db2, 'sybase', 'mongodb', 'docdb', 'sqlserver')
#       And: 'SslMode' has been provided and set to 'require', 'verify-ca' or 'verify-full'
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let DMS_ENDPOINT_TYPE = "AWS::DMS::Endpoint"
let DMS_ENGINE_NAMES_WITH_SSL_SUPPORT = [
    "mysql",
    "oracle",
    "postgres",
    "mariadb",
    "aurora",
    "aurora-postgresql",
    "db2",
    "sybase",
    "mongodb",
    "docdb",
    "sqlserver"
]
let ALLOWED_DMS_SSL_MODES = [
    "require",
    "verify-ca",
    "verify-full"
]

#
# Assignments
#
let dms_endpoints = Resources.*[ Type == %DMS_ENDPOINT_TYPE ]

#
# Primary Rules
#
rule dms_endpoint_ssl_configured_check when is_cfn_template(%INPUT_DOCUMENT)
                                            %dms_endpoints not empty {
    check(%dms_endpoints.Properties)
        <<
        [CT.DMS.PR.2]: Require an AWS Database Migration Service (AWS DMS) Endpoint to encrypt connections for source and target endpoints
        [FIX]: Set the value of the SslMode property to a supported encryption mode for the endpoint engine (one of require, verify-ca, or verify-full).
        >>
}

rule dms_endpoint_ssl_configured_check when is_cfn_hook(%INPUT_DOCUMENT, %DMS_ENDPOINT_TYPE) {
    check(%INPUT_DOCUMENT.%DMS_ENDPOINT_TYPE.resourceProperties)
        <<
        [CT.DMS.PR.2]: Require an AWS Database Migration Service (AWS DMS) Endpoint to encrypt connections for source and target endpoints
        [FIX]: Set the value of the SslMode property to a supported encryption mode for the endpoint engine (one of require, verify-ca, or verify-full).
        >>
}

#
# Parameterized Rules
#
rule check(dms_endpoint) {
    %dms_endpoint [
        # Scenario 2
        EngineName exists
        EngineName in %DMS_ENGINE_NAMES_WITH_SSL_SUPPORT
    ] {
        # Scenario 3
        SslMode exists
        # Scenarios 4 and 5
        SslMode in %ALLOWED_DMS_SSL_MODES
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

### CT.DMS.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DMSEndpointSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: Example DMS endpoint secret
      GenerateSecretString:
        SecretStringTemplate: '{"username": "exampleuser"}'
        GenerateStringKey: password
        PasswordLength: 22
        ExcludeCharacters: '"@/\;+%{},'
  Endpoint:
    Type: AWS::DMS::Endpoint
    Properties:
      DatabaseName: example-db
      EndpointType: target
      Username:
        Fn::Sub: '{{resolve:secretsmanager:${DMSEndpointSecret}::username}}'
      Password:
        Fn::Sub: '{{resolve:secretsmanager:${DMSEndpointSecret}::password}}'
      Port: 1234
      ServerName: server.db.example.com
      EngineName: postgres
      SslMode: require


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DMSEndpointSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: Example DMS endpoint secret
      GenerateSecretString:
        SecretStringTemplate: '{"username": "exampleuser"}'
        GenerateStringKey: password
        PasswordLength: 22
        ExcludeCharacters: '"@/\;+%{},'
  Endpoint:
    Type: AWS::DMS::Endpoint
    Properties:
      DatabaseName: example-db
      EndpointType: target
      Username:
        Fn::Sub: '{{resolve:secretsmanager:${DMSEndpointSecret}::username}}'
      Password:
        Fn::Sub: '{{resolve:secretsmanager:${DMSEndpointSecret}::password}}'
      Port: 1234
      ServerName: server.db.example.com
      EngineName: postgres


```
