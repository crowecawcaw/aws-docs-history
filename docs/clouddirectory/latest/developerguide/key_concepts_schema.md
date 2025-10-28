Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Schema

A schema is a collection of facets that define what objects can be created in a directory
and how they are organized. A schema also enforces data integrity and interoperability. A
single schema can be applied to more than one directory at a time. For more information, see
[Schemas](schemas.md "schemas.md").

## Facets

A facet is a collection of attributes, constraints, and links defined within a schema.
Combined together, facets define the objects in a directory. For example, Person and Device
can be facets to define corporate employees with association of multiple devices. For more
information, see [Facets](schemas_whatarefacets.md "schemas_whatarefacets.md").

## Managed Schemas

A schema provided to make it easier to quickly develop and maintain your applications.
For more information, see [Managed Schema](schemas_managed.md "schemas_managed.md").

## Sample Schemas

The set of sample schemas provided by default in the AWS Directory Service console. For
example, Person, Organization, and Device are all sample schemas. For more information, see
[Sample Schemas](schemas_sampleschemastopic.md "schemas_sampleschemastopic.md").

## Custom Schemas

One or more schemas defined by a user that can be uploaded from the Schemas section or
during the Cloud Directory creation process of the AWS Directory Service console, or created
by API calls.
