# Use AMS SSP to provision AWS Service Catalog AppRegistry in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AppRegistry capabilities directly in your AMS managed account. AppRegistry enables application search, reporting, and management actions from a central location. Builders seldom create applications in a single AWS account. They typically separate application resources by lifecycle phases, such as development, test, and production. AppRegistry allows you to group and view all your resource collections across the AWS accounts that you define.

With AppRegistry, you can store your AWS applications, the collection of resources that are associated with your applications, and application attribute groups.
To learn more, see
[What is AppRegistry](../../../servicecatalog/latest/arguide/intro-app-registry.md "../../../servicecatalog/latest/arguide/intro-app-registry.md").

## FAQ: AWS Service Catalog AppRegistry in AMS

**Q: How do I request access to AWS Service Catalog AppRegistry in my AMS account?**

Request access to AppRegistry by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer-appregistry-console-role`.
After provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Service Catalog AppRegistry in my AMS account?**

Full access to the AppRegistry service is provided with the exception of using the AMS namespace in the `'Name'` tag.

**Q: What are the prerequisites or dependencies to using AWS Service Catalog AppRegistry in my AMS account?**

There are no prerequisites or dependencies to use AppRegistry in your AMS account.
