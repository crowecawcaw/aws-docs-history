# Find KMS keys and key material in an AWS CloudHSM key

store

If you manage an AWS CloudHSM key store, you might need to identify the KMS keys in each AWS CloudHSM
key store. For example, you might need to do some of the following tasks.

- Track the KMS keys in AWS CloudHSM key store in AWS CloudTrail logs.
- Predict the effect on KMS keys of disconnecting an AWS CloudHSM key store.
- Schedule deletion of KMS keys before you delete an AWS CloudHSM key store.
  In addition, you might want to identify the keys in your AWS CloudHSM cluster that serve as key
  material for your KMS keys. Although AWS KMS manages the KMS keys and the key material, you
  still retain control of and responsibility for the management of your AWS CloudHSM cluster, as well as
  the HSMs and backups and the keys in the HSMs. You might need to identify the keys in order to
  audit the key material, protect it from accidental deletion, or delete it from HSMs and cluster
  backups after deleting the KMS key.

All key material for the KMS keys in your AWS CloudHSM key store is owned by the [kmsuser crypto user](keystore-cloudhsm.md#concept-kmsuser "keystore-cloudhsm.md#concept-kmsuser") (CU). AWS KMS sets the key
label attribute, which is viewable only in AWS CloudHSM, to the Amazon Resource Name (ARN) of the
KMS key.

To find KMS keys and key material, use any of the following techniques.

- [Find the KMS keys in an AWS CloudHSM key store](find-cmk-in-keystore.md "find-cmk-in-keystore.md") — How
  to identify the KMS keys in one or all of your AWS CloudHSM key stores.
- [Find all keys for an AWS CloudHSM key store](find-all-kmsuser-keys.md "find-all-kmsuser-keys.md") —
  How to find all keys in your cluster that serve as key material for the KMS keys in your
  AWS CloudHSM key store.
- [Find the AWS CloudHSM key for a KMS key](find-handle-for-cmk-id.md "find-handle-for-cmk-id.md") —
  How to find the key in your cluster that serves as key material for a particular KMS key
  in your AWS CloudHSM key store.
- [Find the KMS key for an AWS CloudHSM key](find-label-for-key-handle.md "find-label-for-key-handle.md")
  — How to find the KMS key for a particular key in your cluster.
