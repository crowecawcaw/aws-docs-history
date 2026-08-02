# Direct SSH

###### Security notice

Direct SSH opens an inbound TCP port on your cluster pods.
We recommend [Remote access using SSH over SSM](vscode-access.md "vscode-access.md") because
it requires no open inbound ports. Only enable Direct SSH if remote access
through SSM cannot meet your needs (for example, no internet access, or
standard SSH tooling required).

Before enabling, review the following:

Cluster-wide impact

`directSSH.enabled: true` opens the configured port on all
workspace pods cluster-wide, not just selected workspaces or users.

Security group scope

Restrict the inbound rule to the narrowest possible source Classless
Inter-Domain Routing (CIDR) block. Never use `0.0.0.0/0`.
Audit regularly using the AWS Config [restricted-ssh
managed rule](../../../config/latest/developerguide/restricted-ssh.md "../../../config/latest/developerguide/restricted-ssh.md").

SSH key lifecycle

You manage the SSH key lifecycle. SSH keys are
long-lived credentials. Without a rotation policy, a compromised key
grants persistent access. Establish an SSH key rotation policy, and
rotate keys periodically, before rolling out to your team.

VPC network isolation

You manage VPC network isolation. When you enable Direct
SSH, sshd starts on the pod, and your VPC security groups and routing
control who can reach it. Make sure that only trusted network sources
(VPN subnet, Direct Connect CIDR, or corporate network range) can reach
the configured port. Direct SSH exposes the SSH port on the pod's
private IP address inside your VPC. A client can reach it only if it has
network connectivity to that VPC, through the same VPC, VPC peering, a
VPN, or Direct Connect.

## Prerequisites

