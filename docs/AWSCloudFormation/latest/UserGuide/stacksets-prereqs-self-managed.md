# Grant self-managed permissions

This topic provides instructions on how to create the IAM service roles required by
 StackSets to deploy across accounts and AWS Regions with
 *self-managed* permissions. These roles are necessary to
 establish a trusted relationship between the account you're administering the StackSet from
 and the account you're deploying stack instances to. Using this permissions model,
 StackSets can deploy to any AWS account in which you have permissions to create an
 IAM role. 

To use *service-managed* permissions, see [Activate trusted
 access](stacksets-orgs-activate-trusted-access.md "stacksets-orgs-activate-trusted-access.md") instead.

###### Topics

* [Self-managed permissions
 overview](#prereqs-self-managed-permissions "#prereqs-self-managed-permissions")
* [Give all users of the administrator
 account permissions to manage stacks in all target accounts](#stacksets-prereqs-accountsetup "#stacksets-prereqs-accountsetup")
* [Set up advanced permissions
 options for StackSet operations](#stacksets-prereqs-advanced-perms "#stacksets-prereqs-advanced-perms")
* [Set up global keys to mitigate confused
 deputy problems](#confused-deputy-mitigation "#confused-deputy-mitigation")

## Self-managed permissions
 overview


Before you create a StackSet with self-managed permissions, you must have created
 IAM service roles in each account.


The basic steps are:



1. Determine which AWS account is the *administrator
 account*.


StackSets are created in this administrator account. A
 *target account* is the account in which you create
 individual stacks that belong to a StackSet.
2. Determine how you want to structure permissions for the StackSet.


The simplest (and most permissive) permissions configuration is where you
 give *all* users and groups in the administrator account
 the ability to create and update *all* the StackSets
 managed through that account. If you need finer-grained control, you can set
 up permissions to specify:




	* Which users and groups can perform StackSet operations in which target
	 accounts.
	* Which resources users and groups can include in their
	 StackSets.
	* Which StackSet operations specific users and groups can
	 perform.
3. Create the necessary IAM service roles in your administrator and target
 accounts to define the permissions you want. 


Specifically, the two required roles are:




	* **AWSCloudFormationStackSetAdministrationRole**
	 – This role is deployed to the administrator account.
	* **AWSCloudFormationStackSetExecutionRole**
	 – This role is deployed to all accounts where you create
	 stack instances.

## Give all users of the administrator
 account permissions to manage stacks in all target accounts


This section shows you how to set up permissions to allow all users and groups of
 the administrator account to perform StackSet operations in all target accounts. It
 guides you through creating the required IAM service roles in your administrator
 and target accounts. Anyone in the administrator account can then create, update, or
 delete any stacks across any of the target accounts. 


By structuring permissions in this manner, users don't pass an administration role
 when creating or updating a StackSet.



![Any user in the administrator account can then create any StackSet in target accounts after setting up a trust relationship.](images/stacksets_perms_master_target.png)


Administrator account
In the administrator account, create an IAM role named
 **AWSCloudFormationStackSetAdministrationRole**.
 


You can do this by creating a stack from the CloudFormation template
 available from [https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetAdministrationRole.yml](https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetAdministrationRole.yml "https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetAdministrationRole.yml"). 


###### Example permissions policy

The administration role created by the preceding template includes
 the following permissions policy. 






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWSCloudFormationStackSetExecutionRole"
 ],
 "Effect": "Allow"
 }
 ]
}`

```



###### Example trust policy 1

The preceding template also includes the following trust policy
 that grants the service permission to use the administration role
 and the permissions attached to the role.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```



###### Example trust policy 2

To deploy stack instances into a target account that resides in a
 Region that's disabled by default, you must also
 include the regional service principal for that Region. Each
 Region that's disabled by default will have its own
 regional service principal.

The following example trust policy grants the service permission
 to use the administration role in the Asia Pacific (Hong Kong) Region
 (`ap-east-1`), a Region that's
 disabled by default. 






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "cloudformation.amazonaws.com",
 "`cloudformation.ap-east-1.amazonaws.com`"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```


For more information, see [Prepare to perform StackSet operations in
 AWS Regions that are disabled by default](stacksets-opt-in-regions.md "stacksets-opt-in-regions.md"). For a list of Region
 codes, see [Regional
 endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints "https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints") in the *AWS General Reference
 Guide*.



