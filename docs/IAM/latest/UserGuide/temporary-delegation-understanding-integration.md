# Understanding your integration

After completing the onboarding process, you can build your integration with IAM temporary delegation. A complete integration typically involves three main categories of work:

## 1. User Experience and Workflow Design

Build a front-end experience in the partner application that guides customers through the temporary delegation workflow. Partner application should:

- Present a clear onboarding or configuration flow where customers can grant temporary access. Label this action clearly, such as "Deploy with IAM temporary delegation".
- Redirect customers to the AWS Management Console to review and approve the delegation request using the console link returned by the CreateDelegationRequest API
- Provide appropriate messaging about what permissions are being requested and why. Customers can see this message on the delegation request details page.
- Handle the customer's return to your application after they complete the approval in AWS.

## 2. API Integration

Use IAM temporary delegation APIs to send and manage delegation requests. Once your AWS accounts are registered, you can access the following APIs:

- _IAM CreateDelegationRequest_ – Creates a delegation request for a customer's AWS account. This API returns a console link that you redirect customers to for reviewing and approving the request.
- _AWS STS GetDelegatedAccessToken_ – Retrieves temporary AWS credentials after a customer approves your delegation request. Use these credentials to perform actions in the customer's account.

Your integration should handle the complete lifecycle of delegation requests, including creating requests, monitoring their status, and retrieving temporary credentials when approved.

## 3. Resource Configuration and Orchestration

Once you obtain temporary credentials, orchestrate the necessary workflows to configure resources in the customer's AWS account. This may include:

- Calling AWS service APIs directly to create and configure resources
- Deploying infrastructure using AWS CloudFormation templates
- Creating IAM roles for ongoing access (requires using permission boundaries)

Your orchestration logic should be idempotent and handle failures gracefully, as customers may need to retry or modify their delegation approvals.
