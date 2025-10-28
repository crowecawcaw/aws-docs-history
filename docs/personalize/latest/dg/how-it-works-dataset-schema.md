# Creating schema JSON files for Amazon Personalize schemas

After you [prepare your data](preparing-training-data.md "preparing-training-data.md"), you are ready to create schema JSON files for each type of data that you are importing.
These files outline the structure and content of your data, including column names and their data types.

You use schema JSON files when you create
an Amazon Personalize schema in [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"). In Amazon Personalize, a _schema_ is a resource that
allows Amazon Personalize to parse the data when you import it into your dataset. You create a schema for each dataset you
are using.

For custom resources, each dataset has specific schema requirements. For Domain dataset groups, the domain you choose determines your dataset and schema requirements.
Each domain has a default schema for each dataset type. When you create a dataset, you can either use the existing domain schema or
create a new one by modifying the existing default schema. Use the default schema as a guide for what data to import for your domain.

The following sections provide custom and domain requirements for creating a schema JSON file for each dataset type.

###### Topics

- [Schema formatting requirements](#general-schema-requirements "#general-schema-requirements")
- [VIDEO_ON_DEMAND datasets and
  schemas](VIDEO-ON-DEMAND-datasets-and-schemas.md "VIDEO-ON-DEMAND-datasets-and-schemas.md")
- [ECOMMERCE datasets and schemas](ECOMMERCE-datasets-and-schemas.md "ECOMMERCE-datasets-and-schemas.md")
- [Custom datasets and
  schemas](custom-datasets-and-schemas.md "custom-datasets-and-schemas.md")

## Schema formatting requirements

When you create a schema for a dataset in a Domain dataset group or Custom dataset group, you must follow these guidelines:

- You must define the schema in
  [Avro format](https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html "https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html").
  For information on the Avro data types we support, see
  [Schema data types](#personalize-datatypes "#personalize-datatypes").
- A schema has a name key whose value must match
  the dataset type.
- The schema fields can appear in any order, but they must match the order of the
  corresponding column headers in your CSV file.
- Schemas must be flat JSON files without nested structures. For example, a field cannot be
  the parent of multiple sub-fields.
- Amazon Personalize schemas don't support complex types such as arrays and maps.
- Schema fields must have unique alphanumeric names. For example,
  you can't add both a `GENRES_FIELD_1` field and a `GENRESFIELD1` field.
- You must define required fields as their required data types. Reserved categorical string fields must have the
  `categorical` attribute set to `true`, while reserved string fields can't be categorical. The keywords can't be in your data.
- If you add your own metadata field of type `string` and you want Amazon Personalize to use it when training,
  it must include the `categorical` attribute or the
  `textual` attribute (only Items schemas support fields
  with the textual attribute).
- Amazon Personalize doesn't use `boolean` type data when training or filtering recommendations. To have Amazon Personalize use boolean data when training or filtering,
  use a field of type _String_ and use the values `"True"` and `"False"`
  in your data. Or you can use type _int_ or _long_ and values `0` and `1`.
- Textual fields must be of the type `string` and must have the `textual` attribute set to `true`. For more information about
  unstructured text data, see [Unstructured text metadata](items-datasets.md#text-data "items-datasets.md#text-data").

Domain dataset group datasets have additional requirements based on both domain and dataset type.
Custom dataset group datasets have additional requirements depending on type.

### Schema data types

Amazon Personalize schemas support the following Avro types for fields:

- float
- double
- int
- long
- string
- boolean
- null

Some required and reserved fields support null data. Adding a `null` type to a field allows you to use imperfect data (for example, metadata with blank values) to generate recommendations.
For information about which fields support null data, see the schema requirements topic for your domain: [VIDEO_ON_DEMAND datasets and
schemas](VIDEO-ON-DEMAND-datasets-and-schemas.md "VIDEO-ON-DEMAND-datasets-and-schemas.md"),
[ECOMMERCE datasets and schemas](ECOMMERCE-datasets-and-schemas.md "ECOMMERCE-datasets-and-schemas.md"), or [Custom datasets and
schemas](custom-datasets-and-schemas.md "custom-datasets-and-schemas.md").
The following example shows how to add a null type for a GENDER field.

```
{
  "name": "GENDER",
  "type": [
    "null",
    "string"
  ],
  "categorical": true
}
```
