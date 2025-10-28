# Get started with

AWS Private CA Connector for Active Directory

With AWS Private CA Connector for Active Directory, you can issue certificates from your private CA to your
Active Directory objects for authentication and encryption. When you create a connector,
AWS Private Certificate Authority creates an endpoint for you in your VPC for your directory objects to request
certificates.

To issue certificates, you create a connector and AD-compatible templates for the
connector. When you create a template, you can set enrollment permissions for your AD
groups.

###### Topics

- [Before you begin](#connector-for-ad-before-you-begin "#connector-for-ad-before-you-begin")
- [Step 1: Create a connector](#connector-for-ad-getting-started-step1 "#connector-for-ad-getting-started-step1")
- [Step 2: Configure Microsoft Active Directory
  policies](#connector-for-ad-getting-started-step2 "#connector-for-ad-getting-started-step2")
- [Step 3: Create a template](#connector-for-ad-getting-started-step3 "#connector-for-ad-getting-started-step3")
- [Step 4: Configure Microsoft group
  permissions](#connector-for-ad-getting-started-step4 "#connector-for-ad-getting-started-step4")

## Before you begin

The following tutorial guides you through the process of creating a connector for AD and a connector template. To follow this tutorial, you must first fulfill the prerequisites listed in the section.

## Step 1: Create a connector

To create a connector, see [Creating a connector for Active Directory](create-connector-for-ad.md "create-connector-for-ad.md").

## Step 2: Configure Microsoft Active Directory

policies

Connector for AD is unable to view or manage the customer's group
policy object (GPO) configuration. The GPO controls the routing of AD requests to
the customer's AWS Private CA or to other authentication or certificate vending servers.
An invalid GPO configuration may result in your requests being routed incorrectly.
It is up to customers to configure and test the Connector for AD
configuration.

Group Policies are associated with a Connector, and you may choose to create
multiple Connectors for a single AD. It is up to you to manage the access control to
each connector if its group policy configurations are different.

The security of the data plane calls depends on Kerberos and your VPC
configuration. Anyone with access to the VPC can make data plane calls as long as
they are authenticated to the corresponding AD. This exists outside of the boundary
of AWSAuth and managing authorization and authentication is up to you, the
customer.

When using AWS Managed Microsoft AD, use the AWS Directory Service **enable-ca-enrollment-policy** command to
configure GPOs on the domain controller of the AWS Managed Microsoft AD instance.

The following command enables enrolling domain controllers:

```
`$`  `aws ds enable-ca-enrollment-policy \
 --pca-connector-arn `MyPcaConnectorAdArn` \
 --directory-id `MyDirectoryId``
```

When using AD Connector, use the following steps to create a GPO that points to the URI
generated when you created a connector. This step is _required_
to use Connector for AD from the console or the command-line.

Configure GPOs.

1. Open **Server Manager** on the DC
2. Go to **Tools** and choose **Group Policy Management** in the upper right corner
   of the console.
3. Go to **Forest > Domains**. Select your
   domain name and right click on your domain. Select _Create a GPO in
   this domain, and link it here …_ and enter `PCA
GPO` for the name.
4. The newly created GPO will now be listed under your domain name.
5. Choose **PCA GPO** and select **Edit**. If a dialog box opens with the alert
   message _This is a link and that changes will be globally
   propagated_, acknowledge the message to continue. The
   **Group Policy Management Editor** should
   open.
6. In the **Group Policy Management Editor**, go
   to **Computer Configuration > Policies > Windows
   Settings > Security Settings > Public Key Policies (choose the
   folder)**.
7. Go to **object type** and choose **Certificate Services Client - Certificate Enrollment
   Policy**
8. In the options, change **Configuration
   Model** to **Enabled**.
9. Confirm that **Active Directory Enrollment
   Policy** is **checked** and
   **Enabled**. Choose **Add**.
10. The **Certificate Enrollment Policy Server**
    window should open.
11. Enter the certificate enrollment policy server endpoint that was generated
    when you created your connector in the **Enter
    enrollment server policy URI** field.
12. Leave the **Authentication Type** as
    **Windows integrated**.
13. Choose **Validate**. After validation succeeds, select **Add**. The dialog box closes.
14. Go back to **Certificate Services Client - Certificate
    Enrollment Policy** and check the box beside the newly created
    connector to ensure that the connector is the default enrollment
    policy
15. Choose **Active Directory Enrollment Policy**
    and select **Remove**.
16. In the confirmation dialog box, choose **Yes** to delete the LDAP-based authentication.
17. Choose **Apply** and **OK** on the \*\*Certificate Services Client
    > Certificate Enrollment Policy\*\* window and close
    > it.
18. Go to the **Public Key Policies** folder and
    choose **Certificate Services Client -
    Auto-Enrollment**.
19. Change the **Configuration Model** option to
    **Enabled**.
20. Confirm that **Renew expired certificates**
    and **Update Certificates** are both checked.
    Leave the other settings as they are.
21. Choose **Apply**, then **OK**, and close the dialogue box.

Configure the Public Key Policies for user configuration next. Go to **User Configuration > Policies > Windows Settings > Security
Settings > Public Key Policies**. Follow the procedures outlined
from step 6 to step 21 to configure the Public Key Policies for user
configuration.

Once you've finished configuring GPOs and Public Key Policies, objects in the
domain will request certificates from AWS Private CA Connector for AD and get
certificates issued by AWS Private CA.

## Step 3: Create a template

To create a template, see [Create a connector template](create-ad-template.md "create-ad-template.md").

## Step 4: Configure Microsoft group

permissions

To configure Microsoft group permissions, see [Manage Connector for AD template access control entries](ad-groups-permissions.md "ad-groups-permissions.md").
