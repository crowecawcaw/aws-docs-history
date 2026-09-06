

# S3 output key template for Amazon S3 delivery
<a name="data-delivery-s3-key-template"></a>

 When delivering to general purpose Amazon S3 buckets, you can configure an S3 output key template to control the object key structure of delivered files. The key template is optional – if not specified, Amazon S3 delivery uses the default template. 

## Default template
<a name="data-delivery-s3-key-template-default"></a>

 If you do not specify a custom key template, Amazon S3 delivery uses the following default: 

```
kinesis-channel/!{channel-name}/!{channel-id}/!{yyyy}/!{MM}/!{dd}/!{HH}/!{channel-name}-!{channel-id}-!{yyyy}-!{MM}-!{dd}-!{HH}-!{mm}!{extension}
```

 The portion before the last forward slash (`/`) forms the object key prefix (the folder structure), and the last segment forms the object name. The default template organizes delivered objects by channel and by hour, and repeats the same values in the object name so that each object is self-describing. Amazon Kinesis Data Streams automatically appends a unique suffix to every object key, so object keys are unique even when the template does not include a time component fine enough to distinguish them. 

## Template variables
<a name="data-delivery-s3-key-template-variables"></a>

 The following variables are available for use in your key template: 


**S3 key template variables**  

| Variable | Description | Example value | 
| --- | --- | --- | 
| \!{channel-name} | The name of the delivery. | my-channel | 
| \!{channel-id} | The unique identifier of the delivery. | abc123def456 | 
| \!{stream-name} | The name of the source Kinesis Data Streams stream. | my-stream | 
| \!{yyyy} | Four-digit year (UTC). | 2026 | 
| \!{yy} | Two-digit year (UTC). | 26 | 
| \!{MM} | Two-digit month (UTC), zero-padded. | 07 | 
| \!{dd} | Two-digit day of month (UTC), zero-padded. | 20 | 
| \!{HH} | Two-digit hour (UTC, 24-hour), zero-padded. | 14 | 
| \!{mm} | Two-digit minute (UTC), zero-padded. | 30 | 
| \!{extension} | A file extension derived from the configured compression type (for example, .gz for GZIP or .zst for ZSTD). If present, it must appear at the end of the template. | .gz | 
| \!{extension:.{{literal}}} | A literal file extension that you specify. Must start with a period and contain only lowercase letters and periods. If present, it must appear at the end of the template. | \!{extension:.json} | 

## Template rules
<a name="data-delivery-s3-key-template-rules"></a>

 Key templates must conform to the following rules: 
+ After all variables are expanded, the resulting object key must not exceed the Amazon S3 object key limit of 1,024 characters. Because Amazon Kinesis Data Streams appends a unique suffix of up to 38 characters, the expanded template itself must not exceed 986 characters.
+ Must not contain path traversal: no consecutive periods (`..`), no period-only path segment (`.`), and must not start with a forward slash (`/`).
+ Must not contain consecutive slashes (`//`).
+ Every variable placeholder must be closed (each `!{` must have a matching `}`) and must use a supported variable name.
+ Allowed literal characters are alphanumeric characters and the following: `! - _ ' . * ( ) / =`. The `=` character lets you express Hive-style partitioning, such as `year=!{yyyy}/month=!{MM}/`.
+ The template can contain at most one extension placeholder (`!{extension}` or `!{extension:.{{literal}}}`), and if present it must appear at the end of the template.
+ When compression (GZIP or ZSTD) is enabled, the template must include an extension placeholder.

**Note**  
 You do not need to include a uniqueness variable in the template. Amazon Kinesis Data Streams automatically appends a unique suffix to each delivered object key. 

## Valid and invalid examples
<a name="data-delivery-s3-key-template-examples"></a>


**Key template examples**  

| Template | Valid | Reason | 
| --- | --- | --- | 
| \!{channel-name}/\!{yyyy}/\!{MM}/\!{dd}/\!{HH}/records\!{extension} | Yes | Uses supported variables and ends with a single extension placeholder. | 
| data/stream=\!{stream-name}/\!{yyyy}-\!{MM}-\!{dd}/\!{HH}\!{mm}\!{extension:.json} | Yes | Hive-style partitioning with a literal extension at the end. | 
| \!{channel-name}/\!{channel-id} | Yes | Minimal template. Kinesis Data Streams appends a unique suffix automatically. | 
| /data/\!{channel-name}\!{extension} | No | Starts with a forward slash. | 
| data/../\!{channel-name}\!{extension} | No | Contains path traversal (..). | 
| data//\!{channel-name}\!{extension} | No | Contains consecutive slashes (//). | 
| \!{channel-name}\!{extension}/\!{yyyy} | No | The extension placeholder is not at the end of the template. | 
| data/\!{partition-id}\!{extension} | No | \!{partition-id} is not a supported variable. | 
| data/\!{channel-name} (with GZIP or ZSTD compression) | No | Compression is enabled but the template has no extension placeholder. | 
| data/\!{channel-name}/\!{yyyy} (missing closing brace) | No | Unclosed variable placeholder. | 