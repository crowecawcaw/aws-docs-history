# Configure SAML and SCIM with Okta and IAM Identity Center

You can automatically provision or synchronize user and group information from Okta into
IAM Identity Center using the [System for
Cross-domain Identity Management (SCIM) 2.0 protocol](scim-profile-saml.md#scim-profile "scim-profile-saml.md#scim-profile"). For more information, see
[Using SAML and SCIM identity federation with external identity
providers](other-idps.md "other-idps.md").

To configure this connection in Okta, you use your SCIM endpoint for IAM Identity Center and a bearer
token that is created automatically by IAM Identity Center. When you configure SCIM synchronization, you
create a mapping of your user attributes in Okta to the named attributes in IAM Identity Center. This
mapping matches the expected user attributes between IAM Identity Center and your Okta account.

Okta supports the following provisioning features when connected to IAM Identity Center through
SCIM:

- Create users – Users assigned to the IAM Identity Center application in Okta are
  provisioned in IAM Identity Center.
- Update user attributes – Attribute changes for users who are assigned to
  the IAM Identity Center application in Okta are updated in IAM Identity Center.
- Deactivate users – Users who are unassigned from the IAM Identity Center application in
  Okta are disabled in IAM Identity Center.
- Group push – Groups (and their members) in Okta are synchronized to
  IAM Identity Center.

###### Note

To minimize administrative overhead in both Okta and IAM Identity Center, we recommend
that you assign and _push_ groups instead of individual
users.
**Objective**

In this tutorial, you will walk through setting up a SAML connection with Okta IAM Identity Center.
Later, you will synchronize users from Okta, using SCIM. In this scenario, you manage all
users and groups in Okta. Users sign in through the Okta portal. To verify everything is
configured correctly, after completing the configuration steps you will sign in as an Okta
user and verify access to AWS resources.

###### Note

You can sign up for an Okta account ([free trial](https://www.okta.com/free-trial/ "https://www.okta.com/free-trial/")) that has
Okta's
[IAM Identity Center
application](https://www.okta.com/integrations/aws-single-sign-on/ "https://www.okta.com/integrations/aws-single-sign-on/") installed. For paid Okta products, you might need
to confirm that your Okta license supports _lifecycle management_ or similar capabilities that enable outbound
provisioning. These features might be necessary to configure SCIM from
Okta to IAM Identity Center.

If you haven't enabled IAM Identity Center yet, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").

## Considerations

- Before you configure SCIM provisioning between Okta and IAM Identity Center, we
  recommend that you first review [Considerations for using automatic
  provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations").
- Every Okta user must have a **First name**,
  **Last name**, **Username** and
  **Display name** value specified.
- Each Okta user has only a single value per data attribute, such as email
  address or phone number. Any users that have multiple values will fail to
  synchronize. If there are users that have multiple values in their
  attributes, remove the duplicate attributes before attempting to provision
  the user in IAM Identity Center. For example, only one phone number attribute can be
  synchronized, since the default phone number attribute is "work phone", use
  the "work phone" attribute to store the user's phone number, even if the
  phone number for the user is a home phone or a mobile phone.
- When using Okta with IAM Identity Center, IAM Identity Center is generally configured as an
  Application in Okta. This allows you to configure multiple instances of
  IAM Identity Center as multiple applications, supporting access to multiple AWS
  Organizations, within a single instance of the Okta.
- Entitlements and role attributes aren't supported and cannot be
  synchronized with IAM Identity Center.
- Using the same Okta group for both assignments and group push isn't
  currently supported. To maintain consistent group memberships between Okta
  and IAM Identity Center, create a separate group and configure it to push groups to
  IAM Identity Center.

## Step 1: Okta: Obtain the SAML metadata from your

Okta account

1. Sign in to the Okta admin dashboard, expand **Applications**, then
   select **Applications**.
2. On the **Applications** page, choose **Browse App
   Catalog**.
3. In the search box, type **AWS IAM Identity Center**, select the app to
   add the IAM Identity Center app.
4. Select the **Sign On** tab.
5. Under **SAML Signing Certificates**, select
   **Actions**, and then select **View IdP
   Metadata**. A new browser tab opens showing the document tree
   of an XML file. Select all of the XML from
   `<md:EntityDescriptor>` to
   `</md:EntityDescriptor>` and copy it to a text file.
6. Save the text file as `metadata.xml`.

Leave the Okta admin dashboard open, you will continue using this console in the later steps.

## Step 2: IAM Identity Center: Configure Okta as the identity

source for IAM Identity Center

1.  Open the [IAM Identity Center
    console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon") as a user with administrative privileges.
2.  Choose **Settings** in the left navigation pane.
3.  On the **Settings** page, choose
    **Actions**, and then choose **Change identity
    source**.
4.  Under **Choose identity source**, select
    **External identity provider**, and then choose
    **Next**.
5.  Under **Configure external identity provider**, do the
    following:
    1. Under **Service provider metadata**, choose
       **Download metadata file** to download the
       IAM Identity Center metadata file and save it on your system. You will provide the
       IAM Identity Center SAML metadata file to Okta later in this tutorial.

    Copy the following items to a text file for easy access:

        * **IAM Identity Center Assertion Consumer Service (ACS)
         URL**
        * **IAM Identity Center issuer URL**

    You'll need these values later in this tutorial. 2. Under **Identity provider metadata**, under
    **IdP SAML metadata**, select **Choose
    file** and then select the
    `metadata.xml` file you created in the
    previous step. 3. Choose **Next**.

6.  After you read the disclaimer and are ready to proceed, enter
    **ACCEPT**.
7.  Choose **Change identity source**.

Leave the AWS console open, you will continue using this console in the
next step. 8. Return to the Okta admin dashboard and select the **Sign On** tab of
the AWS IAM Identity Center app, then select **Edit**. 9. Under **Advanced Sign-on Settings** enter the
following:

    * For **ACS URL**, enter the value you copied for
     **IAM Identity Center Assertion Consumer Service (ACS)
     URL**
    * For **Issuer URL**, enter the value you copied
     for **IAM Identity Center issuer URL**
    * For **Application username format**, select one
     of the options from the menu.


    Ensure the value you choose is unique for each user. For this
     tutorial, select **Okta username**

10. Choose **Save**.

You are now ready to provision users from Okta to IAM Identity Center. Leave the Okta admin dashboard
open, and return to the IAM Identity Center console for the next step.

## Step 3: IAM Identity Center and Okta: Provision Okta

users

1. In the IAM Identity Center console on the **Settings** page, locate the
   **Automatic provisioning** information box, and then
   choose **Enable**. This enables automatic provisioning in
   IAM Identity Center and displays the necessary SCIM endpoint and access token
   information.
2. In the **Inbound automatic provisioning** dialog box,
   copy each of the values for the following options:
   1. **SCIM endpoint** - For example,
      https://scim.`us-east-2`.amazonaws.com/`11111111111-2222-3333-4444-555555555555`/scim/v2
   2. **Access token** - Choose **Show
      token** to copy the value.###### Warning

This is the only time where you can obtain the SCIM endpoint and
access token. Ensure you copy these values before moving forward. You
will enter these values to configure automatic provisioning in Okta
later in this tutorial. 3. Choose **Close**. 4. Return to the Okta admin dashboard and navigate to the IAM Identity Center app. 5. On the **IAM Identity Center app** page, choose the
**Provisioning** tab, and then in the left navigation
under **Settings**, choose
**Integration**. 6. Choose **Edit**, and then select the checkbox next to
**Enable API integration** to enable automatic
provisioning. 7. Configure Okta with the SCIM provisioning values from AWS IAM Identity Center that you
copied earlier in this step:

    1. In the **Base URL** field, enter the
     **SCIM endpoint** value.
    2. In the **API Token** field, enter the
     **Access token** value.

8. Choose **Test API Credentials** to verify the credentials
   entered are valid.

The message **AWS IAM Identity Center was verified successfully!**
displays. 9. Choose **Save**. You're moved to the
**Settings** section, with
**Integration** selected. 10. Under **Settings**, choose **To App**,
and then select the **Enable** checkbox for each of the
**Provisioning to App** features you want to enable.
For this tutorial, select all the options. 11. Choose **Save**.

You are now ready to synchronize your users from Okta with IAM Identity Center.

## Step 4: Okta: Synchronize users from Okta with

IAM Identity Center

By default, no groups or users are assigned to your Okta IAM Identity Center app. Provisioning
groups provisions the users that are members of the group. Complete the following
steps to synchronize groups and users with AWS IAM Identity Center.

1.  In the **Okta IAM Identity Center app** page, choose the
    **Assignments** tab. You can assign both people and
    groups to the IAM Identity Center app.
    1.  To assign people:

            * In the **Assignments** page, choose
             **Assign**, and then choose
             **Assign to people**.
            * Choose the Okta users that you want to have access to
             the IAM Identity Center app. Choose **Assign**, choose
             **Save and Go Back**, and then choose
             **Done**.

        This starts the process of provisioning the users into
        IAM Identity Center.

    2.  To assign groups:

            * In the **Assignments** page, choose
             **Assign**, and then choose
             **Assign to groups**.
            * Choose the Okta groups that you want to have access to
             the IAM Identity Center app. Choose **Assign**, choose
             **Save and Go Back**, and then choose
             **Done**.

        This starts the process of provisioning the users in the group
        into IAM Identity Center.

    ###### Note

    You might be required to specify additional attributes for the
    group if they aren't present in all of the user records. The
    attributes specified for the group will override any individual
    attribute values.

2.  Choose the **Push Groups** tab. Choose the Okta group
    you want to synchronize with IAM Identity Center. Choose **Save**.

The group status changes to **Active** after the group
and its members have been pushed to IAM Identity Center. 3. Return to the **Assignments** tab. 4. To add individual Okta users to IAM Identity Center, use the following steps:

    1. In the **Assignments** page, choose
     **Assign**, and then choose **Assign to
     People**.
    2. Choose the Okta users that you want to have access to the IAM Identity Center
     app. Choose **Assign**, choose **Save and
     Go Back**, and then choose **Done**.


    This starts the process of provisioning the individual users into
     IAM Identity Center.


    ###### Note

    You can also assign users and groups to the AWS IAM Identity Center app,
     from the **Applications** page of the Okta admin dashboard.
     To do this select the **Settings** icon and
     then choose **Assign to Users** or
     **Assign to Groups** and then specify the
     user or group.

5. Return to the IAM Identity Center console. In the left navigation, select
   **Users**, you should see the user list populated by
   your Okta users.

###### Congratulations!

You have successfully set up a SAML connection between Okta and AWS and
have verified that automatic provisioning is working. You can now assign these
users to accounts and applications in **IAM Identity Center**. For this
tutorial, in the next step let's designate one of the users as the IAM Identity Center
administrator by granting them administrative permissions to the
management account.

## Passing attributes for access

control - _Optional_

You can optionally use the [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md") feature in IAM Identity Center to pass an
`Attribute` element with the `Name` attribute set to
`https://aws.amazon.com/SAML/Attributes/AccessControl:`{TagKey}``.
This element allows you to pass attributes as session tags in the SAML assertion. For more
information about session tags, see [Passing session tags in AWS STS](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") in the _IAM User Guide_.

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

The following steps are only required to grant access to AWS accounts only.
These steps are not required to grant access to AWS applications.

###### Note

To complete this step, you'll need an Organization instance of IAM Identity Center. For more
information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

### Step 1: IAM Identity Center: Grant Okta users access to

accounts

1.  In the IAM Identity Center navigation pane, under **Multi-account
    permissions**, choose
    **AWS accounts**.
2.  On the **AWS accounts** page the
    **Organizational structure** displays your
    organizational root with your accounts underneath it in the hierarchy.
    Select the checkbox for your management account, then select
    **Assign users or groups**.
3.  The **Assign users and groups** workflow displays. It
    consists of three steps:
    1.  For **Step 1: Select users and groups**,
        choose the user that will be performing the administrator job
        function. Then choose **Next**.
    2.  For **Step 2: Select permission sets**,
        choose **Create permission set** to open a new
        tab that walks you through the three sub-steps involved in
        creating a permission set.
        1.  For **Step 1: Select permission set
            type** complete the following:

                * In **Permission set type**,
                 choose **Predefined permission
                 set**.
                * In **Policy for predefined permission
                 set**, choose
                 **AdministratorAccess**.

            Choose **Next**.

        2.  For **Step 2: Specify permission set
            details**, keep the default settings, and
            choose **Next**.

        The default settings create a permission set named
        `AdministratorAccess` with
        session duration set to one hour. 3. For **Step 3: Review and create**,
        verify that the **Permission set type**
        uses the AWS managed policy
        **AdministratorAccess**. Choose
        **Create**. On the
        **Permission sets** page, a
        notification appears informing you that the permission
        set was created. You can close this tab in your web
        browser now.On the **Assign users and groups** browser
        tab, you are still on **Step 2: Select permission
        sets** from which you started the create permission
        set workflow.

    In the **Permissions sets** area, choose the
    **Refresh** button. The
    `AdministratorAccess` permission
    set you created appears in the list. Select the checkbox for
    that permission set and then choose
    **Next**. 3. For **Step 3: Review and submit**, review the
    selected user and permission set, then choose
    **Submit**.

    The page updates with a message that your AWS account is
    being configured. Wait until the process completes.

    You are returned to the AWS accounts page. A notification
    message informs you that your AWS account has been
    reprovisioned and the updated permission set applied. When the
    user signs-in they will have the option of choosing the
    `AdministratorAccess` role.

### Step 2: Okta: Confirm Okta users access to AWS

resources

1. Sign in using a test account to the Okta
   dashboard.
2. Under **My Apps**, select the
   AWS IAM Identity Center icon.
3. You should see the AWS account icon. Expand that icon to see the
   list of AWS accounts that the user can access. In this tutorial you
   only worked with a single account, so expanding the icon only shows one
   account.
4. Select the account to display the permission sets available to the
   user. In this tutorial you created the
   **AdministratorAccess** permission set.
5. Next to the permission set are links for the type of access available
   for that permission set. When you created the permission set, you
   specified access to both the AWS Management Console and programmatic access. Select
   **Management console** to open the
   AWS Management Console.
6. The user is signed in to the AWS Management Console.

## Next steps

Now that you've configured Okta as an identity provider and provisioned users in
IAM Identity Center, you can:

- Grant access to AWS accounts, see [Assign user or group access to AWS accounts](assignusers.md "assignusers.md").
- Grant access to cloud applications, see [Assign user access to applications in the IAM Identity Center
  console](assignuserstoapp.md "assignuserstoapp.md").
- Configure permissions based on job functions, see [Create a permission
  set](howtocreatepermissionset.md "howtocreatepermissionset.md").

## Troubleshooting

For general SCIM and SAML troubleshooting with Okta, see the following
sections:

- [Reprovisioning users and
  groups deleted from IAM Identity Center](#reprovisioning-deleted-users-groups "#reprovisioning-deleted-users-groups")
- [Automatic Provisioning Error in
  Okta](#okta-auto-provisioning-error "#okta-auto-provisioning-error")
- [Specific users fail to synchronize into IAM Identity Center from an external SCIM
  provider](troubleshooting.md#issue2 "troubleshooting.md#issue2")
- [Issues regarding contents of SAML assertions created by IAM Identity Center](troubleshooting.md#issue1 "troubleshooting.md#issue1")
- [Duplicate user or group error when provisioning
  users or groups with an external identity provider](troubleshooting.md#duplicate-user-group-idp "troubleshooting.md#duplicate-user-group-idp")
- [Additional resources](#gs-okta-troubleshooting-resources "#gs-okta-troubleshooting-resources")

### Reprovisioning users and

groups deleted from IAM Identity Center

- You could receive the following error message in the Okta Console,
  if you're attempting to change either a user or group in Okta
  that was once synchronized and then deleted from IAM Identity Center:
  - **`Automatic profile push of user `Jane Doe`to app
AWS IAM Identity Center failed: Error while trying to push profile update
for`jane_doe@example.com`: No user returned for user
`xxxxx-xxxxxx-xxxxx-xxxxxxx``**
  - **`Linked group is missing in AWS IAM Identity Center. Change the
linked group to resume pushing group
memberships.`**

- You could also receive the following error message in the
  Okta's Systems Logs for either synchronized and deleted IAM Identity Center
  users or groups:
  - **`Okta Error: Eventfailed
application.provision.user.push_profile : No user returned
for user `xxxxx-xxxxxx-xxxxx-xxxxxxx``**
  - **`Okta Error:
application.provision.group_push.mapping.update.or.delete.failed.with.error
: Linked group is missing in AWS IAM Identity Center. Change the linked
group to resume pushing group
memberships.`**

###### Warning

Users and groups should be deleted from Okta rather than IAM Identity Center if you
have synchronized Okta and IAM Identity Center using SCIM.

###### Troubleshooting deleted IAM Identity Center Users

To address this issue with deleted IAM Identity Center users, the users must be deleted
from Okta. If necessary, these users would also need to be recreated in
Okta. When the user is recreated in Okta, it will also be reprovisioned
into the IAM Identity Center through SCIM. For more information on deleting a user, see
[Okta documentation](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-deactivate-user-account.htm "https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-deactivate-user-account.htm").

###### Note

If you need to remove a Okta user’s access to IAM Identity Center, you should first
remove them from their Group Push and then their Assignment Group in Okta.
This ensures the user is removed from their associated group membership in
IAM Identity Center. For more information on troubleshooting Group Push, see [Okta documentation](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-group-push-troubleshoot.htm "https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-group-push-troubleshoot.htm").

###### Troubleshooting deleted IAM Identity Center Groups

To address this issue with deleted IAM Identity Center groups, the group
must be deleted from Okta. If necessary, these groups would also need to be
recreated in Okta using Group Push. When the user is recreated in Okta, it
will also be reprovisioned into the IAM Identity Center through SCIM. For
more information on deleting a group, see [Okta documentation](https://help.okta.com/oie/en-us/content/topics/users-groups-profiles/usgp-group-push-troubleshoot.htm "https://help.okta.com/oie/en-us/content/topics/users-groups-profiles/usgp-group-push-troubleshoot.htm").

### Automatic Provisioning Error in

Okta

If you receive the following error message in Okta:

**`Automatic provisioning of user Jane Doe to app AWS IAM Identity Center failed:
 Matching user not found`**

See [Okta documentation](https://support.okta.com/help/s/article/aws-iam-identity-center-provisioning-error-automatic-provisioning-of-user-name-of-user-to-app-aws-iam-identity-center-failed-matching-user-not-found?language=en_US "https://support.okta.com/help/s/article/aws-iam-identity-center-provisioning-error-automatic-provisioning-of-user-name-of-user-to-app-aws-iam-identity-center-failed-matching-user-not-found?language=en_US") for more information.

### Additional resources

- For general SCIM troubleshooting tips, see [Troubleshooting IAM Identity Center issues](troubleshooting.md "troubleshooting.md").

The following resources can help you troubleshoot as you work with AWS:

- [AWS re:Post](https://repost.aws/ "https://repost.aws/") - Find FAQs and links to other resources to help you troubleshoot issues.
- [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") - Get technical support
