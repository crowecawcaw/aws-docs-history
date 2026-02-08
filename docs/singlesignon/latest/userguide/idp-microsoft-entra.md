# Configure SAML and SCIM with Microsoft Entra ID and IAM Identity Center

AWS IAM Identity Center supports integration with [Security Assertion Markup Language (SAML) 2.0](scim-profile-saml.md "scim-profile-saml.md") as well as
[automatic
provisioning](provision-automatically.md "provision-automatically.md") (synchronization) of user and group information from Microsoft Entra ID (formerly
known as Azure Active Directory or Azure AD) into IAM Identity Center using the
[System for Cross-domain Identity
Management (SCIM) 2.0](scim-profile-saml.md#scim-profile "scim-profile-saml.md#scim-profile") protocol. For more information, see [Using SAML and SCIM identity federation with external identity
providers](other-idps.md "other-idps.md").

**Objective**

In this tutorial, you will set up a test lab and configure a SAML connection and SCIM
provisioning between Microsoft Entra ID and IAM Identity Center. During the initial preparation steps, you'll create a
test user (Nikki Wolf) in both Microsoft Entra ID and IAM Identity Center which you'll use to test the SAML connection in
both directions. Later, as part of the SCIM steps, you'll create a different test user (Richard
Roe) to verify that new attributes in Microsoft Entra ID are synchronizing to IAM Identity Center as expected.

## Prerequisites

Before you can get started with this tutorial, you'll first need to set up the
following:

- A Microsoft Entra ID tenant. For more information, see [Quickstart: Set up a tenant](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant "https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant") in Microsoft documentation.
- An AWS IAM Identity Center-enabled account. For more information, see [Enable IAM Identity Center](get-started-enable-identity-center.md "get-started-enable-identity-center.md") in the _AWS IAM Identity Center User Guide_.

## Considerations

The following are important considerations about Microsoft Entra ID that can affect how you plan to
implement [automatic provisioning](provision-automatically.md "provision-automatically.md") with IAM Identity Center in
your production environment using the SCIM v2 protocol.

Automatic Provisioning

