# Override an Amazon EKS MNP job

definition

Optionally, you can override the job definition details (such as changing the MNP job size
or child job details). The following provides an example JSON request payload to submit a five
node MNP job, and changes to the `test-eks-container-1` container’s command.

```
{
  "numNodes": 5,
  "nodePropertyOverrides": [
    {
      "targetNodes": "0:",
      "eksPropertiesOverride": {
        "podProperties": {
          "containers": [
            {
              "name": "test-eks-container-1",
              "command": [
                "sleep",
                "150"
              ]
            }
          ]
        }
      }
    }
  ]
}
```

To submit a job with these overrides, save the example to a local file,
_eks-mnp-job-nodeoverride.json_, and use the AWS CLI to submit the job with
the overrides.
