End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# AWS Proton environments

For AWS Proton, an environment represents the set of shared resources and policies that AWS Proton
[services](ag-services.md "ag-services.md") are deployed into. They can contain any resources
that are expected to be shared across AWS Proton service instances. These resources can include VPCs,
clusters, and shared load balancers or API Gateways. An AWS Proton environment must be created before
a service can be deployed to it.

This section describes how to manage environments using create, view, update, and delete
operations. For >additional information, see the [The AWS Proton Service API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Topics

- [IAM Roles](ag-environment-roles.md "ag-environment-roles.md")
- [Create an environment](ag-create-env.md "ag-create-env.md")
- [View environment data](ag-env-view.md "ag-env-view.md")
- [Update an environment](ag-env-update.md "ag-env-update.md")
- [Delete an environment](ag-env-delete.md "ag-env-delete.md")
- [Environment account connections](ag-env-account-connections.md "ag-env-account-connections.md")
- [Customer-managed environments](ag-env-customer-managed.md "ag-env-customer-managed.md")
- [CodeBuild provisioning role
  creation](ag-env-codebuild-provisioning-role-creation.md "ag-env-codebuild-provisioning-role-creation.md")
