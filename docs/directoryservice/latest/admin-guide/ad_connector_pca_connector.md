# Set up AWS Private CA Connector for AD

You can integrate your self-managed Active Directory with AWS Private Certificate Authority using AD Connector to
issue and manage certificates for your AD domain-joined users, groups, and machines.
AWS Private CA Connector for AD provides a fully managed AWS Private CA as a drop-in replacement for your
self-managed enterprise CAs without requiring you to deploy, patch, or update local agents or
proxy servers.

You can set up this integration through the AWS Directory Service
console, the AWS Private CA Connector for AD console, or by calling the [`CreateTemplate`](../../../pca-connector-ad/latest/APIReference/API-CreateTemplate.md "../../../pca-connector-ad/latest/APIReference/API-CreateTemplate.md") API. To use the AWS Private CA Connector for Active Directory console, see [AWS Private CA Connector
for Active Directory](../../../privateca/latest/userguide/connector-for-ad.md "../../../privateca/latest/userguide/connector-for-ad.md"). The following sections describe how to set up this integration from the AWS Directory Service
console.

## Prerequisites

For setup instructions, see [Set up Connector for AD](../../../privateca/latest/userguide/connector-for-ad-getting-started-prerequisites.md "../../../privateca/latest/userguide/connector-for-ad-getting-started-prerequisites.md") in the AWS Private CA Connector for AD User Guide.

## Setting up

AWS Private CA Connector for AD

###### To create a Private CA connector for Active Directory

1. Sign in to the AWS Management Console and open the AWS Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directories** page, choose your directory ID.
3. Under the **Application Management** tab and **AWS apps & services** section, choose **AWS Private CA Connector for AD**.
4. On the **Create Private CA certificate for Active Directory** page, complete the steps to create your Private CA for Active Directory connector.

For more information, see [Creating a connector](../../../privateca/latest/userguide/create-connector-for-ad.md "../../../privateca/latest/userguide/create-connector-for-ad.md").

## View your AWS Private CA Connector for AD

###### To view Private CA connector details

1.  Sign in to the AWS Management Console and open the AWS Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2.  On the **Directories** page, choose your directory ID.
3.  Under the **Application Management** tab and **AWS apps & services** section, view your Private CA connectors and associated Private CA. The following fields display:
    1.  **AWS Private CA Connector ID** – The unique identifier for a AWS Private CA connector. Choose it to view the details page.
    2.  **AWS Private CA subject** – Information regarding the distinguished name for the CA. Choose it to view the details page.
    3.  **Status** – Status check results for the AWS Private CA Connector and AWS Private CA:

            * **Active** – Both checks pass
            * **1/2 checks failed** – One check fails
            * **Failed** – Both checks fail

        For failed status details, hover over the hyperlink to see which check failed.

    4.  **DC Certificates Enrollment status** – Status check for domain controller certificate status:
        - **Enabled** – Certificate enrollment is enabled
        - **Disabled** – Certificate enrollment is disabled

    5.  **Date created** – When the AWS Private CA Connector was created.

For more information, see [View connector details](../../../privateca/latest/userguide/view-connector-for-ad.md "../../../privateca/latest/userguide/view-connector-for-ad.md").

## Verify certificate issuance to AD users

Complete the following steps to confirm that AWS Private CA is issuing certificates to
your self-managed Active Directory:

- Restart your on-premises domain controllers.
- View your certificates with Microsoft Management Console. For
  more information, see [Microsoft documentation](https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in "https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in").
