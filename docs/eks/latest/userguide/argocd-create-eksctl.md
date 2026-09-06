

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an Argo CD capability using eksctl
<a name="argocd-create-eksctl"></a>

Create an Argo CD capability on your Amazon EKS cluster using eksctl.

**Note**  
The following steps require eksctl version `0.215.0` or later. To check your version, run `eksctl version`.

## Prerequisites
<a name="_prerequisites"></a>
+  ** AWS Identity Center configured** – Argo CD requires AWS Identity Center for authentication. Local users are not supported. If you don’t have AWS Identity Center set up, see [Getting started with AWS Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) to create an Identity Center instance, and [Add users](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html) and [Add groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html) to create users and groups for Argo CD access.
+  **At least one user or group in AWS Identity Center** – You must have at least one user or group configured in your Identity Center instance to assign Argo CD RBAC role mappings and provide access to the Argo CD UI.

## Step 1: Create an IAM Capability Role
<a name="_step_1_create_an_iam_capability_role"></a>

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

**Note**  
For this basic setup, no additional IAM policies are needed. If you plan to use Secrets Manager for repository credentials or CodeConnections, you’ll need to add permissions to the role. For IAM policy examples and configuration guidance, see [Manage application secrets with AWS Secrets Manager](integration-secrets-manager.md) and [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md).

## Step 2: Get your AWS Identity Center configuration
<a name="step_2_get_your_shared_aws_identity_center_configuration"></a>

Get your Identity Center instance ARN and user ID for RBAC configuration:

```
# Get your Identity Center instance ARN
aws sso-admin list-instances --query 'Instances[0].InstanceArn' --output text

# Get a user ID for admin access (replace 'your-username' with your Identity Center username)
aws identitystore list-users \
  --identity-store-id $(aws sso-admin list-instances --query 'Instances[0].IdentityStoreId' --output text) \
  --query 'Users[?UserName==`your-username`].UserId' --output text
```

Note these values - you’ll need them in the next step.

## (Optional) Configure a private endpoint
<a name="_optional_configure_a_private_endpoint"></a>

By default, the Argo CD UI and API endpoint are publicly accessible over the internet. If you need to restrict access, you can configure a VPC endpoint. This is recommended for environments with strict network security requirements.

### Create a VPC endpoint for EKS Capabilities
<a name="_create_a_vpc_endpoint_for_eks_capabilities"></a>

Create an interface VPC endpoint for the EKS Capabilities service in your VPC. Replace {{vpc-id}}, {{subnet-id-1 subnet-id-2}}, {{sg-id}}, and {{region-code}} with your own values:

```
aws ec2 create-vpc-endpoint \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.{{region-code}}.eks-capabilities \
  --vpc-id {{vpc-id}} \
  --subnet-ids {{subnet-id-1 subnet-id-2}} \
  --security-group-ids {{sg-id}} \
  --region {{region-code}}
```

**Note**  
The subnets should be in different Availability Zones for high availability.
The security group must allow inbound HTTPS (port 443) traffic from the networks that need to access the Argo CD UI and API.
Note the VPC endpoint ID returned by this command—you’ll need it when creating the capability.

### Verify the VPC endpoint is available
<a name="_verify_the_vpc_endpoint_is_available"></a>

```
aws ec2 describe-vpc-endpoints \
  --vpc-endpoint-ids {{vpce-xxxxxxxx}} \
  --query 'VpcEndpoints[0].State' \
  --output text \
  --region {{region-code}}
```

Wait until the state shows `available` before proceeding.

## Step 3: Create an eksctl configuration file
<a name="_step_3_create_an_eksctl_configuration_file"></a>

Create a file named `argocd-capability.yaml` with the following content. Replace the placeholder values with your cluster’s name, cluster’s region, IAM role ARN, Identity Center instance ARN, Identity Center region, and user ID:

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: {{my-cluster}}
  region: {{cluster-region-code}}

capabilities:
  - name: my-argocd
    type: ARGOCD
    roleArn: {{arn:aws:iam::111122223333:role/ArgoCDCapabilityRole}}
    deletePropagationPolicy: RETAIN
    configuration:
      argocd:
        awsIdc:
          idcInstanceArn: {{arn:aws:sso:::instance/ssoins-123abc}}
          idcRegion: {{idc-region-code}}
        rbacRoleMappings:
          - role: ADMIN
            identities:
              - id: {{38414300-1041-708a-01af-5422d6091e34}}
                type: SSO_USER
```

**Note**  
You can add multiple users or groups to the RBAC mappings. For groups, use `type: SSO_GROUP` and provide the group ID. Available roles are `ADMIN`, `EDITOR`, and `VIEWER`.

If you configured a VPC endpoint for private access, add the `networkConfiguration` section to the capability definition. Replace {{vpce-xxxxxxxx}} with your VPC endpoint ID:

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: {{my-cluster}}
  region: {{cluster-region-code}}

capabilities:
  - name: my-argocd
    type: ARGOCD
    roleArn: arn:aws:iam::{{111122223333}}:role/ArgoCDCapabilityRole
    deletePropagationPolicy: RETAIN
    networkConfiguration:
      elasticNetworkInterfaces:
        vpcEndpointId: {{vpce-xxxxxxxx}}
    configuration:
      argocd:
        awsIdc:
          idcInstanceArn: {{arn:aws:sso:::instance/ssoins-123abc}}
          idcRegion: {{idc-region-code}}
        rbacRoleMappings:
          - role: ADMIN
            identities:
              - id: {{38414300-1041-708a-01af-5422d6091e34}}
                type: SSO_USER
```

**Note**  
When private endpoint is enabled, the Argo CD UI and API are only accessible through the VPC endpoint. Users must be connected to the VPC (or a peered network) to access the Argo CD interface.

## Step 4: Create the Argo CD capability
<a name="_step_4_create_the_argo_cd_capability"></a>

Apply the configuration file:

```
eksctl create capability -f argocd-capability.yaml
```

The command returns immediately, but the capability takes some time to become active.

## Step 5: Verify the capability is active
<a name="_step_5_verify_the_capability_is_active"></a>

Check the capability status. Replace {{region-code}} with the AWS Region that your cluster is in and replace {{my-cluster}} with the name of your cluster.

```
eksctl get capability \
  --region {{region-code}} \
  --cluster {{my-cluster}} \
  --name my-argocd
```

The capability is ready when the status shows `ACTIVE`.

## Step 6: Verify custom resources are available
<a name="_step_6_verify_custom_resources_are_available"></a>

After the capability is active, verify that Argo CD custom resources are available in your cluster:

```
kubectl api-resources | grep argoproj.io
```

You should see `Application` and `ApplicationSet` resource types listed.

## Next steps
<a name="_next_steps"></a>
+  [Working with Argo CD](working-with-argocd.md) - Learn how to create and manage Argo CD Applications
+  [Argo CD considerations](argocd-considerations.md) - Configure SSO and multi-cluster access
+  [Working with capability resources](working-with-capabilities.md) - Manage your Argo CD capability resource