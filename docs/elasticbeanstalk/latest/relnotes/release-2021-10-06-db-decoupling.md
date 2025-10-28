# Release: Elastic Beanstalk adds support for decoupling a database running in an Elastic Beanstalk environment on October 6, 2021

AWS Elastic Beanstalk added support for decoupling a database running in an Elastic Beanstalk environment.

**Release date:** October 6, 2021

## Changes

Elastic Beanstalk provides support for running Amazon RDS instances in your Elastic Beanstalk environment. This works great for development and testing environments. However,
prior to today’s release, it wasn’t ideal for a production environment, because it tied the lifecycle of the database instance to the lifecycle of your
application's environment.

Starting with today’s release you can decouple a database managed by Elastic Beanstalk from a Beanstalk environment. The environment’s health is not affected by
the decoupling operation, and you can keep the database operational as an external database, available for multiple environments to connect to it. You
also have the option to terminate an Elastic Beanstalk environment, while leaving the database operational.

For more information, see [Adding a database to your
Elastic Beanstalk environment](../dg/using-features.managing.md "../dg/using-features.managing.md") in the _AWS Elastic Beanstalk Developer Guide_.
