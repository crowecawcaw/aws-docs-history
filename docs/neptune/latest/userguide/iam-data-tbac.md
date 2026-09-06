

# Tag-based access control for Amazon Neptune data-plane operations
<a name="iam-data-tbac"></a>

Tag-based access control (TBAC) lets you use AWS resource tags and IAM principal tags as conditions in IAM policies and Service Control Policies (SCPs) to control access to Amazon Neptune data-plane operations. With TBAC, you can enforce that only principals whose tags match the tags on a Neptune DB cluster can perform `neptune-db:*` actions against that cluster, without enumerating specific cluster Amazon Resource Names (ARNs) in every policy.

TBAC builds on Neptune's existing security model and complements the [action-based access control](iam-dp-actions.md) data-plane actions.

## How TBAC fits into Neptune's security layers
<a name="iam-data-tbac-security-layers"></a>

Neptune protects your data through multiple, overlapping security mechanisms. TBAC adds an attribute-based authorization layer that works alongside all of them:


**Neptune security layers and how TBAC complements them**  

| Layer | Mechanism | Scope | 
| --- | --- | --- | 
| Network isolation | Virtual private cloud (VPC), security groups, VPC endpoints (PrivateLink) | Controls which hosts can reach Neptune endpoints | 
| Encryption | Transport Layer Security (TLS) 1.3 in transit; AWS KMS-managed encryption at rest | Protects data confidentiality | 
| IAM authentication | AWS Signature Version 4 (SigV4)-signed requests to the Neptune data endpoint | Authenticates the caller | 
| Action-based access control | neptune-db: actions (ReadDataViaQuery, WriteDataViaQuery, etc.) | Controls what operations a principal can perform | 
| Condition keys | neptune-db:QueryLanguage, global context keys | Adds contextual constraints to policies | 
| TBAC | aws:ResourceTag/${TagKey} evaluated against aws:PrincipalTag/${TagKey} | Restricts access based on tag alignment between principal and resource | 
| Administrative tag-based access | aws:ResourceTag, rds:cluster-tag, etc. on management-plane actions | Controls who can manage Neptune infrastructure | 

## Key TBAC concepts
<a name="iam-data-tbac-concepts"></a>

Principal tags  
Tags attached to IAM users, roles, or federated session principals. You can set these via the IAM console, AWS CLI, or identity provider (IdP) Security Assertion Markup Language (SAML) / OpenID Connect (OIDC) attribute mappings.

Resource tags  
Tags attached to Neptune DB clusters using `AddTagsToResource`. These propagate to all instances in the cluster for data-plane policy evaluation.

Condition key variables  
+ `aws:PrincipalTag/{{TagKey}}` — resolves to the tag value on the calling principal.
+ `aws:ResourceTag/{{TagKey}}` — resolves to the tag value on the target Neptune resource.

Supported policy types  
+ **IAM identity policies** — attached to users, groups, or roles.
+ **SCPs** — applied at the AWS Organizations organizational unit (OU) or account level to set permission guardrails.

## Prerequisites for using TBAC
<a name="iam-data-tbac-prerequisites"></a>

Before you can use TBAC with Neptune data-plane operations, you must have the following in place:

1. **Neptune engine version 1.2.0.0 or later** — required for data-plane TBAC support.

1. **IAM authentication enabled** on the Neptune DB cluster.

1. **Tags applied to Neptune DB clusters** — the resource tags that policies will evaluate.

1. **Tags applied to IAM principals** — the principal tags that will be compared against resource tags.

## TBAC policy patterns
<a name="iam-data-tbac-patterns"></a>

The following patterns show common ways to use TBAC in IAM policies for Neptune data-plane operations.

### Deny access when principal and resource tags do not match
<a name="iam-data-tbac-pattern-deny-mismatch"></a>

