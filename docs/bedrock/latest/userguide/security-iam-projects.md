# Managing IAM policies on Projects

Amazon Bedrock Projects support direct IAM policy attachment, allowing you to manage access control at the project resource level. This provides an alternative to managing policies on IAM users and roles.

## Understanding Project-Level IAM Policies

Project-level IAM policies allow you to:

- **Centralize access control**: Define permissions directly on the project resource
- **Simplify management**: Update access without modifying individual user/role policies
- **Audit easily**: View all permissions for a project in one place
- **Delegate administration**: Allow project owners to manage access to their projects

## Attaching IAM Policies to Projects

### Attach a Policy to Grant Access

Attach an IAM policy directly to a project to grant permissions:

```
import boto3
import json

iam = boto3.client('iam', region_name='us-east-1')

project_arn = "arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123"

# Define the identity-based policy document
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowTeamAlphaAccess",
            "Effect": "Allow",
            "Action": [
                "bedrock-mantle:ListTagsForResources",
                "bedrock-mantle:GetProject"
            ],
            "Resource": project_arn
        }
    ]
}

policy_json = json.dumps(policy_document)

# Create a managed policy
create_response = iam.create_policy(
    PolicyName="TeamAlphaAccessPolicy",
    PolicyDocument=policy_json,
    Description="Grants Team Alpha read access to the Bedrock project"
)

policy_arn = create_response['Policy']['Arn']
print(f"Policy created: {policy_arn}")

# Attach the policy to alice (IAM user)
iam.attach_user_policy(
    UserName="alice",
    PolicyArn=policy_arn
)
print("Policy attached to alice")

# Attach the policy to bob (IAM user)
iam.attach_user_policy(
    UserName="bob",
    PolicyArn=policy_arn
)
print("Policy attached to bob")

# Attach the policy to TeamAlphaRole (IAM role)
iam.attach_role_policy(
    RoleName="TeamAlphaRole",
    PolicyArn=policy_arn
)
print("Policy attached to TeamAlphaRole")
```

### Grant Full Project Access to a Team

Allow a team full access to manage and use a project:

```
import boto3
import json

iam = boto3.client('iam', region_name='us-east-1')

project_arn = "arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123"

# Identity-based policy — no Principal block needed
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "FullProjectAccess",
            "Effect": "Allow",
            "Action": "bedrock-mantle:*",
            "Resource": project_arn
        }
    ]
}

# Create a managed policy
create_response = iam.create_policy(
    PolicyName="DataScienceFullAccess",
    PolicyDocument=json.dumps(policy_document),
    Description="Grants DataScienceTeamRole full access to the Bedrock project"
)

policy_arn = create_response['Policy']['Arn']
print(f"Policy created: {policy_arn}")

# Attach to the DataScienceTeamRole
iam.attach_role_policy(
    RoleName="DataScienceTeamRole",
    PolicyArn=policy_arn
)

print("Full access policy attached to DataScienceTeamRole")
```

### Grant Read-Only Access

Attach a policy that allows viewing project details and making inference requests only:

```
import boto3
import json

iam = boto3.client('iam', region_name='us-east-1')

project_arn = "arn:aws:bedrock-mantle:us-east-1:123456789012:project/proj_abc123"

# Identity-based policy — no Principal block needed
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadOnlyAccess",
            "Effect": "Allow",
            "Action": [
                "bedrock-mantle:CreateInference",
                "bedrock-mantle:GetProject",
                "bedrock-mantle:ListProjects",
                "bedrock-mantle:ListTagsForResources"
            ],
            "Resource": project_arn
        }
    ]
}

# Create a managed policy
create_response = iam.create_policy(
    PolicyName="ReadOnlyAccessPolicy",
    PolicyDocument=json.dumps(policy_document),
    Description="Grants viewer1 and viewer2 read-only access to the Bedrock project"
)

policy_arn = create_response['Policy']['Arn']
print(f"Policy created: {policy_arn}")

# Attach to viewer1
iam.attach_user_policy(
    UserName="viewer1",
    PolicyArn=policy_arn
)
print("Policy attached to viewer1")

# Attach to viewer2
iam.attach_user_policy(
    UserName="viewer2",
    PolicyArn=policy_arn
)
print("Policy attached to viewer2")
```
