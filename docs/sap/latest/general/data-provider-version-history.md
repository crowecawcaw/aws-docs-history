# Version history

**Version 4.3.2 (August, 2023)**

- Bug fix : Security updates to address [CVE-2022-45688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45688 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45688").

**Version 4.3.1 (June, 2023)**

- Bug fix : Data Provider is now setup for successful installation of SAP JVM.

**Version 4.3 (January, 2023)**

- Added support for JDK 17
- Added reading configuration information from remote Amazon S3 bucket

**Version 4.2 (November, 2022)**

- Added support for Oracle and Linux
- Added integration with Linux `logrotate` feature
- Updates to the RPM package build.

**Version 4.1.1 (September, 2022)**

- Added support for new Amazon EC2 instance types.

**Version 4.1.0 (January, 2022)**

- Added support for JDK 11.
- Added support for new Amazon EC2 instance types.

**Version 4.0.3 (December, 2021)**

- Bug fixes: Removed Log4j dependency.

**Version 4.0.2 (December, 2021)**

- Bug fixes: Security updates for Log4j2 issue (CVE-2021-44228).

**Version 4.0 (April, 2021)**

- Initial release of the 4.0 version.
- Support for SSM package installation.
- Support for IMDSv2.

**Version 3.0 (April, 2020)**

- Initial release of the 3.0 version.
- Switched the Java Runtime from Oracle to Amazon Corretto.

**Version 2.9 (August 30, 2017)**

- Added support for China Regions.
- Added Linux uninstaller.
- Linux installer can be customized to install from a custom S3 bucket.
- Silent installer for Windows (does not require any input).
- Improvements in determination of access points.
- Support for X1E instance family.

**Version 2.8 (March 1, 2017)**

- SLES 12, Red Hat 7, and Oracle Linux 7 will now use SYSTEMD to manage the daemon.
- Support for SLES and SLES for SAP 12 SP2.
- SLES 12 SP1 systems will get migrated from Linux services to SYSTEMD when trying to install the AWS Data Provider without having it de- installed first.
- Minor changes in logging texts.
- Support for R4 and M4 instance types.
- Updated Windows installation verification.

**Version 2.7 (December 21, 2016)**

- Support for Canada (Central), US East (Ohio), and EU (London) Regions.
- Default access point resolution for common AWS Regions is added.

**Version 2.6 (September 1, 2016)**

- Bug fixes: Installation script checks for existence of wget
- Support for Oracle Linux.

**Version 2.5 (May 2, 2016)**

- Bug fixes: Security and stability fixes in versions 2.2-2.4.
- New: Support for new Amazon EBS volume types:
  - Throughput Optimized HDD (st1)
  - Cold HDD (sc1)

- New: Support for the Amazon EC2 X1 instance family.

**Version 2.1 (January 20, 2016)**

- Support for Asia Pacific (Seoul) Region.
- Bug fix: Version 2.0 pulled files from an incorrect S3 bucket for installation. Version 2.0 needs to be uninstalled before version 2.1 is installed.

**Version 2.0 (December 22, 2015)**

- New: Windows devices in the range sdb to sdzz get correct SCSI device IDs assigned.
- New: Java VM consumption is now limited to 64 MB maximum heap size.

**Version 1.3.1 (July 14, 2015)**

- Bug fixes: Security fixes.
- New: Support for C4, D2, and M4 instance types. Users who migrate instances with installed 1.3 agents will automatically receive support for the new instance types through an updated configuration database on the web.

**Version 1.3 (February 17, 2015)**

- New: Support for new Amazon EC2 C4 instance family.
- Security fix: Upgraded Linux and Windows versions to JRE 8u31.
- Bug fix: Relative performance of c3.8xlarge instances is now reported correctly.
- New: CloudWatch and Amazon EC2 metrics access points:
  - Support for the EU (Frankfurt) Region was added.
  - Access points are user configurable. You can add information about new AWS Regions without having to install a new product version.
  - Access points are now updated from an internet-based database file. You can add new AWS Regions by updating a web-based configuration file and then restarting the daemon/service.

- New: Message log files with fixed disk space consumption are provided on Linux.
- New: User-configurable EC2 instance types are available.
- New: Web update support was added for future EC2 instance types without product updates.
- Bug fix: GP2 volumes now report the correct sample interval time.
- New: User-configurable sample times for new EBS volume types are now available.
- New: The AWS Data Provider for SAP now reports the virtualization type of the EC2 instance.

**Version 1.2.2 (October 1, 2014)**

- Windows bug fix: Installer executable pulls installation from correct Amazon S3 bucket.
- Windows bug fix: AWS Data Provider for SAP now reports the correct disk mapping for Windows EBS volumes with the following names: xvd[a-z][a-z].

**Version 1.2.1 (September 29, 2014)**

- Bug fix: EBS volumes now report correct attribute type ("string") for volume type.

**Version 1.2 (September 16, 2014)**

- New: Support for the T2, R3, and C3 instance families.
- New: Support for post-ECU (EC2 Compute Unit) instance types:
  - New instance types no longer have ECU values.
  - The reference compute power for these instance types is a hardware thread of the given processor. The total CPU power is equal to the number of the vCPUs of a given instance type.

- New: Support for the new EBS GP2 volume type.
  - Every volume is now tagged with the EBS volume type.

- New: Report of EBS one-minute volume statistics.
  - EBS volumes now report their individual sample interval in a separate attribute.

- Bug fix: EBS volume mapping for Windows devices now reports the correct name.
- Bug fix: Installation, update, and operation through HTTP/HTTPS proxies has been fixed.
- New: JRE 8 support has been added on Linux.
