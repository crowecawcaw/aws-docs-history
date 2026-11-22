

# Monitor using the AWS CLI

Use the `get-aws-network-performance-data` command to return network performance metrics. For more information, see [GetAwsNetworkPerformanceData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.html) in the *Amazon EC2 API Reference*.

The following example queries network performance between us-east-1 and us-west-2 on October 26, 2022, from 12:00:00 to 12:30:00 UTC. The request uses the following parameters:
+ **Metric**: The metric type. In this example, `aggregate-latency` returns aggregated latency.
+ **Statistic**: The statistic to return. `p50` returns the median of all data points in each period.
**Note**  
`p50` is the only supported statistic.
+ **Period**: The aggregation interval. In this example, metrics are returned for every five minutes.

```
aws ec2 --region us-east-1 get-aws-network-performance-data --start-time 2022-10-26T12:00:00.000Z --end-time 2022-10-26T12:30:00.000Z --data-queries Id=id1,Source=us-east-1,Destination=us-west-2,Metric=aggregate-latency,Statistic=p50,Period=five-minutes
```

The following is example output.

```json
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
                }
            ]
        }
    ]
}
```