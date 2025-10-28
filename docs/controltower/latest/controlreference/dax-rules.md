# DynamoDB Accelerator controls

###### Topics

- [[CT.DAX.PR.1] Require encryption at rest for all Amazon DynamoDB Accelerator (DAX) clusters](#ct-dax-pr-1-description "#ct-dax-pr-1-description")
- [[CT.DAX.PR.2] Require an Amazon DAX cluster to deploy nodes to at least three Availability Zones](#ct-dax-pr-2-description "#ct-dax-pr-2-description")
- [[CT.DAX.PR.3] Require an Amazon DAX cluster to encrypt data in transit with Transport Layer Security (TLS)](#ct-dax-pr-3-description "#ct-dax-pr-3-description")

## [CT.DAX.PR.1] Require encryption at rest for all Amazon DynamoDB Accelerator (DAX) clusters

This control checks whether Amazon DynamoDB Accelerator (DAX) clusters are encrypted at rest.

###### Note

The control CT.DAX.PR.1 cannot be activated from home Regions
Canada (Central) Region, Europe (Stockholm) Region, and Asia Pacific (Seoul) Region, because the
`AWS::DAX::Cluster` resource type is not available in those Regions. If
your home Region is not one of these three, you can activate the control for these three
Regions from another home Region, if these three Regions are governed by AWS Control Tower in
your landing zone. For example, if your home Region is US West (Oregon) Region, you can deploy
the control to Canada (Central) Region, if Canada (Central) Region is governed by AWS Control Tower.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation Guard Rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DAX::Cluster`
- **AWS CloudFormation guard rule:**
  [CT.DAX.PR.1 rule specification](#ct-dax-pr-1-rule "#ct-dax-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DAX.PR.1 rule specification](#ct-dax-pr-1-rule "#ct-dax-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.DAX.PR.1 example templates](#ct-dax-pr-1-templates "#ct-dax-pr-1-templates")

**Explanation**

Encrypting data at rest reduces the risk that data stored on disk may be accessible to a user who is not authenticated to AWS. Encryption adds another set of access controls, which limits the ability of unauthorized users to gain access to the data. For example, API permissions must decrypt the data before it can be read.

### Remediation for rule failure

Provide an `SSESpecification` configuration with `SSEEnabled` set to `true`.

The examples that follow show how to implement this remediation.

#### Amazon DAX Cluster - Example

Amazon DAX cluster configured with server-side encryption enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DAXCluster": {
        "Type": "AWS::DAX::Cluster",
        "Properties": {
            "IAMRoleARN": {
                "Fn::GetAtt": [
                    "DAXServiceRole",
                    "Arn"
                ]
            },
            "NodeType": "dax.t3.small",
            "ReplicationFactor": 1,
            "SSESpecification": {
                "SSEEnabled": true
            }
        }
    }
}

```

**YAML example**

```

DAXCluster:
  Type: AWS::DAX::Cluster
  Properties:
    IAMRoleARN: !GetAtt 'DAXServiceRole.Arn'
    NodeType: dax.t3.small
    ReplicationFactor: 1
    SSESpecification:
      SSEEnabled: true


```

### CT.DAX.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   dax_cluster_encryption_enabled_check
#
# Description:
#   This control checks whether Amazon DynamoDB Accelerator (DAX) clusters are encrypted at rest.
#
# Reports on:
#   AWS::DAX::Cluster
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
#       And: The input document does not contain any DAX Cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains at least one DAX Cluster resource
#       And: 'SSESpecification' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains at least one DAX Cluster resource
#       And: 'SSESpecification' has been provided and 'SSESpecification.SSEEnabled' is missing or has been set to a
#            value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains at least one DAX Cluster resource
#       And: 'SSESpecification' has been provided and 'SSESpecification.SSEEnabled' is present and has been set to
#            bool(true)
#      Then: PASS

#
# Constants
#
let DAX_CLUSTER_TYPE = "AWS::DAX::Cluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let dax_clusters = Resources.*[ Type == %DAX_CLUSTER_TYPE ]

#
# Primary Rules
#
rule dax_cluster_encryption_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                               %dax_clusters not empty {
    check(%dax_clusters.Properties)
        <<
        [CT.DAX.PR.1]: Require encryption at rest for all Amazon DynamoDB Accelerator (DAX) clusters
            [FIX]: Provide an 'SSESpecification' configuration with 'SSEEnabled' set to 'true'.
        >>
}

rule dax_cluster_encryption_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %DAX_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%DAX_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.DAX.PR.1]: Require encryption at rest for all Amazon DynamoDB Accelerator (DAX) clusters
            [FIX]: Provide an 'SSESpecification' configuration with 'SSEEnabled' set to 'true'.
        >>
}

#
# Parameterized Rules
#
rule check(dax_cluster) {
    %dax_cluster {
        # Scenario 2
        SSESpecification exists
        SSESpecification is_struct

        # Scenario 3 and 4
        SSESpecification {
            SSEEnabled exists
            SSEEnabled == true
        }
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

### CT.DAX.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DAXServiceRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: dax.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: DynamoAccessPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - dynamodb:DescribeTable
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Query
            - dynamodb:Scan
            - dynamodb:BatchGetItem
            - dynamodb:BatchWriteItem
            - dynamodb:ConditionCheckItem
            Resource:
              Fn::Sub: arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:*
  DAXCluster:
    Type: AWS::DAX::Cluster
    Properties:
      IAMRoleARN:
        Fn::GetAtt: [DAXServiceRole, Arn]
      NodeType: dax.t3.small
      ReplicationFactor: 1
      SSESpecification:
        SSEEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DAXServiceRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: dax.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: DynamoAccessPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - dynamodb:DescribeTable
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Query
            - dynamodb:Scan
            - dynamodb:BatchGetItem
            - dynamodb:BatchWriteItem
            - dynamodb:ConditionCheckItem
            Resource:
              Fn::Sub: arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:*
  DAXCluster:
    Type: AWS::DAX::Cluster
    Properties:
      IAMRoleARN:
        Fn::GetAtt: [DAXServiceRole, Arn]
      NodeType: dax.t3.small
      ReplicationFactor: 1
      SSESpecification:
        SSEEnabled: false


```

## [CT.DAX.PR.2] Require an Amazon DAX cluster to deploy nodes to at least three Availability Zones

This control checks whether an Amazon DAX cluster is configured to deploy cluster nodes to at least three Availability Zones.

- **Control objective:** Improve resiliency, Improve availability
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DAX::Cluster`
- **AWS CloudFormation guard rule:**
  [CT.DAX.PR.2 rule specification](#ct-dax-pr-2-rule "#ct-dax-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DAX.PR.2 rule specification](#ct-dax-pr-2-rule "#ct-dax-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.DAX.PR.2 example templates](#ct-dax-pr-2-templates "#ct-dax-pr-2-templates")

**Explanation**

AWS Control Tower recommends that you deploy your Amazon DAX clusters in multiple Availability Zones. This deployment technique allows you to design and operate applications and databases that fail over between Availability Zones automatically, without interruption. For production usage, we strongly recommend that you deploy DAX across at least three nodes, with each node placed into a different Availability Zone.

### Remediation for rule failure

Set the `ReplicationFactor` parameter to an integer value greater than or equal to three (>= 3), and set the `AvailabilityZones` parameter to a list containing three unique Availability Zone entries.

The examples that follow show how to implement this remediation.

#### Amazon DAX cluster - Example

Amazon DAX cluster configured with three nodes and three distinct Availability Zones. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DaxCluster": {
        "Type": "AWS::DAX::Cluster",
        "Properties": {
            "IAMRoleARN": {
                "Fn::GetAtt": [
                    "DaxDynamoAccessRole",
                    "Arn"
                ]
            },
            "NodeType": "dax.t3.small",
            "ReplicationFactor": 3,
            "AvailabilityZones": [
                {
                    "Fn::Select": [
                        0,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                {
                    "Fn::Select": [
                        1,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                {
                    "Fn::Select": [
                        2,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                }
            ]
        }
    }
}

```

**YAML example**

```

DaxCluster:
  Type: AWS::DAX::Cluster
  Properties:
    IAMRoleARN: !GetAtt 'DaxDynamoAccessRole.Arn'
    NodeType: dax.t3.small
    ReplicationFactor: 3
    AvailabilityZones:
      - !Select
        - 0
        - !GetAZs ''
      - !Select
        - 1
        - !GetAZs ''
      - !Select
        - 2
        - !GetAZs ''


```

### CT.DAX.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   dax_cluster_multi_az_check
#
# Description:
#   This control checks whether an Amazon DAX cluster is configured to deploy cluster nodes to at least three Availability Zones.
#
# Reports on:
#   AWS::DAX::Cluster
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
#       And: The input document does not contain any DAX cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ReplicationFactor' has not been provided or has been provided as an integer
#            value less than three (< 3)
#       And: 'AvailabilityZones' has not been provided or provided as an empty list or
#            list with less than three unique entires
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ReplicationFactor' has been provided as an integer value greater than or
#            equal to three (>= 3)
#       And: 'AvailabilityZones' has not been provided or provided as an empty list or
#            list with less than three unique entires
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ReplicationFactor' has not been provided or has been provided as an integer
#            value less than three (< 3)
#       And: 'AvailabilityZones' has been provided as a list with three or more unique entires
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ReplicationFactor' has been provided as an integer value greater than or
#            equal to three (>= 3)
#       And: 'AvailabilityZones' has been provided as a list with three or more unique entires
#      Then: PASS

#
# Constants
#
let DAX_CLUSTER_TYPE = "AWS::DAX::Cluster"
let MINIMUM_NODE_COUNT = 3
let INPUT_DOCUMENT = this

#
# Assignments
#
let dax_clusters = Resources.*[ Type == %DAX_CLUSTER_TYPE ]

#
# Primary Rules
#
rule dax_cluster_multi_az_check when is_cfn_template(%INPUT_DOCUMENT)
                                     %dax_clusters not empty {
    check(%dax_clusters.Properties)
        <<
        [CT.DAX.PR.2]: Require an Amazon DAX cluster to deploy nodes to at least three Availability Zones
        [FIX]: Set the 'ReplicationFactor' parameter to an integer value greater than or equal to three (>= 3), and set the 'AvailabilityZones' parameter to a list containing three unique Availability Zone entries.
        >>
}

rule dax_cluster_multi_az_check when is_cfn_hook(%INPUT_DOCUMENT, %DAX_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%DAX_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.DAX.PR.2]: Require an Amazon DAX cluster to deploy nodes to at least three Availability Zones
        [FIX]: Set the 'ReplicationFactor' parameter to an integer value greater than or equal to three (>= 3), and set the 'AvailabilityZones' parameter to a list containing three unique Availability Zone entries.
        >>
}

#
# Parameterized Rules
#
rule check(dax_cluster) {
    %dax_cluster {
        # Scenario 2
        ReplicationFactor exists

        AvailabilityZones exists
        AvailabilityZones is_list
        AvailabilityZones not empty

        # Scenarios 3, 4 and 5
        ReplicationFactor >= %MINIMUM_NODE_COUNT

        AvailabilityZones[0] exists
        AvailabilityZones[1] exists
        AvailabilityZones[2] exists

        let az_one = AvailabilityZones[0]
        let az_two = AvailabilityZones[1]
        let az_three = AvailabilityZones[2]

        check_az_is_unique(%az_one, %az_two, %az_three)
        check_az_is_unique(%az_two, %az_one, %az_three)
    }
}

rule check_az_is_unique(az, first_az, second_az) {
    %az not in %first_az
    %az not in %second_az
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

### CT.DAX.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DaxDynamoAccessRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: dax.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: DynamoAccessPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - dynamodb:DescribeTable
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Query
            - dynamodb:Scan
            - dynamodb:BatchGetItem
            - dynamodb:BatchWriteItem
            - dynamodb:ConditionCheckItem
            Resource:
              Fn::Sub: arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:*
  DaxCluster:
    Type: AWS::DAX::Cluster
    Properties:
      IAMRoleARN:
        Fn::GetAtt:
        - DaxDynamoAccessRole
        - Arn
      NodeType: dax.t3.small
      ReplicationFactor: 3
      AvailabilityZones:
      - Fn::Select:
        - 0
        - Fn::GetAZs: ''
      - Fn::Select:
        - 1
        - Fn::GetAZs: ''
      - Fn::Select:
        - 2
        - Fn::GetAZs: ''


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DaxDynamoAccessRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: dax.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: DynamoAccessPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - dynamodb:DescribeTable
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Query
            - dynamodb:Scan
            - dynamodb:BatchGetItem
            - dynamodb:BatchWriteItem
            - dynamodb:ConditionCheckItem
            Resource:
              Fn::Sub: arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:*
  DaxCluster:
    Type: AWS::DAX::Cluster
    Properties:
      IAMRoleARN:
        Fn::GetAtt:
        - DaxDynamoAccessRole
        - Arn
      NodeType: dax.t3.small
      ReplicationFactor: 3


```

## [CT.DAX.PR.3] Require an Amazon DAX cluster to encrypt data in transit with Transport Layer Security (TLS)

This control checks whether an Amazon DynamoDB Accelerator (DAX) cluster endpoint is configured to encrypt data in transit with Transport Layer Security (TLS).

- **Control objective:** Encrypt data in transit
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::DAX::Cluster`
- **AWS CloudFormation guard rule:**
  [CT.DAX.PR.3 rule specification](#ct-dax-pr-3-rule "#ct-dax-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.DAX.PR.3 rule specification](#ct-dax-pr-3-rule "#ct-dax-pr-3-rule")
- For examples of PASS and FAIL AWS CloudFormation Templates related to
  this control, see:
  [CT.DAX.PR.3 example templates](#ct-dax-pr-3-templates "#ct-dax-pr-3-templates")

**Explanation**

Amazon DynamoDB Accelerator (DAX) supports encryption in transit of data between your application and your DAX cluster,
so that you can use DAX in applications with stringent encryption requirements. DAX encryption in transit ensures
that all requests and responses between the application and the cluster are encrypted by transport level security (TLS),
and that connections to the cluster can be authenticated by verification of a cluster x509 certificate.

###### Usage considerations

- To enable encryption in transit between your application and DAX cluster, be sure to use a
  recent version of any of the DAX clients that support TLS in your application.

Encryption in transit cannot be enabled on an existing DAX cluster. To use encryption in transit in an existing DAX
application, create a new cluster with encryption in transit enabled, shift your application's traffic to it, then
delete the old cluster.

### Remediation for rule failure

Set the value of the ClusterEndpointEncryptionType property to TLS.

The examples that follow show how to implement this remediation.

#### Amazon DAX Cluster - Example

An Amazon DAX cluster configured to encrypt data in transit. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "DaxCluster": {
        "Type": "AWS::DAX::Cluster",
        "Properties": {
            "IAMRoleARN": {
                "Fn::GetAtt": [
                    "DaxDynamoAccessRole",
                    "Arn"
                ]
            },
            "NodeType": "dax.t3.small",
            "ReplicationFactor": 3,
            "ClusterEndpointEncryptionType": "TLS"
        }
    }
}

```

**YAML example**

```

DaxCluster:
  Type: AWS::DAX::Cluster
  Properties:
    IAMRoleARN: !GetAtt 'DaxDynamoAccessRole.Arn'
    NodeType: dax.t3.small
    ReplicationFactor: 3
    ClusterEndpointEncryptionType: TLS


```

### CT.DAX.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   dax_tls_endpoint_encryption_check
#
# Description:
#   This control checks whether an Amazon DAX cluster endpoint is configured to encrypt data in transit with Transport Layer Security (TLS).
#
# Reports on:
#   AWS::DAX::Cluster
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
#       And: The input document does not contain any DAX cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ClusterEndpointEncryptionType' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ClusterEndpointEncryptionType' has been provided and set to a value other than 'TLS'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains a DAX cluster resource
#       And: 'ClusterEndpointEncryptionType' has been provided and set to 'TLS'
#      Then: PASS

#
# Constants
#
let DAX_CLUSTER_TYPE = "AWS::DAX::Cluster"
let ALLOWED_CLUSTER_ENCRYPTION_TYPES = [ "TLS" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let dax_clusters = Resources.*[ Type == %DAX_CLUSTER_TYPE ]

#
# Primary Rules
#
rule dax_tls_endpoint_encryption_check when is_cfn_template(%INPUT_DOCUMENT)
                                            %dax_clusters not empty {
    check(%dax_clusters.Properties)
        <<
        [CT.DAX.PR.3]: Require an Amazon DAX cluster to encrypt data in transit with Transport Layer Security (TLS)
        [FIX]: Set the value of the ClusterEndpointEncryptionType property to TLS.
        >>
}

rule dax_tls_endpoint_encryption_check when is_cfn_hook(%INPUT_DOCUMENT, %DAX_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%DAX_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.DAX.PR.3]: Require an Amazon DAX cluster to encrypt data in transit with Transport Layer Security (TLS)
        [FIX]: Set the value of the ClusterEndpointEncryptionType property to TLS.
        >>
}

#
# Parameterized Rules
#
rule check(dax_cluster) {
    %dax_cluster {
        # Scenario 2
        ClusterEndpointEncryptionType exists

        # Scenarios 3 and 4
        ClusterEndpointEncryptionType in %ALLOWED_CLUSTER_ENCRYPTION_TYPES
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

### CT.DAX.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  DaxDynamoAccessRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: dax.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: DynamoAccessPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - dynamodb:DescribeTable
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Query
            - dynamodb:Scan
            - dynamodb:BatchGetItem
            - dynamodb:BatchWriteItem
            - dynamodb:ConditionCheckItem
            Resource:
              Fn::Sub: arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:*
  DaxCluster:
    Type: AWS::DAX::Cluster
    Properties:
      IAMRoleARN:
        Fn::GetAtt:
        - DaxDynamoAccessRole
        - Arn
      NodeType: dax.t3.small
      ReplicationFactor: 3
      ClusterEndpointEncryptionType: TLS


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  DaxDynamoAccessRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: dax.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: DynamoAccessPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - dynamodb:DescribeTable
            - dynamodb:PutItem
            - dynamodb:GetItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
            - dynamodb:Query
            - dynamodb:Scan
            - dynamodb:BatchGetItem
            - dynamodb:BatchWriteItem
            - dynamodb:ConditionCheckItem
            Resource:
              Fn::Sub: arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:*
  DaxCluster:
    Type: AWS::DAX::Cluster
    Properties:
      IAMRoleARN:
        Fn::GetAtt:
        - DaxDynamoAccessRole
        - Arn
      NodeType: dax.t3.small
      ReplicationFactor: 3
      ClusterEndpointEncryptionType: NONE


```
