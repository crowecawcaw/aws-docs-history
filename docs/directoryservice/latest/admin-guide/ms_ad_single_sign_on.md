# Enabling single sign-on for AWS Managed Microsoft AD

AWS Directory Service provides the ability to allow your users to access WorkDocs from a computer joined
to the directory without having to enter their credentials separately.

Before you enable single sign-on, you need to take additional steps to enable your users
web browsers to support single sign-on. Users may need to modify their web browser settings to
enable single sign-on.

###### Note

Single sign-on only works when used on a computer that is joined to the Directory Service
directory. It cannot be used on computers that are not joined to the directory.

If your directory is an AD Connector directory and the AD Connector service account does not have the permission to add or remove its service principal name attribute, then for Steps 5 and 6 below, you have two options:

1. You can proceed and will be prompted for the username and password for a directory user that has this permission to add or remove the service principal name attribute on the AD Connector service account. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account permissions are not changed.
2. You can delegate permissions to allow the AD Connector service account to add or remove the service principal name attribute on itself, you can run the below PowerShell commands from a domain joined computer using an account that has permissions to modify the permissions on the AD Connector service account. The below command will give the AD Connector service account the ability to add and remove a service principal name attribute only for itself.

```
$AccountName = 'ConnectorAccountName'
# DO NOT modify anything below this comment.
# Getting Active Directory information.
Import-Module 'ActiveDirectory'
$RootDse = Get-ADRootDSE
[System.GUID]$ServicePrincipalNameGuid = (Get-ADObject -SearchBase $RootDse.SchemaNamingContext -Filter { lDAPDisplayName -eq 'servicePrincipalName' } -Properties 'schemaIDGUID').schemaIDGUID
# Getting AD Connector service account Information.
$AccountProperties = Get-ADUser -Identity $AccountName
$AclPath = $AccountProperties.DistinguishedName
$AccountSid = New-Object -TypeName 'System.Security.Principal.SecurityIdentifier' $AccountProperties.SID.Value
# Getting ACL settings for AD Connector service account.
$ObjectAcl = Get-ACL -Path "AD:\$AclPath"
# Setting ACL allowing the AD Connector service account the ability to add and remove a Service Principal Name (SPN) to itself
$AddAccessRule = New-Object -TypeName 'System.DirectoryServices.ActiveDirectoryAccessRule' $AccountSid, 'WriteProperty', 'Allow', $ServicePrincipalNameGUID, 'None'
$ObjectAcl.AddAccessRule($AddAccessRule)
Set-ACL -AclObject $ObjectAcl -Path "AD:\$AclPath"
```

###### To enable or disable single sign-on with WorkDocs

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, select the
   **Application management** tab.
4. In the **Application access
   URL** section, choose **Enable** to enable single sign-on for WorkDocs.

If you do not see the **Enable** button, you may need to first create
an Access URL before this option will be displayed. For more information about how to create
an access URL, see [Creating an access URL for AWS Managed Microsoft AD](ms_ad_create_access_url.md "ms_ad_create_access_url.md"). 5. In the **Enable Single Sign-On for this directory** dialog box, choose
**Enable**. Single sign-on is enabled for the directory. 6. If you later want to disable single sign-on with WorkDocs, choose
**Disable**, and then in the **Disable Single Sign-On for this
directory** dialog box, choose **Disable** again.

###### Topics

