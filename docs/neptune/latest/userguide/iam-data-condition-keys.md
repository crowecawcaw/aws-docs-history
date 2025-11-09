# IAM condition keys for accessing data in Amazon Neptune

[Using condition keys](security-iam-access-manage.md#iam-using-condition-keys "security-iam-access-manage.md#iam-using-condition-keys"), you can
specify conditions in an IAM policy statement so that the statement takes effect
only when the conditions are true.

The condition keys that you can use in Neptune data-access policy statements
fall into the following categories:

- [Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")   –  
  The subset of AWS global condition keys that Neptune supports in data-access
  policy statements is listed [below](#iam-data-global-condition-keys "#iam-data-global-condition-keys").
- [Service-specific condition keys](#iam-neptune-condition-keys "#iam-neptune-condition-keys")   –  
  These are keys defined by Neptune specifically for use in data-access policy
  statements. At present there is only one, [neptune-db:QueryLanguage](#neptune-db-query-language "#neptune-db-query-language"), which grants
  access only if a specific query language is being used.

## AWS global condition context keys supported by Neptune in data-access policy statements

The following table lists the subset of [AWS
global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") that Amazon Neptune supports for use in data-access
policy statements:

| Global condition keys that you can use in data-access policy statements                                                                                                                                                                          | Condition Keys                                                                                                       | Description | Type |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------- | ---- |
| [`aws:CurrentTime`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-currenttime "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-currenttime")                               | Filters access by the current date and time of the request.                                                          | `String`    |
| [`aws:EpochTime`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-epochtime "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-epochtime")                                     | Filters access by date and time of the request expressed as a UNIX epoch value.                                      | `Numeric`   |
| [`aws:PrincipalAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount")                | Filters access by the account to which the requesting principal belongs.                                             | `String`    |
| [`aws:PrincipalArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalarn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalarn")                            | Filters access by the ARN of the principal that made the request.                                                    | `String`    |
| [`aws:PrincipalIsAWSService`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalisawsservice "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalisawsservice") | Allows access only if the call is being made directly by an AWS service principal.                                   | `Boolean`   |
| [`aws:PrincipalOrgID`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid")                      | Filters access by the identifier of the organization in AWS Organizations to which the requesting principal belongs. | `String`    |
| [`aws:PrincipalOrgPaths`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgpaths "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgpaths")             | Filters access by the AWS Organizations path for the principal who is making the request.                            | `String`    |
| [`aws:PrincipalTag`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltag")                            | Filters access by a tag attached to the principal making the request.                                                | `String`    |
| [`aws:PrincipalType`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltype "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltype")                         | Filters access by the type of principal making the request.                                                          | `String`    |
| [`aws:RequestedRegion`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion")                   | Filters access by the AWS Region that was called in the request.                                                     | `String`    |
| [`aws:SecureTransport`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-securetransport "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-securetransport")                   | Allows access only if the request was sent using SSL.                                                                | `Boolean`   |
| [`aws:SourceIp`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip")                                        | Filters access by the requester's IP address.                                                                        | `String`    |
| [`aws:TokenIssueTime`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tokenissuetime "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tokenissuetime")                      | Filters access by the date and time that temporary security credentials were issued.                                 | `String`    |
| [`aws:UserAgent`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-useragent "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-useragent")                                     | Filters access by the requester's client application.                                                                | `String`    |
| [`aws:userid`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-userid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-userid")                                              | Filters access by the requester's principal identifier.                                                              | `String`    |
| [`aws:ViaAWSService`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-viaawsservice "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-viaawsservice")                         | Allows access only if an AWS service made the request on your behalf.                                                | `Boolean`   |

## Neptune service-specific condition keys

Neptune supports the following service-specific condition key for IAM policies:

| Neptune service-specific condition keys | Condition Keys                                                                                                                                                                                                                                          | Description | Type |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---- |
| `neptune-db:QueryLanguage`              | Filters data access by the query language being used.<br>Valid values are: `Gremlin`, `OpenCypher`,<br>and `Sparql`.<br>Supported actions are `ReadDataViaQuery`,<br>`WriteDataViaQuery`, `DeleteDataViaQuery`,<br>`GetQueryStatus`, and `CancelQuery`. | `String`    |
