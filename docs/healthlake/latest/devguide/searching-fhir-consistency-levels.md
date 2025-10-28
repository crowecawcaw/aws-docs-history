# FHIR Search Consistency Levels

AWS HealthLake's search index operates on an Eventual Consistency model for `GET`
and `POST` with SEARCH operations. With eventual consistency, if there is a pending
search index update for a resource, the search results exclude version N-1 of the resource until
the index update completes.

AWS HealthLake now includes the ability to select how the consistency model will behave for updated
resources. Developers can include either 'Eventual Consistency', the default behavior described above
or 'Strong Consistency'. Strong Consistency will allow the N-1 version of the resource for resources
with pending search index updates to be included in the search results. This can be used for use case
scenarios where all resources are required in the result even when the search index update has not yet
completed. Customers can control this behavior using the `x-amz-fhir-history-consistency-level` request header.

## Consistency levels

Strong consistency

Set `x-amz-fhir-history-consistency-level: strong` to return all matching records, including those with pending search index updates. Use this option when you need to search for resources immediately after updates.

Eventual consistency

Set `x-amz-fhir-history-consistency-level: eventual` to return only records that have completed search index updates. This is the default behavior if no consistency level is specified.

## Usage example

1. When updating a resource:

```
POST <baseURL>/Patient
Content-Type: application/fhir+json
x-amz-fhir-history-consistency-level: strong

{
  "resourceType": "Patient",
  "id": "123",
  "meta": {
    "profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"]
  },
  "identifier": [
    {
      "system": "http://example.org/identifiers",
      "value": "123"
    }
  ],
  "active": true,
  "name": [
    {
      "family": "Smith",
      "given": ["John"]
    }
  ],
  "gender": "male",
  "birthDate": "1970-01-01"
}
```

2. Subsequent search:

```
GET <baseURL>/Patient?_id=123
```

## Best practices

- Use strong consistency when you need to immediately search for recently updated resources
- Use eventual consistency for general queries where immediate visibility isn't critical
- Consider the trade-off between immediate visibility and potential performance impact

###### Note

The consistency level setting affects how quickly updated resources appear in search results but does not impact the actual storage of the resources.

Setting the optional `x-amz-fhir-history-consistency-level` header to 'strong' doubles the write capacity consumption per resource.

This feature is only applicable for data stores that have version history enabled (all datastores created after Oct 25, 2024 have it enabled by default).
