# Configuring encryption in EventBridge Pipes

You can specify the KMS key for EventBridge to use when you create or update a pipe.

## Specifying the AWS KMS key used for encryption when creating a pipe

Choosing the AWS KMS key used for encryption is an option creating a
pipe. The default is to use the AWS owned key provided by
EventBridge.

###### To specify a customer managed key for encryption when creating a

pipe (console)

- Follow these instructions:

[Creating a pipe](eb-pipes-create.md "eb-pipes-create.md").

###### To specify a customer managed key for encryption when creating a pipe (CLI)

- When calling `create-pipe`, use the
  `kms-key-identifier` option to specify the customer managed key for EventBridge to use for encryption on the event
  bus.

## Updating the AWS KMS key used for encryption on EventBridge Pipes

You can update the AWS KMS key being used for encryption at rest on
an existing pipe. This includes:

- Changing from the default AWS owned key to a customer managed key.
- Changing from a customer managed key to the default AWS owned key.
- Changing from one customer managed key to another.

When you update a pipe to use a different AWS KMS key, EventBridge
decrypts any data stored on the pipe and then encrypts it using the new
key.

###### To update the KMS key used for encryption on a pipe

(console)

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  In the navigation pane, choose **Pipes**.
3.  Choose the pipe you want to update.
4.  On the pipe bus details page, choose the
    **Encryption** tab.
5.  Choose the KMS key for EventBridge to use when
    encrypting the data stored on pipe:
    - Choose **Use AWS owned key**
      for EventBridge to encrypt the data using an AWS owned key.

    This AWS owned key is a KMS key
    that EventBridge owns and manages for use in multiple
    AWS accounts. In general, unless you are
    required to audit or control the encryption key that protects
    your resources, an AWS owned key is a good
    choice.

    This is the default.
    - Choose **Use customer managed key** for
      EventBridge to encrypt the data using the customer managed key that you specify or create.

    Customer managed keys are KMS keys in
    your AWS account that you create, own, and
    manage. You have full control over these KMS keys.

        1. Specify an existing customer managed key, or choose
         **Create a new KMS key**.


        EventBridge displays the key status and any key
         aliases that have been associated with the specified
         customer managed key.

###### To update the KMS key used for encryption on a pipe

(CLI)

- When calling `update-pipe`, use the
  `kms-key-identifier` option to specify the customer managed key for EventBridge to use for encrypting pipe
  data.
