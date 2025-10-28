End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Send inputs to test the detector model in AWS IoT Events

There are several ways to receive telemetry data in AWS IoT Events (see [Supported actions to receive data and trigger
actions in AWS IoT Events](iotevents-supported-actions.md "iotevents-supported-actions.md")). This
topic shows you how to create an AWS IoT rule in the AWS IoT console that forwards messages as
inputs to your AWS IoT Events detector. You can use the AWS IoT console's MQTT client to send test
messages. You can use this method to get telemetry data into AWS IoT Events when your devices are able
to send MQTT messages using the AWS IoT message broker.

###### To send inputs to test the detector model

1.  Open the [AWS IoT Core console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/"). In the left
    navigation pane, under **Manage**, choose **Message
    routing**, then choose **Rules**.
2.  Choose **Create rule** in the upper right.
3.  On the **Create a rule** page, complete the following steps:
    1.  **Step 1. Specify rule properties**. Complete the following
        fields:
        - **Rule name.** Enter a name for your rule, such as
          `MyIoTEventsRule`.

        ###### Note

        Do not use spaces.
        - **Rule description**. This is optional.
        - Choose **Next**.

    2.  **Step 2. Configure SQL statement**. Complete the following
        fields:

            * **SQL version**. Select the appropriate option from the
             list.
            * **SQL statement**. Enter `SELECT *, topic(2) as
             motorid FROM 'motors/+/status'`.

        Choose **Next**.

    3.  **Step 3. Attach rule actions**. In the **Rule
        actions** section, complete the following:
        - **Action 1. Select IoT Events.** The following fields
          appear:

              1. **Input name**. Select the appropriate option from the
               list. If your input doesn't appear, choose
               **Refresh**.


              To create a new input, choose **Create IoT Events
               input**. Complete the following fields:




              	+ **Input name**. Enter
              	 `PressureInput`.
              	+ **Description**. This is optional.
              	+ **Upload a JSON file**. Upload a copy of your JSON
              	 file. There is a link to a sample file on this screen, if you don't have a
              	 file. The code includes:



              	```
              	{
              	  "motorid": "Fulton-A32",
              	  "sensorData": {
              	    "pressure": 23,
              	    "temperature": 47
              	  }
              	}

              	```
              	+ **Choose input attributes**. Select the appropriate
              	 option(s).
              	+ **Tags**. This is optional.
              Choose **Create**.


              Return to the **Create rule** screen and refresh the
               **Input name** field. Select the input you just
               created.
              2. **Batch mode**. This is optional. If the payload is an
               array of messages, select this option.
              3. **Message ID**. This is optional, but recommended.
              4. **IAM role**. Select the appropriate role from the list.
               If the role isn't listed, choose **Create new role**.


              Type a **Role name** and choose
               **Create**.

          To add another rule, choose **Add rule action**

        - **Error action**. This section is optional. To add an action,
          choose **Add error action** and select the appropriate action
          from the list.

        Complete the fields that appear.
        - Choose **Next**.

    4.  **Step 4. Review and create.** Review the information on the
        screen and choose **Create**.

4.  In the left navigation pane, under **Test**, choose **MQTT
    test client**.
5.  Choose **Publish to a topic**. Complete the following fields:
    - **Topic name**. Enter a name to identify the message, such as
      `motors/Fulton-A32/status`.
    - **Message payload**. Enter the following:

    ```
    {
      "messageId": 100,
      "sensorData": {
        "pressure": 39
      }
    }
    ```

    ###### Note

    Change the `messageId` each time you publish a new message.

6.  For **Publish**, keep the topic the same, but change the
    `"pressure"` in the payload to a value greater than the threshold value that
    you specified in the detector model (such as `85`).
7.  Choose **Publish**.
    The detector instance that you created generates and sends you an Amazon SNS message. Continue
    to send messages with pressure readings above or below the pressure threshold (70 for this
    example) to see the detector in operation.

In this example, you must send three messages with pressure readings below the threshold
to transition back to the **Normal** state and receive an Amazon SNS message that
indicates the overpressure condition has cleared. Once back in the **Normal**
state, one message with a pressure reading above the limit causes the detector to enter the
**Dangerous** state and send an Amazon SNS message indicating that
condition.

Now that you have created a simple input and detector model, try the following.

- See more detector model examples (templates) on the console.
- Follow the steps in [Create an AWS IoT Events detector for two states using CLI](iotevents-simple-example.md "iotevents-simple-example.md") to create an input and detector model using
  the AWS CLI
- Learn details of the [Expressions to filter, transform, and process event
  data](iotevents-expressions.md "iotevents-expressions.md") used in events.
- Learn about [Supported actions to receive data and trigger
  actions in AWS IoT Events](iotevents-supported-actions.md "iotevents-supported-actions.md").
- If something isn't working, see [Troubleshooting AWS IoT Events](iotevents-troubleshooting.md "iotevents-troubleshooting.md").
