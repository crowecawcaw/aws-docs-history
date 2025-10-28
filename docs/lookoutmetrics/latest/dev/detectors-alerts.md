Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Working with alerts

## Creating alerts

Amazon Lookout for Metrics detectors find anomalies in data. When an anomaly is severe, the detector can send details about it to
another AWS service or resource. You can configure a detector to run an AWS Lambda function to process anomaly
alerts, or send details to an Amazon Simple Notification Service (Amazon SNS) topic. Amazon SNS can then send the information to email subscribers or
an HTTP endpoint, among numerous other supported destinations.

A severity threshold determines when the detector sends anomaly alerts. If you get anomaly alerts for anomalies
that are not interesting, you can increase the threshold. If you don't get enough alerts, you can lower it.

When you create an alert, you can specify a subset of measures or dimensions that are used to create the alert.
That is, you only want to be alerted to anomalies in a certain region or for a specific service, not any anomaly
found in the data. Use the **Criteria for sending the alert** area to specify the measures,
dimensions, and sensitivity score that define the alert.

For example, imagine that you run an e-commerce business that tracks the measures `revenue` and
`orderRate` in the dimensions `marketplace` (country) and `category`. You can
configure the alert criteria to notify you only when anomalies are detected for specific combinations of these
measures and dimensions. Suppose that you specified the following criteria:

- **Measures** – select both `revenue` and
  `orderRate`.
- **Dimensions**
  - `marketplace` – select `US` and `CA`.
  - `category` – select `Electronics` and `Apparels`.

- **Sensitivity score** – set to 60.

In this case, you'll receive an alert only when all of these conditions are met. That means only when

- **Measure** is `revenue` or `orderRate`,
- **AND**
  `marketplace` is either `US` or `CA`.
- **AND**
  `category` is either `Electronics` or `Apparels`.
- **AND** the sensitivity score is greater than or equal to 60.

To send anomaly alerts, a detector uses a [service role](permissions-service.md "permissions-service.md"). When you use
the console to create alerts, you can create a service role or choose one you already have. If you don't have
permission to create roles, ask an administrator to create a service role for Lookout for Metrics.

###### To create an alert

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add alert**.
4. Configure the following options.

######

    * **Alert name** – The name of the alert. Alert names must be unique across all
     detectors in a Region.
    * **Description** – A description of the alert.
    * **Criteria** – The measures, dimensions, and severity score that trigger an
     alert.




    	+ **Measure** – Provide up to 5 measures that you want to receive alerts for
    	 when an anomaly is detected.
    	+ **Dimension** – Provide up to 5 dimensions to monitor for anomalies. You
    	 can provide up to 10 values per dimension.
    	+ **Severity score** – The severity score that the anomaly must reach for
    	 the detector to send an anomaly alert.
    * **Channel** – The destination service.
    * **SNS topic** or **Lambda function** – The resource in the
     target service that receives the anomaly alert.
    * **Role** – A service role that allows the detector to send alerts to the
     resource.

5. Choose **Add alert**.

When the detector finds an anomaly that meets the filter criteria, it sends an anomaly alert. An anomaly alert
is a JSON document with details about the metrics that were affected by the anomaly. The following example shows
an anomaly alert where `revenue` is affected in the `electronics` or `apparels`
categories in two marketplaces, `UK` (United Kingdom) or `FR` (France), and when shipping is
either `standard` or `priority`.

###### Example alert (line endings and indentation added)

