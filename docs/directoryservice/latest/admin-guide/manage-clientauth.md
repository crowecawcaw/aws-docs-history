# Managing smart card authentication settings

You can use two different methods to manage smart card settings. You can use either the
AWS Management Console method or the AWS CLI method.

###### Topics

- [View certificate details](#describe-a-certificate-clientauth "#describe-a-certificate-clientauth")
- [Deregister a certificate](#dergister-a-certificate-clientauth "#dergister-a-certificate-clientauth")
- [Disable smart card authentication](#disable-smart-card-clientauth "#disable-smart-card-clientauth")

## View certificate details

Use either of the following methods to see when a certificate is set to expire.

###### Method 1: To view certificate details in AWS Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your AD Connector directory.
3. On the **Directory details** page, choose the **Networking
   & security** tab.
4. In the **Smart card authentication** section, under **CA
   certificates**, choose the certificate ID to display details about that
   certificate.

###### Method 2: To view certificate details in AWS Directory Service (AWS CLI)

- Run the following command. For the certificate ID, use the identifier returned by
  `register-certificate` or `list-certificates`.

```
aws ds describe-certificate --directory-id `your_directory_id` --certificate-id `your_cert_id`
```

## Deregister a certificate

Use either of the following methods to deregister a certificate.

###### Note

If only one certificate is registered, you must first disable smart card
authentication before you can deregister the certificate.

###### Method 1: To deregister a certificate in AWS Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your AD Connector directory.
3. On the **Directory details** page, choose the **Networking
   & security** tab.
4. In the **Smart card authentication** section, under **CA
   certificates**, select the certificate you want to deregister, choose
   **Actions**, and then choose **Deregister
   certificate**.

###### Important

Ensure that the certificate you are about to deregister is not active or is
currently being used as part of a CA certificate chain for smart card
authentication. 5. In the **Deregister a CA certificate** dialog box, choose
**Deregister**.

###### Method 2: To deregister a certificate in AWS Directory Service (AWS CLI)

- Run the following command. For the certificate ID, use the identifier returned by
  `register-certificate` or `list-certificates`.

```
aws ds deregister-certificate --directory-id `your_directory_id` --certificate-id `your_cert_id`
```

## Disable smart card authentication

Use either of the following methods to disable smart card authentication.

###### Method 1: To disable smart card authentication in AWS Directory Service (AWS Management Console)

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your AD Connector directory.
3. On the **Directory details** page, choose the **Networking
   & security** tab.
4. In the **Smart card authentication** section, choose
   **Disable**.
5. In the **Disable smart card authentication** dialog box, choose
   **Disable**.

###### Method 2: To disable smart card authentication in AWS Directory Service (AWS CLI)

- Run the following command.

```
aws ds disable-client-authentication --directory-id `your_directory_id` --type SmartCard
```
