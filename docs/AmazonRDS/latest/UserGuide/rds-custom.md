# Amazon RDS Custom

Amazon RDS Custom automates database administration tasks and operations. RDS Custom makes it
possible for you as a database administrator to access and customize your database
environment and operating system. With RDS Custom, you can customize to meet the requirements of
legacy, custom, and packaged applications.

For the latest webinars and blogs about RDS Custom, see [Amazon RDS Custom
resources](https://aws.amazon.com/rds/custom/resources/ "https://aws.amazon.com/rds/custom/resources/").

###### Topics

- [Addressing the challenge of database
  customization](#custom-intro.challenge "#custom-intro.challenge")
- [Management model and benefits for Amazon RDS Custom](#custom-intro.solution "#custom-intro.solution")
- [Amazon RDS Custom architecture](custom-concept.md "custom-concept.md")
- [Security in Amazon RDS Custom](custom-security.md "custom-security.md")
- [Working with RDS Custom for Oracle](working-with-custom-oracle.md "working-with-custom-oracle.md")
- [Working with RDS Custom for SQL Server](working-with-custom-sqlserver.md "working-with-custom-sqlserver.md")

## Addressing the challenge of database

customization

Amazon RDS Custom brings the benefits of Amazon RDS to a market that can't easily move to a fully
managed service because of customizations that are required with third-party
applications. Amazon RDS Custom saves administrative time, is durable, and scales with your
business.

If you need the entire database and operating system to be fully managed by AWS, we
recommend Amazon RDS. If you need administrative rights to the database and underlying
operating system to make dependent applications available, Amazon RDS Custom is the better
choice. If you want full management responsibility and simply need a managed compute
service, the best option is self-managing your commercial databases on Amazon EC2.

To deliver a managed service experience, Amazon RDS doesn't let you access the underlying
host. Amazon RDS also restricts access to some procedures and objects that require high-level
privileges. However, for some applications, you might need to perform operations as a
privileged operating system (OS) user.

For example, you might need to do the following:

- Install custom database and OS patches and packages.
- Configure specific database settings.
- Configure file systems to share files directly with their applications.

Previously, if you needed to customize your application, you had to deploy your database on-premises or on Amazon EC2. In this
case, you bear most or all of the responsibility for database management, as summarized in the following table.

| Feature                     | On-premises responsibility | Amazon EC2 responsibility | Amazon RDS responsibility |
| --------------------------- | -------------------------- | ------------------------- | ------------------------- |
| Application optimization    | Customer                   | Customer                  | Customer                  |
| Scaling                     | Customer                   | Customer                  | AWS                       |
| High availability           | Customer                   | Customer                  | AWS                       |
| Database backups            | Customer                   | Customer                  | AWS                       |
| Database software patching  | Customer                   | Customer                  | AWS                       |
| Database software install   | Customer                   | Customer                  | AWS                       |
| OS patching                 | Customer                   | Customer                  | AWS                       |
| OS installation             | Customer                   | Customer                  | AWS                       |
| Server maintenance          | Customer                   | AWS                       | AWS                       |
| Hardware lifecycle          | Customer                   | AWS                       | AWS                       |
| Power, network, and cooling | Customer                   | AWS                       | AWS                       |

When you manage database software yourself, you gain more control, but you're
also more prone to user errors. For example, when you make changes manually, you might
accidentally cause application downtime. You might spend hours checking every change to
identify and fix an issue. Ideally, you want a managed database service that automates
common DBA tasks, but also supports privileged access to the database and underlying
operating system.

## Management model and benefits for Amazon RDS Custom

Amazon RDS Custom is a managed database service for legacy, custom, and packaged applications
that require access to the underlying operating system and database environment. RDS Custom
automates setup, operation, and scaling of databases in the AWS Cloud while granting you
access to the database and underlying operating system. With this access, you can configure
settings, install patches, and enable native features to meet the dependent application's
requirements. With RDS Custom, you can run your database workload using the AWS Management Console or the
AWS CLI.

RDS Custom supports only the Oracle Database and Microsoft SQL Server DB engines.

###### Topics

- [Shared responsibility model in
  RDS Custom](#custom-intro.solution.shared "#custom-intro.solution.shared")
- [Support perimeter and
  unsupported configurations in RDS Custom](#custom-intro.solution.support-perimeter "#custom-intro.solution.support-perimeter")
- [Key benefits of RDS Custom](#custom-intro.solution.benefits "#custom-intro.solution.benefits")

### Shared responsibility model in

RDS Custom

With RDS Custom, you use the managed features of Amazon RDS, but you manage the host and
customize the OS as you do in Amazon EC2. You take on additional database management
responsibilities beyond what you do in Amazon RDS. The result is that you have more control
over database and DB instance management than you do in Amazon RDS, while still benefiting from RDS
automation.

Shared responsibility means the following:

1. You own part of the process when using an RDS Custom feature.

For example, in RDS Custom for Oracle, you control which Oracle database patches to use
and when to apply them to your DB instances. 2. You are responsible for making sure that any customizations to RDS Custom features
work correctly.

To help protect against invalid customization, RDS Custom has automation software
that runs outside of your DB instance. If your underlying Amazon EC2 instance becomes
impaired, RDS Custom attempts to resolve these problems automatically by either
rebooting or replacing the EC2 instance. The only user-visible change is a new
IP address. For more information, see [Amazon RDS Custom host replacement](custom-concept.md#custom-troubleshooting.host-problems "custom-concept.md#custom-troubleshooting.host-problems").

The following table details the shared responsibility model for different features of
RDS Custom.

| Feature                     | Amazon EC2 responsibility | Amazon RDS responsibility | RDS Custom for Oracle responsibility | RDS Custom for SQL Server responsibility |
| --------------------------- | ------------------------- | ------------------------- | ------------------------------------ | ---------------------------------------- |
| Application optimization    | Customer                  | Customer                  | Customer                             | Customer                                 |
| Scaling                     | Customer                  | AWS                       | Shared                               | Shared                                   |
| High availability           | Customer                  | AWS                       | AWS                                  | AWS                                      |
| Database backups            | Customer                  | AWS                       | Shared                               | AWS                                      |
| Database software patching  | Customer                  | AWS                       | Shared                               | AWS for RPEV, Customer for CEV1          |
| Database software install   | Customer                  | AWS                       | Shared                               | AWS for RPEV, Customer for CEV1          |
| OS patching                 | Customer                  | AWS                       | Customer                             | AWS for RPEV, Customer for CEV1          |
| OS installation             | Customer                  | AWS                       | Shared                               | AWS                                      |
| Server maintenance          | AWS                       | AWS                       | AWS                                  | AWS                                      |
| Hardware lifecycle          | AWS                       | AWS                       | AWS                                  | AWS                                      |
| Power, network, and cooling | AWS                       | AWS                       | AWS                                  | AWS                                      |

1 A custom engine version (CEV) is a binary volume snapshot
of a database version and Amazon Machine Image (AMI). An RDS provided engine version
(RPEV) is the default Amazon Machine Image (AMI) and Microsoft SQL Server
installation.

You can create an RDS Custom DB instance using Microsoft SQL Server. In this case:

- You can choose from two licensing models: License Included (LI) and Bring Your Own Media (BYOM).
- With LI, you don't need to purchase SQL Server licenses separately. AWS holds
  the license for the SQL Server database software.
- With BYOM, you provide and install your own Microsoft SQL Server binaries and licensing.

You can create an RDS Custom DB instance using Oracle Database. In this case, you do the
following:

- Manage your own media.

When using RDS Custom, you upload your own database installation files and
patches. You create a custom engine version (CEV) from these files. Then you can
create an RDS Custom DB instance by using this CEV.

- Manage your own licenses.

You bring your own Oracle Database licenses and manage licenses by
yourself.

### Support perimeter and

unsupported configurations in RDS Custom

RDS Custom provides a monitoring capability called the _support
perimeter_. This feature ensures that your host and database environment
are configured correctly. If you make a change that causes your DB instance to go outside the
support perimeter, RDS Custom changes the instance status to
`unsupported-configuration` until you manually fix the configuration
problems. For more information, see [RDS Custom support
perimeter](custom-concept.md#custom-troubleshooting.support-perimeter "custom-concept.md#custom-troubleshooting.support-perimeter").

### Key benefits of RDS Custom

With RDS Custom, you can do the following:

- Automate many of the same administrative tasks as Amazon RDS, including the following:
  - Lifecycle management of databases
  - Automated backups and point-in-time recovery (PITR)
  - Monitoring the health of RDS Custom DB instances and observing changes to the infrastructure, operating
    system, and database processes.
  - Notification or taking action to fix issues depending on
    disruption to the DB instance

- Install third-party applications.

You can install software to run custom applications and agents. Because you have privileged
access to the host, you can modify file systems to support legacy applications.

- Install custom patches.

You can apply custom database patches or modify OS packages on your RDS Custom DB instances.

- Stage an on-premises database before moving it to a fully managed service.

If you manage your own on-premises database, you can stage the database to
RDS Custom as-is. After you familiarize yourself with the cloud environment, you
can migrate your database to a fully managed Amazon RDS DB instance.

- Create your own automation.

You can create, schedule, and run custom automation scripts for reporting,
management, or diagnostic tools.
