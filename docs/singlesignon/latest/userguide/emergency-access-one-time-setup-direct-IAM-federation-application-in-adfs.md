

# One-time setup of a direct IAM federation application with ADFS
<a name="emergency-access-one-time-setup-direct-IAM-federation-application-in-adfs"></a>

This guide describes the one-time setup process for configuring direct IAM federation with ADFS to enable emergency access to AWS accounts when IAM Identity Center is unavailable.

## Prerequisites
<a name="emergency-access-adfs-prerequisites"></a>

If you plan to configure ADFS with AWS Managed Microsoft AD, we recommend that you first [configure Multi-Region replication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_configure_multi_region_replication.html) and continue with the following steps in the additional Region and not in the primary Region for resiliency.

## Plan your Active Directory group naming convention
<a name="emergency-access-adfs-plan-naming"></a>

Create AD groups using a specific naming pattern that enables automated matching between group names and AWS IAM roles.

**Group naming format**: `AWS-<AccountNumber>-<RoleName>`

For an illustration, see the emergency account in the diagram under [How to design emergency role, account, and group mapping ](emergency-access-mapping-design.md). When a user is assigned to this group, they are granted access to the `EmergencyAccess_Role1_RO` role in account `123456789012`. If a user is associated with multiple groups, they see a list of available roles by AWS account and can choose which role to assume.

## AWS configuration
<a name="emergency-access-adfs-aws-configuration"></a>

The complete setup includes configurations in an emergency access account and the workload accounts. For an illustration of the overall setup, see [How to design emergency role, account, and group mapping ](emergency-access-mapping-design.md).

