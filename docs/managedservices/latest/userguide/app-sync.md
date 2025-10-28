# Use AMS SSP to provision AWS AppSync

Use AMS Self-Service Provisioning (SSP) mode to access AWS AppSync capabilities directly in your AMS managed account. AWS AppSync simplifies application development by letting you create a flexible API to securely access,
manipulate, and combine data from one or more data sources. AWS AppSync is a managed service that uses
GraphQL to make it easy for applications to get exactly the data they need.

With AWS AppSync, you can build scalable applications, including those requiring real-time updates,
on a range of data sources such as NoSQL data stores, relational databases, HTTP APIs, and your
custom data sources with AWS Lambda. For mobile and web apps, AWS AppSync additionally provides local
data access when devices go offline, and data synchronization with customizable conflict resolution,
when they are back online.
To learn more, see
[AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/").

## AWS AppSync in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access AWS AppSync in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM roles to your account:
`customer_appsync_service_role` and `customer_appsync_author_role`.
Once provisioned in your account, you must onboard the `customer_appsync_author_role`
in your federation solution.

**Q: What are the restrictions to using the AWS AppSync?**

- When creating a Data Source on AppSync the customer need to
  specify the previously created service role, creation of a new role is not
  allowed and therefore will return an access denied
- AppSync roles are configured to restrict permissions to resources
  containing 'AMS-' or 'MC-' prefixes to prevent any modifications to AMS
  infrastructure.

**Q: What are the prerequisites or dependencies to using AWS AppSync?**

The service allows multiple other services to be used as a data source, The basic permissions to use
them as such is included in the service role (`customer_appsync_service_role`), but
you must manually select the service role when using the service.
