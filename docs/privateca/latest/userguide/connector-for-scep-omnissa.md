# Configure Omnissa Workspace ONE for Connector for SCEP

You can use AWS Private CA as an external certificate authority (CA) with the Omnissa Workspace ONE UEM
(Unified Endpoint Management) system. This guide provides instructions on how to configure
Omnissa Workspace ONE after you create a SCEP connector in AWS.

## Prerequisites

Before you create a SCEP connector for Omnissa Workspace ONE, you must complete the following
prerequisites:

- Create a private CA in the AWS console. For more information, see [Create a private CA in AWS Private CA](create-CA.md "create-CA.md").
- Create a general purpose SCEP connector. For more information, see [Create a
  connector](connector-for-scep-getting-started.md#gs-create-connector-for-scep-console "connector-for-scep-getting-started.md#gs-create-connector-for-scep-console").
- Have an active Omnissa Workspace ONE environment admin account with an Organization
  Group ID.
- If you are enrolling an Apple device, configure the Apple Push Notification
  Service (APNs) for MDM. For more information, see [APNs Certificates](https://docs.omnissa.com/bundle/WorkspaceONE-UEM-Console-BasicsVSaaS/page/APNsCertificates.html "https://docs.omnissa.com/bundle/WorkspaceONE-UEM-Console-BasicsVSaaS/page/APNsCertificates.html") in the Omnissa documentation.

## Step 1: Define a

certificate authority and template in Omnissa Workspace ONE

After creating a private CA and SCEP connector in the AWS console, define the
certificate authority and template in Omnissa Workspace ONE.

###### Add AWS Private CA as a certificate authority

1. From the **System** menu, choose **Enterprise
   Integration** and then choose **Certificate
   Authorities**.
2. Choose **+ ADD** and provide the following
   information:
   - **Name**: AWS-Private-CA.
   - **Description**: AWS Private CA for device certificate
     issuance.
   - **Authority Type**: Select **Generic
     SCEP**.
   - **SCEP URL**: Enter the SCEP URL from AWS Private CA.
   - **Challenge Type**: Select
     **STATIC**.
   - **Static Challenge**: Enter the SCEP static challenge
     password from the Connector for SCEP configuration in the AWS console.
   - Enter the **Retry Timeout** and **Max
     Retries** values.

3. Save the configuration.

###### Create a certificate template

1. From the **System** menu, choose **Enterprise
   Integration**, choose **Certificate Authorities**,
   and then choose **Templates**.
2. Choose **Add Templates** and provide the following
   information:
   - **Template Name**: Device-Cert-Template.
   - **Certificate Authority**: Choose
     **AWS-Private-CA**.
   - **Subject Name**: This is a customizable field. You
     can choose variable values from a list of attributes. For example,
     CN={DeviceReportedName}, O={DevicePlatform},
     OU={CustomAttribute1}
   - **Private Key Length**: 2048 bits.
   - **Private Key Type**: Select
     **Signing** and **Encryption** as
     required
   - **Automatic Renewal**: Enabled/Disabled (Based on
     your needs).

3. Save the template.

## Step 2: Set up

an Omnissa Workspace ONE UEM profile configuration

Create a profile in Omnissa Workspace ONE UEM that directs devices to Connector for SCEP to issue a
certificate.

###### Create a SCEP device profile for certificate distribution

1. From the **Resources** menu, choose **Profiles &
   Baselines**, and then choose **Profiles**.
2. Choose **Add** then **Add Profile**
3. Select the device platform (**Android**,
   **iOS**, **macOS**,
   **Windows**).
4. Set the **Management type** and **Context**
   as appropriate.
5. Set the **Name**: Device-Cert-Profile.
6. Scroll to **SCEP Payload**.
7. Select **SCEP** and then choose
   **+Add**.
8. Use the following configuration:
   - **SCEP**:
     - For **Credential Source** select
       **Defined Certificate Authority**
       (Default).
     - For **Certificate Authority** select
       **AWS-Private-CA**
     - For **Certificate Template** select the
       **Device-Cert-Template** defined in Step
     1.

9. Choose **Next** and in the **Assignment**
   section select the right smart group from the list (assignment group for the
   device).
10. Select **Assignment type** as **Auto** to
    enable auto-renewal.
11. Save and publish the profile.

###### Note

For more information, see [SCEP](https://docs.omnissa.com/bundle/CertificateAuthorityIntegrationsV2302/page/SCEP.html "https://docs.omnissa.com/bundle/CertificateAuthorityIntegrationsV2302/page/SCEP.html") in the Omnissa documentation.

## Step 3: Enroll devices in

Omnissa Workspace ONE

###### Create or verify a smart group

1. From **Groups & Settings** choose
   **Groups** and then choose **Assignment
   Groups**.
2. Create or edit the POC-Devices smart group:
   - **Name**: POC-Devices.
   - **Device Type**: Select **All** or a
     specific platform (Android or iOS, for example).
   - **Criteria**: Use **UserGroup**,
     **Platform and OS**, **OEM and
     Model** to specify the criteria to group the target
     devices.
   - **Ownership**: Select **Any** for
     personal or corporate devices.

3. Save and verify the target devices appear in the **Preview**
   tab.

### Manual device enrollment

Android

- Download the **Workspace ONE Intelligent
  Hub** app from Google Play.
- Open the app and enter the enrollment URL or scan a QR
  code.
- Log in and follow the prompts to enroll as an MDM-managed
  device.

iOS/macOS

- On the device, open **Safari** and navigate
  to the enrollment URL
  (https://<WorkspaceONEUEMHostname>/enroll, for
  example).
- Log in with user credentials.
- Download and install the **Workspace ONE Intelligent
  Hub** app from the App Store.
- Follow prompts to install the MDM profile in
  **Settings** >
  **General** > **VPN & Device
  Management** > **Profile** >
  **Install**.

Windows

- Download the **Workspace ONE Intelligent
  Hub** from the Workspace ONE server or Microsoft
  Store.
- Enroll via the Hub using the enrollment URL and
  credentials.

Assign enrolled devices to the POC-Devices Smart Group in
**Devices** > **List View** >
**More Actions** > **Assign to Smart
Group**.

For more information, see [Automated Device Enrollment](https://docs.omnissa.com/bundle/Apple-Business-ManagerVSaaS/page/AppleBusinessManagerDeviceEnrollment.html "https://docs.omnissa.com/bundle/Apple-Business-ManagerVSaaS/page/AppleBusinessManagerDeviceEnrollment.html") in the Omnissa documentation.

###### Verify enrollment

1. In the Omnissa Workspace ONE UEM Console, go to **Devices** and then
   **List View**.
2. Confirm that your enrolled devices appear with the status set to
   **Enrolled**.
3. Verify devices are in the POC-Devices smart group in the
   **Groups** tab of the **Device
   Details**.

## Step 4: Issue a certificate

###### Trigger issuing a certificate

1. In **Devices**
   **List View**, select the enrolled device.
2. Choose on the **Query** button to prompt a check-in.
3. The Device-Cert-Profile should issue a certifcate via AWS Private CA.

**Verify certificate installation**

Android

Choose **Settings**, then **Security**,
then **Trusted Credentials**, and then
**User** to verify the certificate.

iOS

Go to **Settings**, then choose
**General**, then **VPN & Device
Management**, and then **Configuration
Profile**. Verify that the certificate from AWS-Private-CA is
present.

macOS

Open **Keychain Access** and then **System
Keychain** and verify the certificate.

Windows

Open **certmgr.msc**, then **Personal**,
and then **Certificates** to verify the certificate.

## Troubleshooting

SCEP Errors ("22013 - The SCEP server returned an invalid response" for
example)

- Verify the SCEP URL and static challenge password in Workspace ONE
  match AWS Private CA.
- Test SCEP endpoint connectivity: curl <SCEP_URL>.
- Check AWS CloudTrail logs for AWS Private CA errors
  (`IssueCertificate` failures, for example).

APNs issues (iOS/macOS)

- Make sure the APNs certificate is valid and assigned to the
  correct Organization Group.
- Test APNs connectivity: telnet [gateway.push.apple.com](http://gateway.push.apple.com/ "http://gateway.push.apple.com/") 2195.

Profile installation failures

- Confirm devices are in the correct Smart Group
  (**Devices**, then **List
  View**, and then **Groups**).
- Force a profile sync: **More Actions**, then
  **Send**, and then **Profile
  List**.

Logs

- Android: Use **Logcat** or Workspace ONE
  logs.
- iOS/macOS: log show --predicate 'process == "mdmclient"' --last 1h
  (via Xcode/Apple Configurator).
- Windows: **Event Viewer**, then
  **Applications and Services Logs** and then
  **Microsoft-Windows-DeviceManagement**.
- Workspace ONE UEM: **Monitor**, then
  **Reports & Analytics**, then
  **Events**, and then **Device
  Events**.

For detailed Connector for SCEP monitoring in AWS, see [**Monitor Connector for SCEP**](c4scep-monitoring-overview.md "c4scep-monitoring-overview.md").

## Security considerations

- Store SCEP URLs and secrets securely. For more information, see the [AWS Secrets Manager
  service](../../../secretsmanager.md "../../../secretsmanager.md").
- Restrict smart group criteria to target devices only.
- Regularly renew Apple Push Notifications (APNs) certificates (valid for 1
  year).
- Set short certificate validity periods for proof of concept projects to
  minimize risk.
- For personal devices, make sure cleanup removes all profiles and
  certificates.

For information about how to configure Omnissa Workspace ONE UEM and CA integration using a
SCEP connector, see the [SCEP in Omnissa Workspace ONE](https://docs.omnissa.com/bundle/CertificateAuthorityIntegrationsV2302/page/SCEP.html#:~:text=The%20exception%20to%20this%20requirement,Enable%20or%20disable%20the%20proxy. "https://docs.omnissa.com/bundle/CertificateAuthorityIntegrationsV2302/page/SCEP.html#:~:text=The%20exception%20to%20this%20requirement,Enable%20or%20disable%20the%20proxy.") documentation.
