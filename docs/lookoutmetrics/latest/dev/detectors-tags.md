Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Tagging Lookout for Metrics resources

Organize your Amazon Lookout for Metrics resources by owner, project or department with tags. Tags are key-value pairs that are
supported across AWS services. You can use tags to filter resources, create least-privilege permissions policies,
and add detail to billing reports. Lookout for Metrics also supports tag-based authorization. With tag-based authorization, you
can create [permissions policies](permissions-user.md "permissions-user.md") that limit a user's access to resources with
specific tags. For more information about tag-based authorization, see [Controlling access to AWS resources using resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

You can add tags to [detectors](lookoutmetrics-detectors.md "lookoutmetrics-detectors.md"), [datasets](detectors-dataset.md "detectors-dataset.md"), and [alerts](detectors-alerts.md "detectors-alerts.md") when you create them, or you can add tags to
existing resources. You can use the Lookout for Metrics console or manage tags with the [Lookout for Metrics
API](#detectors-tags-api "#detectors-tags-api"). Start by tagging your detectors to organize them into logical groups.

For more information about tags, see [Tagging AWS resources](../../../general/latest/gr/aws-tagging.md "../../../general/latest/gr/aws-tagging.md") in
the _Amazon Web Services General Reference_.

###### To add tags to a detector in the Lookout for Metrics console

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Tags**.
4. Choose **Manage tags**.
5. Enter a key and value. For example, `Department` and `Marketing`.
6. To add additional tags, choose **Add tag**.
7. Choose **Save**.
   Tags apply to each detector, dataset, and alert individually. They are not shared or inherited.

###### Sections

- [Using tags (Lookout for Metrics API)](#detectors-tags-api "#detectors-tags-api")
- [Tag key and value requirements](#detectors-tags-requirements "#detectors-tags-requirements")

## Using tags (Lookout for Metrics API)

When you create resources with the [CreateAnomalyDetector](../api/API_CreateAnomalyDetector.md "../api/API_CreateAnomalyDetector.md"), [CreateMetricSet](../api/API_CreateMetricSet.md "../api/API_CreateMetricSet.md") and [CreateAlert](../api/API_CreateAlert.md "../api/API_CreateAlert.md")
operations, you can include tags with the `--tags` option. The following example shows how to apply
tags when creating an anomaly detector with the AWS Command Line Interface (AWS CLI).

```
$ `aws lookoutmetrics create-anomaly-detector --anomaly-detector-name my-detector \
 --anomaly-detector-config AnomalyDetectorFrequency=PT10M \
 --anomaly-detector-description "10-minute S3 detector" \
 --tags `Department=Marketing,CostCenter=1234ABCD``
{
    "AnomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector"
}
```

To add tags to an existing resource, use the [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") operation.

```
$ `aws lookoutmetrics tag-resource --resource-arn arn:aws:lookoutmetrics:`us-east-2:123456789012:AnomalyDetector:my-detector` \
 --tags `Department=Marketing,CostCenter=1234ABCD``
```

To remove tags, use the [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md") operation.

```
$ `aws lookoutmetrics untag-resource --resource-arn arn:aws:lookoutmetrics:`us-east-2:123456789012:AnomalyDetector:my-detector` \
 --tag-keys `Department``
```

To view tags, you can use the following API operations:

- [ListTagsForResource](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md") – View the tags associated with a resource.

```
$ `aws lookoutmetrics list-tags-for-resource --resource-arn arn:aws:lookoutmetrics:`us-east-2:123456789012:AnomalyDetector:my-detector``
{
    "Tags": {
        "Department": "Marketing",
        "CostCenter": "1234ABCD"
    }
}
```

- [ListAnomalyDetectors](../api/API_ListAnomalyDetectors.md "../api/API_ListAnomalyDetectors.md"), [ListMetricSets](../api/API_ListMetricSets.md "../api/API_ListMetricSets.md"), [ListAlerts](../api/API_ListAlerts.md "../api/API_ListAlerts.md") – Get a list of resources with
  tag information.

```
$ `aws lookoutmetrics list-anomaly-detectors`
{
    "AnomalyDetectorSummaryList": [
        {
            "Status": "INACTIVE",
            "AnomalyDetectorName": "my-detector",
            "Tags": {
                "Department": "Marketing",
                "CostCenter": "1234ABCD"
            },
            "LastModificationTime": 1612994728.528,
            "CreationTime": 1612994728.528,
            "AnomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector"
        }
    ]
}
```

## Tag key and value requirements

The following requirements apply to tags for Lookout for Metrics resources:

- Maximum number of tags per resource – 50
- Maximum key length – 128 Unicode characters in UTF-8
- Maximum value length – 256 Unicode characters in UTF-8
- Tag keys and values are case sensitive.
- Your tag keys and values can't start with `aws:`. AWS services apply tags that start with
  `aws:`, and those tags can't be modified. They don't count towards tag limits.
- Tag keys and values can contain the following characters: A-Z, a-z, 0-9, space, and \_ . : / = + @ -
  (hyphen). This is the standard set of characters available across AWS services that support tags. Some
  services support additional symbols.
