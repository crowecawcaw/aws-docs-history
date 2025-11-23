# Restrict access to trusted devices for WorkSpaces Personal

By default, users can access their WorkSpaces from any supported device that is
connected to the internet. If your company limits corporate data access to trusted
devices (also known as managed devices), you can restrict WorkSpaces access to
trusted devices with valid certificates.

###### Note

This feature is currently available only when your WorkSpaces Personal directories are
managed through Directory Service including Simple AD, AD Connector, and AWS Managed Microsoft AD directory.

When you enable this feature, WorkSpaces uses certificate-based authentication
to determine whether a device is trusted. If the WorkSpaces client application
can't verify that a device is trusted, it blocks attempts to log in or reconnect
from the device.

For each directory, you can import up to two root certificates. If you import
two root certificates, WorkSpaces presents them both to the client and the client
finds the first valid matching certificate that chains up to either of the
root certificates.

###### Supported clients

- Android, running on Android or Android-compatible Chrome OS systems
- macOS
- Windows

###### Important

This feature is not supported by the following clients:

- WorkSpaces client applications for Linux or iPad
- Third-party clients, including but not limited to, Teradici PCoIP, RDP clients,
  and remote desktop applications.

###### Note

When you enable access for specific clients, make sure that you block access for other
device types that you don't need. For more information about how to do this, see Step 3.7
below.

## Step 1: Create the certificates

This feature requires two types of certificates: root certificates generated
by an internal Certificate Authority (CA) and client certificates that chain
up to a root certificate.

###### Requirements

- Root certificates must be Base64-encoded certificate files in CRT, CERT, or PEM format.
- Root certificates must satisfy the following regular expression pattern, which means that every encoded line,
  beside the last one, has to be exactly 64 characters long: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}
\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)`.
- Device certificates must include a Common Name.
- Device certificates must include the following extensions: `Key Usage: Digital Signature`,
  and `Enhanced Key Usage: Client Authentication`.
- All the certificates in the chain from the device certificate to the trusted root Certificate Authority
  must be installed on the client device.
- The maximum supported length of certificate chain is 4.
- WorkSpaces does not currently support device revocation mechanisms, such as certificate revocation lists (CRL)
  or Online Certificate Status Protocol (OCSP), for client certificates.
- Use a strong encryption algorithm. We recommend SHA256 with RSA, SHA256 with ECDSA,
  SHA384 with ECDSA, or SHA512 with ECDSA.
- For macOS, if the device certificate is in the system keychain, we recommend that
  you authorize the WorkSpaces client application to access those certificates. Otherwise, users
  must enter keychain credentials when they log in or reconnect.

## Step 2: Deploy client certificates to the trusted devices

On the trusted devices for your users, you must install a certificate bundle that includes all the certificates
in the chain from the device certificate to the trusted root Certificate Authority.
You can use your preferred solution to install certificates to your fleet of client devices;
for example, System Center Configuration Manager (SCCM) or mobile device management (MDM). Note that
SCCM and MDM can optionally perform a security posture assessment to determine whether the devices
meet your corporate policies to access WorkSpaces.

The WorkSpaces client applications search for certificates as follows:

- Android - Go to **Settings**, choose **Security & location**,
  **Credentials**, then choose **Install from SD card**.
- Android-compatible Chrome OS systems - Open Android settings and choose **Security & location**,
  **Credentials**, then choose **Install from SD card**.
- macOS - Searches the keychain for client certificates.
- Windows - Searches the user and root certificate stores for client certificates.

## Step 3: Configure the restriction

After you have deployed the client certificates on the trusted devices,
you can enable restricted access at the directory level. This requires the
WorkSpaces client application to validate the certificate on a device
before allowing a user to log in to a WorkSpace.

###### To configure the restriction

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Select the directory and then choose **Actions**,
   **Update Details**.
4. Expand **Access Control Options**.
5. Under **For each device type, specify which devices can access
   WorkSpaces**, choose **Trusted Devices**.
6. Import up to two root certificates. For each root certificate, do the following:
   1. Choose **Import**.
   2. Copy the body of the certificate to the form.
   3. Choose **Import**.

7. Specify whether other types of devices have access to WorkSpaces.
   1. Scroll down to the **Other Platforms** section. By default,
      WorkSpaces Linux clients are disabled, and users can access their WorkSpaces from their
      iOS devices, Android devices, Web Access, Chromebooks, and PCoIP zero client devices.
   2. Select the device types to enable and clear the device types to disable.
   3. To block access from all selected device types, choose **Block**.

8. Choose **Update and Exit**.
