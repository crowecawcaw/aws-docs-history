Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").
 

# Schemas

With Amazon Cloud Directory, schemas define what types of objects can be created within a directory
 (users, devices, and organizations), enforce validation of data for each object class, and
 handle changes to the schema over time. More specifically, a schema defines the
 following:


* One or more types of facets that may be mapped to objects within a directory (such as
 Person, Organization\_Person)
* Attributes that may be mapped to objects within a directory (such as Name, Description).
 Attributes can be required or made optional on various types of facets, and are defined
 within the context of a facet.
* Constraints that may be enforced on object attributes (such as Required, Integer,
 String)
When a schema has been applied to a directory, all data within that directory must then
 conform to that applied schema. In this way, the schema definition is essentially a blueprint
 that can be used to construct multiple directories with applied schemas. Once built, those
 applied schemas may vary from the original blueprint, each in different ways.
 

Applied schemas can later be updated using versioning and then reapplied to all the
 directories that use it. For more information, see [In-Place Schema Upgrade](schemas_inplaceschemaupgrade.md "schemas_inplaceschemaupgrade.md").

Cloud Directory provides API operations to create, read, update, and delete schemas. This allows the
 contents of the schema to be easily consumed by programmatic agents. Such agents access the
 directory to discover the full set of facets, attributes, and constraints that apply to data
 within the directory. For more information about the schema APIs, see the [Amazon Cloud Directory API
 Reference Guide](../APIReference/welcome.md "../APIReference/welcome.md").

Cloud Directory supports uploading a compliant JSON file for schema creation. You can also create and
 manage schemas using the AWS Directory Service console. For more information, see [Create an Amazon Cloud Directory](getting_started_create_directory.md "getting_started_create_directory.md").

###### Topics

* [Schema Lifecycle](schemas_lifecycle.md "schemas_lifecycle.md")
* [Facets](schemas_whatarefacets.md "schemas_whatarefacets.md")
* [In-Place Schema Upgrade](schemas_inplaceschemaupgrade.md "schemas_inplaceschemaupgrade.md")
* [Managed Schema](schemas_managed.md "schemas_managed.md")
* [Sample Schemas](schemas_sampleschemastopic.md "schemas_sampleschemastopic.md")
* [Custom Schemas](schemas_customschematopic.md "schemas_customschematopic.md")
* [Attribute References](schemas_attributereferences.md "schemas_attributereferences.md")
* [Attribute Rules](schemas_attributerules.md "schemas_attributerules.md")
* [Format Specification](schemas_jsonformat.md "schemas_jsonformat.md")
