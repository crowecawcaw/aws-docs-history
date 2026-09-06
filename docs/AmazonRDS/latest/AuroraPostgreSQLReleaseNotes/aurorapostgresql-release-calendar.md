

# Release calendars for Aurora PostgreSQL
<a name="aurorapostgresql-release-calendar"></a>

The release calendars on this page can help you plan your major and minor version upgrades. For more information on Amazon Aurora upgrades, versioning, and lifecycle, see [Amazon Aurora versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.html).

**Topics**
+ [Version currency timelines](#aurorapostgresql.version.currency.timelines)
+ [Release calendar for Aurora PostgreSQL major versions](#aurorapostgresql.major.versions.supported)
+ [Release calendar for Aurora PostgreSQL minor versions](#aurorapostgresql.minor.versions.supported)
+ [Release calendar for Amazon Aurora PostgreSQL Limitless Database minor versions](#aurorapostgresql.limitless.minor.versions.supported)

## Version currency timelines
<a name="aurorapostgresql.version.currency.timelines"></a>

Aurora PostgreSQL tracks community database engine releases on a defined cadence. These version currency timelines are published to give you transparency into that cadence. You can use these timelines to:
+ Plan major version upgrades and estimate when a new Aurora PostgreSQL major version will be available.
+ Schedule minor version upgrades during your maintenance windows.
+ Select the right Aurora Long-Term Support (LTS) version for workloads that require staying on the same minor version across multiple release cycles.

The following table lists the version currency timelines for Aurora PostgreSQL.


| Release type | Timelines | 
| --- | --- | 
| Major versions | Within 8 months of the community's first minor release for the new major version <major>.1 | 
| Minor versions | Within 3 months of the community release | 
| [Aurora LTS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.LTS.html) (per major) | Within 12 months of the Aurora major version release | 

## Release calendar for Aurora PostgreSQL major versions
<a name="aurorapostgresql.major.versions.supported"></a>

Aurora PostgreSQL major versions are available under standard support at least until community end of life for the corresponding community version. You can continue running a major version past its Aurora end of standard support date for a fee. For more information, see [Using Amazon RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) and [Aurora pricing](https://aws.amazon.com/rds/aurora/). 

You can use the following dates to plan your testing and upgrade cycles. 

**Note**  
Dates with only a month and a year are approximate and are updated with an exact date when it's known.  
You can also view information about support dates for major engine versions by using the AWS CLI or the RDS API. For more information, see [Viewing support dates for engine versions in Amazon RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-viewing-support-dates.html).


| PostgreSQL major version | Community release date | Community end of life date | Aurora major version | Aurora PostgreSQL LTS version | Aurora release date | Aurora end of standard support date | Start of RDS Extended Support year 1 pricing | Start of RDS Extended Support year 3 pricing | End of RDS Extended Support date | Minor versions eligible for RDS Extended Support | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| PostgreSQL 11 | 18 October 2018 | November 2023 | Aurora PostgreSQL 3. Applies to PostgreSQL 11.12 and older versions only. For version 11.13 and higher versions, the Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location. | Aurora PostgreSQL 11.9 | 26 November 2019 | 29 February 2024 | 1 April 2024 | 1 April 2026 | 31 March 2027 | Aurora PostgreSQL 11.9 and 11.21 | 
| PostgreSQL 12 | 14 November 2019 | November 2024 | Aurora PostgreSQL 4. Applies to PostgreSQL 12.7 and older versions only. For version 12.8 and higher versions, the Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location. | Aurora PostgreSQL 12.9 | 23 December 2020 | 28 February 2025 | 1 March 2025 | 1 March 2027 | 29 February 2028 | Aurora PostgreSQL 12.9 and 12.22 | 
| PostgreSQL 13 | 24 September 2020 | November 2025 | Aurora PostgreSQL 13. For version 13.3 and higher versions, the Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location when patches to Aurora are released. | Aurora PostgreSQL 13.9 | 26 August 2021 | 28 February 2026 | 1 March 2026 | 1 March 2028 | 28 February 2029 | Aurora PostgreSQL 13.9 and 13.23 | 
| PostgreSQL 14 | 30 September 2021 | November 2026 | Aurora PostgreSQL 14.3 and higher. The Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location when patches to Aurora are released. | Aurora PostgreSQL 14.6 | 24 February 2022 | 28 February 2027 | 1 March 2027 | 1 March 2029 | 28 February 2030 | To be determined | 
| PostgreSQL 15 | 13 October 2022 | November 2027 | Aurora PostgreSQL 15.2 and higher. The Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location when patches to Aurora are released. | Aurora PostgreSQL 15.10 | 8 February 2023 | 29 February 2028 | 1 March 2028 | 1 March 2030 | 28 February 2031 | To be determined | 
| PostgreSQL 16 | 14 September 2023 | 9 November 2028 | Aurora PostgreSQL 16.1 and higher. The Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location when patches to Aurora are released. | Aurora PostgreSQL16.8 | 31 January 2024 | 28 February 2029 | 1 March 2029 | 1 March 2031 | 28 February 2032 | To be determined | 
| PostgreSQL 17 | 26 September 2024 | November 2029 | Aurora PostgreSQL 17.4 and higher. The Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location when patches to Aurora are released. | Aurora PostgreSQL17.7 | 1 May 2025 | 28 February 2030 | 1 March 2030 | 1 March 2032 | 28 February 2033 | To be determined | 
| PostgreSQL 18 | 26 February 2026 | November 2030 | Aurora PostgreSQL 18.3 and higher. The Aurora version is the same as the {{major}}.{{minor}} version of the PostgreSQL community version, with a third digit in the {{patch}} location when patches to Aurora are released. | – | 11 June 2026 | 28 February 2031 | 1 March 2031 | 1 March 2033 | 28 February 2034 | To be determined | 

**Note**  
RDS Extended Support charges only apply after a major version reaches end of standard support. RDS Extended Support for PostgreSQL 11 starts on March 1, 2024, but will not be charged until April 1, 2024. Between March 1 and March 31, all PostgreSQL version 11 DB instances and clusters on RDS are covered under RDS Extended Support.

## Release calendar for Aurora PostgreSQL minor versions
<a name="aurorapostgresql.minor.versions.supported"></a>

Aurora currently supports the following minor versions of PostgreSQL. 

In general, Aurora minor versions are released quarterly. The release schedule might vary to pick up additional features or fixes.

Amazon RDS Extended Support charges apply only to certain minor versions after a major version is eligible for Extended Support. For more information, see [Release calendar for Aurora PostgreSQL major versions](#aurorapostgresql.major.versions.supported).

**Note**  
Dates with only a month and a year are approximate, and will be updated with an exact date when it’s known.


<table>
<thead>
  <tr><th>PostgreSQL minor engine version</th><th>Community release date</th><th>Aurora release date</th><th>Aurora end of standard support date</th><th></th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>18</b></td><td></td><td></td><td></td></tr>
  <tr><td>18.4</td><td>May 2026</td><td>21 August 2026</td><td>31 December 2027</td><td></td><td></td><td></td></tr>
  <tr><td>18.3</td><td>26 February 2026</td><td>11 June 2026</td><td>30 November 2027</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>17</b></td><td></td><td></td><td></td></tr>
  <tr><td>17.10</td><td>May 2026</td><td>21 August 2026</td><td>31 December 2027</td><td></td><td></td><td></td></tr>
  <tr><td>17.9</td><td>26 February 2026</td><td>6 April 2026</td><td>30 September 2027</td><td></td><td></td><td></td></tr>
  <tr><td>17.7 (LTS)</td><td>13 November 2025</td><td>18 December 2025</td><td>28 February 2030</td><td></td><td></td><td></td></tr>
  <tr><td>17.6</td><td>14 August 2025</td><td>25 November 2025</td><td>30 April 2027</td><td></td><td></td><td></td></tr>
  <tr><td>17.5</td><td>8 May 2025</td><td>30 June 2025</td><td>31 December 2026</td><td></td><td></td><td></td></tr>
  <tr><td>17.4</td><td>20 February 2025</td><td>1 May 2025</td><td>30 November 2026</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>16</b></td><td></td><td></td><td></td></tr>
  <tr><td>16.14</td><td>May 2026</td><td>21 August 2026</td><td>31 December 2027</td><td></td><td></td><td></td></tr>
  <tr><td>16.13</td><td>26 February 2026</td><td>6 April 2026</td><td>30 September 2027</td><td></td><td></td><td></td></tr>
  <tr><td>16.11</td><td>13 November 2025</td><td>18 December 2025</td><td>31 May 2027</td><td></td><td></td><td></td></tr>
  <tr><td>16.10</td><td>14 August 2025</td><td>25 November 2025</td><td>30 April 2027</td><td></td><td></td><td></td></tr>
  <tr><td>16.9</td><td>8 May 2025</td><td>30 June 2025</td><td>31 December 2026</td><td></td><td></td><td></td></tr>
  <tr><td>16.8 (LTS)</td><td>20 February 2025</td><td>8 April 2025</td><td>28 February 2029</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>15</b></td><td></td><td></td><td></td></tr>
  <tr><td>15.18</td><td>May 2026</td><td>21 August 2026</td><td>31 December 2027</td><td></td><td></td><td></td></tr>
  <tr><td>15.17</td><td>26 February 2026</td><td>6 April 2026</td><td>30 September 2027</td><td></td><td></td><td></td></tr>
  <tr><td>15.15</td><td>13 November 2025</td><td>18 December 2025</td><td>31 May 2027</td><td></td><td></td><td></td></tr>
  <tr><td>15.14</td><td>14 August 2025</td><td>25 November 2025</td><td>30 April 2027</td><td></td><td></td><td></td></tr>
  <tr><td>15.13</td><td>8 May 2025</td><td>30 June 2025</td><td>31 December 2026</td><td></td><td></td><td></td></tr>
  <tr><td>15.12</td><td>20 February 2025</td><td>8 April 2025</td><td>30 November 2026</td><td></td><td></td><td></td></tr>
  <tr><td>15.10 (LTS)</td><td>21 November 2024</td><td>13 December 2024</td><td>29 February 2028</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>14</b></td><td></td><td></td><td></td></tr>
  <tr><td>14.23</td><td>May 2026</td><td>21 August 2026</td><td>28 February 2027</td><td></td><td></td><td></td></tr>
  <tr><td>14.22</td><td>26 February 2026</td><td>6 April 2026</td><td>28 February 2027</td><td></td><td></td><td></td></tr>
  <tr><td>14.20</td><td>13 November 2025</td><td>18 December 2025</td><td>28 February 2027</td><td></td><td></td><td></td></tr>
  <tr><td>14.19</td><td>14 August 2025</td><td>25 November 2025</td><td>28 February 2027</td><td></td><td></td><td></td></tr>
  <tr><td>14.18</td><td>8 May 2025</td><td>30 June 2025</td><td>31 December 2026</td><td></td><td></td><td></td></tr>
  <tr><td>14.17</td><td>20 February 2025</td><td>8 April 2025</td><td>30 November 2026</td><td></td><td></td><td></td></tr>
  <tr><td>14.6 (LTS)</td><td>10 November 2022</td><td>23 January 2023</td><td>28 February 2027</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>13</b></td><td></td><td></td><td></td></tr>
  <tr><td>13.23*</td><td>13 November 2025</td><td>18 December 2025</td><td>28 February 2026</td><td></td><td></td><td></td></tr>
  <tr><td>13.9 (LTS)*</td><td>10 November 2022</td><td>23 January 2023</td><td>28 February 2026</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>12</b></td><td></td><td></td><td></td></tr>
  <tr><td>12.22*</td><td>21 November 2024</td><td>13 December 2024</td><td>28 February 2025</td><td></td><td></td><td></td></tr>
  <tr><td>12.9* (LTS)</td><td>11 November 2021</td><td>25 February 2022</td><td>28 February 2025</td><td></td><td></td><td></td></tr>
  <tr><td colspan="4"><b>11</b></td><td></td><td></td><td></td></tr>
  <tr><td>11.21*</td><td>10 August 2023</td><td>7 September 2023</td><td>29 February 2024</td><td></td><td></td><td></td></tr>
  <tr><td>11.9* (LTS)</td><td>13 August 2020</td><td>11 December 2020</td><td>29 February 2024</td><td></td><td></td><td></td></tr>
</tbody>
</table>


\* Amazon RDS Extended Support eligible minor engine version. For more information, see [Using Amazon RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html).

LTS - Aurora PostgreSQL long-term support (LTS) releases. For more information see [Aurora PostgreSQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.LTS.html).

## Release calendar for Amazon Aurora PostgreSQL Limitless Database minor versions
<a name="aurorapostgresql.limitless.minor.versions.supported"></a>

Aurora currently supports the following Aurora PostgreSQL Limitless Database minor versions of PostgreSQL.

**Note**  
Dates with only a month and a year are approximate, and will be updated with an exact date when it's known.


| PostgreSQL Limitless minor engine version | Aurora release date | Aurora end of standard support date | 
| --- | --- | --- | 
| 16.11-limitless | February 25, 2026 | October 2027 | 
| 16.10-limitless | February 24, 2026 | September 2027 | 
| 16.9-limitless | September 5, 2025 | March 2027 | 
| 16.8-limitless | May 8, 2025 | November 2026 | 
| 16.6-limitless | January 24, 2025 | September 2026 | 
| 16.4-limitless | October 31, 2024 | September 2026 | 