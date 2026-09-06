

# List Exports in an Account
<a name="ListingExports"></a>

 You can list all exports in your AWS account using the `list-exports` command: 

```
aws simpledbv2 list-exports
```

 The command returns a list of export summaries: 

```
{
  "exportSummaries": [
    {
      "exportArn": "arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/3677e7cd-ca7a-47e2-9d24-2b86115503a6",
      "exportStatus": "SUCCEEDED",
      "requestedAt": "2026-02-03T13:32:04.394000+00:00",
      "domainName": "myDomain"
    },
    {
      "exportArn": "arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/2890f3b6-a683-4277-adb6-c76a9b434b75",
      "exportStatus": "FAILED",
      "requestedAt": "2026-02-03T13:38:00.347000+00:00",
      "domainName": "myDomain"
    },
    {
      "exportArn": "arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/6f7ed325-e8cc-4ffe-aa56-b4f6fa8a0fc5",
      "exportStatus": "SUCCEEDED",
      "requestedAt": "2026-02-06T11:57:09.953000+00:00",
      "domainName": "myDomain"
    }
  ]
}
```

## Filtering and Pagination
<a name="FilteringAndPagination"></a>

 You can filter the list of exports by domain name: 

```
aws simpledbv2 list-exports \
		    --domain-name 'myDomain'
```

 To limit the number of results returned, use the `--max-results` parameter: 

```
aws simpledbv2 list-exports \
		    --max-results 10
```

 If there are more results available, the response includes a `nextToken` field. Use this token in a subsequent request to retrieve the next page of results: 

```
aws simpledbv2 list-exports \
		    --next-token 'AQICAHjER8iQpbgPvrZjCyvsE2xN8rcQnvjivIKJidDDXMn1vQ...'
```

## Data Retention
<a name="DataRetention"></a>

 The `list-exports` command returns information about exports created within the past 3 months. Older export metadata is automatically removed from the system, although the exported data files remain in your Amazon S3 bucket until you delete them. 

## Understanding Exported Data in Amazon S3
<a name="UnderstandingExportedData"></a>

 When an export completes successfully, Amazon SimpleDB creates a structured directory in your Amazon S3 bucket containing the exported data and metadata files. 

### Directory Structure
<a name="DirectoryStructure"></a>

 The exported data is organized in the following directory structure: 

```
AWSSimpleDB/<exportId>/<domainName>/
		├── _started
		├── data/
		│   ├── dataFile_1_2.json
		│   ├── dataFile_3_4.json
		│   └── ...
		├── manifest-file.json
		└── manifest-summary.json
```

\_started  
 An empty marker file created at the beginning of the export to verify bucket write access. 

data/  
 Directory containing one or more JSON files with the exported domain data. File names include random partition identifiers. 

manifest-file.json  
 Metadata file listing all data files with their MD5 checksums and item counts. 

manifest-summary.json  
 Summary file containing export metadata and total item count. 

### Data File Format
<a name="DataFileFormat"></a>

 Each data file in the `data/` directory contains an array of JSON objects, where each object represents a Amazon SimpleDB item. The following example shows the structure: 

```
[
		    {
		        "itemName": "employee1",
		        "attributes": [
		            {"name": "first_name", "values": ["John"]},
		            {"name": "last_name", "values": ["Doe"]},
		            {"name": "department", "values": ["IT"]},
		            {"name": "age", "values": ["30"]}
		        ]
		    },
		    {
		        "itemName": "employee2",
		        "attributes": [
		            {"name": "first_name", "values": ["Jane"]},
		            {"name": "last_name", "values": ["Smith"]},
		            {"name": "department", "values": ["HR"]},
		            {"name": "reportees", "values": ["Jade", "Judith"]}
		        ]
		    }
		]
```

 Each item object contains: 
+  `itemName` – The unique identifier for the item in the domain 
+  `attributes` – An array of attribute objects, each containing: 
  +  `name` – The attribute name 
  +  `values` – An array of values (supporting multi-value attributes) 

 For more information about the Amazon SimpleDB data model, see [Data Model](DataModel.md). 

### Manifest Files
<a name="ManifestFiles"></a>

 The manifest files provide metadata about the export and enable data integrity verification. 

#### manifest-file.json
<a name="ManifestFile"></a>

 This file lists all data files in the export with their checksums: 

```
[
		    {
		        "md5Checksum": "ccc3dIp/7887Xhl7+DaEBQ==",
		        "dataFileS3Key": "AWSSimpleDB/3eb4eaed-872b-4e08-b4b6-ff6999a83e01/myDomain/data/dataFile_1_2.json",
		        "dataFileItemCount": 500
		    },
		    {
		        "md5Checksum": "xyz9aKl/3456Pqr8+EbFCR==",
		        "dataFileS3Key": "AWSSimpleDB/3eb4eaed-872b-4e08-b4b6-ff6999a83e01/myDomain/data/dataFile_3_4.json",
		        "dataFileItemCount": 500
		    }
		]
```

 Use the MD5 checksums to verify the integrity of each data file after download. 

#### manifest-summary.json
<a name="ManifestSummary"></a>

 This file provides a summary of the entire export: 

```
{
    "version":"2025-11-01",
    "exportArn":"arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/a49f3ffd-4b7e-4720-8f5d-f4536313aaf5",
    "requestedAt":"2026-02-16T16:56:43.659Z",
    "s3BucketName":"myBucket",
    "s3ExportPrefix":"AWSSimpleDB/a49f3ffd-4b7e-4720-8f5d-f4536313aaf5/myDomain",
    "domainName":"myDomain",
    "itemsCount":4650,
    "exportDataCutoffTime":"2026-02-16T16:58:35.009Z",
    "s3SseAlgorithm":null,
    "s3SseKmsKeyId":null,
    "s3BucketOwner":"111122223333"
}
```

 Use the `totalItemCount` to verify that all items were exported successfully. 