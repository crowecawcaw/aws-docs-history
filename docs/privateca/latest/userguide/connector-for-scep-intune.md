# Configure Microsoft Intune for Connector for SCEP

You can use AWS Private CA as an external certificate authority (CA) with the Microsoft Intune mobile device management (MDM) system. This guide provides instructions on how to configure Microsoft Intune after you create a Connector for SCEP for Microsoft Intune.

## Prerequisites

Before you create a Connector for SCEP for Microsoft Intune, you must complete the following prerequisites.

- Create an Entra ID.
- Create a Microsoft Intune Tenant.
- Create an App Registration in your Microsoft Entra ID. See [Update an app's requested permissions in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-admin-consent-in-app-registrations-pane "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-admin-consent-in-app-registrations-pane") in the Microsoft Entra documentation for information about how to manage application-level permissions for your App Registration. The App Registration must have the following permissions:
  - Under **Intune** set **scep_challenge_provider**.
  - For **Microsoft Graph** set **Application.Read.All** and **User.Read**.

- You must grant the application in your App Registration admin consent. For information, see [Grant tenant-wide admin consent to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal") in the Microsoft Entra documentation.

###### Tip

When you create the App Registration, take note of the **Application (client) ID** and **Directory (tenant) ID or primary domain**. When you create your Connector for SCEP for Microsoft Intune, you'll enter these values. For information about how to get these values, see [Create a Microsoft Entra application and service principal that can access resources](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal "https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal") in the Microsoft Entra documentation.

## Step 1: Grant AWS Private CA permission to use your Microsoft Entra ID Application

After you create a Connector for SCEP for Microsoft Intune, you must create a federated credential under the Microsoft App Registration so that Connector for SCEP can communicate with Microsoft Intune.

###### To configure AWS Private CA as an external CA in Microsoft Intune

1. In the Microsoft Entra ID console, navigate to the **App registrations**.
2. Choose the application that you created to use with Connector for SCEP. The application (client) ID of the application you click must match the ID you specified when you created the connector.
3. Select **Certificates & secrets** from the **Managed** drop-down menu.
4. Select the **Federated credentials** tab.
5. Select **Add a credential**.
6. From the **Federated credential scenario** drop down menu, choose
   **Other issuer**.
7. Copy and paste the **OpenID issuer** value from your Connector for SCEP for Microsoft Intune details into the **Issuer** field. To view a connector's details, choose the connector from the [Connectors for SCEP](https://console.aws.amazon.com/pca-connector-scep/home#/connectors "https://console.aws.amazon.com/pca-connector-scep/home#/connectors") list in the AWS console. Alternatively, you can get the URL by calling [GetConnector](../../../pca-connector-scep/latest/APIReference/API_GetConnector.md "../../../pca-connector-scep/latest/APIReference/API_GetConnector.md") and then copy the `Issuer` value from the response.
8. For **Type**, select **Explicit subject identifier**.
9. Copy and paste **OpenID subject** value from your connector into the **Value** field. You can view the OpenID issuer value in the connector details page in the AWS console. Alternatively, you can get the URL by calling [GetConnector](../../../pca-connector-scep/latest/APIReference/API_GetConnector.md "../../../pca-connector-scep/latest/APIReference/API_GetConnector.md") and then copy the `Audience` value from the response.
10. (Optional) Enter the name of the instance in the **Name** field. For example, you can name it **AWS Private CA**.
11. (Optional) Enter a description into the **Description** field.
12. Copy and paste the **OpenID Audience** value from your Connector for SCEP for Microsoft Intune details into the **Audience** field. To view a connector's details, choose the connector from the [Connectors for SCEP](https://console.aws.amazon.com/pca-connector-scep/home#/connectors "https://console.aws.amazon.com/pca-connector-scep/home#/connectors") list in the AWS console. Alternatively, you can get the URL by calling [GetConnector](../../../pca-connector-scep/latest/APIReference/API_GetConnector.md "../../../pca-connector-scep/latest/APIReference/API_GetConnector.md") and then copy the `Subject` value from the response.
13. Select **Add**.

## Step 2: Set up a Microsoft Intune configuration profile

After you give AWS Private CA the permission to call Microsoft Intune, you must use Microsoft Intune
to create a Microsoft Intune configuration profile that instructs devices to reach
out to Connector for SCEP for certificate issuance.

1. Create a trusted certificate configuration profile. You must upload the root CA certificate of the chain that you're using with Connector for SCEP into Microsoft Intune to establish trust. For information on how to create a trusted certificate configuration profile, see [Trusted root certificate profiles for Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/protect/certificates-trusted-root "https://learn.microsoft.com/en-us/mem/intune/protect/certificates-trusted-root") in the Microsoft Intune documentation.
2. Create a SCEP certificate configuration profile that points your devices to the connector when they require a new certificate. The configuration profile's **Profile type** should be **SCEP Certificate**. For the configuration profile's root certificate, make sure that you use the trusted certificate that you created in the previous step.

For **SCEP Server URLs**, copy and paste the **Public SCEP URL** from your connector's details into the **SCEP Server URLs** field. To view a connector's details, choose the connector from the [Connectors for SCEP](https://console.aws.amazon.com/pca-connector-scep/home#/connectors "https://console.aws.amazon.com/pca-connector-scep/home#/connectors") list. Alternatively, you can get the URL by calling [ListConnectors](../../../pca-connector-scep/latest/APIReference/API_ListConnectors.md "../../../pca-connector-scep/latest/APIReference/API_ListConnectors.md"), and then copy the `Endpoint` value from the response. For guidance on creating configuration profiles in Microsoft Intune, see [Create and assign SCEP certificate profiles in Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/protect/certificates-profile-scep "https://learn.microsoft.com/en-us/mem/intune/protect/certificates-profile-scep") in the Microsoft Intune documentation.

###### Note

For non-mac OS and iOS devices, if you don't set a validity period in the configuration profile, Connector for SCEP issues a certificate with a validity of one year. If you don't set an Extended Key Usage (EKU) value in the configuration profile, Connector for SCEP issues a certificate with the EKU set with `Client Authentication (Object Identifier: 1.3.6.1.5.5.7.3.2)`. For macOS or iOS devices, Microsoft Intune doesn't respect `ExtendedKeyUsage` or `Validity` parameters in your configuration profiles. For these devices, Connector for SCEP issues a certificate with a one-year validity period to these devices through client authentication.

## Step 3: Verify the connection to Connector for SCEP

After you've created a Microsoft Intune configuration profile that points to the Connector for SCEP endpoint, confirm
that an enrolled device can request a certificate. To confirm, make sure that there
aren't any policy assignment failures. To confirm, in the Intune portal navigate to
**Devices** > **Manage Devices** >
**Configuration** and verify that there's nothing listed under
**Configuration Policy Assignment Failures**. If there is,
confirm your set up with the information from the preceding procedures. If your set
up is correct and there still are failures, then consult [Collect available data from mobile device](https://learn.microsoft.com/en-us/mem/intune/fundamentals/help-desk-operators#collect-available-data-from-mobile-device "https://learn.microsoft.com/en-us/mem/intune/fundamentals/help-desk-operators#collect-available-data-from-mobile-device").

For information about device enrollment, see [What is device enrollment?](https://learn.microsoft.com/en-us/mem/intune/user-help/use-managed-devices-to-get-work-done "https://learn.microsoft.com/en-us/mem/intune/user-help/use-managed-devices-to-get-work-done") in the Microsoft Intune documentation.
