# Outposts server end-of-term options

At the end of your AWS Outposts term, you must choose between the following options:

- [Renew your subscription](#renew-subscription "#renew-subscription") and keep your existing
  Outposts servers.
- [Return your Outposts servers](#end-subscription "#end-subscription").
- [Convert to a month-to-month subscription](#convert-subscription "#convert-subscription") and
  keep your existing Outposts servers.

## Renew your subscription

You must complete the following steps at least **5 business
days** before the current subscription for your Outposts servers ends. Failing to complete
these steps at least 5 business days before the current subscription ends might result in
unanticipated charges.

###### To renew your subscription and keep your existing Outposts servers

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. In the navigation pane, choose **Outposts**.
3. Choose **Actions**.
4. Choose **Renew Outpost**.
5. Choose the subscription term length and payment option.

For pricing, see [AWS Outposts servers
pricing](https://aws.amazon.com/outposts/servers/pricing/ "https://aws.amazon.com/outposts/servers/pricing/"). You can also request a price quote. 6. Choose **Submit support ticket**.

###### Note

If renewing before the current subscription for your Outposts servers ends, you will be charged
immediately for any upfront fees.

Your new subscription will start the day after your current subscription ends.

If you do not indicate that you want to renew your subscription or return your Outposts server, you
will be converted to a month-to-month subscription automatically. Your Outpost will be renewed on
a monthly basis at the rate of the **No Upfront** payment option
that corresponds to your AWS Outposts configuration. Your new monthly subscription will start the day
after your current subscription ends.

## Return Outposts servers

To return a server because the server reached the end of the contract term, you must first
complete the decommission process at least **5 business days**
before the current subscription for your Outposts servers ends. AWS can't start the return process
until you do so. Failing to complete the decommission process at least 5 business days before the
current subscription ends might result in delays in decommissioning and unanticipated
charges.

After you complete the decommission process, you must prepare the server for return, obtain
the shipping label, and pack and return the server to AWS.

You will not be charged a shipping fee when you return an Outposts server. However, if you
return a server that is damaged, you might incur a cost.

###### Tasks

- [Step 1: Prepare the server for return](#prepare-server-for-return "#prepare-server-for-return")
- [Step 2: Decommission the server](#decommision-server "#decommision-server")
- [Step 3: Obtain the return shipping label](#get-shipping-label "#get-shipping-label")
- [Step 4: Pack the server](#package-server "#package-server")
- [Step 5: Return the server through the courier](#get-server-to-courier "#get-server-to-courier")

### Step 1: Prepare the server for return

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

### Step 2: Decommission the server

Complete the following steps at least **5 business days**
before the current subscription for your Outposts servers ends.

###### Important

AWS can't stop the return process after you have submitted your decommission
request.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. In the navigation pane, choose **Outposts**.
3. Choose **Actions**.
4. Choose **Decommission Outpost** and follow the workflow to delete resources.
5. Choose **Submit request**.

###### Note

Returning your Outposts servers before the current subscription ends will not terminate any
outstanding charges associated with this Outpost.

### Step 3: Obtain the return shipping label

###### Important

You must only use the shipping label that AWS provides because it contains specific
information, such as the Asset ID, about the server that you are returning. Do not create your
own shipping label.

###### To obtain your shipping label:

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. On the navigation pane, choose **Orders**.
3. Choose the order for the server you want to return.
4. On the order details page, in the **Order status** section, choose **Print return
   label**.

###### Note

Returning your Outposts servers before the current subscription ends will not terminate any
outstanding charges associated with this Outpost.

### Step 4: Pack the server

To pack your server, use the box and packaging material provided by AWS.

1.  Pack the server in one of the following boxes:

        * The box and packaging material that the server originally came in.
        * The box and packaging material that the replacement server came in.

    Alternatively, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to request a box.

2.  Affix the shipping label that AWS provided, to the outside of the box.

###### Important

Verify that the Asset ID on the shipping label matches the Asset ID on the server that
you are returning.

The Asset ID is located on the pull-out tab on the front of the server. Example:
`1203779889` or `9305589922` 3. Seal the box securely.

### Step 5: Return the server through the courier

You must return the server through the designated courier for your country. You can deliver
the server to the courier or schedule the day and time that you prefer for the courier to pick up
the server. The shipping label that AWS provides contains the correct address to return the
server.

The following table shows who to contact for the country you are shipping from:

| Country                  | Contact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Argentina                | Contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). In your request, include the<br>following information:<br>• The tracking number that is on the AWS-provided shipping label<br>• The date and time that you prefer the courier to pick up the server<br>• A contact name<br>• A phone number<br>• An email address                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Bahrain                  |
| Brazil                   |
| Brunei                   |
| Canada                   |
| Chile                    |
| Colombia                 |
| Hong Kong                |
| India                    |
| Indonesia                |
| Japan                    |
| Malaysia                 |
| Nigeria                  |
| Oman                     |
| Panama                   |
| Peru                     |
| Philippines              |
| Serbia                   |
| Singapore                |
| South Africa             |
| South Korea              |
| Taiwan                   |
| Thailand                 |
| United Arab Emirates     |
| Vietnam                  |
| United States of America | Contact [UPS](https://www.ups.com "https://www.ups.com").<br>You can return the server in the following ways:<br>• Return the server during a routine UPS pickup at your site.<br>• Drop-off the server at a [UPS<br>location](https://www.ups.com/dropoff?loc=en_US "https://www.ups.com/dropoff?loc=en_US").<br>• Schedule a [pickup](https://wwwapps.ups.com/pickup/schedule?loc=en_US "https://wwwapps.ups.com/pickup/schedule?loc=en_US") for a date and time you prefer. Enter the tracking number from the<br>AWS-provided shipping label for free shipping.                                                                                                                                                                                                                                                               |
| All other countries      | Contact [DHL](https://www.dhl.com "https://www.dhl.com").<br>You can return the server in the following ways:<br>• Drop-off the server at a [DHL<br>location](https://mydhl.express.dhl/us/en/locator.html#/find-locations "https://mydhl.express.dhl/us/en/locator.html#/find-locations").<br>• Schedule a [pickup](https://returns.dhl.co.uk/ereturns/ "https://returns.dhl.co.uk/ereturns/") for a date<br>and time you prefer. Enter the DHL Waybill number from the AWS-provided shipping label<br>for free shipping.<br>If you get the following error `Courier pickup can't be scheduled for an import<br>shipment`, it usually means that the pickup country that you selected does not<br>match the pickup country on the return shipment label. Select the country where the<br>shipment originates from and try again. |

## Convert to a month-to-month subscription

To convert to a month-to-month subscription and keep your existing Outposts servers, no action is
needed. If you have questions, open a billing support case.

Your Outpost will be renewed on a monthly basis at the rate of the **No
Upfront** payment option that corresponds to your AWS Outposts configuration. Your new monthly
subscription starts the day after your current subscription ends.
