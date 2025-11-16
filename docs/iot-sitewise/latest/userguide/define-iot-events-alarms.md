# Define AWS IoT Events alarms for AWS IoT SiteWise

###### Note

End of support notice: AWS ended support for AWS IoT Events. For more information, see [AWS IoT Events end of support](../../../iotevents/latest/developerguide/iotevents-end-of-support.md "../../../iotevents/latest/developerguide/iotevents-end-of-support.md").

When you create an AWS IoT Events alarm, AWS IoT SiteWise sends asset property values to AWS IoT Events to evaluate
the state of the alarm. AWS IoT Events alarm definitions depend on an alarm model that you define in
AWS IoT Events. To define an AWS IoT Events alarm on an asset model, you define an alarm composite model that
specifies the AWS IoT Events alarm model as its alarm source property.

AWS IoT Events alarms depend on inputs such as alarm thresholds and alarm notification settings.
You define these inputs as attributes on the asset model. You can then customize these
inputs on each asset based on the model. The AWS IoT SiteWise console can create these attributes for
you. If you define alarms with the AWS CLI or API, you must manually define these attributes
on the asset model.

You can also define other actions that happen when your alarm detects, such as custom
alarm notification actions. For example, you can configure an action that sends a push
notification to an Amazon SNS topic. For more information the actions that you can define,
see [Working with
other AWS services](../../../iotevents/latest/developerguide/iotevents-other-aws-services.md "../../../iotevents/latest/developerguide/iotevents-other-aws-services.md") in the _AWS IoT Events Developer Guide_.

