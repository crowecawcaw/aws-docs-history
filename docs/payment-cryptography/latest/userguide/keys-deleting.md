# Deleting keys

Deleting an AWS Payment Cryptography key deletes the key material and all metadata associated with the key
and is irreversible unless a copy of the key is available outside of AWS Payment Cryptography. After a key is
deleted, you can no longer decrypt the data that was encrypted under that key, which means that
data may become unrecoverable. You should delete a key only when you are sure that you don't
need to use it anymore and no other parties are utilizing this key. If you are not sure,
consider stopping key usage instead of deleting it. You can re-enable a disabled key if you need
to use it again later, but you cannot recover a deleted AWS Payment Cryptography key unless you are able to
re-import it from another source.

Before deleting a key, you should ensure that you no longer need the key. AWS Payment Cryptography does not
store the results of cryptographic operations like CVV2 and is unable to determine if a key is
needed for any persistent cryptographic material.

AWS Payment Cryptography never deletes keys belonging to active AWS accounts unless you explicitly
schedule them for deletion and the mandatory waiting period expires.

However, you might choose to delete an AWS Payment Cryptography key for one or more of the following
reasons:

- To complete the key lifecycle for a key that you no longer need
- To avoid the management overhead associated with maintaining unused AWS Payment Cryptography
  keys

###### Note

If you [close or delete your
AWS account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md"), your AWS Payment Cryptography key become inaccessible. You do not need to schedule
deletion of your AWS Payment Cryptography key separate from closing the account.

AWS Payment Cryptography records an entry in your [AWS CloudTrail](https://console.aws.amazon.com/cloudtrail "https://console.aws.amazon.com/cloudtrail")
log when you schedule deletion of the AWS Payment Cryptography key and when the AWS Payment Cryptography key is actually
deleted.

When using Multi-Region key replication, deleting an Payment Cryptography key that is an Primary Region key (PRK), the Replica Region keys (RRK)
will also be automatically deleted. A RRK cannot be deleted like a PRK. If you want to
delete a RRK, you'll need to [modify the
replication regions for your PRK](keys-multi-region-replication.md#disabling-mrr "keys-multi-region-replication.md#disabling-mrr").

## About the waiting period

Because deleting a key is irreversible, AWS Payment Cryptography requires you to set a waiting period of
between 3–180 days. The default waiting period is seven days.

However, the actual waiting period might be up to 24 hours longer than the one you
scheduled. To get the actual date and time when the AWS Payment Cryptography key will be deleted, use the
GetKey operations. Be sure to note the time zone.

During the waiting period, the AWS Payment Cryptography key status and key state is **Pending
deletion**.

###### Note

An AWS Payment Cryptography key pending deletion cannot be used in any [cryptographic operations](data-operations.md "data-operations.md").

After the waiting period ends, AWS Payment Cryptography deletes the AWS Payment Cryptography key, its aliases, and all
related AWS Payment Cryptography metadata.

Use the waiting period to ensure that you don't need the AWS Payment Cryptography key now or in the
future. If you find that you do need the key during the waiting period, you can cancel key
deletion before the waiting period ends. After the waiting period ends, you cannot cancel key
deletion, and the service deletes the key.

###### Examples

In this example, a key is requested to be deleted. Besides the basic key information,
two relevant fields are that key state has been changed to DELETE_PENDING and
deletePendingTimestamp represents when the key is currently scheduled to delete.

```
`$` `aws payment-cryptography delete-key \
 --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`

```

```

`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h",
 "KeyAttributes": {
 "KeyUsage": "TR31_V2_VISA_PIN_VERIFICATION_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "TDES_3KEY",
 "KeyModesOfUse": {
 "Encrypt": false,
 "Decrypt": false,
 "Wrap": false,
 "Unwrap": false,
 "Generate": true,
 "Sign": false,
 "Verify": true,
 "DeriveKey": false,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "0A3674",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "Enabled": false,
 "Exportable": true,
 "KeyState": "DELETE_PENDING",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2023-06-05T12:01:29.969000-07:00",
 "UsageStopTimestamp": "2023-06-05T14:31:13.399000-07:00",
 "DeletePendingTimestamp": "2023-06-12T14:58:32.865000-07:00"
 }
}`
```

In this example, a pending deletion is cancelled. Once completed successfully, a key
will no longer be deleted per the previous schedule. The response contains the basic key
information; additionally, two relevant fields have changed - `KeyState` and
`deletePendingTimestamp`. `KeyState` is returned to a value of
CREATE_COMPLETE, while `DeletePendingTimestamp` is removed.

```
`$` `aws payment-cryptography restore-key --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`

```

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h",
 "KeyAttributes": {
 "KeyUsage": "TR31_V2_VISA_PIN_VERIFICATION_KEY",
 "KeyClass": "SYMMETRIC_KEY",
 "KeyAlgorithm": "TDES_3KEY",
 "KeyModesOfUse": {
 "Encrypt": false,
 "Decrypt": false,
 "Wrap": false,
 "Unwrap": false,
 "Generate": true,
 "Sign": false,
 "Verify": true,
 "DeriveKey": false,
 "NoRestrictions": false
 }
 },
 "KeyCheckValue": "0A3674",
 "KeyCheckValueAlgorithm": "ANSI_X9_24",
 "Enabled": false,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
 "CreateTimestamp": "2023-06-08T12:01:29.969000-07:00",
 "UsageStopTimestamp": "2023-06-08T14:31:13.399000-07:00"
 }
}`
```
