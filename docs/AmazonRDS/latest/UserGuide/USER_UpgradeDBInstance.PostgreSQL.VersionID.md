

# PostgreSQL version numbers
<a name="USER_UpgradeDBInstance.PostgreSQL.VersionID"></a>

The version numbering sequence for the PostgreSQL database engine is as follows: 
+ For PostgreSQL versions 10 and higher, the engine version number is in the form *major.minor*. The major version number is the integer part of the version number. The minor version number is the fractional part of the version number. 

  A major version upgrade increases the integer part of the version number, such as upgrading from 10.*minor* to 11.*minor*.
+ For PostgreSQL versions lower than 10, the engine version number is in the form *major.major.minor*. The major engine version number is both the integer and the first fractional part of the version number. For example, 9.6 is a major version. The minor version number is the third part of the version number. For example, for version 9.6.12, the 12 is the minor version number.

  A major version upgrade increases the major part of the version number. For example, an upgrade from *9.6*.12 to 11.14 is a major version upgrade, where *9.6* and *11* are the major version numbers.

For information about RDS Extended Support version numbering, see [Amazon RDS Extended Support version naming](extended-support-versions.md#extended-support-naming).