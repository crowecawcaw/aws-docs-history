# Machine learning

Amazon SageMaker Unified Studio is a unified development experience for building analytics, AI/ML, and
generative AI applications at scale. This chapter describes the Amazon SageMaker AI capabilities that
you can use in Amazon SageMaker Unified Studio.

###### Note

When you add a custom tag to a SageMaker AI resource (such as a training job, inference
endpoint, model, or pipeline), add the prefix `ProjectUserTag` to the tag
name. For example:

```
ProjectUserTagMyCustomTag
```

###### Note

ECR repositories must be created with the `AmazonDataZoneProject` tag with
the project ID (which can be found under project details in the project overview page or
from the page URL) as the tag value. If you want to add your own tags, they must be
prefixed with `ProjectUserTag`.

For example, with AWS CLI:

```

aws ecr create-repository \
--repository-name my-repo \
--tags \
Key=AmazonDataZoneProject,Value=5blxelum5cmckb \
Key=ProjectUserTagMyTag,Value=MyTagValue \

```

Example using Jupyterlab notebook:

```

import boto3

# Create ECR client
ecr_client = boto3.client('ecr')

# Define repository name
repository_name = 'my-ecr-repo'

# Define tags
tags = [
    {
        'Key': 'AmazonDataZoneProject',
        'Value': '5blxelum5cmckb'
    },
    {
        'Key': 'ProjectUserTagMyTag',
        'Value': 'MyTagValue'
    },
]

try:
    # Create the repository with tags
    response = ecr_client.create_repository(
        repositoryName=repository_name,
        imageScanningConfiguration={
            'scanOnPush': True
        },
        encryptionConfiguration={
            'encryptionType': 'AES256'
        },
        tags=tags
    )

    repository_uri = response['repository']['repositoryUri']
    print(f"Repository created successfully!")
    print(f"Repository URI: {repository_uri}")

except ecr_client.exceptions.RepositoryAlreadyExistsException:
    print(f"Repository {repository_name} already exists")
    # Add tags to existing repository
    ecr_client.tag_resource(
        resourceArn=f"arn:aws:ecr:{ecr_client.meta.region_name}:{boto3.client('sts').get_caller_identity()['Account']}:repository/{repository_name}",
        tags=tags
    )
    # Get the repository URI
    response = ecr_client.describe_repositories(repositoryNames=[repository_name])
    repository_uri = response['repositories'][0]['repositoryUri']
    print(f"Added tags to existing repository")
    print(f"Repository URI: {repository_uri}")
except Exception as e:
    print(f"Error creating repository: {str(e)}")

```

ECR repositories without the `AmazonDataZoneProject` cannot be used. You
must create new ECR repositories with the `AmazonDataZoneProject` tag. Once
tagged with the `AmazonDataZoneProject` tag, this tag cannot be modified or
removed from your ECR repositories. For more information about ECR repositories, see
[https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md").

###### Topics

- [Machine learning in Identity
  Center-based domains](sagemaker-identity-center-based-domains.md "sagemaker-identity-center-based-domains.md")
- [Machine Learning Workflows in IAM-based
  domains](sagemaker-iam-based-domains.md "sagemaker-iam-based-domains.md")
