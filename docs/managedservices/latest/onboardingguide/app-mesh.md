# Use AMS SSP to provision AWS App Mesh in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS App Mesh capabilities directly in your AMS managed account. AWS App Mesh provides application level networking to make it easy for your services to
communicate with each other across multiple types of compute infrastructure. App Mesh standardizes how your services
communicate, giving you end-to-end visibility and ensuring high-availability for your applications.

AWS App Mesh makes it easy to run services by providing consistent visibility and network traffic controls
for services built across multiple types of compute infrastructure. App Mesh removes the need to update application
code to change how monitoring data is collected or traffic is routed between services. App Mesh configures each
service to export monitoring data and implements consistent communications control logic across your application.
This makes it easy to quickly pinpoint the exact location of errors and automatically re-route network traffic when
there are failures or when code changes need to be deployed.
To learn more, see [AWS App Mesh](https://aws.amazon.com/app-mesh/ "https://aws.amazon.com/app-mesh/").

## AWS App Mesh in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access AWS App Mesh in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service |
Add change type (ct-1w8z66n899dct). This RFC provisions the following IAM role to your
account: `customer_app_mesh_console_role`. After it is provisioned in your account,
you must onboard the role in your federation solution.

**Q: What are the restrictions to using the AWS App Mesh?**

Full functionality of AWS App Mesh is available in your AMS account.

**Q: What are the prerequisites or dependencies to using AWS App Mesh?**

There are no prerequisites or dependencies to use AWS App Mesh in your AMS account.
