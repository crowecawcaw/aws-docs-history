

# Install the CloudWatch agent on Azure
<a name="install-CloudWatch-Agent-on-Azure"></a>

You can run the Amazon CloudWatch agent on Azure to collect metrics, logs, and traces. The agent sends this telemetry to Amazon CloudWatch in your AWS account. This page covers two environments:
+ Azure Virtual Machines – You install the agent package directly on the machine.
+ Azure Kubernetes Service (AKS) – You install the agent through the Amazon CloudWatch Observability Helm chart.

For each environment, you can either use the onboarding scripts or follow the manual steps.

**Finding your Azure resource ID**  
The onboarding scripts identify your virtual machine or cluster by its full Azure resource ID (`CWAGENT_AZURE_RESOURCE_ID`). You can find the resource ID on the resource's Properties page in the Azure portal, or retrieve it by running `az vm show` (or `az aks show`) with `--query id --output tsv`.

## How the agent authenticates from Azure
<a name="install-CloudWatch-Agent-on-Azure-auth"></a>

We recommend that you federate an Azure identity to an AWS IAM role so that the agent uses temporary credentials. This approach avoids storing long-lived AWS access keys on the virtual machine or cluster, which reduces your security risk. The exact mechanism depends on the environment:
+ On a virtual machine, the Azure managed identity issues OpenID Connect (OIDC) tokens. The agent obtains a token from the Azure Instance Metadata Service and calls `AssumeRoleWithWebIdentity` to obtain temporary AWS credentials.
+ On AKS, the cluster's workload identity issues the OIDC token through a projected service account token, and the agent assumes the role in the same way.

In both cases, your AWS account needs the following:
+ An IAM OIDC identity provider for the Azure issuer
+ An IAM role that trusts the issuer and has the CloudWatchAgentServerPolicy managed policy attached

## Azure Virtual Machines
<a name="install-CloudWatch-Agent-on-Azure-vm"></a>

On an Azure virtual machine, you install the agent package in the same way as on an on-premises server. The virtual machine authenticates to AWS with a managed identity that is federated to an AWS IAM role.

### Automated setup (recommended)
<a name="install-CloudWatch-Agent-on-Azure-vm-automated"></a>

The CloudWatch agent provides onboarding scripts that automate the setup. The scripts assign the Azure managed identity, install the agent, and create the AWS IAM role and trust policy. The scripts configure the agent with a default OpenTelemetry configuration. This configuration collects host metrics (such as CPU, memory, disk, and network) and starts an OpenTelemetry Protocol (OTLP) receiver for metrics, logs, and traces from applications on the machine. The agent enriches all of this telemetry and forwards it to the CloudWatch OTLP endpoints.

Run the Azure step first, then the AWS trust step. Provide the role ARN that the AWS trust step creates or updates (by default, `arn:aws:iam::{{account-id}}:role/CloudWatchAgentServerRole`).

**To set up the agent on an Azure virtual machine using the onboarding scripts**

1. On a machine with the Azure CLI signed in (for example, Azure Cloud Shell), run the Azure step with the role ARN and the AWS Region. The script assigns the virtual machine's managed identity, installs and starts the agent, and prints the Azure tenant ID.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/azure/setup.sh | \
     CWAGENT_PLATFORM=azure_vm \
     CWAGENT_AZURE_RESOURCE_ID={{vm-resource-id}} \
     CWAGENT_AWS_ROLE_ARN={{role-arn}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

