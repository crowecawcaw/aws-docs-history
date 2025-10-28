# Implement Over-the-Air(OTA) tasks

You can create OTA tasks in two ways, depending on your update requirements and device targeting strategy:

## One-Time OTA task updates

A one-time OTA task contains a static list of targets (`ManagedThings`) to perform OTA updates.
You can add up to 100 targets at a time. The workflow uses AWS IoT Jobs with Fleet Indexing
while maintaining the managed integrations abstraction layer.

Use the following example to create a one-time OTA task:

```
aws iotmanagedintegrations create-ota-task \
  --description "One-time OTA update" \
  --s3-url "s3://test-job-document-bucket/ota-job-document.json" \
  --protocol HTTP \
  --target ["arn:aws:iotmanagedintegrations:`region`:`account id`:managed-thing/`managed thing id`"] \
  --ota-mechanism PUSH \
  --ota-type ONE_TIME \
  --client-token "foo" \
  --tags '{"key1":"foo","key2":"foo"}'
```

## Continuous OTA task updates

The OTA (Over-the-Air) grouping workflow enables you to deploy firmware updates to groups of
devices based on specific attributes,
using AWS IoT Jobs with Fleet Indexing while maintaining the managed integrations abstraction layer.
Continuous OTA tasks use a query string instead of specific targets.
All devices that match the query criteria
undergo OTA updates, and the query criteria is continually re-evaluated.
The matching targets will have job deployments.

### Configure prerequisites

Before creating continuous OTA tasks, complete these prerequisites:

1. Create a managed thing by calling the
   [CreateManagedThing](../APIReference/API_CreateManagedThing.md "../APIReference/API_CreateManagedThing.md")
   API and perform fleet provisioning.
2. Add metadata attributes to your managed things for query targeting.

Add attributes and metadata to `ManagedThing` using the
[UpdateManagedThing](../APIReference/API_UpdateManagedThing.md "../APIReference/API_UpdateManagedThing.md")
API:

```
aws iotmanagedintegrations update-managed-thing \
  --managed-thing-id "YOUR_MANAGED_THING_ID" \
  --meta-data '{"owner":"managedintegrations","version":"1.0"}'
```

Use the following example to create a continuous OTA task:

```
aws iotmanagedintegrations create-ota-task \
  --description "Continuous OTA update" \
  --s3-url "s3://test-job-document-bucket/ota-job-document.json" \
  --protocol HTTP \
  --ota-mechanism PUSH \
  --ota-type CONTINUOUS \
  --client-token "foo" \
  --ota-target-query-string "attributes.owner=managedintegrations" \
  --tags '{"key1":"foo","key2":"foo"}'
```

### Understand continuous OTA workflow

The continuous OTA update workflow follows these steps:

1. You update managed things with attributes using the
   [UpdateManagedThing](../APIReference/API_UpdateManagedThing.md "../APIReference/API_UpdateManagedThing.md")
   API.
2. Create an OTA job with a query string targeting specific device attributes.
3. The OTA service creates a dynamic Thing Group in AWS IoT Core based on query attributes
4. IoT Jobs executes updates on matching devices
5. You monitor progress via the
   [ListOtaTaskExecutions](../APIReference/API_ListOtaTaskExecutions.md "../APIReference/API_ListOtaTaskExecutions.md")
   API or OTA notifications through Kinesis stream (if enabled).

## Differences between Managed integrations OTA and IoT Jobs

The fundamental distinction between Managed integrations OTA and IoT Jobs lies in
**service orchestration and automation**. Managed integrations OTA provides a
**single-service solution** that
abstracts away the complexity of multi-service coordination.

What Managed integrations OTA does automatically:

- **Dynamic Thing Group creation:** Automatically generates AWS IoT Core
  thing groups based on your query criteria.
- **Target resolution:** Translates query strings
  (Example: `attributes.owner=managedintegrations`) into actual device targets.
- **Service integration:** Seamlessly coordinates between AWS IoT Core,
  IoT Jobs, and Fleet Indexing services.
- **Lifecycle management:** Handles the entire OTA
  workflow from creation to execution monitoring.

What MI OTA eliminates:

- Creating thing groups in AWS IoT Core.
- Adding things to groups.
- Creating IoT Jobs.

Managed integrations OTA handles all three operations internally based on your query string,
automatically discovering devices that match your criteria,
creating IoT Jobs under the hood, and orchestrating the
complete OTA workflow without requiring you to interact with multiple AWS services directly.
