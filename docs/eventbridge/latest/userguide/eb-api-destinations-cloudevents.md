# Sending CloudEvents events to API destinations

CloudEvents is a vendor-neutral specification for event formatting, with the goal of providing
interoperability across services, platforms and systems. You can use EventBridge to
transform AWS service events to CloudEvents before they are sent to a target, such
as an API destination.

###### Note

The following procedure explains how to transform source events into
_structured-mode_ CloudEvents. In the CloudEvents specification, a
structured-mode message is one where the entire event (attributes and data) is encoded
into the payload of the event.

For more information on the CloudEvents specification, see [cloudevents.io](https://cloudevents.io/ "https://cloudevents.io/").

###### To transform AWS events to the CloudEvents format using the console

To transform events to the CloudEvents format prior to delivery to a target, you start by creating an event bus rule. As part of defining the rule, you use an input transformer to have EventBridge transform events prior to sending to the target you specify.

1. Follow the steps in the [Creating rules in Amazon EventBridge](eb-create-rule-visual.md "eb-create-rule-visual.md") procedure.
2. In the [Select targets](eb-create-rule-wizard.md#eb-create-rule-target "eb-create-rule-wizard.md#eb-create-rule-target") step, when prompted to choose an API
   destination as the target type:
   1. Select **EventBridge API destination**.
   2. Do one of the following:
      - Choose **Use an existing API destination** and select an existing API destination
      - Choose **Create a new API destination** and specify the necessary setting to define your new API destination.

      For more information on specifying the required settings, see [Create an API destination in Amazon EventBridge](eb-api-destination-create.md "eb-api-destination-create.md").

   3. Specify the necessary Content-Type header parameters for the CloudEvents events:
      - Under **Header Parameters** choose **Add header parameter**.
      - For **key**, specify `Content-Type`.

      For **value**, specify `application/cloudevents+json; charset=UTF-8`.

3. Specify an execution role for your target.
4. Define an input transformer to transform the source event data into the CloudEvents format:
   1. Under **Additional settings**, for **Configure target input**, choose **Input transformer**.

   Then choose **Configure input transformer**. 2. Under **Target input transformer**, specify the **Input
   path**.

   In the input path below, the region attribute is a custom _extension
   attribute_ of the CloudEvents format. As such it is not required for adherence to the CloudEvents specification.

   CloudEvents allows you to use and create extension attributes not defined in the core specification. For more information,
   including a list of known extension attributes, see [CloudEvents Extension Attributes](https://github.com/cloudevents/spec/blob/main/cloudevents/documented-extensions.md "https://github.com/cloudevents/spec/blob/main/cloudevents/documented-extensions.md")
   in the [CloudEvents specification documentation](https://github.com/cloudevents/spec/tree/main "https://github.com/cloudevents/spec/tree/main") on GitHub.

   ```
   {
     "detail": "$.detail",
     "detail-type": "$.detail-type",
     "id": "$.id",
     "region": "$.region",
     "source": "$.source",
     "time": "$.time"
   }
   ```

   3. For **Template**, enter the template to transform the source event
      data to the CloudEvents format.

   In the template below, `region` is not strictly required, since the
   `region` attribute in the input path is an extension
   attribute to the CloudEvents specification.

   ```
   {
     "specversion":"1.0",
     "id":<id>,
     "source":<source>,
     "type":<detail-type>,
     "time":<time>,
     "region":<region>,
     "data":<detail>
   }
   ```

5. Complete creating the rule following the [procedure steps](eb-create-rule-visual.md "eb-create-rule-visual.md").