When you update or delete an asset model, AWS IoT SiteWise can check if an alarm model in AWS IoT Events
is monitoring an asset property associated with this asset model. This prevents you from deleting an asset property
that an AWS IoT Events alarm is currently using. To enable this feature in AWS IoT SiteWise, you must have the `iotevents:ListInputRoutings` permission.
This permission allows AWS IoT SiteWise to make calls to the [ListInputRoutings](../../../iotevents/latest/apireference/API_ListInputRoutings.md "../../../iotevents/latest/apireference/API_ListInputRoutings.md") API operation supported by AWS IoT Events.
For more information, see [(Optional) ListInputRoutings permission](alarms-iam-permissions.md#alarms-listInputRoutings-permissions "alarms-iam-permissions.md#alarms-listInputRoutings-permissions").

###### Note

The alarm notifications feature isn't available in the China (Beijing) Region.

###### Topics

- [Define an AWS IoT Events alarm (AWS IoT SiteWise
  console)](#define-iot-events-alarm-console "#define-iot-events-alarm-console")
- [Define an AWS IoT Events alarm (AWS IoT Events
  console)](#define-iot-events-alarm-console-ite-console "#define-iot-events-alarm-console-ite-console")
- [Define an AWS IoT Events alarm (AWS CLI)](#define-iot-events-alarm-cli "#define-iot-events-alarm-cli")

## Define an AWS IoT Events alarm (AWS IoT SiteWise

console)

You can use the AWS IoT SiteWise console to define an AWS IoT Events alarm on an existing asset model. To
define an AWS IoT Events alarm on a new asset model, create the asset model, and then complete
these steps. For more information, see [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md").

###### Important

Each alarm requires an attribute that specifies the threshold value to compare
against for the alarm. You must define the threshold value attribute on the asset model
before you can define an alarm.

Consider an example where you want to define an alarm that detects when a wind
turbine exceeds its maximum wind speed rating of 50 mph. Before you define the alarm,
you must define an attribute (**Maximum wind speed**) with a default
value of `50`.

###### To define an AWS IoT Events alarm on an asset model

1.  Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2.  In the navigation pane, choose **Models**.
3.  Choose the asset model for which to define an alarm.
4.  Choose the **Alarm** tab.
5.  Choose **Add alarm**.
6.  In the **Alarm type options** section, choose **AWS IoT Events
    alarm**.
7.  In the **Alarm details** section, do the following:
    1. Enter a name for your alarm.
    2. (Optional) Enter a description for your alarm.

8.  In the **Threshold definitions** section, you define when the alarm
    detects and the severity of the alarm. Do the following:
    1. Select the **Property** on which the alarm detects. Each time
       this property receives a new value, AWS IoT SiteWise sends the value to AWS IoT Events to evaluate
       the state of the alarm.
    2. Select the **Operator** to use to compare the property with
       the threshold value. Choose from the following options:
       - **< less than**
       - **<= less than or equal**
       - **== equal**
       - **!= not equal**
       - **>= greater than or equal**
       - **> greater than**

    3. For **Value**, select the attribute property to use as the threshold
       value. AWS IoT Events compares the value of the property with the
       value of this attribute.
    4. Enter the **Severity** of the alarm. Use a number that your
       team understands to reflect the severity of this alarm.

9.  (Optional) In the **Notification settings - _optional_** section, do the following:
    1. Choose **Active**.

    ###### Note

    If you choose **Inactive**, you and your team won't receive any alarm notifications. 2. For **Recipient**, choose the recipient.

    ###### Important

    You can send alarm notifications to AWS IAM Identity Center users. To use this feature, you must enable
    IAM Identity Center. You can only enable IAM Identity Center in one AWS Region at a time. This means that you can define
    alarm notifications only in the Region where you enable IAM Identity Center. For more information, see
    [Getting
    started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the _AWS IAM Identity Center User Guide_. 3. For **Protocol**, choose from the following options:

        * **Email & text** – The alarm notifies IAM Identity Center
         users with an SMS message and an email message.
        * **Email** – The alarm notifies IAM Identity Center users with an
         email message.
        * **Text** – The alarm notifies IAM Identity Center users with an
         SMS message.

    4. For **Sender**, choose the sender.

    ###### Important

    You must verify the sender email address in Amazon Simple Email Service (Amazon SES). For more
    information, see [Verifying an email address identity](../../../ses/latest/dg/creating-identities.md#just-verify-email-proc "../../../ses/latest/dg/creating-identities.md#just-verify-email-proc"), in the
    _Amazon Simple Email Service Developer Guide_.

10. In the **Default asset state** section, you
    can set the default state for alarms created from this asset model.

###### Note

You activate or deactivate this alarm for assets that you create from this asset model
in a later step. 11. In the **Advanced settings** section, you can configure the permissions,
the additional notification settings, the alarm state actions, the alarm model in SiteWise Monitor,
and the acknowledge flow.

###### Note

AWS IoT Events alarms require the following service roles:

    * A role that AWS IoT Events assumes to send alarm state values to AWS IoT SiteWise.
    * A role that AWS IoT Events assumes to send data to Lambda.
     You only need this role if your alarm sends notifications.

In the **Permissions** section, do the following:

    1. For **AWS IoT Events role**, use an existing role or create a role
     with the required permissions. This role requires the `iotsitewise:BatchPutAssetPropertyValue` permission
     and a trust relationship that allows iotevents.amazonaws.com to assume the role.
    2. For the **AWS IoT Events Lambda role**, use an existing role or create a role
     with the required permissions. This role requires the `lambda:InvokeFunction` and
     `sso-directory:DescribeUser` permissions
     and a trust relationship that allows `iotevents.amazonaws.com` to assume the role.

12. (Optional) In the **Additional notification settings** section, do the following:
    1.  For **Recipient attribute**, you define an attribute whose
        value specifies the recipient of the notification. You can choose IAM Identity Center users as
        recipients.

    You can create an attribute or use an existing attribute on the asset
    model.

        * If you choose **Create a new recipient attribute**, specify the
         **Recipient attribute name** and **Recipient default
         value - **optional**** for the attribute.
        * If you choose **Use an existing recipient attribute**, choose the
         attribute in **Recipient attribute name**. The alarm uses
         the default value of the attribute that you choose.

    You can override the default value on each asset that you create from this
    asset model. 2. For **Custom message attribute**, you define an attribute
    whose value specifies the custom message to send in addition to the default state
    change message. For example, you can specify a message that helps your team
    understand how to address this alarm.

    You can choose to create an attribute or use an existing attribute on the
    asset model.

        * If you choose to **Create a new custom message attribute**, specify the
         **Custom message attribute name** and **Custom message default
         value - *optional*** for the attribute.
        * If you choose **Use an existing custom message attribute**, choose the
         attribute in **Custom message attribute name**. The alarm uses
         the default value of the attribute that you choose.

    You can override the default value on each asset that you create from this
    asset model. 3. For **Manage your Lambda function**, do one of the following:

        * To have AWS IoT SiteWise create a new Lambda function, choose **Create a new lambda from an AWS managed template**.
        * To use an existing Lambda function, choose **Use an existing lambda** and choose the name of the function.

    For more information, see [Managing alarm notifications](../../../iotevents/latest/developerguide/lambda-support.md "../../../iotevents/latest/developerguide/lambda-support.md")
    in the _AWS IoT Events Developer Guide_.

13. (Optional) In the **Set state action** section, do the following:
    1.  Choose **Edit action**.
    2.  Under **Add alarm state actions**, add actions. and the choose **Save**.

    You can add up to 10 actions.AWS IoT Events can perform actions when the alarm is active. You can define built-in actions to use a timer or set a variable,
    or send data to other AWS resources. For more information, see [Supported actions](../../../iotevents/latest/developerguide/iotevents-supported-actions.md "../../../iotevents/latest/developerguide/iotevents-supported-actions.md")
    in the _AWS IoT Events Developer Guide_.

14. (Optional) Under **Manage alarm model in SiteWise Monitor - _optional_**,
    choose **Active** or **Inactive**.

Use this option so that you can update the alarm model in SiteWise Monitorss. This option is enabled by default. 15. Under **Acknowledge flow**, choose **Active** or **Inactive**. For more information about the acknowledge flow, see
[Alarm states](industrial-alarms.md#alarm-states "industrial-alarms.md#alarm-states"). 16. Choose **Add alarm**.

###### Note

The AWS IoT SiteWise console makes multiple API requests to add the alarm to the asset
model. When you choose **Add alarm**, the console opens a dialog box
that shows the progress of these API requests. Stay on this page until each API
requests succeeds or until an API request fails. If a request fails, close the dialog
box, fix the issue, and choose **Add alarm** to try again.

## Define an AWS IoT Events alarm (AWS IoT Events

console)

You can use the AWS IoT Events console to define an AWS IoT Events alarm on an existing asset model. To
define an AWS IoT Events alarm on a new asset model, create the asset model, and then complete
these steps. For more information, see [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md").

###### Important

Each alarm requires an attribute that specifies the threshold value to compare
against for the alarm. You must define the threshold value attribute on the asset model
before you can define an alarm.

Consider an example where you want to define an alarm that detects when a wind
turbine exceeds its maximum wind speed rating of 50 mph. Before you define the alarm,
you must define an attribute (**Maximum wind speed**) with a default
value of `50`.

###### To define an AWS IoT Events alarm on an asset model

1. Navigate to the [AWS IoT Events console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/").
2. In the navigation pane, choose **Alarm models**.
3. Choose **Create alarm model**.
4. Enter a name for your alarm.
5. (Optional) Enter a description for your alarm.
6. In the **Alarm target** section, do the following:
   1. For **Target options**, choose **AWS IoT SiteWise asset property**.
   2. Choose the asset model for which you want to add the alarm.

7. In the **Threshold definitions** section, you define when the alarm
   detects and the severity of the alarm. Do the following:
   1. Select the **Property** on which the alarm detects. Each time
      this property receives a new value, AWS IoT SiteWise sends the value to AWS IoT Events to evaluate
      the state of the alarm.
   2. Select the **Operator** to use to compare the property with
      the threshold value. Choose from the following options:
      - **< less than**
      - **<= less than or equal**
      - **== equal**
      - **!= not equal**
      - **>= greater than or equal**
      - **> greater than**

   3. For **Value**, select the attribute property to use as the threshold
      value. AWS IoT Events compares the value of the property with the
      value of this attribute.
   4. Enter the **Severity** of the alarm. Use a number that your
      team understands to reflect the severity of this alarm.

8. (Optional) In the **Notification settings - _optional_** section, do the following:
   1. For **Protocol**, choose from the following options:
      - **Email & text** – The alarm notifies IAM Identity Center
        users with an SMS message and an email message.
      - **Email** – The alarm notifies IAM Identity Center users with an
        email message.
      - **Text** – The alarm notifies IAM Identity Center users with an
        SMS message.

   2. For **Sender**, choose the sender.

   ###### Important

   You must verify the sender email address in Amazon Simple Email Service (Amazon SES). For more
   information, see [Verifying email addresses in Amazon SES](../../../ses/latest/dg/verify-addresses-and-domains.md "../../../ses/latest/dg/verify-addresses-and-domains.md"), in the
   _Amazon Simple Email Service Developer Guide_. 3. Choose the attribute in **Recipient attribute - _optional_**. The alarm uses
   the default value of the attribute that you choose. 4. Choose the attribute in **Custom message attribute - _optional_**. The alarm uses
   the default value of the attribute that you choose.

9. In the **Instance** section, specify the **Default state** for this alarm. You
   can activate or deactivate this alarm for all assets that you create from this asset model
   in a later step.
10. In the **Advanced settings** settings, you can configure the permissions,
    the additional notification settings, the alarm state actions, the alarm model in SiteWise Monitor,
    and the acknowledge flow.

###### Note

AWS IoT Events alarms require the following service roles:

    * A role that AWS IoT Events assumes to send alarm state values to AWS IoT SiteWise.
    * A role that AWS IoT Events assumes to send data to Lambda.
     You only need this role if your alarm sends notifications.
    1. In the **Acknowledge flow** section, choose **Enabled** or **Disabled**.
     For more information about the acknowledge flow, see
     [Alarm states](industrial-alarms.md#alarm-states "industrial-alarms.md#alarm-states").
    2. In the **Permissions** section, do the following:


    	1. For **AWS IoT Events role**, use an existing role or create a role
    	 with the required permissions. This role requires the `iotsitewise:BatchPutAssetPropertyValue` permission
    	 and a trust relationship that allows iotevents.amazonaws.com to assume the role.
    	2. For the **Lambda role**, use an existing role or create a role
    	 with the required permissions. This role requires the `lambda:InvokeFunction` and
    	 `sso-directory:DescribeUser` permissions
    	 and a trust relationship that allows `iotevents.amazonaws.com` to assume the role.
    3. (Optional) In the **Additional notification settings** pane, do the following:


    	1. For **Manage your Lambda function**, do one of the following:




    		* To have AWS IoT Events create a new Lambda function, choose **Create a new Lambda function**.
    		* To use an existing Lambda function, choose **Use an existing Lambda function** and choose the name of the function.
    	For more information, see [Managing alarm notifications](../../../iotevents/latest/developerguide/lambda-support.md "../../../iotevents/latest/developerguide/lambda-support.md")
    	 in the *AWS IoT Events Developer Guide*.
    4. (Optional) In the **Set state action - *optional*** section, do the following:


    	1. Under **Alarm state actions**, add actions. and the choose **Save**.


    	You can add up to 10 actions.AWS IoT Events can perform actions when the alarm is active. You can define built-in actions to use a timer or set a variable,
     or send data to other AWS resources. For more information, see [Supported actions](../../../iotevents/latest/developerguide/iotevents-supported-actions.md "../../../iotevents/latest/developerguide/iotevents-supported-actions.md")
     in the *AWS IoT Events Developer Guide*.

11. Choose **Create**.

###### Note

The AWS IoT Events console makes multiple API requests to add the alarm to the asset
model. When you choose **Add alarm**, the console opens a dialog box
that shows the progress of these API requests. Stay on this page until each API
requests succeeds or until an API request fails. If a request fails, close the dialog
box, fix the issue, and choose **Add alarm** to try again.

## Define an AWS IoT Events alarm (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to define an AWS IoT Events alarm that monitors an asset
property. You can define the alarm on a new or existing asset model. After you define the
alarm on the asset model, you create an alarm in AWS IoT Events and connect it to the
asset model. In this process, you do the following:

###### Steps

- [Step 1: Define an alarm on an
  asset model](#define-iot-events-alarm-definition-cli "#define-iot-events-alarm-definition-cli")
- [Step 2: Define an AWS IoT Events alarm
  model](#define-iot-events-alarm-model-cli "#define-iot-events-alarm-model-cli")
- [Step 3: Enable data flow between
  AWS IoT SiteWise and AWS IoT Events](#define-iot-events-alarm-data-flow-cli "#define-iot-events-alarm-data-flow-cli")

### Step 1: Define an alarm on an

asset model

Add an alarm definition and associated properties to a new or existing asset
model.

###### To define an alarm on an asset model (CLI)

1. Create a file called `asset-model-payload.json`. Follow the
   steps in these other sections to add your asset model's details to the file, but
   don't submit the request to create or update the asset model. In this section, you
   add an alarm definition to the asset model details in the
   `asset-model-payload.json` file.
   - For more information about how to create an asset model, see [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli").
   - For more information about how to update an existing asset model, see [Update an asset model, component model, or interface
     (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli").###### Note

Your asset model must define at least one asset property, including the asset
property to monitor with the alarm. 2. Add an alarm composite model (`assetModelCompositeModels`) to the
asset model. An AWS IoT Events alarm composite model specifies the `IOT_EVENTS`
type and specifies an alarm source property. You add the alarm source property after
you create the alarm model in AWS IoT Events.

###### Important

The alarm composite model must have the same name as the AWS IoT Events alarm model you
create later. Alarm model names can contain only alphanumeric characters. Specify
a unique, alphanumeric name so that you can use the same name for the alarm
model.

```
{
  `...`
  "assetModelCompositeModels": [
    {
      "name": "BoilerTemperatureHighAlarm",
      "type": "AWS/ALARM",
      "properties": [
        {
          "name": "AWS/ALARM_TYPE",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "IOT_EVENTS"
            }
          }
        },
        {
          "name": "AWS/ALARM_STATE",
          "dataType": "STRUCT",
          "dataTypeSpec": "AWS/ALARM_STATE",
          "type": {
            "measurement": {}
          }
        }
      ]
    }
  ]
}
```

3. Add an alarm threshold attribute to the asset model. Specify the default value
   to use for this threshold. You can override this default value on each asset based
   on this model.

###### Note

The alarm threshold attribute must be an `INTEGER` or a
`DOUBLE`.

```
{
  `...`
  "assetModelProperties": [
    `...`
    {
      "name": "Temperature Max Threshold",
      "dataType": "DOUBLE",
      "type": {
        "attribute": {
          "defaultValue": "105.0"
        }
      }
    }
  ]
}
```

4. (Optional) Add alarm notification attributes to the asset model. These
   attributes specify the IAM Identity Center recipient and other inputs that AWS IoT Events uses to send
   notifications when the alarm changes state. You can override these defaults on each
   asset based on this model.

###### Important

You can send alarm notifications to AWS IAM Identity Center users. To use this feature, you must enable
IAM Identity Center. You can only enable IAM Identity Center in one AWS Region at a time. This means that you can define
alarm notifications only in the Region where you enable IAM Identity Center. For more information, see
[Getting
started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the _AWS IAM Identity Center User Guide_.

Do the following:

    1. Add an attribute that specifies the ID of your IAM Identity Center identity store. You can
     use the IAM Identity Center [ListInstances](../../../singlesignon/latest/APIReference/API_ListInstances.md "../../../singlesignon/latest/APIReference/API_ListInstances.md") API operation to list your identity stores. This
     operation works only in the Region where you enable IAM Identity Center.



    ```
    aws sso-admin list-instances
    ```

    Then, specify the identity store ID (for example, `d-123EXAMPLE`)
     as the default value for the attribute.



    ```
    {
      `...`
      "assetModelProperties": [
        `...`
        {
          "name": "`identityStoreId`",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "`d-123EXAMPLE`"
            }
          }
        }
      ]
    }
    ```
    2. Add an attribute that specifies the ID of the IAM Identity Center user who receives
     notifications. To define a default notification recipient, add an IAM Identity Center user ID
     as the default value. Do one of the following to get an IAM Identity Center user ID:


    	1. You can use the IAM Identity Center [ListUsers](../../../singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.md "../../../singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.md") API to get the ID of a user whose user name you know.
    	 Replace `d-123EXAMPLE` with the ID of your identity
    	 store, and replace `Name` with the user name of the
    	 user.



    	```
    	aws identitystore list-users \
    	  --identity-store-id `d-123EXAMPLE` \
    	  --filters AttributePath=UserName,AttributeValue=`Name`
    	```
    	2. Use the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon")
    	 to browse your users and find a user ID.Then, specify the user ID (for example,
     `123EXAMPLE-a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`) as the default
     value for the attribute, or define the attribute without a default value.



    ```
    {
      `...`
      "assetModelProperties": [
        `...`
        {
          "name": "`userId`",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "`123EXAMPLE-a1b2c3d4-5678-90ab-cdef-33333EXAMPLE`"
            }
          }
        }
      ]
    }
    ```
    3. (Optional) Add an attribute that specifies the default sender ID for SMS
     (text) message notifications. The sender ID displays as the message sender on
     messages that Amazon Simple Notification Service (Amazon SNS) sends. For more information, see [Request a sender
     ID in AWS End User Messaging SMS](../../../sms-voice/latest/userguide/sender-id-request.md "../../../sms-voice/latest/userguide/sender-id-request.md") in the
     *AWS End User Messaging SMS User Guide*.



    ```
    {
      `...`
      "assetModelProperties": [
        `...`
        {
          "name": "`senderId`",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "`MyFactory`"
            }
          }
        }
      ]
    }
    ```
    4. (Optional) Add an attribute that specifies the default email address to use
     as the *from* address in email notifications.



    ```
    {
      `...`
      "assetModelProperties": [
        `...`
        {
          "name": "`fromAddress`",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "`my.factory@example.com`"
            }
          }
        }
      ]
    }
    ```
    5. (Optional) Add an attribute that specifies the default subject to use in
     email notifications.



    ```
    {
      `...`
      "assetModelProperties": [
        `...`
        {
          "name": "`emailSubject`",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "`[ALERT] High boiler temperature`"
            }
          }
        }
      ]
    }
    ```
    6. (Optional) Add an attribute that specifies an additional message to include
     in notifications. By default, notification messages include information about
     the alarm. You can also include an additional message that gives the user more
     information..



    ```
    {
      `...`
      "assetModelProperties": [
        `...`
        {
          "name": "`additionalMessage`",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "`Turn off the power before you check the alarm.`"
            }
          }
        }
      ]
    }
    ```

5. Create the asset model or update the existing asset model. Do one of the
   following:
   - To create the asset model, run the following command.

   ```
   aws iotsitewise create-asset-model --cli-input-json file://asset-model-payload.json
   ```

   - To update the existing asset model, run the following command. Replace
     `asset-model-id` with the ID of the asset
     model.

   ````
   aws iotsitewise update-asset-model \
     --asset-model-id `asset-model-id` \
     --cli-input-json file://asset-model-payload.json
   ```After you run the command, note the `assetModelId` in the
   response.
   ````

The following asset model represents a boiler that reports temperature data.
This asset model defines an alarm that detects when the boiler overheats.

```
{
  "assetModelName": "Boiler Model",
  "assetModelDescription": "Represents a boiler.",
  "assetModelProperties": [
    {
      "name": "Temperature",
      "dataType": "DOUBLE",
      "unit": "C",
      "type": {
        "measurement": {}
      }
    },
    {
      "name": "Temperature Max Threshold",
      "dataType": "DOUBLE",
      "type": {
        "attribute": {
          "defaultValue": "105.0"
        }
      }
    },
    {
      "name": "identityStoreId",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "d-123EXAMPLE"
        }
      }
    },
    {
      "name": "userId",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "123EXAMPLE-a1b2c3d4-5678-90ab-cdef-33333EXAMPLE"
        }
      }
    },
    {
      "name": "senderId",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "MyFactory"
        }
      }
    },
    {
      "name": "fromAddress",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "my.factory@example.com"
        }
      }
    },
    {
      "name": "emailSubject",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "[ALERT] High boiler temperature"
        }
      }
    },
    {
      "name": "additionalMessage",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "Turn off the power before you check the alarm."
        }
      }
    }
  ],
  "assetModelHierarchies": [

  ],
  "assetModelCompositeModels": [
    {
      "name": "BoilerTemperatureHighAlarm",
      "type": "AWS/ALARM",
      "properties": [
        {
          "name": "AWS/ALARM_TYPE",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "IOT_EVENTS"
            }
          }
        },
        {
          "name": "AWS/ALARM_STATE",
          "dataType": "STRUCT",
          "dataTypeSpec": "AWS/ALARM_STATE",
          "type": {
            "measurement": {}
          }
        }
      ]
    }
  ]
}
```

### Step 2: Define an AWS IoT Events alarm

model

Create the alarm model in AWS IoT Events. In AWS IoT Events, you use
_expressions_ to specify values in alarm models. You can
use expressions to specify values from AWS IoT SiteWise to evaluate and use as inputs to the
alarm. When AWS IoT SiteWise sends asset property values to the alarm model, AWS IoT Events
evaluates the expression to get the value of the property or the ID of the asset. You
can use the following expressions in the alarm model:

- Asset property values

To get the value of an asset property, use the following expression. Replace
`assetModelId` with the ID of the asset model and replace
`propertyId` with the ID of the property.

```
$sitewise.assetModel.``assetModelId``.``propertyId``.propertyValue.value
```

- Asset IDs

To get the ID of the asset, use the following expression. Replace
`assetModelId` with the ID of the asset model and replace
`propertyId` with the ID of the property.

```
$sitewise.assetModel.``assetModelId``.``propertyId``.assetId
```

###### Note

When you create the alarm model, you can define literals instead of
expressions that evaluate to AWS IoT SiteWise values. This can reduce the number of attributes
that you define on your asset model. However, if you define a value as a literal, you
can't customize that value on assets based on the asset model. Your AWS IoT SiteWise Monitor users
also can't customize the alarm, because they can configure alarm settings on assets
only.

###### To create an AWS IoT Events alarm model (CLI)

1.  When you create the alarm model in AWS IoT Events, you must specify the ID of
    each property that the alarm uses, which includes the following:

        * The alarm state property in the composite asset model
        * The property that the alarm monitors
        * The threshold attribute
        * (Optional) The IAM Identity Center identity store ID attribute
        * (Optional) The IAM Identity Center user ID attribute
        * (Optional) The SMS sender ID attribute
        * (Optional) The email *from* address attribute
        * (Optional) The email subject attribute
        * (Optional) The additional message attribute

    Run the following command to retrieve the IDs of these properties on the asset
    model. Replace `asset-model-id` with the ID of the asset
    model from the previous step.

```
aws iotsitewise describe-asset-model --asset-model-id `asset-model-id`
```

The operation returns a response that contains the asset model's details. Note
the ID of each property that the alarm uses. You use these IDs when you create the
AWS IoT Events alarm model in the next step. 2. Create the alarm model in AWS IoT Events. Do the following:

    1. Create a file called `alarm-model-payload.json`.
    2. Copy the following JSON object into the file.
    3. Enter a name (`alarmModelName`), description
     (`alarmModelDescription`), and severity (`severity`) for
     your alarm. For severity, specify an integer that reflects your company's
     severity levels.


    ###### Important

    The alarm model must have the same name as the alarm composite
     model that you defined on your asset model earlier.

    Alarm model names can contain only alphanumeric
     characters.



    ```
    {
      **"alarmModelName": "`BoilerTemperatureHighAlarm`",
     "alarmModelDescription": "`Detects when the boiler temperature is high.`",
     "severity": `3`**
    }
    ```
    4. Add the comparison rule (`alarmRule`) to the alarm. This rule
     defines the property to monitor (`inputProperty`), the threshold
     value to compare (`threshold`), and the comparison operator to use
     (`comparisonOperator`).




    	* Replace `assetModelId` with the ID of the asset
    	 model.
    	* Replace `alarmPropertyId` with the ID of the
    	 property that the alarm monitors.
    	* Replace `thresholdAttributeId` with the ID of
    	 the threshold attribute property.
    	* Replace `GREATER` with the operator to use to
    	 compare the property values with the threshold. Choose from the following
    	 options:




    		+ `LESS`
    		+ `LESS_OR_EQUAL`
    		+ `EQUAL`
    		+ `NOT_EQUAL`
    		+ `GREATER_OR_EQUAL`
    		+ `GREATER`

    ```
    {
      "alarmModelName": "`BoilerTemperatureHighAlarm`",
      "alarmModelDescription": "`Detects when the boiler temperature is high.`",
      "severity": `3`,
      **"alarmRule": {
     "simpleRule": {
     "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
     "comparisonOperator": "`GREATER`",
     "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
     }
     }**
    }
    ```
    5. Add an action (`alarmEventActions`) to send alarm state to the
     AWS IoT SiteWise when the alarm changes state.


    ###### Note

    For advanced configuration, you can define additional actions to perform
     when the alarm changes state. For example, you might call an AWS Lambda
     function or publish to an MQTT topic. For more information, see [Working with other AWS services](../../../iotevents/latest/developerguide/iotevents-other-aws-services.md "../../../iotevents/latest/developerguide/iotevents-other-aws-services.md") in the
     *AWS IoT Events Developer Guide*.




    	* Replace `assetModelId` with the ID of the asset
    	 model.
    	* Replace `alarmPropertyId` with the ID of the
    	 property that the alarm monitors.
    	* Replace `alarmStatePropertyId` with the ID of
    	 the alarm state property in the alarm composite model.

    ```
    {
      "alarmModelName": "`BoilerTemperatureHighAlarm`",
      "alarmModelDescription": "`Detects when the boiler temperature is high.`",
      "severity": `3`,
      "alarmRule": {
        "simpleRule": {
          "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
          "comparisonOperator": "`GREATER`",
          "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
        }
      },
      **"alarmEventActions": {
     "alarmActions": [
     {
     "iotSiteWise": {
     "assetId": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.assetId",
     "propertyId": "'`alarmStatePropertyId`'"
     }
     }
     ]
     }**
    }
    ```
    6. (Optional) Configure alarm notification settings. The alarm notification
     action uses a Lambda function in your account to send alarm notifications. For
     more information, see [Requirements for alarm
     notifications in AWS IoT SiteWise](iot-events-alarm-notification-requirements.md "iot-events-alarm-notification-requirements.md"). In the alarm
     notification settings, you can configure SMS and email notifications to send to
     IAM Identity Center users. Do the following:


    	1. Add the alarm notification configuration
    	 (`alarmNotification`) to the payload in
    	 `alarm-model-payload.json`.




    		* Replace `alarmNotificationFunctionArn` with
    		 the ARN of the Lambda function that handles alarm notifications.

    	```
    	{
    	  "alarmModelName": "`BoilerTemperatureHighAlarm`",
    	  "alarmModelDescription": "`Detects when the boiler temperature is high.`",
    	  "severity": `3`,
    	  "alarmRule": {
    	    "simpleRule": {
    	      "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
    	      "comparisonOperator": "`GREATER`",
    	      "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
    	    }
    	  },
    	  "alarmEventActions": {
    	    "alarmActions": [
    	      {
    	        "iotSiteWise": {
    	          "assetId": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.assetId",
    	          "propertyId": "'`alarmStatePropertyId`'"
    	        }
    	      }
    	    ]
    	  },
    	  **"alarmNotification": {
    	 "notificationActions": [
    	 {
    	 "action": {
    	 "lambdaAction": {
    	 "functionArn": "`alarmNotificationFunctionArn`"
    	 }
    	 }
    	 }
    	 ]
    	 }**
    	}
    	```
    	2. (Optional) Configure the SMS notifications
    	 (`smsConfigurations`) to send to an IAM Identity Center user when the alarm
    	 changes state.




    		* Replace `identityStoreIdAttributeId` with
    		 the ID of the attribute that contains the ID of the IAM Identity Center identity
    		 store.
    		* Replace `userIdAttributeId` with the ID of
    		 the attribute that contains the ID of the IAM Identity Center user.
    		* Replace `senderIdAttributeId` with the ID
    		 of the attribute that contains the Amazon SNS sender ID, or remove
    		 `senderId` from the payload.
    		* Replace `additionalMessageAttributeId` with
    		 the ID of the attribute that contains the additional message, or remove
    		 `additionalMessage` from the payload.

    	```
    	{
    	  "alarmModelName": "`BoilerTemperatureHighAlarm`",
    	  "alarmModelDescription": "`Detects when the boiler temperature is high.`",
    	  "severity": `3`,
    	  "alarmRule": {
    	    "simpleRule": {
    	      "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
    	      "comparisonOperator": "`GREATER`",
    	      "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
    	    }
    	  },
    	  "alarmEventActions": {
    	    "alarmActions": [
    	      {
    	        "iotSiteWise": {
    	          "assetId": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.assetId",
    	          "propertyId": "'`alarmStatePropertyId`'"
    	        }
    	      }
    	    ]
    	  },
    	  "alarmNotification": {
    	    "notificationActions": [
    	      {
    	        "action": {
    	          "lambdaAction": {
    	            "functionArn": "`alarmNotificationFunctionArn`"
    	          }
    	        },
    	        **"smsConfigurations": [
    	 {
    	 "recipients": [
    	 {
    	 "ssoIdentity": {
    	 "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
    	 "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
    	 }
    	 }
    	 ],
    	 "senderId": "$sitewise.assetModel.``assetModelId``.``senderIdAttributeId``.propertyValue.value",
    	 "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
    	 }
    	 ]**
    	      }
    	    ]
    	  }
    	}
    	```
    	3. (Optional) Configure the email notifications
    	 (`emailConfigurations`) to send to an IAM Identity Center user when the alarm
    	 changes state.




    		* Replace `identityStoreIdAttributeId` with
    		 the ID of the IAM Identity Center identity store ID attribute property.
    		* Replace `userIdAttributeId` with the ID of
    		 the IAM Identity Center user ID attribute property.
    		* Replace `fromAddressAttributeId` with the
    		 ID of the "from" address attribute property, or remove `from`
    		 from the payload.
    		* Replace `emailSubjectAttributeId` with the
    		 ID of the email subject attribute property, or remove
    		 `subject` from the payload.
    		* Replace `additionalMessageAttributeId` with
    		 the ID of the additional message attribute property, or remove
    		 `additionalMessage` from the payload.

    	```
    	{
    	  "alarmModelName": "`BoilerTemperatureHighAlarm`",
    	  "alarmModelDescription": "`Detects when the boiler temperature is high.`",
    	  "severity": `3`,
    	  "alarmRule": {
    	    "simpleRule": {
    	      "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
    	      "comparisonOperator": "`GREATER`",
    	      "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
    	    }
    	  },
    	  "alarmEventActions": {
    	    "alarmActions": [
    	      {
    	        "iotSiteWise": {
    	          "assetId": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.assetId",
    	          "propertyId": "'`alarmStatePropertyId`'"
    	        }
    	      }
    	    ]
    	  },
    	  "alarmNotification": {
    	    "notificationActions": [
    	      {
    	        "action": {
    	          "lambdaAction": {
    	            "functionArn": "`alarmNotificationFunctionArn`"
    	          }
    	        },
    	        "smsConfigurations": [
    	          {
    	            "recipients": [
    	              {
    	                "ssoIdentity": {
    	                  "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
    	                  "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
    	                }
    	              }
    	            ],
    	            "senderId": "$sitewise.assetModel.``assetModelId``.``senderIdAttributeId``.propertyValue.value",
    	            "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
    	          }
    	        ],
    	        **"emailConfigurations": [
    	 {
    	 "from": "$sitewise.assetModel.``assetModelId``.``fromAddressAttributeId``.propertyValue.value",
    	 "recipients": {
    	 "to": [
    	 {
    	 "ssoIdentity": {
    	 "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
    	 "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
    	 }
    	 }
    	 ]
    	 },
    	 "content": {
    	 "subject": "$sitewise.assetModel.``assetModelId``.``emailSubjectAttributeId``.propertyValue.value",
    	 "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
    	 }
    	 }
    	 ]**
    	      }
    	    ]
    	  }
    	}
    	```
    7. (Optional) Add the alarm capabilities (`alarmCapabilities`) to
     the payload in `alarm-model-payload.json`. In this object,
     you can specify if the acknowledge flow is enabled and the default enable state
     for assets based on the asset model. For more information about the acknowledge
     flow, see [Alarm states](industrial-alarms.md#alarm-states "industrial-alarms.md#alarm-states").



    ```
    {
      "alarmModelName": "`BoilerTemperatureHighAlarm`",
      "alarmModelDescription": "`Detects when the boiler temperature is high.`",
      "severity": `3`,
      "alarmRule": {
        "simpleRule": {
          "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
          "comparisonOperator": "`GREATER`",
          "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
        }
      },
      "alarmEventActions": {
        "alarmActions": [
          {
            "iotSiteWise": {
              "assetId": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.assetId",
              "propertyId": "'`alarmStatePropertyId`'"
            }
          }
        ]
      },
      "alarmNotification": {
        "notificationActions": [
          {
            "action": {
              "lambdaAction": {
                "functionArn": "`alarmNotificationFunctionArn`"
              }
            },
            "smsConfigurations": [
              {
                "recipients": [
                  {
                    "ssoIdentity": {
                      "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
                      "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
                    }
                  }
                ],
                "senderId": "$sitewise.assetModel.``assetModelId``.``senderIdAttributeId``.propertyValue.value",
                "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
              }
            ],
            "emailConfigurations": [
              {
                "from": "$sitewise.assetModel.``assetModelId``.``fromAddressAttributeId``.propertyValue.value",
                "recipients": {
                  "to": [
                    {
                      "ssoIdentity": {
                        "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
                        "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
                      }
                    }
                  ]
                },
                "content": {
                  "subject": "$sitewise.assetModel.``assetModelId``.``emailSubjectAttributeId``.propertyValue.value",
                  "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
                }
              }
            ]
          }
        ]
      },
      **"alarmCapabilities": {
     "initializationConfiguration": {
     "disabledOnInitialization": `false`
     },
     "acknowledgeFlow": {
     "enabled": `true`
     }
     }**
    }
    ```
    8. Add the IAM service role (`roleArn`) that AWS IoT Events can assume to
     send data to AWS IoT SiteWise. This role requires the
     `iotsitewise:BatchPutAssetPropertyValue` permission and a trust
     relationship that allows `iotevents.amazonaws.com` to assume the role.
     To send notifications, this role also requires the
     `lambda:InvokeFunction` and `sso-directory:DescribeUser`
     permissions. For more information, see [Alarm service
     roles](../../../iotevents/latest/developerguide/security-iam.md "../../../iotevents/latest/developerguide/security-iam.md") in the *AWS IoT Events Developer Guide*.




    	* Replace the `roleArn` with the ARN of the role that AWS IoT Events can
    	 assume to perform these actions.

    ```
    {
      "alarmModelName": "`BoilerTemperatureHighAlarm`",
      "alarmModelDescription": "`Detects when the boiler temperature is high.`",
      "severity": `3`,
      "alarmRule": {
        "simpleRule": {
          "inputProperty": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.propertyValue.value",
          "comparisonOperator": "`GREATER`",
          "threshold": "$sitewise.assetModel.``assetModelId``.``thresholdAttributeId``.propertyValue.value"
        }
      },
      "alarmEventActions": {
        "alarmActions": [
          {
            "iotSiteWise": {
              "assetId": "$sitewise.assetModel.``assetModelId``.``alarmPropertyId``.assetId",
              "propertyId": "'`alarmStatePropertyId`'"
            }
          }
        ]
      },
      "alarmNotification": {
        "notificationActions": [
          {
            "action": {
              "lambdaAction": {
                "functionArn": "`alarmNotificationFunctionArn`"
              }
            },
            "smsConfigurations": [
              {
                "recipients": [
                  {
                    "ssoIdentity": {
                      "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
                      "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
                    }
                  }
                ],
                "senderId": "$sitewise.assetModel.``assetModelId``.``senderIdAttributeId``.propertyValue.value",
                "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
              }
            ],
            "emailConfigurations": [
              {
                "from": "$sitewise.assetModel.``assetModelId``.``fromAddressAttributeId``.propertyValue.value",
                "recipients": {
                  "to": [
                    {
                      "ssoIdentity": {
                        "identityStoreId": "$sitewise.assetModel.``assetModelId``.``identityStoreIdAttributeId``.propertyValue.value",
                        "userId": "$sitewise.assetModel.``assetModelId``.``userIdAttributeId``.propertyValue.value"
                      }
                    }
                  ]
                },
                "content": {
                  "subject": "$sitewise.assetModel.``assetModelId``.``emailSubjectAttributeId``.propertyValue.value",
                  "additionalMessage": "$sitewise.assetModel.``assetModelId``.``additionalMessageAttributeId``.propertyValue.value"
                }
              }
            ]
          }
        ]
      },
      "alarmCapabilities": {
        "initializationConfiguration": {
          "disabledOnInitialization": `false`
        },
        "acknowledgeFlow": {
          "enabled": `false`
        }
      },
      "roleArn": "arn:aws:iam::`123456789012`:role/`MyIoTEventsAlarmRole`"
    }
    ```
    9. Run the following command to create the AWS IoT Events alarm model from the
     payload in `alarm-model-payload.json`.



    ```
    aws iotevents create-alarm-model --cli-input-json file://alarm-model-payload.json
    ```
    10. The operation returns a response that includes the ARN of the alarm
     model, `alarmModelArn`. Copy this ARN to set in the alarm definition
     on your asset model in the next step.

### Step 3: Enable data flow between

AWS IoT SiteWise and AWS IoT Events

After you create the required resources in AWS IoT SiteWise and AWS IoT Events, you can enable data
flow between the resources to enable your alarm. In this section, you update the alarm definition
in the asset model to use the alarm model that you created in the previous step.

###### To enable data flow between AWS IoT SiteWise and AWS IoT Events (CLI)

- Set the alarm model as the alarm's source in the asset model. Do the
  following:
  1.  Run the following command to retrieve the existing asset model definition.
      Replace `asset-model-id` with the ID of the asset
      model.

  ```
  aws iotsitewise describe-asset-model --asset-model-id `asset-model-id`
  ```

  The operation returns a response that contains the asset model's
  details. 2. Create a file called `update-asset-model-payload.json` and
  copy the previous command's response into the file. 3. Remove the following key-value pairs from the
  `update-asset-model-payload.json` file:

      + `assetModelId`
      + `assetModelArn`
      + `assetModelCreationDate`
      + `assetModelLastUpdateDate`
      + `assetModelStatus`

  4.  Add the alarm source property (`AWS/ALARM_SOURCE`) to the alarm
      composite model that you defined earlier. Replace
      `alarmModelArn` with the ARN of the alarm
      model, which sets the value of the alarm source property.

  ```
  {
    `...`
    "assetModelCompositeModels": [
      `...`
      {
        "name": "BoilerTemperatureHighAlarm",
        "type": "AWS/ALARM",
        "properties": [
          {
            "id": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "name": "AWS/ALARM_TYPE",
            "dataType": "STRING",
            "type": {
              "attribute": {
                "defaultValue": "IOT_EVENTS"
              }
            }
          },
          {
            "id": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
            "name": "AWS/ALARM_STATE",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/ALARM_STATE",
            "type": {
              "measurement": {}
            }
          },
          **{
   "name": "AWS/ALARM\_SOURCE",
   "dataType": "STRING",
   "type": {
   "attribute": {
   "defaultValue": "`alarmModelArn`"
   }
   }
   }**
        ]
      }
    ]
  }
  ```

  5.  Run the following command to update the asset model with the definition
      stored in the `update-asset-model-payload.json` file. Replace
      `asset-model-id` with the ID of the asset
      model.

  ```
  aws iotsitewise update-asset-model \
    --asset-model-id `asset-model-id` \
    --cli-input-json file://update-asset-model-payload.json
  ```

Your asset model now defines an alarm that detects in AWS IoT Events. The alarm monitors the
target property in all assets based on this asset model. You can configure the alarm on
each asset to customize properties such as the threshold or IAM Identity Center recipient for each
asset. For more information, see [Configure alarms on assets in AWS IoT SiteWise](configure-alarms.md "configure-alarms.md").
