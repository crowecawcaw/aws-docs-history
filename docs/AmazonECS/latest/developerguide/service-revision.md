# Amazon ECS service revisions

A service revision contains a record of the workload configuration Amazon ECS is attempting to
deploy. Whenever you create or deploy a service, Amazon ECS automatically creates and captures
the configuration that you're trying to deploy in the service revision.

Service revisions are read-only and have unique identifiers. For information about the
included properties, see [Properties included in an Amazon ECS service revision](service-revision-property.md "service-revision-property.md").

Service revisions provide the following benefits:

- During a service deployment, you can compare the currently deployed service
  revision (source) with the one being deployed (target).
- When you use the rollback option for a service deployment, Amazon ECS automatically
  rolls back the service deployment to the last successfully deployed service
  revision.
- Service revisions contain the record of the workload configuration in one resource.

## Service revision lifecycle

Amazon ECS automatically creates a new service revision when you create a service, or
update a service property that starts a deployment.

Amazon ECS doesn't create a new service revision for a rollback operation. Amazon ECS uses the
last successful service revision for the rollback.

A service revision is immutable.

Amazon ECS deletes the service revision when you delete a service.

You can view service revisions created on or after October 25, 2024 by using the
console, API, and the CLI.
