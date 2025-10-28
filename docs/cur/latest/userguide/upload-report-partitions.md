# Uploading your report partitions

To query your Cost and Usage Reports data, you need to upload the data into your Athena table. You
must do this for each new AWS CUR report that AWS delivers to you.

###### To upload your latest partitions

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Choose the vertical three dots next to your table name.
3. Choose **Load partitions**.
   If you don't upload your partitions, Athena returns either no results or an error message
   that indicates missing data.
