# Create a table for CloudTrail logs in Athena using manual partitioning

You can manually create tables for CloudTrail log files in the Athena console, and then run
queries in Athena.

###### To create an Athena table for a CloudTrail trail using the Athena console

1. Copy and paste the following DDL statement into the Athena console query
   editor, then modify it according to your requirements. Note that because CloudTrail
   log files are not an ordered stack trace of public API calls, the fields in the
   log files do not appear in any specific order.

```
CREATE EXTERNAL TABLE cloudtrail_logs (
eventversion STRING,
useridentity STRUCT<
               type:STRING,
               principalid:STRING,
               arn:STRING,
               accountid:STRING,
               invokedby:STRING,
               accesskeyid:STRING,
               username:STRING,
               onbehalfof: STRUCT<
                    userid: STRING,
                    identitystorearn: STRING>,
  sessioncontext:STRUCT<
    attributes:STRUCT<
               mfaauthenticated:STRING,
               creationdate:STRING>,
    sessionissuer:STRUCT<
               type:STRING,
               principalid:STRING,
               arn:STRING,
               accountid:STRING,
               username:STRING>,
    ec2roledelivery:string,
    webidfederationdata: STRUCT<
               federatedprovider: STRING,
               attributes: map<string,string>>
  >
>,
eventtime STRING,
eventsource STRING,
eventname STRING,
awsregion STRING,
sourceipaddress STRING,
useragent STRING,
errorcode STRING,
errormessage STRING,
requestparameters STRING,
responseelements STRING,
additionaleventdata STRING,
requestid STRING,
eventid STRING,
resources ARRAY<STRUCT<
               arn:STRING,
               accountid:STRING,
               type:STRING>>,
eventtype STRING,
apiversion STRING,
readonly STRING,
recipientaccountid STRING,
serviceeventdetails STRING,
sharedeventid STRING,
vpcendpointid STRING,
vpcendpointaccountid STRING,
eventcategory STRING,
addendum STRUCT<
  reason:STRING,
  updatedfields:STRING,
  originalrequestid:STRING,
  originaleventid:STRING>,
sessioncredentialfromconsole STRING,
edgedevicedetails STRING,
tlsdetails STRUCT<
  tlsversion:STRING,
  ciphersuite:STRING,
  clientprovidedhostheader:STRING>
)
PARTITIONED BY (region string, year string, month string, day string)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`Account_ID`/';
```

###### Note

We suggest using the `org.apache.hive.hcatalog.data.JsonSerDe`
shown in the example. Although a
`com.amazon.emr.hive.serde.CloudTrailSerde` exists, it does
not currently handle some of the newer CloudTrail fields. 2. (Optional) Remove any fields not required for your table. If you need to read
only a certain set of columns, your table definition can exclude the other
columns. 3. Modify
`s3://amzn-s3-demo-bucket/AWSLogs/`Account_ID`/`
to point to the Amazon S3 bucket that contains the log data that you want to query.
The example uses a `LOCATION` value of logs for a particular account,
but you can use the degree of specificity that suits your application. For
example:

    * To analyze data from multiple accounts, you can roll back the
     `LOCATION` specifier to indicate all `AWSLogs`
     by using `LOCATION
     's3://amzn-s3-demo-bucket/AWSLogs/'`.
    * To analyze data from a specific date, account, and Region, use
     `LOCATION
     's3://amzn-s3-demo-bucket/123456789012/CloudTrail/us-east-1/2016/03/14/'.`
    * To analyze network activity data instead of management events, replace
     `/CloudTrail/` in the `LOCATION` clause with
     `/CloudTrail-NetworkActivity/`.

Using the highest level in the object hierarchy gives you the greatest
flexibility when you query using Athena. 4. Verify that fields are listed correctly. For more information about the full
list of fields in a CloudTrail record, see [CloudTrail record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md").

The example `CREATE TABLE` statement in Step 1 uses the [Hive JSON SerDe](hive-json-serde.md "hive-json-serde.md"). In the example,
the fields `requestparameters`, `responseelements`, and
`additionaleventdata` are listed as type `STRING` in
the query, but are `STRUCT` data type used in JSON. Therefore, to get
data out of these fields, use `JSON_EXTRACT` functions. For more
information, see [Extract JSON data from strings](extracting-data-from-JSON.md "extracting-data-from-JSON.md"). For performance
improvements, the example partitions the data by AWS Region, year, month, and
day. 5. Run the `CREATE TABLE` statement in the Athena console. 6. Use the [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md") command to load the partitions
so that you can query them, as in the following example.

```
ALTER TABLE `table_name` ADD
   PARTITION (region='us-east-1',
              year='2019',
              month='02',
              day='01')
   LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`Account_ID`/CloudTrail/`us-east-1/2019/02/01/`'
```
