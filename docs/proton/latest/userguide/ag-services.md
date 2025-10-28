End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# AWS Proton services

An AWS Proton service is an instantiation of a service template, normally including several service instances and a pipeline. An AWS Proton service instance
is an instantiation of a service template in a specific [environment](ag-environments.md "ag-environments.md"). A service template is a complete definition of
the infrastructure and optional service pipeline for an AWS Proton service.

After you deploy your service instances, you can update them by source code pushes that prompt the CI/CD pipeline or by updating the service to new
versions of its service template. AWS Proton prompts you when new versions of its service template become available so you can update your services to a new
version. When your service is updated, AWS Proton re-deploys the service and service instances.

This chapter shows how to manage services by using create, view, update and delete operations. For additional information, see the [_The AWS Proton Service API Reference_](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Topics

- [Create a service](ag-create-svc.md "ag-create-svc.md")
- [View service data](ag-svc-view.md "ag-svc-view.md")
- [Edit a service](ag-svc-update.md "ag-svc-update.md")
- [Delete a service](ag-svc-delete.md "ag-svc-delete.md")
- [View service instance data](ag-svc-instance-view.md "ag-svc-instance-view.md")
- [Update a service instance](ag-svc-instance-update.md "ag-svc-instance-update.md")
- [Update a service pipeline](ag-svc-pipeline-update.md "ag-svc-pipeline-update.md")
