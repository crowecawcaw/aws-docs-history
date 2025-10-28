We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Controlling Access to

Amazon ML Resources -with IAM

AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for
your users. Using IAM, you can create and manage AWS users, groups, and roles, and use
permissions to allow and deny their access to AWS resources.By using IAM with Amazon Machine Learning (Amazon ML),
you can control whether users in your organization can use specific AWS resources and whether
they can perform a task using specific Amazon ML API actions.

IAM enables you to:

- Create users and groups under your AWS account.
- Assign unique security credentials to each user under your AWS account
- Control each user's permissions to perform tasks using AWS resources
- Easily share your AWS resources with the users in your AWS account
- Create roles for your AWS account and manage permissions to them to define the users or
  services that can assume them
- You can create roles in IAM and manage permissions to control which operations can be
  performed by the entity, or AWS service, that assumes the role. You can also define which
  entity is allowed to assume the role.
  If your organization already has IAM identities, you can use them to grant permissions to
  perform tasks using AWS resources.

For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## IAM Policy Syntax

An IAM policy is a JSON document that consists of one or more statements. Each
statement has the following structure:

```
{
    "Statement":[{
        "Effect":"effect",
        "Action":"action",
        "Resource":"arn",
        "Condition":{
            "condition operator":{
                "key":"value"
            }
        }
    }]
}
```

A policy statement includes the following elements:

- **Effect:** Controls permission to use the resources and
  API actions that you will specify later in the statement. Valid values are
  `Allow` and  `Deny`. By default, IAM users don't have permission
  to use resources and API actions, so all requests are denied. An explicit
  `Allow` overrides the default. An explicit `Deny` overrides any
  `Allows`.
- **Action**: The specific API action or actions for which
  you are granting or denying permission.
- **Resource**: The resource that's affected by the action.
  To specify a resource in the statement, you use its Amazon Resource Name (ARN).
- **Condition (optional)**: Controls when your policy will be
  in effect.

To simplify creating and managing IAM policies, you can use the AWS Policy
Generator and the IAM Policy Simulator.

## Specifying IAM Policy Actions for Amazon MLAmazon ML

In an IAM policy statement, you can specify an API action for any service that supports
IAM. When you create a policy statement for Amazon ML API actions, prepend
`machinelearning:` to the name of the API action, as shown in the following
examples:

- `machinelearning:CreateDataSourceFromS3`
- `machinelearning:DescribeDataSources`
- `machinelearning:DeleteDataSource`
- `machinelearning:GetDataSource`

To specify multiple actions in a single statement, separate them with commas:

```
"Action": ["machinelearning:action1", "machinelearning:action2"]
```

You can also specify multiple actions using wildcards. For example, you can specify all
actions whose name begins with the word "Get":

```
"Action": "machinelearning:Get*"
```

To specify all Amazon ML actions, use the \* wildcard:

```
"Action": "machinelearning:*"
```

For the complete list of Amazon ML API actions, see the [Amazon Machine Learning API
Reference](../APIReference.md "../APIReference.md").

## Specifying ARNs for Amazon ML Resources in IAM Policies

IAM policy statements apply to one or more resources. You specify resources for your
policies by their ARNs.

To specify the ARNs for Amazon ML resources, use the following format:

"Resource":
`arn:aws:machinelearning:region:account:resource-type/identifier`

The following examples show how to specify common ARNs.

Datasource ID: `my-s3-datasource-id`

```

"Resource":
arn:aws:machinelearning:<region>:<your-account-id>:datasource/my-s3-datasource-id

```

ML model ID: `my-ml-model-id`

```

"Resource":
arn:aws:machinelearning:<region>:<your-account-id>:mlmodel/my-ml-model-id

```

Batch prediction ID: `my-batchprediction-id`

```

"Resource":
arn:aws:machinelearning:<region>:<your-account-id>:batchprediction/my-batchprediction-id

```

Evaluation ID: `my-evaluation-id`

```

"Resource": arn:aws:machinelearning:<region>:<your-account-id>:evaluation/my-evaluation-id

```

