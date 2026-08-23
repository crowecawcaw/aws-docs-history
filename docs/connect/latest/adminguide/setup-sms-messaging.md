# Set up SMS messaging in Connect Customer

You can enable SMS messaging on Connect Customer so your customers can text you from
their mobile device. With Amazon Lex, you can automate responses to their questions, saving
agents valuable time and effort.

This topic explains how to set up and test SMS messaging for Connect Customer. You use
AWS End User Messaging SMS to procure an SMS-enabled phone number, enable two-way SMS on the number, and then
import it into Connect Customer.

Using one phone number that is shared for both voice and SMS isn't supported.

###### Contents

- [Step 1: Request a number in
  AWS End User Messaging SMS](#get-sms-number "#get-sms-number")
- [Step 2: Enable two-way SMS on the phone
  number](#enable-twoway-sms "#enable-twoway-sms")
- [Step 3: Update flows to branch on
  SMS contacts](#branch-on-sms-contacts "#branch-on-sms-contacts")
- [Step 4: Test sending and receiving SMS
  messages](#test-sms "#test-sms")
- [Step 5: Prerequisites for going into
  production](#verify-sms-config "#verify-sms-config")
- [Step 6: (Optional) Self-managed
  opt-out](#sms-self-managed-opt-out "#sms-self-managed-opt-out")
- [Customers not receiving SMS
  messages?](#ts-sms-config "#ts-sms-config")
- [Next steps](#sms-nextsteps "#sms-nextsteps")

## Step 1: Request a number in AWS End User Messaging SMS

###### Important

Some countries require phone numbers to be registered for use in the country. It
can take up to 15 business days to process a registration request after it is
submitted. We strongly recommend you begin this process early. For more information
about registering, see [Registrations](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md").

We also strongly recommend reviewing [Best practices for requesting SMS numbers](sms-number.md#bp-request-sms-number "sms-number.md#bp-request-sms-number") before requesting a number.

For instructions for using the CLI to perform this step, see [Request a phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md") in the _AWS End User Messaging SMS User
Guide_.

1. Open the AWS SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Phone numbers** and then **Request
   originator**.
3. On the **Select country** page you must choose the
   **Message destination country** from the drop down that
   messages will be sent to. Choose **Next**.
4. On the **Messaging use case** section, enter the
   following:

   - Under **Number capabilities** choose either
     **SMS** or **Voice**, depending on
     your requirements.

   ###### Important

   Capabilities for SMS and Voice can't be changed after the phone
   number has been purchased.

        + **SMS** – Choose if you need SMS
         capabilities.
        + **Voice (text to audio)** – Choose if
         you need voice capabilities.
   - Under **Estimated monthly SMS message volume per month –
     optional** choose the estimated number of SMS messages you
     will send each month.
   - For **Company headquarters - optional** choose either
     of the following:

     - **Local** – Choose this if your company
       headquarters is in the same country as your customers who will
       receive SMS messages. For example, you would choose this option
       if your headquarters is in the United States and your users who
       will receive messages are also in the United States.
     - **International** – Choose this if your
       company headquarters is not in the same country as your
       customers who will receive SMS messages.

   - For **Two-way messaging** choose
     **Yes** if you require two-way messaging.

5. Choose **Next**.
6. Under **Select originator type** choose one of the
   recommended phone number type or one of the available number types. The
   available options are based on the use case information you filled out in the
   previous steps.

   - If you choose 10DLC and already have a registered campaign, you can
     choose the campaign from the **Associate to registered
     campaign**.
   - If the number type you want isn't available, you can choose
     **Previous** to go back and modify your use case.
     Also check the [Supported countries and regions (SMS channel)](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") to make sure
     the originator type you want is supported in the destination
     country.
   - If you want to request a short code or long code, you need to open a
     case with Support. For more information, see [Requesting short codes for SMS messaging with Amazon Pinpoint
     SMS](../../../sms-voice/latest/userguide/phone-numbers-request-short-code.md "../../../sms-voice/latest/userguide/phone-numbers-request-short-code.md") and [Requesting dedicated long codes for SMS messaging with Amazon
     Pinpoint SMS](../../../sms-voice/latest/userguide/phone-numbers-long-code.md "../../../sms-voice/latest/userguide/phone-numbers-long-code.md").

7. Choose **Next**.
8. On **Review and request** you can verify and edit your
   request before submitting it. Choose **Request**.
9. A **Registration Required** window might appear depending on
   the type of phone number you requested. Your phone number is associated with
   this registration and can't send messages until your registration has been
   approved. For more information about registrations requirements, see [Registrations](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md").

   1. For **Registration form name** enter a friendly
      name.
   2. Choose **Begin registration** to finish registering
      the phone number or **Register later**.

   ###### Important

   Your phone number can't send messages until your registration has
   been approved.

   You are still billed the recurring monthly lease fee for the
   phone number regardless of registration status.

## Step 2: Enable two-way SMS on the phone number

After you have successfully procured a phone number from AWS End User Messaging SMS, you enable two-way
SMS on the phone number with Connect Customer as the message destination. You can
enable two-way SMS messaging for individual phone numbers. When one of your customers
sends a message to your phone number, the message body is sent to Connect Customer.

For instructions for using the CLI to perform this step, see [Two-way SMS messaging](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md") in the _AWS End User Messaging SMS User
Guide_.

###### Note

Connect Customer for two-way SMS is available in the AWS Regions listed in [Messaging integrations](regions.md#messaging-integrations_region "regions.md#messaging-integrations_region").

1. Open the AWS SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Phone numbers**.
3. On the **Phone numbers** page choose a phone number.
4. On the **Two-way SMS** tab choose the **Edit
   settings** button.
5. On the **Edit settings** page choose **Enable two-way
   message**, as shown in following image.

![The AWS End User Messaging SMS edit settings page.](images/sms-edit-settings.png) 6. For **Destination type** choose
**Connect Customer**. 7. For Connect Customer in **Two-way channel role** choose **Choose
existing IAM roles**. 8. In the **Existing IAM roles** drop down choose an existing
IAM role as the message destination. For example IAM policies, see [IAM policies for Connect Customer](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md#phone-number-two-way-connect-iam-policy "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md#phone-number-two-way-connect-iam-policy") in the _AWS End User Messaging SMS User
Guide_.

###### Tip

If you can't create a policy or role, double-check that your Connect Customer
instance is in a [Region supported by
Connect Customer SMS](regions.md#messaging-integrations_region "regions.md#messaging-integrations_region"). 9. Choose **Save changes**. 10. In the **Import Phone Number to Connect Customer** window:

    1. For the **Incoming messages destination** drop down
     choose the Connect Customer instance that will receive incoming messages.



    ![The AWS End User Messaging SMS import phone numbers page.](images/sms-import-phone-number.png)
    2. Choose **Import Phone Number**.

11. After the number is successfully imported to Connect Customer, you can view
it in the Connect Customer admin website: In the left navigation, choose **Channels**,
**Phone numbers**. The SMS number appears on the
**Phone numbers** page, as shown in the following
image.

![The Connect Customer admin website, the Phone numbers page.](images/golden-sms-channel.png)

## Step 3: Update flows to branch on SMS contacts

If you have existing flows that you want to branch when a contact uses SMS, add a
[Check contact
attributes](check-contact-attributes.md "check-contact-attributes.md") block to your flows. This block
enables you to send SMS contacts to a specific queue, or take another action.

1. Add a [Check contact
   attributes](check-contact-attributes.md "check-contact-attributes.md") block to your flow, and
   open the **Properties** page.
2. In **Attribute to check** section, set
   **Namespace** to **Segment attributes**
   and **key** to **Subtype**.

For more information about Segment attributes, see [SegmentAttributes](ctr-data-model.md#segmentattributes "ctr-data-model.md#segmentattributes") in the
_ContactTraceRecord_ topic. 3. In the **Conditions to check** section, set
**condition** to **Equals** and
**value** to **connect:SMS**.

The following image of a **Properties** page shows it's
configured to branch when the contact comes in on the SMS channel.

![The properties page of the check contact attributes block.](images/golden-check-attributes-block.png) 4. Associate the SMS phone number with the flow: In the left navigation, choose
**Channels**, **Phone numbers**, choose
the SMS number, and then choose **Edit**.

![The Edit phone number page.](images/golden-sms-number.png) 5. Under **Flow/IVR**, choose the flow you updated, and then
choose **Save**.

![The properties page of the check contact attributes block.](images/golden-assign-flow-sms-number.png)

###### Tip

When you first purchase a phone number, the phone number's status is
**Pending**. When the phone number is ready to use, the phone
number's status is **Active**. If the phone number requires [registration](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md"), then you must complete that step before the phone
number's status changes to **Active**.

## Step 4: Test sending and receiving SMS messages

In this step you use the Contact Control Panel (CCP) and a mobile phone to test
sending and receiving SMS messages.

###### Important

By default, AWS End User Messaging SMS handles reserved opt-out and help keywords, such as
`STOP` and `HELP`, at the platform level. When a customer
sends one of these keywords, AWS End User Messaging SMS replies automatically and does not forward the
message to Connect Customer. As a result, the message does not appear in the agent CCP. If you
send a keyword while you test, this is expected behavior and does not mean that your
setup is broken.

If a customer sends `STOP`, AWS End User Messaging SMS adds them to the opt-out list, and
later messages to that customer are blocked. To check whether a customer was
inadvertently opted out, review the opt-out list in the AWS End User Messaging SMS console. For more
information, including the full list of reserved keywords, see [Opt-out
lists](../../../sms-voice/latest/userguide/opt-out-list.md "../../../sms-voice/latest/userguide/opt-out-list.md") in the _AWS End User Messaging SMS User Guide_.

To route keyword messages to Connect Customer instead, so that you can handle them in a flow,
enable self-managed opt-out on the phone number. For more information, see [Step 6: (Optional) Self-managed
opt-out](#sms-self-managed-opt-out "#sms-self-managed-opt-out").

1. In your CCP, set your status to **Available**.
2. Using a mobile device, send an SMS to the phone number that you requested in
   [Step 1: Request a number in AWS End User Messaging SMS](#get-sms-number "#get-sms-number").

###### Tip

If your AWS End User Messaging SMS phone number is still in the SMS sandbox, you can only
test sending and receiving SMS messages with verified destination numbers
that you have configured. For move instructions, see [Moving from the SMS sandbox to production](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md").

![The agent CCP and the customer phone sending SMS messages.](images/sms-testing2.png)

## Step 5: Prerequisites for going into production

Before you use SMS in production mode, make sure you've completed the following
prerequisites for AWS End User Messaging SMS.

1. [Move
   your account out of SMS/MMS sandbox mode](../../../sms-voice/latest/userguide/sandbox.md "../../../sms-voice/latest/userguide/sandbox.md")
2. [Set up your registration
   for SMS/MMS](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md")
3. [Confirm
   that your spend quota matches your usage requirements](../../../sms-voice/latest/userguide/awssupport-spend-threshold.md "../../../sms-voice/latest/userguide/awssupport-spend-threshold.md")
4. [Check your opt-out lists](../../../sms-voice/latest/userguide/opt-out-list.md "../../../sms-voice/latest/userguide/opt-out-list.md")

## Step 6: (Optional) Set up self-managed opt-out message processing

Optionally, you can enable self-managed opt-out for your SMS number. For details
about this feature, see [Self-managed
opt-outs](../../../sms-voice/latest/userguide/opt-out-list-self-managed.md "../../../sms-voice/latest/userguide/opt-out-list-self-managed.md"). For setup instructions, see [Managing opt-out
lists](../../../sms-voice/latest/userguide/opt-out-list-managed.md "../../../sms-voice/latest/userguide/opt-out-list-managed.md").

After enabling self-managed opt-out, you should set up Lambda functions and flow
blocks to process SMS opt-out requests from customers and block agents from messaging
customers who have opted out.

###### Important

If you enable this feature, you're responsible for responding to HELP and STOP
requests. You're also responsible for tracking and honoring opt-out requests.
Many countries, regions, and jurisdictions impose severe penalties for sending
unwanted SMS messages. If you enable this feature, make sure you have systems
and processes in place for capturing and managing opt-out requests.

### Two-way communication with agents

Use this setup when the phone number with self-managed opt-out enabled is used
for two-way communication with agents.

Before proceeding, your Connect Customer instance should have the following settings and
resources configured:

- An SMS phone number in your instance.
- You can send and receive messages on that phone number.
- When a customer sends a message to this phone number, they are routed
  to live agents.
- Customer Profiles is enabled and working correctly.

1. **Create an opt-out message processing Lambda
   function for the initial chat message.**

   1. Go to the AWS console for Lambda, and choose
      **Create function** with all the default
      settings.
   2. After the function is created, under the
      **Code** tab, add code for handling customer
      opt-out into the `index.mjs` file.
   3. Create an IAM policy to give the Lambda function sufficient
      access to invoke the APIs in the code. Create a policy with the
      required permissions and attach it to your Lambda execution
      role:

      - The policy should contain permissions to invoke all
        APIs required to process customer opt-out
        requests.
      - Permissions for `kms:GenerateDataKey` and
        `kms:Decrypt` are required if Customer
        Profiles is used.
      - The Lambda execution role name can be found by choosing
        the **Configuration** tab, then going
        to **Permissions**.

2. **Create an opt-out message processing Lambda
   function for all other messages in the contact.**

   1. Go to the AWS console for Lambda, and choose
      **Create function** with all the default
      settings.
   2. After the function is created, under the
      **Code** tab, add code for handling customer
      opt-out into the `index.mjs` file.
   3. Attach the same policy you created in step 1 to your Lambda
      execution role.

3. **Import both Lambda functions into your Connect Customer
   instance.**

   1. Import the Lambda function created in step 1 by following the
      instructions in [Grant Connect Customer access to your AWS Lambda functions](connect-lambda-functions.md "connect-lambda-functions.md").
   2. Run the following CLI command with your AWS account
      credentials to integrate the Lambda function created in step 2
      with the Message Processing flow block:

   ```
   aws connect create-integration-association \
       --instance-id `your-connect-instance-id` \
       --integration-type MESSAGE_PROCESSOR \
       --integration-arn arn:aws:lambda:`region`:`account-id`:function:`function-name` \
       --region `aws-region`
   ```

4. **Create or update the contact
   flow.**

Create a contact flow with the necessary flow blocks at the beginning,
or add them to the existing contact flow that is associated with the
phone number that you've enabled self-managed opt-out for.

    * The flow blocks required are: Set Recording and Analytics
     Behavior, Set Contact Attributes, Invoke AWS Lambda function,
     and Check Contact Attributes.
    * For details on each flow block, see [Flow block definitions in the flow designer in Connect Customer](contact-block-definitions.md "contact-block-definitions.md").
    * For details on using the Set Recording and Analytics Behavior
     block for message processing, see [Enable in-flight sensitive data redaction and message processing](redaction-message-processing.md "redaction-message-processing.md").

### No two-way communication with agents

Use this simpler setup when the phone number with self-managed opt-out enabled
is NOT used for two-way communication with agents (meaning when a customer sends
a message to that phone number, they will NOT be routed to live agents).

1. **Set up an Amazon Lex bot to process customer opt-out
   requests.**

   1. Create an Amazon Lex bot and use it in a Connect Customer flow by following
      the instructions in [Add an Amazon Lex bot to Connect Customer](amazon-lex.md "amazon-lex.md").
   2. When you get to the step for creating bot intents, create a
      bot with the following two intents:

      - **Intent 1:
        CustomerOptOutIntent** – This intent is
        triggered when a customer sends an opt-out keyword like
        "STOP" to the phone number. Configure it to reply with
        a message of your choice.
      - **Intent 2:
        FallbackIntent** – This intent is
        triggered when a customer sends any other message to the
        phone number. Configure it to reply with a different
        message of your choice.###### Note

If you want to perform other checks and update an opt-out list of
your choice, you need to implement a Lambda function with all the
custom logic and link it to the bot. 2. **Create or update the contact
flow.**

Create a contact flow with the necessary flow blocks at the beginning,
or add them to the existing contact flow that is associated with the
phone number that you've enabled self-managed opt-out for.

    * The flow block required is Get Customer Input (you will link
     your Amazon Lex bot to this flow block).
    * For details on each flow block, see [Flow block definitions in the flow designer in Connect Customer](contact-block-definitions.md "contact-block-definitions.md").

## Customers not receiving SMS messages?

Before opening an AWS Support ticket, please verify that you've completed [Step 5: Prerequisites for going into production](#verify-sms-config "#verify-sms-config").

## Next steps

We recommend the following steps to provide the best experience for your agents and
customers.

- [Enable customers to resume chat conversations in Connect Customer](chat-persistence.md "chat-persistence.md"): Customers
  can resume previous conversations with the context, metadata, and transcripts
  carried forward. They don't need to repeat themselves when they return to a
  chat, and agents have access to the entire conversation history.
- [Create quick responses for use with chat and email contacts in Connect Customer](create-quick-responses.md "create-quick-responses.md"): Provide agents with pre-written responses to common customer inquiries that
  they can use while they chat with customers. Quick responses make it faster for
  agents to respond to customers.
