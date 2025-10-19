# Configure SAML and SCIM with Google Workspace and IAM Identity Center

If your organization is using Google Workspace you can integrate your users from Google Workspace into IAM Identity Center to
 give them access to AWS resources. You can achieve this integration by changing your IAM Identity Center
 identity source from the default IAM Identity Center identity source to Google Workspace.

User information from Google Workspace is synchronized into IAM Identity Center using the [System for Cross-domain Identity
 Management (SCIM) 2.0 protocol](scim-profile-saml.md#scim-profile "scim-profile-saml.md#scim-profile"). For more information, see [Using SAML and SCIM identity federation with external identity
 providers](other-idps.md "other-idps.md").

You configure this connection in Google Workspace using your
 SCIM endpoint for IAM Identity Center and an IAM Identity Center bearer token. When you configure SCIM synchronization,
 you create a mapping of your user attributes in Google Workspace to the named attributes in IAM Identity Center. This
 mapping matches the expected user attributes between IAM Identity Center and Google Workspace. To do this, you need
 to set up Google Workspace as an identity provider and connect with your IAM Identity Center.

**Objective**

The steps in this tutorial help guide you through establishing the SAML connection between
 Google Workspace and AWS. Later, you will synchronize users from Google Workspace using SCIM. To verify
 everything is configured correctly, after completing the configuration steps you will
 sign-in as a Google Workspace user and verify access to AWS resources. Note that this tutorial is
 based on a small Google Workspace directory test environment. Directory structures such as groups and
 organization units aren't included in this tutorial. After completing this tutorial, your
 users will be able to access the AWS access portal with your Google Workspace credentials.

###### Note

