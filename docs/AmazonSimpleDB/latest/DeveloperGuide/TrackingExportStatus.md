

# Track Export Status
<a name="TrackingExportStatus"></a>

 After starting an export, you can track its progress using the `get-export` command with the export ARN returned by `start-domain-export`: 

```
aws simpledbv2 get-export \
		    --export-arn 'arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/3eb4eaed-872b-4e08-b4b6-ff6999a83e01'
```

 The command returns detailed information about the export as shown in the following example: 

```
{
		    "exportArn": "arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/3eb4eaed-872b-4e08-b4b6-ff6999a83e01",
		    "clientToken": "ad9ac782-954a-45d1-8d47-8ef843c0ffe2",
		    "exportStatus": "IN_PROGRESS",
		    "domainName": "myDomain",
		    "requestedAt": "2025-06-03T10:05:47.757000+00:00",
		    "s3Bucket": "my-export-bucket",
		    "s3BucketOwner": "111122223333",
		    "exportDataCutoffTime": "2025-06-03T10:05:47.757000+00:00"
		}
```

## Export Status Values
<a name="ExportStatusValues"></a>

 The `exportStatus` field indicates the current state of the export: 

PENDING  
 The export request has been received and is queued for processing. 

IN\_PROGRESS  
 The export is actively being processed and data is being written to Amazon S3. 

SUCCEEDED  
 The export completed successfully and all data has been written to Amazon S3. 

FAILED  
 The export encountered an error. The response includes `failureCode` and `failureMessage` fields with details about the failure. 

## Amazon S3 File Structure During Export
<a name="S3FileStructure"></a>

 As the export progresses, Amazon SimpleDB writes files to your Amazon S3 bucket in the following order: 

1.  An empty `_started` file is created first to verify that the bucket is writable. 

1.  Data files are written to the `data/` directory with names in the format `dataFile<randomPartitionIds>.json`. 

1.  When the export completes successfully, manifest files (`manifest-file.json` and `manifest-summary.json`) are written to the export directory. 

## Understanding `exportDataCutoffTime`
<a name="ExportDataCutoffTime"></a>

 The `exportDataCutoffTime` field indicates the timestamp used to determine which data is included in the export. It is important to understand that Amazon SimpleDB exports are not point-in-time snapshots. 
+  All items inserted **before** this timestamp are included in the export. 
+  Items inserted **after** this timestamp are not included in the export. 
+  For existing items, updates or deletions that occur after the cutoff time may not be reflected in the exported data. 
+  The timestamp represents when domain processing begins, not when the export request was received. 

 If you perform multiple exports over time, you may need to implement deduplication logic when processing the exported data to handle items that appear in multiple exports. 