Before you begin deploying SCIM, we recommend that you first review [Considerations for using automatic
provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations").

Attributes for access control

Attributes for access control is used in permission policies that determine who in your
identity source can access your AWS resources. If an attribute is removed from a user in
Microsoft Entra ID, that attribute will not be removed from the corresponding user in IAM Identity Center. This is a
known limitation in Microsoft Entra ID. If an attribute is changed to a different (non-empty) value on a
user, that change will be synchronized to IAM Identity Center.

Nested Groups

The Microsoft Entra ID user provisioning service cannot read or provision users in nested groups. Only
users that are immediate members of an explicitly assigned group can be read and provisioned.
Microsoft Entra ID doesn't recursively unpack the group memberships of indirectly assigned users or groups
(users or groups that are members of a group that is directly assigned). For more information,
see [Assignment-based scoping](https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/how-provisioning-works#assignment-based-scoping "https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/how-provisioning-works#assignment-based-scoping") in the Microsoft documentation.
Alternatively, you can use [IAM Identity Center configurable AD sync](https://aws.amazon.com/blogs//security/managing-identity-source-transition-for-aws-iam-identity-center/ "https://aws.amazon.com/blogs//security/managing-identity-source-transition-for-aws-iam-identity-center/") to integrate Active Directory groups with
IAM Identity Center.

Dynamic Groups

The Microsoft Entra ID user provisioning service can read and provision users in [dynamic groups](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-create-rule "https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-create-rule"). See below for an example showing the users and groups structure
while using dynamic groups and how they are displayed in IAM Identity Center. These users and groups were
provisioned from Microsoft Entra ID into IAM Identity Center via SCIM

For example, if Microsoft Entra ID structure for dynamic groups is as follows:

1. Group A with members ua1, ua2
2. Group B with members ub1
3. Group C with members uc1
4. Group K with a rule to include members of Group A, B, C
5. Group L with a rule to include members Group B and C

After the user and group information is provisioned from Microsoft Entra ID into IAM Identity Center through SCIM,
the structure will be as follows:

1. Group A with members ua1, ua2
2. Group B with members ub1
3. Group C with members uc1
4. Group K with members ua1, ua2, ub1, uc1
5. Group L with members ub1, uc1

When you configure automatic provisioning using dynamic groups, keep the following
considerations in mind.

- A dynamic group can include a nested group. However, Microsoft Entra ID provisioning service
  doesn’t flatten the nested group. For example, if you have the following Microsoft Entra ID structure
  for dynamic groups:
  - Group A is a parent of group B.
  - Group A has ua1 as a member.
  - Group B has ub1 as a member.

The dynamic group that includes Group A will only include the direct members of group A
(that is, ua1). It won’t recursively include members of group B.

- Dynamic groups can’t contain other dynamic groups. For more information, see [Preview limitations](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-dynamic-rule-member-of#preview-limitations "https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-dynamic-rule-member-of#preview-limitations") in the Microsoft documentation.

## Step 1: Prepare your Microsoft tenant

In this step, you will walk through how to install and configure your AWS IAM Identity Center enterprise
application and assign access to a newly created Microsoft Entra ID test user.

Step 1.1 >
**Step 1.1: Set up the AWS IAM Identity Center enterprise application in
Microsoft Entra ID**

In this procedure, you install the AWS IAM Identity Center enterprise application in Microsoft Entra ID. You
will need this application later to configure your SAML connection with AWS.

1. Sign in to the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") as at least a Cloud Application Administrator.
2. Navigate to **Identity > Applications > Enterprise
   applications**, and then choose **New
   application**.
3. On the **Browse Microsoft Entra Gallery** page, enter
   **`AWS IAM Identity Center`** in the search box.
4. Select **AWS IAM Identity Center** from the results.
5. Choose **Create**.

Step 1.2 >
**Step 1.2: Create a test user in Microsoft Entra ID**

Nikki Wolf is the name of your Microsoft Entra ID test user that you will create in this
procedure.

1. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Users > All
   users**.
2. Select **New user**, and then choose **Create new
   user** at the top of the screen.
3. In **User principal name**, enter
   **`NikkiWolf`**, and then select your
   preferred domain and extension. For example,
   _NikkiWolf_@`example.org`.
4. In **Display name**, enter
   **`NikkiWolf`**.
5. In **Password**, enter a strong password or select the eye icon
   to show the password that was auto-generated, and either copy or write down the
   value that is displayed.
6. Choose **Properties**, in **First name**,
   enter **`Nikki`**. In **Last
   name**, enter **`Wolf`**.
7. Choose **Review + create**, and then choose
   **Create**.

Step 1.3
**Step 1.3: Test Nikki's experience prior to assigning her
permissions to AWS IAM Identity Center**

In this procedure, you will verify what Nikki can successfully sign into her
Microsoft [My Account portal](https://myaccount.microsoft.com/ "https://myaccount.microsoft.com/").

1. In the same browser, open a new tab, go to the [My Account portal](https://myaccount.microsoft.com/ "https://myaccount.microsoft.com/") sign-in page, and
   enter Nikki's full email address. For example,
   _NikkiWolf_@`example.org`.
2. When prompted, enter Nikki's password, and then choose **Sign
   in**. If this was an auto-generated password, you will be prompted to
   change the password.
3. On the **Action Required** page, choose **Ask
   later** to bypass the prompt for additional security methods.
4. On the **My account** page, in the left navigation pane, choose
   **My Apps**. Notice that besides **Add-ins**, no
   apps are displayed at this time. You'll add an **AWS IAM Identity Center** app
   that will appear here in a later step.

Step 1.4
**Step 1.4: Assign permissions to Nikki in
Microsoft Entra ID**

Now that you have verified that Nikki can successfully access the **My
account portal**, use this procedure to assign her user to the
**AWS IAM Identity Center** app.

1. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Applications > Enterprise
   applications** and then choose **AWS IAM Identity Center** from the
   list.
2. On the left, choose **Users and groups**.
3. Choose **Add user/group**. You can ignore the message stating
   that groups are not available for assignment. This tutorial does not use groups for
   assignments.
4. On the **Add Assignment** page, under
   **Users**, choose **None Selected**.
5. Select **NikkiWolf**, and then choose
   **Select**.
6. On the **Add Assignment** page, choose
   **Assign**. NikkiWolf now appears in the list of users who are
   assigned to the **AWS IAM Identity Center** app.

## Step 2: Prepare your AWS account

In this step, you'll walk through how to use **IAM Identity Center** to configure access permissions (via permission set),
manually create a corresponding Nikki Wolf user, and assign her the necessary permissions to
administer resources in AWS.

Step 2.1 >
**Step 2.1: Create a RegionalAdmin permission set in
IAM Identity Center**

This permission set will be used to grant Nikki the necessary AWS account
permissions required to manage Regions from the **Account** page within
the AWS Management Console. All other permissions to view or manage any other information for Nikki's
account is denied by default.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Under **Multi-account permissions**, choose
   **Permission sets**.
3. Choose **Create permission set**.
4. On the **Select permission set type** page, select
   **Custom permission set**, and then choose
   **Next**.
5. Select **Inline policy** to expand it, and then create a policy
   for the permission set using the following steps:
   1. Choose **Add new statement** to create a policy
      statement.
   2. Under **Edit statement**, select
      **Account** from the list, and then choose the following
      checkboxes.
      - **`ListRegions`**
      - **`GetRegionOptStatus`**
      - **`DisableRegion`**
      - **`EnableRegion`**

   3. Next to **Add a resource**, choose
      **Add**.
   4. On the **Add resource** page, under **Resource
      type**, select **All Resources**, and then choose
      **Add resource**. Verify that your policy looks like the
      following:

   ```
   {
       "Statement": [
           {
               "Sid": "Statement1",
               "Effect": "Allow",
               "Action": [
                   "account:ListRegions",
                   "account:DisableRegion",
                   "account:EnableRegion",
                   "account:GetRegionOptStatus"
               ],
               "Resource": [
                   "*"
               ]
           }
       ]
   }
   ```

6. Choose **Next**.
7. On the **Specify permission set details** page, under
   **Permission set name**, enter
   **`RegionalAdmin`**, and then choose
   **Next**.
8. On the **Review and create** page, choose
   **Create**. You should see **RegionalAdmin**
   displayed in the list of permission sets.

Step 2.2 >
**Step 2.2: Create a corresponding NikkiWolf user in
IAM Identity Center**

Since the SAML protocol does not provide a mechanism to query the IdP (Microsoft Entra ID) and
automatically create users here in IAM Identity Center, use the following procedure to manually create
a user in IAM Identity Center that mirrors the core attributes from Nikki Wolfs user in Microsoft Entra ID.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Users**, choose **Add user**, and
   then provide the following information:
   1. For both **Username** and **Email
      address** – Enter the same
      **`NikkiWolf`@`yourcompanydomain.extension`**
      that you used when creating your Microsoft Entra ID user. For example,
      _NikkiWolf_@`example.org`.
   2. **Confirm email address** – Re-enter the email
      address from the previous step
   3. **First name** – Enter
      **`Nikki`**
   4. **Last name** – Enter
      **`Wolf`**
   5. **Display name** – Enter **`Nikki
Wolf`**

3. Choose **Next** twice, then choose **Add
   user**.
4. Select **Close**.

Step 2.3
**Step 2.3: Assign Nikki to the RegionalAdmin permission set in
IAM Identity Center**

Here you locate the AWS account in which Nikki will administer Regions, and then
assign the necessary permissions required for her to successfully access the
AWS access portal.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Under **Multi-account permissions**, choose
   **AWS accounts**.
3. Select the checkbox next to the account name (for example,
   `Sandbox`) where you want to grant Nikki access to manage
   Regions, and then choose **Assign users and groups**.
4. On the **Assign users and groups** page, choose the
   **Users** tab, find and check the box next to Nikki, and then
   choose **Next**.
5. On the **Select permission sets** page, choose
   the `RegionalAdmin` permission set created in Step 2.1, and then choose **Next**.
6. On the **Review and submit** page, review your selections and
   then choose **Submit**.

## Step 3: Configure and test your SAML connection

In this step, you configure your SAML connection using the AWS IAM Identity Center enterprise
application in Microsoft Entra ID together with the external IdP settings in IAM Identity Center.

Step 3.1 >
**Step 3.1: Collect required service provider metadata from
IAM Identity Center**

In this step, you will launch the **Change identity source** wizard
from within the IAM Identity Center console and retrieve the metadata file and the AWS specific
sign-in URL you'll need to enter when configuring the connection with Microsoft Entra ID in the next
step.

1. In the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon"), choose **Settings**.
2. On the **Settings** page, choose the **Identity
   source** tab, and then choose **Actions > Change identity
   source**.
3. On the **Choose identity source** page, select
   **External identity provider**, and then choose
   **Next**.
4. On the **Configure external identity provider** page, under
   **Service provider metadata**, choose **Default IPv4** or
   **Dual-stack**, then select **Download metadata
   file** to download the XML file.
5. In the same section, locate the **AWS access portal sign-in URL**
   value and copy it. You will need to enter this value when prompted in the next
   step.
6. Leave this page open, and move to the next step (**`Step 3.2`**) to configure the AWS IAM Identity Center enterprise
   application in Microsoft Entra ID. Later, you'll return to this page to complete the
   process.

Step 3.2 >

**Step 3.2: Configure the AWS IAM Identity Center enterprise application in
Microsoft Entra ID**

This procedure establishes one-half of the SAML connection on the Microsoft side
using the values from the metadata file and Sign-On URL you obtained in the last
step.

1. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Applications > Enterprise
   applications** and then choose **AWS IAM Identity Center**.
2. On the left, choose **2. Set up Single sign-on**.
3. On the **Set up Single Sign-On with SAML** page, choose
   **SAML**. Then choose **Upload metadata file**,
   choose the folder icon, select the service provider metadata file that you
   downloaded in the previous step, and then choose **Add**.
4. On the **Basic SAML Configuration** page, verify that both the
   **Identifier** and **Reply URL (Assertion Consumer Service URL)** values now
   point to endpoints in AWS.
   - **Identifier** - This is the **Issuer URL**
     from IAM Identity Center. The same value applies regardless of whether you use IPv4-only or
     dual-stack endpoints.
   - **Reply URL (Assertion Consumer Service URL)** - The values
     here include both IPv4-only and dual-stack endpoints from all enabled Regions of
     your IAM Identity Center. You can use the primary Region's ACS URL as the default one so that
     users are redirected to the primary Region when they launch the Amazon Web Services application from
     Microsoft Entra ID. For more information on ACS URLs, see [ACS endpoints in the primary and additional AWS Regions](multi-region-workforce-access.md#acs-endpoints "multi-region-workforce-access.md#acs-endpoints").
   - (Optional) If you replicated IAM Identity Center to additional Regions, you can also
     create a bookmark app in Microsoft Entra ID for the AWS access portal in each additional Region.
     This enables your users to access the AWS access portal in additional Regions from Microsoft Entra ID.
     Make sure to grant your users permissions to access the bookmark apps in Microsoft Entra ID.
     See [Microsoft Entra ID
     documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-linked-sign-on "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-linked-sign-on") for more details. If you plan to replicate IAM Identity Center to
     additional Regions later, visit [Microsoft Entra ID configuration for access
     to additional Regions](#gs-microsoft-entra-multi-region "#gs-microsoft-entra-multi-region") for guidance how
     to enable access to the additional Regions after this initial setup.

5. Under **Sign on URL (Optional)**, paste in the
   **AWS access portal sign-in URL** value you copied in the previous step
   (**`Step 3.1`**), choose
   **Save**, and then choose **X** to close the
   window.
6. If prompted to test single sign-on with AWS IAM Identity Center, choose **No I'll test
   later**. You will do this verification in a later step.
7. On the **Set up Single Sign-On with SAML** page, in the
   **SAML Certificates** section, next to **Federation
   Metadata XML**, choose **Download** to save the metadata
   file to your system. You will need to upload this file when prompted in the next
   step.

Step 3.3 >
**Step 3.3: Configure the Microsoft Entra ID external IdP in
AWS IAM Identity Center**

Here you will return to the **Change identity source** wizard in
the IAM Identity Center console to complete the second-half of the SAML connection in AWS.

1. Return to the browser session you left open from **`Step 3.1`** in the IAM Identity Center console.
2. On the **Configure external identity provider** page, in the
   **Identity provider metadata** section, under **IdP SAML
   metadata**, choose the **Choose file** button, and
   select the identity provider metadata file that you downloaded from Microsoft Entra ID in the
   previous step, and then choose **Open**.
3. Choose **Next**.
4. After you read the disclaimer and are ready to proceed, enter
   **`ACCEPT`**.
5. Choose **Change identity source** to apply your changes.

Step 3.4 >
**Step 3.4: Test that Nikki is redirected to the
AWS access portal**

In this procedure, you will test the SAML connection by signing in to Microsoft's
**My Account portal** with Nikki's credentials. Once authenticated,
you'll select the AWS IAM Identity Center application which will redirect Nikki to the
AWS access portal.

1. Go to the [My Account
   portal](https://myaccount.microsoft.com/ "https://myaccount.microsoft.com/") sign in page, and enter Nikki's full email address. For example,
   _`NikkiWolf`@_`example.org`.
2. When prompted, enter Nikki's password, and then choose **Sign
   in**.
3. On the **My account** page, in the left navigation pane, choose
   **My Apps**.
4. On the **My Apps** page, select the app named
   **AWS IAM Identity Center**. This should prompt you for additional
   authentication.
5. On Microsoft's sign in page, choose your NikkiWolf credentials. If prompted a
   second time for authentication, choose your NikkiWolf credentials again. This should
   automatically redirect you to the AWS access portal.

###### Tip

If you are not redirected successfully, check to make sure the
**AWS access portal sign-in URL** value you entered in **`Step 3.2`** matches the value you copied from
**`Step 3.1`**. 6. Verify that your AWS accounts display.

###### Tip

If the page is empty and no AWS accounts display, confirm that Nikki was
successfully assigned to the **RegionalAdmin** permission set
(see **`Step 2.3`**).

Step 3.5
**Step 3.5: Test Nikki's level of access to manage her
AWS account**

In this step, you will check to determine Nikki's level of access to manage the
Region settings for her AWS account. Nikki should only have sufficient administrator
privileges to manage Regions from the **Accounts** page.

1. In the AWS access portal, choose the **Accounts** tab to display the
   list of accounts. The account names, account IDs, and email addresses associated
   with any accounts where you've defined permission sets appear.
2. Choose the account name (for example, `Sandbox`) where
   you applied the permission set (see **`Step
2.3`**). This will expand the list of permission sets that Nikki
   can choose from to manage her account.
3. Next to **RegionalAdmin** choose **Management
   console** to assume the role you defined in the
   **RegionalAdmin** permission set. This will redirect you to the
   AWS Management Console home page.
4. In the upper-right corner of the console, choose your account name, and then
   choose **Account**. This will take you to the
   **Account** page. Notice that all other sections on this page
   display a message that you do not have the necessary permissions to view or modify
   those settings.
5. On the **Account** page, scroll down to the section
   **AWS Regions**. Select a checkbox for any available Region in
   the table. Notice that Nikki does have the necessary permissions to
   **Enable** or **Disable** the list of Regions
   for her account as was intended.

###### Nicely done!

Steps 1 through 3 helped you to successfully implement and test your SAML
connection. Now, to complete the tutorial, we encourage you to move on to Step 4 to
implement automatic provisioning.

## Step 4: Configure and test your SCIM

synchronization

In this step, you will set up [automatic
provisioning](provision-automatically.md "provision-automatically.md") (synchronization) of user information from Microsoft Entra ID into IAM Identity Center using the
SCIM v2.0 protocol. You configure this connection in Microsoft Entra ID using your SCIM endpoint for IAM Identity Center
and a bearer token that is created automatically by IAM Identity Center.

When you configure SCIM synchronization, you create a mapping of your user attributes in
Microsoft Entra ID to the named attributes in IAM Identity Center. This causes the expected attributes to match between
IAM Identity Center and Microsoft Entra ID.

The following steps walk you through how to enable automatic provisioning of users that
primarily reside in Microsoft Entra ID to IAM Identity Center using the IAM Identity Center app in Microsoft Entra ID.

Step 4.1 >
**Step 4.1: Create a second test user in
Microsoft Entra ID**

For testing purposes, you will create a new user (Richard Roe) in Microsoft Entra ID. Later,
after you set up SCIM synchronization, you will test that this user and all relevant
attributes were synced successfully to IAM Identity Center.

1. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Users > All
   users**.
2. Select **New user**, and then choose **Create new
   user** at the top of the screen.
3. In **User principal name**, enter
   **`RichRoe`**, and then select your
   preferred domain and extension. For example,
   _RichRoe_@`example.org`.
4. In **Display name**, enter
   **`RichRoe`**.
5. In **Password**, enter a strong password or select the eye icon
   to show the password that was auto-generated, and either copy or write down the
   value that is displayed.
6. Choose **Properties**, and then provide the following
   values:
   - **First name** - Enter
     **`Richard`**
   - **Last name** - Enter
     **`Roe`**
   - **Job title** - Enter **`Marketing
Lead`**
   - **Department** - Enter
     **`Sales`**
   - **Employee ID** - Enter
     **`12345`**

7. Choose **Review + create**, and then choose
   **Create**.

Step 4.2 >
**Step 4.2: Enable automatic provisioning in
IAM Identity Center**

In this procedure, you will use the IAM Identity Center console to enable automatic provisioning
of users and groups coming from Microsoft Entra ID into IAM Identity Center.

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon"), and choose **Settings** in the left navigation
   pane.
2. On the **Settings** page, under the **Identity
   source** tab, notice that **Provisioning method** is set
   to **Manual**.
3. Locate the **Automatic provisioning** information box, and then
   choose **Enable**. This immediately enables automatic provisioning
   in IAM Identity Center and displays the necessary SCIM endpoint and access token
   information.
4. In the **Inbound automatic provisioning** dialog box, copy each
   of the values for the following options. You will need to paste these in the next
   step when you configure provisioning in Microsoft Entra ID.
   1. **SCIM endpoint** - For example,
      - IPv4:
        `https://scim.`aws-region`.amazonaws.com/`11111111111-2222-3333-4444-555555555555`/scim/v2`
      - Dual stack:
        `https://scim.`aws-region`.api.aws/`11111111111-2222-3333-4444-555555555555`/scim/v2`

   2. **Access token** - Choose **Show token**
      to copy the value.###### Warning

This is the only time where you can obtain the SCIM endpoint and access token.
Ensure you copy these values before moving forward. 5. Choose **Close**. 6. Under the **Identity source** tab, notice that
**Provisioning method** is now set to
**SCIM**.

Step 4.3 >
**Step 4.3: Configure automatic provisioning in
Microsoft Entra ID**

Now that you have your RichRoe test user in place and have enabled SCIM in IAM Identity Center,
you can proceed with configuring the SCIM synchronization settings in Microsoft Entra ID.

1. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Applications > Enterprise
   applications** and then choose **AWS IAM Identity Center**.
2. Choose **Provisioning**, under **Manage**,
   choose **Provisioning** again.
3. In **Provisioning Mode** select
   **Automatic**.
4. Under **Admin Credentials**, in **Tenant URL**
   paste in the **SCIM endpoint** URL value you copied earlier in
   **`Step 4.2`**. In **Secret
   Token**, paste in the **Access token** value.
5. Choose **Test Connection**. You should see a message indicating
   that the tested credentials were successfully authorized to enable
   provisioning.
6. Choose **Save**.
7. Under **Manage**, choose **Users and groups**,
   and then choose **Add user/group**.
8. On the **Add Assignment** page, under
   **Users**, choose **None Selected**.
9. Select **RichRoe**, and then choose
   **Select**.
10. On the **Add Assignment** page, choose
    **Assign**.
11. Choose **Overview**, and then choose **Start
    provisioning**.

Step 4.4
**Step 4.4: Verify that synchronization
occurred**

In this section, you will verify that Richard's user was successfully provisioned
and that all attributes are displayed in IAM Identity Center.

1.  In the [IAM Identity Center
    console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon"), choose **Users**.
2.  On the **Users** page, you should see your
    **RichRoe** user displayed. Notice that in the **Created
    by** column the value is set to **SCIM**.
3.  Choose **RichRoe**, under **Profile**, verify
    that the following attributes were copied from Microsoft Entra ID.

        * **First name** -
         **`Richard`**
        * **Last name** -
         **`Roe`**
        * **Department** -
         **`Sales`**
        * **Title** - **`Marketing
         Lead`**
        * **Employee number** -
         **`12345`**

    Now that Richard's user has been created in IAM Identity Center, you can assign it to any
    permission set so you can control the level of access he has to your AWS
    resources. For example, you could assign **RichRoe** to the
    `RegionalAdmin` permission set you used earlier to grant
    Nikki the permissions to manage Regions (see **`Step
 2.3`**) and then test his level of access using **`Step 3.5`**.

###### Congratulations!

You have successfully set up a SAML connection between Microsoft and AWS and
have verified that automatic provisioning is working to keep everything in sync. Now
you can apply what you've learned to more smoothly set up your production environment.

## Step 5: Configure ABAC -

_Optional_

Now that you have successfully configured SAML and SCIM, you can optionally choose to
configure attribute-based access control (ABAC). ABAC is an authorization strategy that
defines permissions based on attributes.

With Microsoft Entra ID, you can use either of the following two methods to configure ABAC for use
with IAM Identity Center.

Configure user attributes in Microsoft Entra ID for access control in IAM Identity Center
**Configure user attributes in Microsoft Entra ID for access control in
IAM Identity Center**

In the following procedure, you will determine which attributes in Microsoft Entra ID should be
used by IAM Identity Center to manage access to your AWS resources. Once defined, Microsoft Entra ID sends these
attributes to IAM Identity Center through SAML assertions. You will then need to [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md") in IAM Identity Center
to manage access based on the attributes you passed from Microsoft Entra ID.

Before you begin this procedure, you first need to enable the [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md")
feature. For more information about how to do this, see [Enable and configure attributes for access
control](configure-abac.md "configure-abac.md").

1. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Applications > Enterprise
   applications** and then choose **AWS IAM Identity Center**.
2. Choose **Single sign-on**.
3. In the **Attributes & Claims** section, choose
   **Edit**.
4. On the **Attributes & Claims** page, do the
   following:
   1. Choose **Add new claim**
   2. For **Name**, enter
      `AccessControl:`AttributeName``. Replace
`AttributeName`with the name of the attribute you
are expecting in IAM Identity Center. For example,`AccessControl:**Department**`.
   3. For **Namespace**, enter
      **`https://aws.amazon.com/SAML/Attributes`**.
   4. For **Source**, choose **Attribute**.
   5. For **Source attribute**, use the drop-down list to choose
      the Microsoft Entra ID user attributes. For example,
      `user.**department**`.

5. Repeat the previous step for each attribute you need to send to IAM Identity Center in the
   SAML assertion.
6. Choose **Save**.

Configure ABAC using IAM Identity Center
**Configure ABAC using IAM Identity Center**

With this method, you use the [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md") feature in IAM Identity Center to pass an
`Attribute` element with the `Name` attribute set to
`https://aws.amazon.com/SAML/Attributes/AccessControl:`{TagKey}``.
You can use this element to pass attributes as session tags in the SAML assertion. For
more information about session tags, see [Passing session tags
in AWS STS](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") in the _IAM User Guide_.

To pass attributes as session tags, include the `AttributeValue` element
that specifies the value of the tag. For example, to pass the tag key-value pair
`Department=billing`, use the following attribute:

```
<saml:AttributeStatement>
<saml:Attribute Name="https://aws.amazon.com/SAML/Attributes/AccessControl:Department">
<saml:AttributeValue>billing
</saml:AttributeValue>
</saml:Attribute>
</saml:AttributeStatement>
```

If you need to add multiple attributes, include a separate `Attribute`
element for each tag.

## Assign access to AWS accounts

The following steps are only required to grant access to AWS accounts only. These steps
are not required to grant access to AWS applications.

###### Note

To complete this step, you'll need an Organization instance of IAM Identity Center. For more
information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

### Step 1: IAM Identity Center: Grant Microsoft Entra ID users access to

accounts

1.  Return to the **IAM Identity Center** console. In the IAM Identity Center navigation pane,
    under **Multi-account permissions**, choose
    **AWS accounts**.
2.  On the **AWS accounts** page the **Organizational
    structure** displays your organizational root with your accounts underneath
    it in the hierarchy. Select the checkbox for your management account, then select
    **Assign users or groups**.
3.  The **Assign users and groups** workflow displays. It consists of
    three steps:
    1.  For **Step 1: Select users and groups** choose the user that
        will be performing the administrator job function. Then choose
        **Next**.
    2.  For **Step 2: Select permission sets** choose **Create
        permission set** to open a new tab that steps you through the three
        sub-steps involved in creating a permission set.
        1.  For **Step 1: Select permission set type** complete the
            following:

                * In **Permission set type**, choose **Predefined
                 permission set**.
                * In **Policy for predefined permission set**, choose
                 **AdministratorAccess**.

            Choose **Next**.

        2.  For **Step 2: Specify permission set details**, keep the
            default settings, and choose **Next**.

        The default settings create a permission set named
        `AdministratorAccess` with session duration set to
        one hour. 3. For **Step 3: Review and create**, verify that the
        **Permission set type** uses the AWS managed policy
        **AdministratorAccess**. Choose **Create**.
        On the **Permission sets** page a notification appears
        informing you that the permission set was created. You can close this tab in
        your web browser now. 4. On the **Assign users and groups** browser tab, you are
        still on **Step 2: Select permission sets** from which you
        started the create permission set workflow. 5. In the **Permissions sets** area, choose the
        **Refresh** button. The
        `AdministratorAccess` permission set you created
        appears in the list. Select the checkbox for that permission set and then choose
        **Next**.

    3.  For **Step 3: Review and submit** review the selected user and
        permission set, then choose **Submit**.

    The page updates with a message that your AWS account is being configured.
    Wait until the process completes.

    You are returned to the AWS accounts page. A notification message informs you
    that your AWS account has been reprovisioned and the updated permission set
    applied. When the user sign in they will have the option of choosing the
    `AdministratorAccess` role.

### Step 2: Microsoft Entra ID: Confirm Microsoft Entra ID users access to

AWS resources

1. Return to the **Microsoft Entra ID** console and navigate to your IAM Identity Center
   SAML-based Sign-on application.
2. Select **Users and groups** and select **Add users or
   groups**. You’ll add the user you created in this tutorial in Step 4 to the
   Microsoft Entra ID application. By adding the user, you’ll allow them to sign-in to AWS. Search
   for the user you created at Step 4. If you followed this step, it would be
   `RichardRoe`.
   1. For a demo, see [Federate your existing
      IAM Identity Center instance with Microsoft Entra ID](https://youtu.be/iSCuTJNeN6c?si=29HSAK8DgBEhSVad "https://youtu.be/iSCuTJNeN6c?si=29HSAK8DgBEhSVad")

## Microsoft Entra ID configuration for access to

additional Regions of IAM Identity Center - Optional

If you replicated IAM Identity Center to additional Regions, you must update your identity provider
configuration to enable access to AWS managed applications and AWS accounts through the
additional Regions. The steps below guide you through the procedure. For more details about
this topic including the prerequisites, see [Using IAM Identity Center across multiple
AWS Regions](multi-region-iam-identity-center.md "multi-region-iam-identity-center.md").

1. Retrieve ACS URLs for the additional regions from the IAM Identity Center console as outlined in [ACS endpoints in the primary and additional AWS Regions](multi-region-workforce-access.md#acs-endpoints "multi-region-workforce-access.md#acs-endpoints").
2. In the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") console, navigate to **Identity > Applications > Enterprise
   applications** and then choose **AWS IAM Identity Center**.
3. On the left, choose **2. Set up Single sign-on**.
4. On the **Basic SAML Configuration** page, under **Reply URL
   (Assertion Consumer Service URL)** section, choose **Add
   reply URL** for each additiona Region's ACS URL. You can keep the primary
   Region's ACS URL as the default ones so that users keep getting redirected to the primary
   Region when they launch the AWS IAM Identity Center application from Microsoft Entra ID.
5. When done adding the ACS URLs, save the **AWS IAM Identity Center** application.
6. You can create a bookmark app in Microsoft Entra ID for the AWS access portal in each additional Region.
   This enables your users to access the AWS access portal in additional Regions from Microsoft Entra ID. Make
   sure to grant your users permissions to access the bookmark apps in Microsoft Entra ID. See [Microsoft Entra ID
   documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-linked-sign-on "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-linked-sign-on") for more details.
7. Verify that you can sign into the AWS access portal in each additional Region. Navigate to
   the [AWS access portal URLs](multi-region-workforce-access.md#portal-endpoints "multi-region-workforce-access.md#portal-endpoints") or launch the bookmark apps
   from Microsoft Entra ID.

## Troubleshooting

For general SCIM and SAML troubleshooting with Microsoft Entra ID, see the following sections:

- [Synchronization issues with Microsoft Entra ID and
  IAM Identity Center](#entra-scim-troubleshooting "#entra-scim-troubleshooting")
- [Specific users fail to synchronize into IAM Identity Center from an external SCIM
  provider](troubleshooting.md#issue2 "troubleshooting.md#issue2")
- [Issues regarding contents of SAML assertions created by IAM Identity Center](troubleshooting.md#issue1 "troubleshooting.md#issue1")
- [Duplicate user or group error when provisioning
  users or groups with an external identity provider](troubleshooting.md#duplicate-user-group-idp "troubleshooting.md#duplicate-user-group-idp")
- [Additional resources](#entra-scim-troubleshooting-resources "#entra-scim-troubleshooting-resources")

### Synchronization issues with Microsoft Entra ID and

IAM Identity Center

If you are experiencing issues with Microsoft Entra ID users not synchronizing to IAM Identity Center, it might be
due to a syntax issue that IAM Identity Center has flagged when a new user is being added to IAM Identity Center. You
can confirm this by checking the Microsoft Entra ID audit logs for failed events, such as an
`'Export'`. The **Status Reason** for this event will
state:

```
{"schema":["urn:ietf:params:scim:api:messages:2.0:Error"],"detail":"Request is unparsable, syntactically incorrect, or violates schema.","status":"400"}
```

You can also check AWS CloudTrail for the failed event. This can be done by searching in the
**Event History** console of CloudTrail using the following filter:

```
"eventName":"CreateUser"
```

The error in the CloudTrail event will state the following:

```
"errorCode": "ValidationException",
        "errorMessage": "Currently list attributes only allow single item“
```

Ultimately, this exception means that one of the values passed from Microsoft Entra ID contained
more values than anticipated. The solution is to review the attributes of the user in
Microsoft Entra ID, ensuring that none contain duplicate values. One common example of duplicate values
is having multiple values present for contact numbers such as **mobile**,
**work**, and **fax**. Although separate values, they
are all passed to IAM Identity Center under the single parent attribute
**phoneNumbers**.

For general SCIM troubleshooting tips, see [Troubleshooting](troubleshooting.md#issue2 "troubleshooting.md#issue2").

### Microsoft Entra ID Guest Account Synchronization

If you would like to sync your Microsoft Entra ID guest users to IAM Identity Center, see the following
procedure.

Microsoft Entra ID guest users’ email is different than Microsoft Entra ID users. This difference causes issues
when attempting to synchronize Microsoft Entra ID guest users with IAM Identity Center. For example, see the following
email address for a guest user:

`exampleuser_domain.com#EXT#@domain.onmicrosoft.com.`

IAM Identity Center does not expect the email address to contain the
`#EXT#@domain` format.

1. Sign in to the [Microsoft Entra admin
   center](https://entra.microsoft.com/ "https://entra.microsoft.com/") and navigate to **Identity** >
   **Applications** > **Enterprise applications** and
   then choose **AWS IAM Identity Center**
2. Navigate to the **Single Sign On** tab in the left pane.
3. Select **Edit** which appears next to **User Attributes
   & Claims**.
4. Select **Unique User Identifier (Name ID)** following
   **Required Claims**.
5. You will create two claim conditions for your Microsoft Entra ID users and guest users:
   1. For Microsoft Entra ID users, create a user type for members with source attribute set to
      `user.userprincipalname`.
   2. For Microsoft Entra ID guest users, create a user type for external guests with the source
      attribute set to `user.mail`.
   3. Select **Save** and retry signing in as a Microsoft Entra ID guest
      user.

### Additional resources

- For general SCIM troubleshooting tips, see [Troubleshooting IAM Identity Center issues](troubleshooting.md "troubleshooting.md").
- For Microsoft Entra ID troubleshooting, see [Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity/saas-apps/aws-single-sign-on-provisioning-tutorial#troubleshooting-tips "https://learn.microsoft.com/en-us/entra/identity/saas-apps/aws-single-sign-on-provisioning-tutorial#troubleshooting-tips").
- To learn more about federation across multiple AWS accounts, see [Securing AWS accounts with Azure Active Directory
  Federation](https://aws.amazon.com//blogs/apn/securing-aws-accounts-with-azure-active-directory-federation/ "https://aws.amazon.com//blogs/apn/securing-aws-accounts-with-azure-active-directory-federation/").

The following resources can help you troubleshoot as you work with AWS:

- [AWS re:Post](https://repost.aws/ "https://repost.aws/") - Find FAQs and links to other resources to help you troubleshoot issues.
- [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") - Get technical support