Target accounts
In each target account, create a service role named
 **AWSCloudFormationStackSetExecutionRole** that
 trusts the administrator account. The role must have this exact name.
 You can do this by creating a stack from the CloudFormation template
 available from [https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetExecutionRole.yml](https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetExecutionRole.yml "https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetExecutionRole.yml").
 When you use this template, you are prompted to provide the account ID
 of the administrator account with which your target account must have a
 trust relationship.


###### Important

Be aware that this template grants administrator access. After you
 use the template to create a target account execution role, you must
 scope the permissions in the policy statement to the types of
 resources that you are creating by using StackSets.


The target account service role requires permissions to perform any
 operations that are specified in your CloudFormation template. For example,
 if your template is creating an S3 bucket, then you need permissions to
 create new objects for S3. Your target account always needs full
 CloudFormation permissions, which include permissions to create, update,
 delete, and describe stacks. 


###### Example permissions policy 1

The role created by this template enables the following policy on
 a target account.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "*",
 "Resource": "*"
 }
 ]
}`

```



###### Example permissions policy 2

The following example shows a policy statement with the
 *minimum* permissions for StackSets to work.
 To create stacks in target accounts that use resources from services
 other than CloudFormation, you must add those service actions and
 resources to the
 **AWSCloudFormationStackSetExecutionRole**
 policy statement for each target account.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:*"
 ],
 "Resource": "*"
 }
 ]
}`

```



###### Example trust policy

The following trust relationship is created by the template. The
 administrator account's ID is shown as
 `admin_account_id`.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```


You can configure the trust relationship of an existing target
 account execution role to trust a specific role in the administrator
 account. If you delete the role in the administrator account, and
 create a new one to replace it, you must configure your target
 account trust relationships with the new administrator account role,
 represented by `admin_account_id` in the
 preceding example.




## Set up advanced permissions
 options for StackSet operations


If you require finer-grained control over the StackSets that users and groups
 are creating through a single administrator account, you can use IAM roles to
 specify:



* Which users and groups can perform StackSet operations in which target
 accounts.
* Which resources users and groups can include in their
 StackSets.
* Which StackSet operations specific users and groups can perform.

### Control which users can perform
 StackSet operations in specific target accounts


Use customized administration roles to control which users and groups can
 perform StackSet operations in which target accounts. You might want to control
 which users of the administrator account can perform StackSet operations in which
 target accounts. To do this, you create a trust relationship between each target
 account and a specific customized administration role, rather than creating the
 **AWSCloudFormationStackSetAdministrationRole** service
 role in the administrator account itself. You then activate specific users and
 groups to use the customized administration role when performing StackSet operations
 in a specific target account.


For example, you can create Role A and Role B within your administrator
 account. You can give Role A permissions to access target account 1 through
 account 8. You can give Role B permissions to access target account 9 through
 account 16.



![A trust relationship between a customized administration role and target accounts that allows users to create a StackSet.](images/stacksets_perms_admin_target.png)

Setting up the necessary permissions involves defining a customized
 administration role, creating a service role for the target account, and
 granting users permission to pass the customized administration role when
 performing StackSet operations.


In general, here's how it works once you have the necessary permissions in
 place: When creating a StackSet, the user must specify a customized administration
 role. The user must have permission to pass the role to CloudFormation. In addition,
 the customized administration role must have a trust relationship with the
 target accounts specified for the StackSet. CloudFormation creates the StackSet and
 associates the customized administration role with it. When updating a StackSet, the
 user must explicitly specify a customized administration role, even if it's the
 same customized administration role used with this StackSet previously. CloudFormation
 uses that role to update the stack, subject to the requirements above.



Administrator account
###### Example permissions policy

For each StackSet, create a customized administration role with
 permissions to assume the target account execution role. 

The target account execution role name must be the same in
 every target account. If the role name is
 **AWSCloudFormationStackSetExecutionRole**,
 StackSets uses it automatically when creating a StackSet. If you
 specify a custom role name, users must provide the execution
 role name when creating a StackSet.

Create an [IAM
 service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html") with a custom name and the following
 permissions policy. In the examples below,
 `custom_execution_role` refers to
 the execution role in the target accounts. 






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`custom_execution_role`"
 ],
 "Effect": "Allow"
 }
 ]
}`

