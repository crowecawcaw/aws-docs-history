# Reference: Scheduling policy template

An empty scheduling policy template is shown below. You can use this template to create your scheduling policy
which can then be saved to a file and used with the AWS CLI `--cli-input-json` option. For more information
about these parameters, see [CreateSchedulingPolicy](../APIReference/API_CreateSchedulingPolicy.md "../APIReference/API_CreateSchedulingPolicy.md") in the
_AWS Batch API Reference_.

###### Note

You can generate a job queue template with the following AWS CLI command.

```
`$` `aws batch create-scheduling-policy --generate-cli-skeleton`
```

```
{
    "name": "",
    "fairsharePolicy": {
        "shareDecaySeconds": 0,
        "computeReservation": 0,
        "shareDistribution": [
            {
                "shareIdentifier": "",
                "weightFactor": 0.0
            }
        ]
    },
    "tags": {
        "KeyName": ""
    }
}
```