- [Single sign-on for IE and Chrome](#ie_sso "#ie_sso")
- [Single sign-on for Firefox](#firefox_sso "#firefox_sso")

## Single sign-on for IE and Chrome

To allow Microsoft Internet Explorer (IE) and Google Chrome browsers to
support single sign-on, the following tasks must be performed on the client computer:

- Add your access URL (e.g.,
  https://`<alias>`.awsapps.com) to the list of
  approved sites for single sign-on.
- Enable active scripting (JavaScript).
- Allow automatic logon.
- Enable integrated authentication.

You or your users can perform these tasks manually, or you can change these
settings using Group Policy settings.

###### Topics

- [Manual update for single sign-on on
  Windows](#ie_sso_manual_windows "#ie_sso_manual_windows")
- [Manual update for single sign-on on OS
  X](#chrome_sso_manual_mac "#chrome_sso_manual_mac")
- [Group policy settings for single sign-on](#ie_sso_gpo "#ie_sso_gpo")

### Manual update for single sign-on on

Windows

To manually enable single sign-on on a Windows computer, perform the following
steps on the client computer. Some of these settings may already be set
correctly.

###### To manually enable single sign-on for Internet Explorer and Chrome on

Windows

1. To open the **Internet Properties** dialog box,
   choose the **Start** menu, type `Internet Options` in
   the search box, and choose **Internet Options**.
2. Add your access URL to the list of approved sites for single sign-on
   by performing the following steps:
   1. In the **Internet Properties** dialog box,
      select the **Security** tab.
   2. Select **Local intranet** and choose
      **Sites**.
   3. In the **Local intranet** dialog box, choose
      **Advanced**.
   4. Add your access URL to the list of websites and choose
      **Close**.
   5. In the **Local intranet** dialog box, choose
      **OK**.

3. To enable active scripting, perform the following steps:
   1. In the **Security** tab of the
      **Internet Properties** dialog box, choose **Custom
      level**.
   2. In the **Security Settings - Local Intranet
      Zone** dialog box, scroll down to
      **Scripting** and select
      **Enable** under **Active
      scripting**.
   3. In the **Security Settings - Local Intranet
      Zone** dialog box, choose **OK**.

4. To enable automatic logon, perform the following steps:
   1. In the **Security** tab of the
      **Internet Properties** dialog box, choose **Custom
      level**.
   2. In the **Security Settings - Local Intranet
      Zone** dialog box, scroll down to **User
      Authentication** and select **Automatic
      logon only in Intranet zone** under
      **Logon**.
   3. In the **Security Settings - Local Intranet
      Zone** dialog box, choose **OK**.
   4. In the **Security Settings - Local Intranet
      Zone** dialog box, choose **OK**.

5. To enable integrated authentication, perform the following
   steps:
   1. In the **Internet Properties** dialog box,
      select the **Advanced** tab.
   2. Scroll down to **Security** and select
      **Enable Integrated Windows
      Authentication**.
   3. In the **Internet Properties** dialog box,
      choose **OK**.

6. Close and re-open your browser to have these changes take
   effect.

### Manual update for single sign-on on OS

X

To manually enable single sign-on for Chrome on OS X, perform the following
steps on the client computer. You will need administrator rights on your
computer to complete these steps.

###### To manually enable single sign-on for Chrome on OS X

1. Add your access URL to the [AuthServerAllowlist](https://chromeenterprise.google/policies/#AuthServerAllowlist "https://chromeenterprise.google/policies/#AuthServerAllowlist") policy by running the following
   command:

```
defaults write com.google.Chrome AuthServerAllowlist "https://`<alias>`.awsapps.com"
```

2. Open **System Preferences**, go to the
   **Profiles** panel, and delete the `Chrome
Kerberos Configuration` profile.
3. Restart Chrome and open chrome://policy in Chrome to
   confirm that the new settings are in place.

### Group policy settings for single sign-on

The domain administrator can implement Group Policy settings to make the
single sign-on changes on client computers that are joined to the domain.

###### Note

If you manage the Chrome web browsers on the computers in your domain with
Chrome policies, you must add your access URL to the [AuthServerAllowlist](https://chromeenterprise.google/policies/#AuthServerAllowlist "https://chromeenterprise.google/policies/#AuthServerAllowlist") policy. For more information about setting
Chrome policies, go to [Policy Settings in Chrome](https://source.chromium.org/chromium/chromium/src/+/main:docs/enterprise/add_new_policy.md "https://source.chromium.org/chromium/chromium/src/+/main:docs/enterprise/add_new_policy.md").

###### To enable single sign-on for Internet Explorer and Chrome using Group

Policy settings

1. Create a new Group Policy object by performing the following
   steps:
   1. Open the Group Policy Management tool, navigate to your domain
      and select **Group Policy Objects**.
   2. From the main menu, choose **Action** and
      select **New**.
   3. In the **New GPO** dialog box, enter a
      descriptive name for the Group Policy object, such as
      `IAM Identity Center Policy`, and leave **Source
      Starter GPO** set to **(none)**.
      Click **OK**.

2. Add the access URL to the list of approved sites for single sign-on by
   performing the following steps:
   1. In the Group Policy Management tool, navigate to your domain,
      select **Group Policy Objects**, open the context (right-click)
      menu for your IAM Identity Center policy, and choose **Edit**.
   2. In the policy tree, navigate to **User
      Configuration** > **Preferences**
      > **Windows Settings**.
   3. In the **Windows Settings** list, open the
      context (right-click) menu for **Registry** and choose
      **New registry item**.
   4. In the **New Registry Properties** dialog
      box, enter the following settings and choose **OK**:

   **Action**

   `Update`

   **Hive**

   `HKEY_CURRENT_USER`

   **Path**

   `Software\Microsoft\Windows\CurrentVersion\Internet
 Settings\ZoneMap\Domains\awsapps.com\`<alias>``

   The value for
   `<alias>` is derived
   from your access URL. If your access URL is
   `https://examplecorp.awsapps.com`,
   the alias is `examplecorp`, and the
   registry key will be
   `Software\Microsoft\Windows\CurrentVersion\Internet
 Settings\ZoneMap\Domains\awsapps.com\examplecorp`.

   **Value name**

   `https`

   **Value type**

   `REG_DWORD`

   **Value data**

   `1`

3. To enable active scripting, perform the following steps:
   1. In the Group Policy Management tool, navigate to your domain,
      select **Group Policy Objects**, open the context (right-click)
      menu for your IAM Identity Center policy, and choose **Edit**.
   2. In the policy tree, navigate to **Computer
      Configuration** > **Policies** >
      **Administrative Templates** >
      **Windows Components** > **Internet
      Explorer** > **Internet Control
      Panel** > **Security Page** >
      **Intranet Zone**.
   3. In the **Intranet Zone** list, open the
      context (right-click) menu for **Allow active scripting** and
      choose **Edit**.
   4. In the **Allow active scripting** dialog box,
      enter the following settings and choose **OK**:
      - Select the **Enabled** radio
        button.
      - Under **Options** set **Allow
        active scripting** to
        **Enable**.

4. To enable automatic logon, perform the following steps:
   1. In the Group Policy Management tool, navigate to your domain,
      select Group Policy Objects, open the context (right-click) menu for your SSO
      policy, and choose **Edit**.
   2. In the policy tree, navigate to **Computer
      Configuration** > **Policies** >
      **Administrative Templates** >
      **Windows Components** > **Internet
      Explorer** > **Internet Control
      Panel** > **Security Page** >
      **Intranet Zone**.
   3. In the **Intranet Zone** list, open the
      context (right-click) menu for **Logon options** and choose
      **Edit**.
   4. In the **Logon options** dialog box, enter
      the following settings and choose **OK**:
      - Select the **Enabled** radio
        button.
      - Under **Options** set **Logon
        options** to **Automatic logon only
        in Intranet zone**.

5. To enable integrated authentication, perform the following
   steps:
   1. In the Group Policy Management tool, navigate to your domain,
      select **Group Policy Objects**, open the context (right-click)
      menu for your IAM Identity Center policy, and choose **Edit**.
   2. In the policy tree, navigate to **User
      Configuration** > **Preferences**
      > **Windows Settings**.
   3. In the **Windows Settings** list, open the
      context (right-click) menu for **Registry** and choose
      **New registry item**.
   4. In the **New Registry Properties** dialog
      box, enter the following settings and choose **OK**:

   **Action**

   `Update`

   **Hive**

   `HKEY_CURRENT_USER`

   **Path**

   `Software\Microsoft\Windows\CurrentVersion\Internet
 Settings`

   **Value name**

   `EnableNegotiate`

   **Value type**

   `REG_DWORD`

   **Value data**

   `1`

6. Close the **Group Policy Management Editor** window
   if it is still open.
7. Assign the new policy to your domain by following these steps:
   1. In the Group Policy Management tree, open the context
      (right-click) menu for your domain and choose **Link an Existing
      GPO**.
   2. In the **Group Policy Objects** list, select
      your IAM Identity Center policy and choose **OK**.

These changes will take effect after the next Group Policy update on the
client, or the next time the user logs in.

## Single sign-on for Firefox

To allow Mozilla Firefox browser to support single sign-on, add your access URL
(e.g., https://`<alias>`.awsapps.com) to the list of approved
sites for single sign-on. This can be done manually, or automated with a script.

###### Topics

- [Manual update for single sign-on](#firefox_sso_manual "#firefox_sso_manual")
- [Automatic update for single sign-on](#firefox_sso_script "#firefox_sso_script")

### Manual update for single sign-on

To manually add your access URL to the list of approved sites in Firefox,
perform the following steps on the client computer.

###### To manually add your access URL to the list of approved sites in

Firefox

1. Open Firefox and open the `about:config` page.
2. Open the `network.negotiate-auth.trusted-uris`
   preference and add your access URL to the list of sites. Use a comma (,)
   to separate multiple entries.

### Automatic update for single sign-on

As a domain administrator, you can use a script to add your access URL to the
Firefox `network.negotiate-auth.trusted-uris` user preference
on all computers on your network. For more information, go to [https://support.mozilla.org/en-US/questions/939037](https://support.mozilla.org/en-US/questions/939037 "https://support.mozilla.org/en-US/questions/939037").
