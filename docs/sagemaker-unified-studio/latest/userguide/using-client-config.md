# Using ClientConfig

If using `ClientConfig` for supplying credentials or changing the AWS region name, the `ClientConfig` object will need to be supplied when initializing any further Amazon SageMaker Studio objects, such as `Domain` or `Project`. If using non-prod endpoint for an AWS service, it can also be supplied in the `ClientConfig`. Note: In sagemaker space, datazone endpoint is by default fetched from the metadata JSON file.

```

from sagemaker_studio import ClientConfig, Project
conf = ClientConfig(region="eu-west-1")
proj = Project(config=conf)

```
