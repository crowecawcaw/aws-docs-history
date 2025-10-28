# Editing SMB settings for a gateway

Gateway-level SMB settings let you configure the security strategy, Active Directory
authentication, guest access, local group permissions, and file share visibility for the
SMB file shares on a gateway.

###### To edit gateway level SMB settings

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then choose the gateway for which you
   want to edit SMB settings.
3. From the **Actions** dropdown menu, choose **Edit SMB
   settings**, then choose the settings you want to edit.
   This section contains the following topics, which provide additional information and
   procedures related to configuring each of the individual SMB settings for your
   gateway.

**Topics**

- [Set gateway security
  level](security-strategy.md "security-strategy.md") -
  Learn how to set a security level to specify connection requirements such as
  Server Message Block (SMB) signing and encryption, and whether to allow
  connections from SMB version 1 clients.
- [Configure Active Directory
  authentication](enable-ad-settings.md "enable-ad-settings.md")

* Learn how to configure your corporate Active Directory or AWS Managed
  Microsoft AD for user authenticated access to your SMB file share.

- [Provide guest access](guest-access.md "guest-access.md") - Learn how
  to configure your gateway to allow guest access for any user that provides the
  correct guest account username and password.
- [Configure local
  groups](local-group-settings.md "local-group-settings.md") - Learn how to configure local
  groups to grant Active Directory users special file share permissions.
- [Set file share visibility](file-share-visibility.md "file-share-visibility.md")

* Learn how to specify whether the shares on a gateway are visible when listing
  shares to users.
