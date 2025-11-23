# Amazon Elastic Kubernetes Service (EKS) controls

###### Topics

- [[CT.EKS.PR.1] Require an Amazon EKS cluster to be configured with public access disabled to the cluster Kubernetes API server endpoint](#ct-eks-pr-1-description "#ct-eks-pr-1-description")
- [[CT.EKS.PR.2] Require an Amazon EKS cluster to be configured with secret encryption using AWS Key Management Service (KMS) keys](#ct-eks-pr-2-description "#ct-eks-pr-2-description")

## [CT.EKS.PR.1] Require an Amazon EKS cluster to be configured with public access disabled to the cluster Kubernetes API server endpoint

This control checks whether an Amazon Elastic Kubernetes Service (EKS) cluster endpoint disallows public access to the cluster Kubernetes API server endpoint.

- **Control objective:** Limit network access
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::EKS::Cluster`
- **CloudFormation guard rule:**
  [CT.EKS.PR.1 rule specification](#ct-eks-pr-1-rule "#ct-eks-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.EKS.PR.1 rule specification](#ct-eks-pr-1-rule "#ct-eks-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.EKS.PR.1 example templates](#ct-eks-pr-1-templates "#ct-eks-pr-1-templates")

**Explanation**

When you create a new cluster, Amazon Elastic Kubernetes Service (EKS) creates an endpoint for the managed Kubernetes API server, which you can use to communicate with your cluster using Kubernetes management tools, such as `kubectl`. By default, this API server endpoint is public to the internet, and access to the API server is secured using a combination of AWS Identity and Access Management (IAM) along with native Kubernetes Role-Based Access Control (RBAC). Enabling private access to the Kubernetes API server ensures that all communication between your nodes and the API server stays within your VPC. You can limit the IP addresses that have access to your API server from the internet, or you can completely disallow internet access to the API server.

### Remediation for rule failure

Set the value of the `EndpointPublicAccess` parameter to false and the value of the `EndpointPrivateAccess` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon EKS Cluster - Example

An Amazon EKS cluster configured with public access disabled to the cluster's Kubernetes API server endpoint. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "EKSCluster": {
        "Type": "AWS::EKS::Cluster",
        "Properties": {
            "RoleArn": {
                "Fn::GetAtt": "EKSClusterRole.Arn"
            },
            "ResourcesVpcConfig": {
                "SubnetIds": [
                    {
                        "Ref": "SubnetOne"
                    },
                    {
                        "Ref": "SubnetTwo"
                    }
                ],
                "EndpointPublicAccess": false,
                "EndpointPrivateAccess": true
            }
        }
    }
}

```

**YAML example**

```

EKSCluster:
  Type: AWS::EKS::Cluster
  Properties:
    RoleArn: !GetAtt 'EKSClusterRole.Arn'
    ResourcesVpcConfig:
      SubnetIds:
        - !Ref 'SubnetOne'
        - !Ref 'SubnetTwo'
      EndpointPublicAccess: false
      EndpointPrivateAccess: true


```

### CT.EKS.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   eks_endpoint_no_public_access_check
#
# Description:
#   This control checks whether an Amazon Elastic Kubernetes Service (EKS) cluster endpoint disallows public access to the cluster Kubernetes API server endpoint.
#
# Reports on:
#   AWS::EKS::Cluster
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
#       And: The input document does not contain any Amazon EKS cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EndpointPublicAccess' in 'ResourcesVpcConfig' has not been provided
#       And: 'EndpointPrivateAccess' in 'ResourcesVpcConfig' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EndpointPrivateAccess' in 'ResourcesVpcConfig' has not been provided
#       And: 'EndpointPublicAccess' in 'ResourcesVpcConfig' has not been provided or has been provided and set to a
#            value other than bool(false)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EndpointPublicAccess' in 'ResourcesVpcConfig' has not been provided or has been provided and set to a
#            value other than bool(false)
#       And: 'EndpointPrivateAccess' in 'ResourcesVpcConfig' has been provided and set a value other than bool(true)
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EndpointPublicAccess' in 'ResourcesVpcConfig' has been provided and set to bool(false)
#       And: 'EndpointPrivateAccess' in 'ResourcesVpcConfig' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let EKS_CLUSTER_TYPE = "AWS::EKS::Cluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let eks_clusters = Resources.*[ Type == %EKS_CLUSTER_TYPE ]

#
# Primary Rules
#
rule eks_endpoint_no_public_access_check when is_cfn_template(%INPUT_DOCUMENT)
                                              %eks_clusters not empty {
    check(%eks_clusters.Properties)
        <<
        [CT.EKS.PR.1]: Require an Amazon EKS cluster to be configured with public access disabled to the cluster Kubernetes API server endpoint.
        [FIX]: Set the value of the 'EndpointPublicAccess' parameter to false and the value of the 'EndpointPrivateAccess' parameter to true.
        >>
}

rule eks_endpoint_no_public_access_check when is_cfn_hook(%INPUT_DOCUMENT, %EKS_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%EKS_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.EKS.PR.1]: Require an Amazon EKS cluster to be configured with public access disabled to the cluster Kubernetes API server endpoint.
        [FIX]: Set the value of the 'EndpointPublicAccess' parameter to false and the value of the 'EndpointPrivateAccess' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(eks_cluster) {
    %eks_cluster {
        ResourcesVpcConfig exists
        ResourcesVpcConfig is_struct
        ResourcesVpcConfig {
            # Scenarios 2, 3, 4 and 5
            EndpointPublicAccess exists
            EndpointPublicAccess == false

            EndpointPrivateAccess exists
            EndpointPrivateAccess == true
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

### CT.EKS.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  SubnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetTwo:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ''
  EKSClusterRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: eks.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
  EKSCluster:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn:
        Fn::GetAtt: EKSClusterRole.Arn
      ResourcesVpcConfig:
        SubnetIds:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        EndpointPublicAccess: false
        EndpointPrivateAccess: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  SubnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetTwo:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ''
  EKSClusterRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: eks.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
  EKSCluster:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn:
        Fn::GetAtt: EKSClusterRole.Arn
      ResourcesVpcConfig:
        SubnetIds:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        EndpointPublicAccess: true
        EndpointPrivateAccess: false


```

## [CT.EKS.PR.2] Require an Amazon EKS cluster to be configured with secret encryption using AWS Key Management Service (KMS) keys

This control checks whether Amazon Elastic Kubernetes Service (Amazon EKS) clusters are configured to use Kubernetes secrets encrypted with AWS Key Management Service (KMS) keys.

- **Control objective:** Encrypt data at rest
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::EKS::Cluster`
- **CloudFormation guard rule:**
  [CT.EKS.PR.2 rule specification](#ct-eks-pr-2-rule "#ct-eks-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.EKS.PR.2 rule specification](#ct-eks-pr-2-rule "#ct-eks-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.EKS.PR.2 example templates](#ct-eks-pr-2-templates "#ct-eks-pr-2-templates")

**Explanation**

Kubernetes secrets store sensitive information, such as user certificates, passwords, or API keys. Encrypting Kubernetes secrets at rest bolsters the security of your EKS clusters.

###### Usage considerations

- For a cluster that uses KMS Envelope Encryption, `kms:CreateGrant` permissions are required. The condition `kms:GrantIsForAWSResource` is not supported for the CreateCluster action, and this condition should not be given in KMS policies to control `kms:CreateGrant` permissions for users performing CreateCluster operations.

### Remediation for rule failure

Provide an `EncryptionConfig` configuration with a list of `Resources` that contains `secrets` and a `Provider` configuration containing a `KeyArn`.

The examples that follow show how to implement this remediation.

#### Amazon EKS cluster - Example

Amazon EKS cluster configured to have Kubernetes secrets encrypted using Amazon Elastic Kubernetes Service (KMS) keys. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "EKSCluster": {
        "Type": "AWS::EKS::Cluster",
        "Properties": {
            "RoleArn": {
                "Fn::GetAtt": [
                    "EKSClusterRole",
                    "Arn"
                ]
            },
            "ResourcesVpcConfig": {
                "SubnetIds": [
                    {
                        "Ref": "SubnetOne"
                    },
                    {
                        "Ref": "SubnetTwo"
                    }
                ],
                "EndpointPublicAccess": false,
                "EndpointPrivateAccess": true
            },
            "Logging": {
                "ClusterLogging": {
                    "EnabledTypes": [
                        {
                            "Type": "api"
                        },
                        {
                            "Type": "audit"
                        },
                        {
                            "Type": "authenticator"
                        },
                        {
                            "Type": "controllerManager"
                        },
                        {
                            "Type": "scheduler"
                        }
                    ]
                }
            },
            "EncryptionConfig": [
                {
                    "Resources": [
                        "secrets"
                    ],
                    "Provider": {
                        "KeyArn": {
                            "Fn::GetAtt": [
                                "KMSKey",
                                "Arn"
                            ]
                        }
                    }
                }
            ]
        }
    }
}

```

**YAML example**

```

EKSCluster:
  Type: AWS::EKS::Cluster
  Properties:
    RoleArn: !GetAtt 'EKSClusterRole.Arn'
    ResourcesVpcConfig:
      SubnetIds:
        - !Ref 'SubnetOne'
        - !Ref 'SubnetTwo'
      EndpointPublicAccess: false
      EndpointPrivateAccess: true
    Logging:
      ClusterLogging:
        EnabledTypes:
          - Type: api
          - Type: audit
          - Type: authenticator
          - Type: controllerManager
          - Type: scheduler
    EncryptionConfig:
      - Resources:
          - secrets
        Provider:
          KeyArn: !GetAtt 'KMSKey.Arn'


```

### CT.EKS.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   eks_secrets_encrypted_check
#
# Description:
#   This control checks whether Amazon Elastic Kubernetes Service (Amazon EKS) clusters are configured to use Kubernetes secrets encrypted with AWS Key Management Service (KMS) keys.
#
# Reports on:
#   AWS::EKS::Cluster
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
#       And: The input document does not contain any Amazon EKS cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EncryptionConfig' has not been provided or provided as an empty list
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EncryptionConfig' has been provided as a non-empty list
#       And: There are no entries in 'EncryptionConfig' where 'Resources' has been provided
#            as a non-empty list with at least one value equal to 'secrets'
#       And: For the same entry in 'EncryptionConfig', where 'KeyArn' in 'Provider' has been
#            provided as a non-empty string or valid local reference to a KMS key or key alias
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon EKS cluster resource
#       And: 'EncryptionConfig' has been provided as a non-empty list
#       And: For at least one entry in 'EncryptionConfig', 'Resources' has been provided as a
#            non-empty list with at least one value equal to 'secrets'
#       And: For the same entry in 'EncryptionConfig', 'KeyArn' in 'Provider' has been provided
#            as a non-empty string or valid local reference to a KMS key or key alias
#      Then: PASS

#
# Constants
#
let EKS_CLUSTER_TYPE = "AWS::EKS::Cluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let eks_clusters = Resources.*[ Type == %EKS_CLUSTER_TYPE ]

#
# Primary Rules
#
rule eks_secrets_encrypted_check when is_cfn_template(%INPUT_DOCUMENT)
                                      %eks_clusters not empty {
    check(%eks_clusters.Properties)
        <<
        [CT.EKS.PR.2]: Require an Amazon EKS cluster to be configured with secret encryption using AWS Key Management Service (KMS) keys
        [FIX]: Provide an 'EncryptionConfig' configuration with a list of 'Resources' that contains 'secrets' and a 'Provider' configuration containing a 'KeyArn'.
        >>
}

rule eks_secrets_encrypted_check when is_cfn_hook(%INPUT_DOCUMENT, %EKS_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%EKS_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.EKS.PR.2]: Require an Amazon EKS cluster to be configured with secret encryption using AWS Key Management Service (KMS) keys
        [FIX]: Provide an 'EncryptionConfig' configuration with a list of 'Resources' that contains 'secrets' and a 'Provider' configuration containing a 'KeyArn'.
        >>
}

#
# Parameterized Rules
#
rule check(eks_cluster) {
    %eks_cluster {
        # Scenario 2
        EncryptionConfig exists
        EncryptionConfig is_list
        EncryptionConfig not empty

        # Scenario 3 and 4
        some EncryptionConfig[*] {
            Resources exists
            Resources is_list
            Resources not empty
            some Resources[*] == "secrets"

            Provider exists
            Provider is_struct
            Provider {
                KeyArn exists
                check_is_string_and_not_empty(KeyArn) or
                check_local_references(%INPUT_DOCUMENT, KeyArn, "AWS::KMS::Key") or
                check_local_references(%INPUT_DOCUMENT, KeyArn, "AWS::KMS::Alias")
            }
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

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}

rule check_local_references(doc, reference_properties, referenced_resource_type) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0], %referenced_resource_type)
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this, %referenced_resource_type)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key, referenced_resource_type) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %referenced_resource_type
    }
}


```

### CT.EKS.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  SubnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetTwo:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ''
  EKSClusterRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: eks.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
  KMSKey:
    Type: AWS::KMS::Key
    Properties:
      PendingWindowInDays: 7
      KeyPolicy:
        Version: 2012-10-17
        Id: example-key-policy
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Sub: arn:${AWS::Partition}:iam::${AWS::AccountId}:root
          Action: kms:*
          Resource: '*'
      KeySpec: SYMMETRIC_DEFAULT
  EKSCluster:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn:
        Fn::GetAtt:
        - EKSClusterRole
        - Arn
      ResourcesVpcConfig:
        SubnetIds:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        EndpointPublicAccess: false
        EndpointPrivateAccess: true
      Logging:
        ClusterLogging:
          EnabledTypes:
          - Type: api
          - Type: audit
          - Type: authenticator
          - Type: controllerManager
          - Type: scheduler
      EncryptionConfig:
      - Resources:
        - secrets
        Provider:
          KeyArn:
            Fn::GetAtt: [KMSKey, Arn]


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  SubnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetTwo:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ''
  EKSClusterRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service: eks.amazonaws.com
          Action: sts:AssumeRole
      Path: /
      ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AmazonEKSClusterPolicy
  EKSCluster:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn:
        Fn::GetAtt:
        - EKSClusterRole
        - Arn
      ResourcesVpcConfig:
        SubnetIds:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        EndpointPublicAccess: false
        EndpointPrivateAccess: true
      Logging:
        ClusterLogging:
          EnabledTypes:
          - Type: api
          - Type: audit
          - Type: authenticator
          - Type: controllerManager
          - Type: scheduler


```
