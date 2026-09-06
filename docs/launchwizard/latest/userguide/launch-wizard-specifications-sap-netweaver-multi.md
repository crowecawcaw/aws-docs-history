

# SapNWOnHanaMulti
<a name="launch-wizard-specifications-sap-netweaver-multi"></a>

The following are examples of the specifications required to create multi-node deployments.

Multi-node deployment with HANA database software and infrastructure resources for all SAP components without installing SAP software:

```
{
  "KeyPairName": "ExampleKeyPair",
  "VpcId": "vpc-a1b2c3d4",
  "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
  "AvailabilityZone1PrivateSubnet2Id": "subnet-11111111bbbbbbbbb",
  "Timezone" :"PST",
  "EnableEbsVolumeEncryption" :"Yes",
  "EbsKmsKeyArn" : "arn:aws:kms:us-east-1:111122223333:alias/aws/ebs",
  "CreateSecurityGroup" :"No",
  "DatabaseSecurityGroupId" :"sg-1234567890abcdef0",
  "ApplicationSecurityGroupId" :"sg-021345abcdef6789",
  "SidAdmUserId" :"7002",
  "SapSysGroupId" :"5001",
  "DatabaseSystemId" :"HYD",
  "SapSid" :"S4K",
  "DatabaseInstanceNumber" :"30",
  "InstallAwsBackintAgent" :"Yes",
  "BackintSpecifications": "{\"backintBucketName\":\"launchwizardsoftware\",\"backintBucketFolder\":\"HANABackintBucketFolder\",\"backintBucketRegion\":\"us-east-1\",\"backintKmsKeyArn\":\"arn:aws:kms:us-east-1:111122223333:alias/aws/s3\",\"backintAgentVersion\":\"2.0.2.732\",\"backintContinueOnFailure\":\"No\",\"backintCreateEbsVolume\":\"Yes\"}",
  "PasOperatingSystem" :"SuSE-Linux-15-SP2-For-SAP-HVM",
  "PasAmiId" :"ami-1234567890abcdef0",
  "PasAutomaticRecovery" :"No",
  "PasInstanceType" :"r5.2xlarge",
  "PasHostname" :"pass4123",
  "InstallAas" :"Yes",
  "AasHostCount" :"2",
  "AasAutomaticRecovery" :"Yes",
  "AasInstanceType" :"r5.2xlarge",
  "AasHostnames" :"aas4123,aas4124",
  "DatabaseOperatingSystem" :"SuSE-Linux-15-SP2-For-SAP-HVM",
  "DatabaseAmiId" :"ami-1234567890abcdef0",
  "DatabaseInstanceType" :"r5.8xlarge",
  "DatabaseHostCount" :"2",
  "DatabasePrimaryHostname" :"db123",
  "DatabaseSubordinateHostnames" :"subhan1,subhana2",
  "SapPassword" :"EXAMPLE-PASSWORD",
  "InstallSap":"No",
  "InstallDatabaseSoftware" :"Yes",
  "DatabaseInstallationMediaS3Uri" :"s3://launchwizardsoftware/sapmedia/database/hana-20-sp06-rev60",
  "SetupTransportDomainController" :"No",
  "SnsTopicArn" :"arn:aws:sns:us-east-1:111122223333:InstallStatus",
  "SaveDeploymentArtifacts" :"Yes",
  "DeploymentArtifactsS3Uri" :"s3://launchwizardsoftware",
  "DisableDeploymentRollback" :"Yes",
  "ApplicationDataVolumeType": "gp3",    
  "DatabaseLogVolumeType": "gp3", 
  "DatabaseAutomaticRecovery": "Yes"
}
```

Multi-node deployment with resources for all SAP components without SAP software installed:

```
{
  "KeyPairName": "ExampleKeyPair",
  "VpcId": "vpc-a1b2c3d4",
  "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
  "AvailabilityZone1PrivateSubnet2Id": "subnet-11111111bbbbbbbbb",
  "Timezone" :"PST",
  "EnableEbsVolumeEncryption" :"Yes",
  "EbsKmsKeyArn" : "arn:aws:kms:us-east-1:111122223333:alias/aws/ebs",
  "CreateSecurityGroup" :"No",
  "DatabaseSecurityGroupId" :"sg-1234567890abcdef0",
  "ApplicationSecurityGroupId" :"sg-021345abcdef6789",
  "SidAdmUserId" :"7002",
  "SapSysGroupId" :"5001",
  "DatabaseSystemId" :"HYD",
  "SapSid" :"S4K",
  "DatabaseInstanceNumber" :"30",
  "PasOperatingSystem" :"SuSE-Linux-15-SP2-For-SAP-HVM",
  "PasAmiId" :"ami-1234567890abcdef0",
  "PasAutomaticRecovery" :"No",
  "PasInstanceType" :"r5.2xlarge",
  "PasHostname" :"pass4123",
  "InstallAas" :"Yes",
  "AasHostCount" :"2",
  "AasAutomaticRecovery" :"Yes",
  "AasInstanceType" :"r5.2xlarge",
  "AasHostnames" :"aas4123,aas4124",
  "DatabaseOperatingSystem" :"SuSE-Linux-15-SP2-For-SAP-HVM",
  "DatabaseAmiId" :"ami-1234567890abcdef0",
  "DatabaseInstanceType" :"r5.8xlarge",
  "DatabaseHostCount" :"2",
  "DatabasePrimaryHostname" :"aas4123",
  "DatabaseSubordinateHostnames" :"subhan1,subhana2",
  "SapPassword" :"EXAMPLE-PASSWORD",
  "InstallSap":"No",
  "InstallDatabaseSoftware" :"No",
  "InstallAwsBackintAgent" :"No",
  "SetupTransportDomainController" :"No",
  "SnsTopicArn" :"arn:aws:sns:us-east-1:111122223333:InstallStatus",
  "SaveDeploymentArtifacts" :"Yes",
  "DeploymentArtifactsS3Uri" :"s3://launchwizardsoftware",
  "DisableDeploymentRollback" :"Yes",  
  "ApplicationDataVolumeType": "gp3",    
  "DatabaseLogVolumeType": "gp3", 
  "DatabaseAutomaticRecovery": "Yes"
}
```

