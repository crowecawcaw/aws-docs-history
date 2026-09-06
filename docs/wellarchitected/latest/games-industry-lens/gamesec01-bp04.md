

# GAMESEC01-BP04 Use roles and federated access policies together with account level access policies to grant access to your AWS resources
<a name="gamesec01-bp04"></a>

 New AWS users often use IAM policies only when granting access to others. However, if you are using AWS Organizations, consider how to use service control policies together with IAM policies to grant your studio team members and contractors the necessary levels of access. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-15"></a>

 You can create IAM policies to allow or deny access to AWS services or API actions that work with AWS Identity and Access Management. They can only be applied to IAM identities, such as users, groups, or roles. For example, an IAM policy might be used to provide a user read-only access to Amazon S3. 

 Service control policies (SCPs) are guardrails for your AWS accounts. An SCP doesn't grant permissions, they are used to restrict actions on AWS services for individual member accounts. For example, an SCP can deny an AWS account from accessing a particular Region. 

 When an action is taken, the relevant IAM policy is evaluated in combination with the SCPs. Following up on the previous example, is a role is attempts to run an EC2 instance, IAM indicates is they are permitted ("Allow" for ec2:RunInstances) and the SCPs will determine if their choice of Region is valid ("us-east-1" is permitted, but "us-west-1" is denied by the SCP). 

 Layering IAM policies and SCPs can verify that anyone who accesses your AWS resources will only be given the appropriate permissions that they need. This is especially important to consider if your AWS accounts and resources span multiple Regions, but not everyone within your game studio needs to access all of them. 

 You can tailor IAM policies to grant specific teams specific permissions for updating things like game configurations, managing player data, configuring promotional events, and moderating user-generated content. Meanwhile, you can use SCPs to enforce organization-wide controls crucial for game operations. These might include restricting deployment to only approved Regions where the game operates, helping prevent unauthorized access to sensitive player data stores, enforcing compliance requirements, and controlling costs by limiting service usage across development accounts. 

### Implementation steps
<a name="implementation-steps-15"></a>
+  Use IAM policies to manage permissions for individual users, groups, or roles. 
+  Use service control policies (SCPs) in AWS Organizations to enforce account-level permissions. 
+  Combine IAM policies and SCPs to grant only the required access for specific users and accounts. 

### Resources
<a name="resources-1"></a>
+  [Policies and permissions in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 
+  [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) 
+  [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) 