# Editing Basic Gateway Information

You can use the Storage Gateway console to edit basic information for an existing gateway,
including the gateway name, time zone, and CloudWatch log group.

###### To edit basic information for an existing gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then choose the gateway for which you want
   to edit basic information.
3. From the **Actions** dropdown menu, choose **Edit gateway
   information**.
4. For **Gateway name**, enter a name for your gateway. You can
   search for this name to find your gateway on the list pages in the Storage Gateway
   console.

###### Note

Gateway names must be between 2 and 255 characters, and cannot include a slash
(`\` or `/`).

Changing a gateway's name will disconnect any CloudWatch alarms set up to monitor
the gateway. To reconnect the alarms, update the
**GatewayName** for each alarm in the CloudWatch console. 5. For **Gateway time zone**, choose the local time zone for the
part of the world where you want to deploy your gateway. 6. For **Choose how to set up log group**, choose how to set up
Amazon CloudWatch Logs to monitor the health of your gateway. You can choose from the following
options:

    * **Create a new log group** – Set up a new log group to
     monitor your gateway.
    * **Use an existing log group** – Choose an existing log
     group from the corresponding dropdown list.
    * **Deactivate logging** – Do not use Amazon CloudWatch Logs to monitor
     your gateway.

7. When you finish modifying the settings you want to change, choose **Save
   changes**.
