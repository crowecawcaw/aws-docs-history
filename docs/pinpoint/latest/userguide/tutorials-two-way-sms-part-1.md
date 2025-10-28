**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Set up SMS in Amazon Pinpoint

Before you can set up SMS messages, you need an Amazon Pinpoint project. In this section, you do the
following:

- Create an Amazon Pinpoint project
- Enable the SMS channel and lease a phone number
- Configure two-way SMS messaging
  Before you begin, review the [prerequisites](tutorials-two-way-sms-prereqs.md "tutorials-two-way-sms-prereqs.md").

To get started, you need to create an Amazon Pinpoint project. In Amazon Pinpoint, a
_project_ consists of segments, campaigns, configurations, and
data that are united by a common purpose. For example, you could use a project to
contain all of the content that's related to a particular app, or to a specific brand or
marketing initiative. When you add customer information to Amazon Pinpoint, that information is
associated with a project.

The steps involved in creating a new project differ depending on whether you've
created a project in Amazon Pinpoint previously.

These steps describe the process of creating a new Amazon Pinpoint project if you've
never created a project in the current AWS Region.

###### To create a project

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. Use the Region selector to choose the AWS Region that you want to
   use, as shown in the following image. If you're unsure, choose the
   Region that's located closest to you.

![The Region drop down showing US East (N. Virginia) selected.](images/Region_Selector.png) 3. Under **Get started**, for **Name**,
enter a name for the campaign (such as
`SMSRegistration`), and then choose
**Create project**. 4. On the **Configure features** page, choose
**Skip this step**. 5. In the navigation pane, choose **All
projects**. 6. On the **All projects** page, next to the project you
just created, copy the value that's shown in the **Project
ID** column.

###### Tip

You need to use this ID in a few different places in this
tutorial. Keep the project ID in a convenient place so that you can
copy it later.
These steps describe the process of creating a new Amazon Pinpoint project if you've
already created projects in the current AWS Region.

###### To create a project

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. Use the Region selector to choose the AWS Region that you want to
   use, as shown in the following image. If you're unsure, choose the
   Region that's located closest to you.

![The region drop down showing US East (N. Virginia) selected.](images/Region_Selector.png) 3. On the **All projects** page, choose **Create
a project**. 4. On the **Create a project** window, for
**Project name**, enter a name for the project
(such as `SMSRegistration`). Choose
**Create**. 5. On the **Configure features** page, choose
**Skip this step**. 6. In the navigation pane, choose **All
projects**. 7. On the **All projects** page, next to the project you
just created, copy the value that's shown in the **Project
ID** column.

###### Tip

You need to use this ID in a few different places in this
tutorial. Keep the project ID in a convenient place so that you can
copy it later.

###### Note

Amazon Pinpoint has updated their user guide documentation. To get the latest information
regarding how to create, configure, and manage your SMS and voice resources, see
the new [AWS End User Messaging SMS user guide](../../../sms-voice/latest/userguide/what-is-service.md "../../../sms-voice/latest/userguide/what-is-service.md").

After you create a project, you can start to configure features within that project.
In this section, you enable the SMS channel, and obtain a dedicated phone number to use
when sending SMS messages.

###### Note

This section assumes that you're leasing a United States 10DLC phone number after
brand and campaign registration, United States Toll-Free number, or Canada long
code. If you follow the procedures in this section, but choose a country other than
the United States or Canada, you won't be able to use that number to send SMS
messages. To learn more about leasing SMS-capable long codes in countries other than
the United States or Canada, see [Supported countries and regions (SMS channel)](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") in the
_AWS End User Messaging SMS User Guide_.

To enable the SMS channel using the Amazon Pinpoint console, follow these steps:

###### Enable SMS channel

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, under **Settings**, choose
   **SMS and voice**.
3. Next to **SMS settings**, choose
   **Edit**.
4. Under **General settings**, choose **Enable the SMS
   channel for this project**, and then choose **Save
   changes**.
   To request a phone number using the AWS End User Messaging SMS console, follow these steps:

###### Request a phone number (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").

###### Note

Make sure you request a phone number in the same AWS Region that you created your Amazon Pinpoint project in. 2. In the navigation pane, under **Configurations**, choose
**Phone numbers** and then **Request originator**. 3. On the **Select country** page for **Message
destination country** choose either the United States or Canada.
Choose **Next**. 4. On the **Messaging use case** section, enter the following:

    * Under **Number capabilities** choose
     **SMS**

    ###### Important

    Capabilities for SMS and Voice can't be changed once the phone number has been purchased.
    * For **Two-way messaging** choose **Yes**.

5. Choose **Next**.
6. Under **Select originator type** choose either **Long code** or **10DLC**.

If you choose 10DLC and already have a registered campaign you can choose the campaign
from the **Associate to registered campaign**. 7. Choose **Next**. 8. On **Review and request** you can verify and edit your request before submitting it. Choose **Request**. 9. A **Registration Required** window may appear depending on
the type of phone number you requested. Your phone number is associated with
this registration and you can't send messages until your registration has been
approved. For more information about registrations requirements see [Registrations](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md").

    1. For **Registration form name** enter a friendly name.
    2. Choose **Begin registration** to finish registering the phone
     number or **Register later**.


    ###### Important

    Your phone number can't send messages until your registration has
     been approved.


     You are still billed the recurring monthly lease fee for the phone number regardless of
     registration status. For more information about registrations requirements see [Registrations](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md").

Now that you have a dedicated phone number, you can set up two-way SMS. Enabling
two-way SMS makes it possible for your customers to respond to the SMS messages that you
send them. In this solution, you use two-way SMS to give your customers a way to confirm
that they want to subscribe to your SMS program.

To enable two-way SMS using the AWS End User Messaging SMS console, follow these steps:

###### Enable two-way SMS

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone numbers**.
3. On the **Phone numbers** page choose a phone
   number.
4. On the **Two-way SMS** tab choose the **Edit
   settings** button.
5. On the **Edit settings** page choose **Enable
   two-way message**.
6. For **Destination type** choose
   **Amazon SNS**.
   - **New Amazon SNS topic** – AWS End User Messaging SMS creates a
     topic in your account. The topic is automatically created with
     all of the required permissions. For more information on Amazon SNS
     topics see [Configuring Amazon SNS](../../../sns/latest/dg/sns-configuring.md "../../../sns/latest/dg/sns-configuring.md") in the _Amazon SNS developer guide_.
   - For **incoming message destination** enter a topic name,
     such as `SMSRegistrationFormTopic`.

7. For **Two-way channel role** choose **Use SNS topic policies**.
8. Choose **Save changes**.
   Use the AWS End User Messaging SMS console to add keywords to your phone number that customers send you to
   confirm their subscriptions (such as `Yes` or `Confirm`).

###### Add a keyword

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone number**.
3. On the **Phone number** page choose the phone number to add a
   keyword to.
4. On the **Keywords** tab choose the **Add
   keyword** button.
5. In the **Custom Keyword** pane add the
   following:
   - **Keyword** – The new keyword to add (such as
     `Yes` or
     `Confirm`).
   - **Response message** – The message
     to send back to the recipient.
   - **Keyword action** – The action to perform when
     the keyword is received. Choose **Automatic response**.

6. Choose **Add keyword**.
   **Next**: [Create
   IAM policies and roles](tutorials-two-way-sms-part-2.md "tutorials-two-way-sms-part-2.md")