Multi-node deployment with SAP software installed:

```
{
  "KeyPairName": "ExampleKeyPair",
  "VpcId": "vpc-a1b2c3d4",
  "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
  "AvailabilityZone1PrivateSubnet2Id": "subnet-11111111bbbbbbbbb",
  "Timezone" :"PST",
  "EnableEbsVolumeEncryption" :"Yes",
  "EbsKmsKeyArn" : "arn:aws:kms:us-east-1:111122223333:alias/aws/ebs",
  "CreateSecurityGroup" :"No",
  "DatabaseSecurityGroupId" :"sg-1234567890abcdef0",
  "ApplicationSecurityGroupId" :"sg-021345abcdef6789",
  "SidAdmUserId" :"7002",
  "SapSysGroupId" :"5001",
  "DatabaseSystemId" :"HYD",
  "SapSid" :"S4K",
  "DatabaseInstanceNumber" :"30",
  "InstallAwsBackintAgent" :"Yes",
  "BackintSpecifications": "{\"backintBucketName\":\"launchwizardsoftware\",\"backintBucketFolder\":\"HANABackintBucketFolder\",\"backintBucketRegion\":\"us-east-1\",\"backintKmsKeyArn\":\"arn:aws:kms:us-east-1:111122223333:alias/aws/s3\",\"backintAgentVersion\":\"2.0.2.732\",\"backintContinueOnFailure\":\"No\",\"backintCreateEbsVolume\":\"Yes\"}",
  "PasOperatingSystem" :"SuSE-Linux-15-SP2-For-SAP-HVM",
  "PasAmiId" :"ami-1234567890abcdef0",
  "PasAutomaticRecovery" :"No",
  "PasInstanceType" :"r5.2xlarge",
  "PasHostname" :"pass4123",
  "InstallAas" :"Yes",
  "AasHostCount" :"2",
  "AasAutomaticRecovery" :"Yes",
  "AasInstanceType" :"r5.2xlarge",
  "AasHostnames" :"aas4123,aas4124",
  "DatabaseOperatingSystem" :"SuSE-Linux-15-SP2-For-SAP-HVM",
  "DatabaseAmiId" :"ami-1234567890abcdef0",
  "DatabaseInstanceType" :"r5.8xlarge",
  "DatabaseHostCount" :"2",
  "DatabasePrimaryHostname" :"aas4123",
  "DatabaseSubordinateHostnames" :"subhan1,subhana2",
  "SapPassword" :"EXAMPLE-PASSWORD",
  "InstallSap":"Yes",
  "SetupTransportDomainController" :"No",
  "SapInstallationSpecifications": "{\"parameters\":{\"PRODUCT_ID\":\"saps4hana-2021\",\"HDB_SCHEMA_NAME\":\"SAPABAP1\",\"CI_INSTANCE_NR\":\"22\",\"ASCS_INSTANCE_NR\":\"20\",\"SAPINST_CD_SAPCAR\":\"s3:\/\/launchwizardsoftware\/sapmedia\/sapcar\",\"SAPINST_CD_SWPM\":\"s3:\/\/launchwizardsoftware\/sapmedia\/swpm\/20-sp10\",\"SAPINST_CD_KERNEL\":\"s3:\/\/launchwizardsoftware\/sapmedia\/kernel\/785\",\"SAPINST_CD_LOAD\":\"s3:\/\/launchwizardsoftware\/sapmedia\/exports\/s4h-2021\",\"SAPINST_CD_RDBMS\":\"s3:\/\/launchwizardsoftware\/sapmedia\/database\/hana-20-sp06-rev60\",\"SAPINST_CD_RDBMS_CLIENT\":\"s3:\/\/launchwizardsoftware\/sapmedia\/hana-client\/20-11\"}, \"onFailureBehaviour\": \"CONTINUE\"}",
  "SnsTopicArn" :"arn:aws:sns:us-east-1:111122223333:InstallStatus",
  "SaveDeploymentArtifacts" :"Yes",
  "DeploymentArtifactsS3Uri" :"s3://launchwizardsoftware",
  "DisableDeploymentRollback" :"Yes",  
  "ApplicationDataVolumeType": "gp3",    
  "DatabaseLogVolumeType": "gp3", 
  "DatabaseAutomaticRecovery": "Yes"
}
```

Multi-node deployment with SAP Web Dispatcher, an Application Load Balancer with a secure protocol enabled, and SAP software installed:

