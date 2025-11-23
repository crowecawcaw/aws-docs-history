# Create CloudFormation StackSets with

service-managed permissions

With _service-managed_ permissions, you can deploy stacks to
accounts managed by AWS Organizations in specific Regions. With this model, you don't need to
create IAM roles in each target account and AWS Region. CloudFormation creates the IAM
roles on your behalf. For more information, see [Activate trusted
access](stacksets-orgs-activate-trusted-access.md "stacksets-orgs-activate-trusted-access.md").

###### Topics

- [Considerations](#stacksets-orgs-considerations "#stacksets-orgs-considerations")
- [Create a StackSet
  with service-managed permissions (console)](#stacksets-orgs-associate-stackset-with-org-console "#stacksets-orgs-associate-stackset-with-org-console")
- [Create a StackSet with
  service-managed permissions (AWS CLI)](#stacksets-orgs-associate-stackset-with-org-cli "#stacksets-orgs-associate-stackset-with-org-cli")

## Considerations

Before you create a StackSet with service-managed permissions, consider the
following:

- StackSets with service-managed permissions can be initiated by either
  your organization's management account or delegated administrator accounts,
  but all operations are performed by the management account.
- CloudFormation doesn't deploy stacks to the management account, even if that
  account is part of your organization or belongs to an organizational unit
  (OU).
- Your StackSet can target your entire organization (includes all accounts) or
  specified OUs. When a StackSet targets a parent OU, it automatically includes
  any child OUs. By default, when a StackSet targets specific OUs, it includes all
  accounts within those OUs. However, you can target specific accounts using
  account filter options.
- Multiple StackSets can target the same organization or OU.
- Your can't target accounts outside your organization.
- Your authorization to deploy StackSets depends on the permissions
  assigned to the IAM principal (user, role, or group) you use to sign in to
  the management account. For an example IAM policy that grants permissions
  to deploy to an organization, see [Restrict stack
  set operations based on Region and resource types](security_iam_id-based-policy-examples.md#resource-level-permissions-service-managed-stack-set "security_iam_id-based-policy-examples.md#resource-level-permissions-service-managed-stack-set").
- Delegated administrators have full permissions to deploy to any account in
  your organization. The management account can't limit delegated administrator
  permissions to deploy to specific OUs or StackSet operations.
- Automatic deployment settings apply at the StackSet level. You can't adjust
  automatic deployments selectively for OUs, accounts, or Regions.
- StackSets that use service-managed permissions don't support nested
  stacks or templates that contain macros or transforms.

## Create a StackSet

with service-managed permissions (console)

###### To create a StackSet

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
   that you want to manage the StackSet from.
3. From the navigation pane, choose **StackSets**.
4. From the top of the **StackSets** page, choose
   **Create StackSet**.
5. Under **Permissions**, choose **Service-managed
   permissions**.

###### Note

If trusted access with AWS Organizations is disabled, a banner displays.
Trusted access is required to create or update a StackSet with
service-managed permissions. Only the administrator in the
organization's management account has permissions to [Activate trusted access for
StackSets with AWS Organizations](stacksets-orgs-activate-trusted-access.md "stacksets-orgs-activate-trusted-access.md"). 6. Under **Prerequisite - Prepare template**, choose
**Template is ready**. 7. Under **Specify template**, choose to either specify the
URL for the S3 bucket that contains your stack template or upload a stack
template file. Then, choose **Next**. 8. On the **Specify StackSet details** page, provide a name
for the StackSet, specify any parameters, and then choose
**Next**. 9. On the **Configure StackSet options** page, under
**Tags**, specify any tags to apply to resources in
your stack. For more information about how tags are used in AWS, see
[Organizing
and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing and Cost Management User Guide_. 10. For **Execution configuration**, choose
**Active** to enable CloudFormation's optimized operation
handling:

    * Non-conflicting operations run concurrently for faster deployment
     times.
    * Conflicting operations are automatically queued and processed in
     the order they were requested.

While operations are running or queued, CloudFormation queues all incoming
operations even if they're non-conflicting. You can't change execution
settings during this time. 11. If your template contains IAM resources, for
**Capabilities**, choose **I acknowledge that
this template may create IAM resources** to specify that you
want to use IAM resources in the template. For more information, see [Acknowledging IAM resources in CloudFormation
templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities"). 12. Choose **Next** to proceed and to activate trusted access
if not already activated. 13. On the **Set deployment options** page, under
**Deployment targets**, do one of the following:

    * To deploy to all accounts in your organization, choose
     **Deploy to organization**.
    * To deploy to all accounts in specific OUs, choose **Deploy
     to organizational units (OUs)**. Choose **Add
     an OU**, and then paste the target OU ID in the text
     box. Repeat for each new target OU.

If you chose **Deploy to organizational units (OUs)**,
for **Account filter type**, you can set your deployment
targets to be specific individual accounts by choosing one of the following
options and providing account numbers.

    * **None** (default) – Deploy stacks to all
     accounts in the specified OUs.
    * **Intersection** – Deploy stacks to
     specific individual accounts within the selected OUs.
    * **Difference** – Deploy stacks to all
     accounts in the selected OUs except for specific accounts.
    * **Union** – Deploy stacks to the specified
     OUs plus additional individual accounts.

14. Under **Automatic deployment**, choose whether to
    automatically deploy to accounts that are added to the target organization
    or OUs in the future. For more information, see [Enable or disable automatic
    deployments for StackSets in AWS Organizations](stacksets-orgs-manage-auto-deployment.md "stacksets-orgs-manage-auto-deployment.md").
15. If you enabled automatic deployment, under **Account removal
    behavior**, choose whether stack resources are retained or
    deleted when an account is removed from a target organization or OU.

###### Note

With **Retain stacks** selected, stacks are removed
from your StackSet, but the stacks and their associated resources are
retained. The resources stay in their current state, but will no longer
be part of the StackSet. 16. Under **Specify regions**, choose the Regions you want to
deploy stacks in. 17. For **Deployment options**, do the following:

    * For **Maximum concurrent accounts**, specify how
     many accounts are processed concurrently.
    * For **Failure tolerance**, specify the maximum
     number of account failures allowed per Region. The operation will
     stop and won't proceed to other Regions once this limit is
     reached.
    * For **Region concurrency**, choose how to process
     Regions: **Sequential** (one Region at a time) or
     **Parallel** (multiple Regions
     concurrently).
    * For **Concurrency mode**, choose how concurrency
     behaves during operation execution.




    	+ **Strict failure tolerance** –
    	 Reduces account concurrency level when failures occur,
    	 staying within **Failure tolerance**
    	 +1.
    	+ **Soft failure tolerance** –
    	 Maintains your specified concurrency level (the value of
    	 **Maximum concurrent accounts**)
    	 regardless of failures.
    * For StackSet **dependencies**, add dependent StackSet
     ARNs, staying within 10 dependencies maximum. For more information,
     see [Enable or disable automatic
     deployments for StackSets in AWS Organizations](stacksets-orgs-manage-auto-deployment.md "stacksets-orgs-manage-auto-deployment.md").

18. Choose **Next** to continue.
19. On the **Review** page, verify that your StackSet will deploy
    to the correct accounts in the correct Regions, and then choose
    **Create StackSet**.

The **StackSet details** page opens. You can view the
progress and status of the creation of the stacks in your StackSet.

## Create a StackSet with

service-managed permissions (AWS CLI)

Follow the steps in this section to use the AWS CLI to:

- Create the StackSet container.
- Deploy stack instances.

###### Note

When acting as a delegated administrator, you must include `--call-as
 DELEGATED_ADMIN` in the command.

Deploy to your organization

###### To create a StackSet

1. Use the [create-stack-set](../../../cli/latest/reference/cloudformation/create-stack-set.md "../../../cli/latest/reference/cloudformation/create-stack-set.md") command to
   create a new StackSet named
   `my-stackset`. The
   following example uses a template stored in an S3 bucket,
   enables automatic deployments, and preserves stacks when
   accounts are removed. For more information, see [Enable or disable automatic
   deployments for StackSets in AWS Organizations](stacksets-orgs-manage-auto-deployment.md "stacksets-orgs-manage-auto-deployment.md").

```
aws cloudformation create-stack-set \
  --stack-set-name `my-stackset` \
  --template-url `https://s3.region-code.amazonaws.com/amzn-s3-demo-bucket/MyApp.template` \
  --permission-model `SERVICE_MANAGED` \
  --auto-deployment Enabled=`true`,RetainStacksOnAccountRemoval=`true`,DependsOn=`ARN1,ARN2`
```

2. Use the [list-stack-sets](../../../cli/latest/reference/cloudformation/list-stack-sets.md "../../../cli/latest/reference/cloudformation/list-stack-sets.md") command to
   confirm that your StackSet was created. Your new StackSet is listed in
   the results.

```
aws cloudformation list-stack-sets
```

    * If you set the `--call-as` option to
     `DELEGATED_ADMIN` while signed in to your
     member account, **list-stack-sets**
     returns all StackSets with service-managed
     permissions in the organization's
     management account.
    * If you set the `--call-as` option to
     `SELF` while signed in to your
     AWS account, **list-stack-sets**
     returns all self-managed StackSets in your
     AWS account.
    * If you set the `--call-as` option to
     `SELF` while signed in to the
     organization's management account,
     **list-stack-sets** returns all
     StackSets in the organization's
     management account.

3. Use the [create-stack-instances](../../../cli/latest/reference/cloudformation/create-stack-instances.md "../../../cli/latest/reference/cloudformation/create-stack-instances.md") command
   to add stacks to your StackSet. For the
   `--deployment-targets` option, specify the
   organization root ID to deploy to all accounts in your
   organization.

Set concurrent account processing and other deployment
preferences using the `--operation-preferences`
option. This example uses count-based settings. Note that
`MaxConcurrentCount` must not exceed
`FailureToleranceCount` + 1. For percentage-based
settings, use `FailureTolerancePercentage` or
`MaxConcurrentPercentage` instead.

```
aws cloudformation create-stack-instances --stack-set-name `my-stackset` \
  --deployment-targets OrganizationalUnitIds=`r-a1b2c3d4e5` \
  --regions `us-west-2 us-east-1` \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

For more information, see [CreateStackInstances](../APIReference/API_CreateStackInstances.md "../APIReference/API_CreateStackInstances.md") in the
_AWS CloudFormation API Reference_. 4. Using the `operation-id` that was returned as part
of the **create-stack-instances** output, use the
following [describe-stack-set-operation](../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md "../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md")
command to verify that your stacks were created
successfully.

```
aws cloudformation describe-stack-set-operation \
  --stack-set-name `my-stackset` \
  --operation-id `operation_ID`
```

Deploy to organizational units (OUs)

###### To create a StackSet

1. Use the [create-stack-set](../../../cli/latest/reference/cloudformation/create-stack-set.md "../../../cli/latest/reference/cloudformation/create-stack-set.md") command to
   create a new StackSet named
   `my-stackset`. The
   following example uses a template stored in an S3 bucket and
   includes a parameter that sets a
   `KeyPairName` with
   the value `TestKey`

```
aws cloudformation create-stack-set \
  --stack-set-name `my-stackset` \
  --template-url `https://s3.region-code.amazonaws.com/amzn-s3-demo-bucket/MyApp.template` \
  --permission-model `SERVICE_MANAGED` \
  --parameters `ParameterKey=KeyPairName,ParameterValue=TestKey`
```

2. Use the [list-stack-sets](../../../cli/latest/reference/cloudformation/list-stack-sets.md "../../../cli/latest/reference/cloudformation/list-stack-sets.md") command to
   confirm that your StackSet was created. Your new StackSet is listed in
   the results.

```
aws cloudformation list-stack-sets
```

    * If you set the `--call-as` option to
     `DELEGATED_ADMIN` while signed in to your
     member account, **list-stack-sets**
     returns all StackSets with service-managed
     permissions in the organization's
     management account.
    * If you set the `--call-as` option to
     `SELF` while signed in to your
     AWS account, **list-stack-sets**
     returns all self-managed StackSets in your
     AWS account.
    * If you set the `--call-as` option to
     `SELF` while signed in to the
     organization's management account,
     **list-stack-sets** returns all
     StackSets in the organization's
     management account.

3. Use the [create-stack-instances](../../../cli/latest/reference/cloudformation/create-stack-instances.md "../../../cli/latest/reference/cloudformation/create-stack-instances.md") command
   to add stacks to your StackSet. For the
   `--deployment-targets` option, specify the OU IDs
   to deploy to.

Set concurrent account processing and other deployment
preferences using the `--operation-preferences`
option. This example uses count-based settings. Note that
`MaxConcurrentCount` must not exceed
`FailureToleranceCount` + 1. For percentage-based
settings, use `FailureTolerancePercentage` or
`MaxConcurrentPercentage` instead.

```
aws cloudformation create-stack-instances --stack-set-name `my-stackset` \
  --deployment-targets OrganizationalUnitIds=`ou-rcuk-1x5j1lwo,ou-rcuk-slr5lh0a` \
  --regions `us-west-2 us-east-1` \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

For more information, see [CreateStackInstances](../APIReference/API_CreateStackInstances.md "../APIReference/API_CreateStackInstances.md") in the
_AWS CloudFormation API Reference_. 4. Using the `operation-id` that was returned as part
of the **create-stack-instances** output, use the
following [describe-stack-set-operation](../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md "../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md")
command to verify that your stacks were created
successfully.

```
aws cloudformation describe-stack-set-operation \
  --stack-set-name `my-stackset` \
  --operation-id `operation_ID`
```

Deploy to specific accounts in OUs
You can target specific organizational units (OUs) and use account
filtering to precisely control which accounts receive stack deployments.
By default, stacks deploy to all accounts within specified OUs if no
account filtering is specified.

In the AWS CLI, you specify account filtering with the
`--deployment-targets` option. For more information, see
[DeploymentTargets](../APIReference/API_DeploymentTargets.md "../APIReference/API_DeploymentTargets.md").

After you create the StackSet container with the
**create-stack-set** command, use one of the
following examples to deploy stacks to specific accounts.

###### Target specific accounts in

an OU

The following example deploys stacks only to accounts A1 and A2 in
OU1.

```
aws cloudformation create-stack-instances --stack-set-name `my-stackset` \
  --deployment-targets OrganizationalUnitIds=`OU1,Accounts=A1,A2,AccountFilterType=INTERSECTION` \
  --regions `us-west-2 us-east-1`
```

###### Exclude accounts from an

OU

The following example deploys stacks to all accounts in OU1 except
accounts A1 and A2.

```
aws cloudformation create-stack-instances --stack-set-name `my-stackset` \
  --deployment-targets OrganizationalUnitIds=`OU1,Accounts=A1,A2,AccountFilterType=DIFFERENCE` \
  --regions `us-west-2 us-east-1`
```
