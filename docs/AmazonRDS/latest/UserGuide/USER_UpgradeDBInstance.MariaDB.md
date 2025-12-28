# MariaDB version

numbers

The version numbering sequence for the RDS for MariaDB database engine is either in the
form of _major.minor.patch.YYYYMMDD_ or
_major.minor.patch_, for example, 10.11.5.R2.20231201 or 10.4.30.
The format used depends on the MariaDB engine version.

**major**

The major version number is both the integer and the first fractional part
of the version number, for example, 10.11. A major version upgrade increases
the major part of the version number. For example, an upgrade from
_10.5_.20 to 10.6.12 is a major version upgrade,
where _10.5_ and _10.6_ are the major
version numbers.

**minor**

The minor version number is the third part of the version number, for
example, the 5 in 10.11.5.

**patch**

The patch is the fourth part
of the version number, for example, the R2 in 10.11.5.R2. An RDS patch version
includes important bug fixes added to a minor version after its release.

**YYYYMMDD**

The date is the fifth part of the version number, for example, the 20231201
in 10.11.5.R2.20231201. An RDS date version is a security patch that
includes important security fixes added to a minor version after its
release. It doesn't include any fixes that might change an engine's
behavior.

The following table explains the naming scheme for RDS for MariaDB version 10.11.

| 10.11 minor version | Naming scheme                                                                                                                                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥5                  | New DB instances use _major.minor.patch.YYMMDD_,<br>for example, 10.11.5.R2.20231201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 10.11.5.R2,<br>until your next major or minor version upgrade. |
| < 5                 | Existing DB instances use _major.minor.patch_, for<br>example, 10.11.4.R2.                                                                                                                                                   |

The following table explains the naming scheme for RDS for MariaDB version 10.6.

| 10.6 minor version | Naming scheme                                                                                                                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 14               | New DB instances use _major.minor.patch.YYMMDD_,<br>for example, 10.6.14.R2.20231201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 10.6.14.R2,<br>until your next major or minor version upgrade. |
| < 14               | Existing DB instances use _major.minor.patch_, for<br>example, 10.6.13.R2.                                                                                                                                                   |

The following table explains the naming scheme for RDS for MariaDB version 10.5.

| 10.5 minor version | Naming scheme                                                                                                                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 21               | New DB instances use _major.minor.patch.YYMMDD_,<br>for example, 10.5.21.R2.20231201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 10.5.21.R2,<br>until your next major or minor version upgrade. |
| < 21               | Existing DB instances use _major.minor.patch_, for<br>example, 10.5.20.R2.                                                                                                                                                   |

The following table explains the naming scheme for RDS for MariaDB version 10.4.

| 10.4 minor version | Naming scheme                                                                                                                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 30               | New DB instances use _major.minor.patch.YYMMDD_,<br>for example, 10.4.30.R2.20231201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 10.4.30.R2,<br>until your next major or minor version upgrade. |
| < 30               | Existing DB instances use _major.minor.patch_, for<br>example, 10.4.29.R2.                                                                                                                                                   |
