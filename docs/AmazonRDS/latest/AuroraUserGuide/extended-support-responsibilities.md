# Amazon Aurora and customer responsibilities with Amazon RDS Extended Support

The following content describes the responsibilities of Amazon Aurora and your
responsibilities with RDS Extended Support.

###### Topics

- [Amazon Aurora responsibilities](#extended-support-rds-responsibilities "#extended-support-rds-responsibilities")
- [Your responsibilities](#extended-support-customer-responsibilities "#extended-support-customer-responsibilities")

## Amazon Aurora responsibilities

After the Aurora end of standard support date, Amazon Aurora will supply
patches, bug fixes, and upgrades for engines that are enrolled in RDS Extended Support. This
will occur for up to 3 years, or until you stop using the engines, whichever happens
first.

The patches will be for Critical and High CVEs as defined by the National
Vulnerability Database (NVD) CVSS severity ratings. For more information, see [Vulnerability Metrics](https://nvd.nist.gov/vuln-metrics/cvss# "https://nvd.nist.gov/vuln-metrics/cvss#").

## Your responsibilities

You're responsible for applying the patches, bug fixes, and upgrades given for
Aurora DB clusters or global clusters enrolled in RDS Extended Support.
Amazon Aurora reserves the right to change, replace, or withdraw such
patches, bug fixes, and upgrades at any time. If a patch is necessary to address
security or critical stability issues, Amazon Aurora reserves the right
to update your Aurora DB clusters or global clusters with the patch, or to
require that you install the patch.

You're also responsible for upgrading your engine to a newer engine version
_before_ the RDS end of Extended Support date. The RDS end
of Extended Support date is typically 3 years after the community end of
life. . For the RDS end of Extended Support date for your database major engine
version, see [Amazon Aurora major versions](Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions "Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions").

If you don't upgrade your engine, then after the RDS end of Extended Support date, Amazon Aurora will attempt to upgrade your engine to a newer engine
version that's supported under Aurora standard support. If the upgrade fails, then
Amazon Aurora reserves the right to delete the
Aurora DB cluster or global cluster that's running the engine past the Aurora end
of standard support date. However, before doing so, Amazon Aurora will preserve your
data from that engine.
