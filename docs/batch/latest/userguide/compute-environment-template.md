# Resource: Compute environment template

The following example shows an empty compute environment template. You can use this template to create your
compute environment that can then be saved to a file and used with the AWS CLI `--cli-input-json` option. For
more information about these parameters, see [CreateComputeEnvironment](../APIReference/API_CreateComputeEnvironment.md "../APIReference/API_CreateComputeEnvironment.md") in the
_AWS Batch API Reference_.

###### Note

You can generate a compute environment template with the following AWS CLI command.

```
`$` `aws batch create-compute-environment --generate-cli-skeleton`
```

```
{
    "computeEnvironmentName": "",
    "type": "UNMANAGED",
    "state": "DISABLED",
    "unmanagedvCpus": 0,
    "computeResources": {
        "type": "EC2",
        "allocationStrategy": "BEST_FIT_PROGRESSIVE",
        "minvCpus": 0,
        "maxvCpus": 0,
        "desiredvCpus": 0,
        "instanceTypes": [
            ""
        ],
        "imageId": "",
        "subnets": [
            ""
        ],
        "securityGroupIds": [
            ""
        ],
        "ec2KeyPair": "",
        "instanceRole": "",
        "tags": {
            "KeyName": ""
        },
        "placementGroup": "",
        "bidPercentage": 0,
        "spotIamFleetRole": "",
        "launchTemplate": {
            "launchTemplateId": "",
            "launchTemplateName": "",
            "version": ""
        },
        "ec2Configuration": [
            {
                "imageType": "",
                "imageIdOverride": "",
                "imageKubernetesVersion": ""
            }
        ]
    },
    "serviceRole": "",
    "tags": {
        "KeyName": ""
    },
    "eksConfiguration": {
        "eksClusterArn": "",
        "kubernetesNamespace": ""
    }
}
```
