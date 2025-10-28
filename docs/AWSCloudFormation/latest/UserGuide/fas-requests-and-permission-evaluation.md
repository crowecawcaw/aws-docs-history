# Forward access sessions (FAS) requests and permission

evaluation

When creating, updating, and deleting CloudFormation stacks, users can optionally specify an
IAM role ARN. If no role is provided, CloudFormation uses its default service mechanism to
interact with other AWS services. In this scenario, the caller must have the necessary
permissions for the resources being managed. Alternatively, when a user supplies their own
IAM role, CloudFormation will assume that role to perform service interactions on their
behalf.

Regardless of whether the user provides an IAM role, CloudFormation generates a new
scoped-down FAS token for each resource operation. Consequently, [FAS-related condition keys](../../../IAM/latest/UserGuide/access_forward_access_sessions.md#access_fas_policy_conditions "../../../IAM/latest/UserGuide/access_forward_access_sessions.md#access_fas_policy_conditions"), including `aws:ViaAWSService`, are
populated in both scenarios.

The use of FAS affects how IAM policies are evaluated during CloudFormation operations. When
creating a stack with a template that includes resources affected by FAS-related condition
keys, permission denials may occur.

###### Example IAM policy

Consider the following IAM policy. `Statement2` will consistently prevent
the creation of an `AWS::KMS::Key` resource in CloudFormation. The restriction
will be enforced consistently, whether or not an IAM role is provided during the stack
operation. This is because the `aws:ViaAWSService` condition key is always
set to `true` due to the use of FAS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "kms:CreateKey"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Statement2",
 "Effect": "Deny",
 "Action": [
 "kms:CreateKey"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 }
 ]
}`

```

###### Example stack template

For example, when a user creates a stack with the following example template,
`aws:ViaAWSService` is set to `true`, and role permissions
will be overridden by the FAS policy. Stack creation will be affected by
`Statement2` of the IAM policy, which denies the
`CreateKey` action. This results in a permission denied error.

```
Resources:
  myPrimaryKey:
    Type: AWS::KMS::Key
    Properties:
      Description: An example multi-Region primary key
      KeyPolicy:
        Version: '2012-10-17'
        Id: key-default-1
        Statement:
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !Join
                - ''
                - - 'arn:aws:iam::'
                  - !Ref AWS::AccountId
                  - ':root'
            Action: kms:*
            Resource: '*'
```

For more information about FAS, see [Forward access
sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") in the _IAM User Guide_.

###### Note

Most resources adhere to this behavior. However, if you experience unexpected success
or failure when creating, updating, or deleting a resource, and your IAM policy
includes FAS-related condition keys, it's likely that the resource in question belongs
to a small subset of resources that don't follow this standard pattern.
