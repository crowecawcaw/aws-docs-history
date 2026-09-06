

# Updating an event bus in Amazon EventBridge
<a name="event-bus-update"></a>

You can update the configuration of event buses after you create them. This includes the default event bus, which EventBridge creates in your account automatically.

**To update an event bus (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Event buses**.

1. Choose the event bus you want to update.

1. Do one or more of the following:
   + To create, edit, or delete an archive, see the following procedures:

     [Creating archives](eb-archive-event.md)

     [Updating archives](event-bus-update-archive.md)

     [Deleting archives](eb-archive-delete.md)
   + To add or remove tags, see the following procedure:

     [Managing event bus tags](eb-tagging.md#event-bus-update-tags)
   + To manage event bus permissions, see the following procedure:

     [Managing event bus permissions](eb-event-bus-permissions-manage.md)
   + To change the AWS KMS key used to encrypt events, see the following procedure:

     [Update encryption on an event bus](eb-encryption-event-bus-cmkey-configure.md#eb-encryption-event-bus-cmkey-update)