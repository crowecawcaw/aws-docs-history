# Appendix A: Creating ORR guidance from an incident

This section will provide an example of using a post-incident analysis to generate questions
and guidance for an ORR.

## Scenario

The workload in this incident is deployed using AWS CloudFormation to create infrastructure like a
VPC, Amazon EC2 instances, auto scaling groups, Amazon DynamoDB tables, Amazon S3 buckets, and AWS Identity and Access Management
(IAM) roles and policies. The EC2 instances are configured with an IAM role that allows
them to `GET` and `PUT` items into the DynamoDB table. During an approved
manual change event, the IAM role was updated with additional permissions to allow scan and
query operations of the DynamoDB table to support new functionality in the service. The updated
features to the service are deployed and it operates without issue for several months.

The team is now planning on releasing an additional feature that will require their EC2
instances to download data from an Amazon S3 bucket. As part of the feature release, they update
their CloudFormation template with the required Amazon S3 permissions as well as a number of other
changes, like creating the S3 bucket, and setting the bucket policy. The update is first run
on a beta environment that is used for developer testing, but the environment doesn’t exactly
mirror production and changes aren’t controlled through CI/CD. The update completes
successfully in beta and they proceed to deploy the update in production. Then, the engineer
applying the change immediately starts seeing errors in the logs that all scan and query
operations against their DynamoDB table are failing.

## Mitigation

After seeing the errors, it was obvious to the engineer that the CloudFormation deployment
was the cause. To revert the new changes, the engineer ran the most recent known-to-work
commit of their CloudFormation template. After running the update, the impact was still not
mitigated and the errors continued. At this point, the engineer realizes that the necessary
IAM permissions for those operations were not in the CloudFormation template and manually
adds a new statement to the role’s policy to allow them. This mitigates the impact and the
service returns to normal operation.

## Post-incident analysis

The root cause of this incident was that the manual change to update the IAM policy was
not recorded in the CloudFormation template. When the last update was run, CloudFormation
replaced the current IAM policy with the one in its template, which resulted in removing the
permissions for scan and query operations. The impact wasn’t detected in the beta environment
because the role being used there had an additional IAM policy attached that allowed all
actions on all resources to prevent testing issues related to permissions. There was no other
pre-production environment that exactly mirrored production.

## ORR guidance generation

Based on this event, you can create a question that asks:

| How are you ensuring that you do not impact customers when using AWS CloudFormation to manage AWS resources? |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                              | The guidance for this question would be the following: <br>• Apply the same level of scrutiny to infrastructure managed by CloudFormation as you do for software or configuration changes. <br>• Separate stateful resources into their own stack to reduce the scope of impact of changes. <br>• Use [drift detection](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md") to detect when resources have been changed outside of CloudFormation. <br>• Use [change sets](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md") to validate the intent of your stack update matches the actions that CloudFormation will take when the change set is executed. <br>• Test CloudFormation stack updates in a pre-production environment that mirrors production. <br>• Apply [stack policies](../../../AWSCloudFormation/latest/UserGuide/protect-stack-resources.md "../../../AWSCloudFormation/latest/UserGuide/protect-stack-resources.md") to protect critical resources from being unintentionally updated or deleted. These are some additional questions to consider when preparing a response for this: <br>• How do you ensure that an operator cannot accidentally delete a stack or critical resources managed by CloudFormation? <br>• Are you using CloudFormation change sets to validate that the intent of a change matches the actions CloudFormation will apply? <br>• How are you ensuring that a CloudFormation stack update doesn't affect your largest fault container (usually a Region, zone, or cell)? <br>• How are you ensuring changes are not made to CloudFormation managed resources directly? <br>• How are you partitioning resources across CloudFormation stacks? Finally, provide one or more links to the post-incident analysis that drove the creation of this question to provide cautionary tales of how this has gone wrong before. This helps provide context for the guidance and makes it more concrete for your engineering teams using the ORR. ## Summary The previous guidance could have helped prevent this event. Using change sets would have provided insights that the managed policy was going to be updated. This would have allowed the engineer to quickly do a comparison of the _as-is_ and _to-be_ configuration and identify that those permissions were being removed. Additionally, running the update in a pre-production environment that mirrored production would have identified that the update resulted in errors before ever being applied to production. Finally, enforcing that all changes to resources provisioned by CloudFormation are made through CloudFormation would ensure that the permissions updates were included in the template. For [resources that support it](../../../AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.md "../../../AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.md"), running drift detection before the update will identify that out of band changes were made to a resource. |
