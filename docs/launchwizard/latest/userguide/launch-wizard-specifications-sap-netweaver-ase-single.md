

# SapNWOnAseSingle
<a name="launch-wizard-specifications-sap-netweaver-ase-single"></a>

The following is an example of the specifications required to create a single-node deployment with SAP software installed:

```
{
    "applicationName": "ExampleApp",
    "DisableDeploymentRollback": "Yes",
    "SaveDeploymentArtifacts": "Yes",
    "DeploymentArtifactsS3Uri": "s3://launchwizardsoftware",
    "KeyPairName": "ExampleKeyPair",
    "VpcId": "vpc-01abcde1234567891",
    "Timezone": "UTC",
    "EnableEbsVolumeEncryption": "Yes",
    "EbsKmsKeyArn": "arn:aws:kms:us-east-1:111122223333:alias/aws/ebs",
    "DatabaseDataVolumeType": "io1",
    "DatabaseLogVolumeType": "io1",
    "DatabaseBackupVolumeType": "gp2",
    "SapSid": "ECD",
    "SybSidUserId": "1003",
    "SidAdmUserId": "5000",
    "SapPassword": "EXAMPLE-PASSWORD",
    "ApplicationDataVolumeType": "gp3",
    "SetupTransportDomainController": "Yes",
    "CreateTransportDomainControllerFileSystem": "Yes",
    "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
    "CentralSystemOperatingSystem": "SuSE-Linux-15-SP5-For-SAP-HVM",
    "CentralSystemAmiId": "ami-1234567890abcdef0",
    "CentralSystemInstanceType": "m6a.xlarge",
    "EnableCloudwatchLogs": "Yes",
    "Ec2InstanceRoleName": "AmazonEC2RoleForLaunchWizard",
    "CentralSystemHostname": "sapci",
    "CentralSystemVirtualHostname": "sapvirtualci",
    "CentralSystemAutomaticRecovery": "Yes",
    "AseBackupFilesSpecifications": "[{\"fileSize\":300,\"IOPS\":900,\"throughPut\":250}]",
    "AseAbapDataFilesSpecifications": "[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]",
    "AseAbapLogFilesSpecifications": "[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]",
    "SapInstallationSpecifications": "{\"parameters\":{\"PRODUCT_ID\":\"sapNetweaver-752\",\"CI_INSTANCE_NR\":\"12\",\"ASCS_INSTANCE_NR\":\"10\",\"SAPINST_CD_RDBMS\":\"s3://launchwizardsoftware/database/ase/\",\"SAPINST_CD_SWPM\":\"s3://launchwizardsoftware/swpm/10-sp38/\",\"SAPINST_CD_SAPCAR\":\"s3://launchwizardsoftware/sapcar/SAPCAR_1320-80000935.EXE\",\"SAPINST_CD_KERNEL\":\"s3://launchwizardsoftware/kernel/753/ase/\",\"SAPINST_CD_LOAD\":\"s3://launchwizardsoftware/exports/nw-752/\"}}",
    "CreateSecurityGroup": "Yes",
    "NewDatabaseSecurityGroupName": "example1212_DB_Sec_grp",
    "NewApplicationSecurityGroupName": "example1212_App_Sec_grp",
    "NewSecurityGroupRules": "[{\"type\":\"ip\",\"value\":\"203.0.113.5/32\"}]",
    "SapSysGroupId": "1001",
    "SapVirtualIPOptIn": "Yes",
    "ConfigurationScripts": "{\"preConfigurationScripts\":{\"onFailureBehaviour\":\"CONTINUE\",\"configurationScripts\":[]},\"postConfigurationScripts\":{\"onFailureBehaviour\":\"CONTINUE\",\"configurationScripts\":[]}}",
    "InstallSap": "Yes"
}
```

The following is an example of the specifications required to create a single-node deployment with only infrastructure resources:

