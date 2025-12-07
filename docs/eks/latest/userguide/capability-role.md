**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS capability IAM role

EKS Capabilities require a capability IAM role (or capability role) to be configured.
Capabilities use this role to perform actions on AWS services and to access Kubernetes resources in your cluster through automatically created access entries.

Before you can specify a capability role during capability creation, you must create the IAM role with the appropriate trust policy and permissions for the capability type.
Once this IAM role is created, it can be reused for any number of capability resources.

## Capability role requirements

The capability role must meet the following requirements:

- The role must be in the same AWS account as the cluster and capability resource
- The role must have a trust policy that allows the EKS capabilities service to assume the role
- The role must have permissions appropriate for the capability type and use case requirements (see [Permissions by capability type](#capability-permissions "#capability-permissions"))

## Trust policy for capability roles

All capability roles must include the following trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "capabilities.eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

This trust policy allows EKS to:

- Assume the role to perform AWS API operations
- Tag sessions for audit and tracking purposes

## Permissions by capability type

The IAM permissions required depend on which capability you’re using and your deployment model.

###### Note

For production deployments using IAM Role Selectors with ACK, or when using kro or Argo CD without AWS service integration, the Capability Role may not require any IAM permissions beyond the trust policy.

**kro (Kube Resource Orchestrator)**

No IAM permissions are required. You can create a capability role with no attached policies. kro only requires Kubernetes RBAC permissions to create and manage Kubernetes resources.

**AWS Controllers for Kubernetes (ACK)**

ACK supports two permission models:

- **Simple setup (development/testing)**: Add AWS service permissions directly to the Capability Role. This works well for getting started, single-account deployments, or when all users need the same permissions.
- **Production best practice**: Use IAM Role Selectors to implement least-privilege access. With this approach, the Capability Role only needs `sts:AssumeRole` permission to assume service-specific roles. You don’t add AWS service permissions (like S3 or RDS) to the Capability Role itself—those permissions are granted to individual IAM roles that are mapped to specific namespaces.

IAM Role Selectors enable:

    + Namespace-level permission isolation
    + Cross-account resource management
    + Team-specific IAM roles
    + Least-privilege security model


    Example Capability Role policy for IAM Role Selector approach:



    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": [
            "arn:aws:iam::111122223333:role/ACK-S3-Role",
            "arn:aws:iam::111122223333:role/ACK-RDS-Role",
            "arn:aws:iam::444455556666:role/ACKCrossAccountRole"
          ]
        }
      ]
    }
    ```

    For detailed ACK permission configuration including IAM Role Selectors, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md").

**Argo CD**

No IAM permissions required by default. Optional permissions may be needed for:

- **AWS Secrets Manager**: If using Secrets Manager to store Git repository credentials
- **AWS CodeConnections**: If using CodeConnections for Git repository authentication

Example policy for Secrets Manager and CodeConnections:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "arn:aws:secretsmanager:region:account-id:secret:argocd/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "codeconnections:UseConnection",
        "codeconnections:GetConnection"
      ],
      "Resource": "arn:aws:codeconnections:region:account-id:connection/*"
    }
  ]
}
```

For detailed Argo CD permission requirements, see [Argo CD considerations](argocd-considerations.md "argocd-considerations.md").

## Check for an existing capability role

You can use the following procedure to check if your account already has a capability IAM role suitable for your use case.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**.
3. Search the list of roles for your capability role name (for example, `ACKCapabilityRole` or `ArgoCDCapabilityRole`).
4. If a role exists, select it to view the attached policies and trust relationship.
5. Choose **Trust relationships**, and then choose **Edit trust policy**.
6. Verify that the trust relationship matches the [capability trust policy](#capability-trust-policy "#capability-trust-policy"). If it doesn’t match, update the trust policy.
7. Choose **Permissions** and verify that the role has the appropriate permissions for your capability type and use case.

## Creating a capability IAM role

You can use the AWS Management Console or the AWS CLI to create a capability role.

**AWS Management Console**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**, then **Create role**.
3. Under **Trusted entity type**, select **Custom trust policy**.
4. Copy and paste the [capability trust policy](#capability-trust-policy "#capability-trust-policy") into the trust policy editor.
5. Choose **Next**.
6. On the **Add permissions** tab, select or create policies appropriate for your capability type (see [Permissions by capability type](#capability-permissions "#capability-permissions")). For kro, you can skip this step.
7. Choose **Next**.
8. For **Role name**, enter a unique name for your role, such as `ACKCapabilityRole`, `ArgoCDCapabilityRole`, or `kroCapabilityRole`.
9. For **Description**, enter descriptive text such as `Amazon EKS - ACK capability role`.
10. Choose **Create role**.

**AWS CLI**

1. Copy the [capability trust policy](#capability-trust-policy "#capability-trust-policy") to a file named `capability-trust-policy.json`.
2. Create the role. Replace `ACKCapabilityRole` with your desired role name.

```
aws iam create-role \
  --role-name ACKCapabilityRole \
  --assume-role-policy-document file://capability-trust-policy.json
```

3. Attach the required IAM policies to the role. For ACK, attach policies for the AWS services you want to manage. For Argo CD, attach policies for Secrets Manager or CodeConnections if needed. For kro, you can skip this step.

Example for ACK with S3 permissions:

```
aws iam put-role-policy \
  --role-name ACKCapabilityRole \
  --policy-name S3Management \
  --policy-document file://s3-policy.json
```

## Troubleshooting capability role issues

**Capability creation fails with "Invalid IAM role"**

Verify that:

- The role exists in the same account as the cluster
- The trust policy matches the [capability trust policy](#capability-trust-policy "#capability-trust-policy")
- You have `iam:PassRole` permission for the role

**Capability shows permission errors**

Verify that:

- The role has the necessary IAM permissions for the capability type
- The access entry exists on the cluster for the role
- Additional Kubernetes permissions are configured if required (see [Additional Kubernetes permissions](capabilities-security.md#additional-kubernetes-permissions "capabilities-security.md#additional-kubernetes-permissions"))

**ACK resources fail with "permission denied" errors**

Verify that:

- The role has the necessary IAM permissions for your use case
- For ACK controllers that reference secrets, ensure you’ve associated the `AmazonEKSSecretReaderPolicy` access entry policy scoped to the appropriate namespaces.

For more troubleshooting guidance, see [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").
