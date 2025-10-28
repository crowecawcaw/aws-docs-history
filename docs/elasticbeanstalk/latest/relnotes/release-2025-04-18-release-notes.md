# Release: Elastic Beanstalk adds feature to migrate your Windows IIS applications to AWS Elastic Beanstalk on

April 18, 2025

AWS Elastic Beanstalk releases the **eb migrate** EB CLI command to migrate your Windows IIS applications to Elastic Beanstalk hosted environments on the AWS Cloud.

**Release date:** April 18, 2025

## Changes

AWS offers multiple paths for migrating Windows applications to the cloud. Today Elastic Beanstalk
releases a new streamlined migration option to migrate your IIS applications directly to
AWS Elastic Beanstalk with minimal reconfiguration. The newly released **eb migrate**
command in the Elastic Beanstalk Command Line Interface (EB CLI) automatically creates and
configures Elastic Beanstalk environments optimized for your Windows applications. The Windows IIS
applications that you choose to migrate can be operating on-premises or on an external
environment connected via the internet.

All you need is an internet connection to your account on the AWS Cloud and to download
and install the EB CLI tool to your source server. You can then run the **eb
migrate** command from your source server, and the command will automatically
discover, package, and deploy your IIS applications to an Elastic Beanstalk hosted environment on the AWS
Cloud.

For complete, detailed instructions to migrate your IIS applications to an AWS Elastic Beanstalk
hosted environment, see [Migrating IIS
applications to Elastic Beanstalk](../dg/dotnet-migrating-applications.md "../dg/dotnet-migrating-applications.md") in the _AWS Elastic Beanstalk Developer Guide_.
