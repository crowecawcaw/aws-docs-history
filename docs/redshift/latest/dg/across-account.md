Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sharing data across AWS accounts

You can share data for read purposes across AWS accounts. Sharing data across
AWS accounts works similarly to sharing data within an account. The difference is
that there is a two-way handshake required in sharing data across AWS accounts. A
producer account administrators can either authorize consumer accounts to access
datashares or choose not to authorize any access. To use an authorized datashare, a
consumer account administrator can associate the datashare. The administrator can
associate the datashare with an entire AWS account or with specific clusters in the
consumer account, or decline the datashare. For more information about sharing data
within an account, see [Sharing read access to data within an
AWS account](within-account.md "within-account.md").

A datashare can have data consumers that are either namespaces in the same account
or different AWS accounts. You don't need to create separate datashares for
sharing within an account and cross-account sharing.

For cross-account data sharing, both the producer and consumer cluster must be
encrypted.

When sharing data with AWS accounts, producer administrators share with the
AWS account as an entity. A consumer administrator can decide which namespaces in
the consumer account get access to a datashare.

###### Topics

- [producer administrator actions](producer-cluster-admin.md "producer-cluster-admin.md")
- [Consumer account administrator
  actions](consumer-account-admin.md "consumer-account-admin.md")
- [consumer administrator actions](consumer-cluster-admin.md "consumer-cluster-admin.md")
