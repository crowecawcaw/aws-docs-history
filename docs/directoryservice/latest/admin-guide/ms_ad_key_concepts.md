# AWS Managed Microsoft AD key concepts

You will get more out of AWS Managed Microsoft AD if you become familiar with the following key concepts.

###### Topics

- [Active Directory schema](#ms_ad_key_concepts_schema "#ms_ad_key_concepts_schema")
- [Patching and maintenance for
  AWS Managed Microsoft AD](#ms_ad_key_concepts_maintenance "#ms_ad_key_concepts_maintenance")
- [Group Managed Service Accounts](#ms_ad_key_concepts_gmsa "#ms_ad_key_concepts_gmsa")
- [Kerberos constrained delegation](#ms_ad_key_concepts_kerberos "#ms_ad_key_concepts_kerberos")

## Active Directory schema

A schema is the definition of attributes and classes that are part of a distributed
directory and is similar to fields and tables in a database. Schemas include a set of rules
which determine the type and format of data that can be added or included in the database. The
User class is one example of a _class_ that is stored in the
database. Some example of User class attributes can include the user's first name, last name,
phone number, and so on.

### Schema elements

Attributes, classes and objects are the basic elements that are used to build object
definitions in the schema. The following provides details about schema elements that are
important to know before you begin the process to extend your AWS Managed Microsoft AD schema.

**Attributes**

Each schema attribute, which is similar to a field in a database, has several
properties that define the characteristics of the attribute. For example, the property
used by LDAP clients to read and write the attribute is `LDAPDisplayName`.
The `LDAPDisplayName` property must be unique across all attributes and
classes. For a complete list of attribute characteristics, see [Characteristics
of Attributes](<https://msdn.microsoft.com/en-us/library/ms675578(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/ms675578(v=vs.85).aspx") on the MSDN website. For additional guidance on how to create a
new attribute, see [Defining a New
Attribute](<https://msdn.microsoft.com/en-us/library/ms675883(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/ms675883(v=vs.85).aspx") on the MSDN website.

**Classes**

The classes are analogous to tables in a database and also have several
properties to be defined. For example, the `objectClassCategory` defines the
class category. For a complete list of class characteristics, see [Characteristics
of Object Classes](<https://msdn.microsoft.com/en-us/library/ms675579(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/ms675579(v=vs.85).aspx") on the MSDN website. For more information about how to
create a new class, see [Defining a New
Class](<https://msdn.microsoft.com/en-us/library/ms675884(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/ms675884(v=vs.85).aspx") on the MSDN website.

**Object identifier (OID)**

Each class and attribute must have an OID that is unique for all of your objects.
Software vendors must obtain their own OID to ensure uniqueness. Uniqueness avoids
conflicts when the same attribute is used by more than one application for different
purposes. To ensure uniqueness, you can obtain a root OID from an ISO Name Registration
Authority. Alternatively, you can obtain a base OID from Microsoft. For more information
about OIDs and how to obtain them, see [Object
Identifiers](<https://msdn.microsoft.com/en-us/library/ms677614(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/ms677614(v=vs.85).aspx") on the MSDN website.

**Schema linked attributes**
Some attributes are linked between two classes with forward and back links. The best example
is groups. When you look at a group it shows you the members of the group; if you look
at a user you can see what groups it belongs to. When you add a user to a group, Active
Directory creates a forward link to the group. Then Active Directory adds a back link
from the group to the user. A unique link ID must be generated when creating an
attribute that will be linked. For more information, see [Linked
Attributes](<https://msdn.microsoft.com/en-us/library/ms677270(v=vs.85).aspx> "https://msdn.microsoft.com/en-us/library/ms677270(v=vs.85).aspx") on the MSDN website.

#### Related topics

- [When to extend your AWS Managed Microsoft AD schema](ms_ad_schema_extensions.md#ms_ad_schema_when_to_extend "ms_ad_schema_extensions.md#ms_ad_schema_when_to_extend")
- [Tutorial: Extending your AWS Managed Microsoft AD
  schema](ms_ad_tutorial_extend_schema.md "ms_ad_tutorial_extend_schema.md")

## Patching and maintenance for

AWS Managed Microsoft AD

AWS Directory Service for Microsoft Active Directory, also known as AWS DS for AWS Managed Microsoft AD, is actually Microsoft Active
Directory Domain Services (AD DS), delivered as a managed service. The system uses Microsoft
Windows Server 2019 for the domain controllers (DCs), and AWS adds software to the DCs for
service management purposes. AWS updates (patches) DCs to add new functionality and keep the
Microsoft Windows Server software current. During the patching process, your directory remains
available for use.

### Ensuring availability

By default each directory consists of two DCs, each installed in a different Availability
Zone. At your option, you may add DCs to further increase availability. For critical environments
needing high-availability and fault-tolerance, we recommend deploying additional DCs. AWS patches your DCs
sequentially, during which time the DC that AWS is actively patching is unavailable. In the
event that one or more of your DCs is temporarily out of service, AWS defers patching until
your directory has at least two operational DCs. This lets you use the other operating DCs
during the patch process, which typically takes 30 to 45 minutes per DC, although this time may
vary. To ensure your applications can reach an operating DC in the event that one or more DCs is
unavailable for any reason, including patching, your applications should use the Windows DC
locator service and not use static DC addresses.

### Understanding the patching schedule

To keep the Microsoft Windows Server software current on your DCs, AWS utilizes Microsoft
updates. As Microsoft makes monthly rollup patches available for Windows Server, AWS makes a
best effort to test and apply the rollup to all customer DCs within three calendar weeks. In
addition, AWS reviews updates that Microsoft releases outside of the monthly rollup based on
applicability to DCs and urgency. For security patches that Microsoft rates as
_Critical_ or _Important_, and that are relevant to DCs,
AWS makes every effort to test and deploy the patch within five days.

## Group Managed Service Accounts

With Windows Server 2012, Microsoft introduced a new method that administrators could use
to manage service accounts called group Managed Service Accounts (gMSAs). Using gMSAs, service
administrators no longer needed to manually manage password synchronization between service
instances. Instead, an administrator could simply create a gMSA in Active Directory and then
configure multiple service instances to use that single gMSA.

To grant permissions so users in AWS Managed Microsoft AD can create a gMSA, you must add their
accounts as a member of the _AWS Delegated Managed Service Account
Administrators_ security group. By default, the Admin account is a member of this
group. For more information about gMSAs, see [Group Managed
Service Accounts Overview](<https://technet.microsoft.com/en-us/library/hh831782(v=ws.11).aspx> "https://technet.microsoft.com/en-us/library/hh831782(v=ws.11).aspx") on the Microsoft TechNet website.

**Related AWS Security Blog post**

- [How AWS Managed Microsoft AD Helps to Simplify the Deployment and Improve the
  Security of Active Directory-Integrated .NET Applications](https://aws.amazon.com/blogs/security/how-aws-managed-microsoft-ad-helps-to-simplify-the-deployment-and-improve-the-security-of-active-directory-integrated-net-applications/ "https://aws.amazon.com/blogs/security/how-aws-managed-microsoft-ad-helps-to-simplify-the-deployment-and-improve-the-security-of-active-directory-integrated-net-applications/")

## Kerberos constrained delegation

Kerberos constrained delegation is a feature in Windows Server. This feature gives service
administrators the ability to specify and enforce application trust boundaries by limiting the
scope where application services can act on a user's behalf. This can be useful when you need
to configure which front-end service accounts can delegate to their backend services. Kerberos
constrained delegation also prevents your gMSA from connecting to any and all services on
behalf of your Active Directory users, avoiding the potential for abuse by a rogue
developer.

For example, let's say user jsmith logs into an HR application. You want the SQL Server to
apply jsmith's database permissions. However, by default SQL Server opens the database
connection using the service account credentials that apply hr-app-service's permissions
instead of jsmith's configured permissions. You must make it possible for the HR payroll
application to access the SQL Server database using the jsmith's credentials. To do that, you
enable Kerberos constrained delegation for the hr-app-service service account on your
AWS Managed Microsoft AD directory in AWS. When jsmith logs on, Active Directory provides a Kerberos
ticket that Windows automatically uses when jsmith attempts to access other services in the
network. Kerberos delegation enables the hr-app-service account to reuse the jsmith Kerberos
ticket when accessing the database, thus applying permissions specific to jsmith when opening
the database connection.

To grant permissions that allow users in AWS Managed Microsoft AD to configure Kerberos constrained
delegation, you must add their accounts as a member of the _AWS
Delegated Kerberos Delegation Administrators_ security group. By default, the
Admin account is a member of this group. For more information about Kerberos constrained
delegation, see [Kerberos
Constrained Delegation Overview](<https://technet.microsoft.com/en-us/library/jj553400(v=ws.11).aspx> "https://technet.microsoft.com/en-us/library/jj553400(v=ws.11).aspx") on the Microsoft TechNet website.

[Resource-based constrained delegation](https://docs.microsoft.com/en-us/windows-server/security/kerberos/kerberos-constrained-delegation-overview#resource-based-constrained-delegation-across-domains "https://docs.microsoft.com/en-us/windows-server/security/kerberos/kerberos-constrained-delegation-overview#resource-based-constrained-delegation-across-domains") was introduced with Windows Server 2012. It
provides the back-end service administrator the ability to configure constrained delegation for
the service.
