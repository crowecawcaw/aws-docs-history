# Get started with

Connector for SCEP

With AWS Private Certificate Authority Connector for SCEP, you can issue certificates from your private CA to SCEP-enabled devices and mobile device management (MDM) systems. When you create a connector, AWS Private Certificate Authority creates a public SCEP URL for you to request certificates, and also provides you with information that you can use to integrate into your MDM systems.

To issue certificates, you must create an AWS Private Certificate Authority private CA, create a connector, and then configure your SCEP-enabled MDM systems and devices to request certificates from the connector.

###### Topics

- [Before you begin](#connector-for-scep-getting-started-prerequisites "#connector-for-scep-getting-started-prerequisites")
- [Step 1: Create a connector](#gs-create-connector-for-scep-console "#gs-create-connector-for-scep-console")
- [Step 2: Copy connector details into your MDM system](#gs-connector-for-scep-view-details "#gs-connector-for-scep-view-details")

## Before you begin

The following tutorial guides you through the process of creating a connector for SCEP.

To follow this tutorial, you'll need a private CA and a SCEP-enabled device. You also must first fulfill the prerequisites listed in the [Set up Connector for SCEP](connector-for-scep-setting-up.md "connector-for-scep-setting-up.md") section.

The following procedure guides you how to create a connector using the AWS console.

###### Tasks

- [Step 1: Create a connector](#gs-create-connector-for-scep-console "#gs-create-connector-for-scep-console")
- [Step 2: Copy connector details into your MDM system](#gs-connector-for-scep-view-details "#gs-connector-for-scep-view-details")

## Step 1: Create a connector

You'll create either a connector for general-purpose use or Connector for SCEP for Microsoft Intune. General-purpose connectors are designed for use with SCEP-enabled endpoints, and you manage the SCEP challenge passwords. Connector for SCEP for Microsoft Intune are for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune.

General-purpose

###### To create a connector for general-purpose use

Sign in to your AWS account and open the Connector for SCEP console at
`https://console.aws.amazon.com/pca-connector-scep/home`.

1. Choose **Create connector**.
2. In the **Create connector** page, optionally give the connector a friendly name in the **Name tag** field. The name will be displayed in your list of connectors. If you wish, you can add more tags to the connector by selecting **Add more tags**. A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
3. Under **Connector type**, choose **General-purpose**.
4. Under **Private CA**, choose the private CA to use with this connector. Or, create a new one by selecting **Create private CA**. Due to the inherent vulnerabilities in the SCEP protocol, we recommend using a private CA that's dedicated to this connector. If you created a new CA, when you finish creating it in AWS Private CA, return to the Connector for SCEP console and refresh the list of private CAs. Your new private CA should be available for selection.
5. Under **Challenge password** select **Automatically generate challenge password**. We’ll generate a static challenge password for you when we create this connector.
6. Select **Create connector**.

Microsoft Intune

###### To create Connector for SCEP for Microsoft Intune

Sign in to your AWS account and open the Connector for SCEP console at
`https://console.aws.amazon.com/pca-connector-scep/home`.

1. Choose **Create connector**.
2. On the **Create connector** page, optionally give the connector a friendly name in the **Name tag** field. The name will be displayed in your list of connectors. If you wish, you can add more tags to the connector by selecting **Add more tags**. A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
3. Under **Connector type**, choose **Microsoft Intune**.
   1. For **Application (client) ID**, enter the application (client) ID from your Microsoft Entra ID app registration. For information about using Microsoft Intune with Connector for SCEP, see [Configure your MDM system for
      Connector for SCEP](using-connector-for-scep-with-mdm.md "using-connector-for-scep-with-mdm.md").
   2. For **Directory (tenant) ID or primary domain**, enter either the directory (tenant) ID or primary domain from your Microsoft Entra ID app registration.

4. Under **Private CA**, choose the private CA to use with this connector. Or, create a new one by selecting **Create private CA**. Due to the inherent vulnerabilities in the SCEP protocol, we recommend using a private CA that's dedicated to this connector. If you created a new CA, when you finish creating it in AWS Private CA, return to the Connector for SCEP console and refresh the list of private CAs. Your new private CA should be available for selection.
5. Select **Create connector**.

## Step 2: Copy connector details into your MDM system

After you create your connector, you'll need to copy the following details from the connector into your MDM system. To view a connector's details using the console, select the connector from the list on the [Connectors for SCEP](https://console.aws.amazon.com/pca-connector-scep/home#/connectors "https://console.aws.amazon.com/pca-connector-scep/home#/connectors") console page.

- **Public SCEP URL** - This is the connector's endpoint where your SCEP clients will request certificates from. Take care to only provide this endpoint to trusted entities.
- (General-purpose) **Challenge password** - Under **Challenge
  passwords**, select the password that you automatically generated
  in the preceding procedure and then select **View password** to
  view the password. To create an additional password, select **Create
  password**. Take care to distribute passwords carefully and to only
  highly trusted individuals and clients. A single challenge password can be used
  to issue any certificate, with any subject and SANs, and so should be handled
  with care.
- (Microsoft Intune) **Open ID** values - If you're integrating with Microsoft
  Intune, you must copy the **Open ID issuer**, **Open ID
  subject**, and **Open ID audience** into your
  Microsoft Entra app registration's OpenID Connect (OIDC) credential. For more
  information, see [Configure your MDM system for
  Connector for SCEP](using-connector-for-scep-with-mdm.md "using-connector-for-scep-with-mdm.md").
