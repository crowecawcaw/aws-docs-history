# Configuring encryption on

archives

You can specify the KMS key for EventBridge to use when you create or update an archive.

## Specifying encryption when creating an

archive

Choosing the AWS KMS key used for encryption is an option creating an
archive. The default is to use the AWS owned key provided by EventBridge.

###### To specify a customer managed key for encryption when creating an archive

(console)

- Follow these instructions:

[Creating archives](eb-archive-event.md "eb-archive-event.md").

###### To specify a customer managed key for encryption when creating an archive (CLI)

- When calling `create-archive`, use the
  `kms-key-identifier` option to specify the customer managed key for EventBridge to use for encrypting events stored in the archive.

## Updating encryption on archives

You can update the AWS KMS key being used for encryption at rest on an
existing archive. This includes:

- Changing from the default AWS owned key to a customer managed key.
- Changing from a customer managed key to the default AWS owned key.
- Changing from one customer managed key to another.

###### To update the KMS key used for encrypting events in an archive

(console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Navigate to the archive directly, or from the source event bus:
   - In the navigation pane, choose **Event buses**.

   On the events bus details page, choose the **Archives**
   tab.
   - In the navigation pane, choose **Archives**.

3. Choose the archive you want to update.
4. On the archive details page, choose the
   **Encryption** tab.
5. Choose the KMS key for EventBridge to use when
   encrypting the events stored in the archive.

###### Important

If you have specify that EventBridge use a customer managed key for encrypting the
source event bus, we strongly recommend you also specify a customer managed key
for any archives for the event bus as well.

    * Choose **Use AWS owned key**
     for EventBridge to encrypt the data using an AWS owned key.


    This AWS owned key is a KMS key
     that EventBridge owns and manages for use in multiple
     AWS accounts. In general, unless you are
     required to audit or control the encryption key that protects
     your resources, an AWS owned key is a good
     choice.


    This is the default.
    * Choose **Use customer managed key** for
     EventBridge to encrypt the data using the customer managed key that you specify or create.


    Customer managed keys are KMS keys in
     your AWS account that you create, own, and
     manage. You have full control over these KMS keys.


    	1. Specify an existing customer managed key, or choose
    	 **Create a new KMS key**.


    	EventBridge displays the key status and any key
    	 aliases that have been associated with the specified
    	 customer managed key.

###### To update the KMS key used for encrypting events stored in an archive

(CLI)

- When calling `update-archive`, use the
  `kms-key-identifier` option to specify the customer managed key for EventBridge to use for encrypting events stored in the archive.