```
{
  "AasAutomaticRecovery": "Yes",
  "AasHostCount": "1",
  "AasHostnames": "sapaas1",
  "AasInstanceType": "r5.4xlarge",
  "ApplicationDataVolumeType": "gp3",
  "applicationName": "WdT002zcpgc",
  "ApplicationSecurityGroupId": "sg-1234567890abcdef0",
  "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
  "AvailabilityZone2PrivateSubnet1Id": "subnet-22222222aaaaaaaaa",
  "CreateSecurityGroup": "No",
  "DatabaseAmiId": "ami-0bea9de14f254d7dd",
  "DatabaseAutomaticRecovery": "Yes",
  "DatabaseDataVolumeType": "gp3",
  "DatabaseHostCount": "3",
  "DatabaseInstanceNumber": "30",
  "DatabaseInstanceType": "r5.4xlarge",
  "DatabaseLogVolumeType": "gp3",
  "DatabaseOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
  "DatabasePrimaryHostname": "aas4123",
  "DatabaseSecurityGroupId": "sg-1234567890abcdef0",
  "DatabaseSubordinateHostnames": "subhana1,subhana2",
  "DatabaseSystemId": "HDB",
  "DisableDeploymentRollback": "Yes",
  "EnableEbsVolumeEncryption": "No",
  "InstallAas": "Yes",
  "InstallAwsBackintAgent": "No",
  "InstallDatabaseSoftware": "Yes",
  "InstallSap": "Yes",
  "InstallSapWebDispatcher": "Yes",
  "InstallWebDispatcherLoadBalancer": "Yes",
  "KeyPairName": "ExampleKeyPair",
  "PasAmiId": "ami-0bea9de14f254d7dd",
  "PasAutomaticRecovery": "Yes",
  "PasHostname": "sappas",
  "PasInstanceType": "r5.4xlarge",
  "PasOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
  "SapInstallationSpecifications": "{\"parameters\":{\"PRODUCT_ID\":\"sapNetweaver-752\",\"CI_INSTANCE_NR\":\"12\",\"ASCS_INSTANCE_NR\":\"10\",\"WD_INSTANCE_NR\":\"14\",\"SAPINST_CD_SAPCAR\":\"s3://launchwizard-example/sapcar/\",\"SAPINST_CD_SWPM\":\"s3://launchwizard-example/swpm/10-sp39/\",\"SAPINST_CD_KERNEL\":\"s3://launchwizard-example/kernel/\",\"SAPINST_CD_LOAD\":\"s3://launchwizard-example/exports/nw-752/\",\"SAPINST_CD_RDBMS\":\"s3://launchwizard-example/database/hana-20-sp07/\",\"SAPINST_CD_RDBMS_CLIENT\":\"s3://launchwizard-example/hana-client/20-11/\",\"SAPINST_CD_WD\":\"s3://launchwizard-example-us-east-1/webdisp/\"}}",
  "SapPassword": "EXAMPLE-PASSWORD",
  "SapSid": "SSD",
  "SapSysGroupId": "5001",
  "SaveDeploymentArtifacts": "No",
  "SetupTransportDomainController": "No",
  "SidAdmUserId": "7002",
  "Timezone": "UTC",
  "VpcId": "vpc-a1b2c3d4",
  "WebDispatcherAdminUserId": "5100",
  "WebDispatcherAmiId": "ami-0bea9de14f254d7dd",
  "WebDispatcherAutoRecovery": "Yes",
  "WebDispatcherAvailabilityZone1PrivateSubnetId": "subnet-11111111aaaaaaaaa",
  "WebDispatcherInstanceNumber": "14",
  "WebDispatcherInstanceType": "r5.4xlarge",
  "WebDispatcherLoadBalancerACMCertificateArn": "arn:aws:acm:region:account:certificate/certificate_ID",
  "WebDispatcherLoadBalancerAvailabilityZone1SubnetId": "subnet-11111111aaaaaaaaa",
  "WebDispatcherLoadBalancerAvailabilityZone2SubnetId": "subnet-22222222aaaaaaaaa",
  "WebDispatcherLoadBalancerInternetFacing": "No",
  "WebDispatcherLoadBalancerSecureProtocolEnabled": "Yes",
  "WebDispatcherLoadBalancerSecurityGroupId": "sg-1234567890abcdef0",
  "WebDispatcherLoadBalancerType": "ALB",
  "WebDispatcherOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
  "WebDispatcherSecurityGroupId": "sg-1234567890abcdef0",
  "WebDispatcherServerHostname": "sapwd",
  "WebDispatcherSystemId": "WDD",
  "WebDispatcherVersion": "7.93"
}
```

The following list describes each specification input:
+ **KeyPairName**

  Type: String

  Constraints: Up to 255 ASCII characters

  Example: home

  Description: The name of an existing Amazon EC2 key pair. All instances will launch with this key pair.

  Required: Yes
+ **VpcId**

  Type: String

  Example: vpc-01234567890

  Description: The existing Amazon VPC where you want to deploy the system.

  Required: Yes
+ **AvailabilityZone1PrivateSubnet1Id**

  Type: String

  Example: subnet-11111111aaaaaaaaa

  Description: The existing private subnet where you want to deploy the system.

  Required: Yes
+ **AvailabilityZone1PrivateSubnet2Id**

  Type: String

  Example: subnet-11111111bbbbbbbbb

  Description: The existing private subnet where you want to deploy the system.

  Required: Yes
