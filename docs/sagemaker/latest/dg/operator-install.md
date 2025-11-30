# Install SageMaker AI Spaces Add-on

## Dependencies

**Amazon EKS Pod Identity Agent add-on**

- Required for the operator to obtain AWS credentials
- **Typically pre-installed** on most EKS
  clusters
- Installation: Via EKS add-ons

**Cert-manager**

- Required for TLS certificate management
- **Pre-installed** if using HyperPod quick cluster
  create
- Installation: Via EKS add-ons

**EBS CSI Driver**

- Required for Space persistent storage (EBS volumes)
- **Automatically installed** when using SageMaker
  console to install
- Requires IAM role with `AmazonEBSCSIDriverPolicy` + HyperPod-specific permissions
- Installation: Via EKS add-ons. However, make sure follow the guide to install
  additional permissions needed for HyperPod.
- Reference: [Using the Amazon EBS CSI driver on HyperPod](sagemaker-hyperpod-eks-ebs.md "sagemaker-hyperpod-eks-ebs.md")

## Additional dependencies for WebUI Access

**AWS Load Balancer Controller**

- **Pre-installed** if using HyperPod quick
  cluster create
- Installation: Via Helm
- Manual installation guide: [Installing the AWS Load Balancer Controller](../../../eks/latest/userguide/lbc-helm.md "../../../eks/latest/userguide/lbc-helm.md")

**External DNS**

- Required when using custom domain for WebUI access
- Manages Route53 DNS records automatically
- Requires IAM role with Route53 permissions
- Installation: Via EKS add-ons

## Installation

Before you begin, ensure that you have:

- An active SageMaker HyperPod cluster with at least one worker node running
  Kubernetes version 1.30 or later
- At least one worker node with minimum instance type (XX vCPU, YY GiB
  memory)

### Installing the Amazon SageMaker Spaces add-on

You can install the SageMaker Spaces add-on using either quick install for
default settings or custom install for advanced configuration.

#### Quick install

1. Open the Amazon SageMaker console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose your cluster from the clusters list.
3. On the IDE and Notebooks tab, locate Amazon SageMaker Spaces, then choose Quick install.

Quick install automatically:

- Creates the required IAM roles for the add-on
- Enables remote access mode with required IAM roles for Systems
  Manager
- Installs the add-on and configures pod identity association

#### Custom install

1. Open the Amazon SageMaker console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose your cluster from the clusters list.
3. On the IDE and Notebooks tab, locate Amazon SageMaker Spaces, then
   choose Custom install.
4. Configure the following options:

**IAM roles needed by add-on**

    * Choose whether to create new IAM roles with recommended
     permissions or use existing ones with the required
     permissions (Refer to Admin Permission Set up section
     above)

**Remote access
configuration**

    * Enable to allow users to connect to spaces from local
     Visual Studio Code using AWS Systems Manager
    * For SSM managed instance role:




    	+ **Create new role** –
    	 The add-on creates and manages the role with
    	 required Systems Manager permissions
    	+ **Use existing role**
    	 – Select a pre-configured role with necessary
    	 Systems Manager permissions
    * Ensure the Spaces Add-on Execution Role has PassRole
     permissions for the SSM managed instance role

###### Note

Enabling remote access activates AWS Systems Manager
advanced-instances tier for additional per-instance charges. For
pricing information, see Systems Manager pricing.

**Web browser access
configuration**

    * Enable to allow users to access spaces through a web
     browser using Route 53 DNS and SSL certificates
    * **Prerequisites:** Install
     AWS Load Balancer Controller before enabling browser
     access
    * **Route 53 hosted zone:**
     Select existing zone or choose Create hosted zone
    * **Subdomain:** Enter
     subdomain prefix (alphanumeric and hyphens only, maximum 63
     characters)
    * **SSL certificate:**




    	+ **Create new
    	 certificate** – Automatically requested
    	 and validated from AWS Certificate Manager using
    	 Route 53 DNS records
    	+ **Use existing
    	 certificate** – Select an SSL certificate
    	 from AWS Certificate Manager
    * **Token signing key:** Select
     an AWS KMS asymmetric key for JWT token signing, or choose
     Create signing key

