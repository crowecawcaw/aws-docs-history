# Release calendars for Amazon Aurora MySQL

The release calendars on this page can help you plan your major and minor version upgrades. For more information on Amazon Aurora
upgrades, versioning, and lifecycle, see [Amazon Aurora versions](../AuroraUserGuide/Aurora.VersionPolicy.md "../AuroraUserGuide/Aurora.VersionPolicy.md").

###### Topics

- [Version Currency Timelines](#AuroraMySQL.release-calendars.version-currency "#AuroraMySQL.release-calendars.version-currency")
- [Release calendar for Aurora MySQL major versions](#AuroraMySQL.release-calendars.major "#AuroraMySQL.release-calendars.major")
- [Release calendar for Aurora MySQL minor versions](#AuroraMySQL.release-calendars.minor "#AuroraMySQL.release-calendars.minor")

## Version Currency Timelines

Amazon Aurora MySQL tracks community database engine releases on a defined cadence. These version currency timelines are published to give you
transparency into that cadence. You can use these timelines to:

- Plan major version upgrades and estimate when a new Aurora MySQL major version will be available.
- Schedule minor version upgrades during your maintenance windows.
- Select the right Aurora Long-Term Support (LTS) version for workloads that require staying on the same minor version across multiple release cycles.

The following table lists the version currency timelines for Aurora MySQL.

| Release Type                                                                                                                                  | Timelines                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Major versions                                                                                                                                | Within 12 months of the community's first minor for the new major version <major>.1 (Oracle MySQL LTS majors) |
| Minor versions                                                                                                                                | Within 3 months of the community release                                                                      |
| [Aurora LTS](../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md "../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md") (per major) | Within 12 months of the Aurora major version release                                                          |

## Release calendar for Aurora MySQL major versions

Aurora MySQL major versions are available under standard support at least until community end of life for the corresponding community version.
You can continue running a major version past its Aurora end of standard support date for a fee. For more information, see
[Using Amazon RDS Extended Support](../AuroraUserGuide/extended-support.md "../AuroraUserGuide/extended-support.md") and [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

Aurora MySQL currently supports the following major versions.

###### Note

You can also view information about support dates for major engine versions by
using
the AWS CLI or RDS API. For more information, see [Viewing support dates for engine versions in Amazon RDS Extended Support](../AuroraUserGuide/extended-support-viewing-support-dates.md "../AuroraUserGuide/extended-support-viewing-support-dates.md").

| Community major version | Aurora major version                | Community end of life date | Aurora end of standard support date | RDS start of Extended Support year 1 pricing date | RDS start of Extended Support year 3 pricing date | RDS end of Extended Support date | Minor versions eligible for RDS Extended Support |
| ----------------------- | ----------------------------------- | -------------------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------------------- | -------------------------------- | ------------------------------------------------ |
| MySQL 8.4               | Aurora MySQL version 8.4            | April 2032                 | April 2032                          | To be determined                                  | To be determined                                  | To be determined                 | To be determined                                 |
| MySQL 8.0               | Aurora MySQL version 3              | April 2026                 | 30 April 2028                       | 1 May 2028                                        | Not applicable                                    | 31 July 2029                     | To be determined                                 |
| MySQL 5.7               | Aurora MySQL version 2              | October 2023               | 31 October 2024                     | 1 December 2024                                   | Not applicable                                    | 30 June 2029                     | Aurora MySQL 2.11 and 2.12                       |
| MySQL 5.6 (deprecated)  | Aurora MySQL version 1 (deprecated) | 5 February 2021            | 28 February 2023                    | Not applicable                                    | Not applicable                                    | Not applicable                   | Not applicable                                   |

## Release calendar for Aurora MySQL minor versions

Aurora MySQL currently supports the following minor versions.

In general, Aurora minor versions are released quarterly. The release schedule might vary to pick up additional features or fixes.

Minor versions can reach end of standard support before corresponding major versions do. For example, version 3.07 will reach its
end of standard support date in August 2025, while major version 3 will reach its end of standard support on 30 April 2028.
Amazon RDS will support additional 3.\* minor versions released between these dates.

Amazon RDS Extended Support charges apply only to certain minor versions after a major version is eligible for Extended Support. For more information about major versions eligible for Extended Support, see [Release calendar for Aurora MySQL major versions](#AuroraMySQL.release-calendars.major "#AuroraMySQL.release-calendars.major")
.

| Aurora MySQL version                                                 | Aurora MySQL release date | Aurora MySQL end of standard support date |
| -------------------------------------------------------------------- | ------------------------- | ----------------------------------------- |
| *_8.4.7_<br>• (Compatible with Community MySQL 8.4.7)                | May 21, 2026              | November 30, 2027                         |
| *_3.13_<br>• (Compatible with Community MySQL 8.0.45)                | August 27, 2026           | August 27, 2027                           |
| *_3.12_<br>• (Compatible with Community MySQL 8.0.44)                | February 17, 2026         | February 17, 2027                         |
| *_3.11_<br>• (Compatible with Community MySQL 8.0.43)                | November 13, 2025         | November 13, 2026                         |
| *_3.10_<br>• (Compatible with Community MySQL 8.0.42) (LTS)          | July 31, 2025             | April 30, 2028                            |
| *_3.09_<br>• (Compatible with Community MySQL 8.0.40)                | May 14, 2025              | August 31, 2026                           |
| *_3.08_<br>• (Compatible with Community MySQL 8.0.39)                | November 18, 2024         | August 31, 2026                           |
| *_3.04_<br>• (Compatible with Community MySQL 8.0.28) (LTS)          | July 31, 2023             | October 31, 2026                          |
| *_2.121_<br>• (Compatible with Community MySQL 5.7.40 or<br>5.7.442) | July 25, 2023             | October 31, 2024                          |
| *_2.111_<br>• (Compatible with Community MySQL 5.7.12)               | October 25, 2022          | October 31, 2024                          |

LTS – Aurora MySQL long-term support (LTS) versions. For more information, see
[Long-term support (LTS) and beta releases for Amazon Aurora MySQL](../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md "../AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.md").

1 This minor version will continue to be available when the major version is in Amazon RDS Extended Support.

2 Aurora MySQL 2.12 versions through 2.12.1 are compatible with MySQL version 5.7.40, and versions 2.12.2 and higher
are compatible with MySQL version 5.7.44.
