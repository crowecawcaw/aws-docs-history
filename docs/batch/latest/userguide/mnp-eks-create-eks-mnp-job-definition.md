# Create an Amazon EKS MNP job

definition

To define and run MNP jobs on Amazon EKS, there are new parameters within the [`RegisterJobDefinition`](../APIReference/API_RegisterJobDefinition.md "../APIReference/API_RegisterJobDefinition.md") and [`SubmitJob`](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") API
operations.

- Use [`eksProperties`](../APIReference/API_EksProperties.md "../APIReference/API_EksProperties.md") under the [`nodeProperties`](../APIReference/API_NodeProperties.md "../APIReference/API_NodeProperties.md") section to define your MNP job definition.
- Use [`eksPropertiesOverride`](../APIReference/API_EksPropertiesOverride.md "../APIReference/API_EksPropertiesOverride.md") under the [`nodePropertyOverrides`](../APIReference/API_NodePropertyOverride.md "../APIReference/API_NodePropertyOverride.md") section to override the parameters defined
  in the job definition when submitting an MNP job.
  These actions can be defined through API operations and the AWS Management Console.

## Reference: Register the Amazon EKS MNP

job definition request payload

The following example illustrates how you can register an Amazon EKS MNP job definition
with two nodes.

```
{
  "jobDefinitionName": "MyEksMnpJobDefinition",
  "type": "multinode",
  "nodeProperties": {
    "numNodes": 2,
    "mainNode": 0,
    "nodeRangeProperties": [
      {
        "targetNodes" : "0:",
        "eksProperties": {
          "podProperties": {
            "containers": [
              {
                "name": "test-eks-container-1",
                "image": "public.ecr.aws/amazonlinux/amazonlinux:2",
                "command": [
                  "sleep",
                  "60"
                ],
                "resources": {
                  "limits": {
                    "cpu": "1",
                    "memory": "1024Mi"
                  }
                },
                "securityContext":{
                  "runAsUser":1000,
                  "runAsGroup":3000,
                  "privileged":true,
                  "readOnlyRootFilesystem":true,
                  "runAsNonRoot":true
               }
              }
            ],
            "initContainers": [
               {
                  "name":"init-ekscontainer",
                  "image": "public.ecr.aws/amazonlinux/amazonlinux:2",
                  "command": [
                     "echo",
                     "helloWorld"
                   ],
                   "resources": {
                     "limits": {
                       "cpu": "1",
                       "memory": "1024Mi"
                     }
                  }
               }
            ],
            "metadata": {
               "labels": {
                  "environment" : "test"
               }
            }
          }
        }
      }
    ]
  }
}
```

To register the job definition using the AWS CLI, copy the definition to a local file
named _MyEksMnpJobDefinition.json_ and run the following command.

```
aws batch register-job-definition --cli-input-json file://MyEksMnpJobDefinition.json
```

You will receive the following JSON response.

```
{
    "jobDefinitionName": "MyEksMnpJobDefinition",
    "jobDefinitionArn": "arn:aws:batch:us-east-1:0123456789:job-definition/MyEksMnpJobDefinition:1",
    "revision": 1
}
```
