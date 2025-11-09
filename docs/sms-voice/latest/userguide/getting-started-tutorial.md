# Tutorial for sending a message using AWS End User Messaging SMS

This section provides an overview of the tutorial designed to help you start using
AWS End User Messaging SMS.

**Intended Audience**

This tutorial is designed for system administrators and developers responsible for
setting up, testing, and deploying AWS End User Messaging SMS.

**Features Used**

This tutorial shows you how to use the AWS End User Messaging SMS console to:

- Create and configure a phone pool.
- Request an origination identity, which is either a phone number or sender ID.
- Create and configure a protect configuration.
- Send a test SMS message with the SMS simulator.

**Time Required**

It should take about 10–15 minutes to complete this tutorial.

**Regional Restrictions**

There are no country or regional restrictions associated with using this solution.

**Resource Usage Costs**

There's no charge for creating an AWS account. However, by implementing this solution,
you might incur some or all of the costs that are listed in the following table.

| Description                     | Cost (US dollars)                                                                                                                                                                                                                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Message sending costs           | You pay for each SMS message part that you send through AWS End User Messaging SMS. For more information<br>about pricing, see [AWS End<br>User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").                                                                     |
| Monthly phone number lease cost | You pay a recurring monthly fee to lease each phone number or sender ID. The monthly<br>fee varies depending on the type of phone number and sender ID. For more information about<br>pricing, see [AWS End User<br>Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/"). |

**AWS account permissions**

The account that you use to sign in to the AWS Management Console has to be able to perform the
following tasks:

- Create a pool
- Create a configuration set
- Create an event destination
- Send SMS messages

For more information about account permissions, see [Identity and access management for AWS End User Messaging SMS](security-iam.md "security-iam.md").

## Step 1: Create a pool

The procedures in this section show you how to create a pool and add either a phone number
or sender ID to the pool.

###### To create a pool

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Overview**, in the **Quick
   start** section, choose **Create pool**.
3. Under the **Pool setup** section, enter a name for your pool in
   **Pool name**.
4. Choose one of the following options:
   - **Phone number** – If you choose this option, under
     **Phone numbers available for association**, choose either:
     - **Request simulator number**, and in the
       **Country** dropdown list, choose the destination country and then
       **Request number**.

     ###### Note

     A simulated phone number doesn't require registration. It generates realistic events
     and is used for testing. Messages sent from a simulator number can only be sent to other
     simulator destination numbers and aren't sent over the carrier network.
     - Choose a phone number that you've previously purchased.

   - **Sender ID** – If you choose this option, choose a sender ID
     from **Sender IDs available for association**.

5. Choose **Create phone pool**.

## Step 2: Create a configuration set

The procedures in this section show you how to create a configuration set, add a CloudWatch Events,
Amazon Data Firehose, or Amazon SNS destination and choose the event types.

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Overview**, in the **Quick
   start** section, choose **Create set**.
3. Under the **Configuration set details** section, enter a name in
   **Configuration set name**.
4. For **Event destination setup**, choose either:
   - **Set up CloudFormation** (Recommended) to have AWS CloudFormation create and
     configure CloudWatch, Amazon Data Firehose and Amazon SNS to log all events.
     - For **Event destination name** enter a name for the event
       destination.
     - Choose **Launch stack**.
     - A new browser window will open. Review the **Quick create stack**
       form and check any acknowledgements. Choose **Create stack**.

     ###### Note

     Creating the AWS CloudFormation stack can take up to five minutes.
     - When the status indicator for the AWS CloudFormation stack on the **Create configuration
       set** page is **Stack created**, choose
       **Create**.

   - **Setup event destination** to manually set up the configuration set
     and event destination.
     - For **Event destination name**, enter a name for the event
       destination.
     - For **Destination type**, choose either CloudWatch, Amazon Data Firehose or Amazon SNS.
       For more information on how to setup these event destinations see [Set up Amazon CloudWatch event destination](configuration-sets-cloud-watch.md "configuration-sets-cloud-watch.md"), [Set up Amazon Data Firehose event destination](configuration-sets-kinesis.md "configuration-sets-kinesis.md")
       and [Set up an Amazon SNS event destination](configuration-sets-sns.md "configuration-sets-sns.md")
     - Under **Event types**, choose the appropriate option:
       - **All SMS events (Recommended)** – Send all SMS events
         listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to the event destination.
       - **Custom SMS events** – Choose specific SMS events to send
         to the event destination. To edit the list of events choose **Edit SMS event
         selection**. In the **Edit SMS event selection** window
         choose only the events that you want to log. Choose **Save
         selection**.
       - **All MMS events (Recommended)** – Send all MMS events
         listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to the event destination.
       - **Custom MMS events** – Choose specific MMS events to
         send to the event destination. To edit the list of events choose **Edit MMS
         event selection**. In the **Edit MMS event selection**
         window choose only the events that you want to log. Choose **Save
         selection**.
       - **All voice events (Recommended)** – Send all voice events
         listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to the event destination.
       - **Custom voice events** – Choose specific voice events to
         send to the event destination. To edit the list of events, choose **Edit voice
         event selection**. In the **Edit voice event selection**
         window choose only the events the you want to log. Choose **Save
         selection**.

     - Choose **Create**.

5. Choose **Create configuration set**

## Step 3: Create a protect configuration

The procedures in this section show you how to create a protect configuration to specify
which countries AWS End User Messaging SMS can send messages to.

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Overview**, in the **Quick
   start** section, choose **Create configuration**.
3. Under **Protect configuration details** enter a friendly name for your
   protect configuration in **Protect configuration name**.
4. Under Country rules, select the countries you want to set rules for. For each country,
   choose whether to block, filter, or allow message sending. We recommend:
   - Setting block rules for countries you don't do business in.
   - Using filter rules for countries with high per-message costs or where you have SMS
     pumping concerns.
   - Setting allow rules for countries where you do not wish to use filter.

###### Note

Do not block the country that you are going to send a test message to in the next
step. 5. In **Protect configuration associates** under **Association
type**, choose **Configuration set association**. Under
**Configuration sets available for association**, choose the configuration
set you created in step 2. 6. Choose **Create configuration**.

## Step 4: Send a test message with the SMS

simulator

###### Note

To add a verified destination phone number you must have an originator that's status is
_Active_, see [View a phone number status and capabilities in AWS End User Messaging SMS](phone-numbers-status.md "phone-numbers-status.md"). If you don't have an _Active_ originator
then use a simulator phone number and a simulator destination phone number to send and receive
the test SMS message.

The procedures in this section show you how to send a test SMS message to verify your
environment is correctly configured.

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Overview**, in the **Quick
   start** section, choose **Test SMS sending**.
3. For **Originator**, choose either **Phone pool**,
   **Phone number** or **Sender ID** as the type of originator
   to send the test message. You then need to select the originator identity from the dropdown
   list.
   1. (Optional) If you need a simulator phone number then choose **Request simulator
      number**. In the **Request simulator number** window choose a
      **Country** from the dropdown list and then choose **Request
      number**.

   ###### Important

   Simulator phone numbers can only send to other simulator destination phone numbers
   however they behave like actual phone numbers without sending over the carrier network. You
   can not use a simulator phone number to verify a destination phone number. For example, US
   simulator phone numbers can only send to US destination simulator phone numbers.

4. In the **Destination number** section, choose either **Simulator
   number** or **Verified number** and then select the number from the
   dropdown list.

To view your current list of verified destination numbers choose **Verified
number** then expand **Manage verified destination number**. If you
don't have any verified destination phone numbers, or need to add a new verified destination
phone number, do the following:

    1. To verify a new destination phone number, choose **Verify new
     number**.
    2. In the **Add phone number** window for **Destination phone
     number**, enter the phone number of the device to receive the test message. The
     phone number must start with a '+' and can't contain any spaces, hyphens, or parentheses.
     For example, `+1 (206) 555-0142` is not in the correct format, but
     `+12065550142` is.
    3. Choose **Send verification code**.
    4. The destination device will receive a verification code that is valid for 15 minutes.
     Enter the code the device received into the **Verification code**
     field.
    5. Choose **Verify number**.

5. For **Configuration set**, choose the event destination to receive the
   event data.
6. For **Message body**, enter a custom SMS message.
7. Choose **Send test message**.
8. For **Event logs: CloudWatch**, choose the refresh button to display the event
   log of the test message.

###### Tip

Wait at least at 10 seconds after sending the test SMS message before refreshing.

## Next steps: Move from sandbox to

production

After fully testing your SMS environment in the SMS sandbox, you can request to move to
production.

1. Create an AWS Support case at [https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").
2. Choose the **Looking for service limit increases?** link, then complete
   the following:
   - For **Service**, choose
     **AWS End User Messaging SMS (Pinpoint)**.
   - For **Provide a link to the site or app which will be sending SMS
     messages**, provide information about the website, application, or service that
     will send SMS messages.
   - For **What type of messages do you plan to send**, choose the type of
     message that you plan to send by using your origination identity:
     - **One Time Password** – Messages that provide passwords that
       your customers use to authenticate with your website or application.
     - **Promotional** – Noncritical messages that promote your
       business or service, such as special offers or announcements.
     - **Transactional** – Important informational messages that
       support customer transactions, such as order confirmations or account alerts.
       Transactional messages must not contain promotional or marketing content.

   - For **Which AWS Region will you be sending messages from**, choose
     the AWS Region that you will be sending messages from.
   - For **Which countries do you plan to send messages to**, enter the
     country or region that you want to purchase short codes in.
   - For **How do your customers opt to receive messages from you**,
     provide details about your opt-in process.
   - For **Please provide the message template that you plan to use to send
     messages to your customers**, include the template that you will be using.

3. Under **Requests**, complete the following sections:
   - For the **Region**, choose the AWS Region from which you will be
     sending messages.

   ###### Note

   The Region is required in the **Requests** section. Even if you
   provided this information in the **Case details** section, you must also
   include it here.
   - For **Resource Type**, choose **General
     Limits**.
   - For the **Quota**, choose **SMS Production
     Access**.
   - For **New quota value**, enter 1.

4. Under **Case description**, for **Use case
   description**, enter any relevant details about this
   request.
5. (Optional) If you want to submit any further requests, choose **Add another
   request**.
6. Under **Contact options**, for **Preferred contact
   language**, choose whether you want to receive communications for this case in
   **English** or **Japanese**.
7. When you finish, choose **Submit**.
