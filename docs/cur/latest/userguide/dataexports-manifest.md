

# Data Exports manifest file reference

Data Exports delivers a `Manifest.json` metadata file with each export. The manifest describes the files that were delivered by a specific execution of the export. Use it to identify which data files to ingest and to read the schema of the export.

For more information about the S3 location of the manifest and when it's delivered, see [Understanding export delivery](dataexports-export-delivery.md).

## Manifest fields
<a name="dataexports-manifest-fields"></a>

The manifest is a JSON document with the following top-level fields.



| Field | Type | Description | 
| --- | --- | --- | 
| executionId | String | The ID of the export execution that delivered the files. This is the same value that appears in the delivery path when your export uses the create new report option. | 
| exportArn | String | The Amazon Resource Name (ARN) of the export that produced the files. | 
| columns | List of objects | The columns in the export data files. For the structure of each object, see [columns](#dataexports-manifest-columns). | 
| dataFiles | List of strings | The full S3 URIs of the export data files, in the format s3://<bucket-name>/<path>/<export-name>-<part-number>.<extension>. We recommend identifying which files to ingest by programmatically reading this list. | 
| additionalOutputFiles | List of objects | The additional files that are delivered if you have Athena or Amazon Redshift integration. For the structure of each object, see [additionalOutputFiles](#dataexports-manifest-additional-files). The list is empty if no additional files were delivered. | 
| additionalInfo | Object | Statistics about the export execution. For details, see [additionalInfo](#dataexports-manifest-additionalinfo). | 

## columns
<a name="dataexports-manifest-columns"></a>

Each object in the `columns` list describes one column in the export data files.



| Field | Type | Description | 
| --- | --- | --- | 
| name | String | The name of the column. | 
| type | String | The data type of the column. | 

## additionalOutputFiles
<a name="dataexports-manifest-additional-files"></a>

Each object in the `additionalOutputFiles` list describes one additional file that Data Exports delivered alongside the export data files.



| Field | Type | Description | 
| --- | --- | --- | 
| artifactType | String | The type of the additional file. | 
| name | String | The S3 key of the additional file. | 

## additionalInfo
<a name="dataexports-manifest-additionalinfo"></a>

The `additionalInfo` object contains statistics about the export execution.



| Field | Type | Description | 
| --- | --- | --- | 
| rowCount | Number | The number of line items in the result of the export's query. | 

## Example – Manifest.json file
<a name="dataexports-manifest-example"></a>

The following example shows a manifest for an export that delivered a single data file.

```json
{
  "executionId": "<execution-id>",
  "exportArn": "arn:aws:bcm-data-exports:us-east-1:111122223333:export/<export-id>",
  "columns": [
    {
      "name": "identity_line_item_id",
      "type": "string"
    },
    {
      "name": "bill_bill_type",
      "type": "string"
    }
  ],
  "dataFiles": [
    "s3://amzn-s3-demo-bucket/example-prefix/example-export/data/BILLING_PERIOD=2026-05/example-export-00001.snappy.parquet"
  ],
  "additionalOutputFiles": [],
  "additionalInfo": {
    "rowCount": 5695
  }
}
```