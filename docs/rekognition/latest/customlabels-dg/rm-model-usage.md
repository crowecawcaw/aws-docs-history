# Reporting running duration and inference units used

If you trained and started your model after August 2022, you can use the
`InServiceInferenceUnits` Amazon CloudWatch metric to determine how many hours a
model has run for and the number of [inference units](running-model.md#running-model-inference-units "running-model.md#running-model-inference-units") used during those hours.

###### Note

If you only have one model in an AWS region, you can also get the running time for
the model by tracking successful calls to `StartprojectVersion` and
`StopProjectVersion` in CloudWatch. This approach doesn't work if you run
more that one model in the AWS Region as the metrics don't include information
about the model.

Alternatively, you can use AWS CloudTrail to track calls to
`StartProjectVersion` and `StopProjectVersion` (which
includes the model ARN in the `requestParameters` field of the [event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md")). CloudTrail events are limited to 90 days, but you can store
events for up to 7 years in a [CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md").

The following procedure creates graphs for the following:

- The number of hours that a model has run for.
- The number of inference units that a model has used.
  You can choose a time period up to 15 months in the past. For
  more information about metric retention, see [Metrics retention](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#metrics-retention "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#metrics-retention").

###### To determine model duration and inference units used for a model

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **All metrics** under
   **Metrics**.
3. In the content pane, choose the **Source** tab.
4. Make sure that the **Dashboard** button is selected.
5. In the edit box, replace the existing JSON with the following JSON. Change the following values:
   - `Project_Name` — The project that contains the model that you want to graph.
   - `Version_Name` — The version of the model that you want to graph.
   - `AWS_Region` — The AWS Region that contains the
     model. Make sure that the CloudWatch console is in the same AWS Region, by
     checking the Region selector in the navigation bar at the top of the page.
     Update as necessary.

```
{
    "sparkline": true,
    "metrics": [
        [
            {
                "expression": "SUM(m1)*m1",
                "label": "Inference units used",
                "id": "e1"
            }
        ],
        [
            {
                "expression": "DATAPOINT_COUNT(m1)*m1/m1",
                "label": "Hours running",
                "id": "e2"
            }
        ],
        [
            "AWS/Rekognition",
            "InServiceInferenceUnits",
            "ProjectName",
            "`Project_Name`",
            "VersionName",
            "`Version_Name`",
            {
                "id": "m1",
                "visible": false
            }
        ]
    ],
    "view": "singleValue",
    "stacked": false,
    "region": "`AWS_Region`",
    "stat": "Average",
    "period": 3600,
    "title": "Hours run and inference units used"
}
```

6. Choose **Update**.
7. At the top of the page, choose a timeline. You should see numbers for
   inference units used and hours running during the timeline. Gaps in the graph
   indicate times when the model wasn't running. The screenshot of the console
   below showing inference units used and hours running over time periods, with a
   custom time of 2 weeks set, with the highest values of 214 inference units and
   209 hours running.

![Graph showing inference units.](images/model-duration.png) 8. (Optional) Add the graph to a dashboard by choosing **Actions**
and then **Add to dashboard - improved**.
