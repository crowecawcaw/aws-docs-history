# Release: AWS Elastic Beanstalk introduces a maintenance service-linked role on April 18, 2019

Elastic Beanstalk added a new service-linked role for maintenance, to join the monitoring service-linked role already in use.

**Release date:** April 18, 2019

## Changes

AWS Elastic Beanstalk uses AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Elastic Beanstalk. Service-linked roles are predefined by Elastic Beanstalk
and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up an Elastic Beanstalk environment easier because you don’t have to manually add the necessary permissions. Elastic Beanstalk defines the
permissions of its service-linked roles, and unless defined otherwise, only Elastic Beanstalk can assume its roles.

Elastic Beanstalk already supports a monitoring service-linked role, which it uses for health monitoring and event reporting when no explicit service role is
specified during environment creation. Today's release adds a _maintenance service-linked role_, which Elastic Beanstalk will associate with
environments that need regular maintenance activities. At this time, Elastic Beanstalk will use a maintenance service-linked role with environments that don't have an
[instance profile](../dg/iam-instanceprofile.md "../dg/iam-instanceprofile.md"), as an alternative way to retrieve your application source code from
Amazon Simple Storage Service (Amazon S3) during deployment.

For more information, see [Using Service-Linked Roles for Elastic Beanstalk](../dg/using-service-linked-roles.md "../dg/using-service-linked-roles.md") in the
_AWS Elastic Beanstalk Developer Guide_.
