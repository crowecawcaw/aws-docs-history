

# Outposts server end-of-term options
<a name="term-end-server"></a>

At the end of your AWS Outposts term, you must choose between the following options:
+ [Renew your subscription](#renew-subscription) and keep your existing Outposts servers.
+ [Return your Outposts servers](#end-subscription).
+ [Convert to a month-to-month subscription](#convert-subscription) and keep your existing Outposts servers.

## Renew your subscription
<a name="renew-subscription"></a>

You must complete the following steps at least **5 business days** before the current subscription for your Outposts servers ends. Failing to complete these steps at least 5 business days before the current subscription ends might result in unanticipated charges.

**To renew your subscription and keep your existing Outposts servers**

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. In the navigation pane, choose **Outposts**.

1. Choose **Actions**.

1. Choose **Renew Outpost** and follow the workflow.

**Note**  
If renewing before the current subscription for your Outposts servers ends, you will be charged immediately for any upfront fees.

Your new subscription will start the day after your current subscription ends.

If you do not indicate that you want to renew your subscription or return your Outposts server, you will be converted to a month-to-month subscription automatically. Your Outpost will be renewed on a monthly basis at the rate of the **No Upfront** payment option that corresponds to your AWS Outposts configuration. Your new monthly subscription will start the day after your current subscription ends.

## Return Outposts servers
<a name="end-subscription"></a>

To return a server because the server reached the end of the contract term, you must first complete the decommission process at least **5 business days** before the current subscription for your Outposts servers ends. AWS can't start the return process until you do so. Failing to complete the decommission process at least 5 business days before the current subscription ends might result in delays in decommissioning and unanticipated charges.

After you complete the decommission process, you must prepare the server for return, obtain the shipping label, and pack and return the server to AWS.

You will not be charged a shipping fee when you return an Outposts server. However, if you return a server that is damaged, you might incur a cost.

**Topics**
+ [Step 1: Prepare the server for return](#prepare-server-for-return)
+ [Step 2: Decommission the server](#decommision-server)
+ [Step 3: Obtain the return shipping label](#get-shipping-label)
+ [Step 4: Pack the server](#package-server)
+ [Step 5: Return the server through the courier](#get-server-to-courier)

### Step 1: Prepare the server for return
<a name="prepare-server-for-return"></a>

To prepare the server for return, unshare resources, backup data, delete local network interfaces and terminate active instances.

1. If the Outpost's resources are shared, you must unshare these resources.

   You can unshare a shared Outpost resource in one of the following ways:
   + Use the AWS RAM console. For more information, see [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the *AWS RAM User Guide*.
   + Use the AWS CLI to run the [disassociate-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html) command.

   For the list of Outpost resources that can be shared, see [Shareable Outpost resources](https://docs.aws.amazon.com/outposts/latest/userguide/sharing-outposts.html#sharing-resources).

1. Create backups of the data stored in the instance storage of the Amazon EC2 instances running on the AWS Outposts server.

1. Delete the local network interfaces associated with the instances that were running on the server.

1. Terminate the active instances associated with subnets on your Outpost. To terminate the instances, follow the instructions in [Terminate your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html) in the *Amazon EC2 User Guide*.

1. Destroy the Nitro Security Key (NSK) to cryptographically shred your data on the server. To destroy the NSK, follow the instructions in [Cryptographically shred server data](https://docs.aws.amazon.com/outposts/latest/server-userguide/outpost-maintenance.html#outpost-server-cryptographically-shred-data).

### Step 2: Decommission the server
<a name="decommision-server"></a>

Complete the following steps at least **5 business days** before the current subscription for your Outposts servers ends.
**Important**  
AWS can't stop the return process after you have submitted your decommission request.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. In the navigation pane, choose **Outposts**.

1. Choose **Actions**.

1. Choose **Decommission Outpost** and follow the workflow to delete resources.

1. Choose **Submit request**.

**Note**  
Returning your Outposts servers before the current subscription ends will not terminate any outstanding charges associated with this Outpost.

### Step 3: Obtain the return shipping label
<a name="get-shipping-label"></a>

**Important**  
You must only use the shipping label that AWS provides because it contains specific information, such as the Asset ID, about the server that you are returning. Do not create your own shipping label.

**To obtain your shipping label:**

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. On the navigation pane, choose **Orders**.

1. Choose the order for the server you want to return.

1. On the order details page, in the **Order status** section, choose **Print return label**.

**Note**  
Returning your Outposts servers before the current subscription ends will not terminate any outstanding charges associated with this Outpost.

### Step 4: Pack the server
<a name="package-server"></a>

To pack your server, use the box and packaging material provided by AWS.

1. Pack the server in one of the following boxes:
   + The box and packaging material that the server originally came in.
   + The box and packaging material that the replacement server came in.

   Alternatively, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/) to request a box.

1. Affix the shipping label that AWS provided, to the outside of the box.
**Important**  
Verify that the Asset ID on the shipping label matches the Asset ID on the server that you are returning.  
The Asset ID is located on the pull-out tab on the front of the server. Example: `1203779889` or `9305589922`

1. Seal the box securely.

### Step 5: Return the server through the courier
<a name="get-server-to-courier"></a>

You must return the server through the designated courier for your country. You can deliver the server to the courier or schedule the day and time that you prefer for the courier to pick up the server. The shipping label that AWS provides contains the correct address to return the server.

The following table shows who to contact for the country you are shipping from:


<table>
<thead>
  <tr><th>Country</th><th>Contact</th></tr>
</thead>
<tbody>
  <tr><td>Argentina</td><td rowspan="25">Contact <a href="https://console.aws.amazon.com/support/home#/">AWS Support Center</a>. In your request, include the following information:<ul><li> The tracking number that is on the AWS-provided shipping label </li><li> The date and time that you prefer the courier to pick up the server </li><li> A contact name </li><li> A phone number </li><li> An email address </li></ul></td></tr>
  <tr><td>Bahrain</td></tr>
  <tr><td>Brazil</td></tr>
  <tr><td>Brunei</td></tr>
  <tr><td>Canada</td></tr>
  <tr><td>Chile</td></tr>
  <tr><td>Colombia</td></tr>
  <tr><td>Hong Kong</td></tr>
  <tr><td>India</td></tr>
  <tr><td>Indonesia</td></tr>
  <tr><td>Japan</td></tr>
  <tr><td>Malaysia</td></tr>
  <tr><td>Nigeria</td></tr>
  <tr><td>Oman</td></tr>
  <tr><td>Panama</td></tr>
  <tr><td>Peru</td></tr>
  <tr><td>Philippines</td></tr>
  <tr><td>Serbia</td></tr>
  <tr><td>Singapore</td></tr>
  <tr><td>South Africa</td></tr>
  <tr><td>South Korea</td></tr>
  <tr><td>Taiwan</td></tr>
  <tr><td>Thailand</td></tr>
  <tr><td>United Arab Emirates</td></tr>
  <tr><td>Vietnam</td></tr>
  <tr><td>United States of America</td><td>Contact <a href="https://www.ups.com">UPS</a>.<br />You can return the server in the following ways:<ul><li> Return the server during a routine UPS pickup at your site. </li><li> Drop-off the server at a <a href="https://www.ups.com/dropoff?loc=en_US">UPS location</a>. </li><li> Schedule a <a href="https://wwwapps.ups.com/pickup/schedule?loc=en_US">pickup</a> for a date and time you prefer. Enter the tracking number from the AWS-provided shipping label for free shipping. </li></ul></td></tr>
  <tr><td>All other countries</td><td>Contact <a href="https://www.dhl.com">DHL</a>.<br />You can return the server in the following ways:<ul><li> Drop-off the server at a <a href="https://mydhl.express.dhl/us/en/locator.html#/find-locations">DHL location</a>. </li><li> Schedule a <a href="https://returns.dhl.co.uk/ereturns/">pickup</a> for a date and time you prefer. Enter the DHL Waybill number from the AWS-provided shipping label for free shipping. <br />If you get the following error <code>Courier pickup can't be scheduled for an import shipment</code>, it usually means that the pickup country that you selected does not match the pickup country on the return shipment label. Select the country where the shipment originates from and try again. </li></ul></td></tr>
</tbody>
</table>


## Convert to a month-to-month subscription
<a name="convert-subscription"></a>

To convert to a month-to-month subscription and keep your existing Outposts servers, no action is needed. If you have questions, open a billing support case.

Your Outpost will be renewed on a monthly basis at the rate of the **No Upfront** payment option that corresponds to your AWS Outposts configuration. Your new monthly subscription starts the day after your current subscription ends.