# Required permissions

You need the following permissions to deploy the ParallelCluster API with
Terraform:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:GetTemplate"
 ],
 "Resource": "arn:aws:cloudformation:`us-east-1`:`111122223333`:stack/*",
 "Effect": "Allow",
 "Sid": "CloudFormationRead"
 },
 {
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:CreateChangeSet"
 ],
 "Resource": "arn:aws:cloudformation:`us-east-1`:`111122223333`:stack/MyParallelClusterAPI*",
 "Effect": "Allow",
 "Sid": "CloudFormationWrite"
 },
 {
 "Action": [
 "cloudformation:CreateChangeSet"
 ],
 "Resource": [
 "arn:aws:cloudformation:`us-east-1`:`111122223333`:aws:transform/Include",
 "arn:aws:cloudformation:`us-east-1`:`111122223333`:aws:transform/Serverless-2016-10-31"
 ],
 "Effect": "Allow",
 "Sid": "CloudFormationTransformWrite"
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:`us-east-1`:`111122223333`:*-aws-parallelcluster/parallelcluster/*/api/ParallelCluster.openapi.yaml",
 "arn:aws:s3:`us-east-1`:`111122223333`:*-aws-parallelcluster/parallelcluster/*/layers/aws-parallelcluster/lambda-layer.zip"
 ],
 "Effect": "Allow",
 "Sid": "S3ParallelClusterArtifacts"
 },
 {
 "Action": [
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:GetRole",
 "iam:CreatePolicy",
 "iam:DeletePolicy",
 "iam:GetPolicy",
 "iam:GetRolePolicy",
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy",
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy",
 "iam:ListPolicyVersions"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/*",
 "arn:aws:iam::`111122223333`:policy/*"
 ],
 "Effect": "Allow",
 "Sid": "IAM"
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/ParallelClusterLambdaRole-*",
 "arn:aws:iam::`111122223333`:role/APIGatewayExecutionRole-*"
 ],
 "Effect": "Allow",
 "Sid": "IAMPassRole"
 },
 {
 "Action": [
 "lambda:CreateFunction",
 "lambda:DeleteFunction",
 "lambda:GetFunction",
 "lambda:PublishLayerVersion",
 "lambda:DeleteLayerVersion",
 "lambda:GetLayerVersion",
 "lambda:TagResource",
 "lambda:UntagResource"
 ],
 "Resource": [
 "arn:aws:lambda:`us-east-1`:`111122223333`:layer:PCLayer-*",
 "arn:aws:lambda:`us-east-1`:`111122223333`:function:*-ParallelClusterFunction-*"
 ],
 "Effect": "Allow",
 "Sid": "Lambda"
 },
 {
 "Action": [
 "logs:CreateLogGroup",
 "logs:DeleteLogGroup",
 "logs:DescribeLogGroups",
 "logs:PutRetentionPolicy",
 "logs:TagLogGroup",
 "logs:UntagLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/lambda/*-ParallelClusterFunction-*"
 ],
 "Effect": "Allow",
 "Sid": "Logs"
 },
 {
 "Action": [
 "apigateway:DELETE",
 "apigateway:GET",
 "apigateway:PATCH",
 "apigateway:POST",
 "apigateway:PUT",
 "apigateway:UpdateRestApiPolicy"
 ],
 "Resource": [
 "arn:aws:apigateway:`us-east-1`::/restapis",
 "arn:aws:apigateway:`us-east-1`::/restapis/*",
 "arn:aws:apigateway:`us-east-1`::/tags/*"
 ],
 "Effect": "Allow",
 "Sid": "APIGateway"
 }
 ]
}`

```
