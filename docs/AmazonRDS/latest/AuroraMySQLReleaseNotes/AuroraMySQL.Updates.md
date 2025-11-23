# Aurora MySQL database engine updates

2020-03-05 (version 1.19.6) (Deprecated)

**Version:** 1.19.6

Aurora MySQL 1.19.6 is generally available. Aurora MySQL 1.\* versions are compatible with MySQL 5.6
and Aurora MySQL 2.\* versions are compatible with MySQL 5.7.

This engine version is scheduled to be deprecated on February 28, 2023. For more information, see
[Preparing for Amazon Aurora MySQL-Compatible Edition version 1 end of life](../AuroraUserGuide/Aurora.MySQL56.md "../AuroraUserGuide/Aurora.MySQL56.md").

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can restore the snapshot of an Aurora MySQL 1.\* database into Aurora MySQL 1.19.6.

To create a cluster with an older version of Aurora MySQL, please specify the engine version through the
RDS Console, the AWS CLI, or the Amazon RDS API.

###### Note

This version is currently not available in the following regions:
AWS GovCloud (US-East) [us-gov-east-1],
AWS GovCloud (US-West) [us-gov-west-1].
There will be a separate announcement once it is made available.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.md "../AuroraUserGuide/USER_UpgradeDBInstance.md") in the _Amazon Aurora User Guide_.

## Improvements

**High priority fixes:**

- Fixed an issue of intermittent connection failures after certificate rotation.
