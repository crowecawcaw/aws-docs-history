End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Creating an alarm model in AWS IoT Events

You can use AWS IoT Events alarms to monitor your data and get notified when a threshold is
breached. Alarms provide parameters that you use to create or configure an alarm model.
You can use the AWS IoT Events console or AWS IoT Events API to create or configure the alarm model. When
you configure the alarm model, changes take effect as new data arrives.

## Requirements

The following requirements apply when you create an alarm model.

- You can create an alarm model to monitor an input attribute in AWS IoT Events or an
  asset property in AWS IoT SiteWise.
  - If you choose to monitor an input attribute in AWS IoT Events, [Create an input for models in AWS IoT Events](create-input-overview.md "create-input-overview.md") before you create the
    alarm model.
  - If you choose to monitor an asset property, you must [create an asset
    model](../../../iot-sitewise/latest/userguide/create-asset-models.md "../../../iot-sitewise/latest/userguide/create-asset-models.md") in AWS IoT SiteWise before you create the alarm
    model.

- You must have an IAM role that allows your alarm to perform actions and
  access AWS resources. For more information, see [Setting up permissions for
  AWS IoT Events](iotevents-start.md "iotevents-start.md").
- All the AWS resources that this tutorial uses must be in the same AWS
  Region.

## Creating an alarm model (console)

The following shows you how to create an alarm model to monitor an AWS IoT Events attribute
in the AWS IoT Events console.

1. Sign in to the [AWS IoT Events
   console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/").
2. In the navigation pane, choose **Alarm models**.
3. On the **Alarm models** page, choose **Create
   alarm model**.
4. In the **Alarm model details** section, do the
   following:
   1. Enter a unique name.
   2. (Optional) Enter a description.

5. In the **Alarm target** section, do the following:

###### Important

If you choose **AWS IoT SiteWise asset property**, you must
have created an asset model in AWS IoT SiteWise.

    1. Choose **AWS IoT Events input attribute**.
    2. Choose the input.
    3. Choose the input attribute key. This input attribute is used as a
     key to create the alarm. AWS IoT Events routes inputs associated with this
     key to the alarm.


    ###### Important

    If the input message payload does not contain this input
     attribute key, or if the key is not in the same JSON path
     specified in the key, then the message will fail the ingestion
     in AWS IoT Events.

6.  In the **Threshold definitions** section, you define the
    input attribute, threshold value, and comparison operator that AWS IoT Events uses to
    change the state of the alarm.
    1. For **Input attribute**, choose the attribute
       that you want to monitor.

    Each time that this input attribute receives new data, it's
    evaluated to determine the state of the alarm. 2. For **Operator**, choose the comparison operator.
    The operator compares your input attribute with the threshold value
    for your attribute.

    You can choose from these options:

        * **> greater than**
        * **>= greater than or equal to**
        * **< less than**
        * **<= less than or equal to**
        * **= equal to**
        * **!= not equal to**

    3. For threshold **Value**, enter a number or choose
       an attribute in AWS IoT Events inputs. AWS IoT Events compares this value with the
       value of the input attribute you choose.
    4. (Optional) For **Severity**, Use a number that
       your team understands to reflect the severity of this alarm.

7.  (Optional) In the **Notification settings** section,
    configure notification settings for the alarm.

You can add up to 10 notifications. For **Notification
1**, do the following:

    1. For **Protocol**, choose from the following
     options:




    	* **Email & text** - The alarm sends an
    	 SMS notification and an email notification.
    	* **Email** - The alarm sends an email
    	 notification.
    	* **Text** - The alarm sends an SMS
    	 notification.
    2. For **Sender**, specify the email address that
     can send notifications about this alarm.


    To add more email addresses to your sender list, choose
     **Add sender**.
    3. (Optional) For **Recipient**, choose the
     recipient.


    To add more users to your recipient list, choose **Add new
     user**. You must add new users to your IAM Identity Center store
     before you can add them to your alarm model. For more information,
     see [Manage IAM Identity Center access of alarm
     recipients in AWS IoT Events](sso-authorization-recipients.md "sso-authorization-recipients.md").
    4. (Optional) For **Additional custom message**,
     enter a message that describes what the alarm detects and what
     actions the recipients should take.

8.  In the **Instance** section, you can enable or disable
    all alarm instances that are created based on this alarm model.
9.  In the **Advanced settings** section, do the
    following:
    1.  For **Acknowledge flow**, you can enable or
        disable notifications.

            * If you choose **Enabled**, you receive a
             notification when the alarm state changes. You must
             acknowledge the notification before the alarm state can
             return to normal.
            * If you choose **Disabled**, no action is
             required. The alarm automatically changes to the normal
             state when the measurement returns to the specified
             range.

        For more information, see [Acknowledge flow](iotevents-alarms.md#acknowledge-flow "iotevents-alarms.md#acknowledge-flow").

    2.  For **Permissions**, choose one of the following
        options:

            * You can **Create a new role from AWS policy
             templates** and AWS IoT Events automatically creates an
             IAM role for you.
            * You can **Use an existing IAM role**
             that allows this alarm model to perform actions and access
             other AWS resources.

        For more information, see [Identity and access
        management for AWS IoT Events](security-iam.md "security-iam.md").

    3.  For **Additional notification settings**, you can
        edit your AWS Lambda function to manage alarm notifications. Choose
        one of the following options for your AWS Lambda function:

            * **Create a new AWS Lambda function** -
             AWS IoT Events creates a new AWS Lambda function for you.
            * **Use an existing AWS Lambda function** -
             Use an existing AWS Lambda function by choosing an AWS Lambda
             function name.

        For more information about the possible actions, see [AWS IoT Events working with other AWS services](iotevents-other-aws-services.md "iotevents-other-aws-services.md").

    4.  (Optional) For **Set state action**, you can add
        one or more AWS IoT Events actions to take when the alarm state
        changes.

10. (Optional) You can add **Tags** to manage your alarms.
    For more information, see [Tagging your AWS IoT Events
    resources](tagging-iotevents.md "tagging-iotevents.md").
11. Choose **Create**.
