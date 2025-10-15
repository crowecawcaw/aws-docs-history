# Delete stacks from AWS CloudFormation StackSets

You can delete stacks from StackSets using either the CloudFormation console or the
 AWS CLI. 

###### Topics

* [Delete stacks from your StackSet
 (console)](#stackinstances-delete-console "#stackinstances-delete-console")
* [Delete stacks from your StackSet
 (AWS CLI)](#stackinstances-delete-cli "#stackinstances-delete-cli")
###### Note

Deleting stacks from a top-level organizational unit (OU) removes that OU as a
 StackSet target.


## Delete stacks from your StackSet
 (console)


###### To delete stacks

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
 you created the StackSet in.
3. From the navigation pane, choose **StackSets**. On the
 StackSets page, select the StackSet.
4. With your StackSet selected, choose **Delete stacks from
 StackSet** from the **Actions** menu.
5. On the **Set deployment options** page, first choose the
 accounts and Regions where you want to delete the stacks.


	1. [Self-managed permissions] For **Accounts**,
	 choose **Deploy stacks in accounts** or
	 **Deploy stacks in organizational
	 units**.
	
	
	If you choose **Deploy stacks in accounts**,
	 paste your target account numbers in the **Account
	 numbers** text box, separating multiple numbers with
	 commas.
	
	
	If you choose **Deploy stacks in organizational
	 units**, paste a target OU ID in the
	 **Organization numbers** text box to target all
	 accounts that are part of the specified organization.
	2. [Service-managed permissions] For **Organizational units
	 (OUs)**, specify the target OU IDs. 
	
	
	###### Important
	
	CloudFormation will delete stacks from both the specified target
	 OUs and their child OUs.
	
	
	For **Account filter type**, you can refine which
	 accounts will have stacks deleted by choosing one of the following
	 options and providing account numbers. 
	
	
	
	
		* **None** (default) – Delete stacks
		 from all accounts in the specified OUs.
		* **Intersection** – Delete stacks
		 only from specific individual accounts within the selected
		 OUs.
		* **Difference** – Delete stacks
		 from all accounts in the selected OUs except for specific
		 accounts.
		* **Union** – Delete stacks from the
		 specified OUs plus additional individual accounts.
	3. For **Specify regions**, choose the Regions from
	 which you want to delete stacks within the target accounts.
6. For **Deployment options**, do the following:




	* For **Maximum concurrent accounts**, specify how
	 many accounts are processed concurrently.
	* For **Failure tolerance**, specify the maximum
	 number of account failures allowed per Region. The operation will
	 stop and won't proceed to other Regions once this limit is
	 reached.
	* For **Retain stacks**, enable this option to save
	 the stacks and their associated resources when removing them from
	 your StackSet. The resources stay in their current state but are no
	 longer part of the StackSet.
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
7. Choose **Next**.
8. On the **Review** page, review your choices. To make
 changes, choose **Edit** on the related section.
9. When you are ready to remove the stacks from your StackSet, choose
 **Submit**.


After stack deletion is finished, you can verify that stacks were deleted
 from your StackSet in the StackSet detail page, on the **Stack
 instances** tab.

## Delete stacks from your StackSet
 (AWS CLI)


###### Note

When acting as a delegated administrator, you must include `--call-as
 DELEGATED_ADMIN` in the command. 


Use the **delete-stack-instances** command with your StackSet
 name.


In these examples, we use the `--no-retain-stacks` option because we
 aren't retaining any stacks. Use `--retain-stacks` instead of
 `--no-retain-stacks` if you want to keep the stacks and their
 resources. 


For `--regions`, specify the AWS Regions you want to delete stacks
 from, for example, `us-west-2` and `us-east-1`.


Set concurrent account processing and other preferences using the
 `--operation-preferences` option. These examples use count-based
 settings. Note that `MaxConcurrentCount` must not exceed
 `FailureToleranceCount` + 1. For percentage-based settings, use
 `FailureTolerancePercentage` or `MaxConcurrentPercentage`
 instead. 


###### To delete stacks (self-managed permissions)


For the `--accounts` option, specify the IDs of the account to
 delete stacks from.



```
aws cloudformation delete-stack-instances --stack-set-name `my-stackset` \
  --accounts `account_ID_1 account_ID_2` \
  --regions `us-west-2 us-east-1` \
  --no-retain-stacks \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

###### To delete stacks (service-managed permissions)


For `--deployment-targets`, specify the organization root ID or
 organizational unit (OU) IDs to delete stacks from.


###### Important

CloudFormation will delete stacks from both the specified target OUs and their
 child OUs.



```
aws cloudformation delete-stack-instances --stack-set-name `my-stackset` \
  --deployment-targets OrganizationalUnitIds=`ou-rcuk-1x5jlwo,ou-rcuk-slr5lh0a` \ 
  --regions `us-west-2 us-east-1` \
  --no-retain-stacks \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

For more information, see [DeleteStackInstances](../APIReference/API_DeleteStackInstances.md "../APIReference/API_DeleteStackInstances.md") in the
 *AWS CloudFormation API Reference*.


Optionally, after stack deletion is finished, verify that stacks were deleted from
 your StackSet by running the **describe-stack-set-operation** command to
 show the status and results of the delete stacks operation. For
 `--operation-id`, use the operation ID that was returned by your
 **delete-stack-instances** command.



```
aws cloudformation describe-stack-set-operation --stack-set-name `my-stackset` \
  --operation-id `ddf16f54-ad62-4d9b-b0ab-3ed8e9example`
```