To sign up for a free trial of Google Workspace visit [Google Workspace](https://workspace.google.com/ "https://workspace.google.com/") on Google's website.

If you haven't enabled IAM Identity Center yet, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").


## Considerations



* Before you configure SCIM provisioning between Google Workspace and IAM Identity Center, we
 recommend that you first review [Considerations for using automatic
 provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations").
* SCIM automatic synchronization from Google Workspace is currently limited to user
 provisioning. Automatic group provisioning is not supported at this time.
 Groups can be manually created with AWS CLI Identity Store [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/create-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/create-group.html") command or AWS Identity and Access Management (IAM) API [CreateGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateGroup.html "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateGroup.html"). Alternatively, you can use [ssosync](https://github.com/awslabs/ssosync "https://github.com/awslabs/ssosync") to synchronize
 Google Workspace users and groups into IAM Identity Center.
* Every Google Workspace user must have a **First name**,
 **Last name**, **Username** and
 **Display name** value specified.
* Each Google Workspace user has only a single value per data attribute, such as email
 address or phone number. Any users that have multiple values will fail to
 synchronize. If there are users that have multiple values in their
 attributes, remove the duplicate attributes before attempting to provision
 the user in IAM Identity Center. For example, only one phone number attribute can be
 synchronized, since the default phone number attribute is "work phone", use
 the "work phone" attribute to store the user's phone number, even if the
 phone number for the user is a home phone or a mobile phone.
* Attributes are still synchronized if the user is disabled in IAM Identity Center, but
 still active in Google Workspace.
* If there is an existing user in Identity Center directory with the same
 username and email, the user will be overwritten and synchronized using SCIM
 from Google Workspace.
* There are additional considerations when changing your identity source.
 For more information, see [Changing from IAM Identity Center to an external
 IdP](manage-your-identity-source-considerations.md#changing-from-idc-and-idp "manage-your-identity-source-considerations.md#changing-from-idc-and-idp").

## Step 1: Google Workspace: Configure the SAML application


1. Sign in to your **Google Admin console**
 using an account with super administrator privileges.
2. In the left navigation panel of your **Google Admin
 console**, choose **Apps** and then choose
 **Web and Mobile Apps**.
3. In the **Add app** dropdown list, select **Search
 for apps**.
4. In the search box enter **Amazon Web Services**, then select
 **Amazon Web Services (SAML)** app from the list.
5. On the **Google Identity Provider details -
 Amazon Web Services** page, you can do either of the following:


	1. Download IdP metadata.
	2. Copy the SSO URL, Entity ID URL, and Certificate
	 information.You will need either the XML file or URL information in Step 2.
6. Before moving to the next step in the Google Admin console,
 leave this page open and move to the IAM Identity Center console.

## Step 2: IAM Identity Center and Google Workspace: Change the IAM Identity Center identity
 source and setup Google Workspace as an SAML identity provider


1. Sign in to the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon") using a role with administrative
 permissions.
2. Choose **Settings** in the left navigation pane.
3. On the **Settings** page, choose
 **Actions**, and then choose **Change identity
 source**.




	* If you haven't enabled IAM Identity Center, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md") for more information. After
	 enabling and accessing IAM Identity Center for the first time, you will arrive at
	 the **Dashboard** where you can select
	 **Choose your identity source**.
4. On the **Choose identity source** page, select
 **External identity provider**, and then choose
 **Next**.
5. The **Configure external identity provider** page opens.
 To complete this page and the Google Workspace page in Step 1, you will need to
 complete the following:


	1. Under **Identity Provider metadata** section in
	 the **IAM Identity Center** console, you will need to do either
	 of the following:
	
	
		1. Upload the **Google SAML
		 metadata** as the **IdP SAML
		 metadata** in the IAM Identity Center console.
		2. Copy and paste the **Google SSO
		 URL** into the **IdP Sign-in
		 URL** field, **Google
		 Issuer URL** into the **IdP issuer
		 URL** field, and upload the
		 **Google
		 Certificate** as the **IdP
		 certificate**.
6. After providing the Google metadata in the
 **Identity Provider metadata** section of the
 **IAM Identity Center** console, copy the **IAM Identity
 Assertion Consumer Service (ACS) URL** and **IAM Identity Center
 issuer URL**. You will need to provide these URLs in the
 Google Admin console in the next step.
7. Leave the page open with the IAM Identity Center console and return to the
 Google Admin console. You should be on the
 **Amazon Web Services - Service Provider details** page. Select
 **Continue**.
8. On the **Service provider details** page, enter the
 **ACS URL** and **Entity ID** values.
 You copied these values in the previous step and they can be found in the
 IAM Identity Center console.




	* Paste the **IAM Identity Center Assertion Consumer Service (ACS)
	 URL** into the **ACS URL**
	 field
	* Paste the **IAM Identity Center issuer URL** into the
	 **Entity ID** field.
9. On the **Service provider details** page, complete the
 fields under **Name ID** as follows:




	* For **Name ID format**, select
	 **EMAIL**
	* For **Name ID**, select **Basic
	 Information > Primary email**
10. Choose **Continue**.
11. On the **Attribute Mapping** page, under
 **Attributes**, choose **ADD
 MAPPING**, and then configure these fields under
 **Google Directory
 attribute**:




	* For the
	 `https://aws.amazon.com/SAML/Attributes/RoleSessionName`
	**app attribute**, select the field **Basic
	 Information, Primary Email** from the
	 **Google Directory
	 attributes**.
	* For the `https://aws.amazon.com/SAML/Attributes/Role`
	**app attribute**, select any
	 **Google Directory
	 attributes**. A Google Directory
	 attribute could be **Department**.
12. Choose **Finish**
13. Return to the **IAM Identity Center** console and choose
 **Next**. On the **Review and
 Confirm** page, review the information and then enter
 **ACCEPT** into the space provided. Choose
 **Change identity source.**

You are now ready to enable the Amazon Web Services app in Google Workspace so that your users can be
 provisioned into IAM Identity Center.


## Step 3: Google Workspace: Enable the apps


1. Return to the **Google Admin Console** and
 your AWS IAM Identity Center application which can be found under **Apps**
 and **Web and Mobile Apps**.
2. In the **User access** panel next to **User
 access**, choose the down arrow to expand **User
 access** to display the **Service status**
 panel.
3. In **Service status** panel, choose **ON for
 everyone**, and then choose **SAVE**.

###### Note

To help maintain the principle of least privilege, we recommend that after you
 complete this tutorial you change the **Service status** to
 **OFF for everyone**. Only users that need access to AWS
 should have the service enabled. You can use Google Workspace groups or organizational
 units to give user access to a particular subset of your users.


## Step 4: IAM Identity Center: Set up IAM Identity Center automatic
 provisioning


1. Return to the IAM Identity Center console.
2. On the **Settings** page, locate the **Automatic
 provisioning** information box, and then choose
 **Enable**. This immediately enables automatic
 provisioning in IAM Identity Center and displays the necessary SCIM endpoint and access
 token information.
3. In the **Inbound automatic provisioning** dialog box,
 copy each of the values for the following options. In Step 5 of this
 tutorial, you will enter these values to configure automatic provisioning in
 Google Workspace.


	1. **SCIM endpoint** - For example,
	 https://scim.`us-east-2`.amazonaws.com/`11111111111-2222-3333-4444-555555555555`/scim/v2
	2. **Access token** - Choose **Show
	 token** to copy the value.###### Warning

This is the only time where you can obtain the SCIM endpoint and
 access token. Ensure you copy these values before moving forward.
4. Choose **Close**.


Now that you've set up provisioning in the IAM Identity Center console, in the next step
 you will configure auto provisioning in Google Workspace.

## Step 5:
 Google Workspace: Configure auto provisioning


1. Return to the Google Admin console and your AWS IAM Identity Center
 application which can be found under **Apps** and
 **Web and Mobile apps**. In the **Auto
 provisioning** section, choose **Configure auto
 provisioning**.
2. In the previous procedure, you copied the **Access
 token** value in IAM Identity Center console. Paste that value into the
 **Access token** field and choose
 **Continue**. Also, in the previous procedure, you
 copied the **SCIM endpoint** value in IAM Identity Center console. Paste
 that value into the **Endpoint URL** field and choose
 **Continue**.
3. Verify that all mandatory IAM Identity Center attributes (those marked with \*) are
 mapped to Google Cloud Directory attributes. If not, choose
 the down arrow and map to the appropriate attribute. Choose
 **Continue**.
4. In **Provisioning scope** section, you can choose a group
 with your Google Workspace directory to provide access to the Amazon Web Services app. Skip this
 step and select **Continue**.
5. In **Deprovisioning** section, you can choose how to
 respond to different events that remove access from a user. For each
 situation you can specify the amount of time before deprovisioning begins
 to:




	* within 24 hours
	* after one day
	* after seven days
	* after 30 days
Each situation has a time setting for when to suspend an account's access
 and when to delete the account.


###### Tip

Always set more time before deleting a user's account than for
 suspending a user's account.
6. Choose **Finish.** You are returned to the Amazon Web Services app
 page.
7. In the **Auto-provisioning** section, turn on the toggle
 switch to change it from **Inactive** to
 **Active**. 


###### Note

The activation slider is disabled if IAM Identity Center isn’t turned on for users.
 Choose **User access** and turn the app on to enable
 the slider.
8. In the confirmation dialog box, choose **Turn
 on**.
9. To verify that users are successfully synchronized to IAM Identity Center, return to the
 IAM Identity Center console and choose **Users**.
 The **Users** page lists the users from your Google Workspace
 directory that were created by SCIM. If users aren't listed yet, it might be
 that provisioning is still in process. Provisioning can take up to 24 hours,
 although in most cases it completes within minutes. Make sure to refresh the
 browser window every few minutes.


Select a user and view their details. The information should match the
 information in the Google Workspace directory.

###### Congratulations!

You have successfully set up a SAML connection between Google Workspace and AWS and
 have verified that automatic provisioning is working. You can now assign these
 users to accounts and applications in **IAM Identity Center**.
 For this tutorial, in the next step let's designate one of the users as the
 IAM Identity Center administrator by granting them administrative permissions to the
 management account.


## Passing attributes for access
 control - *Optional*


You can optionally use the [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md") feature in IAM Identity Center to pass an
 `Attribute` element with the `Name` attribute set to
 `https://aws.amazon.com/SAML/Attributes/AccessControl:`{TagKey}``.
 This element allows you to pass attributes as session tags in the SAML assertion. For more
 information about session tags, see [Passing session tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html") in the *IAM User Guide*.


To pass attributes as session tags, include the `AttributeValue` element that
 specifies the value of the tag. For example, to pass the tag key-value pair
 `CostCenter = blue`, use the following attribute.



```
<saml:AttributeStatement>
<saml:Attribute Name="https://aws.amazon.com/SAML/Attributes/AccessControl:CostCenter">
<saml:AttributeValue>blue
</saml:AttributeValue>
</saml:Attribute>
</saml:AttributeStatement>
```

If you need to add multiple attributes, include a separate `Attribute`
 element for each tag. 


## Assign access to AWS accounts


The following steps are only required to grant access to AWS accounts only. These
 steps are not required to grant access to AWS applications.


###### Note

To complete this step, you'll need an Organization instance of IAM Identity Center. For more
 information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").


### Step 1:
 IAM Identity Center: Grant Google Workspace users access to accounts


1. Return to the **IAM Identity Center** console. In the IAM Identity Center navigation
 pane, under **Multi-account permissions**, choose
 **AWS accounts**.
2. On the **AWS accounts** page the
 **Organizational structure** displays your
 organizational root with your accounts underneath it in the hierarchy.
 Select the checkbox for your management account, then select **Assign
 users or groups**.
3. The **Assign users and groups** workflow displays. It
 consists of three steps:


	1. For **Step 1: Select users and groups** choose
	 the user that will be performing the administrator job function.
	 Then choose **Next**.
	2. For **Step 2: Select permission sets** choose
	 **Create permission set** to open a new tab
	 that steps you through the three sub-steps involved in creating a
	 permission set.
	
	
		1. For **Step 1: Select permission set
		 type** complete the following:
		
		
		
		
			* In **Permission set type**,
			 choose **Predefined permission
			 set**.
			* In **Policy for predefined permission
			 set**, choose
			 **AdministratorAccess**.
		Choose **Next**.
		2. For **Step 2: Specify permission set
		 details**, keep the default settings, and
		 choose **Next**.
		
		
		The default settings create a permission set named
		 `AdministratorAccess` with
		 session duration set to one hour.
		3. For **Step 3: Review and create**, verify
		 that the **Permission set type** uses the
		 AWS managed policy
		 **AdministratorAccess**. Choose
		 **Create**. On the **Permission
		 sets** page a notification appears informing
		 you that the permission set was created. You can close this
		 tab in your web browser now.
		4. On the **Assign users and groups**
		 browser tab, you are still on **Step 2: Select
		 permission sets** from which you started the
		 create permission set workflow.
		5. In the **Permissions sets** area, choose
		 the **Refresh** button. The
		 `AdministratorAccess`
		 permission set you created appears in the list. Select the
		 checkbox for that permission set and then choose
		 **Next**.
	3. For **Step 3: Review and submit** review the
	 selected user and permission set, then choose
	 **Submit**.
	
	
	The page updates with a message that your AWS account is being
	 configured. Wait until the process completes.
	
	
	You are returned to the AWS accounts page. A notification
	 message informs you that your AWS account has been reprovisioned
	 and the updated permission set applied. When the user sign in they
	 will have the option of choosing the
	 `AdministratorAccess` role.
	
	
	###### Note
	
	SCIM automatic synchronization from Google Workspace only supports
	 provisioning users. Automatic group provisioning is not
	 supported at this time. You cannot create groups for your Google Workspace
	 users using the AWS Management Console. After provisioning users, you can
	 create groups using AWS CLI Identity Store [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/create-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/create-group.html") command or IAM API [CreateGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateGroup.html "https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateGroup.html").

### Step 2:
 Google Workspace: Confirm Google Workspace users access to AWS resources


1. Sign in to Google using a test user account. To learn how
 to add users to Google Workspace, see [Google Workspace documentation](https://knowledge.workspace.google.com/kb/how-to-create-a-new-user-000007668 "https://knowledge.workspace.google.com/kb/how-to-create-a-new-user-000007668").
2. Select the Google apps launcher (waffle) icon.
3. Scroll to the bottom of the apps list where your custom Google Workspace apps are
 located. The **Amazon Web Services** app is displayed.
4. Select the **Amazon Web Services** app. You are signed into the
 AWS access portal and can see the AWS account icon. Expand that icon to see the
 list of AWS accounts that the user can access. In this tutorial you only
 worked with a single account, so expanding the icon only shows one
 account.
5. Select the account to display the permission sets available to the user.
 In this tutorial you created the **AdministratorAccess**
 permission set.
6. Next to the permission set are links for the type of access available for
 that permission set. When you created the permission set, you specified both
 management console and programmatic access be enabled, so those two options
 are present. Select **Management console** to open the
 AWS Management Console.
7. The user is signed in to the console.

## Next steps


Now that you've configured Google Workspace as an identity provider and provisioned users in
 IAM Identity Center, you can:



* Use the AWS CLI Identity Store [create-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/create-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/create-group.html") command or IAM API [CreateGroup](../IdentityStoreAPIReference/API_CreateGroup.md "../IdentityStoreAPIReference/API_CreateGroup.md") to create groups for your users.


Groups are useful when assigning access to AWS accounts and
 applications. Rather than assign each user individually, you give
 permissions to a group. Later, as you add or remove users from a group, the
 user dynamically gets or loses access to accounts and applications that you
 assigned to the group.
* Configure permissions based on job functions, see [Create a permission
 sets](howtocreatepermissionset.md "howtocreatepermissionset.md").


Permission sets define the level of access that users and groups have to
 an AWS account. Permission sets are stored in IAM Identity Center and can be provisioned
 to one or more AWS accounts. You can assign more than one permission set
 to a user.

###### Note

As an IAM Identity Center administrator, you'll occasionally need to replace older IdP
 certificates with newer ones. For example, you might need to replace an IdP
 certificate when the expiration date on the certificate approaches. The process
 of replacing an older certificate with a newer one is referred to as certificate
 rotation. Make sure to review how to [manage the
 SAML certificates](managesamlcerts.md "managesamlcerts.md") for Google Workspace.


## Troubleshooting


For general SCIM and SAML troubleshooting with Google Workspace, see the following sections:



* [Specific users fail to synchronize into IAM Identity Center from an external SCIM
 provider](troubleshooting.md#issue2 "troubleshooting.md#issue2")
* [Issues regarding contents of SAML assertions created by IAM Identity Center](troubleshooting.md#issue1 "troubleshooting.md#issue1")
* [Duplicate user or group error when provisioning
 users or groups with an external identity provider](troubleshooting.md#duplicate-user-group-idp "troubleshooting.md#duplicate-user-group-idp")
* For Google Workspace troubleshooting, see [Google Workspace documentation](https://support.google.com/a/topic/7579248?sjid=11091727091254312767-NA "https://support.google.com/a/topic/7579248?sjid=11091727091254312767-NA").

The following resources can help you troubleshoot as you work with AWS:



* [AWS re:Post](https://repost.aws/ "https://repost.aws/") - Find FAQs and links to other resources to help you troubleshoot issues.
* [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") - Get technical support