## Example Policies for Amazon MLs

**Example 1: Allow users to read machine learning resources
metadata**

The following policy allows a user or group read the metadata of datasources, ML models,
batch predictions, and evaluations by performing [DescribeDataSources](../APIReference/API_DescribeDataSources.md "../APIReference/API_DescribeDataSources.md"), [DescribeMLModels](../APIReference/API_DescribeMLModels.md "../APIReference/API_DescribeMLModels.md"), [DescribeBatchPredictions](../APIReference/API_DescribeBatchPredictions.md "../APIReference/API_DescribeBatchPredictions.md"), [DescribeEvaluations](../APIReference/API_DescribeEvaluations.md "../APIReference/API_DescribeEvaluations.md"), [GetDataSource](../APIReference/API_GetDataSource.md "../APIReference/API_GetDataSource.md"), [GetMLModel](../APIReference/API_GetMLModel.md "../APIReference/API_GetMLModel.md"), [GetBatchPrediction](../APIReference/API_GetBatchPrediction.md "../APIReference/API_GetBatchPrediction.md"), and [GetEvaluation](../APIReference/API_GetEvaluation.md "../APIReference/API_GetEvaluation.md") actions on the specified
resource(s). The Describe \* operations permissions can't be restricted to a particular
resource.

JSON

```
`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [
 "machinelearning:Get*" ], "Resource": [
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:datasource/S3-DS-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:datasource/REDSHIFT-DS-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:mlmodel/ML-MODEL-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:batchprediction/BP-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:evaluation/EV-ID1"
 ] }, { "Effect": "Allow", "Action": [ "machinelearning:Describe*" ], "Resource": [ "*" ] } ]
 }`

```

**Example 2: Allow users to create machine learning resources**

The following policy allows a user or group to create machine learning datasources, ML
models, batch predictions, and evaluations by performing `CreateDataSourceFromS3`,
`CreateDataSourceFromRedshift`, `CreateDataSourceFromRDS`,
`CreateMLModel`, `CreateBatchPrediction`, and
`CreateEvaluation` actions. You can't restrict the permissions for these actions
to a specific resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "machinelearning:CreateDataSourceFrom*",
 "machinelearning:CreateMLModel",
 "machinelearning:CreateBatchPrediction",
 "machinelearning:CreateEvaluation"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

**Example 3: Allow users to create and delete) real-time endpoints and
perform real-time predictions on an ML model**

The following policy allows users or groups to create and delete real-time endpoints and
perform real-time predictions for a specific ML model by performing
`CreateRealtimeEndpoint`, `DeleteRealtimeEndpoint`, and
`Predict` actions on that model.

JSON

```
`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [
 "machinelearning:CreateRealtimeEndpoint", "machinelearning:DeleteRealtimeEndpoint",
 "machinelearning:Predict" ], "Resource": [
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:mlmodel/ML-MODEL"
 ] } ] }`

```

**Example 4: Allow users to update and delete specific
resources**

The following policy allows a user or group to update and delete specific resources in
your AWS account by giving them permission to perform `UpdateDataSource`,
`UpdateMLModel`, `UpdateBatchPrediction`,
`UpdateEvaluation`, `DeleteDataSource`, `DeleteMLModel`,
`DeleteBatchPrediction`, and `DeleteEvaluation` actions on those
resources in your account.

JSON

```
`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [
 "machinelearning:Update*", "machinelearning:DeleteDataSource", "machinelearning:DeleteMLModel",
 "machinelearning:DeleteBatchPrediction", "machinelearning:DeleteEvaluation" ], "Resource": [
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:datasource/S3-DS-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:datasource/REDSHIFT-DS-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:mlmodel/ML-MODEL-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:batchprediction/BP-ID1",
 "arn:aws:machinelearning:`us-east-1`:`123456789012`:evaluation/EV-ID1"
 ] } ] }`

```

**Example 5: Allow any Amazon MLaction**

The following policy allows a user or group to use any Amazon ML action. Because this policy
grants full access to all of your machine learning resources, restrict it to administrators
only.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "machinelearning:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
