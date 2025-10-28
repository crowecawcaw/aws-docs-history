# Apply an update manually

If a software update is available for your gateway, you can apply it manually by
following the procedure below. This manual update process ignores the maintenance window
schedule and applies the update immediately, even if maintenance updates are turned
off.

###### Note

The following procedure describes how to manually apply an update using the
Storage Gateway console. To perform this action programmatically using the API, see [UpdateGatewaySoftwareNow](https://amazonaws.com/storagegateway/latest/APIReference/API_UpdateGatewaySoftwareNow.html "https://amazonaws.com/storagegateway/latest/APIReference/API_UpdateGatewaySoftwareNow.html") in the _Storage Gateway API
Reference_.

###### To apply a gateway software update manually using the Storage Gateway console:

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. On the navigation pane, choose **Gateways**, and then choose
   the gateway you want to update.

If an update is available, the console displays a blue notification banner on
the gateway **Details** tab, which includes an option to apply
the update. 3. Choose **Apply update now** to immediately update the
gateway.

###### Note

This operation causes a temporary disruption to gateway functionality
while the update installs. During this time, the gateway status appears
**OFFLINE** in the Storage Gateway console. After the update
finishes installing, the gateway resumes normal operation and its status
changes to **RUNNING**.
You can verify that the gateway software was updated to the latest version by checking
the **Details** tab for the selected gateway in the Storage Gateway
console.
