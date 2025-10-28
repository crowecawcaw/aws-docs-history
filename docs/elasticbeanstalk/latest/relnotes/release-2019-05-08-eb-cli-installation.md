# Release: AWS Elastic Beanstalk simplifies EB CLI installation on May 8, 2019

Elastic Beanstalk released open-source scripts to simplify installing the Elastic Beanstalk Command Line Interface (EB CLI).

**Release date:** May 8, 2019

## Changes

The Elastic Beanstalk Command Line Interface (EB CLI) is a command line client that you can use to create, configure, and manage Elastic Beanstalk environments.
Previously, to use the EB CLI, you had to manually install the EB CLI's dependencies, including Python and `pip`. You also had to manage
dependency conflicts with other software in your development environment.

With today's release, you can use the [EB CLI setup scripts](https://github.com/aws/aws-elastic-beanstalk-cli-setup "https://github.com/aws/aws-elastic-beanstalk-cli-setup") to install the
EB CLI and its dependencies. The scripts also create a virtual environment for the EB CLI that is automatically activated when you run
`eb`.

For more information, see [Install the EB CLI Using Setup Scripts](../dg/eb-cli3-install.md "../dg/eb-cli3-install.md") in the
_AWS Elastic Beanstalk Developer Guide_.
