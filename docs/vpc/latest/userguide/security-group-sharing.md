# Share security groups with AWS Organizations

The Shared Security Group feature enables you to share a security group with other
AWS Organizations accounts within the same AWS Region and make the security group
available to be used by those accounts.

The following diagram demonstrates how you can use the Shared Security Group feature to
simplify security group management across accounts in your AWS Organizations:

![A diagram of security group sharing with other accounts in a shared VPC subnet.](images/sec-group-sharing.png)
This diagram shows three accounts that are part of the same Organization. Account A shares a
VPC subnet with Accounts B and C. Account A shares the security group with Accounts B
and C using the Shared Security Group feature. Accounts B and C then use that security
group when they launch instances in the shared subnet. This enables Account A to manage
the security group; any updates to the security group apply to the resources that
Accounts B and C have running in the shared VPC subnet.

###### Requirements of the Shared Security Group feature

- This feature is only available for accounts in the same Organization in
  AWS Organizations. [Resource
  sharing](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") must be enabled in AWS Organizations.
- The account that shares the security group must own both the VPC
  and the security group.
- You cannot share default security groups.
- You cannot share security groups that are in a default VPC.
- Participant accounts can create security groups in a shared VPC
  but they cannot share those security groups.
- A minimum set of permissions is required for an IAM principal to share a
  security group with AWS RAM. Use the `AmazonEC2FullAccess` and
  `AWSResourceAccessManagerFullAccess` managed IAM policies to ensure your IAM
  principals have the required permissions to share and use shared security
  groups. If you use a custom IAM policy, the `c2:PutResourcePolicy` and
  `ec2:DeleteResourcePolicy` actions are required. These are permission-only IAM
  actions. If an IAM principal doesn’t have these permissions granted, an error
  will occur when attempting to share the security group using the AWS RAM.
  **Services that support this feature**

- Amazon API Gateway
- Amazon EC2
- Amazon ECS
- Amazon EFS
- Amazon EKS
- Amazon EMR
- Amazon FSx
- Amazon ElastiCache
- AWS Elastic Beanstalk
- AWS Glue
- Amazon MQ
- Amazon SageMaker AI
- ELB

      + Application Load Balancer
      + Network Load Balancer

  **How this feature affects existing quotas**

[Security group quotas](amazon-vpc-limits.md#vpc-limits-security-groups "amazon-vpc-limits.md#vpc-limits-security-groups") apply. For the
'Security groups per network interface' quota, however, if a participant uses both owned
and shared groups on an Elastic network interface (ENI), the minimum of owner and
participant's quota applies.

Example to demonstrate how the quota is affected by this feature:

- Owner account quota: 4 security groups per
  interface
- Participant account quota: 5 security groups per
  interface.
- Owner shares groups SG-O1, SG-O2, SG-O3, SG-O4, SG-O5 with
  participant. Participant already has groups of their own in
  the VPC: SG-P1, SG-P2, SG-P3, SG-P4, SG-P5.
- If participant creates an ENI and uses only their owned groups, they can associate
  all 5 security groups (SG-P1, SG-P2, SG-P3, SG-P4, SG-P5) because that's their
  quota.
- If the participant creates an ENI and uses any shared groups on it, they can only
  associate up to 4 groups. In this case, the quota for such an ENI is the minimum
  of owner and participant's quotas. Possible valid configurations will look like
  this:
  - SG-O1, SG-P1, SG-P2, SG-P3
  - SG-O1, SG-O2, SG-O3, SG-O4

## Share a security group

This section explains how to use the AWS Management Console and the AWS CLI to share a security group with other accounts in your Organization.

AWS Management Console

###### To share a security group

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose **Security groups**.
3. Choose a security group to view the details.
4. Choose the **Sharing** tab.
5. Choose **Share security group**.
6. Choose **Create resource share**. As a result, the AWS RAM console opens where you’ll create the resource share for the security group.
7. Enter a **Name** for the resource share.
8. Under **Resources - optional**, choose **Security Groups**.
9. Choose a security group. The security group cannot be a default security group and cannot be associated with the default VPC.
10. Choose **Next**.
11. Review the actions that principals will be allowed to perform and choose **Next**.
12. Under **Principals - optional**, choose **Allow sharing only within your organization**.
13. Under **Principals**, select one of the following principal types and enter the appropriate numbers:
    - **AWS account**: The account number of an account in your Organization.
    - **Organization**: The AWS Organizations ID.
    - **Organizational unit (OU)**: The ID of an OU in the Organization.
    - **IAM role**: The ARN of an IAM role. The account that created the role must be a member of the same Organization as the account creating this resource share.
    - **IAM user**: The ARN of an IAM user. The account that created the user must be a member of the same Organization as the account creating this resource share.
    - **Service principal**: You cannot share a security group with a service principal.

14. Choose **Add**.
15. Choose **Next**.
16. Choose **Create resource share**.
17. Under **Shared resources**, wait to see the **Status** of `Associated`. If there is a security group association failure, it may be due to one of the limitations listed above. View the details of the security group and the **Sharing** tab on the details page to see any messages related to why a security group may not be shareable.
18. Return to the VPC console security group list.
19. Choose the security group you shared.
20. Choose the **Sharing** tab. Your AWS RAM resource should be visible there. If it’s not, the resource share creation may have failed and you may need to recreate it.

Command line

###### To share a security group

1. You must first create a resource share for the security group that you want to share with AWS RAM. For steps on how to create a resource share with AWS RAM using the AWS CLI, see [Creating a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_
2. To view created resource share associations, use [get-resource-share-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-resource-share-associations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-resource-share-associations.html").

The security group is now shared. You can select the security group when [launching an EC2 instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") in a shared subnet within the same VPC.

## Stop sharing a security group

This section explains how to use the AWS Management Console and the AWS CLI to stop sharing a security group with other accounts in your Organization.

AWS Management Console

###### To stop sharing a security group

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose **Security groups**.
3. Choose a security group to view the details.
4. Choose the **Sharing** tab.
5. Choose a security group resource share and choose **Stop sharing**.
6. Choose **Yes, stop sharing**.

Command line
**To stop sharing a security group**

Delete the resource share with [delete-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-resource-share.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-resource-share.html").

The security group is no longer being shared. After the owner stops sharing a security
group, the following rules apply:

- Existing participant Elastic Network Interfaces (ENIs) continue to get any security group rule
  updates that are made to unshared security groups. Unsharing only prevents
  the participant from creating new associations with the unshared
  group.
- Participants can no longer associate the unshared security group with any ENIs they own.
- Participants can describe and delete the ENIs that are still associated with unshared security groups.
- If participants still have ENIs associated with the unshared security group, the owner cannot delete the unshared security group. The owner can only delete the security group after participants disassociate (remove) the security group from all their ENIs.
- Participants cannot launch new EC2 instances using an ENI associated with
  an unshared security group.
