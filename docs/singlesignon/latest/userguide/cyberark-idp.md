# Setting up SCIM provisioning between CyberArk and

IAM Identity Center

IAM Identity Center supports automatic provisioning (synchronization) of user information from
CyberArk Directory Platform into IAM Identity Center. This provisioning uses the System
for Cross-domain Identity Management (SCIM) v2.0 protocol. For more information, see [Using SAML and SCIM identity federation with external identity
providers](other-idps.md "other-idps.md").

You configure this connection in CyberArk using your IAM Identity Center SCIM endpoint
and access token. When you configure SCIM synchronization, you create a mapping of your user
attributes in CyberArk to the named attributes in IAM Identity Center. This causes the
expected attributes to match between IAM Identity Center and CyberArk.

This guide is based on CyberArk as of August 2021. Steps for newer versions
may vary. This guide contains a few notes regarding configuration of user authentication
through SAML.

###### Note

Before you begin deploying SCIM, we recommend that you first review the [Considerations for using automatic
provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations"). Then continue reviewing
additional considerations in the next section.

###### Topics

- [Prerequisites](#cyberark-prereqs "#cyberark-prereqs")
- [SCIM considerations](#cyberark-considerations "#cyberark-considerations")
- [Step 1: Enable provisioning in IAM Identity Center](#cyberark-step1 "#cyberark-step1")
- [Step 2: Configure provisioning in
  CyberArk](#cyberark-step2 "#cyberark-step2")
- [(Optional) Step 3: Configure user attributes in
  CyberArk for access control (ABAC) in IAM Identity Center](#cyberark-step3 "#cyberark-step3")
- [(Optional) Passing attributes for access
  control](#cyberark-passing-abac "#cyberark-passing-abac")

## Prerequisites

You will need the following before you can get started:

- CyberArk subscription or free trial. To sign up for a free
  trial visit [CyberArk](https://www.cyberark.com/try-buy/ "https://www.cyberark.com/try-buy/").
- An IAM Identity Center enabled account ([free](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/")). For more information, see [Enable IAM Identity Center](setup-enable-idc.md "setup-enable-idc.md").
- A SAML connection from your CyberArk account to IAM Identity Center, as
  described in [CyberArk documentation for IAM Identity Center](https://docs.cyberark.com/identity/Latest/en/Content/Applications/AppsWeb/AWS_SAML_SSO.htm# "https://docs.cyberark.com/identity/Latest/en/Content/Applications/AppsWeb/AWS_SAML_SSO.htm#").
- Associate the IAM Identity Center connector with the roles, users and organizations you want
  to allow access to AWS accounts.

## SCIM considerations

The following are considerations when using CyberArk federation for
IAM Identity Center:

- Only roles mapped in the application Provisioning section will be synchronized
  to IAM Identity Center.
- The provisioning script is supported only in its default state, once changed
  the SCIM provisioning might fail.
  - Only one phone number attribute can be synchronized and the default is
    “work phone”.

- If the role mapping in CyberArk IAM Identity Center application is changed,
  the below behavior is expected:
  - If the role names are changed - no changes to the group names in
    IAM Identity Center.
  - If the group names are changed - new groups will be created in IAM Identity Center,
    old groups will remain but will have no members.

- User synchronization and de-provisioning behavior can be set up from the
  CyberArk IAM Identity Center application, make sure you set up the right
  behavior for your organization. These are the options you have:
  - Overwrite (or not) users in Identity Center directory with the same
    principal name.
  - De-provision users from IAM Identity Center when the user is removed from the
    CyberArk role.
  - De-provision user behavior - disable or delete.

## Step 1: Enable provisioning in IAM Identity Center

In this first step, you use the IAM Identity Center console to enable automatic provisioning.

###### To enable automatic provisioning in IAM Identity Center

1. After you have completed the prerequisites, open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings** in the left navigation pane.
3. On the **Settings** page, locate the **Automatic provisioning** information box, and then choose **Enable**. This
   immediately enables automatic provisioning in IAM Identity Center and displays the necessary
   SCIM endpoint and access token information.
4. In the **Inbound automatic provisioning** dialog box, copy the SCIM endpoint and access token.
   You'll need to paste these in later when
   you configure provisioning in your IdP.
   1. **SCIM endpoint** - For example,
      https://scim.`us-east-2`.amazonaws.com/`11111111111-2222-3333-4444-555555555555`/scim/v2
   2. **Access token** - Choose **Show token**
      to copy the value.###### Warning

This is the only time where you can obtain the SCIM endpoint and access token.
Ensure you copy these values before moving forward. You will enter these values to
configure automatic provisioning in your IdP later in this tutorial. 5. Choose **Close**.

Now that you have set up provisioning in the IAM Identity Center console, you need to complete the
remaining tasks using the CyberArk IAM Identity Center application. These steps are
described in the following procedure.

## Step 2: Configure provisioning in

CyberArk

Use the following procedure in the CyberArk IAM Identity Center application to
enable provisioning with IAM Identity Center. This procedure assumes that you have already added the
CyberArk IAM Identity Center application to your CyberArk admin
console under **Web Apps**. If you have not yet done so, refer to the
[Prerequisites](#cyberark-prereqs "#cyberark-prereqs"), and then
complete this procedure to configure SCIM provisioning.

###### To configure provisioning in CyberArk

1. Open the CyberArk IAM Identity Center application that you added as part of
   configuring SAML for CyberArk (**Apps > Web
   App**). See [Prerequisites](#cyberark-prereqs "#cyberark-prereqs").
2. Choose the **IAM Identity Center** application and go to the
   **Provisioning** section.
3. Check the box for **Enable provisioning for this
   application** and choose **Live Mode**.
4. In the previous procedure, you copied the **SCIM endpoint**
   value from IAM Identity Center. Paste that value into the **SCIM Service
   URL** field, in the CyberArk IAM Identity Center application set
   the **Authorization Type** to be **Authorization
   Header**.
5. Set the **Header Type** to **Bearer
   Token**.
6. From the previous procedure you copied the **Access token**
   value in IAM Identity Center. Paste that value into the **Bearer Token**
   field in the CyberArk IAM Identity Center application.
7. Click **Verify** to test and apply the configuration.
8. Under the **Sync Options**, choose the right behavior for
   which you want the outbound provisioning from CyberArk to work.
   You can choose to overwrite (or not) existing IAM Identity Center users with similar principal
   name, and the de-provisioning behavior.
9. Under **Role Mapping** set up the mapping from
   CyberArk roles, under the **Name** field to
   the IAM Identity Center group, under the **Destination Group**.
10. Click **Save** at the bottom once you are done.
11. To verify that users have been successfully synchronized to IAM Identity Center, return to
    the IAM Identity Center console and choose **Users**. Synchronized users from
    CyberArk will appear on the **Users** page.
    These users can now be assigned to accounts and can connect within IAM Identity Center.

## (Optional) Step 3: Configure user attributes in

CyberArk for access control (ABAC) in IAM Identity Center

This is an optional procedure for CyberArk should you choose to
configure attributes for IAM Identity Center to manage access to your AWS resources. The attributes
that you define in CyberArk are passed in a SAML assertion to IAM Identity Center. You
then create a permission set in IAM Identity Center to manage access based on the attributes you
passed from CyberArk.

Before you begin this procedure, you must first enable the [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md")
feature. For more information about how to do this, see [Enable and configure attributes for access
control](configure-abac.md "configure-abac.md").

###### To configure user attributes in CyberArk for access control in

IAM Identity Center

1. Open the CyberArk IAM Identity Center application that you installed as part
   of configuring SAML for CyberArk (**Apps > Web
   Apps**).
2. Go to the **SAML Response** option.
3. Under **Attributes**, add the relevant attributes to the
   table following the below logic:
   1. **Attribute Name** is the original attribute name
      from CyberArk.
   2. **Attribute Value** is the attribute name sent in the
      SAML assertion to IAM Identity Center.

4. Choose **Save**.

## (Optional) Passing attributes for access

control

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
