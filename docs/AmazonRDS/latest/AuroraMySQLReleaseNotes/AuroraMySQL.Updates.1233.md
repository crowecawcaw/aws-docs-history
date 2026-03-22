# Aurora MySQL database engine updates 2021-06-28 (version 1.23.3) (Deprecated)

**Version:** 1.23.3

Aurora MySQL 1.23.3 is generally available. Aurora MySQL 1.\* versions are compatible with MySQL 5.6
and Aurora MySQL 2.\* versions are compatible with MySQL 5.7.

This engine version is scheduled to be deprecated on February 28, 2023. For more information, see
[Preparing for Amazon Aurora MySQL-Compatible Edition version 1 end of life](../AuroraUserGuide/Aurora.MySQL56.EOL.md "../AuroraUserGuide/Aurora.MySQL56.EOL.md").

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

To create a cluster with an older version of Aurora MySQL, specify the engine version through the
RDS Console, the AWS CLI, or the Amazon RDS API.

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Improvements

General stability and availability enhancements.

**Security fixes:**

- [CVE-2021-23841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23841 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-23841")
- [CVE-2021-3449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3449 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3449")
- [CVE-2020-28196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28196 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28196")
