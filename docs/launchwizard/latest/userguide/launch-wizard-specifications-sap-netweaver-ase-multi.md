

# SapNWOnAseMulti
<a name="launch-wizard-specifications-sap-netweaver-ase-multi"></a>

The following are examples of the specifications required to create multi-node deployments.

Multi-node deployment with resources for SAP ASE Java stack:

```
{
    "SapInstallationSpecifications": "{ \"onFailureBehaviour\":\"ROLLBACK\",\"parameters\":{\"PRODUCT_ID\":\"sapNetweaverJavaOnly-750\",\"JAVA_CI_INSTANCE_NR\":\"13\",\"JAVA_SCS_INSTANCE_NR\":\"11\",\"SAPINST_CD_SAPCAR\":\"s3:\/\/launchwizardsoftware\/sapmedia\/sapcar\",\"SAPINST_CD_SWPM\":\"s3:\/\/launchwizardsoftware\/sapmedia\/swpm\/20-sp10\",\"SAPINST_CD_KERNEL\":\"s3:\/\/launchwizardsoftware\/sapmedia\/kernel\/785\",\"SAPINST_CD_LOAD\":\"s3:\/\/launchwizardsoftware\/sapmedia\/exports\/s4h-2021\",\"SAPINST_CD_RDBMS\":\"s3:\/\/launchwizardsoftware\/sapmedia\/database\/hana-20-sp06-rev60\" } }",
    "AseJavaDataFilesSpecifications": "[ { \"fileSize\": \"100\", \"throughPut\": \"500\", \"IOPS\": \"3000\" }, { \"fileSize\": \"100\", \"throughPut\": \"500\", \"IOPS\": \"3000\" }, { \"fileSize\": \"100\", \"throughPut\": \"500\", \"IOPS\": \"3000\" } ]",
    "AseJavaLogFilesSpecifications": "[ { \"fileSize\": \"105\", \"throughPut\": \"500\", \"IOPS\": \"3000\" }]",
    "AseBackupFilesSpecifications": "[ { \"fileSize\": \"200\", \"throughPut\": \"30\", \"IOPS\": \"499\" }]",
    "AseJavaSID": "XOX",
    "CustomerTags": "[{\"type\":\"All\",\"key\":\"TestKey1\",\"value\":\"TestValue1\"},{\"type\":\"All\",\"key\":\"TestKey2\",\"value\":\"TestValue2\"},{\"type\":\"All\",\"key\":\"TestKey3\",\"value\":\"TestValue3\"}]",
    "DisableDeploymentRollback": "Yes",
    "AvailabilityZone1PrivateSubnet1Id": "subnet-123456789",
    "CreateSecurityGroup": "No",
    "DatabaseAmiId": "ami-123456789",
    "DatabaseAutomaticRecovery": "Yes",
    "DatabaseBackupVolumeType": "st1",
    "DatabaseDataVolumeType": "gp3",
    "DatabaseInstanceType": "r5.2xlarge",
    "DatabaseLogVolumeType": "gp3",
    "DatabaseOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
    "DatabaseHostname": "sapasedb",
    "PasOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
    "PasAmiId": "ami-123456789",
    "PasHostname": "nwmulpas",
    "PasAutomaticRecovery": "No",
    "PasInstanceType": "r5.2xlarge",
    "EnableCloudwatchLogs": "Yes",
    "EnableEbsVolumeEncryption": "No",
    "InstallSap": "Yes",
    "KeyName": "launchwizard-sap",
    "ApplicationSecurityGroupId": "sg-abcdes1234",
    "DatabaseSecurityGroupId": "sg-abcdes1234",
    "NewSecurityGroupRules": "[]",
    "DatabasePassword": "AseTest134",
    "SapSid": "ACE",
    "SapSysGroupId": "1001",
    "Timezone": "UTC",
    "SaveDeploymentArtifacts": "No",
    "SidAdmUserId": "1002",
    "SybSidUserId": "1003",
    "JavaSybSidUserId": "1006",
    "SetupTransportDomainController": "No",
    "ApplicationDataVolumeType": "gp3",
    "VpcId": "vpc-123456789"
  }
```

Multi-node deployment with resources for SAP ASE ABAP:

