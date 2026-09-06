# Release: Elastic Beanstalk Active Directory domain join for Windows Server environments on August 31, 2026

AWS Elastic Beanstalk now supports automatically joining the Windows Server instances in your environment to an Active Directory domain that you manage with AWS Directory Service.

**Release date:** August 31, 2026

## Changes

Elastic Beanstalk Windows Server environments can now automatically join their instances to an Active Directory domain that you manage with AWS Directory
Service. You turn on the feature with configuration options in the [aws:elasticbeanstalk:windows:activedirectory](../dg/command-options-general.md#command-options-general-elasticbeanstalkwindowsactivedirectory "../dg/command-options-general.md#command-options-general-elasticbeanstalkwindowsactivedirectory") namespace, and each instance
joins the domain when it launches, without custom join logic.

Key features include:

- **Automatic domain join** – Each instance joins the directory at launch, before your application is
  deployed.
- **Organizational unit placement** – Optionally create computer objects in a specific organizational unit (OU)
  with the `DirectoryOU` option.
- **Graceful fall-through** – If a join doesn't succeed, the deployment continues and Elastic Beanstalk emits an event
  so you can diagnose it.

Active Directory domain join is available on Windows Server platform versions released on or after [August 18, 2026](release-2026-08-18-windows.md "release-2026-08-18-windows.md"), in all AWS Regions where Elastic Beanstalk
is available.

For more information, see [Joining instances to an Active Directory
domain](../dg/dotnet-activedirectory.md "../dg/dotnet-activedirectory.md") in the _AWS Elastic Beanstalk Developer Guide_.
