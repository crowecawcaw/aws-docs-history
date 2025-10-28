# Update AWS CloudFormation StackSets

You can update your StackSet using either the CloudFormation console or the AWS CLI.

To add and remove accounts and Regions from a StackSet, see [Add stacks to
StackSets](stackinstances-create.md "stackinstances-create.md") and
[Delete stacks from
StackSets](stackinstances-delete.md "stackinstances-delete.md").
To override parameter values for a stack, see [Override parameters on
stacks](stackinstances-override.md "stackinstances-override.md").

###### Topics

- [Update your StackSet (console)](#stacksets-update-console "#stacksets-update-console")
- [Update your StackSet (AWS CLI)](#stacksets-update-cli "#stacksets-update-cli")

## Update your StackSet (console)

###### To update a StackSet

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
   you created the StackSet in.
3. From the navigation pane, choose **StackSets**.
4. On the **StackSets** page, select the StackSet you want
   to update.
5. With the StackSet selected, choose **Edit StackSet details**
   from the **Actions** menu.
6. On the **Choose a template** page, update the
   **Permissions** section as needed, or skip to the next
   step.
7. For **Prerequisite - Prepare template**, choose
   **Use current template** to use the current template,
   or **Replace current template** to specify an S3 URL to
   another template or upload a new template.
8. Choose **Next**.
9. On the **Specify StackSet details** page, for
   **StackSet description**, update the description for
   the StackSet as needed.
10. For **Parameters**, update the parameter values as
    needed.
11. Choose **Next**.
12. On the **Configure StackSet options** page, for
    **Tags**, modify the tags as needed. You can add,
    update, or delete tags. For more information about how tags are used in
    AWS, see [Organizing
    and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
    _AWS Billing and Cost Management User Guide_.
13. For **Execution configuration**, you can update the
    execution configuration as needed.

###### Note

Remember, you can't change execution settings when operations are
running or queued. 14. If your template contains IAM resources, for
**Capabilities**, choose **I acknowledge that
this template may create IAM resources** to specify that you
want to use IAM resources in the template. For more information, see [Acknowledging IAM resources in CloudFormation
templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities"). 15. Choose **Next**. 16. On the **Set deployment options** page, provide the
accounts and Regions for the update.

CloudFormation will deploy stack updates in the specified accounts within the
first Region, then moves on to the next, and so on, as long as a Region's
deployment failures don't exceed a specified failure tolerance.

    1. [Self-managed permissions] For **Accounts**,
     **Deployment locations**, choose
     **Deploy stacks in accounts**. Paste the target
     account IDs that you used to create your StackSet in the text box,
     separating multiple numbers with commas.


    [Service-managed permissions] Do one of the following:




    	* Choose **Deploy to organizational units
    	 (OUs)**. Enter the target OUs that you used to
    	 create your StackSet.
    	* Choose **Deploy to accounts**. Paste the
    	 target OU IDs or account IDs that you used to create your
    	 StackSet.
    2. For **Specify regions**, specify the order in
     which you want CloudFormation to deploy your updates.
    3. For **Deployment options**, do the
     following:




    	* For **Maximum concurrent accounts**,
    	 specify how many accounts are processed concurrently.
    	* For **Failure tolerance**, specify the
    	 maximum number of account failures allowed per Region. The
    	 operation will stop and won't proceed to other Regions once
    	 this limit is reached.
    	* For **Region concurrency**, choose how to
    	 process Regions: **Sequential** (one Region
    	 at a time) or **Parallel** (multiple
    	 Regions concurrently).
    	* For **Concurrency mode**, choose how
    	 concurrency behaves during operation execution.




    		+ **Strict failure tolerance**
    		 – Reduces account concurrency level when
    		 failures occur, staying within **Failure
    		 tolerance** +1.
    		+ **Soft failure tolerance**
    		 – Maintains your specified concurrency level
    		 (the value of **Maximum concurrent
    		 accounts**) regardless of failures.
    4. Choose **Next** to continue.

17. On the **Review** page, review your choices. To make
    changes, choose **Edit** on the related section.
18. When you're ready to proceed, choose **Submit**.

CloudFormation starts applying your updates to your StackSet, and displays the
**Operations** tab of the StackSet details page. You can
view the progress and status of update operations on the
**Operations** tab.

## Update your StackSet (AWS CLI)

###### Note

When acting as a delegated administrator, you must include `--call-as
 DELEGATED_ADMIN` in the command.

1. ###### To update a StackSet

Use the [update-stack-set](../../../cli/latest/reference/cloudformation/update-stack-set.md "../../../cli/latest/reference/cloudformation/update-stack-set.md") command to make changes to
your StackSet.

In the following examples, we're updating the StackSet by using
`--parameters` option. Specifically, we change the default
snapshot delivery frequency for delivery channel configuration from
`TwentyFour_Hours` to `Twelve_Hours`. Because
we're still using the current template, we add the
`--use-previous-template` option.

Set concurrent account processing and other deployment preferences using
the `--operation-preferences` option. These examples use
count-based settings. Note that `MaxConcurrentCount` must not
exceed `FailureToleranceCount` + 1. For percentage-based
settings, use `FailureTolerancePercentage` or
`MaxConcurrentPercentage` instead.

[Self-managed permissions] For the `--accounts` option, provide
the account IDs you want your update to target.

```
aws cloudformation update-stack-set --stack-set-name `my-stackset` \
  --use-previous-template \
  --parameters `ParameterKey=MaximumExecutionFrequency,ParameterValue=Twelve_Hours` \
  --accounts `account_ID_1 account_ID_2` \
  --regions `us-west-2 us-east-1` \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

[Service-managed permissions] For the `--deployment-targets`
option, provide the organization root ID or organizational unit (OU) IDs you
want your update to target.

```
aws cloudformation update-stack-set --stack-set-name `my-stackset` \
  --use-previous-template \
  --parameters `ParameterKey=MaximumExecutionFrequency,ParameterValue=Twelve_Hours` \
  --deployment-targets OrganizationalUnitIds=`ou-rcuk-1x5j1lwo,ou-rcuk-slr5lh0a` \
  --regions `us-west-2 us-east-1` \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

For more information, see [UpdateStackSet](../APIReference/API_UpdateStackSet.md "../APIReference/API_UpdateStackSet.md") in the
_AWS CloudFormation API Reference_. 2. Verify that your StackSet was updated successfully by running the
**describe-stack-set-operation** command to show the
status and results of your update operation. For
`--operation-id`, use the operation ID that was returned by your
**update-stack-set** command.

```
aws cloudformation describe-stack-set-operation \
  --operation-id `operation_ID`
```