1. On a machine with AWS credentials that have IAM write access to the target account (for example, AWS CloudShell), run the AWS trust step with the tenant ID from the previous step. The script creates the role, attaches CloudWatchAgentServerPolicy, and adds the Azure web-identity trust.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/aws/setup.sh | \
     CWAGENT_PLATFORM=azure_vm \
     CWAGENT_AZURE_TENANT_ID={{tenant-id}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

### Manual setup
<a name="install-CloudWatch-Agent-on-Azure-vm-manual"></a>

**To assign a managed identity to the virtual machine**
**Active Azure CLI subscription**  
The following `az` commands act on the subscription that is active in the Azure CLI. Confirm it with `az account show`, or switch with `az account set --subscription {{subscription-id}}`, before you run them.

1. Assign a system-assigned managed identity to the virtual machine.

   ```
   az vm identity assign --resource-group {{resource-group}} --name {{vm-name}}
   ```

1. Retrieve the Azure tenant ID to use in the next procedure.

   ```
   az account show --query tenantId --output tsv
   ```

**To create the IAM role in your AWS account**

1. Register the Microsoft Entra ID issuer as an IAM OIDC identity provider. The audience (`--client-id-list`) is `https://management.azure.com/`. You don't need to supply a thumbprint. IAM retrieves the top intermediate certificate authority (CA) thumbprint of the issuer's server certificate.

   ```
   aws iam create-open-id-connect-provider \
     --url https://sts.windows.net/{{tenant-id}}/ \
     --client-id-list https://management.azure.com/
   ```

1. Create a trust policy that allows the Azure identity to assume the role. Save it to a file named `trust-policy.json`. Replace {{account-id}} with your AWS account ID and {{tenant-id}} with the Azure tenant ID.
**Reusing an existing IAM role**  
If you reuse an existing role, merge this policy with the role's existing trust policy.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "Federated": "arn:aws:iam::{{account-id}}:oidc-provider/sts.windows.net/{{tenant-id}}/" },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": { "StringEquals": { "sts.windows.net/{{tenant-id}}/:aud": "https://management.azure.com/" } }
       }
     ]
   }
   ```

1. Create the role and attach the CloudWatchAgentServerPolicy managed policy. Note the role ARN that the first command returns.

   ```
   aws iam create-role --role-name {{role-name}} --assume-role-policy-document file://trust-policy.json
   aws iam attach-role-policy --role-name {{role-name}} --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

**To install and start the agent**

1. Download and install the agent on the virtual machine, in the same way as on an on-premises server. See [Install the CloudWatch agent on on-premises servers](install-CloudWatch-Agent-on-premise.md).

