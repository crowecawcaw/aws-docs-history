# Monitor Infrastructure Performance using the AWS CLI

[GetAwsNetworkPerformanceData](../../../AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.md "../../../AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.md") returns network performance metrics. For more information,
see [GetAwsNetworkPerformanceData](../../../AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.md "../../../AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.md").

In the following example, network performance is queried between two
Regions, `us-east-1` and `us-west-2` on
`2022-10-26` between a start-time of `12:00:00` and an end time of
`12:30:00`. The request also uses the following parameters:

- `Metric` indicates what type of metric is being requested. In this example,
  `aggregate-latency`, indicates that the performance metrics are aggregated and
  returned for latency.
- `Statistic` is the median value of the metric. In this example, `p50` is
  the statistic of all the data points gathered within those five minutes.

###### Note

`p50` is the only supported statistic.

- `Period` indicates the interval at which performance the `metric`
  is returned. In this example, `aggregated-latency` metrics are returned for every
  `five-minutes`.

```
aws ec2 --region ap-southeast-3 get-aws-network-performance-data --start-time
   2022-10-26T12:00:00.000Z --end-time 2022-10-26T12:30:00.000Z --data-queries
   Id=id1,Source=us-east-1,Destination=us-west-2,Metric=aggregate-latency,Statistic=p50,Period=five-minutes
```

The results return the following:

```
{
    "DataResponses": [
        {
            "Id": "id1",
            "Source": "us-east-1",
            "Destination": "us-west-2",
            "Metric": "aggregate-latency",
            "Statistic": "p50",
            "Period": "five-minutes",
            "MetricPoints": [
                {
                    "StartDate": "2022-10-26T12:00:00+00:00",
                    "EndDate": "2022-10-26T12:05:00+00:00",
                    "Value": 62.44349,
                    "Status": "OK"
                },
                {
                    "StartDate": "2022-10-26T12:05:00+00:00",
                    "EndDate": "2022-10-26T12:10:00+00:00",
                    "Value": 62.483498,
                    "Status": "OK"
                },
                {
                    "StartDate": "2022-10-26T12:10:00+00:00",
                    "EndDate": "2022-10-26T12:15:00+00:00",
                    "Value": 62.51248,
                    "Status": "OK"
                },
                {
                    "StartDate": "2022-10-26T12:15:00+00:00",
                    "EndDate": "2022-10-26T12:20:00+00:00",
                    "Value": 62.635475,
                    "Status": "OK"
                },
                {
                    "StartDate": "2022-10-26T12:20:00+00:00",
                    "EndDate": "2022-10-26T12:25:00+00:00",
                    "Value": 62.733974,
                    "Status": "OK"
                },
                {
                    "StartDate": "2022-10-26T12:25:00+00:00",
                    "EndDate": "2022-10-26T12:30:00+00:00",
                    "Value": 62.773975,
                    "Status": "OK"
                },
                {
                    "StartDate": "2022-10-26T12:30:00+00:00",
                    "EndDate": "2022-10-26T12:35:00+00:00",
                    "Value": 62.75349,
                    "Status": "OK"
                }
            ]
        }
    ]
}
```
