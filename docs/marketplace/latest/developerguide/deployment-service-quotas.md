The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Service quotas for AWS Marketplace Deployment API

Your AWS account has the following quotas related to the AWS Marketplace Deployment
Service.

Request quotas| **Quota** | **Default** | **Description** |
| --- | --- | --- |
| `Deployment parameter` | 10 | The maximum number of deployment parameters per buyer and product<br>combination |
| `Deployment parameter update frequency` | 100 | The maximum number of times you can update a deployment parameter per<br>24 hours |
| `PutDeploymentParameter throttle` | 1 | The maximum number of `PutDeploymentParameter` requests<br>that you can make per second |
| `ListTagsForResource throttle` | 20 | The maximum number of `ListTagsForResource` requests that<br>you can make per second |
| `TagResource throttle` | 20 | The maximum number of `TagResource` requests that you can<br>make per second |
| `UntagResource throttle` | 20 | The maximum number of `UntagResource` requests that you<br>can make per second |
| `Deployment parameter SecretString name length` | 15,000 | The maximum number of characters for the deployment parameter<br>`SecretString` string |
| `Deployment parameter name length` | 400 | The maximum number of characters in a deployment parameter<br>name |
| `TagList` | 50 | The maximum number of tags per deployment parameter request |
| `ClientToken` | 64 | The maximum number of characters for the `ClientToken`<br>string |
