

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Authenticate to another account with IRSA
<a name="cross-account-access"></a>

You can configure cross-account IAM permissions either by creating an identity provider from another account’s cluster or by using chained `AssumeRole` operations. In the following examples, *Account A* owns an Amazon EKS cluster that supports IAM roles for service accounts. Pods that are running on that cluster must assume IAM permissions from *Account B*.
+  **Option 1** is simpler but requires Account B to create and manage an OIDC identity provider for Account A’s cluster.
+  **Option 2** keeps OIDC management in Account A but requires role chaining through two `AssumeRole` calls.

## Option 1: Create an identity provider from another account’s cluster
<a name="_option_1_create_an_identity_provider_from_another_accounts_cluster"></a>

In this example, Account A provides Account B with the OpenID Connect (OIDC) issuer URL from their cluster. Account B follows the instructions in [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md) and [Assign IAM roles to Kubernetes service accounts](associate-service-account-role.md) using the OIDC issuer URL from Account A’s cluster. Then, a cluster administrator annotates the service account in Account A’s cluster to use the role from Account B ({{444455556666}}).

```
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::444455556666:role/account-b-role
```

## Option 2: Use chained `AssumeRole` operations
<a name="_option_2_use_chained_assumerole_operations"></a>

In this approach, each account creates an IAM role. Account B’s role trusts Account A, and Account A’s role uses OIDC federation to get credentials from the cluster. The Pod then chains the two roles together using AWS CLI profiles.

### Step 1: Create the target role in Account B
<a name="_step_1_create_the_target_role_in_account_b"></a>

Account B ({{444455556666}}) creates an IAM role with the permissions that Pods in Account A’s cluster need. Account B attaches the desired permission policy to this role, then adds the following trust policy.

 **Trust policy for Account B’s role** — This policy allows Account A’s specific IRSA role to assume this role.

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {}
    }
  ]
}
```

**Important**  
For least privilege, replace the `Principal` ARN with the specific role ARN from Account A instead of using the account root (`arn:aws:iam::111122223333:root`). Using the account root allows *any* IAM principal in Account A to assume this role.

### Step 2: Create the IRSA role in Account A
<a name="_step_2_create_the_irsa_role_in_account_a"></a>

Account A ({{111122223333}}) creates a role with a trust policy that gets credentials from the identity provider created with the cluster’s OIDC issuer address.

 **Trust policy for Account A’s role (OIDC federation)** — This policy allows the EKS cluster’s OIDC provider to issue credentials for this role.

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::111122223333:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
        }
      }
    }
  ]
}
```

**Important**  
For least privilege, add a `StringEquals` condition for the `sub` claim to restrict this role to a specific Kubernetes service account. Without a `sub` condition, any service account in the cluster can assume this role. The `sub` value uses the format `system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT_NAME `. For example, to restrict to a service account named `my-service-account` in the `default` namespace:  

```
"oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:default:my-service-account"
```

### Step 3: Attach the AssumeRole permission to Account A’s role
<a name="_step_3_attach_the_assumerole_permission_to_account_as_role"></a>

Account A attaches a permission policy to the role created in Step 2. This policy allows the role to assume Account B’s role.

 **Permission policy for Account A’s role** — This policy grants `sts:AssumeRole` on Account B’s target role.

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::444455556666:role/account-b-role"
        }
    ]
}
```

### Step 4: Configure the Pod to chain roles
<a name="_step_4_configure_the_pod_to_chain_roles"></a>

The application code for Pods to assume Account B’s role uses two profiles: `account_b_role` and `account_a_role`. The `account_b_role` profile uses the `account_a_role` profile as its source. For the AWS CLI, the `~/.aws/config` file is similar to the following.

```
[profile account_b_role]
source_profile = account_a_role
role_arn=arn:aws:iam::444455556666:role/account-b-role

[profile account_a_role]
web_identity_token_file = /var/run/secrets/eks.amazonaws.com/serviceaccount/token
role_arn=arn:aws:iam::111122223333:role/account-a-role
```

To specify chained profiles for other AWS SDKs, consult the documentation for the SDK that you’re using. For more information, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/).