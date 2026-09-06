

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an ACK capability using the AWS CLI
<a name="ack-create-cli"></a>

Create an ACK capability on your Amazon EKS cluster using the AWS CLI. This procedure walks you through creating an IAM role and verifying the capability is active.

## Prerequisites
<a name="_prerequisites"></a>
+  ** AWS CLI** – Version `2.12.3` or later. To check your version, run `aws --version`. For more information, see [Installing](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS Command Line Interface User Guide.
+  ** `kubectl` ** – A command line tool for working with Kubernetes clusters. For more information, see [Set up `kubectl` and `eksctl`](install-kubectl.md).

## Step 1: Create an IAM Capability Role
<a name="_step_1_create_an_iam_capability_role"></a>

Create a trust policy file:

```
cat > ack-trust-policy.json << 'EOF'
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
  --role-name ACKCapabilityRole \
  --assume-role-policy-document file://ack-trust-policy.json
```

Attach the `AdministratorAccess` managed policy to the role:

```
aws iam attach-role-policy \
  --role-name ACKCapabilityRole \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

**Important**  
The suggested `AdministratorAccess` policy grants broad permissions and is intended to streamline getting started. For production use, replace this with a custom policy that grants only the permissions needed for the specific AWS services you plan to manage with ACK. For guidance on creating least-privilege policies, see [Configure ACK permissions](ack-permissions.md) and [Security considerations for EKS Capabilities](capabilities-security.md).

## Step 2: Create the ACK capability
<a name="_step_2_create_the_ack_capability"></a>

Create the ACK capability resource on your cluster. Replace {{region-code}} with the AWS Region that your cluster is in and replace {{my-cluster}} with the name of your cluster.

```
aws eks create-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name my-ack \
  --type ACK \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/ACKCapabilityRole \
  --delete-propagation-policy RETAIN
```

The command returns immediately, but the capability takes some time to become active as EKS creates the required capability infrastructure and components. EKS will install the Kubernetes Custom Resource Definitions related to this capability in your cluster as it is being created.

**Note**  
If you receive an error that the cluster doesn’t exist or you don’t have permissions, verify:  
The cluster name is correct
Your AWS CLI is configured for the correct region
You have the required IAM permissions

## Step 3: Verify the capability is active
<a name="_step_3_verify_the_capability_is_active"></a>

Wait for the capability to become active. Replace {{region-code}} with the AWS Region that your cluster is in and replace {{my-cluster}} with the name of your cluster.

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name my-ack \
  --query 'capability.status' \
  --output text
```

The capability is ready when the status shows `ACTIVE`. Don’t continue to the next step until the status is `ACTIVE`.

You can also view the full capability details:

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name my-ack
```

## Step 4: Verify custom resources are available
<a name="_step_4_verify_custom_resources_are_available"></a>

After the capability is active, verify that ACK custom resources are available in your cluster:

```
kubectl api-resources | grep services.k8s.aws
```

You should see a number of APIs listed for AWS resources.

**Note**  
The capability for AWS Controllers for Kubernetes will install a number of CRDs for a variety of AWS resources.

## Next steps
<a name="_next_steps"></a>
+  [ACK concepts](ack-concepts.md) - Understand ACK concepts and get started
+  [Configure ACK permissions](ack-permissions.md) - Configure IAM permissions for other AWS services
+  [Working with capability resources](working-with-capabilities.md) - Manage your ACK capability resource