# Release: Elastic Beanstalk introduces a managed-updates service-linked role on June 10, 2020

AWS Elastic Beanstalk added a new service-linked role for performing managed updates.

**Release date:** June 10, 2020

## Changes

Elastic Beanstalk uses AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Elastic Beanstalk. Service-linked roles are predefined by Elastic Beanstalk and
include all the permissions that the service requires to call other AWS services on your behalf. A service-linked role makes setting up an Elastic Beanstalk
environment easier because you don’t have to manually add the necessary permissions. Elastic Beanstalk defines the permissions of its service-linked roles, and unless
defined otherwise, only Elastic Beanstalk can assume its roles.

Elastic Beanstalk already supports a monitoring service-linked role. Elastic Beanstalk uses it for health monitoring and event reporting when no explicit service role is
specified during environment creation. Elastic Beanstalk also supports a maintenance service-linked role, which it associates with environments that need regular
maintenance activities.

Today's release adds support for a _managed-updates service-linked role_. When you launch an environment with managed platform
updates enabled and you specify your account's managed-updates service-linked role as the managed-updates service role, Elastic Beanstalk creates this service-linked
role for your account if it doesn't exist yet. Elastic Beanstalk associates it with the new environment. This streamlines the process of enabling managed updates for
new environments in cases that failed before.

For more information, see [Managed Platform Updates](../dg/environment-platform-update-managed.md "../dg/environment-platform-update-managed.md") and [Using service-linked roles for Elastic Beanstalk](../dg/using-service-linked-roles.md "../dg/using-service-linked-roles.md") in the _AWS Elastic Beanstalk Developer Guide_.
