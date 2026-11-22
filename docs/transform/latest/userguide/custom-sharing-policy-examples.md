

# Identity-based policy examples for sharing

The simplest way to grant access is with AWS managed policies, plus the AWS Transform custom actions for sharing that they don't include. The following table shows what each role needs.


| Role | AWS managed policies | 
| --- | --- | 
| Owner | [`AWSTransformCustomManageTransformations`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomManageTransformations) and AWSResourceAccessManagerFullAccess. Also allow transform-custom:PutResourcePolicy and transform-custom:DeleteResourcePolicy. Without them, consumers never get access, and revokes don't finish. To view a TD's resource policy with aws ram get-resource-policies, also allow transform-custom:GetResourcePolicy. | 
| Consumer | [`AWSTransformCustomExecuteTransformations`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations) and AWSResourceAccessManagerResourceShareParticipantAccess. Also allow the following, depending on the share's permission: + To find shared TDs with `atx custom def list`: `transform-custom:ListTransformationPackageMetadata`<br />+ To use the owner's lessons: `transform-custom:ListKnowledgeItems` and `transform-custom:GetKnowledgeItem`<br />+ To download the TD: `transform-custom:GetTransformationPackageUrl`<br />+ To contribute lessons: `transform-custom:ContributeKnowledgeItems`  | 

`AWSResourceAccessManagerFullAccess` lets the owner manage every AWS RAM resource share in the account, not just TD shares. For least privilege, use the following policies instead.

**Owner: Share TDs and manage shares**

The following policy lets an owner share TDs and manage those shares. Its statements use `"Resource": "*"` because a share's ARN doesn't exist until you create it. The conditions on the first two statements limit which shares they can create and change.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CreateTdShares",
      "Effect": "Allow",
      "Action": "ram:CreateResourceShare",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": { "ram:RequestedResourceTypes": "transform-custom:Package" },
        "Null": { "ram:RequestedResourceTypes": "false" }
      }
    },
    {
      "Sid": "AddTdsOrTargetsToShares",
      "Effect": "Allow",
      "Action": "ram:AssociateResourceShare",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": { "ram:RequestedResourceTypes": "transform-custom:Package" }
      }
    },
    {
      "Sid": "ManageAndViewShares",
      "Effect": "Allow",
      "Action": [
        "ram:DisassociateResourceShare",
        "ram:DeleteResourceShare",
        "ram:AssociateResourceSharePermission",
        "ram:GetResourceShares",
        "ram:GetResourceShareAssociations",
        "ram:ListResources",
        "ram:ListResourceSharePermissions"
      ],
      "Resource": "*"
    },
    {
      "Sid": "FindTdsAndWriteSharePolicies",
      "Effect": "Allow",
      "Action": [
        "transform-custom:ListTransformationPackageMetadata",
        "transform-custom:PutResourcePolicy",
        "transform-custom:GetResourcePolicy",
        "transform-custom:DeleteResourcePolicy"
      ],
      "Resource": "*"
    }
  ]
}
```

`CreateTdShares` allows only shares that contain TDs and nothing else. `AddTdsOrTargetsToShares` also allows requests that add only accounts and no resources, because `share create` uses them to invite an account that declined again. Those requests can add accounts to any resource share in your account.

AWS RAM uses your credentials to call `transform-custom:PutResourcePolicy` when a consumer accepts or when you change the permission, and `transform-custom:DeleteResourcePolicy` when you revoke. Without them, the consumer never gets access, or keeps access after you revoke. It calls `transform-custom:GetResourcePolicy` when you view the TD's resource policy with `aws ram get-resource-policies`. Sharing works without it.

**Consumer: Accept shares and run a shared TD with the owner's lessons**

The following policy lets a consumer accept shares and run a shared TD with the owner's lessons:

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "RespondToInvitations",
      "Effect": "Allow",
      "Action": [
        "ram:GetResourceShareInvitations",
        "ram:ListPendingInvitationResources",
        "ram:AcceptResourceShareInvitation",
        "ram:RejectResourceShareInvitation",
        "ram:GetResourceShares",
        "ram:ListResources",
        "ram:ListResourceSharePermissions"
      ],
      "Resource": "*"
    },
    {
      "Sid": "RunSharedTd",
      "Effect": "Allow",
      "Action": "transform-custom:ExecuteTransformation",
      "Resource": "arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade"
    },
    {
      "Sid": "UseOwnerLessons",
      "Effect": "Allow",
      "Action": ["transform-custom:ListKnowledgeItems", "transform-custom:GetKnowledgeItem"],
      "Resource": [
        "arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade",
        "arn:aws:transform-custom:us-east-1:111122223333:package/java17-upgrade/knowledge-item/*"
      ]
    },
    {
      "Sid": "ListTds",
      "Effect": "Allow",
      "Action": "transform-custom:ListTransformationPackageMetadata",
      "Resource": "*"
    }
  ]
}
```

Runs use both lesson actions: `ListKnowledgeItems` on the TD's ARN, and `GetKnowledgeItem` on its lessons, under `knowledge-item/*`. Allow them together. If the share's permission is `Execute`, leave out `UseOwnerLessons`.

To let the consumer download the TD, also allow `transform-custom:GetTransformationPackageUrl` on the TD's ARN. To let it contribute lessons, also allow `transform-custom:ContributeKnowledgeItems` on the TD's ARN.

**Administrator SCP: Keep TD sharing inside your organization**

The following SCP keeps TD sharing inside your organization:

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "DenyExternalSharing",
      "Effect": "Deny",
      "Action": ["ram:CreateResourceShare", "ram:UpdateResourceShare"],
      "Resource": "*",
      "Condition": { "Bool": { "ram:RequestedAllowsExternalPrincipals": "true" } }
    }
  ]
}
```

This SCP blocks sharing any resource type outside the organization, not just TDs. It also blocks `atx custom def share create` for every target, including your own organization and OUs, because the CLI always creates shares that allow external principals. In an organization with this SCP, create shares in the AWS RAM console, or with `aws ram create-resource-share --no-allow-external-principals`.

**Administrator SCP: Block contributing lessons to TDs outside your organization**

The following SCP blocks contributing lessons to TDs outside your organization:

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "DenyContributionOutsideOrg",
      "Effect": "Deny",
      "Action": "transform-custom:ContributeKnowledgeItems",
      "Resource": "*",
      "Condition": { "StringNotEquals": { "aws:ResourceOrgID": "${aws:PrincipalOrgID}" } }
    }
  ]
}
```

The SCP uses the organization of the principal that makes the request, so you don't have to type your organization ID. If the TD's owner account isn't in any organization, `aws:ResourceOrgID` isn't in the request, and the SCP denies the contribution.

**Note**  
Use the exact resource type string `transform-custom:Package` in policies. It's the value that AWS RAM uses in `ram:RequestedResourceTypes` conditions, in `aws ram` filters, and in customer managed permissions.