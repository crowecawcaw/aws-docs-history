

# Schema type mapping
<a name="msk-data-delivery-iceberg-schema-mapping"></a>

When you register a schema in the AWS Glue Schema Registry, the Channel maps the JSON Schema types to Iceberg column types as follows.


| JSON Schema type | Condition | Iceberg column type | 
| --- | --- | --- | 
| `string` | (plain) | `string` | 
| `string` | `format: "date-time"` | `timestamptz` | 
| `string` | `format: "date"` | `date` | 
| `string` | `format: "time"` | `time` | 
| `string` | `format: "uuid"` | `uuid` | 
| `string` | `format: "byte"` or `contentEncoding: "base64"` | `binary` | 
| `integer` | fits in 32-bit range | `int` | 
| `integer` | exceeds 32-bit range | `long` | 
| `number` | with `multipleOf` (for example, `0.001`) | `decimal(38, scale)` | 
| `number` | plain floating point | `double` | 
| `boolean` | — | `boolean` | 
| `object` | with named properties | `struct` | 
| `object` | with `additionalProperties` | `map<string, value_type>` | 
| `array` | — | `list<element_type>` | 
| `enum` | — | `string` | 

**Required columns** — A column is marked required (non-nullable) when it appears in the `"required"` array of the parent object in your JSON Schema.

**Partition key column** — Your table must include a `timestamptz` column that can be used for time-based partitioning (hour). The source column referenced by the partition is automatically treated as required, even if your schema does not list it in the `"required"` array. You can enable an S3 Tables record-expiration job based on the table's partition column — see [Managing S3 Tables record expiration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-record-expiration.html).

The Channel handles source fields as follows:
+ **Extra fields in source data** — Fields present in your source records but not defined in the table schema are silently dropped; they are not written to the Iceberg table.
+ **Missing optional fields** — If a source record omits a field defined as optional in the table schema, the column is written as `null`.
+ **Missing required fields** — If a source record omits a field defined as required, the record fails validation and is sent to the dead-letter queue (DLQ) with an error indicating the missing required field.
+ **Nesting limit** — Schemas with more than 16 levels of nesting are not supported.