**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Working with Argo CD

With Argo CD, you define applications in Git repositories and Argo CD automatically syncs them to your Kubernetes clusters.
This enables declarative, version-controlled application deployment with automated drift detection.

## Prerequisites

Before working with Argo CD, you need:

- An EKS cluster with the Argo CD capability created (see [Create an Argo CD capability](create-argocd-capability.md "create-argocd-capability.md"))
- A Git repository containing Kubernetes manifests
- `kubectl` configured to communicate with your cluster

## Common tasks

The following topics guide you through common Argo CD tasks:

**[Configure repository access](argocd-configure-repositories.md "argocd-configure-repositories.md")** - Configure Argo CD to access your Git repositories using AWS Secrets Manager, AWS CodeConnections, or Kubernetes Secrets.

**[Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md")** - Register target clusters where Argo CD will deploy applications.

**[Working with Argo CD Projects](argocd-projects.md "argocd-projects.md")** - Organize applications and enforce security boundaries using Projects for multi-tenant environments.

**[Configure Argo CD settings](argocd-configure-settings.md "argocd-configure-settings.md")** - Configure Argo CD behavior using the `argocd-cm` ConfigMap, including custom health checks for Custom Resources.

**[Create Applications](argocd-create-application.md "argocd-create-application.md")** - Create Applications that deploy from Git repositories with automated or manual sync policies.

**[Use ApplicationSets](argocd-applicationsets.md "argocd-applicationsets.md")** - Use ApplicationSets to deploy applications across multiple environments or clusters using templates and generators.

## Access the Argo CD UI

Access the Argo CD UI through the EKS console:

1. Open the Amazon EKS console
2. Select your cluster
3. Choose the **Capabilities** tab
4. Choose **Argo CD**
5. Choose **Open Argo CD UI**

The UI provides visual application topology, sync status and history, resource health and events, manual sync controls, and application management.

## Argo CD endpoint URL

When you create an Argo CD capability, you receive a unique endpoint for both the Argo CD UI and API.
The endpoint hostname is _deterministic_: It uses values you already know, such as your capability name, cluster name, AWS account ID, and AWS Region.
If you delete a capability and recreate it with the same cluster name and capability name, you get the same endpoint.
Because the hostname is predictable, you can construct it in advance.
For example, you can pre-configure DNS, automation, or Git webhook integrations before the capability finishes provisioning.
For any capability, the `serverUrl` value from `describe-capability` is the definitive endpoint.

###### Note

Because the endpoint is reused, integrations that pointed at the previous capability — Git webhooks, tokens, and DNS records — connect to the new one automatically, with no indication that the instance changed.
After you recreate a capability, re-verify those integrations and rotate any webhook secrets or tokens that were shared with the previous instance.

### Retrieve the endpoint

To get the exact endpoint for a capability, use the `describe-capability` command and read the `serverUrl` value.
Replace `region-code`, `my-cluster`, and `my-argocd` with your values:

```
aws eks describe-capability \
  --region `region-code` \
  --cluster-name `my-cluster` \
  --capability-name `my-argocd` \
  --query 'capability.configuration.argoCd.serverUrl' \
  --output text
```

###### Note

The `serverUrl` field and the endpoint’s DNS records are available after the capability status changes to `ACTIVE`.

### Endpoint format

The Argo CD endpoint uses the following format:

```
https://`capability-name`-`hash`-`account-id`.eks-capabilities.`region-code`.amazonaws.com
```

The hostname consists of the following components:

- `capability-name` – The name of your Argo CD capability, normalized to lowercase with each underscore (`_`) replaced by a hyphen (`-`). If the normalized name is longer than 41 characters, it’s truncated to 41 characters.
- `hash` – An 8-character hexadecimal value that makes the hostname unique. It’s the first 8 characters of the SHA-256 hash of your capability name and cluster name. The names are joined by a forward slash (`*capability-name*/*cluster-name*`). Use the exact names you specified when you created the capability. This value provides uniqueness only and isn’t a security control.
- `account-id` – Your 12-digit AWS account ID.
- `eks-capabilities.*region-code*.amazonaws.com` – The EKS Capabilities service domain for your AWS Region.

For example, a capability named `my-argocd` on cluster `my-cluster` in account `111122223333` in the `us-west-2` Region has an endpoint similar to the following:

```
https://my-argocd-dc855fdf-111122223333.eks-capabilities.us-west-2.amazonaws.com
```

The hostname uses the normalized capability name, but the hash uses the raw name you specified. For example, the capability `Payments_GitOps` on cluster `my-cluster` normalizes to `payments-gitops` in the hostname, and its hash comes from the raw string `Payments_GitOps/my-cluster`:

```
https://payments-gitops-4ce0b382-111122223333.eks-capabilities.us-west-2.amazonaws.com
```

###### Note

Use the `describe-capability` output to confirm the exact endpoint for your AWS Region.

You can compute the `hash` component yourself. Use `sha256sum` on Linux or `shasum -a 256` on macOS.
The following commands use the example capability `my-argocd` on cluster `my-cluster`.
Substitute the exact names that you specified when you created the capability:

```
# Linux
printf '%s' "my-argocd/my-cluster" | sha256sum | cut -c1-8

# macOS
printf '%s' "my-argocd/my-cluster" | shasum -a 256 | cut -c1-8
```

Both commands return `dc855fdf`.

### Endpoint access and security

The endpoint hostname is not a secret, and knowing it doesn’t grant access to your Argo CD instance.
The hostname exposes the same non-secret information that already appears in the capability Amazon Resource Name (ARN). The `create-capability`, `describe-capability`, and `list-capabilities` operations return this ARN.
AWS Identity Center authentication and Argo CD role-based access control (RBAC) control access to the Argo CD UI and API.

If you configure private endpoint access, the hostname resolves only to private IP addresses associated with your VPC endpoint. You can access the endpoint only from your VPC or connected networks.
For more information, see [Configure private endpoint access for Argo CD](argocd-private-access.md "argocd-private-access.md").

## Upstream documentation

For detailed information about Argo CD features:

- [Argo CD Documentation](https://argo-cd.readthedocs.io/ "https://argo-cd.readthedocs.io/") - Complete user guide
- [Application Spec](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/") - Full Application API reference
- [ApplicationSet Guide](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/ "https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/") - ApplicationSet patterns and examples
- [Argo CD GitHub](https://github.com/argoproj/argo-cd "https://github.com/argoproj/argo-cd") - Source code and examples
