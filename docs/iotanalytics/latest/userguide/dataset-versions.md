End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Keeping multiple versions of datasets

You can choose how many versions of your dataset contents to retain, and for how long, by specifying values for the dataset
`retentionPeriod and versioningConfiguration` fields when invoking the
[CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") and
[UpdateDataset](../APIReference/API_UpdateDataset.md "../APIReference/API_UpdateDataset.md") APIs:

```
...
"retentionPeriod": {
  "unlimited": "boolean",
  "numberOfDays": "integer"
},
"versioningConfiguration": {
  "unlimited": "boolean",
  "maxVersions": "integer"
},
...
```

The settings of these two parameters work together to determine how many versions of data
set contents are retained, and for how long, in the following ways.

|                                                                    |                                                                                                    |                                                                                                              |                                                                                                   |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
|                                                                    | **retentionPeriod** [not specified]                                                                | **retentionPeriod:** unlimited = TRUE, numberOfDays = not set                                                | **retentionPeriod:** unlimited = FALSE, numberOfDays = X                                          |
| **versioningConfiguration:** [not specified]                       | Only the latest version plus the latest succeeded version (if different) are retained for 90 days. | Only the latest version plus the latest succeeded version (if different) are retained for an unlimited time. | Only the latest version plus the latest succeeded version (if different) are retained for X days. |
| **versioningConfiguration:** unlimited = TRUE, maxVersions not set | All versions from the last 90 days will be retained, regardless of how many.                       | There is no limit to the number of versions retained.                                                        | All versions from the last X days will be retained, regardless of how many.                       |
| **versioningConfiguration:** unlimited = FALSE, maxVersions = Y    | No more than Y versions from the last 90 days will be retained.                                    | Up to Y versions will be retained, regardless of how old they are.                                           | No more than Y versions from the last X days will be retained.                                    |
