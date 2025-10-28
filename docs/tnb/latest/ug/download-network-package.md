# Download a network package from

AWS TNB

Learn how to download a network package from the AWS TNB network service
catalog.

Console

###### To download a network package using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Network
   packages**.
3. Use the search box to find the network package
4. Choose the network package.
5. Choose **Actions**,
   **Download**.

AWS CLI

###### To download a network package using the AWS CLI

- Use the [get-sol-network-package-content](../../../cli/latest/reference/tnb/get-sol-network-package-content.md "../../../cli/latest/reference/tnb/get-sol-network-package-content.md") command to download a network
  package.

```
aws tnb get-sol-network-package-content \
--nsd-info-id `^np-[a-f0-9]{17}$` \
--accept "application/zip" \
--endpoint-url "`https://tnb.us-west-2.amazonaws.com`" \
--region `us-west-2`
```
