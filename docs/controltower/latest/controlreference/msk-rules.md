# Amazon Managed Streaming for Apache Kafka (Amazon MSK) controls

###### Topics

- [[CT.MSK.PR.1] Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to enforce encryption in transit between cluster broker nodes](#ct-msk-pr-1-description "#ct-msk-pr-1-description")
- [[CT.MSK.PR.2] Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to be configured with PublicAccess disabled](#ct-msk-pr-2-description "#ct-msk-pr-2-description")

## [CT.MSK.PR.1] Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to enforce encryption in transit between cluster broker nodes

This control checks whether an Amazon MSK cluster is configured to encrypt data in transit between broker nodes of the cluster.

- **Control objective:** Encrypt data in transit
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::MSK::Cluster`
- **CloudFormation guard rule:**
  [CT.MSK.PR.1 rule specification](#ct-msk-pr-1-rule "#ct-msk-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.MSK.PR.1 rule specification](#ct-msk-pr-1-rule "#ct-msk-pr-1-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.MSK.PR.1 example templates](#ct-msk-pr-1-templates "#ct-msk-pr-1-templates")

**Explanation**

Amazon MSK uses TLSv1.2. By default, it encrypts data in transit between the brokers of your Amazon MSK cluster. However, you can override this
default at the time you create the cluster.

###### Usage considerations

- Although we highly recommend enabling in-transit encryption, it can add additional CPU overhead and a few milliseconds of latency.
  Most use cases aren't sensitive to these differences, and the magnitude of impact depends on the configuration of your cluster, clients, and usage profile.

### Remediation for rule failure

In the EncryptionInfo property, provide an `EncryptionInTransit` configuration and set the value of `InCluster` to true. Otherwise, omit the `InCluster` property to adopt the default value of true.

The examples that follow show how to implement this remediation.

#### Amazon MSK Cluster - Example

An Amazon MSK cluster configured to encrypt data in transit between the broker nodes of the cluster. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "MSKCluster": {
        "Type": "AWS::MSK::Cluster",
        "Properties": {
            "BrokerNodeGroupInfo": {
                "ClientSubnets": [
                    {
                        "Ref": "SubnetOne"
                    },
                    {
                        "Ref": "SubnetTwo"
                    }
                ],
                "InstanceType": "kafka.t3.small",
                "SecurityGroups": [
                    {
                        "Fn::GetAtt": [
                            "SecurityGroup",
                            "GroupId"
                        ]
                    }
                ],
                "StorageInfo": {
                    "EBSStorageInfo": {
                        "VolumeSize": 1000
                    }
                }
            },
            "ClusterName": {
                "Fn::Sub": "MSKCluster-${AWS::StackName}"
            },
            "KafkaVersion": "3.4.0",
            "NumberOfBrokerNodes": 2,
            "EnhancedMonitoring": "DEFAULT",
            "EncryptionInfo": {
                "EncryptionInTransit": {
                    "InCluster": true
                }
            }
        }
    }
}

```

**YAML example**

```

MSKCluster:
  Type: AWS::MSK::Cluster
  Properties:
    BrokerNodeGroupInfo:
      ClientSubnets:
        - !Ref 'SubnetOne'
        - !Ref 'SubnetTwo'
      InstanceType: kafka.t3.small
      SecurityGroups:
        - !GetAtt 'SecurityGroup.GroupId'
      StorageInfo:
        EBSStorageInfo:
          VolumeSize: 1000
    ClusterName: !Sub 'MSKCluster-${AWS::StackName}'
    KafkaVersion: 3.4.0
    NumberOfBrokerNodes: 2
    EnhancedMonitoring: DEFAULT
    EncryptionInfo:
      EncryptionInTransit:
        InCluster: true


```

### CT.MSK.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   msk_broker_node_tls_check
#
# Description:
#   This control checks whether an Amazon MSK cluster is configured to encrypt data in transit between broker nodes of the cluster.
#
# Reports on:
#   AWS::MSK::Cluster
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
#       And: The input document does not contain any Amazon MSK cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon MSK cluster resource
#       And: 'InCluster' in 'EncryptionInfo.EncryptionInTransit' has been provided and
#            set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon MSK cluster resource
#       And: 'InCluster' in 'EncryptionInfo.EncryptionInTransit' has not been provided
#      Then: PASS
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon MSK cluster resource
#       And: 'InCluster' in 'EncryptionInfo.EncryptionInTransit' has been provided and
#            set to bool(true)
#      Then: PASS

#
# Constants
#
let MSK_CLUSTER_TYPE = "AWS::MSK::Cluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let msk_clusters = Resources.*[ Type == %MSK_CLUSTER_TYPE ]

#
# Primary Rules
#
rule msk_broker_node_tls_check when is_cfn_template(%INPUT_DOCUMENT)
                                    %msk_clusters not empty {
    check(%msk_clusters.Properties)
        <<
        [CT.MSK.PR.1]: Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to enforce encryption in transit between cluster broker nodes
        [FIX]: In the EncryptionInfo property, provide an 'EncryptionInTransit' configuration and set the value of 'InCluster' to true. Otherwise, omit the 'InCluster' property to adopt the default value of true.
        >>
}

rule msk_broker_node_tls_check when is_cfn_hook(%INPUT_DOCUMENT, %MSK_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%MSK_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.MSK.PR.1]: Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to enforce encryption in transit between cluster broker nodes
        [FIX]: In the EncryptionInfo property, provide an 'EncryptionInTransit' configuration and set the value of 'InCluster' to true. Otherwise, omit the 'InCluster' property to adopt the default value of true.
        >>
}

#
# Parameterized Rules
#
rule check(msk_cluster) {
    %msk_cluster {
        # Scenario 3
        EncryptionInfo not exists or
        # Scenarios 2 and 4
        check_encryption_info_config(this)
    }
}

 rule check_encryption_info_config(msk_cluster) {
     %msk_cluster {
        EncryptionInfo exists
        EncryptionInfo is_struct

        EncryptionInfo {
            EncryptionInTransit not exists or
            check_encryption_in_transit_config(this)
        }
     }
 }

 rule check_encryption_in_transit_config(encryption_info_config) {
     %encryption_info_config {
        EncryptionInTransit exists
        EncryptionInTransit is_struct

        EncryptionInTransit {
            InCluster not exists or
            InCluster == true
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

### CT.MSK.PR.1 example templates

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
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: MSK Security Group
      SecurityGroupIngress:
      - Description: ZooKeeper plaintext
        FromPort: 2181
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 2181
      - Description: Bootstrap servers plaintext
        FromPort: 9092
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9092
      - Description: Bootstrap servers TLS
        FromPort: 9094
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9094
      VpcId:
        Ref: VPC
  MSKCluster:
    Type: AWS::MSK::Cluster
    Properties:
      BrokerNodeGroupInfo:
        ClientSubnets:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        InstanceType: kafka.t3.small
        SecurityGroups:
        - Fn::GetAtt:
          - SecurityGroup
          - GroupId
        StorageInfo:
          EBSStorageInfo:
            VolumeSize: 1000
      ClusterName:
        Fn::Sub: MSKCluster-${AWS::StackName}
      KafkaVersion: 3.4.0
      NumberOfBrokerNodes: 2
      EnhancedMonitoring: DEFAULT
      EncryptionInfo:
        EncryptionInTransit:
          InCluster: true


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
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: MSK Security Group
      SecurityGroupIngress:
      - Description: ZooKeeper plaintext
        FromPort: 2181
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 2181
      - Description: Bootstrap servers plaintext
        FromPort: 9092
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9092
      - Description: Bootstrap servers TLS
        FromPort: 9094
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9094
      VpcId:
        Ref: VPC
  MSKCluster:
    Type: AWS::MSK::Cluster
    Properties:
      BrokerNodeGroupInfo:
        ClientSubnets:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        InstanceType: kafka.t3.small
        SecurityGroups:
        - Fn::GetAtt:
          - SecurityGroup
          - GroupId
        StorageInfo:
          EBSStorageInfo:
            VolumeSize: 1000
      ClusterName:
        Fn::Sub: MSKCluster-${AWS::StackName}
      KafkaVersion: 3.4.0
      NumberOfBrokerNodes: 2
      EnhancedMonitoring: DEFAULT
      EncryptionInfo:
        EncryptionInTransit:
          InCluster: false


```

## [CT.MSK.PR.2] Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to be configured with PublicAccess disabled

This control checks whether an Amazon MSK cluster is configured to disallow public access to cluster brokers by means of the PublicAccess property.

- **Control objective:** Limit network access
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::MSK::Cluster`
- **CloudFormation guard rule:**
  [CT.MSK.PR.2 rule specification](#ct-msk-pr-2-rule "#ct-msk-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.MSK.PR.2 rule specification](#ct-msk-pr-2-rule "#ct-msk-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.MSK.PR.2 example templates](#ct-msk-pr-2-templates "#ct-msk-pr-2-templates")

**Explanation**

Amazon MSK gives you the option to turn on public access to the brokers of Amazon MSK clusters that run Apache Kafka version 2.6.0 or later.
For security reasons, you can't turn on public access while creating an Amazon MSK cluster. However, you can update an existing cluster to make it publicly accessible.

###### Usage considerations

- In addition to configuring the PublicAccess property, other prerequisite conditions are required when you enable public access to Amazon MSK clusters. For more
  information on configuring Amazon MSK clusters for public access, see [Public Access](../../../msk/latest/developerguide/public-access.md "../../../msk/latest/developerguide/public-access.md") in the _Amazon MSK Developer Guide_.

### Remediation for rule failure

In the parameter BrokerNodeGroupInfo.ConnectivityInfo.PublicAccess, set the value of Type to DISABLED, or to adopt the default value of DISABLED, do not provide a PublicAccess configuration.

The examples that follow show how to implement this remediation.

#### Amazon MSK Cluster - Example

An Amazon MSK cluster configured to disallow public access to cluster brokers through the PublicAccess property. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "MSKCluster": {
        "Type": "AWS::MSK::Cluster",
        "Properties": {
            "ClusterName": {
                "Fn::Sub": "MSKCluster-${AWS::StackName}"
            },
            "KafkaVersion": "3.4.0",
            "NumberOfBrokerNodes": 2,
            "EnhancedMonitoring": "DEFAULT",
            "EncryptionInfo": {
                "EncryptionInTransit": {
                    "InCluster": true
                }
            },
            "ClientAuthentication": {
                "Sasl": {
                    "Iam": {
                        "Enabled": true
                    }
                }
            },
            "BrokerNodeGroupInfo": {
                "ClientSubnets": [
                    {
                        "Ref": "SubnetOne"
                    },
                    {
                        "Ref": "SubnetTwo"
                    }
                ],
                "InstanceType": "kafka.t3.small",
                "SecurityGroups": [
                    {
                        "Fn::GetAtt": [
                            "SecurityGroup",
                            "GroupId"
                        ]
                    }
                ],
                "StorageInfo": {
                    "EBSStorageInfo": {
                        "VolumeSize": 1000
                    }
                },
                "ConnectivityInfo": {
                    "PublicAccess": {
                        "Type": "DISABLED"
                    }
                }
            }
        }
    }
}

```

**YAML example**

```

MSKCluster:
  Type: AWS::MSK::Cluster
  Properties:
    ClusterName: !Sub 'MSKCluster-${AWS::StackName}'
    KafkaVersion: 3.4.0
    NumberOfBrokerNodes: 2
    EnhancedMonitoring: DEFAULT
    EncryptionInfo:
      EncryptionInTransit:
        InCluster: true
    ClientAuthentication:
      Sasl:
        Iam:
          Enabled: true
    BrokerNodeGroupInfo:
      ClientSubnets:
        - !Ref 'SubnetOne'
        - !Ref 'SubnetTwo'
      InstanceType: kafka.t3.small
      SecurityGroups:
        - !GetAtt 'SecurityGroup.GroupId'
      StorageInfo:
        EBSStorageInfo:
          VolumeSize: 1000
      ConnectivityInfo:
        PublicAccess:
          Type: DISABLED


```

### CT.MSK.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   msk_public_access_check
#
# Description:
#   This control checks whether an Amazon MSK cluster is configured to disallow public access to cluster brokers by means of the PublicAccess property.
#
# Reports on:
#   AWS::MSK::Cluster
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
#       And: The input document does not contain any Amazon MSK cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon MSK cluster resource
#       And: 'BrokerNodeGroupInfo' has not been provided
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an MSK cluster resource
#       And: 'BrokerNodeGroupInfo' has been provided
#       And: 'Type' in 'ConnectivityInfo.PublicAccess' has been provided and
#            set to a value other than 'DISABLED'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon MSK cluster resource
#       And: 'BrokerNodeGroupInfo' has been provided
#       And: 'Type' in 'ConnectivityInfo.PublicAccess' has not been provided
#      Then: PASS
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an Amazon MSK cluster resource
#       And: 'BrokerNodeGroupInfo' has been provided
#       And: 'Type' in 'ConnectivityInfo.PublicAccess' has been provided and
#            set to 'DISABLED'
#      Then: PASS

#
# Constants
#
let INPUT_DOCUMENT = this
let MSK_CLUSTER_TYPE = "AWS::MSK::Cluster"
let DISABLED_PUBLIC_ACCESS_TYPE = "DISABLED"

#
# Assignments
#
let msk_clusters = Resources.*[ Type == %MSK_CLUSTER_TYPE ]

#
# Primary Rules
#
rule msk_public_access_check when is_cfn_template(%INPUT_DOCUMENT)
                                  %msk_clusters not empty {
    check(%msk_clusters.Properties)
        <<
        [CT.MSK.PR.2]: Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to be configured with PublicAccess disabled
        [FIX]: In the parameter BrokerNodeGroupInfo.ConnectivityInfo.PublicAccess, set the value of Type to DISABLED, or to adopt the default value of DISABLED, do not provide a PublicAccess configuration.
        >>
}

rule msk_public_access_check when is_cfn_hook(%INPUT_DOCUMENT, %MSK_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%MSK_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.MSK.PR.2]: Require an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster to be configured with PublicAccess disabled
        [FIX]: In the parameter BrokerNodeGroupInfo.ConnectivityInfo.PublicAccess, set the value of Type to DISABLED, or to adopt the default value of DISABLED, do not provide a PublicAccess configuration.
        >>
}

#
# Parameterized Rules
#
rule check(msk_cluster) {
    %msk_cluster [
        # Scenario 2
        BrokerNodeGroupInfo exists
        BrokerNodeGroupInfo is_struct
    ] {
        BrokerNodeGroupInfo {
            # Scenarios 3, 4 and 5
            ConnectivityInfo not exists or
            check_connectivity_info_config(this)
        }
    }
}

 rule check_connectivity_info_config(broker_node_group_info) {
     %broker_node_group_info {
        ConnectivityInfo exists
        ConnectivityInfo is_struct

        ConnectivityInfo {
            PublicAccess not exists or
            check_public_access_config(this)
        }
     }
 }

 rule check_public_access_config(connectivity_info_config) {
     %connectivity_info_config {
        PublicAccess exists
        PublicAccess is_struct

        PublicAccess {
            Type not exists or
            Type == %DISABLED_PUBLIC_ACCESS_TYPE
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

### CT.MSK.PR.2 example templates

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
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: MSK Security Group
      SecurityGroupIngress:
      - Description: ZooKeeper plaintext
        FromPort: 2181
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 2181
      - Description: Bootstrap servers plaintext
        FromPort: 9092
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9092
      - Description: Bootstrap servers TLS
        FromPort: 9094
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9094
      VpcId:
        Ref: VPC
  MSKCluster:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName:
        Fn::Sub: MSKCluster-${AWS::StackName}
      KafkaVersion: 3.4.0
      NumberOfBrokerNodes: 2
      EnhancedMonitoring: DEFAULT
      EncryptionInfo:
        EncryptionInTransit:
          InCluster: true
      ClientAuthentication:
        Sasl:
          Iam:
            Enabled: true
      BrokerNodeGroupInfo:
        ClientSubnets:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        InstanceType: kafka.t3.small
        SecurityGroups:
        - Fn::GetAtt:
          - SecurityGroup
          - GroupId
        StorageInfo:
          EBSStorageInfo:
            VolumeSize: 1000
        ConnectivityInfo:
          PublicAccess:
            Type: DISABLED


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
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: MSK Security Group
      SecurityGroupIngress:
      - Description: ZooKeeper plaintext
        FromPort: 2181
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 2181
      - Description: Bootstrap servers plaintext
        FromPort: 9092
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9092
      - Description: Bootstrap servers TLS
        FromPort: 9094
        IpProtocol: tcp
        CidrIp:
          Fn::GetAtt:
          - VPC
          - CidrBlock
        ToPort: 9094
      VpcId:
        Ref: VPC
  MSKCluster:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName:
        Fn::Sub: MSKCluster-${AWS::StackName}
      KafkaVersion: 3.4.0
      NumberOfBrokerNodes: 2
      EnhancedMonitoring: DEFAULT
      EncryptionInfo:
        EncryptionInTransit:
          InCluster: true
      ClientAuthentication:
        Sasl:
          Iam:
            Enabled: true
      BrokerNodeGroupInfo:
        ClientSubnets:
        - Ref: SubnetOne
        - Ref: SubnetTwo
        InstanceType: kafka.t3.small
        SecurityGroups:
        - Fn::GetAtt:
          - SecurityGroup
          - GroupId
        StorageInfo:
          EBSStorageInfo:
            VolumeSize: 1000
        ConnectivityInfo:
          PublicAccess:
            Type: SERVICE_PROVIDED_EIPS


```
