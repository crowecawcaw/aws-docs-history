

# Best practices for using Amazon S3 policies
<a name="orgs_manage_policies_s3_best_practices"></a>

When implementing Amazon S3 policies across your organization, following established best practices helps ensure successful deployment and maintenance.

## Start simply and make small changes
<a name="s3-start-simple-incremental-changes"></a>

To simplify debugging, start with simple policies and make changes one item at a time. Validate the behavior and impact of each change before making the next change. This approach reduces the number of variables you have to account for when an error or unexpected result does happen.

## Establish review processes
<a name="s3-establish-review-processes"></a>

Implement processes to monitor for new policy attributes, evaluate policy exceptions, and make adjustments to maintain alignment with your organizational security and operational requirements.

## Validate changes to your Amazon S3 policies using DescribeEffectivePolicy
<a name="s3-validate-policy-changes"></a>

After you make a change to an Amazon S3 policy, check the effective policies for representative accounts below the level where you made the change. You can view the effective policy by using the AWS Management Console, or by using the DescribeEffectivePolicy API operation or one of its AWS CLI or AWS SDK variants. Ensure that the change you made had the intended impact on the effective policy.

## Communicate and train
<a name="s3-communicate-and-train"></a>

Ensure your organization understands the purpose and impact of your policies. Provide clear guidance on the expected behaviors and how to handle failures due to policy enforcement.

## Plan for legitimate public access needs
<a name="s3-plan-for-public-access"></a>

Before implementing organization-level policies, identify accounts that require public Amazon S3 buckets for legitimate business purposes (such as static website hosting). Consider using OU-level or account-level policy attachment to exclude these accounts, or consolidate public bucket needs into dedicated accounts.

## Monitor policy enforcement
<a name="s3-monitor-policy-enforcement"></a>

Use AWS CloudTrail to monitor policy attachment and enforcement actions. Set up EventBridge rules to automate responses to policy violations or changes.