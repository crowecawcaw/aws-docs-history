# View or edit an AWS Cloud WAN core network Direct Connect

gateway attachment

You can update the edge locations for a Direct Connect gateway attachment using either the Network Manager
console or using the AWS CLI. The Direct Connect gateway attachment must first be created using
the Direct Connect console. For more information about Direct Connect gateway attachments and
Cloud WAN, see [Direct Connect gateway
attachments](cloudwan-dxattach-about.md "cloudwan-dxattach-about.md").

###### Topics

- [View or edit a Direct Connect gateway
  attachment using the console](#cloudwan-dxattachment-update-console "#cloudwan-dxattachment-update-console")
- [Update a Direct Connect gateway attachment
  using the command line or API](#cloudwan-dxattachment-update-cli "#cloudwan-dxattachment-update-cli")

## View or edit a Direct Connect gateway

attachment using the console

Use the following steps he following steps to update the edge locations for a Direct Connect
gateway attachment. The updated edge locations are automatically associated with the
Direct Connect gateway on Direct Connect console.

###### To add a Direct Connect gateway attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.
4. In the navigation pane under he name of the global network, choose **Attachments**.
5. Choose the Direct Connect gateway attachment you want to update, and then choose
   **Edit**.
6. In the **Direct Connect attachment** section, add or remove
   **Edge locations**, and then choose **Edit
   attachment**.

## Update a Direct Connect gateway attachment

using the command line or API

Use the command line or API to update a Direct Connect gateway attachment.

###### To create a Direct Connect gateway attachment using the command line or API

- Use `update-direct-connect-gateway-attachment`. See [update-direct-connect-gateway-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-direct-connect-gateway-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-direct-connect-gateway-attachment.html").
