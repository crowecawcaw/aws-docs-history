# Using service-linked roles for

Amazon Managed Service for Prometheus

Amazon Managed Service for Prometheus uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to Amazon Managed Service for Prometheus. Service-linked roles are predefined by
Amazon Managed Service for Prometheus and include all the permissions that the service requires to call other AWS
services on your behalf.

A service-linked role makes setting up Amazon Managed Service for Prometheus easier because you don’t have to
manually add the necessary permissions. Amazon Managed Service for Prometheus defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon Managed Service for Prometheus can assume its
roles. The defined permissions include the trust policy and the permissions policy, and
that permissions policy cannot be attached to any other IAM entity.

## Using roles for scraping metrics from EKS

When automatically scraping metrics using Amazon Managed Service for Prometheus managed collector, the AWSServiceRoleForAmazonPrometheusScraper
service-linked role is used to make setting up managed collector easier, because you don't have
to manually add the necessary permissions. Amazon Managed Service for Prometheus defines the permissions, and
only Amazon Managed Service for Prometheus can assume the role.

For information about other services that support service-linked roles, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked
roles** column. Choose a **Yes** with a link
to view the service-linked role documentation for that service.

### Service-linked role

permissions for Amazon Managed Service for Prometheus

Amazon Managed Service for Prometheus uses a service-linked role named with the prefix
**AWSServiceRoleForAmazonPrometheusScraper** to allow Amazon Managed Service for Prometheus to automatically scrape metrics in your Amazon EKS clusters.

The AWSServiceRoleForAmazonPrometheusScraper service-linked role trusts the following services to assume the
role:

- `scraper.aps.amazonaws.com`

The role permissions policy named AmazonPrometheusScraperServiceRolePolicy
allows Amazon Managed Service for Prometheus to
complete the following actions on the specified resources:

- Ready and modify network configuration to connect to the network that
  contains your Amazon EKS cluster.
- Read metrics from Amazon EKS clusters and write metrics to your Amazon Managed Service for Prometheus workspaces.

You must configure permissions to allow your users, groups, or roles to create
a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

### Creating a service-linked

role for Amazon Managed Service for Prometheus

You don't need to manually create a service-linked role. When you
create an managed collector instance using Amazon EKS or Amazon Managed Service for Prometheus in the AWS Management Console, the AWS CLI, or the AWS API,
Amazon Managed Service for Prometheus creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action
in another service that uses the features supported by this role.
To learn more, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can
use the same process to recreate the role in your account. When you
create an managed collector instance using Amazon EKS or Amazon Managed Service for Prometheus, Amazon Managed Service for Prometheus creates the service-linked role for you
again.

### Editing a service-linked

role for Amazon Managed Service for Prometheus

Amazon Managed Service for Prometheus does not allow you to edit the AWSServiceRoleForAmazonPrometheusScraper service-linked role.
After you create a service-linked role, you cannot change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

### Deleting a service-linked

role for Amazon Managed Service for Prometheus

You don't need to manually delete the AWSServiceRoleForAmazonPrometheusScraper role. When you
delete all managed collector instances associated with the role in the AWS Management Console, the AWS CLI, or the AWS API, Amazon Managed Service for Prometheus
cleans up the resources and deletes the service-linked role for you.

### Supported Regions for Amazon Managed Service for Prometheus

service-linked roles

Amazon Managed Service for Prometheus supports using service-linked roles in all of the Regions where the
service is available. For more information, see [Supported Regions](what-is-Amazon-Managed-Service-Prometheus.md#AMP-supported-Regions "what-is-Amazon-Managed-Service-Prometheus.md#AMP-supported-Regions").
