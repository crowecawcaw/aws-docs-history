# Using IAM Identity Center to connect with your JumpCloud

Directory Platform

IAM Identity Center supports automatic provisioning (synchronization) of user information from
JumpCloud Directory Platform into IAM Identity Center. This provisioning uses the [Security Assertion Markup
Language (SAML) 2.0](scim-profile-saml.md "scim-profile-saml.md") protocol. For more information, see [Using SAML and SCIM identity federation with external identity
providers](other-idps.md "other-idps.md").

You configure this connection in JumpCloud using your IAM Identity Center SCIM endpoint
and access token. When you configure SCIM synchronization, you create a mapping of your user
attributes in JumpCloud to the named attributes in IAM Identity Center. This causes the
expected attributes to match between IAM Identity Center and JumpCloud.

This guide is based on JumpCloud as of June 2021. Steps for newer versions
may vary. This guide contains a few notes regarding configuration of user authentication
through SAML.

The following steps walk you through how to enable automatic provisioning of users and
groups from JumpCloud to IAM Identity Center using the SCIM protocol.

###### Note

Before you begin deploying SCIM, we recommend that you first review the [Considerations for using automatic
provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations"). Then continue reviewing
additional considerations in the next section.

###### Topics

- [Prerequisites](#jumpcloud-prereqs "#jumpcloud-prereqs")
- [SCIM considerations](#jumpcloud-scim "#jumpcloud-scim")
- [Step 1: Enable provisioning in IAM Identity Center](#jumpcloud-step1 "#jumpcloud-step1")
- [Step 2: Configure provisioning in JumpCloud](#jumpcloud-step2 "#jumpcloud-step2")
- [(Optional) Step 3: Configure user attributes in
  JumpCloud for access control in IAM Identity Center](#jumpcloud-step3 "#jumpcloud-step3")
- [(Optional) Passing attributes for access
  control](#jumpcloud-passing-abac "#jumpcloud-passing-abac")

## Prerequisites

You will need the following before you can get started:

- JumpCloud subscription or free trial. To sign up for a free
  trial visit [JumpCloud](https://console.jumpcloud.com/signup "https://console.jumpcloud.com/signup").
- An IAM Identity Center enabled account ([free](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/")). For more information, see [Enable
  IAM Identity Center](setup-enable-idc.md "setup-enable-idc.md").
- A SAML connection from your JumpCloud account to IAM Identity Center, as
  described in [JumpCloud documentation for IAM Identity Center](https://support.jumpcloud.com/support/s/article/Single-Sign-On-SSO-With-AWS-SSO "https://support.jumpcloud.com/support/s/article/Single-Sign-On-SSO-With-AWS-SSO") .
- If you replicated IAM Identity Center to additional Regions, you must update your identity
  provider
  configuration to enable access to AWS managed applications and AWS accounts from
  those
  Regions. For more details, see
  [Step 3: Update external IdP setup](replicate-to-additional-region.md#update-external-idp-setup "replicate-to-additional-region.md#update-external-idp-setup"). See the
  JumpCloud documentation for additional details.
- Associate the IAM Identity Center connector with the groups you want to allow access to
  AWS accounts.

## SCIM considerations

The following are considerations when using JumpCloud federation for
IAM Identity Center.

- Only groups associated with the AWS Single Sign-On connector in
  JumpCloud will be synchronized with SCIM.
- Only one phone number attribute can be synchronized and the default is "work
  phone."
- Users in JumpCloud directory must have first and last names
  configured to be synchronized to IAM Identity Center with SCIM.
- Attributes are still synchronized if the user is disabled in IAM Identity Center but still
  activate in JumpCloud.
- You can choose to enable SCIM sync for only user information by unchecking the
  "Enable management of User Groups and Group membership" in the connector.

## Step 1: Enable provisioning in IAM Identity Center

In
this first step, you use the IAM Identity Center console to enable automatic provisioning.

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
Now that you have set up provisioning in the IAM Identity Center console, you need
to complete the remaining tasks using the JumpCloud IAM Identity Center connector. These
steps are described in the following procedure.

## Step 2: Configure provisioning in JumpCloud

Use the following procedure in the JumpCloud IAM Identity Center connector to enable
provisioning with IAM Identity Center. This procedure assumes that you have already added the
JumpCloud IAM Identity Center connector to your JumpCloud admin portal and
groups. If you have not yet done so, refer to [Prerequisites](#jumpcloud-prereqs "#jumpcloud-prereqs"), and then complete
this procedure to configure SCIM provisioning.

###### To configure provisioning in JumpCloud

1. Open the JumpCloud IAM Identity Center connector that you installed as part
   of configuring SAML for JumpCloud (**User
   Authentication** > **IAM Identity Center**). See [Prerequisites](#jumpcloud-prereqs "#jumpcloud-prereqs").
2. Choose the **IAM Identity Center** connector, and then choose the third tab **Identity
   Management**.
3. Check the box for **Enable management of User Groups and Group
   membership in this application** if you want groups to SCIM sync.
4. Click on **Configure**.
5. In the previous procedure, you copied the **SCIM endpoint**
   value in IAM Identity Center. Paste that value into the **Base URL** field in
   the JumpCloud IAM Identity Center connector.
6. From the previous procedure you copied the **Access token**
   value in IAM Identity Center. Paste that value into the **Token Key** field
   in the JumpCloud IAM Identity Center connector.
7. Click **Activate** to apply the configuration.
8. Make sure you have a green indicator next to **Single Sign-On
   activated**.
9. Move to the fourth tab **User Groups** and check the groups
   you want to be provisioned with SCIM.
10. Click **Save** at the bottom once you are done.
11. To verify that users have been successfully synchronized to IAM Identity Center, return to
    the IAM Identity Center console and choose **Users**. Synchronized users from
    JumpCloud appear on the **Users** page. These users can
    now be assigned to accounts within IAM Identity Center.

## (Optional) Step 3: Configure user attributes in

JumpCloud for access control in IAM Identity Center

This is an optional procedure for JumpCloud should you choose to
configure attributes for IAM Identity Center to manage access to your AWS resources. The attributes
that you define in JumpCloud are passed in a SAML assertion to IAM Identity Center. You
then create a permission set in IAM Identity Center to manage access based on the attributes you
passed from JumpCloud.

Before you begin this procedure, you must first enable the [Attributes
for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md") feature. For more information about how to do this, see [Enable and configure attributes for access control](configure-abac.md "configure-abac.md").

###### \*\*To configure user attributes in JumpCloud for access

control in IAM Identity Center\*\*

1. Open the JumpCloud IAM Identity Center connector that you installed as part
   of configuring SAML for JumpCloud (**User
   Authentication** > **IAM Identity Center**).
2. Choose the **IAM Identity Center** connector. Then, choose the second tab **IAM Identity Center**.
3. At the bottom of this tab you have **User Attribute
   Mapping**, choose **Add new attribute**, and then
   do the following: You must perform these steps for each attribute you will add
   for use in IAM Identity Center for access control.
   1. In the **Service Provide Attribute Name** field,
      enter `https://aws.amazon.com/SAML/Attributes/AccessControl:`AttributeName`.` Replace `AttributeName`
      with the name of the attribute you are expecting in IAM Identity Center. For example, `https://aws.amazon.com/SAML/Attributes/AccessControl:**`Email`**`
      .
   2. In the **JumpCloud Attribute Name**
      field, choose user attributes from your JumpCloud
      directory. For example, **Email (Work)**.

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
