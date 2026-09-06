

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Porting existing phone numbers
<a name="porting"></a>

In addition to provisioning phone numbers, you can also port numbers from your phone carrier into your inventory. This includes toll-free numbers.

**Note**  
If you need to port international numbers, use Amazon Chime Voice Connector's, or use SIP media applications, you must create an Amazon Chime SDK administrator account and use the Amazon Chime SDK console. For more information about doing that, refer to [Prerequisites](https://docs.aws.amazon.com/chime-sdk/latest/ag/prereqs.html), in the *Amazon Chime SDK Administrator Guide*.

The following sections explain how to port phone numbers.

**Topics**
+ [Prerequisites for porting numbers](#porting-prereqs)
+ [Porting phone numbers in](#port-in)
+ [Submitting required documents](#submit-required-docs)
+ [Viewing request status](#view-port-status)
+ [Assigning ported numbers](#assign-ported-numbers)
+ [Porting phone numbers out](#port-out)
+ [Phone number porting status definitions](#porting-status-definitions)

## Prerequisites for porting numbers
<a name="porting-prereqs"></a>

To port numbers, you must have a Letter of Agency (LOA). You must have an LOA for domestic phone numbers. Download the [Letter of Agency (LOA) form](https://d1.awsstatic.com/whitepapers/AmazonChimeLOA.pdf) and fill it out. If you need to port phone numbers from different carriers, fill out a separate LOA for each carrier.

## Porting phone numbers in
<a name="port-in"></a>

You create a support request to port existing phone numbers in.

**To port existing phone numbers**

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. On the command bar at the top of the page, choose **Support**, then choose **Submit request**.  
![Support menu showing the Submit request and AWS Billing commands.](http://docs.aws.amazon.com/chime/latest/ag/images/porting-request.png)

   That takes you to the AWS Support console.
**Note**  
You can also go directly to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page. If you do, choose **Create case**, then follow the steps below.

1. Under **How can we help**, do the following:

   1. Choose **Account and billing**.

   1. From the **Service** list, choose **Chime SDK (Number Management)**.

   1. From the **Category** list, choose **Phone Number Port In**.

   1. Choose **Next step: Additional information**.

1. Under **Additional information**, do the following

   1. Under **Subject**, enter **Porting phone numbers in**.

   1. Under **Description**, enter the following information:

      For porting US numbers:
      + Billing Telephone Number (BTN) of the account.
      + Authorizing person’s name. This is the person in charge of account billing with the current carrier.
      + Current carrier, if known.
      + Service account number, if this information is present with the current carrier.
      + Service PIN, if available.
      + Service address and customer name, as they appear in your current carrier contract.
      + Requested date and time for the port.
      + (Optional) If you want to port your Billing Telephone Number (BTN), select one of the following options:
        + **I am porting my BTN and I want to replace it with a new BTN that I am providing. I can confirm that this new BTN is on the same account with the current carrier.**
        + **I am porting my BTN and I want to close out my account with my current carrier.**
        + **I am porting my BTN because my account is currently set up so that each phone number is its own BTN.** (Select this option only when your account with the current carrier is set up this way.)
        + After you choose an option, attach your Letter of Agency (LOA) to the request.

      **For porting international numbers:**
      + You must use the SIP Media Application Dial-In product type for non-US phone numbers.
      + Type of number (Local or Toll-Free)
      + Existing phone numbers to port in.
      + Estimate usage volume
      + Country

   1. From the **Phone number type** list, select **Business Calling**, **SIP Media Application Dial-In**, or **Voice Connector**.

   1. Under **Phone number**, enter at least one phone number, even if you're porting multiple numbers.

   1. Under **Porting Date**, enter the desired porting date.

   1. Under **Porting Time**, enter the desired time.

   1. Choose **Next step: Solve now or contact us**.

1. Under **Solve now or contact us**, choose **Contact us**.

1. From the **Preferred contact language list**, choose a language

1. Choose **Web** or **Phone**. If you choose **Phone**, enter your phone number. When finished, choose **Submit**.

AWS Support lets you know whether your phone numbers can be ported from your existing phone carrier. If you can, you need to submit any required documents. The steps in the next section explain how to submit those documents.

## Submitting required documents
<a name="submit-required-docs"></a>

After AWS Support says you can port phone numbers, you need to submit any required documents. The following steps explain how.

**Note**  
AWS Support provides a secure Amazon S3 link for uploading all requested documents. Do not proceed until you receive the link.

**To submit documents**

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. Sign in to your AWS account, then open the Amazon S3 upload link generated specifically for your account.
**Note**  
The link expires after ten days. It is generated specifically for the account that created the case. The link requires an authorized user from the account to perform the upload.

1. Choose **Add Files**, then select the identity documents related to your request.

1. Expand the **Permissions** section, and choose **Specify individual ACL permissions**.

1. At the end of the **Access control list (ACL)** section, choose **Add grantee**, then paste the key provided by AWS Support into the **Grantee** box.

1. Under **Objects**, choose the **Read** checkbox, then choose **Upload**.

After you provide the Letter of Agency (LOA), Support confirms with your existing phone carrier that the information on the LOA is correct. If the information provided on the LOA does not match the information that your phone carrier has on file, Support contacts you to update the information provided on the LOA.

## Viewing request status
<a name="view-port-status"></a>

The following steps explain how to use the Amazon Chime console to view the status of your porting requests.

**To view the status**

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. In the navigation pane, choose **Phone number management**.

1. Choose the **Orders** tab.

The **Status** column shows the status of your request. Support also contacts you with updates and requests for further information, as needed. For more information, see [Phone number porting status definitions](#porting-status-definitions), later in this section.

## Assigning ported numbers
<a name="assign-ported-numbers"></a>

After your phone carrier confirms that the LOA is correct, they review and approve the requested port. Then they provide Support with a Firm Order Commit (FOC) date and time for the port to occur.

On the FOC date, the ported phone numbers are activated for use. You must then assign the numbers to users in the desired account.

**To assign phone numbers**

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. In the navigation pane, choose **Phone number management**.

1. On the **Inventory** tab, select the checkbox next to the number that you want to assign, then choose **Assign**.
**Note**  
You can only choose one number at a time.

1. On the **Assign \+1*phone number* to a user profile** page, select the account for the number, then choose **Next**.

1. Select the user that you want to assign the number to, then choose **Assign**.

## Porting phone numbers out
<a name="port-out"></a>

You port numbers out of Amazon Chime by initiating a porting request with your winning carrier. When submitting information to your winning carrier, include your AWS account ID as the account ID associated with the phone number being ported.

When the porting process finishes and your winning carrier has the numbers, you must unassign and delete those numbers from your inventory. For more information, see [Unassigning Amazon Chime Business Calling phone numbers](unassign-cbc-numbers.md) and [Deleting phone numbers](delete-phone.md) in this guide.

**Important**  
The ability to port numbers out depends on the winning carrier’s ability to accept those numbers.
Verifying the authenticity of the winning carrier's port-out request is critical for the security of your phone number. If the account details are not correct (for example, there's an account ID mismatch), your port-out request may be rejected, causing delays and requiring you to resubmit your request.

### (Optional) How to request a PIN to protect your number
<a name="port-out-pin"></a>

For additional security, you can contact us to apply a PIN to your number. The winning carrier then uses that PIN. Follow these steps:

**To request a PIN**

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. In the navigation pane, under **Contact Us**, choose **Support**.

   That takes you to the AWS Support console.
**Note**  
You can also go directly to the [AWS Support Center](https://console.aws.amazon.com/support/home#/) page. If you do, choose **Create case**, then follow the steps below.

1. Under **How can we help**, do the following:

   1. Choose **Account and billing**.

   1. From the **Service** list, choose **Chime SDK (Number Management)**.

   1. From the **Category** list, choose **Phone Number Port Out**.

   1. Choose **Next step: Additional information**.

1. Under **Additional information**, do the following

   1. Under **Subject**, enter **Porting phone numbers out**.

   1. Under **Description**, enter the following.

      **I would like to assign a pin to my phone number: Pin: ABCD123 Phone Number: 1234567890** 
**Note**  
You must provide an alphanumeric PIN of 4 - 10 characters.

AWS Support associates a PIN with the phone number. When requesting the port with your winning carrier, provide your AWS account ID and PIN. We will use that information to validate any port requests received for your number. 

## Phone number porting status definitions
<a name="porting-status-definitions"></a>

After you submit a request to port existing phone numbers into Amazon Chime, you can view the status of your porting request in the Amazon Chime console under **Calling**, **Phone number management**, **Pending**.

Porting statuses and definitions include the following:

**CANCELLED**  
Support cancelled the porting order because of an issue with the port, such as a cancellation request from the carrier or from you. Support contacts you with details.

**CANCEL\_REQUESTED**  
Support is processing a cancellation of the porting order because of an issue with the port, such as a cancellation request from the carrier or from you. Support contacts you with details.

**CHANGE\_REQUESTED**  
Support is processing your change request, and the carrier response is pending. Allow for additional processing time.

**COMPLETED**  
Your porting order is completed, and your phone numbers are activated.

**EXCEPTION**  
Support contacts you for additional details needed to complete the port request. Allow for additional processing time.

**FOC**  
The FOC date is confirmed with the carrier. Support contacts you to confirm the date.

**PENDING DOCUMENTS**  
Support contacts you for additional documents needed to complete the port request. Allow for additional processing time.

**SUBMITTED**  
Your porting order is submitted, and the carrier response is pending.