```


To specify multiple accounts in a single statement, separate
 them with commas.


```
"Resource": [
  "arn:aws:iam::`target_account_id_1`:role/`custom_execution_role`", 
  "arn:aws:iam::`target_account_id_2`:role/`custom_execution_role`"
]
```
You can specify all target accounts by using a wildcard (\*)
 instead of an account ID.


```
"Resource": [
  "arn:aws:iam::`*`:role/`custom_execution_role`"
]
```

###### Example trust policy 1

You must provide a trust policy for the service role to
 defines which IAM principals can assume the role.






```
`{ 
 "Version":"2012-10-17", 
 "Statement": [ 
 { 
 "Effect": "Allow", 
 "Principal": { 
 "Service": "cloudformation.amazonaws.com" 
 }, 
 "Action": "sts:AssumeRole" 
 } 
 ] 
}`

```



###### Example trust policy 2

To deploy stack instances into a target account that resides
 in a Region that's disabled by default, you must
 also include the regional service principal for that Region.
 Each Region that's disabled by default will have its own
 regional service principal.

The following example trust policy grants the service
 permission to use the administration role in the Asia Pacific (Hong Kong) Region
 (`ap-east-1`), a Region that's
 disabled by default. 






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "cloudformation.amazonaws.com",
 "`cloudformation.ap-east-1.amazonaws.com`"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```


For more information, see [Prepare to perform StackSet operations in
 AWS Regions that are disabled by default](stacksets-opt-in-regions.md "stacksets-opt-in-regions.md"). For a list of Region
 codes, see [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints "https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints") in the *AWS General
 Reference Guide*.


###### Example pass role policy

You also need an IAM permissions policy for your IAM users
 that allows the user to pass the customized administration role
 when performing StackSet operations. For more information, see
 [Granting a user permissions to pass a role to an AWS
 service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html").

In the example below,
 `customized_admin_role` refers to
 the administration role the user needs to pass.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/`customized_admin_role`"
 }
 ]
}`

```




Target accounts
In each target account, create a service role that trusts the
 customized administration role you want to use with this account. 


The target account role requires permissions to perform any
 operations that are specified in your CloudFormation template. For
 example, if your template is creating an S3 bucket, then you need
 permissions to create new objects in S3. Your target account always
 needs full CloudFormation permissions, which include permissions to
 create, update, delete, and describe stacks.


The target account role name must be the same in every target
 account. If the role name is
 **AWSCloudFormationStackSetExecutionRole**,
 StackSets uses it automatically when creating a StackSet. If you specify
 a custom role name, users must provide the execution role name when
 creating a StackSet.


###### Example permissions policy

The following example shows a policy statement with the
 *minimum* permissions for StackSets to
 work. To create stacks in target accounts that use resources
 from services other than CloudFormation, you must add those service
 actions and resources to the permissions policy.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:*"
 ],
 "Resource": "*"
 }
 ]
}`

```



###### Example trust policy

You must provide the following trust policy when you create
 the role to define the trust relationship.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`customized_admin_role`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```





### Control the resources that
 users can include in specific StackSets


Use customized execution roles to control which stack resources users and
 groups can include in their StackSets. For example, you might want to set up
 a group that can only include Amazon S3-related resources in the StackSets they
 create, while another team can only include DynamoDB resources. To do this, you
 create a trust relationship between the customized administration role for each
 group and a customized execution role for each set of resources. The customized
 execution role defines which stack resources can be included in StackSets.
 The customized administration role resides in the administrator account, while
 the customized execution role resides in each target account in which you want
 to create StackSets using the defined resources. You then activate specific
 users and groups to use the customized administration role when performing
 StackSets operations.


For example you can create customized administration roles A, B, and C in the
 administrator account. Users and groups with permission to use Role A can create
 StackSets containing the stack resources specifically listed in customized
 execution role X, but not those in roles Y or Z, or resource not included in any
 execution role.



![A trust relationship between a custom admin role and custom execution role in target accounts, allowing users to create a StackSet.](images/stacksets_perms_admin_execution.png)

When updating a StackSet, the user must explicitly specify a customized
 administration role, even if it's the same customized administration role used
 with this StackSet previously. CloudFormation performs the update using the customized
 administration role specified, so long as the user has permissions to perform
 operations on that StackSet.


Similarly, the user can also specify a customized execution role. If they
 specify a customized execution role, CloudFormation uses that role to update the
 stack, subject to the requirements above. If the user doesn't specify a
 customized execution role, CloudFormation performs the update using the customized
 execution role previously associated with the StackSet, so long as the user has
 permissions to perform operations on that StackSet.



Administrator account
Create a customized administration role in your administrator
 account, as detailed in [Control which users can perform
 StackSet operations in specific target accounts](#stacksets-prereqs-multiadmin "#stacksets-prereqs-multiadmin"). Include a trust
 relationship between the customized administration role and the
 customized execution roles that you want it to use.


###### Example permissions policy

The following example is a permissions policy for both the
 **AWSCloudFormationStackSetExecutionRole**
 defined for the target account, in addition to a customized
 execution role.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Stmt1487980684000",
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole" 
 ],
 "Resource": [ 
 "arn:aws:iam::*:role/AWSCloudFormationStackSetExecutionRole",
 "arn:aws:iam::*:role/`custom_execution_role`" 
 ]
 } 
 ]
}`

