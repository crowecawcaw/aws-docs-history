• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Using the Quick Setup API to manage configurations and

deployments

You can use the API provided by Quick Setup to create and manage configurations and
deployments using the AWS CLI or your preferred SDK. You can also use CloudFormation to create a
configuration manager resource that deploys configurations. Using the API, you create
configuration managers that deploy configuration _definitions_.
Configuration definitions contain all of the necessary information to deploy a
particular configuration type. For more information about the Quick Setup API, see the
[Quick Setup API
Reference](../../../quick-setup/latest/APIReference.md "../../../quick-setup/latest/APIReference.md").

The following examples demonstrate how to create configuration managers using the
AWS CLI and CloudFormation.

AWS CLI

```
aws ssm-quicksetup create-configuration-manager \
--name `configuration manager name` \
--description `Description of your configuration manager`
--configuration-definitions `JSON string containing configuration defintion`
```

The following is an example JSON string containing a configuration
definition for patch policy.

```
'{"Type":"AWSQuickSetupType-PatchPolicy","LocalDeploymentAdministrationRoleArn":"arn:aws:iam::123456789012:role/AWS-QuickSetup-StackSet-Local-AdministrationRole","LocalDeploymentExecutionRoleName":"AWS-QuickSetup-StackSet-Local-ExecutionRole","Parameters":{"ConfigurationOptionsInstallNextInterval":"true","ConfigurationOptionsInstallValue":"cron(0 2 ? * SAT#1 *)","ConfigurationOptionsPatchOperation":"ScanAndInstall","ConfigurationOptionsScanNextInterval":"false","ConfigurationOptionsScanValue":"cron(0 1 * * ? *)","HasDeletedBaseline":"false","IsPolicyAttachAllowed":"true","OutputBucketRegion":"","OutputLogEnableS3":"false","OutputS3BucketName":"","OutputS3KeyPrefix":"","PatchBaselineRegion":"us-east-1","PatchBaselineUseDefault":"custom","PatchPolicyName":"dev-patch-policy","RateControlConcurrency":"5","RateControlErrorThreshold":"0%","RebootOption":"RebootIfNeeded","ResourceGroupName":"","SelectedPatchBaselines":"{\"ALMA_LINUX\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-0cb0c4966f86b059b\",\"label\":\"AWS-AlmaLinuxDefaultPatchBaseline\",\"description\":\"Default Patch Baseline for Alma Linux Provided by AWS.\",\"disabled\":false},\"AMAZON_LINUX_2\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-0be8c61cde3be63f3\",\"label\":\"AWS-AmazonLinux2DefaultPatchBaseline\",\"description\":\"Baseline containing all Security and Bugfix updates approved for Amazon Linux 2 instances\",\"disabled\":false},\"AMAZON_LINUX_2023\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-05c9c9bf778d4c4d0\",\"label\":\"AWS-AmazonLinux2023DefaultPatchBaseline\",\"description\":\"Default Patch Baseline for Amazon Linux 2023 Provided by AWS.\",\"disabled\":false},\"DEBIAN\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-09a5f8eb62bde80b1\",\"label\":\"AWS-DebianDefaultPatchBaseline\",\"description\":\"Default Patch Baseline for Debian Provided by AWS.\",\"disabled\":false},\"MACOS\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-0ee4f94581368c0d4\",\"label\":\"AWS-MacOSDefaultPatchBaseline\",\"description\":\"Default Patch Baseline for MacOS Provided by AWS.\",\"disabled\":false},\"ORACLE_LINUX\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-06bff38e95fe85c02\",\"label\":\"AWS-OracleLinuxDefaultPatchBaseline\",\"description\":\"Default Patch Baseline for Oracle Linux Server Provided by AWS.\",\"disabled\":false},\"REDHAT_ENTERPRISE_LINUX\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-0cbb3a633de00f07c\",\"label\":\"AWS-RedHatDefaultPatchBaseline\",\"description\":\"Default Patch Baseline for Redhat Enterprise Linux Provided by AWS.\",\"disabled\":false},\"ROCKY_LINUX\":{\"value\":\"arn:aws:ssm:us-east-1:123456789012:patchbaseline/pb-03ec98bc512aa3ac0\",\"label\":\"AWS-RockyLinuxDefaultPatchBaseline\",\"description\":\"Default Patch Baseline for Rocky Linux Provided by AWS.\",\"disabled\":false},\"UBUNTU\":{\"value\":\"pb-06e3563bd35503f2b\",\"label\":\"custom-UbuntuServer-Blog-Baseline\",\"description\":\"Default Patch Baseline for Ubuntu Provided by AWS.\",\"disabled\":false},\"WINDOWS\":{\"value\":\"pb-016889927b2bb8542\",\"label\":\"custom-WindowsServer-Blog-Baseline\",\"disabled\":false}}","TargetInstances":"","TargetOrganizationalUnits":"ou-9utf-example","TargetRegions":"us-east-1,us-east-2","TargetTagKey":"Patch","TargetTagValue":"true","TargetType":"Tags"}}' \
```

CloudFormation

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
SSMQuickSetupTestConfigurationManager:
Type: "AWS::SSMQuickSetup::ConfigurationManager"
Properties:
    Name: "MyQuickSetup"
    Description: "Test configuration manager"
    ConfigurationDefinitions:
    - Type: "AWSQuickSetupType-CFGRecording"
      Parameters:
        TargetAccounts:
            Ref: AWS::AccountId
        TargetRegions:
            Ref: AWS::Region
        LocalDeploymentAdministrationRoleArn: !Sub "arn:aws:iam::${AWS::AccountId}:role/AWS-QuickSetup-StackSet-ContractTest-AdministrationRole"
        LocalDeploymentExecutionRoleName: "AWS-QuickSetup-StackSet-ContractTest-ExecutionRole"
    Tags:
        foo1: "bar1"
```
