# Use AMS SSP to provision AWS Amplify in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Amplify capabilities directly in your AMS managed account. The AWS Amplify is a complete solution that allows frontend web and mobile developers to easily build, connect, and host fullstack applications. Amplify provides flexibility to leverage the breadth of AWS services as your use cases evolve. Amplify provides products to build fullstack iOS, Android, Flutter, Web, and React Native apps.
To learn more, see
[AWS Amplify](https://docs.amplify.aws/console "https://docs.amplify.aws/console").

## AWS Amplify in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request AWS Amplify to be set up in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type. This RFC provisions the following IAM role to your account: `customer_amplify_console_role`. After provisioned to your account, you must onboard the role in your federation solution.

Additionally, you must provide a Risk Acceptance because AWS Amplify has infrastructure-mutating permissions. To do this, work with your Cloud Service Delivery Manager (CSDM).

**Q: What are the restrictions to using AWS Amplify in my AMS account?**

You must use `'amplify*'` as the prefix for your buckets when working with Amplify, unless RA and specified otherwise.

**Q: What are the prerequisites or dependencies to using AWS Amplify in my
AMS account?**

There are no prerequisites for the use of AWS Amplify in your AMS account.

**Malz environments only**: The default onboarded role for Amplify is "customer_amplify_console_role". To use a custom role, first deploy the IAM entities. Then, create an additional RFC to add your custom role to the Service Control Policy for Application Accounts allow list.
