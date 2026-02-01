# Elastic Beanstalk platform versions scheduled for retirement

AWS Elastic Beanstalk provides managed platforms that support running web applications developed for specific programming languages, frameworks, and web
containers. Elastic Beanstalk offers one or more platform versions for each platform. For details about currently supported platform versions, see [Elastic Beanstalk supported platforms](platforms-supported.md "platforms-supported.md").

This page lists platform versions that Elastic Beanstalk has scheduled for retirement, because some of their components are reaching their End of Life (EOL). These
platform versions remain available until the published retirement date of their retiring components. For a list of component retirement dates, see
[AWS Elastic Beanstalk platform schedules](../dg/platforms-schedule.md "../dg/platforms-schedule.md") in the _AWS Elastic Beanstalk Developer Guide_.

###### Note

On [July 18, 2022](../relnotes/release-2022-07-18-linux-al1-retire.md "../relnotes/release-2022-07-18-linux-al1-retire.md") Elastic Beanstalk set the
status of all platform branches based on Amazon Linux AMI (AL1) to **retired**.
For more information, see
[AL1 platform retirement FAQ](../dg/using-features.migration-al.md "../dg/using-features.migration-al.md") in the _AWS Elastic Beanstalk Developer Guide_.

The following sections provide information about all retiring platform versions.

###### Topics

- [PHP](#platforms-retiring.PHP "#platforms-retiring.PHP")

## PHP

Elastic Beanstalk has scheduled the following PHP platform versions for retirement.

| Platform Version and _Solution Stack Name_                                           | AMI              | Language   | Composer | Proxy Server                          | End Date   |
| ------------------------------------------------------------------------------------ | ---------------- | ---------- | -------- | ------------------------------------- | ---------- |
| **PHP 8.1 AL2023 version 4.9.2**<br>_64bit Amazon Linux 2023 v4.9.2 running PHP 8.1_ | 2023.10.20260120 | PHP 8.1.34 | 2.9.4    | nginx 1.28.1 (default), Apache 2.4.66 | 2026-03-31 |
| **PHP 8.1 AL2 version 3.12.2**<br>_64bit Amazon Linux 2 v3.12.2 running PHP 8.1_     | 2.0.20260120     | PHP 8.1.33 | 2.9.5    | nginx 1.28.1 (default), Apache 2.4.66 | 2026-03-31 |

For information about current platform versions, see [PHP](platforms-supported.md#platforms-supported.PHP "platforms-supported.md#platforms-supported.PHP").
