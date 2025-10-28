# Create the table for CloudTrail

logs in Athena using partition projection

Because CloudTrail logs have a known structure whose partition scheme you can specify in
advance, you can reduce query runtime and automate partition management by using the
Athena partition projection feature. Partition projection automatically adds new
partitions as new data is added. This removes the need for you to manually add
partitions by using `ALTER TABLE ADD PARTITION`.

The following example `CREATE TABLE` statement automatically uses partition
projection on CloudTrail logs from a specified date until the present for a single
AWS Region. In the `LOCATION` and `storage.location.template`
clauses, replace the `bucket`,
`account-id`, and
`aws-region` placeholders with
correspondingly identical values. For `projection.timestamp.range`, replace
`2020`/`01`/`01`
with the starting date that you want to use. After you run the query successfully, you
can query the table. You do not have to run `ALTER TABLE ADD PARTITION` to
load the partitions.

```
CREATE EXTERNAL TABLE cloudtrail_logs_pp(
    eventversion STRING,
    useridentity STRUCT<
        type: STRING,
        principalid: STRING,
        arn: STRING,
        accountid: STRING,
        invokedby: STRING,
        accesskeyid: STRING,
        username: STRING,
        onbehalfof: STRUCT<
             userid: STRING,
             identitystorearn: STRING>,
        sessioncontext: STRUCT<
            attributes: STRUCT<
                mfaauthenticated: STRING,
                creationdate: STRING>,
            sessionissuer: STRUCT<
                type: STRING,
                principalid: STRING,
                arn: STRING,
                accountid: STRING,
                username: STRING>,
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
    readonly STRING,
    resources ARRAY<STRUCT<
        arn: STRING,
        accountid: STRING,
        type: STRING>>,
    eventtype STRING,
    apiversion STRING,
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
PARTITIONED BY (
   `timestamp` string)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/AWSLogs/`account-id`/`CloudTrail`/`aws-region`'
TBLPROPERTIES (
  'projection.enabled'='true',
  'projection.timestamp.format'='yyyy/MM/dd',
  'projection.timestamp.interval'='1',
  'projection.timestamp.interval.unit'='DAYS',
  'projection.timestamp.range'='`2020`/`01`/`01`,NOW',
  'projection.timestamp.type'='date',
  'storage.location.template'='s3://amzn-s3-demo-bucket/AWSLogs/`account-id`/`CloudTrail`/`aws-region`/${timestamp}')
```

For more information about partition projection, see [Use partition projection with Amazon Athena](partition-projection.md "partition-projection.md").
