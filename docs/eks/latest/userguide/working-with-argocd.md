

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with Argo CD
<a name="working-with-argocd"></a>

With Argo CD, you define applications in Git repositories and Argo CD automatically syncs them to your Kubernetes clusters. This enables declarative, version-controlled application deployment with automated drift detection.

## Prerequisites
<a name="_prerequisites"></a>

Before working with Argo CD, you need:
+ An EKS cluster with the Argo CD capability created (see [Create an Argo CD capability](create-argocd-capability.md))
+ A Git repository containing Kubernetes manifests
+  `kubectl` configured to communicate with your cluster

## Common tasks
<a name="_common_tasks"></a>

The following topics guide you through common Argo CD tasks:

 ** [Configure repository access](argocd-configure-repositories.md) ** - Configure Argo CD to access your Git repositories using AWS Secrets Manager, AWS CodeConnections, or Kubernetes Secrets.

 ** [Register target clusters](argocd-register-clusters.md) ** - Register target clusters where Argo CD will deploy applications.

 ** [Working with Argo CD Projects](argocd-projects.md) ** - Organize applications and enforce security boundaries using Projects for multi-tenant environments.

 ** [Configure Argo CD settings](argocd-configure-settings.md) ** - Configure Argo CD behavior using the `argocd-cm` ConfigMap, including custom health checks for Custom Resources.

 ** [Create Applications](argocd-create-application.md) ** - Create Applications that deploy from Git repositories with automated or manual sync policies.

 ** [Use ApplicationSets](argocd-applicationsets.md) ** - Use ApplicationSets to deploy applications across multiple environments or clusters using templates and generators.

## Access the Argo CD UI
<a name="_access_the_argo_cd_ui"></a>

Access the Argo CD UI through the EKS console:

1. Open the Amazon EKS console

1. Select your cluster

1. In the left navigation pane, choose **Capabilities** 

1. Choose **Argo CD** 

1. Choose **Open Argo CD UI** 

The UI provides visual application topology, sync status and history, resource health and events, manual sync controls, and application management.

## Argo CD endpoint URL
<a name="argocd-endpoint-url"></a>