1. Set the AWS Region and the ARN of the role to assume, then start the agent with the default OpenTelemetry configuration (`default:otel`). The default OpenTelemetry configuration reads the role ARN from the `CWAGENT_ROLE_ARN` environment variable.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a set-env -e AWS_REGION={{region}}
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a set-env -e CWAGENT_ROLE_ARN={{role-arn}}
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m auto -c default:otel -s
   ```

## Azure Kubernetes Service (AKS)
<a name="install-CloudWatch-Agent-on-Azure-aks"></a>

On AKS, you install the agent through the Amazon CloudWatch Observability Helm chart. The cluster authenticates to AWS with workload identity that is federated to an AWS IAM role.

### Automated setup (recommended)
<a name="install-CloudWatch-Agent-on-Azure-aks-automated"></a>

The onboarding scripts automate the setup. The scripts configure the cluster's workload identity, install the chart, and create the AWS IAM role and trust policy. The chart installs the agent with a default OpenTelemetry configuration. This configuration enables OTel Container Insights and starts an OTLP receiver for metrics, logs, and traces from applications in the cluster. The agent enriches all of this telemetry and forwards it to the CloudWatch OTLP endpoints.

Run the Azure step first, then the AWS trust step. The AWS trust step needs the cluster's OIDC issuer URL, which is available only after the Azure step enables the issuer. Provide the role ARN that the AWS trust step creates or updates (by default, `arn:aws:iam::{{account-id}}:role/CloudWatchAgentServerRole`).

**To set up the agent on AKS using the onboarding scripts**

1. On a machine with the Azure CLI signed in (for example, Azure Cloud Shell), run the Azure step with the role ARN and the AWS Region. The script enables the OIDC issuer and workload identity on the cluster, installs the agent, and prints the cluster's OIDC issuer URL.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/azure/setup.sh | \
     CWAGENT_PLATFORM=azure_aks \
     CWAGENT_AZURE_RESOURCE_ID={{cluster-resource-id}} \
     CWAGENT_AWS_ROLE_ARN={{role-arn}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

1. On a machine with AWS credentials that have IAM write access to the target account (for example, AWS CloudShell), run the AWS trust step with the OIDC issuer URL from the previous step. The script creates the role, attaches CloudWatchAgentServerPolicy, and federates the cluster issuer.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/aws/setup.sh | \
     CWAGENT_PLATFORM=azure_aks \
     CWAGENT_AZURE_OIDC_ISSUER={{issuer-url}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

### Manual setup
<a name="install-CloudWatch-Agent-on-Azure-aks-manual"></a>

**To enable workload identity on the cluster**
**Active Azure CLI subscription**  
The following `az` commands act on the subscription that is active in the Azure CLI. Confirm it with `az account show`, or switch with `az account set --subscription {{subscription-id}}`, before you run them.

1. Enable the OIDC issuer and workload identity on the AKS cluster.

   ```
   az aks update \
     --resource-group {{resource-group}} \
     --name {{cluster-name}} \
     --enable-oidc-issuer \
     --enable-workload-identity
   ```

1. Retrieve the cluster's OIDC issuer URL to use in the next procedure.

   ```
   az aks show \
     --resource-group {{resource-group}} \
     --name {{cluster-name}} \
     --query oidcIssuerProfile.issuerUrl --output tsv
   ```

**To create the IAM role in your AWS account**

1. Register the cluster's OIDC issuer as an IAM OIDC identity provider. The audience (`--client-id-list`) is `sts.amazonaws.com`.

   ```
   aws iam create-open-id-connect-provider --url {{issuer-url}} --client-id-list sts.amazonaws.com
   ```

1. Create a trust policy that allows the agent's service account to assume the role. Save it to a file named `trust-policy.json`. Replace {{account-id}} with your AWS account ID and {{issuer-host}} with the issuer URL without the `https://` prefix.
**Reusing an existing IAM role**  
If you reuse an existing role, merge this policy with the role's existing trust policy.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "Federated": "arn:aws:iam::{{account-id}}:oidc-provider/{{issuer-host}}" },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": { "StringEquals": { "{{issuer-host}}:sub": "system:serviceaccount:amazon-cloudwatch:cloudwatch-agent", "{{issuer-host}}:aud": "sts.amazonaws.com" } }
       }
     ]
   }
   ```

1. Create the role and attach the CloudWatchAgentServerPolicy managed policy. Note the role ARN that the first command returns.

   ```
   aws iam create-role --role-name {{role-name}} --assume-role-policy-document file://trust-policy.json
   aws iam attach-role-policy --role-name {{role-name}} --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

**To install the agent**

1. Add the Amazon CloudWatch Observability Helm chart repository and install the chart. Set `k8sMode`, `roleArn`, `region`, and `clusterName`. Enable OTel Container Insights and assign the default OpenTelemetry configuration to the node agent.

   ```
   helm repo add aws-observability https://aws-observability.github.io/helm-charts
   helm repo update
   
   helm upgrade --install amazon-cloudwatch-observability aws-observability/amazon-cloudwatch-observability \
     --set k8sMode=AKS \
     --set roleArn={{role-arn}} \
     --set region={{region}} \
     --set clusterName={{cluster-name}} \
     --set containerInsights.enabled=false \
     --set containerLogs.enabled=false \
     --set otelContainerInsights.enabled=true \
     --set otelContainerInsights.logs.enabled=true \
     --set-string 'agents[0].name=cloudwatch-agent' \
     --set-string 'agents[0].config=default:otel' \
     --set-string 'agents[1].name=cloudwatch-agent-cluster-scraper' \
     --set-string 'agents[1].mode=deployment' \
     --set-string 'agents[1].config=default' \
     --namespace amazon-cloudwatch --create-namespace
   ```

1. List every `agents[]` entry as shown. The Helm `--set` flag replaces a whole list element, so if you omit the cluster-scraper entry, you remove it.