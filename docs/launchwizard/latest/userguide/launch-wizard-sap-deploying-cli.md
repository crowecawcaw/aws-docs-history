# Deploying an SAP application

(AWS CLI)

You can deploy, describe, and delete SAP applications you create using Launch Wizard with
the AWS CLI. For more information on the AWS Launch Wizard APIs, see the [AWS Launch Wizard API reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Topics

- [Prerequisites](#launch-wizard-sap-deploying-cli-prerequisites "#launch-wizard-sap-deploying-cli-prerequisites")
- [AWS CLI
  examples](#launch-wizard-sap-deploying-cli-examples "#launch-wizard-sap-deploying-cli-examples")

## Prerequisites

The following requirements must be met before you can use the AWS CLI to create
Launch Wizard deployments.

- Install or update the AWS CLI. For more information, see [Install or
  update the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Complete the getting started requirements in [Set up for AWS Launch Wizard for SAP](launch-wizard-sap-setting-up.md "launch-wizard-sap-setting-up.md").

## AWS CLI

examples

The following examples demonstrate how you can use the Launch Wizard API operations
with the AWS CLI.

Create a deployment
You can create a deployment for your SAP application using the
`CreateDeployment` Launch Wizard API operation. You can use
the [ListWorkloadDeploymentPatterns](../APIReference/API_ListWorkloadDeploymentPatterns.md "../APIReference/API_ListWorkloadDeploymentPatterns.md")
operation to discover the supported values for the
`--workload-name` and
`--deployment-pattern-name` parameters. SAP
applications deployed using this API operation can't be cloned from
the AWS Launch Wizard console. For more information, see [CreateDeployment](../APIReference/API_CreateDeployment.md "../APIReference/API_CreateDeployment.md").

###### Tip

You can pass inputs to the `specifications`
parameter for your deployment as a file for easier usage. For
more information on the available specifications for each
deployment pattern, including examples, see [Deployment specifications](../APIReference/launch-wizard-specifications.md "../APIReference/launch-wizard-specifications.md").

```
`$` aws launch-wizard create-deployment --workload-name `SAP` --deployment-pattern-name `SapHanaSingle` --name `ExampleName` --region `us-east-1` --specifications file://`hana-single-specifications.json`

`{
 "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}`
```

Delete a deployment
You can delete an SAP deployment using the
`DeleteDeployment` Launch Wizard API operation. For more
information, see [DeleteDeployment](../APIReference/API_DeleteDeployment.md "../APIReference/API_DeleteDeployment.md").

```
`$` aws launch-wizard delete-deployment --deployment-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` --region `us-east-1`

`{
 "status": "DELETE_INITIATING",
 "statusReason": "Finished processing DeleteApp request"
}`
```

Get deployment details
You can get deployment details for an SAP deployment using the
`GetDeployment` Launch Wizard API operation. For more
information, see [GetDeployment](../APIReference/API_GetDeployment.md "../APIReference/API_GetDeployment.md").

```
`$` aws launch-wizard get-deployment --deployment-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` --region `us-east-1`

`{
 "deployment": {
 "name": "ExampleName",
 "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "workloadName": "SAP",
 "patternName": "SapHanaSingle",
 "status": "COMPLETED",
 "createdAt": "2023-10-10T17:18:49.150000-07:00",
 "specifications": {
 "ApplicationSecurityGroupId": "sg-1234567890abcdef0",
 "AvailabilityZone1PrivateSubnet1Id": "subnet-1234567890abcdef0",
 "CreateSecurityGroup": "No",
 "DatabaseAmiId": "ami-1234567890abcdef0",
 "DatabaseAutomaticRecovery": "Yes",
 "DatabaseDataVolumeType": "gp3",
 "DatabaseHostCount": "1",
 "DatabaseInstanceType": "r3.2xlarge",
 "DatabaseLogVolumeType": "gp3",
 "DatabaseOperatingSystem": "SuSE-Linux-12-SP5-HVM",
 "DatabaseOthersVolumeType": "gp3",
 "DatabasePrimaryHostname": "sapci",
 "DatabaseSecurityGroupId": "sg-1234567890abcdef0",
 "DatabaseSystemId": "HDB",
 "DisableDeploymentRollback": "true",
 "Ec2InstanceRoleName": "AmazonEC2RoleForLaunchWizard",
 "EnableCloudwatchLogs": "Yes",
 "EnableEbsVolumeEncryption": "Yes",
 "EnvironmentType": "production",
 "InstallDatabaseSoftware": "No",
 "KeyPairName": "canary-test",
 "NewSecurityGroupRules": "[{\"type\":\"ip\",\"value\":\"10.0.0.0/32\"}]",
 "PrimaryAZ": "us-east-1a",
 "SapInstanceNumber": "00",
 "SaveDeploymentArtifacts": "false",
 "SnsTopicArn": "arn:aws:sns:us-east-1:111122223333:ExampleTopic",
 "Timezone": "UTC",
 "VpcId": "vpc-1234567890abcdef0"
 },
 "resourceGroup": "LaunchWizard-SapHanaSingle-ExampleGroup-abcd1234"
 }
}`
```

Get workload details
You can get workload details for an SAP deployment using the
`GetWorkload` Launch Wizard API operation. For more
information, see [GetWorkload](../APIReference/API_GetWorkload.md "../APIReference/API_GetWorkload.md").

```
`$` aws launch-wizard get-workload --workload-name `SAP` --region `us-east-1`

`{
 "workload": {
 "workloadName": "SAP",
 "displayName": "SAP",
 "description": "AWS Launch Wizard for SAP is a service that guides you through the sizing, configuration, and deployment of SAP applications on AWS.",
 "documentationUrl": https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html,
 "iconUrl": "https://example.com/example.png",
 "status": "ACTIVE"
 }
}`
```

List deployments
You can list an SAP deployment using the
`ListDeployments` Launch Wizard API operation. For more
information, see [ListDeployments](../APIReference/API_ListDeployments.md "../APIReference/API_ListDeployments.md").

```
`$` aws launch-wizard list-deployments --filter name=`DEPLOYMENT_STATUS`,values=`IN_PROGRESS` --region `us-east-1`

`{
 "deployments": [
 {
 "name": "ExampleName",
 "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "workloadName": "SAP",
 "patternName": "SapHanaSingle",
 "status": "IN_PROGRESS",
 "createdAt": "2023-04-24T13:10:09.857000-07:00"
 }
 ]
}`
```

List deployment events
You can list SAP deployment events using the
`ListDeploymentEvents` Launch Wizard API operation. For more
information, see [ListDeploymentEvents](../APIReference/API_ListDeployments.md "../APIReference/API_ListDeployments.md").

```
`$` aws launch-wizard list-deployment-events --deployment-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` --region `us-east-1`

`{
 "deploymentEvents": [
 {
 "name": "Create secure parameter",
 "description": "Creates a new secure parameter",
 "status": "COMPLETED",
 "statusReason": "",
 "timestamp": "2021-12-22T16:35:17.227000-08:00"
 },
 {
 "name": "Create resource group",
 "description": "Creates a resource group with all the application resources",
 "status": "COMPLETED",
 "statusReason": "",
 "timestamp": "2021-12-22T16:35:17.909000-08:00"
 },
 {
 "name": "Delete application resource group",
 "description": "Deletes the application resource group",
 "status": "COMPLETED",
 "statusReason": "",
 "timestamp": "2023-05-10T15:50:51.156000-07:00"
 },
 {
 "name": "Delete secure parameters",
 "description": "Deletes a secure parameter",
 "status": "COMPLETED",
 "statusReason": "",
 "timestamp": "2023-05-10T15:50:51.451000-07:00"
 }
 ]
}`
```

List workloads
You can list workload details for SAP deployments using the
`ListWorkloads` Launch Wizard API operation. For more
information, see [ListWorkloads](../APIReference/API_ListWorkloads.md "../APIReference/API_ListWorkloads.md").

```
`$` aws launch-wizard list-workloads --region `us-east-1`

`{
 "workloads": [
 {
 "displayName": "SAP",
 "workloadName": "SAP"
 },
 {
 "displayName": "Exchange Server",
 "workloadName": "ExchangeServer"
 },
 {
 "displayName": "MS SQL Server",
 "workloadName": "SQL"
 },
 {
 "displayName": "Amazon EKS",
 "workloadName": "EKS"
 },
 {
 "displayName": "Microsoft Active Directory",
 "workloadName": "MicrosoftActiveDirectory"
 },
 {
 "displayName": "Microsoft IIS",
 "workloadName": "IIS"
 },
 {
 "displayName": "Remote Desktop Gateway",
 "workloadName": "RDGW"
 }
 ]
}`
```

List workload deployment patterns
You can list the available patterns for SAP workloads using the
`ListWorkloadDeploymentPatterns` Launch Wizard API operation.
For more information, see [ListWorkloadDeploymentPatterns](../APIReference/API_ListWorkloadDeploymentPatterns.md "../APIReference/API_ListWorkloadDeploymentPatterns.md").

```
`$` aws launch-wizard list-workload-deployment-patterns --workload-name `SAP` --region `us-east-1`

`{
 "workloadDeploymentPatterns": [
 {
 "workloadName": "SAP",
 "deploymentPatternName": "SapHanaHA",
 "workloadVersionName": "2023-10-30-23-00-00",
 "displayName": "Cross-AZ SAP HANA database high availability setup",
 "description": "Deploy SAP HANA with high availability configured across two Availability Zones.",
 "status": "ACTIVE"
 },
 {
 "workloadName": "SAP",
 "deploymentPatternName": "SapHanaMulti",
 "workloadVersionName": "2023-10-30-23-00-00",
 "displayName": "SAP HANA database on multiple EC2 instances",
 "description": "Deploy SAP HANA in a multi-node, scale-out architecture.",
 "status": "ACTIVE"
 },
 {
 "workloadName": "SAP",
 "deploymentPatternName": "SapHanaSingle",
 "workloadVersionName": "2023-10-30-23-00-00",
 "displayName": "SAP HANA database on a single Amazon EC2 instance",
 "description": "Deploy SAP HANA in a single-node, scale-up architecture, with up to 24TB of memory.",
 "status": "ACTIVE"
 },
 {
 "workloadName": "SAP",
 "deploymentPatternName": "SapNWOnHanaHA",
 "workloadVersionName": "2023-10-30-23-00-00",
 "displayName": "Cross-AZ SAP NetWeaver system setup",
 "description": "Deploy Amazon EC2 instances for ASCS/ERS and SAP HANA databases across two Availability Zones, and spread the deployment of application servers across them.",
 "status": "ACTIVE"
 },
 {
 "workloadName": "SAP",
 "deploymentPatternName": "SapNWOnHanaMulti",
 "workloadVersionName": "2023-10-30-23-00-00",
 "displayName": "SAP NetWeaver system on multiple EC2 instances",
 "description": "Deploy an SAP NetWeaver system using a distributed deployment model, which includes an ASCS/PAS server, single/multiple SAP HANA servers running SAP HANA databases, and multiple application servers.",
 "status": "ACTIVE"
 },
 {
 "workloadName": "SAP",
 "deploymentPatternName": "SapNWOnHanaSingle",
 "workloadVersionName": "2023-10-30-23-00-00",
 "displayName": "SAP NetWeaver on SAP HANA system on a single Amazon EC2 instance",
 "description": "Deploy an SAP application on the same Amazon EC2 instance as your SAP HANA Database.",
 "status": "ACTIVE"
 }
 ]
}`
```
