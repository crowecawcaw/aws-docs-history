# Permissions for interceptors

When configuring interceptors, your gateway service role must have the lambda:InvokeFunction IAM permissions to invoke the Lambda functions that serve as interceptors. The service role needs specific permissions to execute interceptor functions during request and response processing.

For detailed information about configuring the required permissions for your gateway service role, including permissions to Lambda, see [Gateway service role permissions](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions").