###### Note

Standard Route 53 charges apply for hosted zones and DNS
queries. For pricing information, see Route 53 pricing.

#### EKS Addon Installation - Jupyter K8s with WebUI

##### Configuration File

Create `addon-config.yaml`:

```
jupyter-k8s:
  workspacePodWatching:
    enable: true

jupyter-k8s-aws-hyperpod:
  clusterWebUI:
    enabled: true
    domain: "<DOMAIN_NAME>"
    awsCertificateArn: "<ACM_CERTIFICATE_ARN>"
    kmsEncryptionContext:
      enabled: true
    traefik:
      shouldInstall: true
    auth:
      kmsKeyId: "<KMS_KEY_ARN>"
```

**Replace the following
placeholders:**

- <DOMAIN_NAME>: Your domain name (e.g.,
  `jupyter.example.com`)
- <ACM_CERTIFICATE_ARN>: Your ACM certificate ARN (e.g. `arn:aws:acm:us-west-2:111122223333:certificate/12345678-1234-1234-1234-123456789012`,
- <KMS_KEY_ARN>: Your KMS key ARN (e.g., `arn:aws:kms:us-west-2:111122223333:key/12345678-1234-1234-1234-123456789012`

##### Installation via AWS CLI

```
aws eks create-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --configuration-values file://addon-config.yaml \
  --resolve-conflicts OVERWRITE \
  --region <AWS_REGION>
```

**To update existing addon:**

```
aws eks update-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --configuration-values file://addon-config.yaml \
  --resolve-conflicts OVERWRITE \
  --region <AWS_REGION>
```

##### Installation via AWS Management Console

1. Go to **EKS Console** → Select
   your cluster
2. Click **Add-ons** tab → **Add new**
3. Select **SageMaker Spaces**
   addon
4. Paste the YAML config above in **Optional
   configuration settings**
5. Click **Ads**

##### Verify Installation

```
# Check addon status
aws eks describe-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --region <AWS_REGION>
```

##### Customizing ALB Attributes

By default, the addon creates a public load balancer for use with the
web UI. You can customize the load balancer attributes using the EKS
addon properties.

To create an internal ALB, set the scheme to
`internal`:

```
jupyter-k8s-aws-hyperpod:
  clusterWebUI:
    enabled: true
    domain: "<DOMAIN_NAME>"
    awsCertificateArn: "<ACM_CERTIFICATE_ARN>"
    alb:
      scheme: "internal"  # Default is "internet-facing"
```

You can also use the `alb.annotations` field to customize ALB settings:

```
jupyter-k8s-aws-hyperpod:
  clusterWebUI:
    enabled: true
    domain: "<DOMAIN_NAME>"
    awsCertificateArn: "<ACM_CERTIFICATE_ARN>"
    alb:
      scheme: "internal"
      annotations:
        alb.ingress.kubernetes.io/security-groups: "<SECURITY_GROUP_ID>"
        alb.ingress.kubernetes.io/subnets: "<SUBNET_ID_1>,<SUBNET_ID_2>"
        alb.ingress.kubernetes.io/load-balancer-attributes: "idle_timeout.timeout_seconds=60"
```

**Common ALB annotations:**

- `alb.ingress.kubernetes.io/security-groups`: Specify security groups for the ALB
- `alb.ingress.kubernetes.io/subnets`: Specify subnets for the ALB
- `alb.ingress.kubernetes.io/load-balancer-attributes`: Set ALB attributes (idle timeout, access logs, etc.)

See [AWS Load Balancer Controller documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/annotations/ "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/ingress/annotations/") for all
available annotations.

### Upgrade / versioning of add-on

```
aws eks update-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --configuration-values file://addon-config.yaml \
  --resolve-conflicts OVERWRITE \
  --region <AWS_REGION>
```
