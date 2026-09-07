

# Set up SAML 2.0 for WorkSpaces Personal
<a name="setting-up-saml"></a>

Enable WorkSpaces client application registration and signing in to WorkSpaces for your users by using their SAML 2.0 identity provider (IdP) credentials and authentication methods by setting up identity federation using SAML 2.0. To set up identity federation using SAML 2.0, use an IAM role and a relay state URL to configure your IdP and enable AWS. This grants your federated users access to a WorkSpaces directory. The relay state is the WorkSpaces directory endpoint to which users are forwarded after successfully signing in to AWS. 

**Topics**
+ [Requirements](#setting-up-saml-requirements)
+ [Prerequisites](#setting-up-saml-prerequisites)
+ [Step 1: Create a SAML identity provider in AWS IAM](#create-saml-identity-provider)
+ [Step 2: Create a SAML 2.0 federation IAM role](#create-saml-iam-role)
+ [Step 3: Embed an inline policy for the IAM role](#embed-inline-policy)
+ [Step 4: Configure your SAML 2.0 identity provider](#configure-saml-id-provider)
+ [Step 5: Create assertions for the SAML authentication response](#create-assertions-saml-auth)
+ [Step 6: Configure the relay state of your federation](#configure-relay-state)
+ [Step 7: Enable integration with SAML 2.0 on your WorkSpaces directory](#enable-integration-saml)

## Requirements
<a name="setting-up-saml-requirements"></a>
+ SAML 2.0 authentication is available in the following Regions:
  + US East (N. Virginia) Region
  + US West (Oregon) Region
  + Africa (Cape Town) Region
  + Asia Pacific (Mumbai) Region
  + Asia Pacific (Seoul) Region
  + Asia Pacific (Singapore) Region
  + Asia Pacific (Sydney) Region
  + Asia Pacific (Tokyo) Region
  + Canada (Central) Region
  + Europe (Frankfurt) Region
  + Europe (Ireland) Region
  + Europe (London) Region
  + South America (São Paulo) Region
  + Israel (Tel Aviv) Region
  + AWS GovCloud (US-West)
  + AWS GovCloud (US-East)
+ To use SAML 2.0 authentication with WorkSpaces,the IdP must support unsolicited IdP-initiated SSO with a deep link target resource or relay state endpoint URL. Examples of IdPs include ADFS, Azure AD, Duo Single Sign-On, Okta, PingFederate, and PingOne. Consult your IdP documentation for more information.
+ SAML 2.0 authentication will function with WorkSpaces launched using Simple AD, but this isn't recommended as Simple AD doesn't integrate with SAML 2.0 IdPs.
+ SAML 2.0 authentication is supported on the following WorkSpaces clients. Other client versions are unsupported for SAML 2.0 authentication. Open Amazon WorkSpaces [Client Downloads](https://clients.amazonworkspaces.com/) to find the latest versions:
  + Windows client application version 5.1.0.3029 or later
  + macOS client version 5.x or later
  + Linux client for Ubuntu 22.04 version 2024.1 or later, Ubuntu 20.04 version 24.1 or later
  + Web Access

  Other client versions won't be able to connect to WorkSpaces enabled for SAML 2.0 authentication unless fallback is enabled. For more information, see [ Enable SAML 2.0 authentication on the WorkSpaces directory.](https://d1.awsstatic.com/workspaces-saml-guide.pdf)

For step-by-step instructions to integrate SAML 2.0 with WorkSpaces using ADFS, Azure AD, Duo Single Sign-On, Okta, OneLogin, PingFederate and PingOne for Enterprise, review the [Amazon WorkSpaces SAML Authentication Implementation Guide](https://d1.awsstatic.com/workspaces-saml-guide.pdf).

## Prerequisites
<a name="setting-up-saml-prerequisites"></a>

Complete the following prerequisites before configuring your SAML 2.0 identity provider (IdP) connection to a WorkSpaces directory.

1. Configure your IdP to integrate user identities from the Microsoft Active Directory that is used with the WorkSpaces directory. For a user with a WorkSpace, the **sAMAccountName** and **email** attributes for the Active Directory user and the SAML claim values must match for the user to sign in to WorkSpaces using the IdP. For more information about integrating Active Directory with your IdP, consult your IdP documentation.

1. Configure your IdP to establish a trust relationship with AWS.
   + See [Integrating third-party SAML solution providers with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.html) for more information on configuring AWS federation. Relevant examples include IdP integration with AWS IAM to access the AWS management console.
   + Use your IdP to generate and download a federation metadata document that describes your organization as an IdP. This signed XML document is used to establish the relying party trust. Save this file to a location that you can access from the IAM console later.

1. Create or register a directory for WorkSpaces by using the WorkSpaces management console. For more information, see [Manage directories for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html). SAML 2.0 authentication for WorkSpaces is supported for the following directory types:
   + AD Connector
   + AWS Managed Microsoft AD

1. Create a WorkSpace for a user who can sign in to the IdP using a supported directory type. You can create a WorkSpace using the WorkSpaces management console, AWS CLI, or WorkSpaces API. For more information, see [Launch a virtual desktop using WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html). 

## Step 1: Create a SAML identity provider in AWS IAM
<a name="create-saml-identity-provider"></a>

First, create a SAML IdP in AWS IAM. This IdP defines your organization's IdP-to-AWS trust relationship using the metadata document generated by the IdP software in your organization. For more information, see [ Creating and managing a SAML identity provider (Amazon Web Services Management Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html#idp-manage-identityprovider-console). For information about working with SAML IdPs in AWS GovCloud (US-West)and AWS GovCloud (US-East), see [AWS Identity and Access Management](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iam.html). 

## Step 2: Create a SAML 2.0 federation IAM role
<a name="create-saml-iam-role"></a>

Next, create a SAML 2.0 federation IAM role. This step establishes a trust relationship between IAM and your organization's IdP, which identifies your IdP as a trusted entity for federation.

To create an IAM role for SAML IdP

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles** > **Create role**.

1.  For **Role type**, choose **SAML 2.0 federation**. 

1.  For **SAML Provider** select the SAML IdP that you created. 
**Important**  
Don't choose either of the two SAML 2.0 access methods, **Allow programmatic access only** or **Allow programmatic and Amazon Web Services Management Console access**.

1. For **Attribute**, choose **SAML:sub\_type**.

1. For **Value** enter `persistent`. This value restricts role access to SAML user streaming requests that include a SAML subject type assertion with a value of persistent. If the SAML:sub\_type is persistent, your IdP sends the same unique value for the NameID element in all SAML requests from a particular user. For more information about the SAML:sub\_type assertion, see the **Uniquely identifying users in SAML-based federation** section in [ Using SAML-based federation for API access to AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html#CreatingSAML-configuring).

1. Review your SAML 2.0 trust information, confirming the correct trusted entity and condition, and then choose **Next: Permissions**. 

1. On the **Attach permissions policies** page, choose **Next: Tags**.

1. (Optional) Enter a key and value for each tag that you want to add. For more information, see [Tagging IAM users and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html).

1. When you're done, choose **Next: Review**. You'll create and embed an inline policy for this role later.

1. For **Role name**, enter a name that identifies the purpose of this role. Because multiple entities might reference the role, you can't edit the role's name once it is created.

1. (Optional) For **Role description**, enter a description for the new role.

1. Review the role details and choose **Create role**.

1. Add the sts:TagSession permission to your new IAM role's trust policy. For more information, see [Passing session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html). In your new IAM role's details, choose the **Trust relationships** tab, and then choose **Edit trust relationship\***. When Edit Trust Relationship policy editor opens, add the **sts:TagSession\*** permission, as follows:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Federated": "arn:aws:iam::{{111122223333}}:saml-provider/IDENTITY-PROVIDER"
               },
               "Action": [
                   "sts:AssumeRoleWithSAML",
                   "sts:TagSession"
               ],
               "Condition": {
                   "StringEquals": {
                       "SAML:aud": "https://signin.aws.amazon.com/saml"
                   }
               }
           }
       ]
   }
   ```

------

Replace `IDENTITY-PROVIDER` with the name of the SAML IdP you created in Step 1. Then choose **Update Trust Policy**.

## Step 3: Embed an inline policy for the IAM role
<a name="embed-inline-policy"></a>

Next, embed an inline IAM policy for the role that you created. When you embed an inline policy, the permissions in that policy can't be accidentally attached to the wrong principal entity. The inline policy provides federated users with access to the WorkSpaces directory.

**Important**  
IAM policies to manage access to AWS based on the source IP are not supported for the `workspaces:Stream` action. To manage IP access controls for WorkSpaces, use [IP access control groups](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html). Additionally, when using SAML 2.0 authentication you can use IP access control policies if they are available from your SAML 2.0 IdP.

1. In the details for the IAM role that you created, choose the **Permissions** tab, and then add required permissions to the role's permissions policy. The **Create policy wizard** will start.

1. In **Create policy**, choose the **JSON** tab.

1. Copy and paste the following JSON policy into the JSON window. Then, modify the resource by entering your AWS Region Code, account ID, and directory ID. In the following policy, `"Action": "workspaces:Stream"` is the action that provides your WorkSpaces users with permissions to connect to their desktop sessions in the WorkSpaces directory.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "workspaces:Stream",
               "Resource": "arn:aws:workspaces:us-east-1:123456789012:directory/DIRECTORY-ID",
               "Condition": {
                   "StringEquals": {
                       "workspaces:userId": "${saml:sub}"
                   }
               }
           }
       ]
   }
   ```

------

   Replace `REGION-CODE` with the AWS Region where your WorkSpaces directory exists. Replace `DIRECTORY-ID` with the WorkSpaces directory ID, which can be found in the WorkSpaces management console. For resources in AWS GovCloud (US-West) or AWS GovCloud (US-East), use the following format for the ARN: `arn:aws-us-gov:workspaces:REGION-CODE:ACCOUNT-ID-WITHOUT-HYPHENS:directory/DIRECTORY-ID`.

1. When you're done, choose **Review policy**. The [Policy Validator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html) will report any syntax errors.

## Step 4: Configure your SAML 2.0 identity provider
<a name="configure-saml-id-provider"></a>

Next, depending on your SAML 2.0 IdP, you may need to manually update your IdP to trust AWS as a service provider by uploading the `saml-metadata.xml` file at [https://signin.aws.amazon.com/static/saml-metadata.xml](https://signin.aws.amazon.com/static/saml-metadata.xml) to your IdP. This step updates your IdP’s metadata. For some IdPs, the update may already be configured. If this is the case, proceed to the next step.

If this update isn't already configured in your IdP, review the documentation provided by your IdP for information about how to update the metadata. Some providers give you the option to type the URL, and the IdP obtains and installs the file for you. Others require you to download the file from the URL and then provide it as a local file.

**Important**  
At this time, you can also authorize users in your IdP to access the WorkSpaces application you have configured in your IdP. Users who are authorized to access the WorkSpaces application for your directory don't automatically have a WorkSpace created for them. Likewise, users that have a WorkSpace created for them are not automatically authorized to access the WorkSpaces application. To successfully connect to a WorkSpace using SAML 2.0 authentication, a user must be authorized by the IdP and must have a WorkSpace created.

**Note**  
If your end users will frequently switch between multiple different WorkSpaces user identities while using the same SAML 2.0 identity provider (IdP), ensure that your IdP is configured to force authentication (ForceAuthn) at each login attempt. This prevents your IdP from reusing an existing SSO session, which may otherwise cause authentication failures when your users are switching to another WorkSpace. Refer to your IdP's documentation for guidance on enabling the ForceAuthn (or equivalent) setting.

## Step 5: Create assertions for the SAML authentication response
<a name="create-assertions-saml-auth"></a>

Next, configure the information that your IdP sends to AWS as SAML attributes in its authentication response. Depending on your IdP, this is already configured, skip this step and continue to [ Step 6: Configure the relay state of your federation](https://docs.aws.amazon.com/workspaces/latest/adminguide/setting-up-saml.html#configure-relay-state).

If this information isn't already configured in your IdP, provide the following:
+ **SAML Subject NameID** – The unique identifier for the user who is signing in. The value must match the WorkSpaces user name, and is typically the **sAMAccountName** attribute for the Active Directory user.
+ **SAML Subject Type** (with a value set to `persistent`) – Setting the value to `persistent` ensures that your IdP sends the same unique value for the `NameID` element in all SAML requests from a particular user. Make sure that your IAM policy includes a condition to only allow SAML requests with a SAML sub\_type set to `persistent`, as described in [ Step 2: Create a SAML 2.0 federation IAM role](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html#external-identity-providers-grantperms).
+ **`Attribute` element with the `Name` attribute set to `https://aws.amazon.com/SAML/Attributes/Role`** – This element contains one or more `AttributeValue` elements that list the IAM role and SAML IdP to which the user is mapped by your IdP. The role and IdP are specified as a comma-delimited pair of ARNs. An example of the expected value is `arn:aws:iam::ACCOUNTNUMBER:role/ROLENAME,arn:aws:iam::ACCOUNTNUMBER:saml-provider/PROVIDERNAME`.
+ **`Attribute` element with the `Name` attribute set to `https://aws.amazon.com/SAML/Attributes/RoleSessionName`** – This element contains one `AttributeValue` element that provides an identifier for the AWS temporary credentials that are issued for SSO. The value in the `AttributeValue` element must be between 2 and 64 characters long, can contain only alphanumeric characters, underscores, and the following characters: **\_ . : / = \+ - @**. It can't contain spaces. The value is typically an email address or a user principal name (UPN). It shouldn't be a value that includes a space, such as a user's display name.
+ **`Attribute` element with the `Name` attribute set to `https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email`** – This element contains one `AttributeValue` element that provides the email address of the user. The value must match the WorkSpaces user email address as defined in the WorkSpaces directory. Tag values may include combinations of letters, numbers, spaces, and **\_ . : / = \+ - @** characters. For more information, see [Rules for tagging in IAM and AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules) in the *IAM User Guide*.
+ **`Attribute` element with the `Name` attribute set to `https://aws.amazon.com/SAML/Attributes/PrincipalTag:UserPrincipalName` (optional)** – This element contains one `AttributeValue` element that provides the Active Directory `userPrincipalName` for the user who is signing in. The value must be provided in the format of `username@domain.com`. This parameter is used with certificate-based authentication as the Subject Alternative Name in the end user certificate. For more information, see Certificate-Based Authentication.
+ **`Attribute` element with the `Name` attribute set to `https://aws.amazon.com/SAML/Attributes/PrincipalTag:ObjectSid` (optional)** – This element contains one `AttributeValue` element that provides the Active Directory security identifier (SID) for the user who is signing in. This parameter is used with certificate-based authentication to enable strong mapping to the Active Directory user. For more information, see Certificate-Based Authentication.
+ **`Attribute` element with the `Name` attribute set to `https://aws.amazon.com/SAML/Attributes/PrincipalTag:ClientUserName` (optional)** – This element contains one `AttributeValue` element that provides an alternative user name format. Use this attribute if you have use cases that require user name formats such as `corp\username`, `corp.example.com\username`, or `username@corp.example.com` to login using the WorkSpaces client. Tag keys and values can include any combination of letters, numbers, spaces, and **\_ : / . \+ = @ -** characters. For more information, see [Rules for tagging in IAM and AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules) in the *IAM User Guide*. To claim `corp\username` or `corp.example.com\username` formats, replace **\\** with **/**in the SAML assertion.
+ **`Attribute`element with the `Name` attribute set to https://aws.amazon.com/SAML/Attributes/PrincipalTag:Domain (optional)** – This element contains one `AttributeValue` element that provides the Active Directory DNS fully qualified domain name (FQDN) for users signing in. This parameter is used with certificate-based authentication when the Active Directory `userPrincipalName` for the user contains an alternative suffix. The value must be provided in the `domain.com`, including any subdomains.
+ **`Attribute` element with the `Name` attribute set to https://aws.amazon.com/SAML/Attributes/SessionDuration (optional)** – This element contains one `AttributeValue` element that specifies the maximum amount of time that a federated streaming session for a user can remain active before reauthentication is required. The default value is 3600 seconds (60 minutes). For more information, see the [ SAML `SessionDurationAttribute`](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.html#saml_role-session-duration). 
**Note**  
Although `SessionDuration` is an optional attribute, we recommend that you include it in the SAML response. If you don't specify this attribute, the session duration is set to a default value of 3600 seconds (60 minutes). WorkSpaces desktop sessions are disconnected after their session duration expires.

For more information about how to configure these elements, see [ Configuring SAML assertions for the authentication response](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.html) in the *IAM User Guide*. For information about specific configuration requirements for your IdP, see your IdP's documentation.

## Step 6: Configure the relay state of your federation
<a name="configure-relay-state"></a>

Next, use your IdP to configure the relay state of your federation to point to the WorkSpaces directory relay state URL. After successful authentication by AWS, the user is directed to the WorkSpaces directory endpoint, defined as the relay state in the SAML authentication response.

The following is the relay state URL format:

```
https://relay-state-region-endpoint/sso-idp?registrationCode=registration-code
```

Construct your relay state URL from your WorkSpaces directory registration code and the relay state endpoint associated with the Region in which your directory is located. The registration code can be found in the WorkSpaces management console.

Optionally, if you are using cross-region redirection for WorkSpaces, you can substitute the registration code with the fully qualified domain name (FQDN) associated with directories in your primary and failover Regions. For more information, see [Cross-region redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html). When using cross-region redirection and SAML 2.0 authentication, both primary and failover directories need to be enabled for SAML 2.0 authentication and independently configured with the IdP, using the relay state endpoint associated with each Region. This will allow the FQDN to be configured correctly when users register their WorkSpaces client applications before signing in, and will allow users to authenticate during a failover event.

The following table lists the relay state endpoints for the Regions where WorkSpaces SAML 2.0 authentication is available.


**Regions where WorkSpaces SAML 2.0 authentication is available**  

| Region | Relay state endpoint | 
| --- | --- | 
| US East (N. Virginia) Region | +  workspaces.euc-sso.us-east-1.aws.amazon.com <br />+  (FIPS) workspaces.euc-sso-fips.us-east-1.aws.amazon.com  | 
| US West (Oregon) Region | +  workspaces.euc-sso.us-west-2.aws.amazon.com <br />+  (FIPS) workspaces.euc-sso-fips.us-west-2.aws.amazon.com  | 
| Africa (Cape Town) Region | workspaces.euc-sso.af-south-1.aws.amazon.com | 
| Asia Pacific (Mumbai) Region | workspaces.euc-sso.ap-south-1.aws.amazon.com | 
| Asia Pacific (Seoul) Region | workspaces.euc-sso.ap-northeast-2.aws.amazon.com | 
| Asia Pacific (Singapore) Region | workspaces.euc-sso.ap-southeast-1.aws.amazon.com | 
| Asia Pacific (Sydney) Region | workspaces.euc-sso.ap-southeast-2.aws.amazon.com | 
| Asia Pacific (Tokyo) Region | workspaces.euc-sso.ap-northeast-1.aws.amazon.com | 
| Canada (Central) Region | workspaces.euc-sso.ca-central-1.aws.amazon.com | 
| Europe (Frankfurt) Region | workspaces.euc-sso.eu-central-1.aws.amazon.com | 
| Europe (Ireland) Region | workspaces.euc-sso.eu-west-1.aws.amazon.com | 
| Europe (London) Region | workspaces.euc-sso.eu-west-2.aws.amazon.com | 
| South America (São Paulo) Region | workspaces.euc-sso.sa-east-1.aws.amazon.com | 
| Israel (Tel Aviv) Region | workspaces.euc-sso.il-central-1.aws.amazon.com | 
| AWS GovCloud (US-West) |  +  workspaces.euc-sso.us-gov-west-1.amazonaws-us-gov.com <br />+  (FIPS) workspaces.euc-sso-fips.us-gov-west-1.amazonaws-us-gov.com   For more information about, see [ Amazon WorkSpaces](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-workspaces.html) in the *AWS GovCloud (US) User Guide*.   | 
| AWS GovCloud (US-East) |  +  workspaces.euc-sso.us-gov-east-1.amazonaws-us-gov.com <br />+  (FIPS) workspaces.euc-sso-fips.us-gov-east-1.amazonaws-us-gov.com   For more information about, see [ Amazon WorkSpaces](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-workspaces.html) in the *AWS GovCloud (US) User Guide*.   | 

With an identity provider (IdP)-initiated flow, you can opt to specify the client you want to use for SAML 2.0 federation. To do so, specify either `native` or `web` at end of the relay state URL, after `&client=`. When the parameter is specified in a relay state URL, the corresponding sessions will automatically start in the specified client.

## Step 7: Enable integration with SAML 2.0 on your WorkSpaces directory
<a name="enable-integration-saml"></a>

You can use the WorkSpaces console to enable SAML 2.0 authentication on the WorkSpaces directory.

**To enable integration with SAML 2.0**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose on the Directory ID for your WorkSpaces.

1. Under **Authentication**, choose **Edit**.

1. Choose **Edit SAML 2.0 Identity Provider**.

1. Check **Enable SAML 2.0 authentication**.

1. For the **User Access URL** and **IdP deep link parameter name**, enter values that are applicable to your IdP and the application you have configured in Step 1. The default value for the IdP deep link parameter name is “RelayState“ if you omit this parameter. The following table lists user access URL and parameter names that are unique to various identity providers for applications.   
**Domains and IP addresses to add to your allow list**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/adminguide/setting-up-saml.html)

   The user access URL is usually defined by the provider for unsolicited IdP-initiated SSO. A user can enter this URL in a web browser to federate directly to the SAML application. To test the user access URL and parameter values for your IdP, choose **Test**. Copy and paste the test URL to a private window in your current browser or another browser to test the SAML 2.0 logon without disrupting your current AWS management console session. When IdP-initiated flow opens, you can register your WorkSpaces client. For more information, see [ Identity provider (IdP)-initiated flow](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-saml.html).

1. Manage fallback settings by checking or unchecking **Allow clients that do not support SAML 2.0 to login**. Enable this setting to continue providing your users access to WorkSpaces using client types or versions that do not support SAML 2.0 or if users need time to upgrade to the latest client version.
**Note**  
This setting allows users to bypass SAML 2.0 and log in using directory authentication using older client versions.

1. To use SAML with the web client, enable Web Access. For more information, see [Enable and configure Amazon WorkSpaces Web Access](https://docs.aws.amazon.com/workspaces/latest/adminguide/web-access.html).
**Note**  
PCoIP with SAML is not supported on Web Access.

1. Choose **Save**. Your WorkSpaces directory is now enabled with SAML 2.0 integration. You can use the IdP-initiated and client application-initiated flows to register WorkSpaces client applications and sign in to WorkSpaces.