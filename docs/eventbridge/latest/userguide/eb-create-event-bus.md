# Creating an event bus in Amazon EventBridge

You can create a custom [event bus](eb-event-bus.md "eb-event-bus.md") to receive [events](eb-events.md "eb-events.md") from your applications. Your applications can also
send events to the default event bus. When you create an event bus, you can attach a [resource-based policy](eb-use-resource-based.md "eb-use-resource-based.md") to grant permissions to
other accounts. Then other accounts can send events to the event bus in the current
account.

The following video goes through creating event
buses:

###### To create a custom event bus

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Event buses**.
3. Choose **Create event bus**.
4. Enter a name for the new event bus.
5. Choose the KMS key for EventBridge to use when encrypting the
   event data stored on the event bus.

###### Note

Schema discovery is not supported for event buses encrypted
using a customer managed key. To enable schema discovery on an
event bus, choose to use an AWS owned key. For more information, see [KMS key options](eb-encryption-at-rest-key-options.md "eb-encryption-at-rest-key-options.md").

    * Choose **Use AWS owned key** for EventBridge to encrypt the data using an AWS owned key.


    This AWS owned key is a KMS key that EventBridge owns and manages for use in multiple AWS
     accounts. In general, unless you are required to audit or control the
     encryption key that protects your resources, an AWS owned key
     is a good choice.


    This is the default.
    * Choose **Use customer managed key** for EventBridge to encrypt the data using the customer managed key that you
     specify or create.


    Customer managed keys are KMS keys in your AWS account that you create, own, and manage. You have full
     control over these KMS keys.


    	1. Specify an existing customer managed key, or choose
    	 **Create a new KMS key**.


    	EventBridge displays the key status and any key aliases that
    	 have been associated with the specified customer managed key.
    	2. Choose the Amazon SQS queue to use as the dead-letter queue (DLQ) for
    	 this event bus, if any.


    	EventBridge sends events that aren't successfully encrypted
    	 to the DLQ, if configured, so you can process them later.

6. (Optional) Under **Logs - optional**, you can set up how EventBridge logs event information, including how to configure those logs.

For more information about event bus logs, see [Logging event buses](eb-event-bus-logs.md "eb-event-bus-logs.md") .

CloudWatch logs is selected as a log destination by default, as is the
`ERROR` log level. So, by default, EventBridge creates a new
CloudWatch log group to which it sends log records containing the
`ERROR` level of detail.

To have EventBridge send log records to any of the supported log
destinations, do the following:

    1. Under **Logs - optional**, choose the destinations to
     which you want log records delivered.
    2. For **Log level**, choose the level of information
     for EventBridge to include in log records. The `ERROR`
     log level is selected by default.


    For more information, see [Specifying log level](eb-event-bus-logs.md#eb-event-bus-logs-level "eb-event-bus-logs.md#eb-event-bus-logs-level").
    3. Select **Include detail data** if you want EventBridge to include event and target information in log records.


    For more information, see [Including details in
     logs](eb-event-bus-logs.md#eb-event-logs-data "eb-event-bus-logs.md#eb-event-logs-data").
    4. Configure each log destination you selected.

7.  Configure optional event bus features:
    - Specify a resource-based policy by doing one of the following:

          + Enter the policy that includes the permissions to grant for the event bus.
           You can paste in a policy from another source or enter the JSON for the
           policy. You can use one of the [example policies](eb-event-bus-perms.md "eb-event-bus-perms.md") and modify it for your
           environment.
          + To use a template for the policy, choose **Load template**. Modify the policy as
           appropriate for your environment, including adding additional actions that you authorize the principal in
           the policy to use.

      For more information about granting permissions to an event bus through resource-based policies, see [Permissions for event buses in Amazon EventBridge](eb-event-bus-perms.md "eb-event-bus-perms.md").

    - Enable an archive (optional)

    You can create an archive of events so that you can easily replay them at
    a later time. For example, you might want to replay events to recover from
    errors or to validate new functionality in your application. For more
    information, see [Archiving and replaying events in Amazon EventBridge](eb-archive.md "eb-archive.md")

        1. Under **Archives**, choose
         **Enabled**.
        2. Specify a name and description for the archive.


        You can't change the archive name once it has been created.


        When creating an archive as part of creating a new event bus, you can't set the event retention period or an event pattern for the archive.
         You can specify these for the archive once it has been created. For more information, see [Updating
         archives](event-bus-update-archive.md "event-bus-update-archive.md").

    - Enable schema discovery (optional)

    Enable schema discovery to have EventBridge
    automatically infer schemas directly from events running on this event bus. For more information, see [Amazon EventBridge schemas](eb-schema.md "eb-schema.md")

        1. Under **Schema discovery**, choose
         **Enabled**.

    ###### Note

    Schema discovery is not supported for event buses encrypted
    using a customer managed key. To enable schema discovery on an
    event bus, choose to use an AWS owned key. For more information, see [KMS key options](eb-encryption-at-rest-key-options.md "eb-encryption-at-rest-key-options.md").
    - Specify tags (optional)

    A tag is a custom attribute label that you assign to an AWS resource. Use tags to identify and organize your AWS resources.
    Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For more information, see [Tagging resources in Amazon EventBridge](eb-tagging.md "eb-tagging.md")

        1. Under **Tags**, choose **Add new tag**.
        2. Specify a key and, optionally, a value for the new tag.

8.  Choose **Create**.
