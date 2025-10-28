# Updating archives on Amazon EventBridge event

buses

You can update the following:

- Archive description
- The event pattern used to filter which events are sent to the archive.
- The retention period for events.
- The AWS KMS key used for event encryption.

For more information, see [Encrypting archives](encryption-archives.md "encryption-archives.md").
You cannot change the name or source event bus for an archive once it has been created.

###### Note

Schema discovery is not supported for event buses encrypted
using a customer managed key. To enable schema discovery on an
event bus, choose to use an AWS owned key. For more information, see [KMS key options](eb-encryption-at-rest-key-options.md "eb-encryption-at-rest-key-options.md").

###### To update an archive (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Navigate to the archive directly, or from the source event bus:
   - In the navigation pane, choose **Event buses**.

   On the events bus details page, choose the **Archives**
   tab.
   - In the navigation pane, choose **Archives**.

3. Select the archive, and then select **Edit**.
4. Update the archive.

###### To update an archive for an event bus (AWS CLI)

- Use [update-archive](../../../cli/latest/reference/events/update-archive.md "../../../cli/latest/reference/events/update-archive.md").
