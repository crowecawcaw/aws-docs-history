# Workforce access through an additional Region

This section explains how your workforce can access the AWS access portal, AWS accounts, and
applications when you have enabled IAM Identity Center in multiple Regions.

The AWS access portal in an additional Region displays the AWS accounts and applications
your workforce has access to in the same way as in the primary Region. Your workforce can sign
into the AWS access portal in an additional Region through a direct link to the regional portal
endpoint (for example, `https://ssoins-111111h2222j33pp.eu-west-1.portal.amazonaws.com`)
or through a [bookmark app](replicate-to-additional-region.md#update-external-idp-setup "replicate-to-additional-region.md#update-external-idp-setup") you set up in the
external IdP.

You can use the AWS access portal endpoint in an additional Region to authorize the AWS CLI for
access to APIs as an IAM Identity Center user. This functionality works in the same way as in the primary
Region. However, CLI authorizations are not replicated across enabled Regions. Therefore, you
have to authorize the CLI in each Region individually.

## User sessions across multiple AWS Regions

IAM Identity Center replicates user sessions from the originating Region to the other enabled Regions.
Session revocation and sign-out in one Region are also replicated to the other Regions.

### Session revocation by IAM Identity Center administrators

IAM Identity Center administrators can revoke user sessions in additional Regions. As sessions are
replicated across Regions, under normal conditions it suffices to revoke a session in a
single Region and let IAM Identity Center replicate the change to the other enabled Regions. If the
primary Region of IAM Identity Center has a disruption, administrators can perform this operation in
additional Regions.

## AWS access portal endpoints in the primary and additional AWS Regions

If you need to look up the AWS access portal URLs for the enabled Regions, follow these steps:

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Management** tab.
4. In the **Regions for IAM Identity Center** section, choose **View
   all AWS access portal URLs**.

The following table specifies the AWS access portal endpoints across the primary and
additional Regions of an IAM Identity Center instance.

| AWS access portal endpoint | Primary Region | Additional Region | URL pattern and example                                                                                                                                                       |
| -------------------------- | -------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Classic IPv4 only1         | Yes            | No                | **Pattern:**<br>`https://`[Identity Store ID]`.awsapps.com/start`<br>**Example:**<br>`https://d-12345678.awsapps.com/start`                                                   |
| Custom-alias IPv4 only1    | Yes (optional) | No                | **Pattern:**<br>`https://`[custom alias]`.awsapps.com/start`<br>**Example:**<br>`https://mycompany.awsapps.com/start`                                                         |
| Alternative IPv4 only2     | Yes            | Yes               | **Pattern:**<br>`https://`[Identity Center instance ID]`.`[Region]`.portal.amazonaws.com`<br>**Example:**<br>`https://ssoins-111111h2222j33pp.eu-west-1.portal.amazonaws.com` |
| Dual-stack2                | Yes            | Yes               | **Pattern:**<br>`https://`[Identity Center instance ID]`.portal.`[Region]`.app.aws`<br>**Example:**<br>`https://ssoins-111111h2222j33pp.portal.eu-west-1.app.aws`             |

1 In additional Regions, the custom alias is not supported,
and the `awsapps.com` parent domain is not available.

2 The alternative IPv4 only and dual-stack portal endpoints
don't have the trailing `/start` in the URL.

## Assertion Consumer Service (ACS) endpoints in the primary and additional AWS Regions

If you need to look up the ACS URLs or download them as part of the SAML metadata, follow
these steps:

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Identity source** tab.
4. In the **Actions** dropdown menu, choose **Manage
   authentication**.
5. The **Service provider metadata** section displays the
   AWS access portal and ACS URL for each enabled Region. IPv4-only and dual-stack URLs are
   displayed in the respective tabs. If your IdP supports uploading the SAML metadata file,
   you can choose **Download metadata file** to download the SAML metadata file with all ACS URLs.
   If this is not supported, or you prefer to add them individually, you can copy individual ones from the table,
   or choose **View ACS URLs** and then **Copy all URLs**.

The following table specifies the SAML Assertion Consumer Service (ACS) endpoints across the
primary and additional Regions of an IAM Identity Center instance:

| ACS endpoint            | Primary Region | Additional Region | URL pattern and example                                                                                                                                                                                                   |
| ----------------------- | -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IPv4 only               | Yes            | Yes               | **Pattern:**<br>`https://`[Region]`.signin.aws/platform/saml/acs/`[Tenant<br>ID]``<br>**Example:**<br>`https://us-west-2.signin.aws/platform/saml/acs/1111111111111111-aaee-ffff-dddd-11111111111`                        |
| Alternative IPv4 only\* | Yes            | No                | **Pattern:**<br>`https://`[Region]`<br>.signin.aws.amazon.com/platform/saml/acs/`[Tenant ID]``<br>**Example:**<br>`https://us-west-2.signin.aws.amazon.com/platform/saml/acs/1111111111111111-aaee-ffff-dddd-11111111111` |
| Dual-stack              | Yes            | Yes               | **Pattern:**<br>`https://`[Region]`.sso.signin.aws/platform/saml/acs/`[Tenant ID]``<br>**Example:**<br>`https://us-west-2.sso.signin.aws/platform/saml/acs/1111111111111111-aaee-ffff-dddd-11111111111`                   |

\*IAM Identity Center no longer uses this endpoint for instances created starting in February 2026.
While this endpoint remains available for earlier instances, we recommend using one of the other two endpoints instead.

## Using AWS managed applications without multiple ACS URLs

Some external identity providers (IdPs) don't support multiple assertion consumer service
(ACS) URLs in their IAM Identity Center application. Multiple ACS URLs are a SAML feature that is required for direct sign-in to a specific Region in a multi-Region IAM Identity Center.

For example, if you launch an AWS managed application through an application link, the
system triggers sign-in through the application's connected IAM Identity Center Region.
However, if the ACS URL for that Region is not configured in the external IdP, the sign-in
fails.

To resolve this issue, work with your IdP vendor to enable support for multiple ACS
URLs. In the meantime, you can still use AWS managed applications in additional Regions.
First, sign into the Region whose ACS URL is configured in the external IdP (the primary
Region by default). After you have an active session in IAM Identity Center, you can launch the
application from the AWS access portal in any enabled Region, or through an application link.