```

{
  "anomalyDetectorArn": "arn:aws:lookoutmetrics:us-west-2:123456789101:AnomalyDetector:testBugBash",
  "anomalyScore": 83.33,
  "consoleUrl": "https://us-west-2.console.aws.amazon.com/lookoutmetrics/home?region=us-west-2#arn:aws:lookoutmetrics:us-west-2:123456789101:AnomalyDetector:myDetector/anomalies/anomaly/60359687-afb8-4c46-af3d-aea03614a53f",
  "anomalyGroupId": "60359687-afb8-4c46-af3d-aea03614a53f",
  "alertName": "myAlertName",
  "alertArn": "arn:aws:lookoutmetrics:us-west-2:123456789101:Alert:myAlertName",
  "alertEventId": "arn:aws:lookoutmetrics:us-west-2:123456789101:Alert:myAlertName:event/60359687-afb8-4c46-af3d-aea03614a53f",
  "alertDescription": "SNS Alert for anomalies in Revenue",
  "impactedMetric": {
    "metricName": "revenue",
    "dimensionContribution": [
      {
        "dimensionName": "category",
        "dimensionValueContributions": [
          {
            "dimensionValue": "apparels",
            "valueContribution": 68
          },
          {
            "dimensionValue": "electronics",
            "valueContribution": 32
          }
        ]
      },
      {
        "dimensionName": "marketplace",
        "dimensionValueContributions": [
          {
            "dimensionValue": "UK",
            "valueContribution": 68
          },
          {
            "dimensionValue": "FR",
            "valueContribution": 32
          }
        ]
      },
      {
        "dimensionName": "shipping",
        "dimensionValueContributions": [
          {
            "dimensionValue": "standard",
            "valueContribution": 68
          },
          {
            "dimensionValue": "priority",
            "valueContribution": 32
          }
        ]
      }
    ],
    "relevantTimeSeries": [
      {
        "timeSeriesId": "978d818762cf3669fajhg8398jk9fd036310832a18bbc4f3f5b17c1f0bf1086683eda16678503580d704f518",
        "dimensions": [
          {
            "dimensionName": "category",
            "dimensionValue": "electronics"
          },
          {
            "dimensionName": "marketplace",
            "dimensionValue": "FR"
          },
          {
            "dimensionName": "shipping",
            "dimensionValue": "priority"
          }
        ],
        "metricValue": 650
      },
      {
        "timeSeriesId": "f1b5e0a7f64b249jma947nf0wnf7qncsoa48ea08eb0f0afc17a12a11c423944e871659be0748c98b1f039cad5bda0e0c244c3035a84a50123b9d1697e599612993c6c",
        "dimensions": [
          {
            "dimensionName": "category",
            "dimensionValue": "apparels"
          },
          {
            "dimensionName": "marketplace",
            "dimensionValue": "UK"
          },
          {
            "dimensionName": "shipping",
            "dimensionValue": "standard"
          }
        ],
        "metricValue": 1200
      }
    ]
  },
  "timestamp": "2022-01-15T04:25Z[UTC]"
}

```

In the preceding example, the detector identified unusually high revenue values (650 and 1200) in UK and FR
for category apparels and electronics. The value for UK, apparels, and standard shipping was farther from the
expected value, so its contribution to the anomaly (68%) is greater than the value for FR, electronics and
priority shipping. Overall, the anomaly for the two metrics had an severity score of 83.33.

The severity score is a measurement of how unexpected the observed metric values are based on the detector's
understanding of your data. It takes into consideration when the anomaly occurred, such as the time of day, and
how many metrics were affected.

As the detector learns more about your data, anomalies for similar events might have higher or lower severity
scores. You can guide its learning by providing feedback on affected metrics in an anomaly. For more information,
see [Working with anomalies](detectors-anomalies.md "detectors-anomalies.md").

## Updating alerts

After an alert is created, you can update the alert if it does not meet your needs. You can change whether
AWS Lambda or Amazon Simple Notification Service is used to send updates, the alert description, the alert sensitivity threshold, and the
alert criteria.

###### To update an alert

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Alerts** in the **Detectors** pane.
4. Choose an alert.
5. Configure the following options.

######

    * **Description** – A description of the alert.
    * **Criteria** – The measures, dimensions, and severity score that trigger an
     alert.




    	+ **Measure** – Provide up to 10 measures that you want to receive alerts
    	 for when an anomaly is detected.
    	+ **Dimension** – Provide up to 10 dimensions to monitor for anomalies. You
    	 can provide up to 10 values per dimension.
    	+ **Severity score** – The severity score that the anomaly must reach for
    	 the detector to send an anomaly alert.
    * **Channel** – The destination service.
    * **SNS topic** or **Lambda function** – The resource in the
     target service that receives the anomaly alert.
    * **Role** – A service role that allows the detector to send alerts to the
     resource.

6. Choose **Save**.
