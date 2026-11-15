

# Configure Migration Defaults
<a name="transform-vmware-ms-migration-defaults"></a>

AWS Transform provides intelligent defaults for your migration configuration, including how Amazon EC2 instances are launched and how replication is set up. You can accept these defaults and start migrating immediately, or customize them through the chat interface or a visual review. Defaults apply across all your target accounts and can be overridden at the wave level during wave setup.

## Amazon EC2 recommendation preferences
<a name="transform-vmware-ms-ec2-recommendations"></a>

AWS Transform analyzes your source server utilization and recommends optimally sized Amazon EC2 instances, which helps you avoid overprovisioning from the start. You can configure your Amazon EC2 recommendation preferences to control how instance types are selected for your migrated servers.

AWS Transform uses the same Amazon EC2 rightsizing mechanism as compute assessments. For more information about how Amazon EC2 recommendations are generated, see [Amazon EC2 right-sizing](transform-app-assessments-compute.md#transform-app-assessments-compute-ec2).

**Note**  
You can modify the suggested Amazon EC2 instance types to include recommendations from the [Migration Evaluator](https://aws.amazon.com/migration-evaluator/), [AWS Optimization and Licensing Assessment (OLA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/aws-ola.html), or an AWS Transform assessment job.

## Migration initialization
<a name="transform-vmware-ms-mgn-initialization"></a>

AWS Transform automatically sets up the required migration infrastructure in your target accounts before migration begins. This includes initializing MGN for every AWS Region in which you plan to migrate, as well as all target accounts. During the initialization process:
+ The required IAM roles and policies are created.
+ The required default templates are configured.

For information about the initialization process, see [Initializing AWS Transform MGN with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html) in the *MGN User Guide*.

## Amazon EC2 launch template
<a name="transform-vmware-ms-default-launch"></a>

The launch settings include two parts: the general launch settings, and the Amazon EC2 launch template, which determines how a test or cutover instance is launched for each source server in AWS.

Launch settings, including the Amazon EC2 launch template, can be defined at the account level and are then applied to each source server automatically each time you add a source server to AWS Transform MGN. The launch settings defaults defined in this section can be applied to all your target accounts automatically.

AWS Transform presents the list of available launch template settings. You can choose to continue with the defaults or configure your launch template. If you choose to configure, AWS Transform provides a link to a human-in-the-loop (HITL) review that contains all the parameters of the launch template settings. You can also make modifications directly through the chat interface for any parameters you wish.

[Source servers](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html) are created with the account launch template settings. After source servers are created with these default settings, you can change them at the source server launch settings level. You can change source server settings on any parameter using the chat interface, or for bulk operations using the inventory Excel file during [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md).

To review the full list of launch template settings and details, see [Launch general settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-general-settings.html) in the *MGN User Guide*.

## Additional Amazon EC2 launch template changes
<a name="transform-vmware-ms-launch-template-changes"></a>

Make additional Amazon EC2 launch template changes on the template ID for each target account. This option is available inside the wave setup. AWS Transform guides you through it and provides the appropriate link.

## Post-launch actions
<a name="transform-vmware-ms-post-launch-actions"></a>

Post-launch actions automate modernization and validation tasks that run on each source server immediately after it launches as a test or cutover instance in AWS. AWS Transform Rehost takes the post-launch actions available in MGN and provides these capabilities so that the agent can recommend, configure, and run them on your behalf as part of the migration workflow. Actions are run through AWS Systems Manager (Systems Manager), and can be either one of the predefined actions available in MGN or a custom action created from an existing Systems Manager document.

Post-launch actions can be defined at the account level and are then applied to each source server automatically each time you add a source server to MGN. The post-launch action defaults defined in this section can be applied to all your target accounts automatically.

AWS Transform first presents the list of available post-launch actions across your target accounts. It then offers to define a new post-launch action and apply it across your target account migration. AWS Transform also provides AI-powered recommendations based on the operating system and best practices for your inventory. You can choose to continue with the defaults or configure your own actions.

You can also choose a post-launch action that is already defined in MGN. Prompt the agent to show the list of predefined post-launch actions available. For more information about this list, see [Predefined post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html) in the *MGN User Guide*.

### Creating a new post-launch action
<a name="transform-vmware-ms-post-launch-create"></a>

If you choose to create a new post-launch action, the agent prompts you to provide the Systems Manager document name or Systems Manager ARN to build the post-launch action with. The Systems Manager document should be created in advance through the AWS Systems Manager console. For more information about creating a Systems Manager document, see [Creating Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html) in the *AWS Systems Manager User Guide*.

The agent then generates a human-in-the-loop interface where you provide the required fields:
+ **Post-launch action name** – The agent provides a default name, which you can change.
+ **Post-launch action order** – The default order value is 1001, unless the account already has post-launch actions defined, in which case the new action is placed last in the run order. You can change the order. For more information about post-launch action order, see [Post-launch settings](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html) in the *MGN User Guide*.
+ **Required Systems Manager parameter values** – Provide the values for any parameters required by the Systems Manager document.

You can also make modifications directly through the chat interface for any parameters you wish.

Source servers are created with the account post-launch action settings. After source servers are created with these default settings, you can change them at the source server level. You can change source server settings on any action using the chat interface, or for bulk operations using the inventory Excel file during [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md).

### Post-launch actions in the inventory file
<a name="transform-vmware-ms-post-launch-inventory"></a>

The Rehost agent extends the inventory file with a post-launch action template defined for each source server. This allows customers to update or add post-launch actions per source server during the rehost to MGN import process. To delete specific post-launch actions from a source server, use the `active` column to indicate `FALSE`. Post-launch actions in the inventory file use the following naming convention:

`mgn:launch:post-actions:<ACTION_NAME>:<FIELD_NAME>`

A global toggle controls whether post-launch actions run:

`mgn:launch:post-actions:enabled` (`TRUE`/`FALSE`)

**Fields per action**
+ `ssmDocumentName` (String, required) – The Systems Manager document to execute.
+ `order` (Integer, required) – Execution order; must be between 1000 and 10000. Actions execute in ascending order — lower values run first.
+ `active` (`TRUE`/`FALSE`, optional) – Whether the action is active.
+ `mustSucceedForCutover` (`TRUE`/`FALSE`, optional) – Whether the action must succeed before cutover.
+ `timeoutSeconds` (Integer, optional) – Timeout in seconds.
+ `description` (String, optional) – Human-readable description.
+ `parameters` (JSON, optional) – Systems Manager document parameters.

**Parameters JSON structure**

The `parameters` field is provided as a JSON structure:

```
{
  "parameters": {
    "Operation": [
      {"value": "Scan", "type": "String"}
    ]
  },
  "externalParameters": {
    "InstanceId": "ec2.InstanceId"
  }
}
```
+ `parameters` – Maps document parameter names to a list of value references (each with a `value` and an optional `type`, which defaults to `String`).
+ `externalParameters` – Maps document parameter names to dynamic path strings (no Systems Manager parameter is created).