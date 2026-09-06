

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an ACK capability using eksctl
<a name="ack-create-eksctl"></a>

Create an ACK capability on your Amazon EKS cluster using eksctl.

**Note**  
The following steps require eksctl version `0.215.0` or later. To check your version, run `eksctl version`.

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

Create the ACK capability using eksctl. Replace {{region-code}} with the AWS Region that your cluster is in and replace {{my-cluster}} with the name of your cluster.

```
eksctl create capability \
  --cluster {{my-cluster}} \
  --region {{region-code}} \
  --name ack \
  --type ACK \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/ACKCapabilityRole
```

The command returns immediately, but the capability takes some time to become active.

## Step 3: Verify the capability is active
<a name="_step_3_verify_the_capability_is_active"></a>

Check the capability status:

```
eksctl get capability \
  --cluster {{my-cluster}} \
  --region {{region-code}} \
  --name ack
```

The capability is ready when the status shows `ACTIVE`.

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