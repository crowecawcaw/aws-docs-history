# Managing keys

To get started with AWS Payment Cryptography, create an AWS Payment Cryptography key.

This section explains how to create and manage various AWS Payment Cryptography key types throughout
their lifecycle. You'll learn how to create, view, and edit keys, as well as how to tag
keys, create key aliases, and enable or disable keys.

An AWS Payment Cryptography key is a regional resource. If you intend to use a given key in multiple
AWS Regions, you can enable Multi-Region key replication which securely copies key material and metadata to
AWS Regions you specify within the same AWS Partition and Account. The source key in
Multi-Region key replication is known as the [Primary Region key](terminology.md#term.prk "terminology.md#term.prk") (PRK) and this remains
the authoritative source for all key management activities. The replicated key is known as
the [Replica Region key](terminology.md#term.rrk "terminology.md#term.rrk")(RRK) and this is a read-only replica of the
PRK. You should consider using Multi-Region keys with your keys to meet design goals around
availability, disaster recovery, and low latency.

###### Topics

- [Creating keys](create-keys.md "create-keys.md")
- [Listing keys](keys-list.md "keys-list.md")
- [Enabling and disabling keys](keys-enable-disable.md "keys-enable-disable.md")
- [Replicating AWS Payment Cryptography keys](keys-multi-region-replication.md "keys-multi-region-replication.md")
- [Deleting keys](keys-deleting.md "keys-deleting.md")
- [Importing and exporting keys](keys-importexport.md "keys-importexport.md")
- [Using aliases](keys-managealias.md "keys-managealias.md")
- [Get keys](getkeys.md "getkeys.md")
- [Tagging keys](tagging-keys.md "tagging-keys.md")
- [Understanding key attributes for AWS Payment Cryptography key](keys-validattributes.md "keys-validattributes.md")
