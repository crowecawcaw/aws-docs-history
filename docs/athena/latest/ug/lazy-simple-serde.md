# Lazy Simple SerDe for CSV, TSV, and custom-delimited files

Because this is the default SerDe in Athena for data in CSV, TSV, and custom-delimited
formats, specifying it is optional. In your `CREATE TABLE` statement, if you
don't specify a SerDe and specify only `ROW FORMAT DELIMITED`, Athena uses this
SerDe. Use this SerDe if your data does not have values enclosed in quotes.

For reference documentation about the Lazy Simple SerDe, see the [Hive SerDe](https://cwiki.apache.org/confluence/display/Hive/DeveloperGuide#DeveloperGuide-HiveSerDe "https://cwiki.apache.org/confluence/display/Hive/DeveloperGuide#DeveloperGuide-HiveSerDe") section of the Apache Hive Developer Guide.

## Serialization library name

The serialization library name for the Lazy Simple SerDe is
`org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe`. For source code
information, see [LazySimpleSerDe.java](https://github.com/apache/hive/blob/master/serde/src/java/org/apache/hadoop/hive/serde2/lazy/LazySimpleSerDe.java "https://github.com/apache/hive/blob/master/serde/src/java/org/apache/hadoop/hive/serde2/lazy/LazySimpleSerDe.java") on GitHub.com.

## Ignoring headers

To ignore headers in your data when you define a table, you can use the
`skip.header.line.count` table property, as in the following
example.

```
TBLPROPERTIES ("skip.header.line.count"="1")
```

For examples that ignore headers, see the `CREATE TABLE` statements in
[Query Amazon VPC flow logs](vpc-flow-logs.md "vpc-flow-logs.md") and [Query Amazon CloudFront logs](cloudfront-logs.md "cloudfront-logs.md").

The following example shows how to use the `LazySimpleSerDe` library to
create a table in Athena from CSV data. To deserialize custom-delimited files using
this SerDe, follow the pattern in the examples but use the `FIELDS TERMINATED
 BY` clause to specify a different single-character delimiter. Lazy Simple
SerDe does not support multi-character delimiters.

###### Note

Replace `myregion` in `s3://athena-examples-`myregion`/path/to/data/` with the region identifier where you run Athena, for example, `s3://athena-examples-us-west-1/path/to/data/`.

Use the `CREATE TABLE` statement to create an Athena table from the
underlying data in CSV stored in Amazon S3.

```
CREATE EXTERNAL TABLE flight_delays_csv (
    yr INT,
    quarter INT,
    month INT,
    dayofmonth INT,
    dayofweek INT,
    flightdate STRING,
    uniquecarrier STRING,
    airlineid INT,
    carrier STRING,
    tailnum STRING,
    flightnum STRING,
    originairportid INT,
    originairportseqid INT,
    origincitymarketid INT,
    origin STRING,
    origincityname STRING,
    originstate STRING,
    originstatefips STRING,
    originstatename STRING,
    originwac INT,
    destairportid INT,
    destairportseqid INT,
    destcitymarketid INT,
    dest STRING,
    destcityname STRING,
    deststate STRING,
    deststatefips STRING,
    deststatename STRING,
    destwac INT,
    crsdeptime STRING,
    deptime STRING,
    depdelay INT,
    depdelayminutes INT,
    depdel15 INT,
    departuredelaygroups INT,
    deptimeblk STRING,
    taxiout INT,
    wheelsoff STRING,
    wheelson STRING,
    taxiin INT,
    crsarrtime INT,
    arrtime STRING,
    arrdelay INT,
    arrdelayminutes INT,
    arrdel15 INT,
    arrivaldelaygroups INT,
    arrtimeblk STRING,
    cancelled INT,
    cancellationcode STRING,
    diverted INT,
    crselapsedtime INT,
    actualelapsedtime INT,
    airtime INT,
    flights INT,
    distance INT,
    distancegroup INT,
    carrierdelay INT,
    weatherdelay INT,
    nasdelay INT,
    securitydelay INT,
    lateaircraftdelay INT,
    firstdeptime STRING,
    totaladdgtime INT,
    longestaddgtime INT,
    divairportlandings INT,
    divreacheddest INT,
    divactualelapsedtime INT,
    divarrdelay INT,
    divdistance INT,
    div1airport STRING,
    div1airportid INT,
    div1airportseqid INT,
    div1wheelson STRING,
    div1totalgtime INT,
    div1longestgtime INT,
    div1wheelsoff STRING,
    div1tailnum STRING,
    div2airport STRING,
    div2airportid INT,
    div2airportseqid INT,
    div2wheelson STRING,
    div2totalgtime INT,
    div2longestgtime INT,
    div2wheelsoff STRING,
    div2tailnum STRING,
    div3airport STRING,
    div3airportid INT,
    div3airportseqid INT,
    div3wheelson STRING,
    div3totalgtime INT,
    div3longestgtime INT,
    div3wheelsoff STRING,
    div3tailnum STRING,
    div4airport STRING,
    div4airportid INT,
    div4airportseqid INT,
    div4wheelson STRING,
    div4totalgtime INT,
    div4longestgtime INT,
    div4wheelsoff STRING,
    div4tailnum STRING,
    div5airport STRING,
    div5airportid INT,
    div5airportseqid INT,
    div5wheelson STRING,
    div5totalgtime INT,
    div5longestgtime INT,
    div5wheelsoff STRING,
    div5tailnum STRING
)
    PARTITIONED BY (year STRING)
    ROW FORMAT DELIMITED
      FIELDS TERMINATED BY ','
      ESCAPED BY '\\'
      LINES TERMINATED BY '\n'
    LOCATION 's3://athena-examples-`myregion`/flight/csv/';
```

Run `MSCK REPAIR TABLE` to refresh partition metadata each time a new
partition is added to this table:

```
MSCK REPAIR TABLE flight_delays_csv;
```

Query the top 10 routes delayed by more than 1 hour:

```
SELECT origin, dest, count(*) as delays
FROM flight_delays_csv
WHERE depdelayminutes > 60
GROUP BY origin, dest
ORDER BY 3 DESC
LIMIT 10;
```

###### Note

The flight table data comes from [Flights](http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time "http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time") provided by US Department of Transportation, [Bureau of Transportation Statistics](http://www.transtats.bts.gov/ "http://www.transtats.bts.gov/"). Desaturated from original.

To create an Athena table from TSV data stored in Amazon S3, use `ROW FORMAT
 DELIMITED` and specify the `\t` as the tab field delimiter,
`\n` as the line separator, and `\` as the escape
character. The following excerpt shows this syntax. No sample TSV flight data is
available in the `athena-examples` location, but as with the CSV
table, you would run `MSCK REPAIR TABLE` to refresh partition metadata
each time a new partition is added.

```
...
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
...
```