```
{
    "applicationName": "ExampleApp2",
    "DisableDeploymentRollback": "Yes",
    "SaveDeploymentArtifacts": "No",
    "KeyPairName": "ExampleKeyPair",
    "VpcId": "vpc-01abcde1234567891",
    "Timezone": "UTC",
    "EnableEbsVolumeEncryption": "Yes",
    "EbsKmsKeyArn": "arn:aws:kms:us-east-1:111122223333:alias/aws/ebs",
    "DatabaseDataVolumeType": "io2",
    "DatabaseLogVolumeType": "io2",
    "DatabaseBackupVolumeType": "io2",
    "SapSid": "ECD",
    "SybSidUserId": "1003",
    "SidAdmUserId": "5000",
    "ApplicationDataVolumeType": "gp3",
    "SetupTransportDomainController": "No",
    "AvailabilityZone1PrivateSubnet1Id": "subnet-11111111aaaaaaaaa",
    "CentralSystemOperatingSystem": "Red-Hat-Enterprise-Linux-9.0-For-SAP-HA-US-HVM",
    "CentralSystemAmiId": "ami-1234567890abcdef0",
    "CentralSystemInstanceType": "m5.4xlarge",
    "EnableCloudwatchLogs": "Yes",
    "Ec2InstanceRoleName": "AmazonEC2RoleForLaunchWizard",
    "CentralSystemHostname": "sapci",
    "CentralSystemVirtualHostname": "sapvirtualci",
    "CentralSystemAutomaticRecovery": "Yes",
    "AseBackupFilesSpecifications": "[{\"fileSize\":300,\"IOPS\":900,\"throughPut\":250}]",
    "AseAbapDataFilesSpecifications": "[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]",
    "AseAbapLogFilesSpecifications": "[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]",
    "SapInstallationSpecifications": "{\"parameters\":{\"PRODUCT_ID\":\"sapNetweaver-752\",\"CI_INSTANCE_NR\":\"12\",\"ASCS_INSTANCE_NR\":\"10\"}}",
    "CreateSecurityGroup": "No",
    "DatabaseSecurityGroupId": "sg-1234567890abcdef0",
    "ApplicationSecurityGroupId": "sg-021345abcdef6789",
    "SapSysGroupId": "2001",
    "SapVirtualIPOptIn": "Yes",
    "ConfigurationScripts": "{\"preConfigurationScripts\":{\"onFailureBehaviour\":\"CONTINUE\",\"configurationScripts\":[]},\"postConfigurationScripts\":{\"onFailureBehaviour\":\"CONTINUE\",\"configurationScripts\":[]}}",
    "InstallSap": "No"
}
```

The following list describes each specification input:
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
+ **DatabaseDataVolumeType**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2` \| `fsx`

  Description: The Amazon EBS volume type, or Amazon FSx for NetApp ONTAP (if supported) file share, for database data.

  Conditional: If `fsx` is specified for `DatabaseDataVolumeType`, you must also specify `fsx` for `DatabaseLogVolumeType`.

  Required: Yes
+ **DatabaseLogVolumeType**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2` \| `fsx`

  Description: The Amazon EBS volume type, or FSx for ONTAP (if supported) file share, for database logging.

  Conditional: If `fsx` is specified for `DatabaseLogVolumeType`, you must also specify `fsx` for `DatabaseDataVolumeType`.

  Required: Yes
