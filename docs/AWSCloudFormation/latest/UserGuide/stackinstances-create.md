# Add stacks to CloudFormation StackSets

When you create a StackSet, you can create the stacks for that StackSet. CloudFormation also
 enables you to add more stacks, for additional accounts and Regions, at any point after
 the StackSet is created. You can add stacks using either the CloudFormation console or the
 AWS CLI.

###### Topics

* [Add stacks to a StackSet
 (console)](#stackinstances-create-console "#stackinstances-create-console")
* [Add stacks to a StackSet (AWS CLI)](#stackinstances-create-cli "#stackinstances-create-cli")

## Add stacks to a StackSet
 (console)


###### To add stacks to a StackSet

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
 you created the StackSet in.
3. From the navigation pane, choose **StackSets**. On the
 StackSets page, select the StackSet that you created.
4. With the StackSet selected, choose **Add stacks to StackSet**
 from the **Actions** menu.
5. On the **Set deployment options** page, do the
 following:


	1. For **Add stacks to StackSet**, choose
	 **Deploy new stacks**.
	2. Next, do the following depending on your StackSet's permissions
	 configuration:
	
	
	
	
		* [Self-managed permissions] For
		 **Accounts**, **Deployment
		 locations**, choose **Deploy stacks in
		 accounts**. Paste your target account numbers
		 in the text box, separating multiple numbers with
		 commas.
		* [Service-managed permissions] For **Deployment
		 targets**, do one of the following:
		
		
		
		
			+ Choose **Deploy to organization**
			 to deploy to all accounts in your
			 organization.
			+ Choose **Deploy to organizational units
			 (OUs)** to deploy to all accounts in
			 specific OUs. Choose **Add another
			 OU**, and then paste the target OU ID in
			 the text box. Repeat for each new target OU.
			 CloudFormation also targets any child OUs of your
			 selected targets.
		###### Note
		
		If you add an OU that your StackSet already targets,
		 CloudFormation creates new stacks in any accounts in the OU
		 that don't already have stacks from your StackSet (for
		 example, accounts that were added to the OU after your
		 StackSet was created and with automatic deployments
		 disabled).
	3. For **Specify regions**, specify which
	 AWS Regions to deploy to in the target accounts you specified in
	 the previous step. By default, CloudFormation will deploy stacks in the
	 specified accounts within the first Region, then moves on to the
	 next, and so on, as long as a Region's deployment failures don't
	 exceed a specified failure tolerance.
	4. For **Deployment options**, do the
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
	5. Choose **Next**.
6. On the **Specify Overrides** page, leave the property
 values as specified. You won't be overriding any property values for the
 stacks you're going to create. Choose **Next**.
7. On the **Review** page, review your choices. To make
 changes, choose **Edit** on the related section.
8. When you're ready to proceed, choose **Submit**.


CloudFormation starts creating your stacks. View the progress and status of
 the creation of the stacks in your StackSet in the StackSet details page that opens
 when you choose **Submit**. When complete, your new stacks
 should be listed on the **Stack instances** tab.

## Add stacks to a StackSet (AWS CLI)


###### Note

When acting as a delegated administrator, you must include `--call-as
 DELEGATED_ADMIN` in the command. 


###### To add stacks to a StackSet with self-managed permissions


Use the **create-stack-instances** CLI command. For the
 `--accounts` option, provide the accounts IDs for which you want
 to create stacks.



```
aws cloudformation create-stack-instances --stack-set-name `my-stackset` \
  --accounts `account_id` --regions `eu-west-1 us-west-2`
```

###### To add stacks to a StackSet with service-managed permissions


Use the **create-stack-instances** CLI command. For the
 `--deployment-targets` option, provide the organization (root) ID
 or OU IDs for which you want to create stacks. For example commands that target
 specific accounts, see [Create a StackSet with
 service-managed permissions (AWS CLI)](stacksets-orgs-associate-stackset-with-org.md#stacksets-orgs-associate-stackset-with-org-cli "stacksets-orgs-associate-stackset-with-org.md#stacksets-orgs-associate-stackset-with-org-cli").



```
aws cloudformation create-stack-instances --stack-set-name `my-stackset` \
  --deployment-targets OrganizationalUnitIds=`ou-rcuk-r1qi0wl7` --regions `eu-west-1 us-west-2`
```

###### Note

If you add an OU that your StackSet already targets, CloudFormation creates new stacks
 in any accounts in the OU that don't already have stacks from your StackSet (for
 example, accounts that were added to the OU after your StackSet was created and with
 automatic deployments disabled).
