# ID mapping tables in AWS Clean Rooms

An _ID mapping table_ is a resource in AWS Clean Rooms that enables
multiparty identity mapping in a collaboration.

Before you create an ID mapping table, you must first have both source and target data
configured as ID namespaces.

After you create an ID mapping table, you use an ID mapping workﬂow to translate the source
ID namespace to the target ID namespace. You can do this using either a rule-based method, or a
provider service transcoding method.

An _ID mapping workflow_ is a data processing job that maps
data from an input data source to an input data target based on the specified ID mapping
workflow method. This workflow populates an ID mapping table.

###### Note

ID mapping tables can only be created from datasets that are stored in Amazon S3 and crawled
into AWS Glue tables.

There are two ID mapping workflow methods: rule-based ID mapping or provider services ID
mapping:

- Rule-based ID mapping – You use matching rules to translate first-party data from
  a source to a target.
- Provider services ID mapping – You use the LiveRamp provider service to translate
  third-party data from a source to a target.

###### Note

The currently supported transcoding service provider is LiveRamp. Any member in the
collaboration who has an subscription with LiveRamp through AWS Data Exchange can create the ID
mapping table. If you already have a subscription to LiveRamp, but not through AWS Data Exchange,
contact LiveRamp to get a private offer. For more information, see [Subscribe to a provider service on AWS Data Exchange](../../../entityresolution/latest/userguide/setting-up.md#subscribe-provider-service "../../../entityresolution/latest/userguide/setting-up.md#subscribe-provider-service") in the _AWS Entity Resolution
User Guide_.

###### Topics

- [Creating and populating a new ID mapping
  table](create-id-mapping-table.md "create-id-mapping-table.md")
- [Populating an existing ID mapping table](populate-id-mapping-table.md "populate-id-mapping-table.md")
- [Editing an ID mapping table](edit-id-mapping-table.md "edit-id-mapping-table.md")
- [Deleting an ID mapping table](delete-id-mapping-table.md "delete-id-mapping-table.md")
