

# Choose between the ASCP and AWCP for Amazon EKS

Secrets Manager provides two ways to deliver secrets to workloads on Amazon Elastic Kubernetes Service. Both use your workload's AWS credentials, retrieve secrets on your application's behalf, and don't require an AWS SDK in your code. They differ in how your application receives the secret.
+ The **AWS Secrets and Configuration Provider (ASCP)** mounts secrets as files in your Pods. You declare what to mount in a `SecretProviderClass`.
+ The **AWS Workload Credentials Provider (AWCP)** runs as a sidecar container on Amazon EKS and serves secrets to your application over a local HTTP endpoint from an in-memory cache. The same HTTP interface is available on Amazon ECS, Lambda (as an extension), and Amazon EC2. For instructions on running it as a sidecar, see [Install the AWS Workload Credentials Provider](workload-credentials-provider.md#workload-credentials-provider-install).

## Which one to use
<a name="eks-choose-ascp-or-agent-which"></a>

Use the ASCP when your workload:
+ Reads secrets from files or environment variables, and you don't want to change application code.
+ Runs on clusters where a platform team installs and manages secret delivery once per cluster, with the Amazon EKS add-on, Helm, or YAML.
+ Also needs parameters from AWS Systems Manager Parameter Store. AWCP retrieves only Secrets Manager secrets.
+ Needs to assume an IAM role to retrieve secrets, for example a role in the account that owns them. The ASCP can assume one role for each `SecretProviderClass`.

Use AWCP when your workload:
+ Needs to fetch the latest secret value on demand, for example after an authentication failure, without restarting the Pod.
+ Needs to assume a different IAM role for each request or each secret.
+ Must not write secret values to the Pod file system or to Kubernetes Secrets.
+ Runs on AWS Fargate, for Amazon EKS or Amazon ECS.
+ Also runs outside Kubernetes, and you want one way to consume secrets everywhere.

The ASCP suits applications that already read configuration from files. AWCP suits applications that you are writing or updating to fetch secrets at runtime.

## Comparison
<a name="eks-choose-ascp-or-agent-compare"></a>

The following table compares how the ASCP and AWCP deliver secrets to your application.


| Feature | ASCP | AWCP | 
| --- | --- | --- | 
| How the application gets secrets | Mounted files. The Secrets Store CSI Driver can also sync them to Kubernetes Secrets for environment variables. | HTTP GET request to localhost | 
| Application code change | None | The application or its entrypoint calls the local endpoint | 
| Where values are stored | Pod volume, and etcd if you sync to Kubernetes Secrets | AWCP memory only | 
| Rotated values | Secrets Store CSI Driver rotation (alpha, off by default) fetches secrets again on a poll interval. The application reloads files. Environment variables need a Pod restart. | Caches each secret for a set time to live (TTL), 300 seconds by default. After the TTL expires, AWCP fetches the latest value on the next request. Use refreshNow=true for an immediate refresh. | 
| Cross-account secrets | Supported with the Pod's role, through the secret's resource policy and the AWS KMS key policy, or with assumeRoleArn in the SecretProviderClass to assume a role in the account that owns the secret | Supported through resource policies, or with roleArn to assume a different role per request or per pre-fetched secret | 
| If retrieval fails at startup | The Pod doesn't start | The application handles the error | 

The following table compares where each option runs and who manages it.


| Feature | ASCP | AWCP | 
| --- | --- | --- | 
| AWS Fargate for Amazon EKS | Not supported | Supported with IAM Roles for Service Accounts (IRSA). Amazon EKS Pod Identity isn't available on Fargate. | 
| Amazon ECS, including AWS Fargate | Not supported | Supported | 
| Install and upgrade | Amazon EKS add-on (recommended), Helm, or YAML. One installation per cluster. | Sidecar container in each Pod spec | 
| Typical owner | A platform team installs it. Application teams create a SecretProviderClass. | Each application team | 

## Operating model: Amazon EKS add-on or sidecar
<a name="eks-choose-ascp-or-agent-operating-model"></a>

The `aws-secrets-store-csi-driver-provider` Amazon EKS add-on installs the ASCP and the Secrets Store CSI Driver that it depends on. You install, configure, and upgrade it with the Amazon EKS console, the AWS CLI, **eksctl**, or infrastructure as code. AWS validates each add-on version to work with Amazon EKS and keeps it patched. The add-on doesn't need its own IAM role. You give each Pod access to its secrets through Amazon EKS Pod Identity or IAM Roles for Service Accounts (IRSA).

AWCP runs as a sidecar, so each application team adds it to its Pod spec and manages its image version and configuration. Choose the ASCP when central, cluster-level management matters most. Choose AWCP when per-application control over refresh, the role used for each request, or portability beyond Kubernetes matters more.

## Related resources
<a name="eks-choose-ascp-or-agent-resources"></a>
+ For instructions on installing the ASCP, see [Install ASCP for Amazon EKS](ascp-eks-installation.md).
+ For information about the ASCP add-on, see [AWS add-ons available for Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html) in the *Amazon EKS User Guide*.
+ For information about AWCP, see [Using the AWS Workload Credentials Provider](workload-credentials-provider.md).
+ For AWCP source code and releases, see the [AWS Workload Credentials Provider repository](https://github.com/aws/aws-workload-credentials-provider) on the GitHub website.