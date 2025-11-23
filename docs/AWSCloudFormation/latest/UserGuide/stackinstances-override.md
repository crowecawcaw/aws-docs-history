# Override parameter values on stacks within

your CloudFormation StackSet

In certain cases, you might want stacks in certain Regions or accounts to have
different property values than those specified in the StackSet itself. For example, you
might want to specify a different value for a given parameter based on whether an
account is used for development or production. For these situations, CloudFormation allows
you to override parameter values in stacks by account and Region. You can override
template parameter values when you first create the stacks, and you can override
parameter values for existing stacks. You can only set parameters you've previously
overridden in stacks back to the values specified in the StackSet.

Parameter value overrides apply to stacks in the accounts and Regions you select.
During StackSet updates, any parameter values overridden for a stack aren't updated, but
retain their overridden value.

You can only override parameter _values_ that are specified in the
StackSet; to add or delete a parameter itself, you need to update the StackSet template. If you
add a parameter to a StackSet template, then before you can override that parameter value in
a stack you must first update all stacks with the new parameter and value specified in
the StackSet. Once all stacks have been updated with the new parameter, you can then
override the parameter value in individual stacks as desired.

To learn how to override StackSet parameter values when you create stacks, see [Add stacks to
StackSets](stackinstances-create.md "stackinstances-create.md").

###### Topics

- [Override parameters on stacks
  (console)](#stackinstances-override-console "#stackinstances-override-console")
- [Override parameters on stacks
  (AWS CLI)](#stackinstances-override-cli "#stackinstances-override-cli")

## Override parameters on stacks

(console)

###### To override parameters for specific stacks

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
   you created the StackSet in.
3. From the navigation pane, choose **StackSets**. On the
   StackSets page, select your StackSet.
4. With the StackSet selected, choose **Override StackSet
   parameters** from the **Actions** menu.
5. On the **Set deployment options** page, provide the
   accounts and Regions for the stacks that you'll create overrides for.

By default, CloudFormation will deploy stacks in the specified accounts within
the first Region, then moves on to the next, and so on, provided that a
Region's deployment failures don't exceed a specified failure
tolerance.

    1. [Self-managed permissions] For **Deployment
     locations**, choose **Deploy stacks in
     accounts**. Paste some or all the target account IDs
     that you used to create your StackSet.


    [Service-managed permissions] Do one of the following:




    	* Choose **Deploy to organizational units
    	 (OUs)**. Enter one or more of the target OUs
    	 that you used to create your StackSet. The overridden parameter
    	 values only apply to the accounts that are currently in the
    	 target OUs and their child OUs. Accounts added to the target
    	 OUs and their child OUs in the future will use the StackSet
    	 default values and not the overridden values.
    	* Choose **Deploy to accounts**. Paste some
    	 or all the target OU IDs or account IDs that you used to
    	 create your StackSet.
    2. For **Specify regions**, add one or more of the
     Regions into which you have deployed stacks for this StackSet.


    If you add multiple Regions, the order of the Regions under
     **Specify regions** determines their deployment
     order.
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
    4. Choose **Next**.

6. On the **Specify Overrides** page, select the checkboxes
   for the parameters to override, and then choose **Override StackSet
   value** from the **Edit override value**
   menu.
7. On the **Override StackSet parameter values** page, make
   your changes and then choose **Save changes**.

###### Note

To set any overridden parameters back to using the value specified in
the StackSet, check all parameters and choose **Set to StackSet
value** from the **Edit override value**
menu. Doing so removes all overridden values once you update the
stacks. 8. On the **Review** page, review your choices. To make
changes, choose **Edit** on the related section. 9. When you're ready to proceed, choose **Submit**.

CloudFormation starts updating your stacks. View the progress and status of
the stacks in the StackSet details page that opens when you choose
**Submit**.

## Override parameters on stacks

(AWS CLI)

###### Note

When acting as a delegated administrator, you must include `--call-as
 DELEGATED_ADMIN` in the command.

###### To override parameters for specific stacks

1. Use the [update-stack-instances](../../../cli/latest/reference/cloudformation/update-stack-instances.md "../../../cli/latest/reference/cloudformation/update-stack-instances.md") AWS CLI command and
   specify the `--parameter-overrides` option.

[Self-managed permissions] For the `--accounts` option, provide
the account IDs for which you want to override parameter values on
stacks.

```
aws cloudformation update-stack-instances --stack-set-name `my-stackset` \
  --parameter-overrides `ParameterKey=Subnets,ParameterValue=subnet-1baa3351\\,subnet-27b86940` \
  --accounts `account_id` --regions `us-east-1`
```

[Service-managed permissions] For the `--deployment-targets`
option, provide the organization root ID, OU IDs, or AWS Organizations account IDs
for which you want to override parameters on stacks. In this example, we
override parameter values for stacks in all accounts in the OU with the
`ou-rcuk-1x5j1lwo` ID.

The overridden parameter values only apply to the accounts that are
currently in the target OU and its child OUs. Accounts added to the target
OU and its child OUs in the future will use the StackSet default values and not
the overridden values.

```
aws cloudformation update-stack-instances --stack-set-name `my-stackset` \
  --parameter-overrides `ParameterKey=Subnets,ParameterValue=subnet-1baa3351\\,subnet-27b86940` \
  --deployment-targets OrganizationalUnitIds=`ou-rcuk-1x5j1lwo` \
  --regions `us-east-1`
```

2. Verify that your parameter values were successfully overridden on stacks
   by running the **describe-stack-set-operation** command to
   show the status and results of your update operation. For
   `--operation-id`, use the operation ID that was returned by
   your **update-stack-instances** command.

```
aws cloudformation describe-stack-set-operation --operation-id `operation_ID`
```
