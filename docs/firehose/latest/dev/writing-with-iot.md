# Configure AWS IoT to send data to Firehose

You can configure AWS IoT to send information to a Firehose stream by adding an
action.

###### To create an action that sends events to an existing Firehose stream

1. When creating a rule in the AWS IoT console, on the **Create a
   rule** page, under **Set one or more actions**, choose
   **Add action**.
2. Choose **Send messages to an Amazon Kinesis Firehose stream**.
3. Choose **Configure action**.
4. For **Stream name**, choose an existing Firehose stream.
5. For **Separator**, choose a separator character to be inserted
   between records.
6. For **IAM role name**, choose an existing IAM role or choose
   **Create a new role**.
7. Choose **Add action**.
   For more information about creating AWS IoT rules, see [AWS IoT Rule Tutorials](../../../iot/latest/developerguide/iot-rules-tutorial.md "../../../iot/latest/developerguide/iot-rules-tutorial.md").
