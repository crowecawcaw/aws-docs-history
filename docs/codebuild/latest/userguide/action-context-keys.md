# AWS CodeBuild condition keys

AWS CodeBuild provides a set of condition keys that you can use in IAM policies to enforce
your organizational policies on CodeBuild resources such as projects and fleets. The condition
keys cover most of the CodeBuild API request contexts, including network settings, credential
configurations and compute restrictions.

###### Topics

- [Enforce VPC connectivity
  settings on your projects and fleets](#action-context-keys-example-overrideVPC "#action-context-keys-example-overrideVPC")
- [Prevent unauthorized
  modifications to project buildspec](#action-context-keys-example-overridebuildspec "#action-context-keys-example-overridebuildspec")
- [Restrict compute types for
  your builds](#action-context-keys-example-computechoice "#action-context-keys-example-computechoice")
- [Control environment variable
  settings](#action-context-keys-example-env-variables "#action-context-keys-example-env-variables")
- [Use variables in condition key
  names](#action-context-keys-example-variables "#action-context-keys-example-variables")
- [Check
  the existence of attributes in API requests](#action-context-keys-example-env-denyoverride "#action-context-keys-example-env-denyoverride")

## Enforce VPC connectivity

settings on your projects and fleets

This policy allows the caller to use the selected VPCs, subnets, and security groups
when creating CodeBuild projects and fleets. For more information about multivalued
context keys, see [Single-valued vs. multivalued context keys](../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "codebuild:CreateProject",
 "codebuild:CreateFleet"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "codebuild:vpcConfig.vpcId": [
 "vpc-01234567890abcdef",
 "vpc-abcdef01234567890"
 ],
 "codebuild:vpcConfig.subnets": [
 "subnet-1234abcd",
 "subnet-5678abcd"
 ],
 "codebuild:vpcConfig.securityGroupIds": [
 "sg-12345678abcdefghij",
 "sg-01234567abcdefghij"
 ]
 }
 }
 }]
}`

```

## Prevent unauthorized

modifications to project buildspec

This policy does not allow the caller to override the buildspec in the
`buildspecOverride` field.

###### Note

The `codebuild:source.buildspec` condition key supports only the Null
operator to check the existence of the API field. It doesn’t evaluate the content of
the buildspec.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "codebuild:StartBuild",
 "Resource": "*"
 }, {
 "Effect": "Deny",
 "Action": "codebuild:StartBuild",
 "Resource": "*",
 "Condition": {
 "Null": {
 "codebuild:source.buildspec": "false"
 }
 }
 }]
}`

```

## Restrict compute types for

your builds

This policy allows creating fleets that can build with only `c5.large` or
`m5.large`
[compute instance type](build-env-ref-compute-types.md#environment-reserved-capacity.instance-types "build-env-ref-compute-types.md#environment-reserved-capacity.instance-types").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "codebuild:CreateFleet",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "codebuild:computeConfiguration.instanceType": ["c5.large", "m5.large"]
 }
 }
 }]
}`

```

## Control environment variable

settings

This policy allows the caller to override the `STAGE` environment variable
to be either `BETA` or `GAMMA`. It also explicitly denies
overriding `STAGE` to be `PRODUCTION`, and denies overriding the
`MY_APP_VERSION` environment variable. For multiple value context keys,
please see [Single-valued vs. multivalued context keys](../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuild"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "codebuild:environment.environmentVariables/STAGE.value": [
 "BETA",
 "GAMMA"
 ]
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "codebuild:StartBuild"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "codebuild:environment.environmentVariables/STAGE.value": "PRODUCTION"
 },
 "ForAnyValue:StringEquals": {
 "codebuild:environment.environmentVariables.name": [
 "MY_APP_VERSION"
 ]
 }
 }
 }
 ]
}`

```

## Use variables in condition key

names

You can use variables in condition key names like
`secondarySources/${sourceIdentifier}.location` and
`secondaryArtifacts/${artifactIdentifier}.location`, where you can
specify your secondary [source](../APIReference/API_ProjectSource.md "../APIReference/API_ProjectSource.md") or secondary [artifact](../APIReference/API_ProjectArtifacts.md "../APIReference/API_ProjectArtifacts.md") identifier in the IAM policy. The policy below allows the caller
to create a project with a specific source location for the secondary source
`mySecondSource`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codebuild:CreateProject",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "codebuild:secondarySources/mySecondSource.location": "my-source-location"
 }
 }
 }
 ]
}`

```

## Check

the existence of attributes in API requests

CodeBuild supports condition keys to check the existence of some fields in the API
request. The policy enforces the VPC requirement when creating or updating
projects.

```

{
    "Version": "2012-10-17"		 	 	 		 	 	 ,
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "codebuild:CreateProject",
            "codebuild:UpdateProject"
        ],
        "Resource": "*",
        "Condition": {
            "Null": {
                "codebuild:vpcConfig.vpcId": "false"
            }
        }
    }]
}

```