+ **DatabaseBackupVolume**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2` \| `fsx`

  Description: The Amazon EBS volume type, or Amazon FSx for NetApp ONTAP (if supported) file share, for database backup.

  Required: Yes
+ **SapSid**

  Type: String

  Constraints: This value must consist of 3 characters.

  Example: HDB

  Description: The SAP application system ID for installation and setup.

  Required: Yes
+ **SybSidUserId**

  Type: String

  Constraints: The minimum is 100, and the maximum is 65536.

  Example: 1000

  Description: The system ID user ID for SAP ASE database.

  Required: Yes
+ **SidAdmUserId**

  Type: String

  Constraints: The minimum is 100, and the maximum is 65536.

  Example: 1002

  Description: The UID for the `<sid>adm` user. The default UID is `1002`.

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
+ **ApplicationDataVolumeType**

  Type: String

  AllowedValues: `gp2` \| `gp3` \| `io1` \| `io2`

  Description: The Amazon EBS volume type for the SAP application.

  Required: Yes
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
+ **AvailabilityZone1PrivateSubnet1Id**

  Type: String

  Example: subnet-11111111aaaaaaaaa

  Description: The existing private subnet where you want to deploy the system.

  Required: Yes
+ **CentralSystemOperatingSystem**

  Type: String

  Example: SuSE-Linux-12-SP5-For-SAP-HVM

  Description: The operating system (including the version) for database.

  AllowedValues: `SuSE-Linux-12-SP4-HVM | SuSE-Linux-12-SP4-For-SAP-HVM | SuSE-Linux-12-SP5-HVM | SuSE-Linux-12-SP5-For-SAP-HVM | SuSE-Linux-15-HVM | SuSE-Linux-15-For-SAP-HVM | SuSE-Linux-15-SP1-HVM | SuSE-Linux-15-SP1-For-SAP-HVM | SuSE-Linux-15-SP2-HVM | SuSE-Linux-15-SP2-For-SAP-HVM | SuSE-Linux-15-SP3-HVM | SuSE-Linux-15-SP3-For-SAP-HVM | SuSE-Linux-15-SP4-HVM | SuSE-Linux-15-SP5-HVM | SuSE-Linux-15-SP6-HVM | SuSE-Linux-15-SP4-For-SAP-HVM | SuSE-Linux-15-SP5-For-SAP-HVM| SuSE-Linux-15-SP6-For-SAP-HVM | Red-Hat-Enterprise-Linux-7.6-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-7.7-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-7.9-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.1-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.2-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.4-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.6-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-8.8-For-SAP-HA-US-HVM| Red-Hat-Enterprise-Linux-8.10-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-9.0-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-9.2-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-9.4-For-SAP-HA-US-HVM | Red-Hat-Enterprise-Linux-7.6-BYOS | Red-Hat-Enterprise-Linux-7.7-BYOS | Red-Hat-Enterprise-Linux-8.1-BYOS | Red-Hat-Enterprise-Linux-8.2-BYOS | Red-Hat-Enterprise-Linux-8.4-BYOS | Red-Hat-Enterprise-Linux-8.6-BYOS | Red-Hat-Enterprise-Linux-8.8-BYOS| Red-Hat-Enterprise-Linux-8.10-BYOS | Red-Hat-Enterprise-Linux-9.0-BYOS | Red-Hat-Enterprise-Linux-9.2-BYOS | Red-Hat-Enterprise-Linux-9.4-BYOS | SuSE-Linux-12-SP4-For-SAP-BYOS-HVM | SuSE-Linux-12-SP5-For-SAP-BYOS-HVM | SuSE-Linux-15-For-SAP-BYOS-HVM | SuSE-Linux-15-SP1-For-SAP-BYOS-HVM | SuSE-Linux-15-SP2-For-SAP-BYOS-HVM | SuSE-Linux-15-SP3-For-SAP-BYOS-HVM | SuSE-Linux-15-SP4-For-SAP-BYOS-HVM | SuSE-Linux-15-SP5-For-SAP-BYOS-HVM | SuSE-Linux-15-SP6-For-SAP-BYOS-HVM ` 

  Required: Yes
+ **CentralSystemAmiId**

  Type: String

  Example: ami-11111111111111

  Description: The AMI ID to use for the database nodes. The AMI can be provided by Amazon, sourced from AWS Marketplace, or with Bring your own images (BYOI). If the AMI from AWS Marketplace is using the Bring Your Own Subscription model (BYOS), you must provide the registation code for SUSE distributions or an account and password for RHEL distributions.

  Required: Yes
+ **CentralSystemInstanceType**

  Type: String

  Example: r5.2xlarge

  Description: The instance type used for database nodes.

  Required: Yes
+ **EnableCloudwatchLogs**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to enable Amazon CloudWatch logs.

  Required: No
+ **EC2InstanceRoleName**

  Type: String

  Example: `AmazonEC2RoleForLaunchWizard`

  Description: The name of the Amazon EC2 instance role.

  Required: Yes
+ **CentralSystemHostname**

  Type: String

  Example: sapci

  Description: The host name or DNS short name to use for the primary database node.

  Required: Yes
+ **CentralSystemVirtualHostname**

  Type: String

  Example: sapvirtualci

  Description: The virtual host name or DNS short name to use for the primary database node.

  Required: Yes
+ **CentralSystemAutomaticRecovery**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specify `Yes` to enable Amazon CloudWatch action based recovery for database nodes or `No` to keep it disabled. For HA deployments, set this value to `No` as the cluster will manage availability for the nodes.

  Required: Yes
+ **AseBackupFileSpecifications**

  Type: String

  Example: `[{\"fileSize\":300,\"IOPS\":900,\"throughPut\":250}]`

  Description: Parameters for the backup filesystem for SAP ASE database formatted as stringified JSON.

  Required: Yes
+ **AseAbapDataFilesSpecifications**

  Type: String

  Example: `[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]`

  Description: Parameters for the data filesystem for SAP ASE database formatted as stringified JSON.

  Required: Yes
+ **AseAbapLogFilesSpecifications**

  Type: String

  Example: `[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]`

  Description: Parameters for the log filesystem for SAP ASE database formatted as stringified JSON.

  Required: Yes
+ **SapInstallationSpecifications**

  Type: String

  Example: `{"parameters":{"PRODUCT_ID":"saps4hana-2022","HDB_SCHEMA_NAME":"SAPABAP1","CI_INSTANCE_NR":"12","ASCS_INSTANCE_NR":"10","SAPINST_CD_SAPCAR":"{{s3://launchwizard-test-sap-media/sapcar}}","SAPINST_CD_SWPM":"{{s3://launchwizard-test-sap-media/swpm/10-sp30}}","SAPINST_CD_KERNEL":"{{s3://launchwizard-test-sap-media/kernel}}","SAPINST_CD_LOAD":"{{s3://launchwizard-test-sap-media/exports/nw-75}}","SAPINST_CD_RDBMS":"{{s3://launchwizard-test-sap-media/database}}","SAPINST_CD_RDBMS_CLIENT":"{{s3://launchwizard-test-sap-media/hana-client}}"}, "onFailureBehaviour": "CONTINUE/ROLLBACK"}`

  Description: A list of SAP Application installation parameters formatted as stringified JSON. You can specify any of the following values for the `PRODUCT_ID`: `sapNetWeaver-752 | sapNetWeaver-750 | sapNetweaverJavaOnly-750 | saps4hana-1909 | saps4hana-2020 | saps4hana-2021 | saps4hana-2022 | saps4hana-2023 | saps4hanafoundations-2021 | saps4hanafoundations-2022 | saps4hanafoundations-2023 | sapbw4hana-2.0 | sapbw4hana-2021 | sapsolman-7.2`

  Conditional: If you specify `Yes` for `InstallSap`, you must also provide input for this specification.

  Required: No
+ **CreateSecurityGroup**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether you want to create new security groups for the deployment.

  Required: Yes
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
+ **NewSecurityGroupRules**

  Type: String

  Example: `"[{\"type\":\"ip\",\"value\":\"10.0.0.0/32\"},{\"type\":\"securityGroupId\",\"value\":\"sg-0e1c107d640209244\"}]"`

  Description: A list of CIDR blocks or Security Group IDs to be used for creating a new security group.

  Conditional: If you specify `Yes` for `CreateSecurityGroup`, you must also provide input for this configuration.

  Required: No
+ **SapSysGroupId**

  Type: String

  Example: 1001

  Description: GID for the `sapsys` group. The default GID is `1001`.

  Required: Yes
+ **SapVirtualIPOptIn**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies if or not a virtual IP address is assigned to the EC2 instance hosting the SAP system.

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
+ **InstallSap**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies whether to install SAP. The following specification combinations can be used to customize your application:
  + To install SAP application software, specify `No` for `InstallDatabaseSoftware` and `Yes` for `InstallSap`.
  + To install only the database software and deploy infrastructure resources for the application and database components, specify `Yes` for `InstallDatabaseSoftware` and `No` for `InstallSap`.
  + To only deploy infrastructure resources for the SAP application and database components, specify `No` for `InstallDatabaseSoftware` and `InstallSap`.

  Required: Yes