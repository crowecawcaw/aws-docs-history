# Troubleshooting CloudFormation

When you use CloudFormation, you might encounter issues when you create, update, or delete
 CloudFormation stacks. The following sections can help you troubleshoot some common issues that
 you might encounter.

For general questions about CloudFormation, see the [AWS CloudFormation FAQs](https://aws.amazon.com/cloudformation/faqs/ "https://aws.amazon.com/cloudformation/faqs/"). You can also search for
 answers and post questions in the [CloudFormation community](https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w "https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w") on AWS re:Post.

###### Topics

* [Troubleshooting guide](#basic-ts-guide "#basic-ts-guide")
* [Troubleshooting errors](#troubleshooting-errors "#troubleshooting-errors")
* [Contacting support](#contacting-support "#contacting-support")

## Troubleshooting guide


If CloudFormation fails to create, update, or delete your stack, you can view error
 messages or logs to help you learn more about the issue. The following tasks describe
 general methods for troubleshooting a CloudFormation issue. For information about specific
 errors and solutions, see the [Troubleshooting errors](#troubleshooting-errors "#troubleshooting-errors") section.



* Use the [CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/")
 to view the status of your stack. In the console, you can view a list of stack
 events while your stack is being created, updated, or deleted. From this list,
 find the failure event and then view the status reason for that event. The
 status reason might contain an error message from CloudFormation or from a
 particular service that can help you troubleshoot your problem. For more
 information about viewing stack events, see [View CloudFormation stack events](view-stack-events.md "view-stack-events.md").
* For Amazon EC2 issues, view the `cloud-init` and cfn logs. These logs
 are published on the Amazon EC2 instance in the `/var/log/`
 directory. These logs capture processes and command outputs while CloudFormation is
 setting up your instance. For Windows, view the EC2Configure service in
 `%ProgramFiles%\Amazon\EC2ConfigService`, EC2 Launch in
 `%ProgramData%\Amazon\EC2-Windows\Launch\Logs`, EC2
 Launch v2 in `%ProgramData%\Amazon\EC2Launch\log`, and cfn
 logs in `C:\cfn\log`.


You can also configure your CloudFormation template so that the logs are published
 to Amazon CloudWatch, which displays logs in the AWS Management Console so you don't have to connect
 to your Amazon EC2 instance. For more information, see [View CloudFormation logs in the console](https://aws.amazon.com/blogs/devops/view-cloudformation-logs-in-the-console/ "https://aws.amazon.com/blogs/devops/view-cloudformation-logs-in-the-console/") in the Application Management
 Blog.

## Troubleshooting errors


When you come across the following errors with your CloudFormation stack, you can use the
 following solutions to help you find the source of the problems and fix them.


###### Topics

* [Delete stack
 fails](#troubleshooting-errors-delete-stack-fails "#troubleshooting-errors-delete-stack-fails")
* [Dependency error](#troubleshooting-errors-dependency-error "#troubleshooting-errors-dependency-error")
* [AWS Config and
 AWS Systems Manager conflicts](#troubleshooting-errors-config-system-manager-conflict "#troubleshooting-errors-config-system-manager-conflict")
* [Error parsing parameter when passing a list](#troubleshooting-errors-error-parsing-parameter-when-passing-a-list "#troubleshooting-errors-error-parsing-parameter-when-passing-a-list")
* [Insufficient
 IAM permissions](#troubleshooting-errors-insufficient-iam-permissions "#troubleshooting-errors-insufficient-iam-permissions")
* [Invalid value or unsupported resource property](#troubleshooting-errors-invalid-value-or-unsupported-resource-property "#troubleshooting-errors-invalid-value-or-unsupported-resource-property")
* [Quota exceeded](#troubleshooting-errors-limit-exceeded "#troubleshooting-errors-limit-exceeded")
* [Nested stacks are
 stuck in UPDATE\_COMPLETE\_CLEANUP\_IN\_PROGRESS,
 UPDATE\_ROLLBACK\_COMPLETE\_CLEANUP\_IN\_PROGRESS, or
 UPDATE\_ROLLBACK\_IN\_PROGRESS](#troubleshooting-errors-nested-stacks-are-stuck "#troubleshooting-errors-nested-stacks-are-stuck")
* [No updates to
 perform](#troubleshooting-errors-no-updates-to-perform "#troubleshooting-errors-no-updates-to-perform")
* [Resource failed to
 stabilize during a create, update, or delete stack operation](#troubleshooting-resource-did-not-stabilize "#troubleshooting-resource-did-not-stabilize")
* [Security group does not exist in VPC](#troubleshooting-errors-security-group-does-not-exist-in-vpc "#troubleshooting-errors-security-group-does-not-exist-in-vpc")
* [Update rollback
 failed](#troubleshooting-errors-update-rollback-failed "#troubleshooting-errors-update-rollback-failed")
* [Wait condition didn't receive the required number of signals from an Amazon EC2
 instance](#troubleshooting-errors-wait-condition-didnt-receive-the-required-number-of-signals "#troubleshooting-errors-wait-condition-didnt-receive-the-required-number-of-signals")
* [Resource
 removed from stack but not deleted](#troubleshooting-errors-resource-removed-not-deleted "#troubleshooting-errors-resource-removed-not-deleted")

### Delete stack
 fails


To resolve this situation, try the following:



* Some resources must be empty before they can be deleted. For example, you
 must delete all objects in an Amazon S3 bucket or remove all instances in an
 Amazon EC2 security group before you can delete the bucket or security
 group.
* Ensure that you have the necessary IAM permissions to delete the
 resources in the stack. In addition to CloudFormation permissions, you must be
 allowed to use the underlying services, such as Amazon S3 or Amazon EC2.
* When stacks are in the `DELETE_FAILED` state because CloudFormation
 couldn't delete a resource, rerun the [deletion](../APIReference/API_DeleteStack.md "../APIReference/API_DeleteStack.md") with the
 `RetainResources` parameter and specify the resource that
 CloudFormation can't delete. CloudFormation deletes the stack without deleting the
 retained resource. Retaining resources is useful when you can't delete a
 resource, such as an S3 bucket that contains objects that you want to keep,
 but you still want to delete the stack.


After you delete the stack, you can manually delete retained resources by
 using their associated AWS service.


Alternatively, you may consider using the `FORCE_DELETE_STACK`
 option with the `DeletionMode` parameter. For more information on
 force deleting a stack, see [Delete a stack from the CloudFormation console](cfn-console-delete-stack.md "cfn-console-delete-stack.md").
* You can't delete stacks that have termination protection enabled. If you
 attempt to delete a stack with termination protection enabled, the deletion
 fails and the stack--including its status--remains unchanged. Disable
 termination protection on the stack, then perform the delete operation
 again.


This includes [nested stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md")
 whose root stacks have termination protection enabled. Deactivate
 termination protection on the root stack, then perform the delete operation
 again. It's strongly recommended that you don't delete nested stacks
 directly, but only delete them as part of deleting the root stack and all
 its resources.


For more information, see [Protect CloudFormation stacks from being
 deleted](using-cfn-protect-stacks.md "using-cfn-protect-stacks.md").
* For all other issues, if you have AWS Support, you can create a Support case.
 See [Contacting support](#contacting-support "#contacting-support").

### Dependency error


To resolve a dependency error, add a `DependsOn` attribute to resources
 that depend on other resources in your template. In some cases, you must explicitly
 declare dependencies so that CloudFormation can create or delete resources in the
 correct order. For example, if you create an Elastic IP and a VPC with an Internet
 gateway in the same stack, the Elastic IP must depend on the Internet gateway
 attachment. For more information, see [DependsOn
 attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-dependson.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-dependson.html").


### AWS Config and
 AWS Systems Manager conflicts


AWS Config and AWS Systems Manager can automate infrastructure management tasks which can
 cause conflict with the deployment of a CloudFormation stack. Do the following to avoid
 any potential conflicts:



* Review the configuration of AWS Config and Systems Manager in the associated AWS account
 and AWS Region.
* Check for active rules or automation documents that might be triggered
 during a CloudFormation deployment. These may potentially cause conflicts or
 resource dependencies that conflict with your deployment.
* Check your CloudFormation template for any resources managed by AWS Config and
 Systems Manager. Check for potential overlaps or interdependencies and consider
 adjusting the template or automation configuration to avoid
 conflicts.
* Temporarily disable or suspend any related AWS Config rules or Systems Manager automations
 during CloudFormation deployment. Remember to restore the original
 configurations after the successful deployment to maintain the desired level
 of automation and compliance.
* Review the CloudFormation logs and error messages for any reference to AWS Config
 and Systems Manager-related issues to help pinpoint the source of the conflict.

For more information on AWS Config rules, see [Evaluating Resources
 with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html "https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html").


For more information on Systems Manager automations, see [AWS Systems Manager
 Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html").


### Error parsing parameter when passing a list


When you use the AWS CLI or CloudFormation to pass in a list, add the escape character
 (`\`) before each comma. The following sample shows how you specify
 an input parameter when using the AWS CLI.



```
ParameterKey=CIDR,ParameterValue='10.10.0.0/16\,10.10.0.0/24\,10.10.1.0/24'
```

### Insufficient
 IAM permissions


When you work with a CloudFormation stack, you not only need permissions to use
 CloudFormation, you must also have permission to use the underlying services that are
 described in your template. For example, if you're creating an Amazon S3 bucket or
 starting an Amazon EC2 instance, you need permissions to Amazon S3 or Amazon EC2. Review your IAM
 policy and verify that you have the necessary permissions before you work with
 CloudFormation stacks. For more information see, [Control CloudFormation access with AWS Identity and Access Management](control-access-with-iam.md "control-access-with-iam.md").


### Invalid value or unsupported resource property


When you create or update a CloudFormation stack, your stack can fail due to invalid
 input parameters, unsupported resource property names, or unsupported resource
 property values. For input parameters, verify that the resource exists. For example,
 when you specify an Amazon EC2 key pair or VPC ID, the resource must exist in your
 account and in the region in which you are creating or updating your stack. You can
 use [AWS-specific parameter
 types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md") to ensure that you use valid values.


For resource property names and values, update your template to use valid names
 and values. For more information, see the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html").


### Quota exceeded


Verify that you didn't reach a resource quota. For example, the default maximum
 number of Amazon EC2 On-Demand instances that you can launch is 5. If try to create more
 Amazon EC2 On-Demand instances than your account quota, the instance creation fails and
 you receive the error `Status=start_failed`. To view the default AWS
 quotas by service, see [AWS
 service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html") in the *AWS General Reference*.


For CloudFormation quotas and tweaking strategies, see [Understand CloudFormation quotas](cloudformation-limits.md "cloudformation-limits.md").


Also, during an update, if a resource is replaced, CloudFormation creates new resource
 before it deletes the old one. This replacement might put your account over the
 resource quota, which would cause your update to fail. You can delete excess
 resources or request a [quota
 increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html").


### Nested stacks are
 stuck in `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS`,
 `UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS`, or
 `UPDATE_ROLLBACK_IN_PROGRESS`


A nested stack failed to roll back. Because of potential resource dependencies
 between nested stacks, CloudFormation doesn't start cleaning up nested stack resources
 until all nested stacks have been updated or have rolled back. When a nested stack
 fails to roll back, CloudFormation cancels all operations, regardless of the state that
 the other nested stacks are in. A nested stack that completed updating or rolling
 back but didn't receive a signal from CloudFormation to start cleaning up because
 another nested failed to roll back is in an
 `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS` or
 `UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS` state. A nested stack
 that failed to update but didn't receive a signal to start rolling back is in an
 `UPDATE_ROLLBACK_IN_PROGRESS` state.


A nested stack might fail to roll back because of changes that were made outside
 of CloudFormation, when the stack template doesn't accurately reflect the state of the
 stack. A nested stack might also fail if an Auto Scaling group in a nested stack had an
 insufficient resource signal timeout period when the group was created or
 updated.


To fix the stack, contact [AWS Support](#contacting-support "#contacting-support").


### No updates to
 perform


To update a CloudFormation stack, you must submit template or parameter value changes
 to CloudFormation. However, CloudFormation won't recognize some template changes as an
 update, such as changes to a deletion policy, update policy, condition declaration,
 or output declaration. If you need to make such changes without making any other
 change, you can add or modify a metadata attribute for any of your resources. The
 metadata attribute can be any arbitrary value, as CloudFormation does not interpret its
 content. For more information, see [Metadata
 attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-metadata.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-metadata.html").


### Resource failed to
 stabilize during a create, update, or delete stack operation


A resource didn't respond because the operation exceeded the CloudFormation timeout
 period or an AWS service was interrupted. For service interruptions, [check](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") that the relevant AWS service is
 running, and then retry the stack operation.


If the AWS services have been running successfully, check if your stack contains
 one of the following resources:



* `AWS::AutoScaling::AutoScalingGroup` for create, update, and
 delete operations
* `AWS::CertificateManager::Certificate` for create
 operations
* `AWS::CloudFormation::Stack` for create, update, and delete
 operations
* `AWS::ElasticSearch::Domain` for update operations
* `AWS::RDS::DBCluster` for create and update operations
* `AWS::RDS::DBInstance` for create, update, and delete
 operations
* `AWS::Redshift::Cluster` for update operations

Operations for these resources might take longer than the default timeout period.
 The timeout period depends on the resource and credentials that you use. To extend
 the timeout period, specify a [service
 role](using-iam-servicerole.md "using-iam-servicerole.md") when you perform the stack operation. If you're already using a
 service role, or if your stack contains a resource that isn't listed, contact [AWS Support](#contacting-support "#contacting-support").


If your stack is in the `UPDATE_ROLLBACK_FAILED` state, see [Update Rollback
 Failed](#troubleshooting-errors-update-rollback-failed "#troubleshooting-errors-update-rollback-failed").


### Security group does not exist in VPC


Verify that the security group exists in the VPC that you specified. If the
 security group exists, ensure that you specify the security group ID and not the
 security group name. For example, the `AWS::EC2::SecurityGroupIngress`
 resource has a `SourceSecurityGroupName` and
 `SourceSecurityGroupId` properties. For VPC security groups, you must
 use the `SourceSecurityGroupId` property and specify the security group
 ID.


### Update rollback
 failed


A dependent resource can't return to its original state, causing the rollback to
 fail (`UPDATE_ROLLBACK_FAILED` state). For example, you might have a
 stack that's rolling back to an old database instance that was deleted outside of
 CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes
 that the database instance still exists and attempts to roll back to it, causing the
 update rollback to fail.


Depending on the cause of the failure, you can manually fix the error and continue
 the rollback. By continuing the rollback, you can return your stack to a working
 state (the `UPDATE_ROLLBACK_COMPLETE` state), and then try to update the
 stack again. The following list describes solutions to common errors that cause
 update rollback failures:



* Failed to receive the required number of signals

Use the [signal-resource](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/signal-resource.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/signal-resource.html") command to manually send the
 required number of successful signals to the resource that's
 waiting for them, and then continue rolling back the update. For
 example, during an update rollback, instances in an Auto Scaling group
 might fail to signal success within the specified timeout
 duration. Manually send success signals to the Auto Scaling group. When
 you continue the update rollback, CloudFormation sees your signals
 and proceeds with the rollback.
* Changes to a resource were made outside of CloudFormation

Manually sync resources so that they match the original
 stack's template, and then continue rolling back the update. For
 example, if you manually deleted a resource that CloudFormation is
 attempting to roll back to, you must manually create that
 resource with the same name and properties it had in the
 original stack.
* Insufficient permissions

Check that you have sufficient IAM permissions to modify
 resources, and then continue the update rollback. For example,
 your IAM policy might allow you to create an S3 bucket, but
 not modify the bucket. Add the modify actions to your
 policy.
* Invalid security token

CloudFormation requires a new set of credentials. No change is
 required. Continue rolling back the update, which refreshes the
 credentials.
* Limitation error

Delete resources that you don't need or request a [quota increase](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html"), and then
 continue rolling back the update. For example, if your account
 quota for the number of EC2 On-Demand instances is 5 and the
 update rollback exceeds that quota, it will fail.
* Resource didn't stabilize

A resource didn't respond because the operation might have
 exceeded the CloudFormation timeout period or an AWS service might
 have been interrupted. No change is required. After the resource
 operation is complete or the AWS service is back in operation,
 continue rolling back the update.

To continue rolling back an update, you can use the CloudFormation console or AWS
 command line interface (AWS CLI). For more information, see [Continue rolling back an
 update](using-cfn-updating-stacks-continueupdaterollback.md "using-cfn-updating-stacks-continueupdaterollback.md").


If none of these solutions work, you can skip the resources that CloudFormation can't
 successfully roll back. For more information, see the `ResourcesToSkip`
 parameter for the [ContinueUpdateRollback](../APIReference/API_ContinueUpdateRollback.md "../APIReference/API_ContinueUpdateRollback.md") API operation in the
 *AWS CloudFormation API Reference*. CloudFormation sets the status of the
 specified resources to `UPDATE_COMPLETE` and continues to roll back the
 stack. After the rollback is complete, the state of the skipped resources will be
 inconsistent with the state of the resources in the stack template. Before you
 perform another stack update, you must modify the resources or update the stack to
 be consistent with each other. If you don't, subsequent stack updates might fail and
 make your stack unrecoverable.


### Wait condition didn't receive the required number of signals from an Amazon EC2
 instance


To resolve this situation, try the following:



* Ensure that the AMI you're using has the CloudFormation helper scripts
 installed. If the AMI doesn't include the helper scripts, you can also
 download them to your instance. For more information, see the [CloudFormation helper scripts reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-helper-scripts-reference.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-helper-scripts-reference.html") in the
 *AWS CloudFormation Template Reference Guide*.
* Verify that the `cfn-signal` command was successfully run on
 the instance. You can view logs, such as
 `/var/log/cloud-init.log` or
 `/var/log/cfn-init.log`, to help you debug the
 instance launch. You can retrieve the logs by logging in to your instance,
 but you must [disable rollback on
 failure](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options") or else CloudFormation deletes the instance after your stack
 fails to create. You can also [publish the logs](https://aws.amazon.com/blogs/devops/view-cloudformation-logs-in-the-console/ "https://aws.amazon.com/blogs/devops/view-cloudformation-logs-in-the-console/") to Amazon CloudWatch. For Windows, you can view cfn
 logs in `C:\cfn\log` and EC2Config service logs in
 `%ProgramFiles%\Amazon\EC2ConfigService`.
* Verify that the instance has a connection to the Internet. If the instance
 is in a VPC, the instance should be able to connect to the Internet through
 a NAT device if it's is in a private subnet or through an Internet gateway
 if it's in a public subnet. To test the instance's Internet connection, try
 to access a public web page, such as `http://aws.amazon.com`. For
 example, you can run the following command on the instance. It should return
 an HTTP 200 status code.



```
`curl -I https://aws.amazon.com`
```

For information about configuring a NAT device, see [NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html") in the
 *Amazon VPC User Guide*.

### Resource
 removed from stack but not deleted


During a stack update, CloudFormation has removed a resource from a stack but not
 deleted the resource. The resource still exists, but is no longer accessible through
 CloudFormation. This may occur during stack updates where:



* CloudFormation needs to replace an existing resource, so it first creates a
 new resource, then attempts to delete the old resource.
* You have removed the resource from the stack template, so CloudFormation
 attempts to delete the resource from the stack.

However, there may be cases where CloudFormation can't delete the resource. For
 example, if the user doesn't have permissions to delete a resource of a given
 type.


CloudFormation attempts to delete the old resource three times. If CloudFormation can't
 delete the old resource, it removes the old resource from the stack and continues
 updating the stack. When the stack update is complete, CloudFormation issues an
 `UPDATE_COMPLETE` stack event, but includes a
 `StatusReason` that states that one or more resources couldn't be
 deleted. CloudFormation also issues a `DELETE_FAILED` event for the specific
 resource, with a corresponding `StatusReason` providing more detail on
 why CloudFormation failed to delete the resource.


To resolve this situation, delete the resource directly using the console or API
 for the underlying service.


## Contacting support


If you have AWS Support, you can create a technical support case at [https://console.aws.amazon.com/support/home#/](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). Before you contact
 support, gather the following information:



* The ID of the stack. You can find the stack ID in the
 **Overview** tab of the [CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"). For more information, see
 [View stack information from the
 CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md").


###### Important

Don't make changes to the resources in the stack outside of CloudFormation. Making changes to the
 resources in your stack outside of CloudFormation might put your stack in an unrecoverable state.
* Any stack error messages. For information about viewing stack error messages,
 see the [Troubleshooting guide](#basic-ts-guide "#basic-ts-guide")
 section.
* For Amazon EC2 issues, gather the `cloud-init` and cfn logs. These logs
 are published on the Amazon EC2 instance in the `/var/log/`
 directory. These logs capture processes and command outputs while your instance
 is setting up. For Windows, gather the EC2Configure service and cfn logs in
 `%ProgramFiles%\Amazon\EC2ConfigService` and
 `C:\cfn\log`.

You can also search for answers and post questions in the [CloudFormation community](https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w "https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w") on AWS re:Post.
