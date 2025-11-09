# Configure index rotation for OpenSearch Service

For the OpenSearch Service destination, you can specify a time-based index rotation option from one
of the following five options: **NoRotation**,
**OneHour**, **OneDay**, **OneWeek**, or
**OneMonth**.

Depending on the rotation option you choose, Amazon Data Firehose appends a portion of the UTC
arrival timestamp to your specified index name. It rotates the appended timestamp
accordingly. The following example shows the resulting index name in OpenSearch Service
for each index rotation option, where the specified index name is
**myindex** and the arrival timestamp is
`2016-02-25T13:00:00Z`.

| RotationPeriod | IndexName               |
| -------------- | ----------------------- |
| `NoRotation`   | `myindex`               |
| `OneHour`      | `myindex-2016-02-25-13` |
| `OneDay`       | `myindex-2016-02-25`    |
| `OneWeek`      | `myindex-2016-w08`      |
| `OneMonth`     | `myindex-2016-02`       |

###### Note

With the `OneWeek` option, Data Firehose auto-create indexes using the
format of <YEAR>-w<WEEK NUMBER> (for example, `2020-w33`),
where the week number is calculated using UTC time and according to the following US
conventions:

- A week starts on Sunday
- The first week of the year is the first week that contains a Saturday in
  this year