This is the most common TBAC pattern. It denies all Neptune data-plane actions unless the principal's tags match the resource's tags. You can apply this as an SCP for organization-wide enforcement or as an IAM policy for targeted control.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNeptuneProjectMismatch",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
        }
      }
    },
    {
      "Sid": "DenyNeptuneDepartmentMismatch",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceTag/Department": "${aws:PrincipalTag/Department}"
        }
      }
    }
  ]
}
```

**How it works:** Each statement uses a separate `StringNotEquals` condition for a single tag key. The Deny triggers independently for each tag—if the resource's `Project` tag does not match the principal's `Project` tag, access is denied regardless of the `Department` tag. This ensures a principal tagged with `Project=FraudDetection` can only access Neptune clusters also tagged `Project=FraudDetection`, and similarly for `Department`.

### Deny access when required resource tags are missing
<a name="iam-data-tbac-pattern-deny-missing"></a>

This pattern prevents access to Neptune clusters that have not been properly tagged, ensuring all clusters are enrolled in the TBAC scheme:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNeptuneMissingProjectTag",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:ResourceTag/Project": "true"
        }
      }
    },
    {
      "Sid": "DenyNeptuneMissingDepartmentTag",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:ResourceTag/Department": "true"
        }
      }
    }
  ]
}
```

**How it works:** The `Null` condition evaluates to true when the specified tag key does not exist on the resource. This forces all Neptune clusters to carry the required classification tags before any principal can access them.

### Combining TBAC with action-based access control
<a name="iam-data-tbac-pattern-combined-actions"></a>

TBAC can be combined with specific `neptune-db:` actions to create fine-grained, tag-aware policies:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReadOnlyForMatchingTags",
      "Effect": "Allow",
      "Action": [
        "neptune-db:ReadDataViaQuery",
        "neptune-db:GetQueryStatus",
        "neptune-db:GetEngineStatus"
      ],
      "Resource": "arn:aws:neptune-db:*:*:*/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
        }
      }
    }
  ]
}
```

### Query language restriction with TBAC
<a name="iam-data-tbac-pattern-query-language"></a>

Combine TBAC with the `neptune-db:QueryLanguage` condition key to restrict both which clusters a principal can access and which query languages they can use:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOpenCypherOnlyForMatchingProject",
      "Effect": "Allow",
      "Action": [
        "neptune-db:ReadDataViaQuery",
        "neptune-db:WriteDataViaQuery"
      ],
      "Resource": "arn:aws:neptune-db:*:*:*/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}",
          "neptune-db:QueryLanguage": "OpenCypher"
        }
      }
    }
  ]
}
```

## Using TBAC with service control policies
<a name="iam-data-tbac-scps"></a>

SCPs are ideal for enforcing TBAC because they set permission boundaries across an entire organizational unit (OU) or account without requiring changes to individual IAM policies.

We recommend the following SCP strategy:

1. Apply a Deny-based SCP at the OU level that blocks `neptune-db:*` when tags don't match.

1. Apply a second statement denying access to untagged resources.

1. Your individual accounts can retain their Allow policies for specific `neptune-db:` actions—the SCP acts as a guardrail.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNeptuneProjectMismatch",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceTag/Project": "${aws:PrincipalTag/Project}"
        }
      }
    },
    {
      "Sid": "DenyNeptuneDepartmentMismatch",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:ResourceTag/Department": "${aws:PrincipalTag/Department}"
        }
      }
    },
    {
      "Sid": "DenyNeptuneMissingProjectTag",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:ResourceTag/Project": "true"
        }
      }
    },
    {
      "Sid": "DenyNeptuneMissingDepartmentTag",
      "Effect": "Deny",
      "Action": "neptune-db:*",
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:ResourceTag/Department": "true"
        }
      }
    }
  ]
}
```

## Implementing TBAC for Neptune
<a name="iam-data-tbac-implementation"></a>

### Step 1: Define your tag taxonomy
<a name="iam-data-tbac-step-taxonomy"></a>

Choose tag keys that represent your organizational boundaries. Common patterns:


**Example tag taxonomy**  

| Tag key | Purpose | Example values | 
| --- | --- | --- | 
| Project | Application or workload identifier | FraudDetection, RecommendationEngine | 
| Department | Business unit or cost center | Engineering, Finance, Analytics | 
| Environment | Deployment stage | production, staging, development | 
| Team | Owning team | graph-platform, data-science | 

### Step 2: Tag your Neptune DB clusters
<a name="iam-data-tbac-step-tag-clusters"></a>

Use the AWS CLI to add the required classification tags to your Neptune DB clusters:

```
aws neptune add-tags-to-resource \
  --resource-name arn:aws:rds:{{us-east-1}}:{{123456789012}}:cluster:{{my-neptune-cluster}} \
  --tags Key=Project,Value=FraudDetection Key=Department,Value=Engineering
