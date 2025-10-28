# Configuring encryption on EventBridge event buses

You can specify the KMS key for EventBridge to use when you create or update an
event bus. You can also update the default event bus to use a customer managed key as well.

## Specifying the AWS KMS key used for encryption when creating an event bus

Choosing the AWS KMS key used for encryption is part of creating an
event bus. The default is to use the AWS owned key provided by
EventBridge.

###### To specify a customer managed key for encryption when creating an event

bus (console)

- Follow these instructions:

[Creating an event bus](eb-create-event-bus.md "eb-create-event-bus.md").

###### To specify a customer managed key for encryption when creating an event

bus (CLI)

- When calling `create-event-bus`, use the
  `kms-key-identifier` option to specify the customer managed key for EventBridge to use for encryption on the event
  bus.

Optionally, use `dead-letter-config` to specify a dead-letter queue (DLQ).

## Updating the AWS KMS key used for encryption on an event bus

You can update the AWS KMS key being used for encryption at
rest on an existing event bus. This includes:

- Changing from the default AWS owned key to a customer managed key.
- Changing from a customer managed key to the default AWS owned key.
- Changing from one customer managed key to another.

When you update an event bus to use a different AWS KMS key,
EventBridge decrypts any data stored on the event bus and then encrypts it using the new
key.

###### To update the KMS key used for encryption on an event

bus (console)

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  In the navigation pane, choose **Event buses**.
3.  Choose the event bus you want to update.
4.  On the events bus details page, choose the **Encryption**
    tab.
5.  Choose the KMS key for EventBridge to use when
    encrypting the event data stored on the event bus:
    - Choose **Use AWS owned key** for
      EventBridge to encrypt the data using an AWS owned key.

    This AWS owned key is a KMS key that
    EventBridge owns and manages for use in multiple AWS accounts. In general, unless you are required to
    audit or control the encryption key that protects your resources, an
    AWS owned key is a good choice.

    This is the default.
    - Choose **Use customer managed key** for
      EventBridge to encrypt the data using the customer managed key that you specify or create.

    Customer managed keys are KMS keys in your
    AWS account that you create, own, and manage. You
    have full control over these KMS keys.

        1. Specify an existing customer managed key, or choose
         **Create a new KMS key**.


        EventBridge displays the key status and any key
         aliases that have been associated with the specified customer managed key.
        2. Choose the Amazon SQS queue to use as the dead-letter queue
         (DLQ) for this event bus, if any.


        EventBridge sends events that aren't successfully
         encrypted to the DLQ, if configured, so you can process them
         later.

###### To update the KMS key used for encryption on an event

bus (CLI)

- When calling `update-event-bus`, use the
  `kms-key-identifier` option to specify the customer managed key for EventBridge to use for encryption on the event
  bus.

Optionally, use `dead-letter-config` to specify a dead-letter queue (DLQ).

###### To update the KMS key used for encryption on the

default event bus, using CloudFormation

Because EventBridge provisions the default event bus into your account
automatically, you cannot create it using a CloudFormation template, as
you normally would for any resource you wanted to include in a CloudFormation stack. To include the default event bus in a CloudFormation stack, you must first _import_ it into a
stack. Once you have imported the default event bus into a stack, you can then
update the event bus properties as desired.

- Follow these instructions:

[Updating a default bus
using CloudFormation](event-bus-update-default-cfn.md "event-bus-update-default-cfn.md").
