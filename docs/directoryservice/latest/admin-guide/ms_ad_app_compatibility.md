# Application compatibility for

AWS Managed Microsoft AD

AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) is compatible with multiple AWS services and third-party
applications.

The following is a list of compatible AWS applications and services:

- Amazon Chime
- Amazon Connect
- Amazon EC2
- Quick Suite
- Amazon RDS
- WorkDocs
- Amazon WorkMail
- AWS Client VPN
- AWS IAM Identity Center
- AWS License Manager
- AWS Management Console
- FSx for Windows File Server
- WorkSpaces
  For more information, see [Enabling access to AWS applications and
  services for your AWS Managed Microsoft AD](ms_ad_enable_apps_services.md "ms_ad_enable_apps_services.md").

Due to the magnitude of custom and commercial off-the-shelf applications that use Active Directory, AWS does not and cannot perform formal or broad verification of third-party
application compatibility with AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). Although AWS works with
customers in an attempt to overcome any potential application installation challenges they might
encounter, we are unable to guarantee that any application is or will continue to be compatible
with AWS Managed Microsoft AD.

The following third-party applications are compatible with AWS Managed Microsoft AD:

- Active Directory-Based Activation (ADBA)
- Active Directory Certificate Services (AD CS): Enterprise Certificate Authority
- Active Directory Federation Services (AD FS)
- Active Directory Users and Computers (ADUC)
- Application Server (.NET)
- Microsoft Entra (formerly known as Azure Active Directory (Azure AD))
- Microsoft Entra Connect (formerly known as Azure Active Directory Connect)
- Distributed File System Replication (DFSR)
- Distributed File System Namespaces (DFSN)
- Microsoft Remote Desktop Services Licensing Server
- Microsoft SharePoint Server
- Microsoft SQL Server (including SQL Server Always On Availability Groups)
- Microsoft System Center Configuration Manager (SCCM) - The user deploying SCCM must be a
  member of the AWS Delegated System Management Administrators group.
- Microsoft Windows and Windows Server OS
- Office 365
  Note that not all configurations of these applications may be supported.

## Compatibility guidelines

Although applications may have configurations that are incompatible, application
deployment configurations can often overcome incompatibility. The following describes the most
common reasons for application incompatibility. Customers can use this information to
investigate compatibility characteristics of a desired application and identify potential
deployment changes.

- **Domain administrator or other privileged permissions
  –** Some applications state that you must install them as the domain
  administrator. Because AWS must retain exclusive control of this permission level in
  order to deliver Active Directory as a managed service, you cannot act as the domain
  administrator to install such applications. However, you can often install such
  applications by delegating specific, less privileged, and AWS supported permissions to
  the person who performs the installation. For more details on the precise permissions that
  your application requires, ask your application provider. For more information about
  permissions that AWS allows you to delegate, see [What gets created with your
  AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").
- **Access to privileged Active Directory containers –**
  Within your directory, AWS Managed Microsoft AD provides an Organizational Unit (OU) over which you
  have full administrative control. You do not have create or write permissions and may have
  limited read permissions to containers that are higher in the Active Directory tree than
  your OU. Applications that create or access containers for which you have no permissions
  might not work. However, such applications often have an ability to use a container that
  you create in your OU as an alternative. Check with your application provider to find ways
  to create and use a container in your OU as an alternative. For more information on
  your OU, see [What gets created with your
  AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").
- **Schema changes during the install workflow –** Some
  Active Directory applications require changes to the default Active Directory schema, and
  they may attempt to install those changes as part of the application installation
  workflow. Due to the privileged nature of schema extensions, AWS makes this possible by
  importing Lightweight Directory Interchange Format (LDIF) files through the Directory Service console,
  CLI, or SDK only. Such applications often come with an LDIF file that you can apply to the
  directory through the Directory Service schema update process. For more information about how the LDIF
  import process works, see [Tutorial: Extending your AWS Managed Microsoft AD
  schema](ms_ad_tutorial_extend_schema.md "ms_ad_tutorial_extend_schema.md"). You can install the application in a way
  to bypass the schema installation during the installation process.

## Known incompatible applications

The following lists commonly requested commercial off-the-shelf applications for which we
have not found a configuration that works with AWS Managed Microsoft AD. AWS updates this list from time
to time at its sole discretion as a courtesy to help you avoid unproductive efforts. AWS
provide this information without warranty or claims regarding current or future
compatibility.

- Active Directory Certificate Services (AD CS): Certificate Enrollment Web
  Service
- Active Directory Certificate Services (AD CS): Certificate Enrollment Policy Web
  Service
- Microsoft Exchange Server
- Microsoft Skype for Business Server
