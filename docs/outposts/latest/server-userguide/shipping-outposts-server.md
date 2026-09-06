

# Return an Outposts server
<a name="shipping-outposts-server"></a>

**Note**  
If you received a server that was damaged in shipping, see [Step 2: Inspect the Outposts server equipment](https://docs.aws.amazon.com/outposts/latest/install-server/install-inspect.html) in the *AWS Outposts server installation guide*.  
To return a server that is in use and you want to replace or a server whose subscription has ended, review this section.

If AWS Outposts detects a defect in a server, we will inform you, start the replacement process to send you a new server, and provide you with the return label through the AWS Outposts console. You will not be charged a shipping fee when you return an Outposts server. However, if you return a server that is damaged, you might incur a cost.

To get started, complete the following steps.

**Topics**
+ [Step 1: Prepare the server for return](#prepare-server-for-return)
+ [Step 2: Print the return label](#get-shipping-label)
+ [Step 3: Pack the server](#package-server)
+ [Step 4: Return the server through the courier](#get-server-to-courier)

## Step 1: Prepare the server for return
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

## Step 2: Print the return label
<a name="get-shipping-label"></a>

**Important**  
You must only use the return label that AWS provides because it contains specific information, such as the Asset ID, about the server that you are returning. Do not create your own return label.

**To obtain your return label:**

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. On the navigation pane, choose **Orders**.

1. Choose the order for the server you want to return.

1. On the order details page, in the **Order status** section, choose **Print return label**.

**Note**  
Returning your Outposts servers before the current subscription ends will not terminate any outstanding charges associated with this Outpost.

## Step 3: Pack the server
<a name="package-server"></a>

To pack your server, use the box and packaging material provided by AWS.

1. Pack the server in one of the following boxes:
   + The box and packaging material that the server originally came in.
   + The box and packaging material that the replacement server came in.

   Alternatively, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/) to request a box.

1. Affix the return label that AWS provided, to the outside of the box.
**Important**  
Verify that the Asset ID on the return label matches the Asset ID on the server that you are returning.  
The Asset ID is located on the pull-out tab on the front of the server. Example: `1203779889` or `9305589922`

1. Seal the box securely.

## Step 4: Return the server through the courier
<a name="get-server-to-courier"></a>

You must return the server through the designated courier for your country. You can deliver the server to the courier or schedule the day and time that you prefer for the courier to pick up the server. The return label that AWS provides contains the correct address to return the server.

The following table shows who to contact for the country you are shipping from:


<table>
<thead>
  <tr><th>Country</th><th>Contact</th></tr>
</thead>
<tbody>
  <tr><td>Argentina</td><td rowspan="25">Contact <a href="https://console.aws.amazon.com/support/home#/">AWS Support Center</a>. In your request, include the following information:<ul><li> The tracking number that is on the AWS-provided return label </li><li> The date and time that you prefer the courier to pick up the server </li><li> A contact name </li><li> A phone number </li><li> An email address </li></ul></td></tr>
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
  <tr><td>Mexico</td><td>AWS contacts <a href="https://www.dbschenker.com/global">DB Schenker</a> and requests a pickup from your location. DB Schenker then contacts you to schedule the date and time for the pickup.</td></tr>
  <tr><td>United States of America</td><td>Contact <a href="https://www.ups.com">UPS</a>.<br />You can return the server in the following ways:<ul><li> Return the server during a routine UPS pickup at your site. </li><li> Drop-off the server at a <a href="https://www.ups.com/dropoff?loc=en_US">UPS location</a>. </li><li> Schedule a <a href="https://wwwapps.ups.com/pickup/schedule?loc=en_US">pickup</a> for a date and time you prefer. Enter the tracking number from the AWS-provided return label for free shipping. </li></ul></td></tr>
  <tr><td>All other countries</td><td>Contact <a href="https://www.dhl.com">DHL</a>.<br />You can return the server in the following ways:<ul><li> Drop-off the server at a <a href="https://mydhl.express.dhl/us/en/locator.html#/find-locations">DHL location</a>. </li><li> Schedule a <a href="https://returns.dhl.co.uk/ereturns/">pickup</a> for a date and time you prefer. Enter the DHL Waybill number from the AWS-provided return label for free shipping. <br />If you get the following error <code>Courier pickup can't be scheduled for an import shipment</code>, it usually means that the pickup country that you selected does not match the pickup country on the return shipment label. Select the country where the shipment originates from and try again. </li></ul></td></tr>
</tbody>
</table>
