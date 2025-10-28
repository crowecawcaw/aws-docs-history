Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Working with filters

When you add a dataset to a detector, you can specify a subset of dimensions that are used to create filters.
That way you only monitor for anomalies in a certain region or for a specific service, not any anomaly found in the
data. Use the **Filters** area to specify the dimensions and values that define the filter.

For example, imagine that you run an ecommerce business that tracks the measures `revenue` and
`orderRate` in the dimensions `marketplace` (country) and `category`. You can
create a filter so that only certain countries or categories are monitored. Suppose that you specified the following
dimension filtering criteria:

- **Measures** – select both `revenue` and
  `orderRate`.
- **Dimensions**

      + `marketplace` – select `US` and `CA`.
      + `category` – select `Electronics` and `Apparels`.

  In this case, you're monitoring only the records that meet all of these conditions. That means only when:

- **Measure** is `revenue` or `orderRate`,
- **AND**
  `marketplace` is either `US` or `CA`.
- **AND**
  `category` is either `Electronics` or `Apparels`.
  Note that when creating a filter, dimensions are joined with the AND operation, and values within a dimension
  are joined with the OR operation.

## Creating filters

When you add a datasource to a detector, you can specify one or more dimensions that are used to filter your data.

###### Create a filter in the Lookout for Metrics console:

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add a dataset**.
4. Provide the information to **Choose a datasource** as outlined in [Detector Statuses](detectors-setup.md#dataset-create "detectors-setup.md#dataset-create").
5. Choose **Next**.
6. Choose the measures that you want to monitor.
7. In **Dimension filters**, add up to five dimensions for the filter. For each dimension
   filter, you can include up to 10 values. Remember that dimensions are joined with the AND operation, and
   values are joined with the OR operation.
8. Choose **Next**.
9. Review your selections, then choose **Save and activate**.

You can create a filter using the `DimensionFilterList` object within the [CreateMetricSet](../api/API_CreateMetricSet.md "../api/API_CreateMetricSet.md") operation. For example, consider the following code.

```

"DimensionFilterList": [
  {"Country": [
    { "Value": "US",
      "FilterOperation": "equals" },
    { "Value": "UK",
      "FilterOperation": "equals" }
  ]},
  {"Year": [
    { "Value": "2000",
      "FilterOperation": "equals" }
  ]}
]

```

In this example, you are filtering in all items where the dimension `year` is `2000` and the dimension `country` is either `US` or `UK`.
