# Key concepts and best practices for

AWS Managed Microsoft AD

You can get more out of your AWS Managed Microsoft AD by becoming familiar with key concepts and best
practices. Key concepts help you understand how AWS Managed Microsoft AD works. Key concepts include learning more
about Active Directory schema, patching schedule, and Group Managed Service Accounts. Active Directory schema includes
elements like attributes, classes, and objects that make up AWS Managed Microsoft AD. AWS patches your
AWS Managed Microsoft AD domain controllers with Microsoft updates on your behalf. You can also learn more about
group Managed Service Accounts (gMSAs) and use them with your AWS Managed Microsoft AD.

You can avoid problems with your AWS Managed Microsoft AD by considering best practices. Some of these
best practices include:

- When setting up your AWS Managed Microsoft AD, configuring the security groups to meet your needs,
  remember your administrator account ID and password, and enable conditional forwarder
  setting.
- When using your AWS Managed Microsoft AD, don't alter the organizational unit AWS created when
  the directory is created, monitor performance with tools like Amazon CloudWatch and Amazon SNS,
  and use SMB 2.x clients.
- When programming applications to work with AWS Managed Microsoft AD, use Windows DC locator
  service, load test changes before rolling them out to production environments, and use efficient LDAP
  queries to avoid significant CPU cycles in a domain controller.

###### Topics

- [AWS Managed Microsoft AD key concepts](ms_ad_key_concepts.md "ms_ad_key_concepts.md")
- [AWS Managed Microsoft AD best practices](ms_ad_best_practices.md "ms_ad_best_practices.md")
