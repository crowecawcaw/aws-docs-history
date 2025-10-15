# Enable or disable automatic
 deployments for StackSets in AWS Organizations

CloudFormation can automatically deploy additional stacks to new AWS Organizations accounts when
 they're added to your target organization or organizational units (OUs). You can enable
 automatic deployments and choose whether to delete or retain stacks and their associated
 resources when accounts are removed from target OUs. These settings can be modified
 anytime for StackSets that use service-managed permissions.


## How automatic deployments
 work


When automatic deployments are enabled, they're triggered when accounts are added
 to a target organization or OU, removed from a target organization or OU, or moved
 between target OUs.


For example, consider `StackSet1` that targets `OU1` in the
 `us-east-1` Region and `StackSet2` that targets
 `OU2` in the `us-east-1` Region. `OU1` contains
 `AccountA`. 


If you move `AccountA` from `OU1` to `OU2` with
 automatic deployments enabled, CloudFormation automatically runs a delete operation to
 remove the `StackSet1` stack from `AccountA` and queues a
 create operation that adds the `StackSet2` stack to
 `AccountA`.


## Considerations


The following are considerations when using automatic deployments:



* The automatic deployments feature is enabled at the StackSet level. You can't
 adjust automatic deployments selectively for OUs, accounts, or
 Regions.
* Overridden parameter values only apply to the accounts that are currently
 in the target OUs and their child OUs. Accounts added to the target OUs and
 their child OUs in the future will use the StackSet default values and not the
 overridden values.
* If you target specific accounts and enable automatic deployments, your
 StackSet will continue to use the account level filter defined in the last
 deployment while also deploying to newly added accounts within the deployed
 organization. To prevent deployments to newly added accounts, disable
 automatic deployments.

## Enable or disable
 automatic deployments (console)


###### To enable or disable automatic deployments

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
 you created the StackSet in.
3. From the navigation pane, choose **StackSets**.
4. On the **StackSets** page, select the option next to the
 name of the StackSet to update.
5. Choose **Edit automatic deployment** from the
 **Actions** menu in the upper right corner.
6. From the dialog box that opens, do the following:


	1. For **Automatic deployment**, choose
	 **Activated** or
	 **Deactivated**.
	2. For **Account removal behavior**, choose
	 **Delete stacks** or **Retain
	 stacks**. Retained resources stay in their current
	 state, but will no longer be part of the StackSet.
7. Choose **Save**.

## Enable or disable
 automatic deployments (AWS CLI)


###### To enable or disable automatic deployments

1. Use the [update-stack-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack-set.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack-set.html") command with the
 `--auto-deployment` option.


The following command enables automatic deployments.



```
aws cloudformation update-stack-set --stack-set-name `my-stackset` \
  --use-previous-template --auto-deployment Enabled=true,RetainStacksOnAccountRemoval=`true`
```

Alternatively, to disable automatic deployments, specify
 `Enabled=false` as the value for the
 `--auto-deployment` option, as in the following example. 



```
aws cloudformation update-stack-set --stack-set-name `my-stackset` \
  --use-previous-template --auto-deployment Enabled=false
```
2. Using the operation ID that was returned as part of the
 **update-stack-set** output, run [describe-stack-set-operation](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-set-operation.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-set-operation.html") to verify that
 your StackSet was updated successfully.



```
aws cloudformation describe-stack-set-operation --operation-id `operation_ID`
```
