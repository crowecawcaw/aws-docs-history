

# Data retrieval APIs for AWS CodeDeploy
<a name="awscodedeploy"></a>

AWS CodeDeploy provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="codedeploy-BatchGetApplicationRevisions"></a>[BatchGetApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplicationRevisions.html) | Get information about one or more application revisions | Read | 
| <a name="codedeploy-BatchGetApplications"></a>[BatchGetApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplications.html) | Get information about multiple applications associated with the IAM user | Read | 
| <a name="codedeploy-BatchGetDeploymentGroups"></a>[BatchGetDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentGroups.html) | Get information about one or more deployment groups | Read | 
| <a name="codedeploy-BatchGetDeploymentInstances"></a>[BatchGetDeploymentInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentInstances.html) | Get information about one or more instance that are part of a deployment group | Read | 
| <a name="codedeploy-BatchGetDeploymentTargets"></a>[BatchGetDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentTargets.html) | Return an array of one or more targets associated with a deployment. This method works with all compute types and should be used instead of the deprecated BatchGetDeploymentInstances. The maximum number of targets that can be returned is 25 | Read | 
| <a name="codedeploy-BatchGetDeployments"></a>[BatchGetDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeployments.html) | Get information about multiple deployments associated with the IAM user | Read | 
| <a name="codedeploy-BatchGetOnPremisesInstances"></a>[BatchGetOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetOnPremisesInstances.html) | Get information about one or more on-premises instances | Read | 
| <a name="codedeploy-GetApplication"></a>[GetApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplication.html) | Get information about a single application associated with the IAM user | List | 
| <a name="codedeploy-GetApplicationRevision"></a>[GetApplicationRevision](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplicationRevision.html) | Get information about a single application revision for an application associated with the IAM user | List | 
| <a name="codedeploy-GetDeployment"></a>[GetDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeployment.html) | Get information about a single deployment to a deployment group for an application associated with the IAM user | List | 
| <a name="codedeploy-GetDeploymentConfig"></a>[GetDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentConfig.html) | Get information about a single deployment configuration associated with the IAM user | List | 
| <a name="codedeploy-GetDeploymentGroup"></a>[GetDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentGroup.html) | Get information about a single deployment group for an application associated with the IAM user | List | 
| <a name="codedeploy-GetDeploymentInstance"></a>[GetDeploymentInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentInstance.html) | Get information about a single instance in a deployment associated with the IAM user | List | 
| <a name="codedeploy-GetDeploymentTarget"></a>[GetDeploymentTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentTarget.html) | Return information about a deployment target | Read | 
| <a name="codedeploy-GetOnPremisesInstance"></a>[GetOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetOnPremisesInstance.html) | Get information about a single on-premises instance | List | 
| <a name="codedeploy-ListApplicationRevisions"></a>[ListApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplicationRevisions.html) | Get information about all application revisions for an application associated with the IAM user | List | 
| <a name="codedeploy-ListApplications"></a>[ListApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplications.html) | Get information about all applications associated with the IAM user | List | 
| <a name="codedeploy-ListDeploymentConfigs"></a>[ListDeploymentConfigs](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentConfigs.html) | Get information about all deployment configurations associated with the IAM user | List | 
| <a name="codedeploy-ListDeploymentGroups"></a>[ListDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentGroups.html) | Get information about all deployment groups for an application associated with the IAM user | List | 
| <a name="codedeploy-ListDeploymentInstances"></a>[ListDeploymentInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentInstances.html) | Get information about all instances in a deployment associated with the IAM user | List | 
| <a name="codedeploy-ListDeploymentTargets"></a>[ListDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentTargets.html) | Return an array of target IDs that are associated a deployment | List | 
| <a name="codedeploy-ListDeployments"></a>[ListDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeployments.html) | Get information about all deployments to a deployment group associated with the IAM user, or to get all deployments associated with the IAM user | List | 
| <a name="codedeploy-ListGitHubAccountTokenNames"></a>[ListGitHubAccountTokenNames](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListGitHubAccountTokenNames.html) | List the names of stored connections to GitHub accounts | List | 
| <a name="codedeploy-ListOnPremisesInstances"></a>[ListOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListOnPremisesInstances.html) | Get a list of one or more on-premises instance names | List | 
| <a name="codedeploy-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListTagsForResource.html) | Return a list of tags for the resource identified by a specified ARN. Tags are used to organize and categorize your CodeDeploy resources | List | 