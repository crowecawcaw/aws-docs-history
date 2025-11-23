# Enable Data Lifecycle Manager default policies across accounts and Regions

Using CloudFormation StackSets, you can enable Amazon Data Lifecycle Manager default policies across multiple accounts and
AWS Regions with a single operation.

You can use stack sets to enable default policies in one of the following ways:

- **Across an AWS organization** — Ensures that default
  policies are enabled and configured consistently across an entire AWS organization or specific
  organizational units in an organization. This is done using _service-managed permissions_.
  CloudFormation StackSets creates the required IAM roles on your behalf.
- **Across specific AWS accounts** — Ensures that default
  policies are enabled and configured consistently across specific target accounts. This requires
  _self-managed permissions_. You create the IAM roles required to establish
  the trust relationship between the stack set administrator account and the target accounts.
  For more information, see [Permission models for stack sets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md#stacksets-concepts-stackset-permission-models "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md#stacksets-concepts-stackset-permission-models") in the _AWS CloudFormation User Guide_.

Use the following procedures to enable Amazon Data Lifecycle Manager default policies across an entire AWS organization,
across specific OUs, or across specific target accounts.

###### Prerequisites

Do one of the following, depending on how you are enabling the default policies:

- (Across AWS organizations) You must [enable all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") and [activate trusted access with AWS Organizations](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.md"). You must also use the organization's management
  account or a [delegated administrator account](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.md").
- (Across specific target accounts) You must [grant self-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md") by creating the roles required to establish a
  trusted relationship between stack set administrator account and target accounts.

Console

###### To enable default policies across an AWS organization or across specific target accounts

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the navigation pane, choose **StackSets**, then choose
   **Create StackSet**.
3. For **Permissions**, do one of the following, depending on how you are enabling
   the default policies:
   - (Across an AWS organization) Choose **Service-managed permissions**.
   - (Across specific target accounts) Choose **Self-service permissions**. Then,
     for **IAM admin role ARN**, select the IAM service role that that you created
     for the administrator account, and for **IAM execution role name**, enter the
     name of the IAM service role that you created in the target accounts.

4. For **Prepare template**, choose **Use a sample template**.
5. For **Sample templates**, do one of the following:
   - (Default policy for EBS snapshots) Select **Create Amazon Data Lifecycle Manager default policies for EBS
     Snapshots.**
   - (Default policy for EBS-backed AMIs) Select **Create Amazon Data Lifecycle Manager default policies for
     EBS-backed AMIs**.

6. Choose **Next**.
7. For **StackSet name** and **StackSet description**,
   enter a descriptive name and brief description.
8. In the **Parameters** section, configure the default policy settings as
   needed.

###### Note

For critical workloads, we recommend **CreateInterval = 1 day** and
**RetainInterval = 7 days**. 9. Choose **Next**. 10. (Optional) For **Tags**, specify tags to help you identify the StackSet and
stack resources. 11. For **Managed execution**, choose **Active**. 12. Choose **Next**. 13. For **Add stacks to stack set**, choose **Deploy new stacks**. 14. Do one of the following, depending on how you are enabling the default policies:

    * (Across AWS organization) For **Deployment targets** choose one of the
     following options:




    	+ To deploy across an entire AWS organization, choose **Deploy to organization**.
    	+ To deploy to specific organizational units (OU), choose **Deploy to organizational
    	 units**, and then for **OU ID**, enter the OU ID. To add additional
    	 OUs, choose **Add another OU**.
    * (Across specific target accounts) For **Accounts**, do one of the following:




    	+ To deploy to specific target accounts, choose **Deploy stacks in accounts**,
    	 and then for **Account numbers**, enter the IDs of the target accounts.
    	+ To deploy to all accounts in a specific OU, choose **Deploy stack to all accounts in
    	 an organizational unit**, and then for **Organization numbers**, enter
    	 the ID of the target OU.

15. For **Automatic deployment**, choose **Activated**.
16. For **Account removal behavior**, choose **Retain stacks**.
17. For **Specify regions**, select specific Regions in which to enable default policies,
    or choose **Add all Regions** to enable default policies in all Regions.
18. Choose **Next**.
19. Review the stack set settings, select **I acknowledge that CloudFormation might create IAM
    resources**, and then choose **Submit**.

AWS CLI

###### To enable default policies across an AWS organization

1. Create the stack set. Use the [create-stack-set](../../../cli/latest/reference/cloudformation/create-stack-set.md "../../../cli/latest/reference/cloudformation/create-stack-set.md") command.

For `--permission-model`, specify `SERVICE_MANAGED`.

For `--template-url`, specify one of the following template URLs:

    * (Default policies for EBS-backed AMIs) `https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/DataLifecycleManagerAMIDefaultPolicy.yaml`
    * (Default policies for EBS snapshots) `https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/DataLifecycleManagerEBSSnapshotDefaultPolicy.yaml`

For `--parameters`, specify the settings for the default policies. For supported parameters,
parameter descriptions, and valid values, download the template using the URL and then view the template
using a text editor.

For `--auto-deployment`, specify `Enabled=true, RetainStacksOnAccountRemoval=true`.

```
`$` aws cloudformation create-stack-set \
--stack-set-name `stackset_name` \
--permission-model SERVICE_MANAGED \
--template-url `template_url` \
--parameters "ParameterKey=`param_name_1`,ParameterValue=`param_value_1`" "ParameterKey=`param_name_2`,ParameterValue=`param_value_2`" \
--auto-deployment "Enabled=true, RetainStacksOnAccountRemoval=true"
```

2. Deploy the stack set. Use the [create-stack-instances](../../../cli/latest/reference/cloudformation/create-stack-instances.md "../../../cli/latest/reference/cloudformation/create-stack-instances.md") command.

For `--stack-set-name`, specify the name of the stack set you created in the previous step.

For `--deployment-targets OrganizationalUnitIds`, specify the ID of the root OU to deploy
to an entire organization, or OU IDs to deploy to specific OUs in the organization.

For `--regions`, specify the AWS Regions in which to enable the default policies.

```
`$` aws cloudformation create-stack-instances \
--stack-set-name `stackset_name` \
--deployment-targets OrganizationalUnitIds=`'["root_ou_id"]'` | `'["ou_id_1", "ou_id_2]'` \
--regions '["`region_1`", "`region_2`"]'
```

###### To enable default policies across specific target accounts

1. Create the stack set. Use the [create-stack-set](../../../cli/latest/reference/cloudformation/create-stack-set.md "../../../cli/latest/reference/cloudformation/create-stack-set.md") command.

For `--template-url`, specify one of the following template URLs:

    * (Default policies for EBS-backed AMIs) `https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/DataLifecycleManagerAMIDefaultPolicy.yaml`
    * (Default policies for EBS snapshots) `https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/DataLifecycleManagerEBSSnapshotDefaultPolicy.yaml`

For `--administration-role-arn`, specify the ARN of the IAM service role that you previously
created for the stack set administrator.

For `--execution-role-name`, specify the name of IAM service role that you created in the
target accounts.

For `--parameters`, specify the settings for the default policies. For supported parameters,
parameter descriptions, and valid values, download the template using the URL and then view the template
using a text editor.

For `--auto-deployment`, specify `Enabled=true, RetainStacksOnAccountRemoval=true`.

```
`$` aws cloudformation create-stack-set \
--stack-set-name `stackset_name` \
--template-url `template_url` \
--parameters "ParameterKey=`param_name_1`,ParameterValue=`param_value_1`" "ParameterKey=`param_name_2`,ParameterValue=`param_value_2`" \
--administration-role-arn `administrator_role_arn` \
--execution-role-name `target_account_role` \
--auto-deployment "Enabled=true, RetainStacksOnAccountRemoval=true"
```

2. Deploy the stack set. Use the [create-stack-instances](../../../cli/latest/reference/cloudformation/create-stack-instances.md "../../../cli/latest/reference/cloudformation/create-stack-instances.md") command.

For `--stack-set-name`, specify the name of the stack set you created in the previous step.

For `--accounts`, specify the IDs of the target AWS accounts.

For `--regions`, specify the AWS Regions in which to enable the default policies.

```
`$` aws cloudformation create-stack-instances \
--stack-set-name `stackset_name` \
--accounts '["`account_ID_1`","`account_ID_2`"]' \
--regions '["`region_1`", "`region_2`"]'
```
