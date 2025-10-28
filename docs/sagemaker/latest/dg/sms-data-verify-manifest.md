# Label verification and adjustment data in the

output manifest

Amazon SageMaker Ground Truth writes label verification data to the output manifest within the metadata
for the label. It adds two properties to the metadata:

- A `type` property, with a value of
  "`groundtruth/label-verification`.
- A `worker-feedback` property, with an array of `comment`
  values. This property is added when the worker enters comments. If there are no
  comments, the field doesn't appear.
  The following example output manifest shows how label verification data
  appears:

```
{
  "source-ref":"S3 bucket location",
  "verify-bounding-box":"1",
  "verify-bounding-box-metadata":
  {
    "class-name": "bad",
    "confidence": 0.93,
    "type": "groundtruth/label-verification",
    "job-name": "verify-bounding-boxes",
    "human-annotated": "yes",
    "creation-date": "2018-10-18T22:18:13.527256",
    "worker-feedback": [
      {"comment": "The bounding box on the bird is too wide on the right side."},
      {"comment": "The bird on the upper right is not labeled."}
    ]
  }
}
```

The worker output of adjustment tasks resembles the worker output of the original
task, except that it contains the adjusted values and an `adjustment-status`
property with the value of `adjusted` or `unadjusted` to indicate
whether an adjustment was made.

For more examples of the output of different tasks, see [Labeling job output data](sms-data-output.md "sms-data-output.md").
