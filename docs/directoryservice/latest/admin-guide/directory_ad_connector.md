# AD Connector

AD Connector is a directory gateway with which you can redirect directory requests to your
on-premises Microsoft Active Directory without caching any information in the cloud.
AD Connector comes in two sizes, small and large. A small AD Connector is designed for smaller organizations
and is intended to handle a low number of operations per second. A large AD Connector is designed for
larger organizations and is intended to handle a moderate to high number of operations per second.
You can spread application loads across
multiple AD Connectors to scale to your performance needs. There are no enforced user or
connection limits.

AD Connector does not support Active Directory transitive trusts. AD Connectors and your on-premises Active Directory domains have a 1-to-1 relationship.
That is, for each on-premises domain, including child domains in an Active Directory forest that you want to
authenticate against, you must create a unique AD Connector.

###### Note

AD Connector cannot be shared with other AWS accounts. If this is a requirement,
consider using AWS Managed Microsoft AD to [Share your AWS Managed Microsoft AD](ms_ad_directory_sharing.md "ms_ad_directory_sharing.md"). AD Connector is also not multi-VPC aware, which
means that AWS applications like [WorkSpaces](https://aws.amazon.com/workspaces "https://aws.amazon.com/workspaces")
are required to be provisioned into the same VPC as your AD Connector.

Once set up, AD Connector offers the following benefits:

- Your end users and IT administrators can use their existing corporate credentials to log
  on to AWS applications such as WorkSpaces, WorkDocs, or Amazon WorkMail.
- You can manage AWS resources like Amazon EC2 instances or Amazon S3 buckets through IAM
  role-based access to the AWS Management Console.
- You can consistently enforce existing security policies (such as password expiration,
  password history, and account lockouts) whether users or IT administrators are accessing
  resources in your on-premises infrastructure or in the AWS Cloud.
- You can use AD Connector to enable multi-factor authentication by integrating with
  your existing RADIUS-based MFA infrastructure to provide an additional layer of security
  when users access AWS applications.
  Continue reading the topics in this section to learn how to connect to a directory and make
  the most of AD Connector features.

###### Topics

- [Getting started with AD Connector](ad_connector_getting_started.md "ad_connector_getting_started.md")
- [Best practices for AD Connector](ad_connector_best_practices.md "ad_connector_best_practices.md")
- [Maintain your AD Connector directory](ad_connector_maintain.md "ad_connector_maintain.md")
- [Secure your AD Connector directory](ad_connector_security.md "ad_connector_security.md")
- [Monitor your AD Connector directory](ad_connector_monitor.md "ad_connector_monitor.md")
- [Access to AWS applications and services from AD Connector](ad_connector_manage_apps_services.md "ad_connector_manage_apps_services.md")
- [Ways to join an Amazon EC2 instance to your Active Directory](ad_connector_join_instance.md "ad_connector_join_instance.md")
- [AD Connector quotas](ad_connector_limits.md "ad_connector_limits.md")
- [Troubleshooting AD Connector](ad_connector_troubleshooting.md "ad_connector_troubleshooting.md")
