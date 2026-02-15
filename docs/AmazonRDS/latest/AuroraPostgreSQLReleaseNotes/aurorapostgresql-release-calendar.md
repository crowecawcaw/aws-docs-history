# Release calendars for Aurora PostgreSQL

The release calendars on this page can help you plan your major and minor version upgrades. For more information on Amazon Aurora upgrades, versioning,
and lifecycle, see [Amazon Aurora versions](../AuroraUserGuide/Aurora.md "../AuroraUserGuide/Aurora.md").

###### Topics

- [Release calendar for Aurora PostgreSQL major versions](#aurorapostgresql.major.versions.supported "#aurorapostgresql.major.versions.supported")
- [Release calendar for Aurora PostgreSQL minor versions](#aurorapostgresql.minor.versions.supported "#aurorapostgresql.minor.versions.supported")

## Release calendar for Aurora PostgreSQL major versions

Aurora PostgreSQL major versions are available under standard support at least until
community end of life for the corresponding community version. You can continue running
a major version past its Aurora end of standard support date for a fee. For more
information, see [Using Amazon RDS Extended Support](../AuroraUserGuide/extended-support.md "../AuroraUserGuide/extended-support.md") and [Aurora pricing](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/").

You can use the following dates to plan your testing and upgrade cycles.

###### Note

Dates with only a month and a year are approximate and are updated with an exact date when it's known.

You can also view information about support dates for major engine
versions by using the AWS CLI or the RDS API. For more information,
see [Viewing support dates for engine versions in Amazon RDS Extended Support](../AuroraUserGuide/extended-support-viewing-support-dates.md "../AuroraUserGuide/extended-support-viewing-support-dates.md").

| PostgreSQL major version | Community release date | Community end of life date | Aurora major version                                                                                                                                                                                                                                                  | Aurora PostgreSQL LTS version | Aurora release date | Aurora end of standard support date | Start of RDS Extended Support year 1 pricing | Start of RDS Extended Support year 3 pricing | End of RDS Extended Support date | Minor versions eligible for RDS Extended Support |
| ------------------------ | ---------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------- | ----------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------- | ------------------------------------------------ |
| PostgreSQL 11            | 18 October 2018        | November 2023              | Aurora PostgreSQL 3. Applies to PostgreSQL 11.12 and older versions only. For version 11.13 and higher versions, the Aurora<br>version is the same as the `major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the `patch` location. | Aurora PostgreSQL 11.9        | 26 November 2019    | 29 February 2024                    | 1 April 2024                                 | 1 April 2026                                 | 31 March 2027                    | Aurora PostgreSQL 11.9 and 11.21                 |
| PostgreSQL 12            | 14 November 2019       | November 2024              | Aurora PostgreSQL 4. Applies to PostgreSQL 12.7 and older versions only. For version 12.8 and higher versions, the Aurora<br>version is the same as the `major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the `patch` location.   | Aurora PostgreSQL 12.9        | 23 December 2020    | 28 February 2025                    | 1 March 2025                                 | 1 March 2027                                 | 29 February 2028                 | Aurora PostgreSQL 12.9 and 12.22                 |
| PostgreSQL 13            | 24 September 2020      | November 2025              | Aurora PostgreSQL 13. For version 13.3 and higher versions, the Aurora version is the same<br>as the `major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the<br>`patch` location when patches to Aurora are released.               | Aurora PostgreSQL 13.9        | 26 August 2021      | 28 February 2026                    | 1 March 2026                                 | 1 March 2028                                 | 28 February 2029                 | Aurora PostgreSQL 13.9 and 13.23                 |
| PostgreSQL 14            | 30 September 2021      | November 2026              | Aurora PostgreSQL 14.3 and higher. The Aurora version is the same as the<br>`major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the<br>`patch` location when patches to Aurora are released.                                        | Aurora PostgreSQL 14.6        | 24 February 2022    | 28 February 2027                    | 1 March 2027                                 | 1 March 2029                                 | 29 February 2030                 | To be determined                                 |
| PostgreSQL 15            | 10 November 2022       | November 2027              | Aurora PostgreSQL 15.2 and higher. The Aurora version is the same as the<br>`major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the<br>`patch` location when patches to Aurora are released.                                        | Aurora PostgreSQL 15.10       | 8 February 2023     | 29 February 2028                    | 1 March 2028                                 | 1 March 2030                                 | 28 February 2031                 | To be determined                                 |
| PostgreSQL 16            | 14 September 2023      | 9 November 2028            | Aurora PostgreSQL 16.1 and higher. The Aurora version is the same as the<br>`major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the<br>`patch` location when patches to Aurora are released.                                        | –                             | 31 January 2024     | 28 February 2029                    | 1 March 2029                                 | 1 March 2031                                 | 28 February 2032                 | To be determined                                 |
| PostgreSQL 17            | 20 February 2025       | November 2029              | Aurora PostgreSQL 17.4 and higher. The Aurora version is the same as the<br>`major`.`minor` version of the<br>PostgreSQL community version, with a third digit in the<br>`patch` location when patches to Aurora are released.                                        | –                             | 1 May 2025          | 28 February 2030                    | 1 March 2030                                 | 1 March 2032                                 | 28 February 2033                 | To be determined                                 |

###### Note

RDS Extended Support charges only apply after a major version reaches end of standard support. RDS Extended Support for PostgreSQL 11 starts on March 1, 2024,
but will not be charged until April 1, 2024. Between March 1 and March 31, all PostgreSQL version 11 DB instances and clusters on RDS are covered under RDS Extended Support.

## Release calendar for Aurora PostgreSQL minor versions

Aurora currently supports the following minor versions of PostgreSQL.

In general, Aurora minor versions are released quarterly. The release schedule might vary to pick up additional features or fixes.

Amazon RDS Extended Support charges apply only to certain minor versions after a major version is eligible for Extended Support. For more information, see [Release calendar for Aurora PostgreSQL major versions](#aurorapostgresql.major.versions.supported "#aurorapostgresql.major.versions.supported").

###### Note

Dates with only a month and a year are approximate, and will be updated with an exact date when it’s known.

| PostgreSQL minor engine version | Community release date | Aurora release date | Aurora end of standard support date |
| ------------------------------- | ---------------------- | ------------------- | ----------------------------------- |
| **17**                          |
| 17.7                            | 13 November 2025       | 18 December 2025    | July 2027                           |
| 17.6                            | 14 August 2025         | 25 November 2025    | June 2027                           |
| 17.5                            | 8 May 2025             | 30 June 2025        | December 2026                       |
| 17.4                            | 20 February 2025       | May 1 2025          | November 2026                       |
| **16**                          |
| 16.11                           | 13 November 2025       | 18 December 2025    | July 2027                           |
| 16.10                           | 14 August 2025         | 25 November 2025    | June 2027                           |
| 16.9                            | 8 May 2025             | 30 June 2025        | December 2026                       |
| 16.8 (LTS)                      | 20 February 2025       | April 8 2025        | 28 February 2029                    |
| 16.6                            | 21 November 2024       | 13 December 2024    | May 2026                            |
| 16.4                            | 08 August 2024         | 30 September 2024   | May 2026                            |
| **15**                          |
| 15.15                           | 13 November 2025       | 18 December 2025    | July 2027                           |
| 15.14                           | 14 August 2025         | 25 November 2025    | June 2027                           |
| 15.13                           | 8 May 2025             | 30 June 2025        | December 2026                       |
| 15.12                           | 20 February 2025       | April 8 2025        | November 2026                       |
| 15.10 (LTS)                     | 21 November 2024       | 13 December 2024    | 29 February 2028                    |
| 15.8                            | 08 August 2024         | 30 September 2024   | May 2026                            |
| **14**                          |
| 14.20                           | 13 November 2025       | 18 December 2025    | July 2027                           |
| 14.19                           | 14 August 2025         | 25 November 2025    | June 2027                           |
| 14.18                           | 8 May 2025             | 30 June 2025        | December 2026                       |
| 14.17                           | 20 February 2025       | April 8 2025        | November 2026                       |
| 14.15                           | 21 November 2024       | 13 December 2024    | May 2026                            |
| 14.13                           | 08 August 2024         | 30 September 2024   | May 2026                            |
| 14.6 (LTS)                      | 10 November 2022       | 23 January 2023     | 28 February 2027                    |
| **13**                          |
| 13.23                           | 13 November 2025       | 18 December 2025    | 28 February 2026                    |
| 13.22                           | 14 August 2025         | 25 November 2025    | 28 February 2026                    |
| 13.21                           | 8 May 2025             | 30 June 2025        | 28 February 2026                    |
| 13.20                           | 20 February 2025       | April 8 2025        | 28 February 2026                    |
| 13.18                           | 21 November 2024       | 13 December 2024    | 28 February 2026                    |
| 13.16                           | 08 August 2024         | 30 September 2024   | 28 February 2026                    |
| 13.9 (LTS)                      | 10 November 2022       | 23 January 2023     | 28 February 2026                    |
| **12**                          |
| 12.22\*                         | 21 November 2024       | 13 December 2024    | 28 February 2025                    |
| 12.9\<br>• (LTS)                | 11 November 2021       | 25 February 2022    | 28 February 2025                    |
| **11**                          |
| 11.21\*                         | 10 August 2023         | 7 September 2023    | 29 February 2024                    |
| 11.9\<br>• (LTS)                | 13 August 2020         | 11 December 2020    | 29 February 2024                    |

\* Amazon RDS Extended Support eligible minor engine version. For more information, see [Using Amazon RDS Extended Support](../AuroraUserGuide/extended-support.md "../AuroraUserGuide/extended-support.md").

LTS - Aurora PostgreSQL long-term support (LTS) releases. For more information see [Aurora PostgreSQL long-term support (LTS) releases](../AuroraUserGuide/AuroraPostgreSQL.Updates.md "../AuroraUserGuide/AuroraPostgreSQL.Updates.md").
