# Managing data stores with AWS HealthLake

With AWS HealthLake, you create and manage data stores for FHIR R4 resources. When you create a
HealthLake data store, a FHIR data respository is made available via a RESTful API [endpoint](reference-healthlake-endpoints-quotas.md#reference-healthlake-endpoints "reference-healthlake-endpoints-quotas.md#reference-healthlake-endpoints"). You can choose to import (preload)
Synthea open source FHIR R4 health data into your data store when you create it. For more
information, see [Preloaded data
types](reference-healthlake-preloaded-data-types.md "reference-healthlake-preloaded-data-types.md").

###### Important

HealthLake supports two types of FHIR data store authorization strategies, AWS SigV4 or
SMART on FHIR. You must choose one of the authorization strategies prior to creating a HealthLake
FHIR data store. For more information, see [Data store authorization
strategy](getting-started-concepts.md#concept-data-store-authorization-strategy "getting-started-concepts.md#concept-data-store-authorization-strategy").

To find the FHIR-related capabilities (behaviors) of an active HealthLake data store, retrieve
its [Capability Statement](reference-fhir-capability-statement.md "reference-fhir-capability-statement.md").

The following topics describe how to use HealthLake cloud native actions to create, describe,
list, tag, and delete FHIR data stores using the AWS CLI, AWS SDKs, and AWS Management Console.

###### Topics

- [Creating a data store](managing-data-stores-create.md "managing-data-stores-create.md")
- [Getting data store
  properties](managing-data-stores-describe.md "managing-data-stores-describe.md")
- [Listing data stores](managing-data-stores-list.md "managing-data-stores-list.md")
- [Tagging data stores](managing-data-stores-tagging.md "managing-data-stores-tagging.md")
- [Deleting a data store](managing-data-stores-delete.md "managing-data-stores-delete.md")
