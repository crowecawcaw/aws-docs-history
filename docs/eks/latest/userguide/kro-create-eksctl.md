**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a kro capability using eksctl

This topic describes how to create a kro (Kube Resource Orchestrator) capability using eksctl.

###### Note

The following steps require eksctl version `0.220.0` or later.
To check your version, run `eksctl version`.

## Step 1: Create an IAM Capability Role

Create a trust policy file:

```
 cat > kro-trust-policy.json << 'EOF'
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
EOF
```

Create the IAM role:

```
 aws iam create-role \
  --role-name KROCapabilityRole \
  --assume-role-policy-document file://kro-trust-policy.json
```

###### Note

Unlike ACK and Argo CD, kro does not require additional IAM permissions beyond the trust policy.
kro operates entirely within your cluster and does not make AWS API calls.

## Step 2: Create the kro capability

Create the kro capability using eksctl.
Replace `region-code` with the AWS Region that your cluster is in and replace `my-cluster` with the name of your cluster.

```
 eksctl create capability \
  --region <replaceable>region-code</replaceable> \
  --cluster <replaceable>my-cluster</replaceable> \
  --name my-kro \
  --type KRO \
  --role-arn arn:aws:iam::[.replaceable]<literal>111122223333</literal>:role/KROCapabilityRole
```

The command returns immediately, but the capability takes some time to become active.

## Step 3: Verify the capability is active

Check the capability status.
Replace `region-code` with the AWS Region that your cluster is in and replace `my-cluster` with the name of your cluster.

```
 eksctl get capability \
  --region <replaceable>region-code</replaceable> \
  --cluster <replaceable>my-cluster</replaceable> \
  --name my-kro
```

The capability is ready when the status shows `ACTIVE`.

## Step 4: Grant permissions to manage Kubernetes resources

By default, kro can only create and manage ResourceGraphDefinitions and their instances.
To allow kro to create and manage the underlying Kubernetes resources defined in your ResourceGraphDefinitions, associate the `AmazonEKSClusterAdminPolicy` access policy with the capability’s access entry.

Get the capability role ARN:

```
 CAPABILITY_ROLE_ARN=$(aws eks describe-capability \
  --region <replaceable>region-code</replaceable> \
  --cluster <replaceable>my-cluster</replaceable> \
  --name my-kro \
  --query 'capability.roleArn' \
  --output text)
```

Associate the cluster admin policy:

```
 aws eks associate-access-policy \
  --region <replaceable>region-code</replaceable> \
  --cluster <replaceable>my-cluster</replaceable> \
  --principal-arn $CAPABILITY_ROLE_ARN \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy \
  --access-scope type=cluster
```

###### Important

The `AmazonEKSClusterAdminPolicy` grants broad permissions to create and manage all Kubernetes resources and is intended to streamline getting started.
For production use, create more restrictive RBAC policies that grant only the permissions needed for the specific resources your ResourceGraphDefinitions will manage.
For guidance on configuring least-privilege permissions, see [Configure kro permissions](kro-permissions.md "kro-permissions.md") and [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").

## Step 5: Verify custom resources are available

After the capability is active, verify that kro custom resources are available in your cluster:

```
 kubectl api-resources | grep kro.run
```

You should see the `ResourceGraphDefinition` resource type listed.

## Next steps

- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand kro concepts and resource composition
- [kro concepts](kro-concepts.md "kro-concepts.md") - Learn about SimpleSchema, CEL expressions, and composition patterns
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your kro capability resource