```




Target accounts
In the target accounts in which you want to create your
 StackSets, create a customized execution role that grants
 permissions to the services and resources that you want users and
 groups to be able to include in the StackSets.


###### Example permissions policy

The following example provides the minimum permissions for
 StackSets, along with permission to create Amazon DynamoDB
 tables.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamoDb:createTable"
 ],
 "Resource": "*"
 }
 ]
}`

```



###### Example trust policy

You must provide the following trust policy when you create
 the role to define the trust relationship.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`customized_admin_role`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```





### Set up permissions for specific
 StackSet operations


In addition, you can set up permissions for which user and groups can perform
 specific StackSet operations, such as creating, updating, or deleting StackSets
 or stack instances. For more information, see [Actions, resources, and condition keys for CloudFormation](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudformation.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudformation.html") in the
 *Service Authorization Reference*.


## Set up global keys to mitigate confused
 deputy problems


The confused deputy problem is a security issue where an entity that doesn't have
 permission to perform an action can coerce a more-privileged entity to perform the
 action. In AWS, cross-service impersonation can result in the confused deputy
 problem. Cross-service impersonation can occur when one service (the
 *calling service*) calls another service (the
 *called service*). The calling service can be manipulated to
 use its permissions to act on another customer's resources in a way it shouldn't
 otherwise have permission to access. To prevent this, AWS provides tools that help
 you protect your data for all services with service principals that have been given
 access to resources in your account.


We recommend using the [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn") and [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount") global condition context keys in
 resource policies to limit the permissions that AWS CloudFormation StackSets gives another service to the
 resource. If you use both global condition context keys, the
 `aws:SourceAccount` value and the account in the
 `aws:SourceArn` value must use the same account ID when used in the
 same policy statement.


The most effective way to protect against the confused deputy problem is to use
 the `aws:SourceArn` global condition context key with the full ARN of the
 resource. If you don't know the full ARN of the resource or if you are specifying
 multiple resources, use the `aws:SourceArn` global context condition key
 with wildcards (`*`) for the unknown portions of the ARN. For example,
 `arn:aws:`cloudformation`::`123456789012`:*`.
 Whenever possible, use `aws:SourceArn`, because it's more specific. Use
 `aws:SourceAccount` only when you can't determine the correct ARN or
 ARN pattern.


When StackSets assumes the **Administration** role in your
 **administrator** account, StackSets populates your
 **administrator** account ID and StackSets Amazon Resource
 Name (ARN). Therefore, you can define conditions for [global keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount")
`aws:SourceAccount` and `aws:SourceArn` in the trust
 relationships to prevent [confused deputy
 problems](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html"). The following example shows how you can use the
 `aws:SourceArn` and `aws:SourceAccount` global condition
 context keys in StackSets to prevent the confused deputy problem.



Administrator account
###### Example Global keys for
 `aws:SourceAccount` and
 `aws:SourceArn`

When using StackSets, define the global keys
 `aws:SourceAccount` and `aws:SourceArn` in
 your
 **AWSCloudFormationStackSetAdministrationRole**
 trust policy to prevent confused deputy problems.






```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:cloudformation:*:`111122223333`:stackset/*"
 }
 }
 }
 ]
}`

```



###### Example StackSets
 ARNs

Specify your associated StackSets ARNs for finer
 control.

JSONJSON




```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`",
 "aws:SourceArn": [
 "arn:aws:cloudformation:`STACKSETS-REGION`:`111122223333`:stackset/`STACK-SET-ID-1`",
 "arn:aws:cloudformation:`STACKSETS-REGION`:`111122223333`:stackset/`STACK-SET-ID-2`"
 ]
 }
 }
 }
 ]
}`

```