```
{
    "SapInstallationSpecifications": "{ \"onFailureBehaviour\":\"ROLLBACK\",\"parameters\":{\"PRODUCT_ID\":\"PRODUCT_ID\":\"sapNetweaver-752\",\"CI_INSTANCE_NR\":\"12\",\"ASCS_INSTANCE_NR\":\"10\",\"SAPINST_CD_SAPCAR\":\"s3:\/\/launchwizardsoftware\/sapmedia\/sapcar\",\"SAPINST_CD_SWPM\":\"s3:\/\/launchwizardsoftware\/sapmedia\/swpm\/20-sp10\",\"SAPINST_CD_KERNEL\":\"s3:\/\/launchwizardsoftware\/sapmedia\/kernel\/785\",\"SAPINST_CD_LOAD\":\"s3:\/\/launchwizardsoftware\/sapmedia\/exports\/s4h-2021\",\"SAPINST_CD_RDBMS\":\"s3:\/\/launchwizardsoftware\/sapmedia\/database\/hana-20-sp06-rev60\" } }",
    "AseAbapDataFilesSpecifications": "[ { \"fileSize\": \"100\", \"throughPut\": \"500\", \"IOPS\": \"3000\" }, { \"fileSize\": \"100\", \"throughPut\": \"500\", \"IOPS\": \"3000\" }, { \"fileSize\": \"100\", \"throughPut\": \"500\", \"IOPS\": \"3000\" } ]",
    "AseAbapLogFilesSpecifications": "[ { \"fileSize\": \"105\", \"throughPut\": \"500\", \"IOPS\": \"3000\" }]",
    "AseBackupFilesSpecifications": "[ { \"fileSize\": \"200\", \"throughPut\": \"30\", \"IOPS\": \"499\" }]",
    "CustomerTags": "[{\"type\":\"All\",\"key\":\"TestKey1\",\"value\":\"TestValue1\"},{\"type\":\"All\",\"key\":\"TestKey2\",\"value\":\"TestValue2\"},{\"type\":\"All\",\"key\":\"TestKey3\",\"value\":\"TestValue3\"}]",
    "DisableDeploymentRollback": "Yes",
    "AvailabilityZone1PrivateSubnet1Id": "subnet-123456789",
    "CreateSecurityGroup": "No",
    "DatabaseAmiId": "ami-123456789",
    "DatabaseAutomaticRecovery": "Yes",
    "DatabaseBackupVolumeType": "st1",
    "DatabaseDataVolumeType": "gp3",
    "DatabaseInstanceType": "r5.2xlarge",
    "DatabaseLogVolumeType": "gp3",
    "DatabaseOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
    "DatabaseHostname": "sapasedb",
    "PasOperatingSystem": "SuSE-Linux-15-SP4-For-SAP-HVM",
    "PasAmiId": "ami-123456789",
    "PasHostname": "nwmulpas",
    "PasAutomaticRecovery": "No",
    "PasInstanceType": "r5.2xlarge",
    "EnableCloudwatchLogs": "Yes",
    "EnableEbsVolumeEncryption": "No",
    "InstallSap": "Yes",
    "KeyName": "launchwizard-sap",
    "ApplicationSecurityGroupId": "sg-123456789",
    "DatabaseSecurityGroupId": "sg-123456789",
    "NewSecurityGroupRules": "[]",
    "DatabasePassword": "Temp123456",
    "SapSid": "ACE",
    "SapSysGroupId": "1001",
    "Timezone": "UTC",
    "SaveDeploymentArtifacts": "No",
    "SidAdmUserId": "1002",
    "SybSidUserId": "1003",
    "SetupTransportDomainController": "No",
    "ApplicationDataVolumeType": "gp3",
    "VpcId": "vpc-123456789"
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
+ **AseJavaSID**

  Type: String

  Description: The SAP JAVA application system ID for installation and setup.

  Constraints: This value must consist of 3 characters.

  Example: HDB

  Conditional: You must specify the `Solman` product ID in `SapInstallSpecification` to provide a value for this specification.

  Required: Yes
+ **JavaSidUserId**

  Type: String

  Description: The system ID user ID for the JAVA application.

  Constraints: The minimum is 100, and the maximum is 65536.

  Example: 1000

  Required: Yes
+ **JavaSybSidUserId**

  Type: String

  Description: The system ID user ID for SAP JAVA application.

  Constraints: The minimum is 100, and the maximum is 65536.

  Example: 1000

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
+ **TransportDomainControllerFileSystemId**

  Type: String

  Example: `fs-1234567890abcdef0`

  Description: The ID of an existing Elastic File System for the transport domain controller.

  Conditional: If you specify `No` for `CreateTransportDomainControllerFileSystem`, you must also provide input for this specification.

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
+ **ConfigurationScripts**

  Type: String

  Example: `{"preConfigurationScripts":{"onFailureBehaviour":"{{CONTINUE}}","configurationScripts":[{"nodeTypesToRunScriptFor":["{{DB}}"],"s3URL":"{{s3://launchwizard-scripts-preconfig-us-west-2/preconfig-install.sh}}","sequence":"{{0}}"}]},"postConfigurationScripts":{"onFailureBehaviour":"{{CONTINUE}}","configurationScripts":[{"nodeTypesToRunScriptFor":["{{DB}}"],"s3URL":"{{s3://launchwizard-scripts-postconfig-us-west-2/postconfig-install.sh}}","sequence":"{{0}}"}]}}`

  Description: A list of pre- and post-configuration deployment scripts formatted as stringified JSON. You can specify one or more pre- or post-configuration scripts separately, or together. You must provide the follow details for each script:
  + The URL for the script that has been uploaded to Amazon S3.
  + A sequence number which specifies the order of execution.
  + The type of node to run the script on. You can specify `DB`, and `PAS`.
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
+ **AasHostnames**

  Type: String

  Example: AASPrimary

  Description: The host name or DNS short name to use for the AAS node.

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
+ **AasVirtualHostnames**

  Type: String

  Description: The virtual host name or DNS short name to use for the AAS node.

  Example: AasVirtualHostname

  Conditional: You must specify `Yes` to `SapVirtualIPOptIn` to provide a value for this specification.

  Required: No
+ **AasVirtualByoip**

  Type: String

  Description: A private virtual IPv4 address to be used by the AAS node.

  Example: 10.0.1.10

  Conditional: You must specify `true` for `InstallAas` and `Yes` to `SapVirtualIPOptIn` to provide a value for this specification.

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
+ **PasHostname**

  Type: String

  Example: PASPrimary

  Description: The host name or DNS short name to use for the PAS node.

  Required: Yes
+ **PasVirtualHostname**

  Type: String

  Description: The virtual host name or DNS short name to use for the database node.

  Example: PasVirtHostName

  Conditional: You must specify `Yes` to `SapVirtualIPOptIn` to provide a value for this specification.

  Required: No
+ **PasVirtualByoip**

  Type: String

  Description: A private virtual IPv4 address to be used by the PAS node.

  Example: 10.0.1.10

  Conditional: You must specify `Yes` to `SapVirtualIPOptIn` to provide a value for this specification.

  Required: No
+ **PasByoip**

  Type: String

  Example: 10.0.1.10

  Description: A private IPv4 address to be used by the PAS node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

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
+ **DatabasePrimaryByoip**

  Type: String

  Example: 10.0.1.10

  Description: A private IPv4 address to be used by the primary SAP HANA node. If no value is provided, Amazon EC2 will assign an available IPv4 address in the subnet.

  Required: No
+ **DatabaseAutomaticRecovery**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specify `Yes` to enable Amazon CloudWatch action based recovery for SAP Hana nodes or `No` to keep it disabled. For HA deployments, set this value to `No` as the cluster will manage availability for the nodes.

  Required: Yes
+ **DedicatedHostId**

  Type: CommaDelimitedList String

  Example: h-012a3456b7890cdef

  Description: The existing Dedicated Hosts on which you want to launch your instances.

  Conditional: If you are using Amazon EC2 High Memory Instances, you must provide an input for this specification. For more information on Amazon EC2 High Memory Instances, see [Amazon EC2 High Memory Instances](https://aws.amazon.com/ec2/instance-types/high-memory/).

  Required: No
+ **DatabaseInstanceType**

  Type: String

  Example: r5.2xlarge

  Description: The instance type used for SAP HANA nodes.

  Required: Yes
+ **DatabaseHostname**

  Type: String

  Description: The host name or DNS short name to use for the database node.

  Example: DBHostName

  Required: No
+ **DatabaseVirtualHostName**

  Type: String

  Description: The virtual host name or DNS short name to use for the database node.

  Example: DBVirtHostName

  Required: No
+ **DatabasePrimaryVirtualByoip**

  Type: String

  Description: A private virtual IPv4 address to be used by the primary SAP HANA node.

  Example: 10.0.1.10

  Conditional: You must specify `Yes` to `SapVirtualIPOptIn` to provide a value for this specification.

  Required: No
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
+ **AseJavaDataFilesSpecifications**

  Type: String

  Description: Parameters for the data filesystem for SAP ASE database formatted as stringified JSON.

  Example: `[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]`

  Required: Yes
+ **AseJavaLogFilesSpecifications**

  Type: String

  Description: Parameters for the log filesystem for SAP ASE database formatted as stringified JSON.

  Example: `[{\"fileSize\":300,\"IOPS\":3000,\"throughPut\":250}]`

  Required: Yes
+ **AseBackupFileSpecifications**

  Type: String

  Example: `[{\"fileSize\":300,\"IOPS\":900,\"throughPut\":250}]`

  Description: Parameters for the backup filesystem for SAP ASE database formatted as stringified JSON.

  Required: Yes
+ **SapVirtualIPOptIn**

  Type: String

  AllowedValues: `Yes` \| `No`

  Description: Specifies if or not a virtual IP address is assigned to the EC2 instance hosting the SAP system.

  Required: No