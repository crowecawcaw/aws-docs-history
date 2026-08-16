**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability using the AWS CLI

Create an Argo CD capability on your Amazon EKS cluster using the AWS CLI. This procedure walks you through creating an IAM role, configuring AWS Identity Center integration, and verifying the capability is active.

## Prerequisites

- **AWS CLI** – Version `2.12.3` or later. To check your version, run `aws --version`. For more information, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the AWS Command Line Interface User Guide.
- **`kubectl`** – A command line tool for working with Kubernetes clusters. For more information, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- **AWS Identity Center configured** – Argo CD requires AWS Identity Center for authentication. Local users are not supported. If you don’t have AWS Identity Center set up, see [Getting started with AWS Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") to create an Identity Center instance, and [Add users](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md") and [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") to create users and groups for Argo CD access.
- **At least one user or group in AWS Identity Center** – You must have at least one user or group configured in your Identity Center instance to assign Argo CD RBAC role mappings and provide access to the Argo CD UI.

## Step 1: Create an IAM capability role

Create a trust policy file:

```
cat > argocd-trust-policy.json << 'EOF'
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
  --role-name ArgoCDCapabilityRole \
  --assume-role-policy-document file://argocd-trust-policy.json
```

###### Note

If you plan to use the optional integrations with AWS Secrets Manager or AWS CodeConnections, add permissions to the role.
For IAM policy examples and configuration guidance, see [Manage application secrets with AWS Secrets Manager](integration-secrets-manager.md "integration-secrets-manager.md") and [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md "integration-codeconnections.md").

## (Optional) Configure a private endpoint

By default, the Argo CD UI and API endpoint are publicly accessible over the internet. If you need to restrict access, you can configure a VPC endpoint.
This is recommended for environments with strict network security requirements.

### Create a VPC endpoint for EKS Capabilities

Create an interface VPC endpoint for the EKS Capabilities service in your VPC.
Replace `vpc-id`, `subnet-id-1`, `subnet-id-2`, `sg-id`, and `region-code` with your own values:

```
aws ec2 create-vpc-endpoint \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.`region-code`.eks-capabilities \
  --vpc-id `vpc-xxxxxxxx` \
  --subnet-ids `subnet-xxxxxxxx`
            `subnet-yyyyyyyy` \
  --security-group-ids `sg-xxxxxxxx` \
  --region `region-code`

```

###### Note

- The subnets should be in different Availability Zones for high availability.
- The security group must allow inbound HTTPS (port 443) traffic from the networks that need to access the Argo CD UI and API.
- Note the VPC endpoint ID returned by this command—you’ll need it when creating the capability.

### Verify the VPC endpoint is available

```
aws ec2 describe-vpc-endpoints \
  --vpc-endpoint-ids `vpce-xxxxxxxx` \
  --query 'VpcEndpoints[0].State' \
  --output text \
  --region `region-code`

```

Wait until the state shows `available` before proceeding.

## Step 2: Create the Argo CD capability

Create the Argo CD capability resource on your cluster.

First, set environment variables for your Identity Center configuration:

```
# Get your Identity Center instance ARN (replace region if your IDC instance is in a different region)
export IDC_INSTANCE_ARN=$(aws sso-admin list-instances --region `region-code` --query 'Instances[0].InstanceArn' --output text)

# Get a user ID for RBAC mapping (replace with your username and region if needed)
export IDC_USER_ID=$(aws identitystore list-users \
  --region `region-code` \
  --identity-store-id $(aws sso-admin list-instances --region `region-code` --query 'Instances[0].IdentityStoreId' --output text) \
  --query 'Users[?UserName==`your-username`].UserId' --output text)

echo "IDC_INSTANCE_ARN=$IDC_INSTANCE_ARN"
echo "IDC_USER_ID=$IDC_USER_ID"
```

Create the capability with Identity Center integration. Replace `region-code` with the AWS Region where your cluster is located, `my-cluster` with your cluster name, and `idc-region-code` with the region code where your Identity Center instance is located:

```
aws eks create-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-argocd \
  --type ARGOCD \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/ArgoCDCapabilityRole \
  --delete-propagation-policy RETAIN \
  --configuration '{
    "argoCd": {
      "awsIdc": {
        "idcInstanceArn": "'$IDC_INSTANCE_ARN'",
        "idcRegion": "'[.replaceable]`idc-region-code`'"
      },
      "rbacRoleMappings": [{
        "role": "ADMIN",
        "identities": [{
          "id": "'$IDC_USER_ID'",
          "type": "SSO_USER"
        }]
      }]
    }
  }'
```

If you configured a VPC endpoint for private access, include the `network-configuration` parameter to create the capability with a private endpoint.
Replace `vpce-xxxxxxxx` with your VPC endpoint ID:

```
aws eks create-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-argocd \
  --type ARGOCD \
  --role-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/ArgoCDCapabilityRole \
  --delete-propagation-policy RETAIN \
  --network-configuration '{
    "elasticNetworkInterfaces": {
      "vpcEndpointId": "'[.replaceable]`vpce-xxxxxxxx`'"
    }
  }' \
  --configuration '{
    "argoCd": {
      "awsIdc": {
        "idcInstanceArn": "'$IDC_INSTANCE_ARN'",
        "idcRegion": "'[.replaceable]`idc-region-code`'"
      },
      "rbacRoleMappings": [{
        "role": "ADMIN",
        "identities": [{
          "id": "'$IDC_USER_ID'",
          "type": "SSO_USER"
        }]
      }]
    }
  }'
```

The command returns immediately, but the capability takes some time to become active as EKS creates the required capability infrastructure and components.
EKS installs the Kubernetes Custom Resource Definitions (CRDs) in your cluster during capability creation.

###### Note

If you receive an error that the cluster doesn’t exist or you don’t have permissions, verify:

- The cluster name is correct
- Your AWS CLI is configured for the correct region
- You have the required IAM permissions

## Step 3: Verify the capability is active

Wait for the capability to become active. Replace `region-code` with the AWS Region where your cluster is located and `my-cluster` with your cluster name.

```
aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-argocd \
  --query 'capability.status' \
  --output text
```

The capability is ready when the status shows `ACTIVE`.
Wait until the status is `ACTIVE` before you continue to the next step.

You can also view the full capability details:

```
aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name my-argocd
```

## Step 4: Verify custom resources are available

After the capability is active, verify that Argo CD custom resources are available in your cluster:

```
kubectl api-resources | grep argoproj.io
```

You should see `Application` and `ApplicationSet` resource types listed.

## Next steps

- [Working with Argo CD](working-with-argocd.md "working-with-argocd.md") - Configure repositories, register clusters, and create Applications
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - Multi-cluster architecture and advanced configuration
- [Working with capability resources](working-with-capabilities.md "working-with-capabilities.md") - Manage your Argo CD capability resource
