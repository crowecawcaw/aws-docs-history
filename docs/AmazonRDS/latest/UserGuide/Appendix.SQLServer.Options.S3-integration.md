# Transferring files between RDS for SQL Server and Amazon S3

You can use Amazon RDS stored procedures to download and upload files between Amazon S3 and your RDS DB instance. You can also use Amazon RDS
stored procedures to list and delete files on the RDS instance.

The files that you download from and upload to S3 are stored in the `D:\S3` folder. This is the only folder that you can
use to access your files. You can organize your files into subfolders, which are created for you when you include the
destination folder during download.

Some of the stored procedures require that you provide an Amazon Resource Name (ARN) to your S3 bucket and file. The format for your
ARN is `arn:aws:s3:::`amzn-s3-demo-bucket`/file_name`. Amazon S3 doesn't require an account number or AWS Region in ARNs.

S3 integration tasks run sequentially and share the same queue as native backup and restore
tasks. At maximum, you can have only two tasks in progress at any time in this queue. It
can take up to five minutes for the task to begin processing.

## Downloading files

from an Amazon S3 bucket to a SQL Server DB instance

To download files from an S3 bucket to an RDS for SQL Server DB instance, use the Amazon RDS stored
procedure `msdb.dbo.rds_download_from_s3` with the following
parameters.

| Parameter name    | Data type | Default | Required | Description                                                                                                                                                                                                                 |
| ----------------- | --------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@s3_arn_of_file` | NVARCHAR  | –       | Required | The S3 ARN of the file to download, for example:<br>`arn:aws:s3:::`amzn-s3-demo-bucket`/mydata.csv`                                                                                                                         |
| `@rds_file_path`  | NVARCHAR  | –       | Optional | The file path for the RDS instance. If not specified, the file path is<br>`D:\S3\`<filename in s3>``. RDS<br>supports absolute paths and relative paths. If you want to create a<br>subfolder, include it in the file path. |
| `@overwrite_file` | INT       | 0       | Optional | Overwrite the existing file:<br>0 = Don't overwrite<br>1 = Overwrite                                                                                                                                                        |

You can download files without a file extension and files with the following file
extensions: .bcp, .csv, .dat, .fmt, .info, .lst, .tbl, .txt, and .xml.

###### Note

Files with the .ispac file extension are supported for download when SQL Server
Integration Services is enabled. For more information on enabling SSIS, see
[SQL Server Integration Services](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").

Files with the following file extensions are supported for download when SQL Server
Analysis Services is enabled: .abf, .asdatabase, .configsettings,
.deploymentoptions, .deploymenttargets, and .xmla. For more information on
enabling SSAS, see [SQL Server Analysis Services](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").

The following example shows the stored procedure to download files from S3.

```
exec msdb.dbo.rds_download_from_s3
	    @s3_arn_of_file='arn:aws:s3:::`amzn-s3-demo-bucket`/`bulk_data.csv`',
	    @rds_file_path='D:\S3\`seed_data\data.csv`',
	    @overwrite_file=`1`;
```

The example `rds_download_from_s3` operation creates a folder named
`seed_data` in `D:\S3\`, if the folder doesn't exist yet.
Then the example downloads the source file `bulk_data.csv` from S3 to a
new file named `data.csv` on the DB instance. If the file previously
existed, it's overwritten because the `@overwrite_file` parameter is set
to `1`.

## Uploading files from a

SQL Server DB instance to an Amazon S3 bucket

To upload files from an RDS for SQL Server DB instance to an S3 bucket, use the Amazon RDS stored
procedure `msdb.dbo.rds_upload_to_s3` with the following
parameters.

| Parameter name    | Data type | Default | Required | Description                                                                                                 |
| ----------------- | --------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| `@s3_arn_of_file` | NVARCHAR  | –       | Required | The S3 ARN of the file to be created in S3, for example:<br>`arn:aws:s3:::`amzn-s3-demo-bucket`/mydata.csv` |
| `@rds_file_path`  | NVARCHAR  | –       | Required | The file path of the file to upload to S3. Absolute and relative paths are<br>supported.                    |
| `@overwrite_file` | INT       | –       | Optional | Overwrite the existing file:<br>0 = Don't overwrite<br>1 = Overwrite                                        |

The following example uploads the file named `data.csv` from the specified
location in `D:\S3\seed_data\` to a file `new_data.csv` in the
S3 bucket specified by the ARN.

```
exec msdb.dbo.rds_upload_to_s3
		@rds_file_path='D:\S3\`seed_data\data.csv`',
		@s3_arn_of_file='arn:aws:s3:::`amzn-s3-demo-bucket`/`new_data.csv`',
		@overwrite_file=`1`;
```

If the file previously existed in S3, it's overwritten because the @overwrite_file
parameter is set to `1`.