Direct SSH requires ExternalDNS, an Amazon Route 53 Private Hosted Zone, VPC
connectivity from client machines, and (optionally) the AWS Load Balancer
Controller. For the full list of prerequisites, see
[Prerequisites for Direct SSH](permission-setup.md#permission-direct-ssh "permission-setup.md#permission-direct-ssh").

If web browser access is already enabled on your cluster, all prerequisites are
in place. Before you proceed, verify your ExternalDNS is configured
with `--policy=sync`. For details, see
[ExternalDNS configuration](#direct-ssh-appendix-externaldns "#direct-ssh-appendix-externaldns").

If web browser access is not yet configured, see
[(Optional) Setting up prerequisites](#direct-ssh-appendix "#direct-ssh-appendix"). For more information about
enabling web browser access, see
[EKS Addon Installation - Jupyter K8s with WebUI](operator-install.md#webui-install "operator-install.md#webui-install").

## Configure Direct SSH for your cluster

###### Cluster-wide scope

`directSSH.enabled: true` starts sshd on the configured
port in all workspace pods cluster-wide. SSH provides the same access as
JupyterLab terminal: same user (`sagemaker-user`), same
filesystem.

### Step 1: Add security group rule for SSH

Web browser access uses HTTPS (443) through an Application Load Balancer
(ALB). Because Direct SSH connects directly to pod IPs on the configured
port, you need to add a security group inbound rule.

###### VPC configuration is your responsibility

You must configure your VPC correctly, including
security groups, routing, and network access controls. Direct SSH
starts sshd on the pod. Your VPC determines who can reach it.
Restrict access to only the CIDRs that can SSH into workspaces (for
example, your corporate network range, VPN tunnel subnet, or Direct
Connect CIDR). Do not use `0.0.0.0/0`.

###### Verify the correct security group before modifying

HyperPod instance groups can override VPC config at the group level
through `OverrideVpcConfig`, including security groups. The
correct security group to modify depends on whether your workspace
instance group has an override. Adding the rule to the wrong security
group results in a silent `Connection timed out`
error.

Check whether your workspace instance group has an SG override:

```
aws sagemaker describe-cluster \
  --cluster-name <HYPERPOD_CLUSTER_NAME> \
  --region <AWS_REGION> \
  --query 'InstanceGroups[*].{Name:InstanceGroupName, OverrideSGs:OverrideVpcConfig.SecurityGroupIds}'
```

#### Option A: The instance group has a security group override

If `OverrideSGs` is non-null, add the rule to that Security
Group:

```
SG_ID=<SG_ID_FROM_OVERRIDE_VPC_CONFIG>
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp \
  --port <SSH_PORT> \
  --cidr <SOURCE_CIDR> \
  --region <AWS_REGION>
```

#### Option B: The instance group has no security group override

If `OverrideSGs` is null, use the cluster-level Security
Group from the SageMaker HyperPod cluster VPC configuration:

```
SG_ID=$(aws sagemaker describe-cluster --cluster-name <HYPERPOD_CLUSTER_NAME> --region <AWS_REGION> \
  --query 'VpcConfig.SecurityGroupIds[0]' --output text)
aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp \
  --port <SSH_PORT> \
  --cidr <SOURCE_CIDR> \
  --region <AWS_REGION>
```

The following table shows where to find each placeholder value.

| Placeholder               | Where to get it                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<HYPERPOD_CLUSTER_NAME>` | In the SageMaker AWS Management Console, choose **HyperPod Clusters**.<br>Or run `aws sagemaker list-clusters`.                                                     |
| `<SSH_PORT>`              | The port that you configured in<br>`directSSH.port` (the default is 22). It must<br>match the security group inbound rule.                                          |
| `<AWS_REGION>`            | The AWS Region where your HyperPod and EKS clusters<br>are deployed.                                                                                                |
| `<SOURCE_CIDR>`           | The CIDR of your trusted network: VPN tunnel<br>subnet, Direct Connect CIDR, or corporate network range<br>(for example, 10.192.16.0/24). Must not be<br>0.0.0.0/0. |

### Step 2: Enable Direct SSH

Add `directSSH` to your addon configuration alongside
`clusterWebUI`:

```
jupyter-k8s-aws-hyperpod:
  clusterWebUI:
    enabled: true
    domain: "<DOMAIN_NAME>"
    awsCertificateArn: "<ACM_CERTIFICATE_ARN>"
    traefik:
      shouldInstall: true
  directSSH:
    enabled: true
    port: <SSH_PORT>          # default: 22
    domain: "<ROUTE53_HOSTED_ZONE_DOMAIN>"
```

The following table shows where to find each placeholder value.

| Placeholder                    | Where to get it                                                                                                                                                                                                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<DOMAIN_NAME>`                | The domain that you configured when you enabled<br>web browser access (for example,<br>spaces.example.com). For more information, see<br>[EKS Addon Installation<br>• Jupyter K8s with WebUI](operator-install.md#webui-install "operator-install.md#webui-install"). |
| `<ACM_CERTIFICATE_ARN>`        | AWS Certificate Manager (ACM) AWS Management Console, choose **Certificates**, then select<br>your wildcard certificate ARN                                                                                                                                           |
| `<ROUTE53_HOSTED_ZONE_DOMAIN>` | Route 53 AWS Management Console, choose **Hosted Zones**, then<br>select the Private Hosted Zone name used for<br>ExternalDNS (for example, workspaces.internal)                                                                                                      |
| `<SSH_PORT>`                   | Port sshd listens on inside workspace pods.<br>Default 22. Use a non-privileged port (for example,<br>2222) if your security group or corporate policy<br>restricts port 22. The SG inbound rule must match this<br>value.                                            |

###### directSSH and remoteAccess are mutually exclusive

`directSSH` and `remoteAccess` are mutually
exclusive. Enabling both causes `helm upgrade` to fail
with: "directSSH and remoteAccess are mutually exclusive. Enable only
one." Disable `remoteAccess` before enabling
`directSSH`.

Update the addon:

```
aws eks update-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --configuration-values file://addon-config.yaml \
  --resolve-conflicts OVERWRITE \
  --region <AWS_REGION>
```

To disable Direct SSH, see
[Revoking Direct SSH access](#direct-ssh-revoke "#direct-ssh-revoke").

### Step 3: Verify Direct SSH is active

```
# Check addon status
aws eks describe-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --region <AWS_REGION>

# Check headless services created for workspaces
kubectl get svc -l app.kubernetes.io/component=direct-ssh

# Verify DNS record resolves (from within VPC)
dig <workspace-name>.<namespace>.<ROUTE53_HOSTED_ZONE_DOMAIN>
```

## Connect to your workspace using Direct SSH

Use the following procedures to connect to your workspace using Direct SSH,
manage your SSH keys, and troubleshoot connection problems.

### How SSH authentication works

Direct SSH uses standard public key authentication. Each user generates
their own SSH key pair and adds the public key to their workspace.
Private keys never leave the user's machine.

The following are key facts about SSH access:

- SSH gives the same access as JupyterLab terminal: same user
  (`sagemaker-user`), same filesystem, same
  tools.
- Keys are per-workspace. A key in one workspace does not grant
  access to other workspaces.
- The SageMaker AI Spaces startup script automatically creates the
  `.ssh/` directory with the correct permissions.
- Keys persist across workspace restarts (stored on PVC) and are
  deleted when the workspace is deleted.

###### Current limitation

The SSH username is always `sagemaker-user` regardless
of who is connecting. You cannot use a personal username. All
sessions run as the same workspace user. Per-user identity in shell
prompts and audit logs is not available in the current release.

### Step 1: Generate an SSH key on your client machine

Run this command once to create your key pair:

```
ssh-keygen -t ed25519 -f ~/.ssh/my-workspace-key
```

This creates:

- `~/.ssh/my-workspace-key` — private key (keep
  secret, never share)
- `~/.ssh/my-workspace-key.pub` — public key (add to
  your workspace)

### Step 2: Add your public key to your workspace

Use **either** of the following methods to add
your public key. You do not need to do both.

#### Add your key through web browser access

1. Open your workspace in the browser (see
   [Web browser access](browser-access.md "browser-access.md")).
2. Open a terminal. In JupyterLab, choose
   **File**, **New**,
   **Terminal**. In Code Editor, choose
   **Terminal**, **New Terminal**.
3. Copy your public key from your local machine:
   `cat ~/.ssh/my-workspace-key.pub`
4. Paste into the workspace terminal:

```
echo "ssh-ed25519 AAAA...your-key... user@machine" >> ~/.ssh/authorized_keys
```

#### Add your key through kubectl

```
POD=$(kubectl get pods -n <namespace> -l workspace.jupyter.org/workspace-name=<space-name> \
  -o jsonpath='{.items[0].metadata.name}')
cat ~/.ssh/my-workspace-key.pub | kubectl exec -n <namespace> -i $POD -c workspace -- \
  bash -c "cat >> /home/sagemaker-user/.ssh/authorized_keys"
```

### Step 3: Connect to your workspace using SSH

```
ssh -p <SSH_PORT> -i ~/.ssh/my-workspace-key sagemaker-user@<space-name>.<namespace>.<domain>
```

###### SSH port

Use the SSH port that your administrator configured for Direct SSH. If
your administrator kept the default port (22), you can omit the
`-p` option. If they configured a non-default port (for
example, 2222), you must include `-p <SSH_PORT>` or the
connection fails with `Connection refused`. Contact your
administrator if you are unsure which port to use.

Example:

```
ssh -p 2222 -i ~/.ssh/my-workspace-key sagemaker-user@my-space.default.spaces.example.com
```

### Step 4: Configure SSH for easy access

This optional step simplifies future connections. Add the following to
`~/.ssh/config`:

```
Host my-space
    HostName <space-name>.<namespace>.<domain>
    Port <SSH_PORT>
    User sagemaker-user
    IdentityFile ~/.ssh/my-workspace-key
    ServerAliveInterval 15
    ServerAliveCountMax 3
```

Set `Port` to the port your administrator configured. You can
omit this line if Direct SSH uses the default port (22). Then connect with:
`ssh my-space`

### Step 5: Connect a remote IDE

After Direct SSH works from your terminal (Step 3), any Remote-SSH
capable IDE connects using the same `~/.ssh/config` entry.
You do not need additional AWS configuration for this connection.

#### Install the Remote-SSH extension

| IDE     | Extension                                                                  |
| ------- | -------------------------------------------------------------------------- |
| VS Code | **Extensions**, search "Remote<br>• SSH", choose Install<br>(by Microsoft) |
| Kiro    | **Extensions**, search "Remote<br>• SSH", choose<br>Install                |
| Cursor  | **Extensions**, search "Remote<br>• SSH", choose<br>Install                |

#### Connect from the IDE

1. Open the **Command Palette**, then choose "Remote-SSH: Connect to
   Host..."
2. Select your workspace from the list (uses
   `~/.ssh/config` from Step 4).
3. The IDE installs its server component on the workspace
   (one-time, approximately 30 seconds).
4. A remote window opens with full editor features, including
   IntelliSense, terminal, and file explorer.

###### Open your workspace files in VS Code

In VS Code, after connecting, choose **File**, **Open Folder**,
`/home/sagemaker-user` to open your workspace files
directly.

### Key management and revocation

You manage your SSH keys. SSH keys are long-lived
credentials with no automatic expiry. A key in
`authorized_keys` grants access to your workspace until you
explicitly remove it.

#### To rotate your key

We recommend rotating your keys periodically.

1. Generate a new key pair on your client machine:
   `ssh-keygen -t ed25519 -f
 ~/.ssh/my-workspace-key-new`
2. Add the new public key to your workspace (Step 2). Both
   old and new keys work simultaneously.
3. Verify the new key works:
   `ssh -p <SSH_PORT> -i ~/.ssh/my-workspace-key-new
 sagemaker-user@<hostname>`
4. Remove the old key from `authorized_keys` in
   your workspace terminal:

```
# List current keys with line numbers
cat -n ~/.ssh/authorized_keys
# Remove a specific line (for example, line 1)
sed -i '1d' ~/.ssh/authorized_keys
```

#### If your private key is compromised

Act immediately. A compromised key grants full workspace access
until you remove it from `authorized_keys`.

1. Open your workspace through web browser access (JupyterLab or
   Code Editor). For instructions, see
   [Web browser access](browser-access.md "browser-access.md").
2. Remove the compromised key from
   `authorized_keys`:

```
# View all authorized keys
cat ~/.ssh/authorized_keys
# Option A: Edit directly
nano ~/.ssh/authorized_keys
# Option B: Remove all keys and re-add only trusted ones
> ~/.ssh/authorized_keys
echo "ssh-ed25519 AAAA...new-trusted-key..." >> ~/.ssh/authorized_keys
```

3. Verify the compromised key no longer works by attempting
   to connect with it. You should receive
   `Permission denied (publickey)`.
4. If you cannot access the workspace through web browser access,
   contact your cluster administrator to exec into the pod and clear
   `authorized_keys` directly.

#### Best practices

| Practice                                 | Why                                                                                           |
| ---------------------------------------- | --------------------------------------------------------------------------------------------- |
| Use ed25519 keys                         | Shorter, faster, more secure than RSA                                                         |
| Use a passphrase on your private key     | Protects against key theft. Even if stolen, the<br>key cannot be used without the passphrase. |
| One key per device                       | Easier to revoke a single device's access<br>without affecting others                         |
| Never share private keys                 | Each user and device must have its own key<br>pair                                            |
| Review `authorized_keys`<br>periodically | Remove keys for devices you no longer<br>use                                                  |

## Revoking Direct SSH access

To avoid leaving an open security group rule after you disable Direct SSH,
complete all three steps in order. Do not skip Step 2.

###### Notify your users before revoking access

Notify your users before you revoke access. ExternalDNS removes DNS
records within approximately 30 seconds of Step 3, which blocks new
connections.

### Step 1: Disable in Helm chart

Remove the `directSSH` section from your addon
configuration file entirely. Helm defaults
`directSSH.enabled` to `false` when the key is
absent:

```
jupyter-k8s-aws-hyperpod:
  clusterWebUI:
    enabled: true
    domain: "<DOMAIN_NAME>"
    ...
  # directSSH section removed
```

Alternatively, explicitly set `enabled: false`:

```
directSSH:
  enabled: false
```

### Step 2: Remove the security group inbound rule

```
# Find the rule ID
aws ec2 describe-security-group-rules \
  --filters Name=group-id,Values=<SG_ID> \
  --query 'SecurityGroupRules[?IpProtocol==`tcp` && FromPort==`<SSH_PORT>`].[SecurityGroupRuleId,CidrIpv4]' \
  --output table \
  --region <AWS_REGION>

# Remove the rule
aws ec2 revoke-security-group-ingress \
  --group-id <SG_ID> \
  --security-group-rule-ids <RULE_ID> \
  --region <AWS_REGION>
```

### Step 3: Apply to cluster

```
aws eks update-addon \
  --cluster-name <CLUSTER_NAME> \
  --addon-name amazon-sagemaker-spaces \
  --configuration-values file://addon-config.yaml \
  --resolve-conflicts OVERWRITE \
  --region <AWS_REGION>
```

Running this command removes the headless Services for all workspaces.
ExternalDNS then deletes the Route 53 A records within approximately 30
seconds. After ExternalDNS removes the records, new SSH connections can no
longer resolve the workspace hostname.

### What happens after revocation

| Component            | State after revocation                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| DNS records          | ExternalDNS removes them within approximately 30<br>seconds. New connections cannot resolve the workspace<br>hostname. |
| SG inbound rule      | Closed after Step 2. No network path reaches the<br>port.                                                              |
| New SSH connections  | Blocked. The hostname no longer resolves, and the SG<br>rule closes the port.                                          |
| Workspace data (PVC) | Unaffected. The PVC keeps your files, authorized\_keys,<br>and host key.                                               |

## Troubleshooting

| Symptom                                   | Cause                                                      | Fix                                                                                                                                                                                                                |
| ----------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `NXDOMAIN`                                | DNS not resolving                                          | Verify hosted zone exists, VPC associated,<br>ExternalDNS running                                                                                                                                                  |
| `Connection timed out`                    | SG blocking: rule added to wrong SG or missing<br>entirely | Check `OverrideVpcConfig` on instance<br>group (Admin Step 1). Verify TCP inbound rule covers<br>your source CIDR.                                                                                                 |
| `Connection refused`                      | sshd not running                                           | Check space is in Running state and<br>`directSSH` is enabled                                                                                                                                                      |
| `Permission denied (publickey)`           | Key not in `authorized_keys`                               | Add public key through web browser access or kubectl (End User<br>Step 2)                                                                                                                                          |
| `Host key changed` warning                | Space was recreated (new pod, new host key)                | On your client machine:<br>`ssh-keygen -R <hostname>` then<br>reconnect                                                                                                                                            |
| `Stale DNS records after space deletion`  | ExternalDNS running with<br>`--policy=upsert-only`         | Update ExternalDNS deployment to<br>`--policy=sync` and add<br>`--txt-owner-id=<cluster-name>`.<br>Manually clean up existing stale records:<br>`aws route53 list-resource-record-sets --hosted-zone-id <ZONE_ID>` |
| IDE: "Could not establish connection"     | sshd not yet ready                                         | Wait 60-90 seconds after workspace creation, then<br>retry                                                                                                                                                         |
| IDE: Hangs at "Installing VS Code Server" | Workspace has no internet access                           | Your workspace downloads the VS Code server binary from an<br>external host on first connection. Contact your administrator if<br>the workspace is air-gapped.                                                     |
| IDE: `Permission denied`                  | IdentityFile path mismatch                                 | Verify terminal SSH works first, then check<br>IdentityFile in `~/.ssh/config`                                                                                                                                     |
| IDE: Connection drops after idle          | No keepalive configured                                    | Add `ServerAliveInterval 15` and<br>`ServerAliveCountMax 3` to<br>`~/.ssh/config`                                                                                                                                  |

## (Optional) Setting up prerequisites

Use this section only if web browser access is not already enabled, or to
verify or update your ExternalDNS configuration.

### Installing from scratch

If web browser access is not yet configured, you need the following before
enabling Direct SSH:

1. **Route 53 hosted zone** — a
   domain or subdomain that you own, registered in Route 53
2. **External DNS** — deployed
   through EKS add-ons, with IAM role having Route 53
   permissions
3. **AWS Load Balancer
   Controller** — required if you use web browser
   access (ALB ingress). For HyperPod-specific installation notes,
   see [AWS Load Balancer Controller: HyperPod vpcId requirement](#direct-ssh-appendix-lbc "#direct-ssh-appendix-lbc").
4. **VPC connectivity** — VPN
   or Direct Connect from client machines to the VPC

For the additional dependencies and the web browser
access configuration steps, see
[Install SageMaker AI Spaces Add-on](operator-install.md "operator-install.md").

### AWS Load Balancer Controller: HyperPod vpcId requirement

The standard AWS Load Balancer Controller installation documentation
does not mention the `vpcId` parameter. On HyperPod clusters,
omitting `vpcId` causes the installation to fail. You must
provide it explicitly.

Get your VPC ID:

```
aws sagemaker describe-cluster \
  --cluster-name <HYPERPOD_CLUSTER_NAME> \
  --region <AWS_REGION> \
  --query 'VpcConfig.VpcId' \
  --output text
```

Install with the required HyperPod parameters:

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=<EKS_CLUSTER_NAME> \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set enableServiceMutatorWebhook=false \
  --set vpcId=<VPC_ID>
```

| Parameter                           | Why required on HyperPod                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `vpcId`                             | HyperPod VPC is not auto-discoverable by the<br>controller. Installation fails without it.             |
| `enableServiceMutatorWebhook=false` | The mutating webhook conflicts with HyperPod's<br>service configuration                                |
| `serviceAccount.create=false`       | Service account must be pre-created with the correct<br>IRSA or Pod Identity annotation before install |

Create the service account (aws-load-balancer-controller)
with the appropriate IAM role annotation before running this command.
For more information about the IAM policy and service account creation
steps, see
[Amazon EKS Load Balancer Controller IRSA setup](../../../eks/latest/userguide/lbc-helm.md "../../../eks/latest/userguide/lbc-helm.md")
in the Amazon EKS User Guide.

### ExternalDNS configuration

ExternalDNS synchronizes Kubernetes Services with DNS providers.
Configure ExternalDNS with the following settings when you use it with
Amazon Route 53 in a production environment.

###### ExternalDNS requires the sync policy

You must configure ExternalDNS with
`--policy=sync`.

By default, ExternalDNS uses
`--policy=upsert-only`. This creates and updates DNS
records but never deletes them. When you delete a workspace, the A
and TXT records in Amazon Route 53 remain as stale entries.

Use `--policy=upsert-only` only for testing, and change
it to `--policy=sync` for production. You must also set
the `--txt-owner-id` flag, which tells ExternalDNS which
records it owns and which records to delete on cleanup.

Configure your ExternalDNS deployment with the following
arguments:

```
--provider=aws
--source=service                          # watches Services (required for headless Services)
--domain-filter=<ROUTE53_HOSTED_ZONE>     # restricts ExternalDNS to your hosted zone only
--policy=sync                             # enables deletion of stale records on space deletion
--txt-owner-id=<CLUSTER_NAME>             # identifies which records this ExternalDNS instance owns
```

In the preceding arguments, replace the following values:

- `<ROUTE53_HOSTED_ZONE>` — your
  Amazon Route 53 private hosted zone domain (for example,
  `workspaces.internal`)
- `<CLUSTER_NAME>` — your EKS cluster
  name (for example, `my-hyperpod-cluster`)

To verify your current ExternalDNS policy, run the following
command:

```
kubectl get deployment -n kube-system external-dns \
  -o jsonpath='{.spec.template.spec.containers[0].args}' | tr ',' '\n' | grep -E 'policy|owner|source|domain'
```
