# ID namespaces in AWS Clean Rooms

An _ID namespace_ is a wrapper around your identity table
that enables you to provide metadata explaining your dataset and how to use it in an ID mapping
workflow. An _ID mapping workflow_ is a data processing job
that maps data from an input data source to an input data target based on the specified ID
mapping method. It produces an ID mapping table.

There are two types of ID namespaces: **Source** and
**Target**. The **Source** contains configurations for the
source data that will be processed in an ID mapping workflow. The **Target**
contains a configuration of the target data which all sources will resolve to. To deﬁne the
input data that you want to resolve across two AWS accounts, create an ID namespace source and
an ID namespace target to translate your data from one set (**Source**) to
another (**Target**).

You can either create a new ID namespace or you can associate an existing one. For more
information about how to create an ID namespace in AWS Entity Resolution, see [Define input
data using an ID namespace](../../../entityresolution/latest/userguide/id-namespace.md "../../../entityresolution/latest/userguide/id-namespace.md") in the _AWS Entity Resolution User
Guide_.

###### Topics

- [Creating and associating a new ID namespace](create-new-id-namespace.md "create-new-id-namespace.md")
- [Associating an existing ID namespace](associate-existing-id-namespace.md "associate-existing-id-namespace.md")
- [Editing ID namespace associations](edit-id-namespace-association.md "edit-id-namespace-association.md")
- [Disassociating ID namespace
  associations](disassociate-id-namespace-association.md "disassociate-id-namespace-association.md")