+ **ProxyServerAddress**

  Type: String

  Example: http://10.x.x.x:8080

  Description: The `ProxyServerAddress` address for http access. For example, {{http://xyz.abc.com:8080}} or {{http://10.x.x.x:8080}}.

  Required: No
+ **NoProxy**

  Type: String

  Example: http://10.x.x.x:8080

  Description: A comma separated list of URLs, CIDR ranges, or IP addresses for which to disable ProxyServerAddress settings using the `NO_ProxyServerAddress` environment variable. You can specify input for this specification when input has been provided for `ProxyServerAddress`. Any values you specify are appended to the default configuration for the `NO_ProxyServerAddress` environment variable. The following entries are used by default:

  `NO_ProxyServerAddress="localhost,127.0.0.1,169.254.169.254,.internal,{VPC_CIDR_RANGE}"`

  Required: No
+ **Timezone**

  Type: String

  Example: UTC

  Description: The time zone to configure for your SAP resources.

  Required: Yes
+ **EnableEbsVolumeEncryption**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to encrypt the EBS volumes used for the deployment. 

  Required: Yes
+ **EbsKmsKeyArn**

  Type: String

  Example: arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

  Description: Specifies a KMS key ARN for encrypting EBS volumes when `EnableEbsVolumeEncryption` is set to `Yes`.

  Conditional: If `EnableEbsVolumeEncryption` is `Yes`, you must specify a KMS key ARN.

  Required: No
+ **CreateSecurityGroup**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether you want to create new security groups for the deployment.

  Required: Yes
+ **NewSecurityGroupRules**

  Type: String

  Example: `"[{\"type\":\"ip\",\"value\":\"10.0.0.0/32\"},{\"type\":\"securityGroupId\",\"value\":\"sg-0e1c107d640209244\"}]"`

  Description: A list of CIDR blocks or Security Group IDs to be used for creating a new security group.

  Conditional: If you specify `Yes` for `CreateSecurityGroup`, you must also provide input for this configuration.

  Required: No
+ **NewDatabaseSecurityGroupName**

  Type: String

  Example: dbsgname

  Description: The name of the database tier security group.

  Conditional: If you specify `Yes` for `CreateSecurityGroup`, you must also provide input for this configuration.

  Required: No
+ **NewApplicationSecurityGroupName**

  Type: String

  Example: dbsgname

  Description: The name of the application tier security group.

  Conditional: If you specify `Yes` for `CreateSecurityGroup`, you must also provide input for this configuration.

  Required: No
+ **DatabaseSecurityGroupId**

  Type: String

  Example: sg-1234567890abcdef

  Description: The security group ID for your HANA database.

  Conditional: If you specify `No` for `CreateSecurityGroup`, you must provide an input for this configuration.

  Required: No
+ **ApplicationSecurityGroupId**

  Type: String

  Example: sg-1234567890ghijkl

  Description: The security group ID for your SAP application.

  Conditional: If you specify `No` for `CreateSecurityGroup`, you must provide an input for this configuration.

  Required: No
+ **DomainName**

  Type: String

  Example: example.com

  Description: The domain name to be used for the deployment.

  Required: No
+ **HostedZoneName**

  Type: String

  Example: example.com

  Description: The Amazon Route 53 hosted zone name.

  Required: No
+ **HostedZoneId**

  Type: String

  Example: Z36KTIQEXAMPLE

  Description: Route 53 hosted zone id.

  Conditional: If you specify a value for `HostedZoneName`, you must also provide input for this specification.

  Required: No
+ **DedicatedHostId**

  Type: CommaDelimitedList String

  Example: h-012a3456b7890cdef

  Description: The existing Dedicated Hosts on which you want to launch your instances.

  Conditional: If you are using Amazon EC2 High Memory Instances, you must provide an input for this specification. For more information on Amazon EC2 High Memory Instances, see [Amazon EC2 High Memory Instances](https://aws.amazon.com/ec2/instance-types/high-memory/).

  Required: No
+ **ConfigurationScripts**

  Type: String

  Example: `{"preConfigurationScripts":{"onFailureBehaviour":"{{CONTINUE}}","configurationScripts":[{"nodeTypesToRunScriptFor":["{{DB}}"],"s3URL":"{{s3://launchwizard-scripts-preconfig-us-west-2/preconfig-install.sh}}","sequence":"{{0}}"}]},"postConfigurationScripts":{"onFailureBehaviour":"{{CONTINUE}}","configurationScripts":[{"nodeTypesToRunScriptFor":["{{DB}}"],"s3URL":"{{s3://launchwizard-scripts-postconfig-us-west-2/postconfig-install.sh}}","sequence":"{{0}}"}]}}`

  Description: A list of pre- and post-configuration deployment scripts formatted as stringified JSON. You can specify one or more pre- or post-configuration scripts separately, or together. You must provide the follow details for each script:
  + The URL for the script that has been uploaded to Amazon S3.
  + A sequence number which specifies the order of execution.
  + The type of node to run the script on. You can specify `DB`, and `PAS`.
  + The behavior to use should a failure or timeout occur when running the script. You can specify `CONTINUE` to proceed with the deployment or `ROLLBACK` to cancel the deployment.

  Required: No
+ **SidAdmUserId**

  Type: String

  Example: 1002

  Description: The UID for the `<sid>adm` user. The default UID is `1002`.

  Required: Yes
+ **SapSysGroupId**

  Type: String

  Example: 1001

  Description: GID for the `sapsys` group. The default GID is `1001`.

  Required: Yes
+ **DatabaseSystemId**

  Type: String

  Constraints: This value must consist of 3 characters.

  Example: HDB

  Description: The SAP HANA system ID for installation and setup.

  Required: Yes
+ **SapSid**

  Type: String

  Constraints: This value must consist of 3 characters.

  Example: HDB

  Description: The SAP application system ID for installation and setup.

  Required: Yes
+ **ApplicationDataVolumeType**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2`

  Description: The Amazon EBS volume type for the SAP application.

  Required: Yes
+ **DatabaseInstanceNumber**

  Type: String

  Constraints: The instance number must be between `00` and `97`.

  Example: 00

  Description: The SAP HANA instance number to use for installation, setup, and to open ports for security groups.

  Required: Yes
+ **InstallAwsBackintAgent**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install the AWS Backint Agent for SAP HANA.

  Conditional: This specification can only used in this deployment pattern if `InstallSap` is specified as `Yes`, or `InstallSap` is specified as `No` and `InstallDatabaseSoftware` is set to `Yes`.

  Required: Yes
+ **BackintSpecifications**

  Type: String

  Example:

  ```
  "{\"backintBucketName\":\"{{amzn-s3-demo-bucket}}\",\"backintBucketFolder\":\"{{HANABackintBucketFolder}}\",\"backintBucketRegion\":\"{{us-east-1}}\",\"backintKmsKeyArn\":\"{{arn:aws:kms:us-east-1:111122223333:alias/aws/s3}}\",\"backintAgentVersion\":\"{{2.0.2.732}}\",\"backintContinueOnFailure\":\"{{No}}\",\"backintCreateEbsVolume\":\"{{No}}\"}"
  ```

  Description: Parameters for the AWS Backint Agent for SAP HANA formatted as stringified JSON.

  Conditional: If you specify `Yes` for `InstallAwsBackintAgent`, you must also provide input for this specification.

  Required: No
+ **PasOperatingSystem**

  Type: String

  Example: SuSE-Linux-12-SP5-For-SAP-HVM

  Description: The operating system (including the version) for the PAS node.

  Required: Yes
+ **PasAmiId**

  Type: String

  Example: ami-33333333333333

  Description: The AMI ID to use for the PAS node. The AMI can be provided by Amazon, sourced from AWS Marketplace, or with Bring your own images (BYOI). If the AMI from AWS Marketplace is using the Bring Your Own Subscription model (BYOS), you must provide the registation code for SUSE distributions or an account and password for RHEL distributions.

  Required: Yes
+ **PasByoip**

  Type: String

  Example: 10.0.1.10

  Description: A private IPv4 address to be used by the PAS node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **PasSlesByosRegistrationCode**

  Type: String

  Description: The SLES registration code for Bring Your Own Subscription model (BYOS) images.

  Conditional: If you specify SUSE as the operating system, and it uses BYOS, you must also provide input for this specification.

  Required: No
+ **PasRhelByosUsername**

  Type: String

  Example: admin

  Description: The username in the Red Hat Enterprise Linux (RHEL) operating system to use.

  Conditional: If you specify a BYOS RHEL AMI, you must also provide input for this specification.

  Required: No
+ **PasRhelByosUserPassword**

  Type: String

  Description: The password for the user specified in `PasRhelByosUsername`.

  Conditional: If you specify a BYOS RHEL AMI, you must also provide input for this specification.

  Required: No
+ **PasAutomaticRecovery**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specify `Yes` to enable Amazon CloudWatch action based recovery for the PAS node or `No` to keep it disabled. For HA deployments, set this value to `No` as the cluster will manage availability for the nodes.

  Required: Yes
+ **PasInstanceType**

  Type: String

  Example: r5.2xlarge

  Description: The instance type used for the PAS node.

  Required: Yes
+ **PasHostname**

  Type: String

  Example: PASPrimary

  Description: The host name or DNS short name to use for the PAS node.

  Required: Yes
+ **InstallAas**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install AAS instances.

  Required: Yes
+ **AasHostCount**

  Type: Number

  Min: 0

  Max: 10

  Description: The number of AAS instances to deploy.

  Conditional: If you specify `true` for `InstallAas`, you must provide a value for this specification.

  Required: Yes
+ **AasByoip**

  Type: String

  Example: 10.0.1.10

  Description: A private IPv4 address to be used by the AAS node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Conditional: You must specify `true` for `InstallAas` to provide a value for this specification.

  Required: No
+ **AasAutomaticRecovery**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specify `Yes` to enable Amazon CloudWatch action based recovery for the PAS node or `No` to keep it disabled. For HA deployments, set this value to `No` as the cluster will manage availability for the nodes.

  Conditional: If you specify `true` for `InstallAas`, you must provide a value for this specification.

  Required: Yes
+ **AasInstanceType**

  Type: String

  Example: r5.2xlarge

  Description: The instance type used for the AAS node.

  Conditional: If you specify `true` for `InstallAas`, you must provide a value for this specification.

  Required: Yes
+ **AasHostnames**

  Type: String

  Example: AASPrimary

  Description: The host name or DNS short name to use for the AAS node.

  Conditional: If you specify `true` for `InstallAas`, you must provide a value for this specification.

  Required: Yes
+ **DatabaseOperatingSystem**

  Type: String

  Example: SuSE-Linux-12-SP5-For-SAP-HVM

  Description: The operating system (including the version) for SAP HANA.

  AllowedValues: `SuSE-Linux-12-SP4-HVM | SuSE-Linux-12-SP4-For-SAP-HVM | SuSE-Linux-12-SP5-HVM | SuSE-Linux-12-SP5-For-SAP-HVM | SuSE-Linux-15-HVM | SuSE-Linux-15-For-SAP-HVM | SuSE-Linux-15-SP1-HVM | SuSE-Linux-15-SP1-For-SAP-HVM | SuSE-Linux-15-SP2-HVM | SuSE-Linux-15-SP2-For-SAP-HVM | SuSE-Linux-15-SP3-HVM | SuSE-Linux-15-SP3-For-SAP-HVM | SuSE-Linux-15-SP4-HVM | SuSE-Linux-15-SP5-HVM | SuSE-Linux-15-SP6-HVM | SuSE-Linux-15-SP4-For-SAP-HVM | SuSE-Linux-15-SP5-For-SAP-HVM| SuSE-Linux-15-SP6-For-SAP-HVM | Red-Hat-Enterprise-Linux-7.6-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-7.7-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-7.9-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.1-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.2-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.4-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.6-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.8-For-SAP-HA-US-HVM| Red-Hat-Enterprise-Linux-8.10-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-9.0-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-9.2-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-9.4-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-7.6-BYOS | Red-Hat-Enterprise-Linux-7.7-BYOS | Red-Hat-Enterprise-Linux-8.1-BYOS | Red-Hat-Enterprise-Linux-8.2-BYOS | Red-Hat-Enterprise-Linux-8.4-BYOS | Red-Hat-Enterprise-Linux-8.6-BYOS | Red-Hat-Enterprise-Linux-8.8-BYOS| Red-Hat-Enterprise-Linux-8.10-BYOS | Red-Hat-Enterprise-Linux-9.0-BYOS | Red-Hat-Enterprise-Linux-9.2-BYOS | Red-Hat-Enterprise-Linux-9.4-BYOS | SuSE-Linux-12-SP4-For-SAP-BYOS-HVM | SuSE-Linux-12-SP5-For-SAP-BYOS-HVM | SuSE-Linux-15-For-SAP-BYOS-HVM | SuSE-Linux-15-SP1-For-SAP-BYOS-HVM | SuSE-Linux-15-SP2-For-SAP-BYOS-HVM | SuSE-Linux-15-SP3-For-SAP-BYOS-HVM | SuSE-Linux-15-SP4-For-SAP-BYOS-HVM | SuSE-Linux-15-SP5-For-SAP-BYOS-HVM | SuSE-Linux-15-SP6-For-SAP-BYOS-HVM ` 

  Required: Yes
+ **DatabaseAmiId**

  Type: String

  Example: ami-11111111111111

  Description: The AMI ID to use for the SAP HANA nodes. The AMI can be provided by Amazon, sourced from AWS Marketplace, or with Bring your own images (BYOI). If the AMI from AWS Marketplace is using the Bring Your Own Subscription model (BYOS), you must provide the registation code for SUSE distributions or an account and password for RHEL distributions.

  Required: Yes
+ **DatabasePrimaryByoip**

  Type: String

  Example: 10.0.1.10

  Description: A private IPv4 address to be used by the primary SAP HANA node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **DatabaseStandbyByoips**

  Type: String

  Example: 10.0.1.11

  Description: A private IPv4 address to be used by the standby SAP HANA node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **DatabaseAutomaticRecovery**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specify `Yes` to enable Amazon CloudWatch action based recovery for SAP Hana nodes or `No` to keep it disabled. For HA deployments, set this value to `No` as the cluster will manage availability for the nodes.

  Required: Yes
+ **DatabaseInstanceType**

  Type: String

  Example: r5.2xlarge

  Description: The instance type used for SAP HANA nodes.

  Required: Yes
+ **DatabasePrimaryHostname**

  Type: String

  Example: HanaPrimary

  Description: The host name or DNS short name to use for the primary SAP HANA node.

  Required: Yes
+ **DatabaseSubordinateHostnames**

  Type: String

  Example: SubordinateName1,SubordinateName2

  Description: A comma-separated list of the host names or DNS short names to use for the subordinate nodes.

  Required: No
+ **DatabaseSlesByosRegistrationCode**

  Type: String

  Description: The SLES registration code for Bring Your Own Subscription model (BYOS) images.

  Conditional: If you specify SUSE as the operating system, and it uses BYOS, you must also provide input for this specification.

  Required: No
+ **DatabaseRhelByosUserName**

  Type: String

  Example: admin

  Description: The username in the Red Hat Enterprise Linux (RHEL) operating system to use.

  Conditional: If you specify a BYOS RHEL AMI, you must also provide input for this specification.

  Required: No
+ **DatabaseRhelByosUserPassword**

  Type: String

  Description: The password for the user specified in `DatabaseRhelByosUserName`.

  Conditional: If you specify a BYOS RHEL AMI, you must also provide input for this specification.

  Required: No
+ **SapPassword**

  Type: String

  Description: Specifes the password to use for setting up the SAP application and database defaults users. The password must:
  + Be between 10 and 13 alphanumeric characters.
  + Not begin with a number or special character.
  + Have at least one uppercase letter.
  + Have at least one lowercase letter.
  + Have at least one digit.
  + Only use the following special characters: **\#**, **@**, and **\_**.

  Required: Yes
+ **DatabaseLogVolumeType**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2` \| `fsx`

  Description: The Amazon EBS volume type, or FSx for ONTAP (if supported) file share, for database logging.

  Conditional: If `fsx` is specified for `DatabaseLogVolumeType`, you must also specify `fsx` for `DatabaseDataVolumeType`.

  Required: Yes
+ **DatabaseOthersVolumeType**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2`

  Default: `gp3`

  Description: The Amazon EBS volume type for other file systems, including the root volume.

  Conditional: If `fsx` is specified for `DatabaseDataVolumeType` and `DatabaseLogVolumeType`, you must provide input for this specification.

  Required: No
+ **InstallDatabaseSoftware**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install SAP HANA software.

  Required: Yes
+ **DatabaseInstallationMediaS3Uri**

  Type: String

  Example: s3://myhanabucket/sap-hana-sps11/

  Description: The full path to the Amazon S3 location with SAP HANA installation media.

  Required: No
+ **DatabaseHostAutoFailover**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specified whether the SAP HANA host should use automatic failover.

  Conditional: If you specify `fsx` for your volume types, you must also provide input for this specification.

  Required: Yes
+ **DatabaseStandbyNodeCount**

  Type: Number

  Min: 0

  Max: 17

  Description: The number of SAP HANA standby hosts to deploy.

  Conditional: If you specify `fsx` for your volume types and `DatabaseHostAutoFailover` is set to `Yes`, you must also provide input for this specification.

  Required: Yes
+ **DatabaseStandbyHostnames**

  Type: String

  Example: `standby1`, `standby2`, `standby3`

  Description: The host names, or DNS short names, to use for the SAP HANA standby nodes. You can specify multiple values as a comma-separated list.

  Conditional: If you specify `fsx` for your volume types, you must also provide input for this specification.

  Required: No
+ **DatabaseStandbyByoips**

  Type: String

  Example: 10.0.1.11

  Description: A private IPv4 address to be used by the standby SAP HANA node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **DatabaseHostCount**

  Type: Number

  Min: 1

  Max: 17

  Description: The number of hosts to deploy. When you specify `1` for `Min`, only the master HANA database is deployed in a scale-up architecture. When you specify `2` or higher for `Min`, subordinate nodes are deployed with the master HANA database in a scale-out architecture.

  Required: Yes
+ **DatabaseDataFsxVolumeSize**

  Type: Number

  Example: 500

  Description: The volume size of the SAP HANA data volume on Amazon FSx, in GBs.

  Conditional: If you specify `fsx` for `DatabaseDataVolumeType`, you must also provide input for this specification.

  Required: No
+ **DatabaseLogFsxVolumeSize**

  Type: Number

  Example: 50

  Description: The volume size of the SAP HANA log volume on Amazon FSx, in GBs.

  Conditional: If you specify `fsx` for `DatabaseLogVolumeType`, you must also provide input for this specification.

  Required: No
+ **DatabaseOtherFsxVolumeSize**

  Type: Number

  Example: 50

  Description: The volume size of the other SAP HANA volume on Amazon FSx, in GBs.

  Conditional: If you specify `fsx` for `DatabaseOthersVolumeType`, you must also provide input for this specification.

  Required: No
+ **SetupTransportDomainController**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to use transport FS.

  Required: Yes
+ **CreateTransportDomainControllerFileSystem**

  Type: String

  AllowedValues: `Yes` \| `No`

  Default: `No`

  Description: Specifies whether to create a new Amazon EFS for the transport domain controller.

  Conditional: You must specify `Yes` for `SetupTransportDomainController` to provide value for this specification.

  Required: No
+ **TransportDomainControllerFileSystemId**

  Type: String

  Example: `fs-1234567890abcdef0`

  Description: The ID of an existing Elastic File System for the transport domain controller.

  Conditional: If you specify `No` for `CreateTransportDomainControllerFileSystem`, you must also provide input for this specification.

  Required: Yes
+ **InstallSap**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install SAP. The following specification combinations can be used to customize your application:
  + To install SAP application software, specify `No` for `InstallDatabaseSoftware` and `Yes` for `InstallSap`.
  + To install only the database software and deploy infrastructure resources for the application and database components, specify `Yes` for `InstallDatabaseSoftware` and `No` for `InstallSap`.
  + To only deploy infrastructure resources for the SAP application and database components, specify `No` for `InstallDatabaseSoftware` and `InstallSap`.

  Required: Yes
+ **SapInstallationSpecifications**

  Type: String

  Example without SAP Web Dispatcher: `{"parameters":{"PRODUCT_ID":"saps4hana-2022","HDB_SCHEMA_NAME":"SAPABAP1","CI_INSTANCE_NR":"12","ASCS_INSTANCE_NR":"10","SAPINST_CD_SAPCAR":"{{s3://launchwizard-test-sap-media/sapcar}}","SAPINST_CD_SWPM":"{{s3://launchwizard-test-sap-media/swpm/10-sp30}}","SAPINST_CD_KERNEL":"{{s3://launchwizard-test-sap-media/kernel}}","SAPINST_CD_LOAD":"{{s3://launchwizard-test-sap-media/exports/nw-75}}","SAPINST_CD_RDBMS":"{{s3://launchwizard-test-sap-media/database}}","SAPINST_CD_RDBMS_CLIENT":"{{s3://launchwizard-test-sap-media/hana-client}}"}, "onFailureBehaviour": "CONTINUE/ROLLBACK"}`

  Example with SAP Web Dispatcher: {"parameters":{"PRODUCT\_ID":"sapNetweaver-752","CI\_INSTANCE\_NR":"12","ASCS\_INSTANCE\_NR":"10","WD\_INSTANCE\_NR":"14","ASCS\_VIRTUAL\_HOSTNAME":"sapvirascs","ASCS\_OVERLAY\_IP":"10.0.0.8","ERS\_VIRTUAL\_HOSTNAME":"sapvirers","ERS\_OVERLAY\_IP":"10.0.0.9","DB\_VIRTUAL\_HOSTNAME":"sapvirdb","SAP\_PACEMAKER\_TAG":"sappacetag","SAPINST\_CD\_SAPCAR":"s3://launchwizard-example/sapcar/","SAPINST\_CD\_SWPM":"s3://launchwizard-example/swpm/10-sp39/","SAPINST\_CD\_KERNEL":"s3://launchwizard-example/kernel/","SAPINST\_CD\_LOAD":"s3://launchwizard-example/exports/nw-752/","SAPINST\_CD\_RDBMS":"s3://launchwizard-example/database/hana-20-sp07/","SAPINST\_CD\_RDBMS\_CLIENT":"s3://launchwizard-example/hana-client/20-11/","SAPINST\_CD\_WD":"s3://launchwizard-example-us-east-1/webdisp/"}

  Description: A list of SAP Application installation parameters formatted as stringified JSON. You can specify any of the following values for the `PRODUCT_ID`: `sapNetWeaver-752 | sapNetWeaver-750 | sapNetweaverJavaOnly-750 | saps4hana-1909 | saps4hana-2020 | saps4hana-2021 | saps4hana-2022 | saps4hana-2023 | saps4hanafoundations-2021 | saps4hanafoundations-2022 | saps4hanafoundations-2023 | sapbw4hana-2.0 | sapbw4hana-2021 | sapsolman-7.2`

  Conditional: If you specify `Yes` for `InstallSap`, you must also provide input for this specification.

  Required: No
+ **SnsTopicArn**

  Type: String

  Example: arn:aws:sns:us-east-1:1234567890:Test-Topic

  Description: The Amazon SNS topic used to receive the final deployment status from Launch Wizard.

  Required: No
+ **DisableDeploymentRollback**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to disable rollback of the CloudFormation stack if the stack creation fails.

  Required: Yes
+ **SaveDeploymentArtifacts**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to save the deployment artifacts in Service Catalog after deployment is complete.

  Required: Yes
+ **DeploymentArtifactsS3Uri**

  Type: String

  Example: s3://save-test-us-east-1

  Description: The Amazon S3 URI in which to save the deployment artifacts for Service Catalog.

  Required: No
+ **InstallSapWebDispatcher**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install SAP Web Dispatcher.

  Required: No
+ **InstallWebDispatcherLoadBalancer**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to deploy a load balancer in front of SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` and `InstallSap` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerType**

  Type: String

  AllowedValues: ALB \| NLB

  Description: Specifies the kind of load balancer to deploy in front of SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, and`InstallWebDispatcherLoadBalancer` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerInternetFacing**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether the load balancer in front of SAP Web Dispatcher is internet-facing.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, and`InstallWebDispatcherLoadBalancer` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherInstanceNumber**

  Type: Number

  Min: 00

  Max: 97

  Description: The double-digit instance number for the SAP Web Dispatcher instance.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` and `InstallSap` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherAdminUserId**

  Type: Number

  Min: 100

  Max: 65536

  Description: The user ID number for the SAP Web Dispatcher administrator.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherSystemId**

  Type: String

  Description: This value must consist of 3 uppercase characters.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherVersion**

  Type: String

  AllowedValues: `7.89`

  Description: The SAP Web Dispatcher version to use. For more information, see [ Supported versions of SAP Web Dispatcher](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-versions.html).

  Conditional: This specification can only be used if `InstallSapWebDispatcher` and `InstallSap` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherOperatingSystem**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: The operating system to use for SAP Web Dispatcher nodes. For more information, see [Operating systems](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-versions.html#launch-wizard-sap-ascs-support-os).

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherAmiId**

  Type: String

  Example: ami-44444444444444

  Description: The AMI ID to use for SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherInstanceType**

  Type: String

  Example: r5.2xlarge

  Description: The instance type to use for SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherAutoRecovery**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: .

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as Yes. Specify `Yes` to enable Amazon CloudWatch action based recovery for the SAP Web Dispatcher nodes or `No` to keep it disabled.

  Required: Yes
+ **WebDispatcherAvailabilityZone1PrivateSubnetId**

  Type: String

  Example: subnet-11111111aaaaaaaaa

  Description: The existing private subnet where you want to deploy SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallWebDispatcherLoadBalancer` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherServerHostname**

  Type: String

  Example: sapwdprimary

  Description: The host name or DNS short name to use for the SAP Web Dispatcher node.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerSecureProtocolEnabled**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies the ACM certificate to use for your load balancer’s TLS/HTTPS listener.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, and`InstallWebDispatcherLoadBalancer` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerACMCertificateArn**

  Type: String

  Example: 

  Description: The ARN of the ACM certificate to use for your load balancer’s TLS/HTTPS listener.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, `InstallWebDispatcherLoadBalancer`, and WebDispatcherLoadBalancerSecureProtocolEnabled are specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerAvailabilityZone1SubnetId**

  Type: String

  Example: subnet-11111111aaaaaaaaa

  Description: The existing private subnet where you want to deploy SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, and`InstallWebDispatcherLoadBalancer` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerAvailabilityZone2SubnetId**

  Type: String

  Example: subnet-22222222aaaaaaaaa

  Description: The additional existing private subnet where you want to deploy SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, and`InstallWebDispatcherLoadBalancer` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherSecurityGroupId**

  Type: String

  Example: 

   sg-1234567890abcdef

  Description: The security group to assign to your SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherLoadBalancerSecurityGroupId**

  Type: String

  Example: sg-1234567890abcdef

  Description: The security group to assign to the load balancer for SAP Web Dispatcher nodes.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, and`InstallWebDispatcherLoadBalancer` are specified as `Yes`.

  Required: Yes
+ **NewWebDispatcherSecurityGroupName**

  Type: String

  Example: 

  Description: The name of the security group to create for SAP Web Dispatcher.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, `InstallWebDispatcherLoadBalancer`, and`CreateSecurityGroup` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherRhelByosUserName**

  Type: String

  Description: The username for the RHEL BYOS AMI.

  Conditional:

   This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherRhelByosUserPassword**

  Type: String

  Description: The password for the RHEL BYOS AMI.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WebDispatcherSlesByosRegistrationCode**

  Type: String

  Description: The registration code for the SUSE BYOS AMI.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WdByoip**

  Type: String

  Example: 10.0.0.1

  Description: The BYOIP address to use.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` is specified as `Yes`.

  Required: Yes
+ **WdVirtualByoip**

  Type: String

  Example: 10.0.0.2

  Description: The virtual BYOIP address to use.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` and `SapVirtualIpOptIn` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherServerVirtualHostname**

  Type: String

  Example: 

  Description: The virtual hostname to use when you use a virtual BYOIP address.

  Conditional: This specification can only be used if `InstallSapWebDispatcher` and `SapVirtualIpOptIn` are specified as `Yes`.

  Required: Yes
+ **WebDispatcherNewLoadBalancerSecurityGroupName**

  Type: String

  Example: 

  Description: The name of the security group to create for the load balancer for SAP Web Dispatcher.

  Conditional: This specification can only be used if `InstallSapWebDispatcher`, `InstallSap`, `InstallWebDispatcherLoadBalancer`, and`CreateSecurityGroup` are specified as `Yes`.

  Required: Yes