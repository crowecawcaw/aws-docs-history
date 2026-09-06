

# Data retrieval APIs for AWS Security Token Service
<a name="awssecuritytokenservice"></a>

AWS Security Token Service provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="sts-GetAccessKeyInfo"></a>[GetAccessKeyInfo](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetAccessKeyInfo.html) | Obtain details about the access key id passed as a parameter to the request | Read | 
| <a name="sts-GetCallerIdentity"></a>[GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) | Obtain details about the IAM identity whose credentials are used to call the API | Read | 
| <a name="sts-GetServiceBearerToken"></a>[GetServiceBearerToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_bearer.html) | Obtain a STS bearer token for an AWS root user, IAM role, or an IAM user | Read | 
| <a name="sts-GetSessionToken"></a>[GetSessionToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html) | Obtain a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for an AWS account or IAM user | Read | 