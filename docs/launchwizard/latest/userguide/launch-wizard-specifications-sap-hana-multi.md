

# SapHanaMulti
<a name="launch-wizard-specifications-sap-hana-multi"></a>

The following is an example of the specifications required to create a SAP HANA deployment with multiple nodes and HANA database software installed:

```
{
  "KeyPairName": "ExampleKeyPair",
  "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
  "VpcId": "vpc-a1b2c3d4",
  "Timezone" :"PST",
  "EnableEbsVolumeEncryption" :"Yes",
  "EbsKmsKeyArn": "arn:aws:kms:us-east-1:111122223333:alias/aws/ebs",
  "DatabaseSecurityGroupId" :"sg-1234567890abcdef0",
  "ApplicationSecurityGroupId" :"sg-1234567890abcdef0",
  "CreateSecurityGroup": "No",
  "SapSysGroupId" :"5002",
  "DatabaseSystemId" :"HYD",
  "DatabaseInstanceNumber": "00",
  "DatabasePassword" :"EXAMPLE-PASSWORD",
  "InstallDatabaseSoftware" :"Yes",
  "DatabaseInstallationMediaS3Uri" :"s3://launchwizardsoftware/sapmedia/database/hana-20-sp06-rev60",
  "DatabaseOperatingSystem": "SuSE-Linux-15-SP2-For-SAP-HVM",
  "DatabaseAmiId" :"ami-1234567890abcdef0",
  "DatabasePrimaryHostname" :"hanasingle",
  "DatabaseSubordinateHostnames" :"hanasub1,hanasub2",
  "DatabaseHostCount" :"3",
  "DatabaseInstanceType" :"r5.4xlarge",
  "InstallAwsBackintAgent" :"Yes",
  "BackintSpecifications": "{\"backintBucketName\":\"launchwizardsoftware\",\"backintBucketFolder\":\"HANABackintBucketFolder\",\"backintBucketRegion\":\"us-east-1\",\"backintKmsKeyArn\":\"arn:aws:kms:us-east-1:111122223333:alias/aws/s3\",\"backintAgentVersion\":\"2.0.2.732\",\"backintContinueOnFailure\":\"No\",\"backintCreateEbsVolume\":\"No\"}",
  "DisableDeploymentRollback" :"Yes",
  "SnsTopicArn" :"arn:aws:sns:us-east-1:111122223333:InstallStatus",
  "SaveDeploymentArtifacts" :"Yes",
  "DeploymentArtifactsS3Uri" :"s3://launchwizardsoftware",  
  "DatabaseAutomaticRecovery": "Yes",    
  "DatabaseLogVolumeType": "gp3"
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

  Example: `{"preConfigurationScripts":{"onFailureBehaviour":"{{CONTINUE}}","configurationScripts":[{"nodeTypesToRunScriptFor":["DB"],"s3URL":"{{s3://launchwizard-scripts-preconfig-us-west-2/preconfig-install.sh}}","sequence":"{{0}}"}]},"postConfigurationScripts":{"onFailureBehaviour":"{{CONTINUE}}","configurationScripts":[{"nodeTypesToRunScriptFor":["DB"],"s3URL":"{{s3://launchwizard-scripts-postconfig-us-west-2/postconfig-install.sh}}","sequence":"{{0}}"}]}}`

  Description: A list of pre- and post-configuration deployment scripts formatted as stringified JSON. You can specify one or more pre- or post-configuration scripts separately, or together. You must provide the follow details for each script:
  + The URL for the script that has been uploaded to Amazon S3.
  + A sequence number which specifies the order of execution.
  + The type of node to run the script on. You can only specify `DB` for this deployment.
  + The behavior to use should a failure or timeout occur when running the script. You can specify `CONTINUE` to proceed with the deployment or `ROLLBACK` to cancel the deployment.

  Required: No
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
+ **DatabaseInstanceNumber**

  Type: String

  Constraints: The instance number must be between `00` and `97`.

  Example: 00

  Description: The SAP HANA instance number to use for installation, setup, and to open ports for security groups.

  Required: Yes
+ **DatabasePassword**

  Type: String

  Description: The password must:
  + Be between 10 and 13 alphanumeric characters.
  + Not begin with a number or special character.
  + Have at least one uppercase letter.
  + Have at least one lowercase letter.
  + Have at least one digit.
  + Only use the following special characters: **\#**, **@**, and **\_**.

  Conditional: This specification is only required if `Yes` was specified for `InstallDatabaseSoftware`.

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
+ **DatabasePrimaryHostname**

  Type: String

  Example: HanaPrimary

  Description: The host name or DNS short name to use for the primary SAP HANA node.

  Required: Yes
+ **DatabaseSubordinateHostnames**

  Type: String

  Example: SubordinateName1,SubordinateName2

  Description: A comma-separated list of the host names or DNS short names to use for the subordinate nodes.

  Required: Yes
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
+ **InstallAwsBackintAgent**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install the AWS Backint Agent for SAP HANA.

  Conditional: This specification can only used in this deployment pattern if `InstallDatabaseSoftware` is specified as `Yes`.

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
+ **DatabasePrimaryByoip**

  Type: String

  Example: 10.0.1.10

  Description: A private IPv4 address to be used by the primary SAP HANA node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **DatabaseSubordinateByoips**

  Type: String

  Example: 10.0.1.11

  Description: A private IPv4 address to be used by the secondary SAP HANA node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **DatabaseHostCount**

  Type: Number

  Min: 2

  Max: 17

  Description: The number of hosts to deploy.

  Required: Yes
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