```

### Step 3: Tag your IAM principals
<a name="iam-data-tbac-step-tag-principals"></a>

Use the AWS CLI to tag IAM roles with the same keys and values used on your Neptune clusters. For IAM roles:

```
aws iam tag-role \
  --role-name {{NeptuneAppRole}} \
  --tags Key=Project,Value=FraudDetection Key=Department,Value=Engineering
```

For federated users, pass tags via SAML/OIDC session tags using `aws:PrincipalTag` attributes from your identity provider.

### Step 4: Deploy the TBAC policy
<a name="iam-data-tbac-step-deploy"></a>

Attach as an SCP for organization-wide enforcement, or as an IAM policy for targeted control.

### Step 5: Protect tag integrity
<a name="iam-data-tbac-step-protect-tags"></a>

Restrict who can modify tags on Neptune resources and IAM principals:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyTagModification",
      "Effect": "Deny",
      "Action": [
        "rds:AddTagsToResource",
        "rds:RemoveTagsFromResource"
      ],
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "aws:TagKeys": ["Project", "Department"]
        }
      }
    }
  ]
}
```

## Important considerations for TBAC
<a name="iam-data-tbac-considerations"></a>
+ **Propagation delay** — Changes to IAM policies take up to 10 minutes to apply to Neptune resources. Changes to cluster tags (adding, modifying, or removing tags) take approximately 5 minutes to propagate to data-plane policy evaluation. Plan for this delay when updating tags on active clusters.
+ **Cluster-level granularity** — You apply tags to Neptune DB clusters at the cluster level. All instances in a cluster share the same policy evaluation. TBAC does not provide sub-graph or vertex/edge-level access control.
+ **IAM authentication required** — TBAC only applies when IAM authentication is enabled on the cluster. Connections without IAM auth bypass these policies entirely.
+ **Tag immutability** — Secure your tagging operations. If a principal can modify their own tags or the resource tags, they can bypass TBAC controls. Use SCPs or permission boundaries to restrict `iam:TagRole`, `iam:TagUser`, `rds:AddTagsToResource`, and `rds:RemoveTagsFromResource`.
+ **Null tag handling** — If a principal lacks a tag that the policy references via `${aws:PrincipalTag/{{Key}}}`, the variable resolves to an empty string. Design your policies to handle this case (the "missing tags" deny pattern above addresses this for resource tags).
+ **Multiple condition keys** — When multiple condition keys appear in the same `Condition` block, they are evaluated with AND logic. For `StringNotEquals`, a Deny only triggers when *all* specified conditions are true simultaneously. To deny on *any* single tag mismatch, use separate policy statements for each tag key (as shown in the patterns above).

## Relationship to existing Neptune security features
<a name="iam-data-tbac-relationship"></a>


**How TBAC complements existing Neptune security features**  

| Existing feature | What it controls | How TBAC complements it | 
| --- | --- | --- | 
| VPC / Security Groups | Network-level access to port 8182 | TBAC adds identity-aware authorization on top of network controls | 
| IAM Authentication (SigV4) | Verifies caller identity | TBAC uses the authenticated identity's tags for authorization decisions | 
| Action-based access control | Which operations (read/write/delete/load) a principal can perform | TBAC adds which clusters a principal can target, based on tag alignment | 
| neptune-db:QueryLanguage condition key | Which query languages (Gremlin, openCypher, SPARQL) are permitted | Can be combined with TBAC in the same policy statement | 
| Administrative tag-based access (rds:\* actions) | Who can manage Neptune infrastructure | TBAC extends the same tag-based pattern to data-plane (neptune-db:\*) actions | 
| AWS KMS encryption | Data confidentiality at rest | Orthogonal—TBAC controls authorization, not encryption | 