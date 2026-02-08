# PingFederate

IAM Identity Center supports automatic provisioning (synchronization) of user and group information
from the PingFederate product by Ping Identity (hereafter
“Ping”) into IAM Identity Center. This provisioning uses the System for Cross-domain
Identity Management (SCIM) v2.0 protocol. For more information, see [Using SAML and SCIM identity federation with external identity
providers](other-idps.md "other-idps.md").

You configure this connection in
PingFederate using your IAM Identity Center SCIM endpoint and access token. When you
configure SCIM synchronization, you create a mapping of your user attributes in
PingFederate to the named attributes in IAM Identity Center. This causes the expected
attributes to match between IAM Identity Center and PingFederate.

This guide is based on PingFederate version 10.2. Steps for other
versions may vary. Contact Ping for more information about how to configure
provisioning to IAM Identity Center for other versions of PingFederate.

The following steps walk you through how to enable automatic provisioning of users and
groups from PingFederate to IAM Identity Center using the SCIM protocol.

###### Note

Before you begin deploying SCIM, we recommend that you first review the [Considerations for using automatic
provisioning](provision-automatically.md#auto-provisioning-considerations "provision-automatically.md#auto-provisioning-considerations"). Then continue reviewing additional
considerations in the next section.

###### Topics

- [Prerequisites](#pingfederate-prereqs "#pingfederate-prereqs")
- [Considerations](#pingfederate-considerations "#pingfederate-considerations")
- [Step 1: Enable provisioning in IAM Identity Center](#pingfederate-step1 "#pingfederate-step1")
- [Step 2: Configure provisioning in
  PingFederate](#pingfederate-step2 "#pingfederate-step2")
- [(Optional) Step 3: Configure user attributes in
  PingFederate for access control in IAM Identity Center](#pingfederate-step3 "#pingfederate-step3")
- [(Optional) Passing attributes for access
  control](#pingfederate-passing-abac "#pingfederate-passing-abac")
- [Troubleshooting](#pingfederate-troubleshooting "#pingfederate-troubleshooting")

## Prerequisites

You'll need the following before you can get started:

- A working PingFederate server. If you do not have an existing
  PingFederate server, you might be able to obtain a free trial or
  developer account from the [Ping Identity](https://www.pingidentity.com/developer/en/get-started.html#:~:text=Get%20started%20developing%20with%20open,a%20developer%20trial%20of%20PingOne. "https://www.pingidentity.com/developer/en/get-started.html#:~:text=Get%20started%20developing%20with%20open,a%20developer%20trial%20of%20PingOne.") website. The trial includes licenses and software downloads
  and associated documentation.
- A copy of the PingFederate IAM Identity Center Connector software installed on
  your PingFederate server. For more information about how to obtain
  this software, see [IAM Identity Center Connector](https://support.pingidentity.com/s/marketplace-integration/a7i1W000000TOZ1/ "https://support.pingidentity.com/s/marketplace-integration/a7i1W000000TOZ1/") on the Ping Identity website.
- An IAM Identity Center-enabled account ([free](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/")). For more information, see [Enable IAM Identity Center](setup-enable-idc.md "setup-enable-idc.md").
- A SAML connection from your PingFederate instance to IAM Identity Center. For
  instructions on how to configure this connection, see the
  PingFederate documentation. In summary, the recommended path is to
  use the IAM Identity Center Connector to configure "Browser SSO" in PingFederate,
  using the “download" and "import" metadata features on both ends to exchange SAML
  metadata between PingFederate and IAM Identity Center.
- If you replicated IAM Identity Center to additional Regions, you must update your identity
  provider
  configuration to enable access to AWS managed applications and AWS accounts from those
  Regions. For more details, see
  [Step 3: Update external IdP setup](replicate-to-additional-region.md#update-external-idp-setup "replicate-to-additional-region.md#update-external-idp-setup"). See the
  PingFederate documentation for additional details.

## Considerations

The following are important considerations about PingFederate that
can affect how you implement provisioning with IAM Identity Center.

- If an attribute (such as a phone number) is removed from a user in the data
  store configured in PingFederate, that attribute will not be removed
  from the corresponding user in IAM Identity Center. This is a known limitation in
  PingFederate’s provisioner implementation. If an attribute is
  changed to a different (non-empty) value on a user, that change will be synchronized
  to IAM Identity Center.

## Step 1: Enable provisioning in IAM Identity Center

In this first step, you use the IAM Identity Center console to enable automatic
provisioning.

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

Now that you have set up provisioning in the IAM Identity Center console, you must complete the
remaining tasks using the PingFederate administrative console., The steps
are described in the following procedure.

## Step 2: Configure provisioning in

PingFederate

Use the following procedure in the PingFederate administrative
console to enable integration between IAM Identity Center and the IAM Identity Center Connector. This procedure
assumes that you have already installed the IAM Identity Center Connector software. If you have not
yet done so, refer to [Prerequisites](#pingfederate-prereqs "#pingfederate-prereqs"), and then complete this procedure to configure
SCIM provisioning.

###### Important

If your PingFederate server has not been previously configured for
outbound SCIM provisioning, you may need to make a configuration file change to enable
provisioning. For more information, see Ping documentation. In summary,
you must modify the `pf.provisioner.mode` setting in the
**pingfederate-<version>/pingfederate/bin/run.properties**
file to a value other than `OFF` (which is the default), and restart the
server if currently running. For example, you may choose to use
`STANDALONE` if you don’t currently have a high-availability
configuration with PingFederate.

###### To configure provisioning in PingFederate

1. Sign on to the PingFederate administrative console.
2. Select **Applications** from the top of the page, then click
   **SP Connections**.
3. Locate the application you created previously to form your SAML connection with
   IAM Identity Center, and click on the connection name.
4. Select **Connection Type** from the dark navigation headings
   near the top of the page. You should see **Browser SSO** already
   selected from your previous configuration of SAML. If not, you must complete those
   steps first before you can continue.
5. Select the **Outbound Provisioning** check box, choose
   **IAM Identity Center Cloud Connector** as the type, and click
   **Save**. If **IAM Identity Center Cloud Connector** does not
   appear as an option, ensure that you have installed the IAM Identity Center Connector and have
   restarted your PingFederate server.
6. Click **Next** repeatedly until you arrive on the
   **Outbound Provisioning** page, and then click the
   **Configure Provisioning** button.
7. In the previous procedure, you copied the **SCIM endpoint**
   value in IAM Identity Center. Paste that value into the **SCIM URL** field in the
   PingFederate console. Also, in the previous procedure you copied the
   **Access token** value in IAM Identity Center. Paste that value into the
   **Access Token** field in the PingFederate
   console. Click **Save**.
8. On the **Channel Configuration (Configure Channels)** page,
   click **Create**.
9. Enter a **Channel Name** for this new provisioning channel
   (such as `AWSIAMIdentityCenterchannel`), and click
   **Next**.
10. On the **Source** page, choose the **Active Data
    Store** you want to use for your connection to IAM Identity Center, and click
    **Next**.

###### Note

If you have not yet configured a data source, you must do so now. See the
Ping product documentation for information on how to choose and
configure a data source in PingFederate. 11. On the **Source Settings** page, confirm all values are correct
for your installation, then click **Next**. 12. On the **Source Location** page, enter settings appropriate to
your data source, and then click **Next**. For example, if using
Active Directory as an LDAP directory:

    1. Enter the **Base DN** of your AD forest (such as
     `DC=myforest,DC=mydomain,DC=com`).
    2. In **Users > Group DN**, specify a single group that
     contains all of the users that you want to provision to IAM Identity Center. If no such single
     group exists, create that group in AD, return to this setting, and then enter
     the corresponding DN.
    3. Specify whether to search subgroups (**Nested Search**),
     and any required LDAP **Filter**.
    4. In **Groups > Group DN**, specify a single group that
     contains all of the groups that you want to provision to IAM Identity Center. In many cases,
     this may be the same DN as you specified in the **Users**
     section. Enter **Nested Search** and
     **Filter** values as required.

13. On the **Attribute Mapping** page, ensure the following, and
    then click **Next**:
    1.  The **userName** field must be mapped to an
        **Attribute** that is formatted as an email
        (user@domain.com). It must also match the value that the user will use to log in
        to Ping. This value in turn is populated in the SAML `nameId` claim
        during federated authentication and used for matching to the user in IAM Identity Center. For
        example, when using Active Directory, you may choose to specify the
        `UserPrincipalName` as the **userName**.
    2.  Other fields suffixed with a **\*** must be mapped to
        attributes that are non-null for your users.

14. On the **Activation & Summary** page, set the
    **Channel Status** to **Active** to cause the
    synchronization to start immediately after the configuration is saved.
15. Confirm that all configuration values on the page are correct, and click
    **Done**.
16. On the **Manage Channels** page, click
    **Save**.
17. At this point, provisioning starts. To confirm activity, you can view the
    **provisioner.log** file, located by default in the
    **pingfederate-<version>/pingfederate/log**
    directory on your PingFederate server.
18. To verify that users and groups have been successfully synchronized to IAM Identity Center,
    return to the IAM Identity Center Console and choose **Users**. Synchronized
    users from PingFederate appear on the **Users**
    page. You can also view synchronized groups on the **Groups**
    page.

## (Optional) Step 3: Configure user attributes in

PingFederate for access control in IAM Identity Center

This is an optional procedure for PingFederate if you choose to
configure attributes you will use in IAM Identity Center to manage access to your AWS resources. The
attributes that you define in PingFederate are passed in a SAML assertion
to IAM Identity Center. You will then create a permission set in IAM Identity Center to manage access based on the
attributes you passed from PingFederate.

Before you begin this procedure, you must first enable the [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md")
feature. For more information about how to do this, see [Enable and configure attributes for access
control](configure-abac.md "configure-abac.md").

###### To configure user attributes in PingFederate for access control in

IAM Identity Center

1. Sign on to the PingFederate administrative console.
2. Choose **Applications** from the top of the page, then click
   **SP Connections**.
3. Locate the application you created previously to form your SAML connection with
   IAM Identity Center, and click on the connection name.
4. Choose **Browser SSO** from the dark navigation headings near
   the top of the page. Then click on **Configure Browser
   SSO**.
5. On the **Configure Browser SSO** page, choose
   **Assertion Creation**, and then click on **Configure
   Assertion Creation**.
6. On the **Configure Assertion Creation** page, choose
   **Attribute Contract**.
7. On the **Attribute Contract** page, under **Extend the
   Contract** section, add a new attribute by performing the following
   steps:
   1. In the text box, enter
      `https://aws.amazon.com/SAML/Attributes/AccessControl:`AttributeName``,
replace `AttributeName`with the name of the attribute you
are expecting in IAM Identity Center. For example,`https://aws.amazon.com/SAML/Attributes/AccessControl:**Department**`.
   2. For **Attribute Name Format**, choose
      **urn:oasis:names:tc:SAML:2.0:attrname-format:uri**.
   3. Choose **Add**, and then choose
      **Next**.

8. On the **Authentication Source Mapping** page, choose the
   Adapter Instance configured with your application.
9. On the **Attribute Contract Fulfillment** page, choose the
   **Source** (_data store_) and
   **Value** (_data store attribute_) for the
   **Attribute Contract**
   `https://aws.amazon.com/SAML/Attributes/AccessControl:**Department**`.

###### Note

If you have not yet configured a data source, you will need to do so now. See
the Ping product documentation for information on how to choose and
configure a data source in PingFederate. 10. Click **Next** repeatedly until you arrive on the
**Activation & Summary** page, and then click
**Save**.

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

## Troubleshooting

For general SCIM and SAML troubleshooting with PingFederate, see the following sections:

- [Specific users fail to synchronize into IAM Identity Center from an external SCIM
  provider](troubleshooting.md#issue2 "troubleshooting.md#issue2")
- [Issues regarding contents of SAML assertions created by IAM Identity Center](troubleshooting.md#issue1 "troubleshooting.md#issue1")
- [Duplicate user or group error when provisioning
  users or groups with an external identity provider](troubleshooting.md#duplicate-user-group-idp "troubleshooting.md#duplicate-user-group-idp")
- For more information on PingFederate, see [PingFederate documentation](https://docs.pingidentity.com/pingfederate/latest/pf_pf_landing_page.html "https://docs.pingidentity.com/pingfederate/latest/pf_pf_landing_page.html").

The following resources can help you troubleshoot as you work with AWS:

- [AWS re:Post](https://repost.aws/ "https://repost.aws/") - Find FAQs and links to other resources to help you troubleshoot issues.
- [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") - Get technical support
