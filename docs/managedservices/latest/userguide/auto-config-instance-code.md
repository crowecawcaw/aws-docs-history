# Automatically update code on Linux instances

AMS automatically updates on instance code on Linux instances. This helps to improve operational stability and security of
the AMS components and environment altogether.

**FAQ:**

What's included in the On Instance Code (OIC) on Linux?
OIC includes ams-toolkit package along with some configuration files and cron jobs.
AMS require these files and packages for integration (Active Directory, CloudFormation and other dependencies).
We pre-bake these files into AMS-provided AMIs or install onto your instance during workload ingestion.

When will AMS update OIC?
AMS update OIC when we release a new version with bug fixes or other improvements. The workflow to
check the OIC version and update runs daily.
