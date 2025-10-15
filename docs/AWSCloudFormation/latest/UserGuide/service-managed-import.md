# Service-managed stack import for AWS CloudFormation StackSets

The CloudFormation stack import operation can import existing stacks into new or existing StackSets,
 so that you can migrate existing stacks to a StackSet in one operation. StackSets extends the
 functionality of stacks, so you can create, update, or delete stacks across multiple accounts and
 Regions with a single operation.


###### Considerations for service-managed stack imports


* The stack import operation requires a management account or delegated admin account in
 which you can manage the associated AWS Organizations such as enabling trust access with
 StackSets.
* The target accounts must be members of the AWS Organizations managed by the management account or
 delegated admin account.
* Target stack exists in one of the target OUs.
* The target account should be a member of AWS Organizations.
* AWS Organizations access should be in the `ACTIVATED` state for the Organizations.
* Stacks being imported should be present in any of the member accounts, and not the
 management account.
###### Topics

* [Import a service-managed stack
 into a new StackSet (console)](#import-service-managed-stack-to-new-stackset "#import-service-managed-stack-to-new-stackset")
* [Create and import a
 service-managed stack into an existing StackSet (console)](#import-service-managed-stack-to-existing-stackset "#import-service-managed-stack-to-existing-stackset")
* [Import a
 service-managed stack into an existing StackSet (console)](#import-service-managed-stack-to-existing-stackset-console "#import-service-managed-stack-to-existing-stackset-console")
* [Importing a service-managed stack
 into a StackSet (AWS CLI)](#import-service-managed-stack-to-stackset.cli "#import-service-managed-stack-to-stackset.cli")

## Import a service-managed stack
 into a new StackSet (console)


Import a stack into a new StackSet using the AWS Management Console


To import a new stack into a StackSet, identify a stack that contains the resource you
 want to import.


1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the navigation pane, choose **StackSets**.
3. At the top of the **StackSets** page, choose **Create
 StackSet**.
4. On the **Choose a template** page, do the following:


	1. For **StackSet permission model** choose **Service-managed
	 permissions**.
	2. For **Prerequisite - Prepare template**, choose **Template is
	 ready**, and choose your template by using one of the following options:
	
	
	
	
		* For **Amazon S3 URL**, enter your Amazon S3 URL in the **Amazon S3
		 URL** field.
		* For **Upload a template file**, choose a CloudFormation template on your
		 local computer.Accept your settings and choose **Next**.
5. On the **Specify StackSet details** page, do the following:


	1. Enter a StackSet name in the **StackSet name** box.
	2. (Optional) Enter a description in the **StackSet description**
	 section.On the **Configure StackSet options** page, review your choices and
 choose **Next**.
6. On the **Set deployment options** page, do the following:


	1. For **Add stacks to stack set**, choose **Import stacks to
	 stack set**.
	2. For **Stacks to import**, choose your stack import method.
	
	
		1. For **Stack ID** enter your stack ID.
		2. For **Stack URL** enter the Amazon S3 URL.
7. Under **Associate organizational units**, do the
 following:


	1. Choose **Associate with organization** to use root OU.
	2. Choose **Associate with organizational units (OUs)** to enter parent
	 OU IDs for the stacks to import. For example, if `Stack 1` and `Stack
	 2` are under `OU1`, and `Stack 3` is under `OU2`,
	 enter `OU1` and `OU2`.Accept your settings and choose **Next**.
8. Review your settings on the **Review** page and choose
 **Submit**.

## Create and import a
 service-managed stack into an existing StackSet (console)


To import an existing stack into a new StackSet, identify a stack that contains the
 resource you want to import.


###### To create a StackSet and import a stack

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the navigation pane, choose **StackSets**.
3. At the top of the **StackSets** page, choose **Create
 StackSet**.
4. On the **Choose a template** page, do the following:


	1. For **StackSet permission model** choose **Service-managed
	 permissions**.
	2. For **Prerequisite - Prepare template**, choose **Template is
	 ready**, and choose your template by using one of the following options:
	
	
	
	
		* For **Amazon S3 URL**, enter your Amazon S3 URL in the **Amazon S3
		 URL** field.
		* For **Upload a template file**, choose a CloudFormation template on your
		 local computer.Accept your settings and choose **Next**.
5. On the **Specify StackSet details** page, do the following:


	1. Enter a StackSet name in the **StackSet name** box.
	2. (Optional) Enter a description in the **StackSet description**
	 section.On the **Configure StackSet options** page, review your choices and
 choose **Next**.
6. On the **Set deployment options** page, do the following:


	1. For **Add stacks to stack set**, choose **Deploy new
	 stacks**.
7. For the **Associate organizational units** section, do the
 following:


	1. Choose **Associate with organization** to use root OU.
	2. Choose **Associate with organizational units (OUs)** to enter parent
	 OU IDs for the stacks to import. For example, if `Stack 1` and `Stack
	 2` are under `OU1`, and `Stack 3` is under `OU2`,
	 enter `OU1` and `OU2`.
8. For **Specify regions** and **Deployment options**,
 review your choices.


Accept your settings and choose **Next**.
9. Review your settings on the **Review** page and choose
 **Submit**.

## Import a
 service-managed stack into an existing StackSet (console)


Choose your StackSet and identify the stack you want to import.


###### To import
 a stack to an existing StackSet

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the navigation pane, choose **StackSets**.
3. Choose the StackSet you want to import a stack to, and then choose **Add stacks
 to StackSet** from the **Actions** drop-down.
4. On the **Set deployment options** page, do the following:


	1. For **Add stacks to stack set**, choose **Import stacks to
	 stack set**.
	2. Under **Stacks to import**, do the following
	
	
		1. For **Stack ID**, enter your stack ID.
		2. For **Stack URL**, enter the Amazon S3 URL.
	3. Under **Associate organizational units**, do the following:
	
	
		1. Choose **Associate with organization** to use root OU.
		2. Choose **Associate with organizational units (OUs)** to enter parent
		 OU IDs for the stacks to import. For example, if `Stack 1` and `Stack
		 2` are under `OU1`, and `Stack 3` is under `OU2`,
		 enter `OU1` and `OU2`.Accept your settings and choose **Next**.
5. Review the **Specify overrides** page and choose
 **Next**.
6. Confirm and review the **Review** page and choose
 **Submit**.

## Importing a service-managed stack
 into a StackSet (AWS CLI)


Once a StackSet is created, you can import your stacks by passing the stack ID's of the
 stacks being imported. You may also pass the OU ID list to which you want to map it to.


CloudFormation will import user provided stacks within those OUs and use those OUs as
 deployment targets for the StackSet. Stack IDs presented in the input will map to the nearest
 OU in OU ID list input internally. If a stack doesn't belong to an existing OU ID in the input
 list, then the AWS CLI will return the `StackNotFoundException` error.


The `import-stacks-to-stack-set` operation creates stack instances for the
 stacks in the OU ID input. The following AWS CLI examples use the
 `import-stacks-to-stack-set` operation to import a stack into a StackSet.



* To use the `import-stacks-to-stack-sets` operation, specify
 `stack-ids` or `stack-ids-url` you want to import to your stack
 set.



```
aws cloudformation import-stacks-to-stack-set \
  --stack-set-name `ServiceMangedStackSet` \
  --stack-ids "`arn:123456789012:us-east-1:Stack1`" \
  --organizational-unit-ids `ou-examplerootid111-exampleouid111`
```


```
aws cloudformation import-stacks-to-stack-set \
  --stack-set-name `ServiceMangedStackSet` \
  --stack-ids-url `https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/file-name.json` \
  --organizational-unit-ids `ou-examplerootid111-exampleouid111`
```

###### Note

The `import-stacks-to-stack-sets` operation, requires you to specify at least
 one organizational unit ID (OU ID) so that it can associate the stack being imported to that
 particular OU. This operation doesn't create stack instances for other member accounts in the
 associated OUs. To update member accounts for the associated OUs, use
 `create-stack-instances` or `update-stack-instances`.


`create-stack-set` creates stack instances for all the accounts under the OUs
 with a user provided template, either from direct upload or Amazon S3. The following AWS CLI examples
 use the `create-stack-set` operation to import a stack into a new StackSet.



* To use the `create-stack-set` operation, specify your StackSet name and
 import a stack to a newly created StackSet.



```
aws cloudformation create-stack-set \
  --template-url `https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/file-name.json` \
  --permission-model SERVICE_MANAGED \
  --auto-deployment Enabled=true
```
