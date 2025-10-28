# Return an Outposts server

###### Note

If you received a server that was damaged in shipping, see [Step 2: Inspect the Outposts server equipment](../install-server/install-inspect.md "../install-server/install-inspect.md") in the _AWS Outposts server installation guide_.

To return a server that is in use and you want to replace or a server whose subscription has ended, review this section.

If AWS Outposts detects a defect in a server, we will inform you, start the replacement
process to send you a new server, and provide you with the return label through the AWS Outposts
console. You will not be charged a shipping fee when you return an Outposts server. However, if
you return a server that is damaged, you might incur a cost.

To get started, complete the following steps.

###### Tasks

- [Step 1: Prepare the server for return](#prepare-server-for-return "#prepare-server-for-return")
- [Step 2: Print the return label](#get-shipping-label "#get-shipping-label")
- [Step 3: Pack the server](#package-server "#package-server")
- [Step 4: Return the server through the courier](#get-server-to-courier "#get-server-to-courier")

## Step 1: Prepare the server for return

To prepare the server for return, unshare resources, backup data, delete local network
interfaces and terminate active instances.

1. If the Outpost's resources are shared, you must unshare these resources.

You can unshare a shared Outpost resource in one of the following ways:

    * Use the AWS RAM console. For more information, see [Updating a resource
     share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the *AWS RAM User Guide*.
    * Use the AWS CLI to run the [disassociate-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html") command.

For the list of Outpost resources that can be shared, see [Shareable Outpost
resources](../userguide/sharing-outposts.md#sharing-resources "../userguide/sharing-outposts.md#sharing-resources"). 2. Create backups of the data stored in the instance storage of the Amazon EC2 instances running
on the AWS Outposts server. 3. Delete the local network interfaces associated with the instances that were running on the
server. 4. Terminate the active instances associated with subnets on your Outpost. To terminate the
instances, follow the instructions in [Terminate your instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in
the _Amazon EC2 User Guide_. 5. Destroy the Nitro Security Key (NSK) to cryptographically shred your data on the server.
To destroy the NSK, follow the instructions in [Cryptographically shred server data](outpost-maintenance.md#outpost-server-cryptographically-shred-data "outpost-maintenance.md#outpost-server-cryptographically-shred-data").

## Step 2: Print the return label

###### Important

You must only use the return label that AWS provides because it contains specific
information, such as the Asset ID, about the server that you are returning. Do not create your
own return label.

###### To obtain your return label:

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. On the navigation pane, choose **Orders**.
3. Choose the order for the server you want to return.
4. On the order details page, in the **Order status** section, choose **Print return
   label**.

###### Note

Returning your Outposts servers before the current subscription ends will not terminate any
outstanding charges associated with this Outpost.

## Step 3: Pack the server

To pack your server, use the box and packaging material provided by AWS.

1.  Pack the server in one of the following boxes:

        * The box and packaging material that the server originally came in.
        * The box and packaging material that the replacement server came in.

    Alternatively, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to request a box.

2.  Affix the return label that AWS provided, to the outside of the box.

###### Important

Verify that the Asset ID on the return label matches the Asset ID on the server that
you are returning.

The Asset ID is located on the pull-out tab on the front of the server. Example:
`1203779889` or `9305589922` 3. Seal the box securely.

## Step 4: Return the server through the courier

You must return the server through the designated courier for your country. You can deliver
the server to the courier or schedule the day and time that you prefer for the courier to pick up
the server. The return label that AWS provides contains the correct address to return the
server.

The following table shows who to contact for the country you are shipping from:

| Country                  | Contact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Argentina                | Contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). In your request, include the following information: <br>• The tracking number that is on the AWS-provided return label <br>• The date and time that you prefer the courier to pick up the server <br>• A contact name <br>• A phone number <br>• An email address                                                                                                                                                                                                                                                                                                                                                                                                            |
| Bahrain                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Brazil      |
| Brunei                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Canada      |
| Chile                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Colombia    |
| Hong Kong                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | India       |
| Indonesia                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Japan       |
| Malaysia                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Nigeria     |
| Oman                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Panama      |
| Peru                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Philippines |
| Serbia                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Singapore   |
| South Africa             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | South Korea |
| Taiwan                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Thailand    |
| United Arab Emirates     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Vietnam     |
| Mexico                   | AWS contacts [DB Schenker](https://www.dbschenker.com/global "https://www.dbschenker.com/global") and requests a pickup from your location. DB Schenker then contacts you to schedule the date and time for the pickup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| United States of America | Contact [UPS](https://www.ups.com "https://www.ups.com"). You can return the server in the following ways: <br>• Return the server during a routine UPS pickup at your site. <br>• Drop-off the server at a [UPS location](https://www.ups.com/dropoff?loc=en_US "https://www.ups.com/dropoff?loc=en_US"). <br>• Schedule a [pickup](https://wwwapps.ups.com/pickup/schedule?loc=en_US "https://wwwapps.ups.com/pickup/schedule?loc=en_US") for a date and time you prefer. Enter the tracking number from the AWS-provided return label for free shipping.                                                                                                                                                                                                                                               |
| All other countries      | Contact [DHL](https://www.dhl.com "https://www.dhl.com"). You can return the server in the following ways: <br>• Drop-off the server at a [DHL location](https://mydhl.express.dhl/us/en/locator.html#/find-locations "https://mydhl.express.dhl/us/en/locator.html#/find-locations"). <br>• Schedule a [pickup](https://returns.dhl.co.uk/ereturns/ "https://returns.dhl.co.uk/ereturns/") for a date and time you prefer. Enter the DHL Waybill number from the AWS-provided return label for free shipping. If you get the following error `Courier pickup can't be scheduled for an import shipment`, it usually means that the pickup country that you selected does not match the pickup country on the return shipment label. Select the country where the shipment originates from and try again. |
