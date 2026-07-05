Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Security best practices

Amazon Q Business provides several security features to consider as you develop and
implement your own security policies. The following best practices are general guidelines
and don't represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

## Apply principle of least privilege

Amazon Q provides a granular access policy for applications using IAM roles. We recommend that the roles be granted only the minimum set of
privileges required by the job, such as covering your application and access to log
destination. We also recommend auditing the jobs for permissions on a regular basis and
upon any change to your application.

## Role-based access control (RBAC) permissions

Administrators should strictly control role-based access control (RBAC) permissions
for Amazon Q applications.
