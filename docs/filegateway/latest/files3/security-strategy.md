# Set a security level for your gateway

By using a S3 File Gateway, you can specify a security level for your gateway. By
specifying this security level, you can set whether your gateway should require
Server Message Block (SMB) signing or SMB encryption, or whether you want to allow
SMB version 1.

###### To configure security level

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then choose the gateway for which
   you want to edit SMB settings.
3. From the **Actions** dropdown menu, choose **Edit
   SMB settings**, then choose **SMB security
   settings**.
4. For **Security level**, choose one of the
   following:

###### Note

For information about configuring this setting using the AWS API, see [UpdateSMBSecurityStrategy](../../../storagegateway/latest/APIReference/API_UpdateSMBSecurityStrategy.md "../../../storagegateway/latest/APIReference/API_UpdateSMBSecurityStrategy.md") in the _AWS Storage Gateway API Reference_.

A higher security strategy level can affect performance of the
gateway.

    * **Enforce AES256 encryption** – If you
     choose this option, S3 File Gateway only allows connections from SMBv3
     clients that use 256-bit AES encryption algorithms. 128-bit
     algorithms are not allowed. This option is recommended for
     environments that handle sensitive data. It works with all current
     SMB clients on Microsoft Windows.
    * **Enforce encryption** – If you choose
     this option, S3 File Gateway only allows connections from SMBv3 clients
     that have encryption turned on. Both 256-bit and 128-bit algorithms
     are allowed. This option is recommended for environments that handle
     sensitive data. It works with all current SMB clients on Microsoft
     Windows.
    * **Enforce signing** – If you choose this
     option, S3 File Gateway only allows connections from SMBv2 or SMBv3 clients
     that have signing turned on. This option works with all current SMB
     clients on Microsoft Windows.
    * **Client negotiated** – If you choose this
     option, requests are established based on what is negotiated by the
     client. This option is recommended when you want to maximize
     compatibility across different clients in your environment.

###### Note

For gateways activated before June 20, 2019, the default security
level is **Client negotiated**.

For gateways activated on June 20, 2019 and later, the default
security level is **Enforce encryption**. 5. Choose **Save**.
