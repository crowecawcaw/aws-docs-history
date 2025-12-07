**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an ACK capability using eksctl

This topic describes how to create an AWS Controllers for Kubernetes (ACK) capability using eksctl.

###### Note

The following steps require eksctl version `0.220.0` or later.
To check your version, run `eksctl version`.

## Step 1: Create an IAM Capability Role

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

###### Important

The suggested `AdministratorAccess` policy grants broad permissions and is intended to streamline getting started.
For production use, replace this with a custom policy that grants only the permissions needed for the specific AWS services you plan to manage with ACK.
For guidance on creating least-privilege policies, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md") and [Security considerations for EKS Capabilities](capabilities-security.md "capabilities-security.md").

###### Important

This policy grants permissions for S3 bucket management with `"Resource": "*"`, which allows operations on all S3 buckets.

For production use: \* Restrict the `Resource` field to specific bucket ARNs or name patterns \* Use IAM condition keys to limit access by resource tags \* Grant only the minimum permissions needed for your use case

For other AWS services, see [Configure ACK permissions](ack-permissions.md "ack-permissions.md").

Attach the policy to the role:

```
aws iam attach-role-policy \
  --role-name ACKCapabilityRole \
  --policy-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):policy/ACKS3Policy
```

## Step 2: Create the ACK capability

Create the ACK capability using eksctl.
Replace `region-code` with the AWS Region that your cluster is in and replace `my-cluster` with the name of your cluster.

```
eksctl create capability \
  --cluster [.replaceable]`my-cluster` \
  --region [.replaceable]`region-code` \
  --name ack \
  --type ACK \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/ACKCapabilityRole \
  --ack-service-controllers s3
```

###### Note

The `--ack-service-controllers` flag is optional.
If omitted, ACK enables all available controllers.
For better performance and security, consider enabling only the controllers you need.
You can specify multiple controllers: `--ack-service-controllers s3,rds,dynamodb`

The command returns immediately, but the capability takes some time to become active.

## Step 3: Verify the capability is active

Check the capability status:

```
eksctl get capability \
  --cluster [.replaceable]`my-cluster` \
  --region [.replaceable]`region-code` \
  --name ack
```

The capability is ready when the status shows `ACTIVE`.

## Step 4: Verify custom resources are available

After the capability is active, verify that ACK custom resources are available in your cluster:

```
kubectl api-resources | grep services.k8s.aws
```

You should see a number of APIs listed for AWS resources.

###### Note

The capability for AWS Controllers for Kubernetes will install a number of CRDs for a variety of AWS resources.

## Next steps

- [ACK concepts](ack-concepts.md "ack-concepts.md") - Understand ACK concepts and get started
- [Configure ACK permissions](ack-permissions.md "ack-permissions.md") - Configure IAM permissions for other AWS services
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your ACK capability resource
