# Use AMS SSP to provision AWS Step Functions in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Step Functions capabilities directly in your AMS managed account. AWS Step Functions is a Web service that enables you to coordinate the components of distributed applications and microservices by
using visual workflows.
You build applications from individual components that each perform a discrete function, or task, allowing you to scale
and change applications quickly.
Step Functions provides a reliable way to coordinate components and step through the functions of your application. Step
Functions offers a graphical
console to visualize the components of your application as a series of steps. It automatically triggers and tracks each
step, and retries when there are errors,
so your application runs in order and as expected, every time. Step Functions logs the state of each step, so when things
do go wrong, you can diagnose and debug problems quickly.
To learn more, see [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/").

## Step Functions in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Step Functions in my AMS account?**

Request access to AWS Step Functions by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account: `customer_step_functions_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Step Functions in my AMS account?**

Full functionality of the AWS Step Functions is available in your AMS account.

**Q: What are the prerequisites or dependencies to using AWS Step Functions in my AMS account?**

At runtime, the role used by Step Functions must have access to the
services used by the step function. For example, a step function could
depend on Lambda functions. Someone authoring a step function is likely to
be creating Lambda functions at the same time and would have to request
access to that service as well.
