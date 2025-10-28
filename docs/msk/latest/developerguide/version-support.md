# Amazon MSK version support

This topic describes the [Amazon MSK version support policy](#version-support-policy "#version-support-policy") and the procedure for [Upgrade the Apache Kafka version](version-upgrades.md "version-upgrades.md"). If you're upgrading your Kafka version, follow the best practices outlined in [Best practices for version upgrades](version-upgrades-best-practices.md "version-upgrades-best-practices.md").

###### Topics

- [Amazon MSK version support policy](#version-support-policy "#version-support-policy")
- [Upgrade the Apache Kafka version](version-upgrades.md "version-upgrades.md")
- [Best practices for version upgrades](version-upgrades-best-practices.md "version-upgrades-best-practices.md")

## Amazon MSK version support policy

This section describes the support policy for Amazon MSK supported Kafka versions.

- All Kafka versions are supported until they reach their end of support date. For details on end of support dates, see [Supported Apache Kafka versions](supported-kafka-versions.md "supported-kafka-versions.md"). Upgrade your MSK cluster to the recommended Kafka version or higher version before the end of support date. For details about upgrading your Apache Kafka version, see [Upgrade the Apache Kafka version](version-upgrades.md "version-upgrades.md"). A cluster using a Kafka version after its end of support date is auto-upgraded to the recommended Kafka version. Automatic upgrades can happen at any time after the end of support date. You will not receive any notification before the upgrade.
- MSK will phase out support for newly created clusters that use Kafka versions with published end of support dates.