When you create an Argo CD capability, you receive a unique endpoint for both the Argo CD UI and API. By default, the endpoint hostname is *deterministic*: It uses values you already know, such as your capability name, cluster name, AWS account ID, and AWS Region. If you delete a capability and recreate it with the same cluster name and capability name, you get the same default endpoint. Because the hostname is predictable, you can construct it in advance. For example, you can pre-configure DNS, automation, or Git webhook integrations before the capability finishes provisioning. You can also specify a custom prefix for the hostname. For more information, see [Use a custom endpoint prefix](#argocd-endpoint-prefix). For any capability, the `serverUrl` value from `describe-capability` is the definitive endpoint.

**Note**  
Because the endpoint is reused, integrations that pointed at the previous capability — Git webhooks, tokens, and DNS records — connect to the new one automatically, with no indication that the instance changed. After you recreate a capability, re-verify those integrations and rotate any webhook secrets or tokens that were shared with the previous instance.

### Retrieve the endpoint
<a name="_retrieve_the_endpoint"></a>

To get the exact endpoint for a capability, use the `describe-capability` command and read the `serverUrl` value. Replace {{region-code}}, {{my-cluster}}, and {{my-argocd}} with your values:

```
aws eks describe-capability \
  --region {{region-code}} \
  --cluster-name {{my-cluster}} \
  --capability-name {{my-argocd}} \
  --query 'capability.configuration.argoCd.serverUrl' \
  --output text
```

**Note**  
The `serverUrl` field and the endpoint’s DNS records are available after the capability status changes to `ACTIVE`.

### Endpoint format
<a name="_endpoint_format"></a>

By default, the Argo CD endpoint uses the following format:

```
https://{{capability-name}}-{{hash}}-{{account-id}}.eks-capabilities.{{region-code}}.amazonaws.com
```

The hostname consists of the following components:
+  {{capability-name}} – The name of your Argo CD capability, normalized to lowercase with each underscore (`_`) replaced by a hyphen (`-`). If the normalized name is longer than 41 characters, it’s truncated to 41 characters.
+  {{hash}} – An 8-character hexadecimal value that makes the hostname unique. It’s the first 8 characters of the SHA-256 hash of your capability name and cluster name. The names are joined by a forward slash (` capability-name/cluster-name `). Use the exact names you specified when you created the capability. This value provides uniqueness only and isn’t a security control.
+  {{account-id}} – Your 12-digit AWS account ID.
+  `eks-capabilities.region-code.amazonaws.com` – The EKS Capabilities service domain for your AWS Region.

For example, a capability named `my-argocd` on cluster `my-cluster` in account `111122223333` in the `us-west-2` Region has an endpoint similar to the following:

```
https://my-argocd-dc855fdf-111122223333.eks-capabilities.us-west-2.amazonaws.com
```

The hostname uses the normalized capability name, but the hash uses the raw name you specified. For example, the capability `Payments_GitOps` on cluster `my-cluster` normalizes to `payments-gitops` in the hostname, and its hash comes from the raw string `Payments_GitOps/my-cluster`:

```
https://payments-gitops-4ce0b382-111122223333.eks-capabilities.us-west-2.amazonaws.com
```

**Note**  
Use the `describe-capability` output to confirm the exact endpoint for your AWS Region.

You can compute the {{hash}} component yourself. Use `sha256sum` on Linux or `shasum -a 256` on macOS. The following commands use the example capability `my-argocd` on cluster `my-cluster`. Substitute the exact names that you specified when you created the capability:

```
# Linux
printf '%s' "my-argocd/my-cluster" | sha256sum | cut -c1-8

# macOS
printf '%s' "my-argocd/my-cluster" | shasum -a 256 | cut -c1-8
```

Both commands return `dc855fdf`.

### Use a custom endpoint prefix
<a name="argocd-endpoint-prefix"></a>

Instead of using the default hostname, you can specify a prefix for your endpoint. If you specify an endpoint prefix when you create the capability, the endpoint uses the following format:

```
https://{{endpoint-prefix}}-{{account-id}}.eks-capabilities.{{region-code}}.amazonaws.com
```

A custom prefix replaces the capability name and the hash, so the hostname starts with your prefix followed by your AWS account ID. For example, the prefix `payments` in account `111122223333` in the `us-west-2` Region produces the following endpoint:

```
https://payments-111122223333.eks-capabilities.us-west-2.amazonaws.com
```

An endpoint prefix must meet the following requirements:
+ Contains 1 to 50 characters
+ Contains only lowercase letters (`a-z`), numbers (`0-9`), and hyphens (`-`)
+ Starts and ends with a letter or a number
+ Is unique within your AWS account and AWS Region
+ Isn’t a prefix that Amazon EKS reserves

Amazon EKS reserves a small set of prefixes that collide with well-known hostnames, such as `www`, `api`, and `admin`. This set can change. If you specify a reserved prefix, the request fails with an `InvalidParameterException` that names the prefix. If another capability in your AWS account and AWS Region already uses the prefix, the request fails with a `ResourceInUseException`.

To specify a prefix, include `endpointPrefix` in the `argoCd` object that you pass to the `--configuration` parameter of `aws eks create-capability`. The following example uses the prefix `payments`:

```
{
  "argoCd": {
    "endpointPrefix": "payments",
    "awsIdc": {
      "idcInstanceArn": "{{arn:aws:sso:::instance/ssoins-1234567890abcdef}}",
      "idcRegion": "{{idc-region-code}}"
    },
    "rbacRoleMappings": [{
      "role": "ADMIN",
      "identities": [{
        "id": "{{user-id}}",
        "type": "SSO_USER"
      }]
    }]
  }
}
```

For the complete procedure, see [Create an Argo CD capability using the AWS CLI](argocd-create-cli.md). You can also specify the prefix when you create the capability in the AWS Management Console. For more information, see [Create an Argo CD capability using the Console](argocd-create-console.md). In AWS CloudFormation, use the `EndpointPrefix` property of `Configuration.ArgoCd` in the `AWS::EKS::Capability` resource.

```
Resources:
  ArgoCdCapability:
    Type: AWS::EKS::Capability
    Properties:
      ClusterName: {{my-cluster}}
      CapabilityName: {{my-argocd}}
      Type: ARGOCD
      RoleArn: {{arn:aws:iam::111122223333:role/ArgoCDCapabilityRole}}
      DeletePropagationPolicy: RETAIN
      Configuration:
        ArgoCd:
          EndpointPrefix: payments
          AwsIdc:
            IdcInstanceArn: {{arn:aws:sso:::instance/ssoins-1234567890abcdef}}
            IdcRegion: {{idc-region-code}}
```

 `EndpointPrefix` is a create-only property. Adding, changing, or removing it in a stack update replaces the capability: CloudFormation deletes the existing capability before it creates the new one, so Argo CD is unavailable until the new capability is active.

If you don’t specify a prefix, the endpoint uses the default format. To confirm the prefix for a capability, add `--query 'capability.configuration.argoCd.endpointPrefix'` to the `describe-capability` command. The output includes this field only for capabilities that you created with a prefix.

**Important**  
You can’t change the endpoint prefix after you create the capability. To use a different prefix, delete the capability and create a new one. This interrupts Argo CD deployments until the new capability is active. Before you delete the capability, review the deletion guidance in [Delete a capability](working-with-capabilities.md#capabilities-delete).

A prefix is scoped to your AWS account and AWS Region, not to a single cluster. The hash in the default hostname depends on your cluster name, but a prefix doesn’t. This means you can keep the same Argo CD endpoint when you move to a different cluster. For example, you can replace a hub cluster and give the new capability the same prefix.

Only one capability at a time can use a prefix in an AWS account and AWS Region. Delete the old capability before you create the new one. After the capability finishes deleting, AWS releases its prefix. You can then reuse that prefix on any cluster in the same AWS account and AWS Region, and you get the same endpoint. Before you create the new capability, confirm that the old capability no longer appears in the `list-capabilities` output for its original cluster. The endpoint is unavailable between the two capabilities.

The new capability is a separate Argo CD instance with its own configuration. Integrations that point at the endpoint, such as Git webhooks, DNS records, and CI jobs, reach the new instance. For more information, see the note in [Argo CD endpoint URL](#argocd-endpoint-url).

### Endpoint access and security
<a name="_endpoint_access_and_security"></a>

The endpoint hostname is not a secret, and knowing it doesn’t grant access to your Argo CD instance. The default hostname exposes the same non-secret information that already appears in the capability Amazon Resource Name (ARN). The `create-capability`, `describe-capability`, and `list-capabilities` operations return this ARN. If you specify a custom endpoint prefix, the hostname also exposes the prefix that you chose. Don’t include sensitive information in an endpoint prefix. AWS Identity Center authentication and Argo CD role-based access control (RBAC) control access to the Argo CD UI and API.

If you configure private endpoint access, the hostname resolves only to private IP addresses associated with your VPC endpoint. You can access the endpoint only from your VPC or connected networks. For more information, see [Configure private endpoint access for Argo CD](argocd-private-access.md).

## Upstream documentation
<a name="_upstream_documentation"></a>

For detailed information about Argo CD features:
+  [Argo CD Documentation](https://argo-cd.readthedocs.io/) - Complete user guide
+  [Application Spec](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/) - Full Application API reference
+  [ApplicationSet Guide](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/) - ApplicationSet patterns and examples
+  [Argo CD GitHub](https://github.com/argoproj/argo-cd) - Source code and examples