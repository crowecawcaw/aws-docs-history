# Dedicated Direct Connect connections

To create an Direct Connect dedicated connection, you need the following information:

**Direct Connect location**

Work with a partner in the AWS Direct Connect Partner Program to help you establish
network circuits between an Direct Connect location and your data center, office, or
colocation environment. They can also help provide colocation space within the
same facility as the location. For more information, see [APN Partners Supporting
Direct Connect](https://aws.amazon.com/directconnect/partners "https://aws.amazon.com/directconnect/partners").

**Port speed**

The possible values are 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps.

You can't change the port speed after you create the connection request. To change the port
speed, you must create and configure a new connection.

You can create a connection using either the Connection wizard or create a Classic
connection. Using the Connection wizard you can set up connections using resiliency
recommendations. The wizard is recommended if you're setting up connections for the
first time. If you prefer, you can use Classic to create connections one-at-a-time.
Classic is recommended if you've already got an existing setup that you want to add
connections to. You can create a standalone connection, or you can create a connection
to associate with a LAG in your account. If you associate a connection with a LAG, it's
created with the same port speed and location that is specified in the LAG.

After you request the connection, we make a Letter of Authorization and Connecting Facility
Assignment (LOA-CFA) available to you to download or email you with a request for more
information. If you receive a request for more information, you must respond within 7
days or the connection is deleted. The LOA-CFA is the authorization to connect to AWS,
and is required by your network provider to order a cross connect for you. If you do not
have equipment in the Direct Connect location, you cannot order a cross connect for yourself
there.

The following operations are available for dedicated connections:

- [Create a connection using the Connection wizard](create-connection.md "create-connection.md")
- [Create a Classic connection](#connection-classic "#connection-classic")
- [View Direct Connect connection details](viewdetails.md "viewdetails.md")
- [Update an Direct Connect connection](updateconnection.md "updateconnection.md")
- [Associate a MACsec CKN/CAK with a
  connection](associate-key-connection.md "associate-key-connection.md")
- [Remove the association between a MACsec secret key
  and an Direct Connect connection](disassociate-key-connection.md "disassociate-key-connection.md")
- [Delete an Direct Connect connection](deleteconnection.md "deleteconnection.md")
  You can add a dedicated connection to a link aggregation group (LAG) allowing you to treat
  multiple connections as a single one. For information, see [Associate a connection with a LAG](associate-connection-with-lag.md "associate-connection-with-lag.md").

After you create a connection, create a virtual interface to connect to public and private
AWS resources. For more information, see [Virtual interfaces and hosted virtual interfaces](WorkingWithVirtualInterfaces.md "WorkingWithVirtualInterfaces.md").

If you do not have equipment at an Direct Connect location, first contact an AWS Direct Connect Partner at
the AWS Direct Connect Partner Program. For more information, see [APN Partners Supporting
Direct Connect](https://aws.amazon.com/directconnect/partners "https://aws.amazon.com/directconnect/partners").

If you want to create a connection that uses MAC Security (MACsec), review the
prerequisites before you create the connection. For more information, see [MACsec prerequisites for dedicated connections](MACsec.md#mac-sec-prerequisites "MACsec.md#mac-sec-prerequisites").

## Letter of Authorization and Connecting Facility

Assignment (LOA-CFA)

After we have processed your connection request, you can download the LOA-CFA. If the link
is not enabled, the LOA-CFA is not yet available for you to download. Check your
email for a request for information.

The downloaded LoA is digitally signed and watermarked to validate the
authenticity of the LoA issued by AWS. The digital signature and watermark in the
LoA. The PDF document prevents a modified or potentially fraudulent LoA from being
acted upon by the facilities provider at Direct Connect sites. The digital signature
can be authenticated by opening the PDF and reviewing the signature panel. A valid
document will show the "Signature is valid" and "Document has not been modified
since the signature was applied". The watermark repeats the patch panel and strands
assigned across the body of the LoA as a visual, but non-secure, indicator of
authenticity.

Billing automatically starts when the port is active or 90 days after the LOA has
been issued, whichever comes first. You can avoid billing charges by deleting the
port prior to activation or within 90 days of the LOA being issued.

If your connection is not up after 90 days, and the LOA-CFA has not been issued,
we will send you an email alerting you that the port will be deleted in 10 days. If
you fail to activate the port within the additional 10 day period, the port will
automatically be deleted and you'll need to restart the port creation
process.

For the steps to download the LoA-CFA, see [Download the LOA-CFA](download-loa-cfa.md "download-loa-cfa.md").

###### Note

For more information about pricing, see [Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/ "https://aws.amazon.com/directconnect/pricing/"). If you no longer want the connection after you
have reissued the LOA-CFA, you must delete the connection yourself. For more
information, see [Delete an Direct Connect connection](deleteconnection.md "deleteconnection.md").

###### Topics

- [Create a connection using the Connection wizard](create-connection.md "create-connection.md")
- [Create a Classic connection](#connection-classic "#connection-classic")
- [Download the LOA-CFA](download-loa-cfa.md "download-loa-cfa.md")
- [Associate a MACsec CKN/CAK with a
  connection](associate-key-connection.md "associate-key-connection.md")
- [Remove the association between a MACsec secret key
  and a connection](disassociate-key-connection.md "disassociate-key-connection.md")

## Create an Direct Connect Classic connection

For dedicated connections, you can submit a connection request using the Direct Connect console. For hosted connections, work with an AWS Direct Connect Partner
to request a hosted connection. Ensure that you have the following information:

- The port speed that you require. For dedicated connections, you can't change the port
  speed after you create the connection request. For hosted connections, your
  AWS Direct Connect Partner can change the speed.
- The Direct Connect location at which the connection is to be terminated.

###### Note

You cannot use the Direct Connect console to request a hosted connection. Instead,
contact an AWS Direct Connect Partner, who can create a hosted connection for you, which you then
accept. Skip the following procedure and go to [Accept your hosted connection](toolkit-classic.md#get-started-accept-hosted-connection "toolkit-classic.md#get-started-accept-hosted-connection").

###### To create a new Direct Connect connection

1.  Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  On the **Direct Connect** screen, under **Get started**, choose
    **Create a connection**.
3.  Choose **Classic**.
4.  For **Name**, enter a name for the connection.
5.  For **Location**, select the appropriate Direct Connect
    location.
6.  If applicable, for **Sub Location**, choose the floor
    closest to you or your network provider. This option is only available if
    the location has meet-me rooms (MMRs) in multiple floors of the
    building.
7.  For **Port Speed**, choose the connection
    bandwidth.
8.  For **On-premises**, select **Connect through an
    Direct Connect partner** when you use this connection to connect to
    your data center.
9.  For **Service provider**, select the AWS Direct Connect Partner. If you
    use a partner that is not in the list, select
    **Other**.
10. If you selected **Other** for **Service
    provider**, for **Name of other provider**,
    enter the name of the partner that you use.
11. (Optional) Choose **Add tag** to add key/value pairs to
    further help identify this connection.

        * For **Key**, enter the key name.
        * For **Value**, enter the key value.

    To remove an existing tag, choose the tag and then choose
    **Remove tag**. You can't have empty
    tags.

12. Choose **Create Connection**.

It can take up to 72 business hours for AWS to review your request and provision a port
for your connection. During this time, you might receive an email with a request for more
information about your use case or the specified location. The email is sent to the email
address that you used when you signed up for AWS. You must respond within 7 days or the
connection is deleted.

For more information, see [Dedicated and hosted connections](WorkingWithConnections.md "WorkingWithConnections.md").
