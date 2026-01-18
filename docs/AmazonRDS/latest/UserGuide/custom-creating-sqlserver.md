# RDS Custom service-linked role

A _service-linked role_ gives Amazon RDS Custom access to resources in your AWS account. It makes
using RDS Custom easier because you don't have to manually add the necessary permissions. RDS Custom defines the permissions of its
service-linked roles, and unless defined otherwise, only RDS Custom can assume its roles. The defined permissions include the trust
policy and the permissions policy, and that permissions policy can't be attached to any other IAM entity.

When you create an RDS Custom DB instance, both the Amazon RDS and RDS Custom service-linked roles are created (if they don't already
exist) and used. For more information, see [Using service-linked roles for
Amazon RDS](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md").

The first time that you create an RDS Custom for SQL Server DB instance, you might receive the
following error: **`The service-linked role is in the process of being created.
 Try again later.`** If you do, wait a few minutes and then try again to
create the DB instance.
