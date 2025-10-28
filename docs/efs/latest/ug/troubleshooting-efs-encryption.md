# Troubleshooting encryption

###### Following, you can find information about troubleshooting encryption

issues for Amazon EFS.

- [Mounting with encryption of data in transit
  fails](#mounting-tls-fails "#mounting-tls-fails")
- [Mounting with encryption of data in transit
  is interrupted](#mounting-tls-interrupt "#mounting-tls-interrupt")
- [Encrypted-at-rest file system can't be
  created](#unable-to-encrypt "#unable-to-encrypt")
- [Unusable encrypted file system](#unusable-encrypt "#unusable-encrypt")

## Mounting with encryption of data in transit

fails

By default, when you use the Amazon EFS mount helper with Transport Layer Security
(TLS), it enforces hostname checking. Some systems don't support this feature,
such as when you use Red Hat Enterprise Linux or CentOS. In these cases, mounting an
EFS file system using TLS fails.

###### Action to take

We recommend that you upgrade the version of stunnel on your client to
support hostname checking. For more information, see [Upgrading stunnel](upgrading-stunnel.md "upgrading-stunnel.md").

## Mounting with encryption of data in transit

is interrupted

It's possible, however unlikely, that your encrypted connection to your Amazon EFS file
system can hang or be interrupted by client-side events.

###### Action to take

If your connection to your Amazon EFS file system with encryption of data in
transit is interrupted, take the following steps:

1. Ensure that the stunnel service is running on the client.
2. Confirm that the watchdog application
   `amazon-efs-mount-watchdog` is running on the client. You can
   find out whether this application is running with the following
   command:

```
ps aux | grep [a]mazon-efs-mount-watchdog
```

3. Check your support logs. For more information, see [Getting support logs](mount-helper-logs.md "mount-helper-logs.md").
4. Optionally, you can enable your stunnel logs and check the information in
   those as well. You can change the configuration of your logs in
   `/etc/amazon/efs/efs-utils.conf` to enable the stunnel
   logs. However, doing so requires unmounting and then remounting the file
   system with the mount helper for the changes to take effect.

###### Important

Enabling the stunnel logs can use up a nontrivial amount of space on
your file system.

If the interruptions continue, contact AWS Support.

## Encrypted-at-rest file system can't be

created

You've tried to create a new encrypted-at-rest file system. However, you get an
error message saying that AWS KMS is unavailable.

###### Action to take

This error can occur in the rare case that AWS KMS becomes temporarily
unavailable in your AWS Region. If this happens, wait until AWS KMS returns to
full availability, and then try again to create the file system.

## Unusable encrypted file system

An encrypted file system consistently returns NFS server errors. These errors can
occur when EFS can't retrieve your master key from AWS KMS for one of the following
reasons:

- The key was disabled.
- The key was deleted.
- Permission for Amazon EFS to use the key was revoked.
- AWS KMS is temporarily unavailable.

###### Action to take

First, confirm that the AWS KMS key is enabled. You can do so by viewing the
keys in the console. For more information, see [Viewing Keys](../../../kms/latest/developerguide/viewing-keys.md "../../../kms/latest/developerguide/viewing-keys.md") in the
_AWS Key Management Service Developer Guide_.

If the key is not enabled, enable it. For more information, see [Enabling and Disabling Keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") in the
_AWS Key Management Service Developer Guide_.

If the key is pending deletion, then this status disables the key. You can cancel
the deletion, and re-enable the key. For more information, see [Scheduling and Canceling Key Deletion](../../../kms/latest/developerguide/deleting-keys.md#deleting-keys-scheduling-key-deletion "../../../kms/latest/developerguide/deleting-keys.md#deleting-keys-scheduling-key-deletion") in the
_AWS Key Management Service Developer Guide_.

If the key is enabled, and you're still experiencing an issue, or if you encounter
an issue re-enabling your key, contact AWS Support.
