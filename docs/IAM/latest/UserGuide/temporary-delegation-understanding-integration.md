

# Understanding your integration
<a name="temporary-delegation-understanding-integration"></a>

After completing the onboarding process, you can build your integration with IAM temporary delegation. A complete integration typically involves three main categories of work:

## 1. User Experience and Workflow Design
<a name="temporary-delegation-user-experience"></a>

Build a front-end experience in the partner application that guides customers through the temporary delegation workflow. Partner application should:
+ Present a clear onboarding or configuration flow where customers can grant temporary access. Label this action clearly, such as "Deploy with IAM temporary delegation".
+ Redirect customers to the AWS Management Console to review and approve the delegation request using the console link returned by the CreateDelegationRequest API
+ Provide appropriate messaging about what permissions are being requested and why. Customers can see this message on the delegation request details page.
+ Handle the customer's return to your application after they complete the approval in AWS.

### Best Practices for Temporary Delegation Requests
<a name="temporary-delegation-request-best-practices"></a>

When implementing temporary delegation for your partner application, follow the below defined best practices to help customers verify request authenticity and accuracy.

**1. Include User-Identifiable Context in Request Messages**

You should include user-specific context in delegation request message. This information helps users identify the requests from their existing partner workflow and distinguish legitimate requests. Suggested information in request message:
+ Customer's account identifier or username in your service
+ Workspace name, subscription ID, or organization identifier
+ Specific resource being accessed (cluster name, project name, environment)
+ Unique transaction or request identifier generated for this delegation attempt

Example request message:

```
Request from Partner A workspace "production-analytics"
Account: user@example.com
Workspace ID: 1234ABCD
Cluster: ml-training-cluster-01
Request ID: 1111-2222-3333-4444
```

**2. Optional: Include AWS Account ID when Initiating Delegation**

If the customer account ID is available, include it in the delegation request. This verification step creates an additional binding between the customer's intent and the delegation token.

**3. Design Request Messages for Security Verification**

Structure your request messages to enable customers to confidently verify legitimacy before granting access. User experience requirements:
+ Display the request message prominently in your application interface before redirecting to AWS
+ Use clear, descriptive language that connects directly to the customer's current action
+ Avoid generic messages that could apply to any delegation request
+ Include sufficient detail for customers to verify the request matches their intended workflow
+ Display the AWS account ID that will receive delegated access
+ Provide a clear explanation of what permissions your application will request

Include a confirmation notice in your application before redirecting customers to the AWS consent screen:

```
⚠️ Redirecting to IAM Temporary Delegation
You are about to grant [Your Service Name] temporary access to your AWS account.

Before clicking "Allow" on the AWS consent screen:
• Verify the request details match your current action
• Confirm the AWS account ID matches your intended account
• Make sure you initiated this request from [Your Service Name]
```

**4. Session Binding Recommendations**

While AWS IAM handles the core authorization flow, implement these practices in your application to strengthen session integrity:
+ Generate unique, single-use request identifiers for each delegation attempt
+ Associate delegation requests with the customer's active application session
+ Implement appropriate request expiration depending on your delegation process
+ Validate that delegation callbacks match the originating request context
+ Log all delegation request initiations and completions for security monitoring

By following these best practices, you help create a more secure temporary delegation experience.

## 2. API Integration
<a name="temporary-delegation-api-integration"></a>

Use IAM temporary delegation APIs to send and manage delegation requests. After your AWS accounts are registered, you can access the following APIs:
+ *IAM CreateDelegationRequest* – Creates a delegation request for a customer's AWS account. This API returns a console link that you redirect customers to for reviewing and approving the request.
+ *AWS STS GetDelegatedAccessToken* – Retrieves temporary AWS credentials after a customer approves your delegation request. Use these credentials to perform actions in the customer's account.

Your integration should handle the complete lifecycle of delegation requests, including creating requests, monitoring their status, and retrieving temporary credentials when approved.

## 3. Resource Configuration and Orchestration
<a name="temporary-delegation-resource-configuration"></a>

After you obtain temporary credentials, orchestrate the necessary workflows to configure resources in the customer's AWS account. This might include:
+ Calling AWS service APIs directly to create and configure resources
+ Deploying infrastructure using AWS CloudFormation templates
+ Creating IAM roles for ongoing access (requires using permission boundaries). As a defense-in-depth measure, we recommend that you use dynamic role names, for example, a name with a randomly generated suffix. This approach makes the role name in each customer account unique and unpredictable.

Your orchestration logic should be idempotent and handle failures gracefully, as customers might need to retry or modify their delegation approvals.