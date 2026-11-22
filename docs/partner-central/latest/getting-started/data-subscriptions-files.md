

# Understanding the delivered files

AWS Partner Central writes everything under the `AWSDataSubscriptions/` prefix of your bucket. Each delivered file has the following key, where `{{account-id}}` is your AWS account ID, `{{dataset}}` is the folder from [Available datasets](data-subscriptions-datasets.md), and the date is the delivery day in UTC:

```
AWSDataSubscriptions/{{account-id}}/{{dataset}}/{{yyyy}}/{{MM}}/{{dd}}/{{file}}
```

The key includes the following segments:
+ `{{account-id}}` – Your AWS account ID.
+ `{{dataset}}` – The folder name for the subscribed dataset.
+ `{{yyyy/MM/dd}}` – The delivery date in UTC.
+ `{{file}}` – The delivered file name.

The following folder structure shows a bucket that receives the ACE Leads dataset.

```
AWSDataSubscriptions/
    access-check.json
    111122223333/
        leads/
            2026/11/19/
                20261119063015_0000_part_00.parquet
                20261119063015_0001_part_00.parquet
                20261119151414_0000_part_00.parquet
                _SUCCESS
            2026/11/20/
                _SUCCESS
```

Keep the following points in mind about the delivered files:
+ There is one folder for each delivery day. A day folder can contain several files.
+ File names start with a 14-digit identifier of the delivery run. The rest of the name can vary. Use the `_SUCCESS` file to find a day's files.
+ Files are never changed after delivery. Corrections arrive as new rows in a later file or on a later day.
+ Rows are change records. Each row has a `row_type` column with the value `INSERT`, `UPDATE`, or `DELETE`, a `row_modified_date` column with the UTC time of the change, and a key column (marked in the dataset tables). Apply the rows to your copy of the data by key, in order of `row_modified_date`. A row can be delivered more than once. Applying the same row again has no effect.
+ `AWSDataSubscriptions/access-check.json` is an empty test file that AWS Partner Central writes when you create a subscription. You can ignore it or expire it with a lifecycle rule. If you add a rule, scope it to that file so that it doesn't expire your delivered files.

## The \_SUCCESS file
<a name="data-subscriptions-confidence-file"></a>

When a delivery day is complete, AWS Partner Central writes one `_SUCCESS` file into the day folder, after every data file of the day. Read a day folder only after its `_SUCCESS` file exists. The leading underscore makes Amazon Athena, Apache Spark, and Apache Hive treat the file as hidden, so a table that points at the dataset folder doesn't read it as data.

The file is a JSON object that lists the files of the day. The following example shows a day with three files.

```json
{
    "schemaVersion": 1,
    "dataset": "leads",
    "day": "2026-11-19",
    "status": "DATA",
    "objectCount": 3,
    "totalBytes": 5242880,
    "objects": [
        { "key": "20261119063015_0000_part_00.parquet", "size": 2097152 },
        { "key": "20261119063015_0001_part_00.parquet", "size": 1048576 },
        { "key": "20261119151414_0000_part_00.parquet", "size": 2097152 }
    ],
    "deliveredAt": "2026-11-20T02:10:44Z"
}
```

The following list describes each field in the `_SUCCESS` file.

`status`  
`DATA` when the day has files, or `NO_DATA` when the day is complete and nothing changed. Every day gets a `_SUCCESS` file, so a missing file always means that the day isn't finished, never that nothing happened.

`objects`, `objectCount`, `totalBytes`  
The complete list of the day's files, with each key relative to the day folder and its size in bytes. AWS Partner Central writes the `_SUCCESS` file once and doesn't change it, so this list is authoritative. Read exactly these files, and ignore any other object in the folder.

`dataset`, `day`, `deliveredAt`  
The folder, the delivery day, and the time in UTC when AWS Partner Central wrote the file.

`schemaVersion`  
The version of this format, currently `1`. Ignore fields that you don't recognize.

Apply days in order. A later day's `_SUCCESS` file can appear before an earlier day's. Wait for the earlier day and apply it first. To react to deliveries instead of polling, configure an Amazon S3 Event Notification or an Amazon EventBridge rule on your bucket for the prefix `AWSDataSubscriptions/{{account-id}}/` and the suffix `_SUCCESS`.