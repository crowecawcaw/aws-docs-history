

# S3 Metadata annotation table schema
<a name="metadata-tables-annotation-schema"></a>

The annotation table tracks the latest annotations on the objects in your general purpose bucket. Each row represents one annotation on a specific object version. You can use the annotation table to discover and retrieve objects based on annotation content. For example, you can query the annotation table to find all objects with a specific annotation, retrieve annotation content that matches a predicate based on object size or key prefix, or correlate annotations across objects.

When you enable the annotation table for your metadata table configuration, the table goes through a process known as *backfilling*, during which Amazon S3 scans your general purpose bucket to retrieve the annotation data for all objects. Depending on the number of objects in your bucket, this process can take minutes to hours. When backfilling is finished, the status changes from **Backfilling** to **Active**.

**Note**  
You're charged for backfilling your annotation table. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

Annotation tables have the following schema:


| Column name | Required? | Data type | Description | 
| --- | --- | --- | --- | 
| `bucket` | Yes | String | The name of the general purpose bucket. | 
| `object_key` | Yes | String | The object key name (or key) that uniquely identifies the object in the bucket. | 
| `object_version_id` | No | String | The object's version ID. | 
| `object_join_key` | Yes | String | A unique identifier for the object, assigned with each new version, or when the null version is created or overwritten. Use this column to join with the inventory or journal tables. | 
| `name` | Yes | String | The annotation name. | 
| `sequence_number` | Yes | String | An ordinal value for sorting annotation revisions. For a given bucket, `object_key`, and `object_version_id`, a lexicographically larger `sequence_number` implies the record was introduced more recently. | 
| `last_modified_date` | No | Timestamp NTZ (no time zone) | The date and time when the annotation was last modified. | 
| `size` | No | Long | The size of the annotation payload in bytes. | 
| `e_tag` | No | String | The ETag of the annotation content. | 
| `checksum_algorithm` | No | String | The checksum algorithm used for the annotation. If no checksum is present, this value is null. | 
| `replication_status` | No | String | The replication status of the annotation. `PENDING`, `COMPLETED`, and `FAILED` are visible only at the replication source. `REPLICA` is visible only at the replication destination. If there is no applicable replication configuration, this value is null. | 
| `text_value` | No | String | The annotation content (UTF-8 text). | 