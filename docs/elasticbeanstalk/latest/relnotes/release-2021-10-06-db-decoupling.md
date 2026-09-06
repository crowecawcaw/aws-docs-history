

# Release: Elastic Beanstalk adds support for decoupling a database running in an Elastic Beanstalk environment on October 6, 2021
<a name="release-2021-10-06-db-decoupling"></a>

AWS Elastic Beanstalk added support for decoupling a database running in an Elastic Beanstalk environment.

**Release date:** October 6, 2021

## Changes
<a name="release-2021-10-06-db-decoupling.changes"></a>

Elastic Beanstalk provides support for running Amazon RDS instances in your Elastic Beanstalk environment. This works great for development and testing environments. However, prior to today’s release, it wasn’t ideal for a production environment, because it tied the lifecycle of the database instance to the lifecycle of your application's environment.

Starting with today’s release you can decouple a database managed by Elastic Beanstalk from a Beanstalk environment. The environment’s health is not affected by the decoupling operation, and you can keep the database operational as an external database, available for multiple environments to connect to it. You also have the option to terminate an Elastic Beanstalk environment, while leaving the database operational. 

For more information, see [ Adding a database to your Elastic Beanstalk environment ](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.db.html) in the *AWS Elastic Beanstalk Developer Guide*.