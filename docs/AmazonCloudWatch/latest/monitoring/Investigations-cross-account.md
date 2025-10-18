# Cross-account investigations

 Cross-account CloudWatch investigations enables you to investigate application issues that span multiple
 AWS accounts from a centralized monitoring account. This feature allows you to
 correlate telemetry data, metrics, and logs across up to 25 accounts, in addition to the
 monitoring account, to gain comprehensive visibility into distributed applications and
 troubleshoot complex multi-account scenarios. 

###### Topics

* [Prerequisites](#Investigations-cross-account-prereq "#Investigations-cross-account-prereq")
* [Setup your
 monitoring account for cross-account access](#Investigations-cross-account-monitoring-account "#Investigations-cross-account-monitoring-account")
* [Setup your source
 account(s) for cross-account access](#Investigations-cross-account-source-account "#Investigations-cross-account-source-account")
* [Investigating
 multi-account issues](#Investigations-cross-account-investigation "#Investigations-cross-account-investigation")

## Prerequisites



* Multi-account investigation requires you to already have cross-account
 observability set up in order to view cross-account telemetries. To complete
 the prerequisite, set up either [cross-account observability](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-monitoring-by-using-amazon-cloudwatch-observability-access-manager.html "https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-monitoring-by-using-amazon-cloudwatch-observability-access-manager.html") or the [cross-account dashboard](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md").
* Setup an investigation group. For cross-account observability, this should
 be in the monitoring account. You can also set them up in the source
 accounts and run single account investigations there.

## Setup your
 monitoring account for cross-account access


###### Setup your monitoring account for cross-account access

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **AI Operations**,
 **Configuration**.
3. Under **Configure Cross-account access**, select
 **Configure**.
4. Add the Account ID for up to 25 accounts under the **List source
 accounts** section.
5. Update your IAM role.


	1. Automatically
	
	
	
	
		* If you choose **Automatically update the assistant
		 role (recommended)** , this creates a customer
		 managed policy named
		 `AIOpsAssistantCrossAccountPolicy-${guid}`
		 that includes the `sts:AssumeRole` statements
		 needed to assume the assistant role in the specified source
		 accounts. Choosing the automatic update option defaults the
		 IAM role name to
		 `AIOps-CrossAccountInvestigationRole` in the
		 source accounts .
		
		
		
		JSON
		
		
		
		
		
		```
		`{
		 "Version":"2012-10-17", 
		 "Statement": {
		 "Effect": "Allow",
		 "Action": "sts:AssumeRole",
		 "Resource": [
		 "arn:aws:iam::777777777777:role/AIOps-CrossAccountInvestigationRole",
		 "arn:aws:iam::555555555555:role/AIOps-CrossAccountInvestigationRole",
		 "arn:aws:iam::666666666666:role/AIOps-CrossAccountInvestigationRole"
		 ]
		 }
		}`
		
		```
		* If the monitoring account owner removes a source account
		 from the cross-account configuration, the IAM policy will
		 not update automatically. You must manually update the IAM
		 role and policy to ensure it always has the minimum
		 permissions possible.
		* You might reach the limit of managed policies per role if
		 the permissions are not manually updated when a source
		 account is removed. You must delete any unused managed
		 policies attached to your investigation role.
	2. Manually
	
	
	
	
		* The following example shows the trust policy required for
		 the assistant role: 
		
		
		
		JSON
		
		
		
		
		
		```
		`{
		 "Version":"2012-10-17", 
		 "Statement": [
		 {
		 "Sid": "AllowAIOpsAssumeRole",
		 "Effect": "Allow",
		 "Principal": {
		 "Service": "aiops.amazonaws.com"
		 },
		 "Action": "sts:AssumeRole",
		 "Condition": {
		 "StringEquals": {
		 "sts:ExternalId": "arn:aws:aiops:`us-east-1`:`123456789012`:investigation-group/AaBbcCDde1EfFG2g"
		 }
		 }
		 }
		 ]
		}`
		
		```
		
		
		
		
		
		You can use the AWS CLI to create the custom source account
		 role and then attach the `AIOpsAssistantPolicy`
		 to the role using the following commands, replacing the
		 placeholder values with the appropriate values for your
		 environment: 
		
		
		
		```
		**aws iam create-role**
		 --role-name `custom-role-name`
		 --assume-role-policy-document 
		    '{ 
		       "Version": "2012-10-17",		 	 	  
		       "Statement": [ 
		                 { 
		                      "Effect": "Allow",
		                      "Principal": { "AWS": "`investigation-group-role-arn`"
		                          }, 
		                      "Action": "sts:AssumeRole", 
		                      "Condition": {
		                                 "StringEquals": { 
		                                          "sts:ExternalId": "`investigation-group-arn`"
		                                            } } } ] }' 
		
		**aws iam attach-role-policy** 
		 --role-name `custom-role-name`
		 --policy-arn arn:aws:iam::aws:policy/AIOpsAssistantPolicy
		```
		* To grant cross-account access, the permission policy of
		 the assistant role in the monitoring account must contain
		 the following. If you are configuring the monitoring account
		 manually, the role name can be whatever you choose. It does
		 not default to
		 `AIOps-CrossAccountInvestigationRole`, make
		 sure to specify the name of the assistant role for each of
		 the source accounts. 
		
		
		
		JSON
		
		
		
		
		
		```
		`{
		 "Version":"2012-10-17", 
		 "Statement": {
		 "Effect": "Allow",
		 "Action": "sts:AssumeRole",
		 "Resource": [
		 "arn:aws:iam::`777777777777`:role/`custom_source_account_role_name`",
		 "arn:aws:iam::`555555555555`:role/`custom_source_account_role_name`",
		 "arn:aws:iam::`666666666666`:role/`custom_source_account_role_name`"
		 ]
		 }
		}`
		
		```
		* Use the AWS CLI to update the monitoring account
		 investigation group with the custom source account role ARN
		 using the following command, replacing the placeholder
		 values with the appropriate values for your environment: 
		
		
		
		```
		**aws aiops update-investigation-group** 
		 --identifier `investigation-group-id`
		 --cross-account-configurations sourceRoleArn=`sourceRoleArn1`  sourceRoleArn=`sourceRoleArn2`
		```
		
		For more details on this command, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/aiops/update-investigation-group.html "https://docs.aws.amazon.com/cli/latest/reference/aiops/update-investigation-group.html").

## Setup your source
 account(s) for cross-account access


1. Provision an IAM role with the name
 `AIOps-CrossAccountInvestigationRole` if you selected the
 **Automatically update the assistant role** option to
 set up the monitoring account. If you used the manual setup option,
 provision the IAM role with your customized source account role
 name.


	1. Attach the AWS managed policy `AIOpsAssistantPolicy`
	 to the role in the IAM console.
	2. The trust policy of the role on the source account looks like
	 this. `ExternalID` must be specified on the policy. Use
	 the monitoring account investigation group ARN.
	
	
	
	JSON
	
	
	
	
	
	```
	`{
	 "Version":"2012-10-17", 
	 "Statement": [
	 {
	 "Effect": "Allow",
	 "Principal": {
	 "AWS": "arn:aws:iam::123456789012:role/investigation-role-name"
	 },
	 "Action": "sts:AssumeRole",
	 "Condition": {
	 "StringEquals": {
	 "sts:ExternalId": "investigation-group-arn"
	 }
	 }
	 }
	 ]
	}`
	
	```
2. This must be done in each of the source accounts.
3. If you set up the monitoring account role through the console, the role
 name of the source account defaults to
 `AIOps-CrossAccountInvestionRole`.
4. Confirm access by logging into the monitoring account, navigating to
 **Investigation Group**, then
 **Configuration**, and then choosing
 **Cross-account setup**.


Make sure the source account shows up in the cross-account configuration,
 and the status is **Linked to monitoring account**.

## Investigating
 multi-account issues


After you set up CloudWatch cross-account observability dashboard, you can view and
 investigate from a cross-account telemetry in your monitoring account. You must add
 a cross-account telemetry from the source account in order to run an investigation
 into that source account. 


For detailed information about how to create an investigation, see [Investigate operational issues in your
 environment](Investigations-Investigate.md "Investigations-Investigate.md").
