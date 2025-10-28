# Use AMS SSP to provision AWS Lambda in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Lambda capabilities directly in your AMS managed account. AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume,
there is no charge when your code is not running.
With Lambda, you can run code for virtually any type of application or back-end service, all with zero administration.
upload your code and Lambda takes care of
everything required to run and scale your code with high availability. You can set up your code to automatically trigger
from other AWS services, or call it directly from any Web or mobile app.
To learn more, see [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/").

## Lambda in AWS Managed Services FAQ

**Q: How do I request access to AWS Lambda in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM roles to your account:
`customer_lambda_admin_role` and
`customer_lambda_basic_execution_role`. After it's
provisioned in your account, you must onboard the roles in your federation
solution.

**Q: What are the restrictions to using AWS Lambda in my AMS account?**

- A Lambda function is designed to be invoked by event sources. For a list of services that can
  be used as a Lambda event source, see
  [Using AWS Lambda with Other Services](../../../lambda/latest/dg/lambda-services.md "../../../lambda/latest/dg/lambda-services.md"). Not all of these services are currently available in AMS accounts. If you require a service that isn't available, then work with your
  AMS CSDM to file an exception.
- By default AMS provides you with a basic Lambda initiation role containing the
  `AWSLambdaBasicExecutionRole` and
  `AWSXrayWriteOnlyAccess` permissions; for information, see
  [AWS Lambda
  Initiation Role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md"). If you require additional permissions, such as
  the ability to provision Lambda functions within your AMS VPC, submit an RFC with the
  Management | AWS service | Self-provisioned service | Add (managed automation)(ct-3qe6io8t6jtny) change type.

**Q: What are the prerequisites or dependencies to using AWS Lambda in my AMS account?**

There are no prerequisites or dependencies to get started with AWS Lambda; however, depending on your
specific use case, you might require access to other AWS services to
create event sources, or additional permissions for your function to perform various actions. If additional
permissions are needed, submit an RFC with the Management | AWS service | Self-provisioned service | Add (managed automation) change type (ct-3qe6io8t6jtny).

**Q: What do I need to do to run a Lambda function in any of my accounts?**

To deploy a Lambda function in a core account, use the following guidelines:

- Make sure that SSPS for AWS Lambda is onboarded.
- There are no specific restrictions prohibiting this deployment under the AMS responsibilities, as long as your AMS resources are protected and compliant.
- If you want AMS to create the Lambda function, then you must first use the SSPS role provided for AWS Lambda. Then, if you still want AMS assistance to deploy or support the function, contact your CA and start the out of scope (OOS) process.
