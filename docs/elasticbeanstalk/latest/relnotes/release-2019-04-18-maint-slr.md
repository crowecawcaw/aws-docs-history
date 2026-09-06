

# Release: AWS Elastic Beanstalk introduces a maintenance service-linked role on April 18, 2019
<a name="release-2019-04-18-maint-slr"></a>

Elastic Beanstalk added a new service-linked role for maintenance, to join the monitoring service-linked role already in use.

**Release date:** April 18, 2019

## Changes
<a name="release-2019-04-18-maint-slr.changes"></a>

AWS Elastic Beanstalk uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Elastic Beanstalk. Service-linked roles are predefined by Elastic Beanstalk and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up an Elastic Beanstalk environment easier because you don’t have to manually add the necessary permissions. Elastic Beanstalk defines the permissions of its service-linked roles, and unless defined otherwise, only Elastic Beanstalk can assume its roles.

Elastic Beanstalk already supports a monitoring service-linked role, which it uses for health monitoring and event reporting when no explicit service role is specified during environment creation. Today's release adds a *maintenance service-linked role*, which Elastic Beanstalk will associate with environments that need regular maintenance activities. At this time, Elastic Beanstalk will use a maintenance service-linked role with environments that don't have an [instance profile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-instanceprofile.html), as an alternative way to retrieve your application source code from Amazon Simple Storage Service (Amazon S3) during deployment.

For more information, see [Using Service-Linked Roles for Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-service-linked-roles.html) in the *AWS Elastic Beanstalk Developer Guide*.