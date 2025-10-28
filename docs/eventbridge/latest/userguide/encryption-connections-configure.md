# Configuring encryption on

connections

You can specify the KMS key for EventBridge to use when you create or update a connection.

## Specifying AWS KMS keys when creating connections

Choosing the AWS KMS key used for encryption is optional when creating a
connection. By default, EventBridge uses an AWS owned key.

###### To specify a customer managed key for encryption when creating a connection

(console)

- Follow these instructions:

[Creating
connections](eb-target-connection-create.md "eb-target-connection-create.md").

###### To specify a customer managed key for encryption when creating a connection (CLI)

- When calling `create-connection`, use the `kms-key-identifier` option
  to specify the customer managed key for EventBridge to use for
  encryption of the connection's secret.

## Updating AWS KMS keys for

connections

You can update the KMS key being used for encrypting an existing connection. This
includes:

- Changing from the default AWS owned key to a customer managed key.
- Changing from a customer managed key to the default AWS owned key.
- Changing from one customer managed key to another.

When you update a connection to use a different KMS key , EventBridge decrypts the
connection's secret and then encrypts it using the new key. Make sure the
KMS key you specify has the necessary permissions. For more information, see [Connection key
policy](encryption-connections.md#encryption-connections-key-policy "encryption-connections.md#encryption-connections-key-policy").

###### To update the KMS key used for encryption on a connection

(console)

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  In the navigation pane, choose **Integration**, and then
    choose **Connections**.
3.  Choose the connection you want to update.
4.  On the connection details page, under **Encryption**, choose the KMS key for EventBridge to use when encrypting
    the connection's secret:
    - Choose **Use AWS owned key** for
      EventBridge to encrypt the secret using an AWS owned key.

    This AWS owned key is a KMS key
    that EventBridge owns and manages for use in multiple
    AWS accounts. In general, unless you are
    required to audit or control the encryption key that protects
    your resources, an AWS owned key is a good
    choice.

    This is the default.
    - Choose **Choose a different AWS KMS key (advanced)** for EventBridge to encrypt the secret using the customer managed key
      that you specify or create.

    Customer managed keys are KMS keys in
    your AWS account that you create, own, and
    manage. You have full control over these KMS keys.

        1. Specify an existing customer managed key, or choose
         **Create a new KMS key**.


        Make sure the KMS key you specify has the necessary
         permissions. For more information, see [Connection key
         policy](encryption-connections.md#encryption-connections-key-policy "encryption-connections.md#encryption-connections-key-policy").


        EventBridge displays the key status and any key
         aliases that have been associated with the specified
         customer managed key.

###### To update the KMS key used for encryption on a connection

(CLI)

- When calling `update-connection`, use the `kms-key-identifier` option
  to specify the customer managed key for EventBridge to use for
  encrypting the connection secret.