1. [Create a SAML identity provider](#emergency-access-adfs-create-saml-provider)

1. [Create emergency access roles](#emergency-access-adfs-create-roles)

1. [Configure workload account roles](#emergency-access-adfs-configure-workload-accounts)

### Create a SAML identity provider
<a name="emergency-access-adfs-create-saml-provider"></a>

In the emergency access account, create a SAML identity provider in IAM by following the steps in [Create a SAML identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html). Download the required metadata from your ADFS server:

`https://<yourADFSserverFQDN>/FederationMetadata/2007-06/FederationMetadata.xml`

### Create emergency access roles
<a name="emergency-access-adfs-create-roles"></a>

[Create emergency access roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html) in the emergency account using SAML 2.0 Federation as the trusted entity type. Select the SAML 2.0 provider you created in the previous step.

**Considerations:**
+ **Include all Regions where you operate** — select every Region in which you have active workloads to ensure federation remains available during a Regional disruption.
+ **Configure at least one additional Regional endpoint, even if you operate in a single Region** — for example, if you operate only in `us-east-1`, add `us-west-2` as a secondary endpoint. You can fail over your IdP to the `us-west-2` SAML sign-in endpoint and still access your `us-east-1` resources, even without any workloads in `us-west-2`.
+ **Enable both the non-regional endpoint and regional endpoints** — Although the non-regional endpoint (`https://signin.aws.amazon.com/saml`) is highly available, it is hosted in a single AWS Region, `us-east-1`, while regional endpoints (`https://<region>.signin.aws.amazon.com/saml`) improve resiliency by reducing dependency on a single global endpoint.

**Configure trust policy**

Refer to [One-time setup of a direct IAM federation application in Okta](emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md) for an example trust policy with multiple sign-in regional endpoints. Replace the sample regional endpoints and SAML provider ARNs with yours.

**Configure permissions policies**

Refer to [One-time setup of a direct IAM federation application in Okta](emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md) for an example permissions policy that you attach to the emergency access roles.

### Configure workload account roles
<a name="emergency-access-adfs-configure-workload-accounts"></a>

For the workload account roles, configure a custom trust policy that allows the emergency access roles in the emergency access account to assume them. Refer to [One-time setup of a direct IAM federation application in Okta](emergency-access-one-time-setup-direct-IAM-federation-application-in-idp.md) for an example trust policy, where account `123456789012` is the emergency access account.

## Active Directory configuration
<a name="emergency-access-adfs-ad-configuration"></a>

The following steps describe how to configure Active Directory and ADFS for emergency access.

1. [Create groups](#emergency-access-adfs-create-groups)

1. [Create a relying party](#emergency-access-adfs-create-relying-party)

1. [Create claim rules](#emergency-access-adfs-create-claim-rules)

### Create groups
<a name="emergency-access-adfs-create-groups"></a>

Create emergency groups in Active Directory according to the naming convention described earlier (for example, `AWS-123456789012-EmergencyAccess_Role1_RO`). Assign users to these groups through your existing provisioning mechanisms.

### Create a relying party
<a name="emergency-access-adfs-create-relying-party"></a>

ADFS federation requires a relying party configuration. The relying party is AWS Security Token Service (AWS STS), which outsources authentication to ADFS as the identity provider.

1. In the ADFS Management console, use the Action menu and select **Add Relying Party Trust**. Select **Claims aware** when adding a relying party.

1. For federation metadata, enter the Metadata URL from the identity provider metadata info on the IAM console. For example:

   `https://signin.aws.amazon.com/static/saml/SAMLSPXXXXXX/saml-metadata.xml`

1. Set the display name for the relying party (for example, **AWS Account Access**) and then choose **Next**.

1. Select who you want to enable to access AWS. You can select specific groups and define requirements like MFA.

1. Choose **Close** on the Finish page to complete the Add Relying Party Trust Wizard. AWS is now configured as a relying party.

### Create claim rules
<a name="emergency-access-adfs-create-claim-rules"></a>

ADFS uses Claims Rule Language to issue and transform claims between claims providers and relying parties. You need to create four claim rules: NameId, RoleSessionName, Get AD Groups, and Roles for AWS Access.

Right-click on the relying party and then choose **Edit Claim Issuance Policy**. Choose **Add Rule** to add rules.

**1. NameId**

1. Select **Transform an Incoming Claim** and then choose **Next**.

1. Use the following settings:
   + Claim rule name: `NameId`
   + Incoming claim type: `Windows Account Name`
   + Outgoing claim type: `Name ID`
   + Outgoing name ID format: `Persistent Identifier`
   + Pass through all claim values: checked

1. Choose **OK**.

**2. RoleSessionName**

1. Choose **Add Rule**.

1. In the Claim rule template list, select **Send LDAP Attributes as Claims**.

1. Use the following settings:
   + Claim rule name: `RoleSessionName`
   + Attribute store: `Active Directory`
   + LDAP Attribute: `E-Mail-Addresses`
   + Outgoing Claim type: `https://aws.amazon.com/SAML/Attributes/RoleSessionName`

1. Choose **OK**.

**3. Get AD Groups**

1. Choose **Add Rule**.

1. In the Claim rule template list, select **Send Claims Using a Custom Rule** and then choose **Next**.

1. For Claim Rule Name, enter `Get AD Groups`, and then in Custom rule, enter the following:

   ```
   c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
   => add(store = "Active Directory", types = ("http://temp/variable"), query = ";tokenGroups;{0}", param = c.Value);
   ```

   This custom rule uses a script in the claim rule language that retrieves all the groups the authenticated user is a member of and places them into a temporary claim named `http://temp/variable`.
**Note**  
Ensure there's no trailing whitespace to avoid unexpected results.

**4. Role Attributes**

1. Choose **Add Rule**.

1. In the Claim rule template list, select **Send Claims Using a Custom Rule** and then choose **Next**.

1. For Claim Rule Name, enter `Roles`, and then in Custom rule, enter the following:

   ```
   c:[Type == "http://temp/variable", Value =~ "(?i)^AWS-([\d]{12})"]
   => issue(Type = "https://aws.amazon.com/SAML/Attributes/Role", Value = RegExReplace(c.Value, "AWS-([\d]{12})-", "arn:aws:iam::$1:saml-provider/<ADFS>,arn:aws:iam::$1:role/"));
   ```

   This custom rule uses regular expressions to transform each of the group memberships of the form `AWS-<Account Number>-<Role Name>` into the IAM role ARN and IAM federation provider ARN form that AWS expects.
**Note**  
In the example rule language above, `ADFS` represents the logical name given to the SAML identity provider in the AWS identity provider setup. Change this based on the logical name you chose in the IAM console for your identity provider.

## Test the configuration
<a name="emergency-access-adfs-test-configuration"></a>

Test that the solution works by authenticating at `https://<yourADFSserverFQDN>/adfs/ls/IdpInitiatedSignOn.aspx`. Select the name of the relying party you created from the dropdown list of the sites.

## Update default SAML assertion endpoint in ADFS
<a name="emergency-access-adfs-update-saml-endpoint"></a>

**Important**  
When configuring relying party trust in ADFS, the SAML Assertion endpoint defaults to `https://signin.aws.amazon.com/` which is not a global endpoint and is located in `us-east-1`. We recommend that you modify the default endpoint to a regional endpoint different from where your IAM Identity Center is configured for resiliency. For example, if your IAM Identity Center is deployed in `us-east-1` and you also operate in `us-west-2`, change the default SAML Assertion consumer endpoint to `https://us-west-2.signin.aws.amazon.com/saml`.

1. Choose **Properties** on the relying party trust and go to the **Monitoring** tab. Clear the checkbox **Automatically Update relying party**.

1. Go to the **Endpoints** tab, select your preferred sign-in endpoint, and choose **Edit**.

1. Select the checkbox **Set the trusted URL as default**. Choose **OK** and **Apply** for the setting to take effect.

**Note**  
Most IdPs enable you to keep an application integration deactivated until required. We recommend that you keep the direct IAM federation application deactivated in your IdP until required for emergency access.