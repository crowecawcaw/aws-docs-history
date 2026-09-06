

# Export a domain to Amazon S3
<a name="HowToExportDomainToS3"></a>

 After completing the prerequisites, you can start exporting a domain using the `start-domain-export` command. The following example shows a basic export operation: 

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333'
```

 The command returns information about the export request: 

```
{
		    "clientToken": "ad9ac782-954a-45d1-8d47-8ef843c0ffe2",
		    "exportArn": "arn:aws::sdb:us-east-1:111122223333:domain/myDomain/export/3eb4eaed-872b-4e08-b4b6-ff6999a83e01",
		    "requestedAt": "2025-07-04T09:51:56.064000+00:00"
		}
```

 The `exportArn` uniquely identifies the export and is used to track its status and retrieve information about the export. 