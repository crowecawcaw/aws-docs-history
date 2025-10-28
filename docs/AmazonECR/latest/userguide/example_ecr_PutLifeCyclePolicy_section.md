# Use `PutLifeCyclePolicy` with an AWS SDK or CLI

The following code examples show how to use `PutLifeCyclePolicy`.

CLI

**AWS CLI**

**To create a lifecycle policy**

The following `put-lifecycle-policy` example creates a lifecycle policy for the specified repository in the default registry for an account.

```
`aws ecr put-lifecycle-policy \
 --repository-name `"project-a/amazon-ecs-sample"` \
 --lifecycle-policy-text `"file://policy.json"``

```

Contents of `policy.json`:

```
{
   "rules": [
       {
           "rulePriority": 1,
           "description": "Expire images older than 14 days",
           "selection": {
               "tagStatus": "untagged",
               "countType": "sinceImagePushed",
               "countUnit": "days",
               "countNumber": 14
           },
           "action": {
               "type": "expire"
           }
       }
   ]
}
```

Output:

```
{
   "registryId": "<aws_account_id>",
   "repositoryName": "project-a/amazon-ecs-sample",
   "lifecyclePolicyText": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Expire images older than 14 days\",\"selection\":{\"tagStatus\":\"untagged\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":14},\"action\":{\"type\":\"expire\"}}]}"
}
```

For more information, see [Lifecycle Policies](LifecyclePolicies.md "LifecyclePolicies.md") in the _Amazon ECR User Guide_.

- For API details, see
  [PutLifeCyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-life-cycle-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-life-cycle-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples").

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def put_lifecycle_policy(self, repository_name: str, lifecycle_policy_text: str):
        """
        Puts a lifecycle policy for an ECR repository.

        :param repository_name: The name of the repository to put the lifecycle policy for.
        :param lifecycle_policy_text: The lifecycle policy text to put.
        """
        try:
            self.ecr_client.put_lifecycle_policy(
                repositoryName=repository_name,
                lifecyclePolicyText=lifecycle_policy_text,
            )
            print(f"Put lifecycle policy for repository {repository_name}.")
        except ClientError as err:
            logger.error(
                "Couldn't put lifecycle policy for repository %s. Here's why %s",
                repository_name,
                err.response["Error"]["Message"],
            )
            raise



```

Example that puts an expiration date policy.

```
    def put_expiration_policy(self):
        """
        Puts an expiration policy on the ECR repository.
        """
        policy_json = {
            "rules": [
                {
                    "rulePriority": 1,
                    "description": "Expire images older than 14 days",
                    "selection": {
                        "tagStatus": "any",
                        "countType": "sinceImagePushed",
                        "countUnit": "days",
                        "countNumber": 14,
                    },
                    "action": {"type": "expire"},
                }
            ]
        }

        self.ecr_wrapper.put_lifecycle_policy(
            self.repository_name, json.dumps(policy_json)
        )



```

- For API details, see
  [PutLifeCyclePolicy](../../../goto/boto3/ecr-2015-09-21/PutLifeCyclePolicy.md "../../../goto/boto3/ecr-2015-09-21/PutLifeCyclePolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon ECR with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
