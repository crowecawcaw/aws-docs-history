# Understand licensing options and considerations for Microsoft SQL Server on Amazon EC2

There are two ways in which you can license Microsoft SQL Server on Amazon EC2 on the AWS Cloud. You acquire your own
existing SQL Server licenses, or those which are provided by AWS. The most cost-effective license
strategy for your workload will depend on multiple factors. For more information on comparing
the costs of SQL Server editions, see [Compare SQL Server editions](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-editions.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-editions.md") on the AWS Prescriptive Guidance website.

###### Topics

- [Licensing options](#sql-server-on-ec2-licensing-options "#sql-server-on-ec2-licensing-options")
- [Licensing
  considerations](#sql-server-on-ec2-licensing-considerations "#sql-server-on-ec2-licensing-considerations")
- [Amazon EC2 High Availability for SQL Server on Amazon EC2](sql-high-availability.md "sql-high-availability.md")

## Licensing options

You can launch Amazon Elastic Compute Cloud (Amazon EC2) instances with Microsoft SQL Server licenses included from AWS,
or you can bring your own SQL Server licenses for use on AWS. You can perform a license type
conversion for SQL Server in certain configurations if your needs change. For the most license
flexibility, you can import your VM into AWS. For more information, see [Eligible
license types for license type conversion](../../../license-manager/latest/userguide/conversion-types.md "../../../license-manager/latest/userguide/conversion-types.md") in the _AWS License Manager
User Guide_.

###### Licensing options topics

- [License-included](#sql-server-on-ec2-licensing-options-included "#sql-server-on-ec2-licensing-options-included")
- [BYOL](#sql-server-on-ec2-licensing-options-byol "#sql-server-on-ec2-licensing-options-byol")

### License-included

Windows Server with currently supported versions of Microsoft SQL Server AMIs are available
from AWS in a variety of combinations. AWS provides these AMIs with SQL Server software and
operating system updates already installed. When you purchase an Amazon EC2 instance with a
Windows Server AMI, licensing costs and compliance are handled for you. For more
information, see [Find a SQL Server license-included AMI](sql-server-on-ec2-amis.md "sql-server-on-ec2-amis.md").

Amazon EC2 offers a variety of instance types and sizes that you can configure for your
target workload. Amazon EC2 AMIs with Windows Server require no Client Access Licenses (CALs).
They also include two Microsoft Remote Desktop Services licenses for administrative
purposes.

For SQL Server license-included AMIs, use the installation and setup media included in
`C:\SQLServerSetup` to perform in-place SQL Server version upgrades, make changes
to the default installation, add new features, or install additional named
instances.

### BYOL

When you launch a SQL Server instance from an imported AMI, you can bring your existing
licenses with the Bring Your Own License model (BYOL), and let AWS manage them to ensure
compliance with licensing rules that you set. To import your own licensed image, you can
use a service such as [VM Import/Export](../../../vm-import/latest/userguide/what-is-vmimport.md "../../../vm-import/latest/userguide/what-is-vmimport.md") or [AWS Application Migration Service](../../../mgn/index.md "../../../mgn/index.md"). After you import your
licensed image, and it is available as a private AMI in your AWS account on the Amazon EC2
console, you can use the AWS License Manager service to create a license configuration.

After you create the license configuration, you must associate the AMI that contains
your licensed operating system image with the configuration. Then, you must create a host
resource group and associate it with the license configuration. After you associate your
host resource group with the configuration, License Manager automatically manages your hosts when
you launch instances into a host resource group, and ensures that you do not exceed your
configured license count limits. For more information, see the [Getting started](../../../license-manager/latest/userguide/getting-started.md "../../../license-manager/latest/userguide/getting-started.md")
section of the _License Manager User Guide_.

You can also bring your own SQL Server licenses with Active Software Assurance to default
(shared) tenant Amazon EC2 through Microsoft License Mobility through Software Assurance. For
information about how to sign up for Microsoft License Mobility, see [License
Mobility](https://aws.amazon.com/windows/resources/licensemobility/ "https://aws.amazon.com/windows/resources/licensemobility/").

## Licensing

considerations

There are many considerations for cost effectively licensing your Microsoft SQL Server on Amazon EC2
workload. Your use case, and existing license agreements, will determine whether to bring
your own license to AWS with the Bring Your Own License model (BYOL) or to use license
included AMIs from AWS. The following topics should help determine which approach you
might take. For more information, see [Licensing - SQL Server](https://aws.amazon.com/windows/faq/#licensing-sql-q "https://aws.amazon.com/windows/faq/#licensing-sql-q") on the _Amazon Web
Services and Microsoft Frequently Asked Questions_ page.

###### Licensing considerations topics

- [Choose a SQL Server
  edition](#sql-server-on-ec2-licensing-considerations-editions "#sql-server-on-ec2-licensing-considerations-editions")
- [Purchase SQL Server
  from AWS](#sql-server-on-ec2-licensing-considerations-purchasing "#sql-server-on-ec2-licensing-considerations-purchasing")
- [Use BYOL for SQL Server on
  AWS](#sql-server-on-ec2-licensing-considerations-byol "#sql-server-on-ec2-licensing-considerations-byol")
- [Quantify license requirements](#sql-server-on-ec2-licensing-considerations-quantify "#sql-server-on-ec2-licensing-considerations-quantify")
- [License Mobility
  with SQL Server](#sql-server-on-ec2-licensing-considerations-mobility "#sql-server-on-ec2-licensing-considerations-mobility")
- [Track BYOL license
  consumption](#sql-server-on-ec2-licensing-considerations-track "#sql-server-on-ec2-licensing-considerations-track")
- [SQL Server CALs](#sql-server-on-ec2-licensing-considerations-cals "#sql-server-on-ec2-licensing-considerations-cals")
- [Licensing for
  passive failover](#sql-server-on-ec2-licensing-considerations-failover "#sql-server-on-ec2-licensing-considerations-failover")

### Choose a SQL Server

edition

The edition of SQL Server that is used will determine the supported features your
implementation will have available. For example, the edition determines the maximum
compute capacity used by a single instance of the SQL Server Database Engine, and the high
availability options you might implement. For a comparison of SQL Server editions and
supported features, see [Editions and supported features of SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver16") in the Microsoft
documentation.

### Purchase SQL Server

from AWS

You can utilize Microsoft SQL Server licenses included from AWS. You can choose any of the
following editions for your use on Amazon EC2 instances.

- SQL Server Web
- SQL Server Standard
- SQL Server Enterprise

###### Note

- SQL Server Express AMIs are available for use from AWS. This free edition of SQL Server doesn’t incur
  additional charges as there is no licensing fee.
- SQL Server Developer edition is eligible for use in non-production, development, and
  test workloads. Once downloaded from Microsoft, you can bring and install SQL Server
  Developer edition on Amazon EC2 instances in the AWS Cloud. Dedicated infrastructure is
  not required for SQL Server Developer edition. For more information, see [https://www.microsoft.com/en-us/sql-server/sql-server-downloads](https://www.microsoft.com/en-us/sql-server/sql-server-downloads "https://www.microsoft.com/en-us/sql-server/sql-server-downloads").

### Use BYOL for SQL Server on

AWS

You can use BYOL licenses for SQL Server on AWS. The requirements differ depending on if
the licenses have active Software Assurance.

###### SQL Server licenses with active Software Assurance

You can bring your SQL Server licenses with active Software Assurance to default (shared)
tenant Amazon EC2 through License Mobility benefits. Microsoft requires that you complete and
send a License Mobility verification form which can be downloaded [here](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility?activetab=software-assurance-license-mobility-pivot%3aprimaryr2 "https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-license-mobility?activetab=software-assurance-license-mobility-pivot%3aprimaryr2"). For more information, see [License Mobility](https://aws.amazon.com/windows/resources/licensemobility/ "https://aws.amazon.com/windows/resources/licensemobility/").

###### SQL Server licenses without active Software Assurance

SQL Server licenses without Software Assurance can be deployed on Amazon Elastic Compute Cloud Dedicated Hosts
if the licenses are purchased prior to 10/1/2019 or added as a true-up under an active
Enterprise Enrollment that was effective prior to 10/1/2019. In these specific BYOL
scenarios, the licenses can only be upgraded to versions that were available prior to
10/1/2019. For more information, see [Dedicated Hosts](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md") in
the _Amazon EC2 User Guide_, and the [Amazon EC2 Dedicated Hosts FAQs](https://aws.amazon.com/ec2/dedicated-hosts/faqs/ "https://aws.amazon.com/ec2/dedicated-hosts/faqs/").

### Quantify the

required SQL Server licenses for BYOL

If you are licensing SQL Server under Microsoft License Mobility through Software
Assurance, the number of licenses required varies based on the instance type, version of
SQL Server, and the Microsoft licensing model you choose. For assistance with virtual core
licensing calculations under the Microsoft Product Terms based on the instance type, see
[SQL License
Mobility](https://aws.amazon.com/windows/resources/licensemobility/sql/ "https://aws.amazon.com/windows/resources/licensemobility/sql/").

If you are using Dedicated Hosts, Amazon EC2 provides you with the number of physical cores
installed on the Dedicated Host. Using this information, you can calculate the number of
SQL Server licenses that you need to bring in. For more information, see [Amazon EC2 Dedicated
Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/#host-configuration "https://aws.amazon.com/ec2/dedicated-hosts/pricing/#host-configuration") and the [SQL Server 2022 licensing guide](https://download.microsoft.com/download/9/3/d/93d32de6-f268-45ed-ba25-2f9a6756b6af/SQL_Server_2022_Licensing_guide.pdf "https://download.microsoft.com/download/9/3/d/93d32de6-f268-45ed-ba25-2f9a6756b6af/SQL_Server_2022_Licensing_guide.pdf").

### License Mobility

with SQL Server

SQL Server licenses with active Software Assurance are eligible for Microsoft License
Mobility and can be deployed on default or dedicated tenant Amazon EC2. For more information on
bringing SQL Server licenses with active Software Assurance to default tenant EC2, see [Microsoft License
Mobility](https://aws.amazon.com/windows/resources/licensemobility/ "https://aws.amazon.com/windows/resources/licensemobility/").

It is also possible to bring SQL Server licenses without active Software Assurance to EC2
Dedicated Hosts. To be eligible, the licenses must be purchased prior to October 1, 2019
or added as a true-up under an active Enterprise Enrollment that was effective prior to
October 1, 2019. For additional FAQs about Dedicated Hosts, see the [Dedicated Hosts](https://aws.amazon.com/windows/faq/#dedicated-hosts "https://aws.amazon.com/windows/faq/#dedicated-hosts") section of
the _Amazon Web Services and Microsoft FAQ_.

### Track BYOL license

consumption

You can use AWS License Manager to manage your software licenses for SQL Server. With License Manager, you can
create license configurations, take inventory of your license-consuming resources,
associate licenses with resources, and track inventory and compliance. For more
information, see [What is AWS License Manager?](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md")
in the _AWS License Manager User Guide_.

### SQL Server client access

licenses (CALs)

When you are using SQL Server on Amazon EC2, license included instances do not require client
access licenses (CALs) for SQL Server. An unlimited number of end users can access SQL Server on a
license-included instance.

When you bring your own SQL Server licenses to Amazon EC2 through Microsoft License Mobility or
BYOL, you must continue to follow the licensing rules in place on-premises. If you
purchased SQL Server under the Server/CAL model, you still require CALs to meet Microsoft
licensing requirements, but these CALs would remain on-premises and enable end user access
SQL Server running on AWS.

### Licensing for

passive failover

There are various factors to consider when licensing passive failover for SQL Server. The
information in this section pertains only to the SQL Server licenses and not the Windows Server
licenses. In all cases, you must license Windows Server.

###### Using instances that include the license for SQL Server

When you purchase SQL Server license included instances on EC2, you must license passive
failover instances.

###### Bringing SQL Server licenses with active Software Assurance to default tenant

Amazon EC2

When you bring SQL Server 2014 and later versions with Software Assurance to
default tenant EC2, you must license the virtual cores (vCPUs) on the active instance. In
return, Software Assurance permits one passive instance (equal or lesser
size) where SQL Server licensing is not required.

###### Bringing SQL Server to Amazon EC2 Dedicated Instances

SQL Server 2014 and later versions require Software Assurance for SQL Server passive failover
benefits on dedicated infrastructure. When you bring SQL Server with Software Assurance, you
must license the cores on the active instance/host and are permitted one passive
instance/host (equal or lesser size) where SQL Server licensing is not required.

SQL Server 2008 - SQL Server 2012R2 are eligible for passive failover on an Amazon EC2 Dedicated Hosts
infrastructure without active Software Assurance. In these scenarios, you will license the
active instance/host, and it will be permitted one passive instance/host of equal or
lesser size where SQL Server licensing is not required.

There are specific BYOL scenarios that do not require Microsoft License Mobility
through Software Assurance. An Amazon EC2 Dedicated Hosts infrastructure is always required in
these scenarios. To be eligible, the licenses must be purchased prior to October 1, 2019
or added as a true-up under an active Enterprise Enrollment that was effective prior to
October 1, 2019. In these specific BYOL scenarios, the licenses can only be upgraded to
versions that were available prior to October 1, 2019.
