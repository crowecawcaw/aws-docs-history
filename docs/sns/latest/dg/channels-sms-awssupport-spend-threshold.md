# Requesting increases to your

monthly Amazon SNS SMS spending quota

Amazon SNS provides spending quotas to help you manage the maximum per-month cost incurred by
sending SMS using your account. The spending quota limits your risk in case of malicious
attack, and prevents your upstream application from sending more messages than expected. You
can configure Amazon SNS to stop publishing SMS messages when it determines that sending an SMS
message will incur a cost that exceeds your spending quota for the current month.

To ensure your operations are not impacted, we recommend requesting a spending quota high
enough to support your production workloads. For more information, see [Step 1: Open an Amazon SNS SMS
case](#channels-sms-awssupport-spend-threshold-open "#channels-sms-awssupport-spend-threshold-open"). Once you have received the quota, you can manage your risk by applying the
full quota, or a smaller value, as described in [Step 2: Update your SMS
settings](#channels-sms-awssupport-spend-threshold-settings "#channels-sms-awssupport-spend-threshold-settings"). By applying a smaller value, you can control your monthly spending with
the option to scale up if necessary.

###### Important

Because Amazon SNS is a distributed system, it stops sending SMS messages within minutes if
the spending quota is exceeded. During this period, if you continue to send SMS
messages, you might incur costs that exceed your quota.

We set the spending quota for all new accounts at $1.00 (USD) per month. This quota is
intended to let you test the message-sending capabilities of Amazon SNS. To request an increase
to the SMS spending quota for your account, open a quota increase case in the AWS Support
Center.

###### Topics

- [Step 1: Open an Amazon SNS SMS
  case](#channels-sms-awssupport-spend-threshold-open "#channels-sms-awssupport-spend-threshold-open")
- [Step 2: Update your
  SMS settings on the Amazon SNS console](#channels-sms-awssupport-spend-threshold-settings "#channels-sms-awssupport-spend-threshold-settings")

## Step 1: Open an Amazon SNS SMS

case

You can request an increase to your monthly spending quota by opening a quota increase
case in the AWS Support Center.

###### Note

Some of the fields on the request form are marked as "optional." However, Support
requires all of the information that's mentioned in the following steps in order to
process your request. If you don't provide all of the required information, you may
experience delays in processing your request.

1.  Sign in to the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2.  On the **Support** menu, choose **Support
    Center**.
3.  On the **Your support cases** pane, choose **Create
    case**.
4.  Choose the **Looking for service limit increases?** link,
    then complete the following:
    - For **Limit type**, choose
      **SNS Text Messaging**.
    - (Optional) For **Provide a link to the site or app which will
      be sending SMS messages**, provide information about the
      website, application, or service that will send SMS messages.
    - (Optional) For **What type of messages do you plan to
      send**, choose the type of message that you plan to send
      using your long code:
      - **One Time Password** – Messages that
        provide passwords that your customers use to authenticate with
        your website or application.
      - **Promotional** – Noncritical messages
        that promote your business or service, such as special offers or
        announcements.
      - **Transactional** – Important
        informational messages that support customer transactions, such
        as order confirmations or account alerts. Transactional messages
        must not contain promotional or marketing content.

    - (Optional) For **Which AWS Region will you be sending
      messages from**, choose the region that you'll be sending
      messages from.
    - (Optional) For **Which countries do you plan to send messages
      to**, enter the country or region that you want to purchase
      short codes in.
    - (Optional) In the **How do your customers opt to receive
      messages from you**, provide details about your opt-in
      process.
    - (Optional) In the **Please provide the message template that
      you plan to use to send messages to your customers** field,
      include the template that you will be using.

5.  Under **Requests**, complete the following sections:
    - For the **Region**, choose the Region from which
      you'll be sending messages.

    ###### Note

    The Region is required in the **Requests**
    section. Even if you provided this information in the **Case
    details** section you must also include it here.
    - For **Resource Type**, choose **General
      Limits**.
    - For **Limit**, choose **Account Spend
      Threshold Increase**.

6.  For New limit value, enter the maximum amount (in USD) that you can spend on
    SMS each calendar month.
7.  Under **Case description**, for **Use case
    description**, provide the following details:

        * The website or app of the company or service that's sending SMS
         messages.
        * The service that's provided by your website or app, and how your SMS
         messages contribute to that service.
        * How users sign up to voluntarily receive your SMS messages on your
         website, app, or other location.

    If your requested spending quota (the value you specified for **New
    quota value**) exceeds $10,000 (USD), provide the following
    additional details for each country that you're messaging:

        * Whether you're using a sender ID or short code. If you're using a
         sender ID, provide:




        	+ The sender ID.
        	+ Whether the sender ID is registered with wireless carriers in
        	 the country.
        * The maximum expected transactions-per-second (TPS) for your
         messaging.
        * The average message size.
        * The template for the messages that you send to the country.
        * (Optional) Character encoding needs, if any.

8.  (Optional) If you want to submit any further requests, choose **Add
    another request**. If you include multiple requests, provide the
    required information for each. For the required information, see the other
    sections within [Requesting support for Amazon SNS SMS messaging](channels-sms-awssupport.md "channels-sms-awssupport.md").
9.  Under **Contact options**, for **Preferred contact
    language**, choose the language in which you want to receive
    communications for this case.
10. When you finish, choose **Submit**.

The Support team provides an initial response to your request within 24 hours.

To prevent our systems from being used to send unsolicited or malicious content, we
consider each request carefully. If we can, we will grant your request within this 24-hour
period. However, if we need additional information from you, it might take longer to resolve your
request.

If your use case doesn't align with our policies, we might be unable to grant your request.

## Step 2: Update your

SMS settings on the Amazon SNS console

After we notify you that your monthly spending quota has been increased, you have to
adjust the spending quota for your account on the Amazon SNS console.

###### Important

You must complete the following steps or your SMS spend limit will not be
increased.

###### To adjust your spending quota on the console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Open the left navigation menu, expand **Mobile**, and then
   choose **Text messaging (SMS)**.
3. On the **Mobile text messaging (SMS)** page, in the
   **Text messaging preferences** section, choose
   **Edit**.
4. On the **Edit text messaging preferences** page, in the
   **Details** section, enter your new SMS spend limit in the
   **Account spend limit** field.

###### Note

You might receive a warning that the entered value is larger than the
default spend limit. You can ignore this. 5. Choose **Save** changes.

###### Note

If you get an "Invalid Parameter" error, check the contact from AWS
Support and confirm that you entered the correct new SMS spend limit. If you
still experience a problem, open a case in the AWS Support Center.
