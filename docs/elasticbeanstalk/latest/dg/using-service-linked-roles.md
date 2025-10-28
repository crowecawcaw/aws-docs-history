# Using service-linked roles for Elastic Beanstalk

AWS Elastic Beanstalk uses AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Elastic Beanstalk. Service-linked roles are predefined by
Elastic Beanstalk and include all the permissions that the service requires to call other AWS services on your behalf.

Elastic Beanstalk defines a few types of service-linked roles:

- _Monitoring service-linked role_ – Allows Elastic Beanstalk to monitor the health of running environments and publish health event notifications.
- _Maintenance service-linked role_ – Allows Elastic Beanstalk to perform regular maintenance activities for your running environments.
- _Managed-updates service-linked role_ – Allows Elastic Beanstalk to perform scheduled platform updates of your running environments.

###### Topics

- [The monitoring service-linked role](using-service-linked-roles-monitoring.md "using-service-linked-roles-monitoring.md")
- [The maintenance service-linked role](using-service-linked-roles-maintenance.md "using-service-linked-roles-maintenance.md")
- [The managed-updates service-linked role](using-service-linked-roles-managedupdates.md "using-service-linked-roles-managedupdates.md")
