# Add users and set up service accounts

## Fine grained access control - our recommendation

Users are differentiated based on their Kubernetes username. The user’s
Kubernetes username is defined in their Access Entry. To ensure two human users have
distinct usernames, there are two options:

1. Recommended - Multiple human users can use the same role as long as each
   one has their own distinct session name that will persist between sessions.
   By default, Kubernetes usernames for IAM roles are in the format
   `arn:aws:sts::{ACCOUNT_ID}:assumed-role/{ROLE_NAME}/{SESSION_NAME}`. With this
   default, users will already be differentiated by session name. An Admin has a few
   ways to enforce unique session names per user.
   - SSO login - Users using SSO login will by default have a session
     name tied to their AWS username
   - Central credentials vending service - For enterprise customers,
     they may have some internal credential vending service that users
     can call to get credentials with their identity.
   - Role based enforcement - Require IAM users to set their
     `aws:username` as their role session name when they assume an IAM role
     in your AWS account. Documentation on how to do this is here: [https://aws.amazon.com/blogs/security/easily-control-naming-individual-iam-role-sessions/](https://aws.amazon.com/blogs/security/easily-control-naming-individual-iam-role-sessions/ "https://aws.amazon.com/blogs/security/easily-control-naming-individual-iam-role-sessions/")

2. If 2 Data Scientists are using different access entries (different IAM
   role or user), they will always be counted as different users.

**Creating access entry**

Required IAM policy for data scientist role:

- `eks:DescribeCluster`

Required access entry policies

- `AmazonSagemakerHyperpodSpacePolicy` - scoped to namespace DS should create spaces in
- `AmazonSagemakerHyperpodSpaceTemplatePolicy` - scoped to
  “jupyter-k8s-shared” namespace

## Private and Public spaces

We support 2 types of sharing patterns: “Public” and “OwnerOnly”. Both the
“AccessType” and “OwnershipType” fields use these 2 values.

- AccessType: Public spaces can be accessed by anyone with permissions in
  the namespace, while OwnerOnly can only be accessed by the space creator as
  well as administrator users. Administrator users are defined with the
  following criteria:
- OwnershipType: Public spaces can be modified/deleted by anyone with
  permissions in the namespace, OwnerOnly can be modified/deleted by the
  creator or the Admin.

Admin users are defined by:

1. Part of the `system:masters` Kubernetes group
2. Part of the Kubernetes group defined in the CLUSTER_ADMIN_GROUP
   environment variable in the helm chart.

A user’s groups can be configured using EKS access entries. A space can be defined
as “Public” or “OwnerOnly” by configuring the spec in the object:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  labels:
    app.kubernetes.io/name: jupyter-k8s
  name: example-workspace
spec:
  displayName: "Example Workspace"
  image: "public.ecr.aws/sagemaker/sagemaker-distribution:3.4.2-cpu"
  desiredStatus: "Running"
  ownershipType: "Public"/"OwnerOnly"
  accessType: "Public"/"OwnerOnly"
  # more fields here
```
