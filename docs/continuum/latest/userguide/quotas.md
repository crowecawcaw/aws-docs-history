

# Quotas for AWS Continuum
<a name="quotas"></a>

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of AWS Continuum. The default quotas for your account might change depending on regional factors, payment history, fraudulent usage, or approval of a quota increase request.

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific.

To request a quota increase for AWS Continuum, contact your AWS account team.

Your AWS account has the following quotas related to AWS Continuum.


| Resource | Default | Description | 
| --- | --- | --- | 
| Integrations | 10 | The maximum number of integrations, such as GitHub integrations, that you can connect in this account in the current Region. | 
| Environments | 10 | The maximum number of environments that you can create in this account in the current Region. | 
| Repositories per environment | 10 | The maximum number of code repositories that you can add to a single environment across all integrations. | 
| Collectors | 1 | The maximum number of AWS Continuum collectors that you can create in this account in the current Region. | 
| Collectors per environment | 100 | The maximum number of AWS Continuum collectors that you can associate with a single environment. | 

**Note**  
If an existing environment contains more than 10 repositories, you can view the environment and update settings that do not change its repository selection. To change its repository selection or start a new scan, reduce the selection to your account's current repository quota or fewer.