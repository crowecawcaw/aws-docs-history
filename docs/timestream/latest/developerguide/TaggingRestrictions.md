For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Tagging restrictions

Each tag consists of a key and a value, both of which you define. The following restrictions apply:

- Each Timestream for LiveAnalytics table can have only one tag with the same key. If you try
  to add an existing tag, the existing tag value is updated to the new
  value.
- A value acts as a descriptor within a tag category. In Timestream for LiveAnalytics the value cannot be empty or null.
- Tag keys and values are case sensitive.
- The maximum key length is 128 Unicode characters.
- The maximum value length is 256 Unicode characters.
- The allowed characters are letters, white space, and numbers, plus the following special
  characters: `+ - = . _ : /`
- The maximum number of tags per resource is 50.
- AWS-assigned tag names and values are automatically assigned the `aws:`
  prefix, which you can't assign. AWS-assigned tag names don't count toward the tag
  limit of 50. User-assigned tag names have the prefix `user:` in the cost
  allocation report.
- You can't backdate the application of a tag.
