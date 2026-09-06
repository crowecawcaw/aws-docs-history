

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Initializing AWS Transform MGN with the API
<a name="mgn-initialize-api"></a>

In order to use AWS Transform MGN (MGN), the service must first be initialized for any AWS Region in which you plan to use MGN.

You can initialize the service via the console or via the API.

During the initialization process:
+ The required IAM roles and policies will be created.
+ The required templates are configured.

You can initialize AWS Transform MGN through the API. This option allows you to automate service initialization through a script when initializing multiple accounts.

You can also initialize MGN using the console. For more information, see [Initializing MGN with the console](mgn-initialize-console.md).

To initialize the service via the API, take the following steps:

1. Create the required IAM roles.

1. Create the replication template and launch template.
**Note**  
You must complete both steps to finalize the service initialization process.

## Creating the required IAM roles
<a name="mgn-initialize-api-iam"></a>

To initialize MGN with the API, create the following IAM roles through the [IAM CreateRole API](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html). Learn more about [creating IAM roles in the AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html). Creation of each role must include the following parameters:



<table>
<thead>
  <tr><th>Role name</th><th colspan="3">Trusted entities</th></tr>
  <tr><th></th><th><b>Principal</b></th><th><b>Action</b></th><th><b>Condition</b></th></tr>
</thead>
<tbody>
  <tr><td><b>AWSApplicationMigrationReplicationServerRole</b></td><td>"ec2.amazonaws.com"</td><td>"sts:AssumeRole"</td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationConversionServerRole</b></td><td>"ec2.amazonaws.com"</td><td>"sts:AssumeRole"</td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationMGHRole</b></td><td>"mgn.amazonaws.com"</td><td>"sts:AssumeRole"</td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationLaunchInstanceWithDrsRole</b></td><td>"ec2.amazonaws.com"</td><td>"sts:AssumeRole"</td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationLaunchInstanceWithSsmRole</b></td><td>"ec2.amazonaws.com"</td><td>"sts:AssumeRole" </td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationFsxProxyRole</b></td><td>"mgn.amazonaws.com"</td><td>"sts:AssumeRole"</td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationFsxProxyLinkRole</b></td><td>"mgn.amazonaws.com"</td><td>"sts:AssumeRole"</td><td>-</td></tr>
  <tr><td><b>AWSApplicationMigrationAgentRole</b></td><td>"mgn.amazonaws.com"</td><td>["sts:AssumeRole", "sts:SetSourceIdentity"]</td><td>{"StringLike": {"sts:SourceIdentity": "s-*", "aws:SourceAccount": "&lt;SOURCE-ACCOUNT-ID&gt;"}</td></tr>
</tbody>
</table>


1. Attach Managed Policy** AWSApplicationMigrationReplicationServerPolicy** to Role **AWSApplicationMigrationReplicationServerRole**

1. Attach Managed Policy **AWSApplicationMigrationConversionServerPolicy **to Role **AWSApplicationMigrationConversionServerRole**

1. Attach Managed Policy** AWSApplicationMigrationMGHAccess** to Role **AWSApplicationMigrationMGHRole**

1. Attach Managed Policies** AmazonSSMManagedInstanceCore** and ** AWSElasticDisasterRecoveryEc2InstancePolicy** to Role **AWSApplicationMigrationLaunchInstanceWithDrsRole**

1. Attach Managed Policy** AmazonSSMManagedInstanceCore** to Role **AWSApplicationMigrationLaunchInstanceWithSsmRole**

1. Attach Managed Policy** AWSApplicationMigrationFSxProxyPolicy** to Role **AWSApplicationMigrationFsxProxyRole**

1. Attach Managed Policy** AWSApplicationMigrationFSxProxyVPCPolicy** to Role **AWSApplicationMigrationFsxProxyLinkRole**

1. Attach Managed Policy** AWSApplicationMigrationAgentPolicy\_v2** to Role **AWSApplicationMigrationAgentRole**

Once the policies are attached to the roles, run the `aws mgn initialize-service` command. This will automatically create the service-linked role, create instance profiles, and add Roles to Instance Profiles. After running this command, you must still create the replication configuration template and launch configuration template to finalize initialization. 

[Learn more about AWS Transform MGN roles and managed policies](security-iam-awsmanpol.md).

## Creating the templates
<a name="mgn-initialize-api-templates"></a>

To finalize the initialization process, you will need to [create the replication template](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateReplicationConfigurationTemplate.html) and launch template by running the following commands:
+ `aws mgn create-replication-configuration-template`
+ `aws mgn create-launch-configuration-template`