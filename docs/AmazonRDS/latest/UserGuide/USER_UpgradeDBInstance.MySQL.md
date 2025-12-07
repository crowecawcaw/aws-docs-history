# MySQL version numbers

The version numbering sequence for the RDS for MySQL database engine is either in the
form of _major.minor.patch.YYYYMMDD_ or
_major.minor.patch_, for example, 8.0.33.R2.20231201 or 5.7.44.
The format used depends on the MySQL engine version. For information about RDS Extended Support
version numbering, see [Amazon RDS Extended Support version naming](extended-support-versions.md#extended-support-naming "extended-support-versions.md#extended-support-naming").

**major**

The major version number is both the integer and the first fractional part
of the version number, for example, 8.0. A major version upgrade increases
the major part of the version number. For example, an upgrade from
_5.7_.44 to 8.0.33 is a major version upgrade, where
_5.7_ and _8.0_ are the major
version numbers.

**minor**

The minor version number is the third part of the version number, for
example, the 33 in 8.0.33.

**patch**

The patch is the fourth part of the version number, for example, the R2 in
8.0.33.R2. An RDS patch version includes important bug fixes added to a
minor version after its release.

**YYYYMMDD**

The date is the fifth part of the version number, for example, the
20231201 in 8.0.33.R2.20231201. An RDS date version is a security patch that
includes important security fixes added to a minor version after its
release. It doesn't include any fixes that might change an engine's
behavior.

The following table explains the naming scheme for RDS for MySQL version 8.4.

| 8.4 minor version | Naming scheme                                                                                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 3               | New DB instances use<br>_major.minor.patch.YYMMDD_, for example,<br>8.4.3.R2.20241201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 8.4.3.R2,<br>until your next major or minor version upgrade. |

The following table explains the naming scheme for RDS for MySQL version 8.0.

| 8.0 minor version | Naming scheme                                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 33              | New DB instances use _major.minor.patch.YYMMDD_,<br>for example, 8.0.33.R2.20231201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 8.0.33.R2,<br>until your next major or minor version upgrade. |
| < 33              | Existing DB instances use _major.minor.patch_, for<br>example, 8.0.32.R2.                                                                                                                                                  |

The following table explains the naming scheme for RDS for MySQL version 5.7.

| 5.7 minor version | Naming scheme                                                                                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 42              | New DB instances use<br>_major.minor.patch.YYMMDD_, for example,<br>5.7.42.R2.20231201.<br>Existing DB instances might use<br>_major.minor.patch_, for example, 5.7.42.R2,<br>until your next major or minor version upgrade. |
