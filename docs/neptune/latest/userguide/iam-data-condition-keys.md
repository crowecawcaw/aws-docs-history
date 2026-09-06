

# IAM condition keys for accessing data in Amazon Neptune
<a name="iam-data-condition-keys"></a>

[Using condition keys](security-iam-access-manage.md#iam-using-condition-keys), you can specify conditions in an IAM policy statement so that the statement takes effect only when the conditions are true.

The condition keys that you can use in Neptune data-access policy statements fall into the following categories:
+ [Global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)   –   The subset of AWS global condition keys that Neptune supports in data-access policy statements is listed [below](#iam-data-global-condition-keys).
+ [Service-specific condition keys](#iam-neptune-condition-keys)   –   These are keys defined by Neptune specifically for use in data-access policy statements. At present there is only one, [neptune-db:QueryLanguage](#neptune-db-query-language), which grants access only if a specific query language is being used.

## AWS global condition context keys supported by Neptune in data-access policy statements
<a name="iam-data-global-condition-keys"></a>

The following table lists the subset of [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) that Amazon Neptune supports for use in data-access policy statements:


**Global condition keys that you can use in data-access policy statements**  

| Condition Keys | Description | Type | 
| --- | --- | --- | 
| [`aws:CurrentTime`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-currenttime) | Filters access by the current date and time of the request. | String | 
| [`aws:EpochTime`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-epochtime) | Filters access by date and time of the request expressed as a UNIX epoch value. | Numeric | 
| [`aws:PrincipalAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalaccount) | Filters access by the account to which the requesting principal belongs. | String | 
| [`aws:PrincipalArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalarn) | Filters access by the ARN of the principal that made the request. | String | 
| [`aws:PrincipalIsAWSService`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalisawsservice) | Allows access only if the call is being made directly by an AWS service principal. | Boolean | 
| [`aws:PrincipalOrgID`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid) | Filters access by the identifier of the organization in AWS Organizations to which the requesting principal belongs. | String | 
| [`aws:PrincipalOrgPaths`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgpaths) | Filters access by the AWS Organizations path for the principal who is making the request. | String | 
| [`aws:PrincipalTag`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag) | Filters access by a tag attached to the principal making the request. | String | 
| [`aws:PrincipalType`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltype) | Filters access by the type of principal making the request. | String | 
| [`aws:RequestedRegion`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion) | Filters access by the AWS Region that was called in the request. | String | 
| [`aws:RequestTag`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) | Filters access based on the presence of tag key-value pairs in the request. | String | 
| [`aws:ResourceTag`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) | Filters access based on tag key-value pairs attached to the resource. | String | 
| [`aws:SecureTransport`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-securetransport) | Allows access only if the request was sent using SSL. | Boolean | 
| [`aws:SourceIp`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceip) | Filters access by the requester's IP address. | String | 
| [`aws:TagKeys`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) | (Multivalue key) Filters access based on the presence of tag keys in the request. | ArrayOfString | 
| [`aws:TokenIssueTime`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tokenissuetime) | Filters access by the date and time that temporary security credentials were issued. | String | 
| [`aws:UserAgent`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-useragent) | Filters access by the requester's client application. | String | 
| [`aws:userid`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-userid) | Filters access by the requester's principal identifier. | String | 
| [`aws:ViaAWSService`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-viaawsservice) | Allows access only if an AWS service made the request on your behalf. | Boolean | 

## Neptune service-specific condition keys
<a name="iam-neptune-condition-keys"></a>

Neptune supports the following service-specific condition key for IAM policies:


**Neptune service-specific condition keys**  

| Condition Keys | Description | Type | 
| --- | --- | --- | 
| neptune-db:QueryLanguage | Filters data access by the query language being used.<br />Valid values are: `Gremlin`, `OpenCypher`, and `Sparql`.<br />Supported actions are `ReadDataViaQuery`, `WriteDataViaQuery`, `DeleteDataViaQuery`, `GetQueryStatus`, and `CancelQuery`. | String | 