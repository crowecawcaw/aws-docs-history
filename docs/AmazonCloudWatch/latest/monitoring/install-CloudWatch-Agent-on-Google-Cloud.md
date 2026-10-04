

# Install the CloudWatch agent on Google Cloud
<a name="install-CloudWatch-Agent-on-Google-Cloud"></a>

You can run the Amazon CloudWatch agent on Google Cloud to collect metrics, logs, and traces. The agent sends this telemetry to Amazon CloudWatch in your AWS account. This page covers two environments:
+ Google Compute Engine (GCE) – You install the agent package directly on the instance.
+ Google Kubernetes Engine (GKE) – You install the agent through the Amazon CloudWatch Observability Helm chart.

For each environment, you can either use the onboarding scripts or follow the manual steps.

**Identifying your instance or cluster**  
The onboarding scripts identify your instance or cluster by project, location, and name. The project comes from `CWAGENT_GCP_PROJECT`, or from the Google Cloud CLI default when you omit it. The location (`CWAGENT_GCP_LOCATION`) is the zone for an instance, and the zone or region for a cluster.

## How the agent authenticates from Google Cloud
<a name="install-CloudWatch-Agent-on-Google-Cloud-auth"></a>

We recommend that you federate a Google Cloud identity to an AWS IAM role so that the agent uses temporary credentials. This approach avoids storing long-lived AWS access keys on the instance or cluster, which reduces your security risk. The exact mechanism depends on the environment:
+ On an instance, the attached service account issues OpenID Connect (OIDC) tokens. The agent obtains a token from the GCE metadata server and calls `AssumeRoleWithWebIdentity` to obtain temporary AWS credentials.
+ On GKE, the cluster issues the OIDC token through a projected service account token, and the agent assumes the role in the same way.

In both cases, your AWS account needs an IAM role that trusts the Google Cloud identity and has the CloudWatchAgentServerPolicy managed policy attached.

**Google is a built-in identity provider**  
For instances, you don't create an IAM OIDC identity provider. IAM has Google built in, so the trust policy names `accounts.google.com` directly. For GKE, you do register the cluster's OIDC issuer as an IAM OIDC identity provider.

## Google Compute Engine (GCE)
<a name="install-CloudWatch-Agent-on-Google-Cloud-gce"></a>

On a GCE instance, you install the agent package in the same way as on an on-premises server. The instance authenticates to AWS with its attached service account, which is federated to an AWS IAM role.

**The instance needs a service account**  
Instances receive the project's default service account when you create them, unless you opt out. Attaching a service account to an existing instance requires stopping the instance first, so neither the scripts nor the manual steps change it for you.

### Automated setup (recommended)
<a name="install-CloudWatch-Agent-on-Google-Cloud-gce-automated"></a>

The CloudWatch agent provides onboarding scripts that automate the setup. The scripts read the instance's service account, install the agent, and create the AWS IAM role and trust policy. The scripts configure the agent with a default OpenTelemetry configuration. This configuration collects host metrics (such as CPU, memory, disk, and network). It also starts an OpenTelemetry Protocol (OTLP) receiver for metrics, logs, and traces from applications on the instance. The agent enriches all of this telemetry and forwards it to the CloudWatch OTLP endpoints.

Run the Google Cloud step first, then the AWS trust step. Provide the role ARN that the AWS trust step creates or updates (by default, `arn:aws:iam::{{account-id}}:role/CloudWatchAgentServerRole`).

**Reusing an existing IAM role**  
Both scripts are safe to run even if the IAM role already exists. The AWS trust step merges the Google trust into the role's existing trust policy instead of replacing it, so other trust statements remain. It attaches `CloudWatchAgentServerPolicy` only if the role doesn't already have it, and leaves the role's other policies unchanged.

**To set up the agent on a GCE instance using the onboarding scripts**

1. On a machine with the Google Cloud CLI signed in (for example, Cloud Shell), run the Google Cloud step with the role ARN and the AWS Region. The script reads the instance's service account, installs and starts the agent, and prints the service account unique ID.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/gcp/setup.sh | \
     CWAGENT_PLATFORM=gcp_gce \
     CWAGENT_GCP_LOCATION={{zone}} \
     CWAGENT_GCP_INSTANCE_NAME={{instance-name}} \
     CWAGENT_AWS_ROLE_ARN={{role-arn}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

1. On a machine with AWS credentials that have IAM write access to the target account (for example, AWS CloudShell), run the AWS trust step with the service account unique ID from the previous step. The script creates the role, attaches `CloudWatchAgentServerPolicy`, and adds the Google web-identity trust.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/aws/setup.sh | \
     CWAGENT_PLATFORM=gcp_gce \
     CWAGENT_GCP_SA_UNIQUE_ID={{unique-id}} \
     CWAGENT_AWS_ROLE_ARN={{role-arn}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

### Manual setup
<a name="install-CloudWatch-Agent-on-Google-Cloud-gce-manual"></a>

**To find the instance's service account**
**Active Google Cloud project**  
The following `gcloud compute` commands act on the project that is active in the Google Cloud CLI. Confirm it with `gcloud config get-value project`, or add `--project {{project-id}}`, before you run them. Don't scope `gcloud iam service-accounts describe` to a project. A service account email is globally unique, and the account can belong to a different project than the instance.

1. Retrieve the email of the service account attached to the instance. If the command returns nothing, the instance has no service account.

   ```
   gcloud compute instances describe {{instance-name}} --zone {{zone}} --format 'value(serviceAccounts[0].email)'
   ```

1. Retrieve the service account's unique ID to use in the next procedure. The trust policy matches on this value, not on the email address.

   ```
   gcloud iam service-accounts describe {{service-account-email}} --format 'value(uniqueId)'
   ```

**To create the IAM role in your AWS account**

1. Create a trust policy that allows the service account to assume the role. Save it to a file named `trust-policy.json`. Replace {{unique-id}} with the service account unique ID.
**Reusing an existing IAM role (GCE)**  
If you reuse an existing role, merge this policy with the role's existing trust policy. Keep the `Sid` value. Every GCE statement uses the same `accounts.google.com` principal, so the `Sid` is what identifies the statement for this service account. A statement without one is replaced the next time you run the onboarding scripts.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "GCE{{unique-id}}",
         "Effect": "Allow",
         "Principal": { "Federated": "accounts.google.com" },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": { "StringEquals": { "accounts.google.com:aud": "{{unique-id}}", "accounts.google.com:sub": "{{unique-id}}", "accounts.google.com:oaud": "sts.amazonaws.com" } }
       }
     ]
   }
   ```

   To onboard more than one service account to the same role, add a separate statement for each one, with its own `Sid` and unique ID.

   On tokens that Google issues to a service account, IAM matches `sub` against the service account unique ID. It matches `aud` against the token's authorized party (`azp`), which Google also sets to the unique ID. It matches `oaud` against the audience that the agent requested the token for, which is `sts.amazonaws.com`.

1. Create the role and attach the CloudWatchAgentServerPolicy managed policy. Note the role ARN that the first command returns.

   ```
   aws iam create-role --role-name {{role-name}} --assume-role-policy-document file://trust-policy.json
   aws iam attach-role-policy --role-name {{role-name}} --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

**To install and start the agent**

1. Download and install the agent on the instance, in the same way as on an on-premises server. See [Install the CloudWatch agent on on-premises servers](install-CloudWatch-Agent-on-premise.md).

1. Set the AWS Region and the ARN of the role to assume, then start the agent with the default OpenTelemetry configuration (`default:otel`). The default OpenTelemetry configuration reads the role ARN from the `CWAGENT_ROLE_ARN` environment variable.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a set-env -e AWS_REGION={{region}}
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a set-env -e CWAGENT_ROLE_ARN={{role-arn}}
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m auto -c default:otel -s
   ```

## Google Kubernetes Engine (GKE)
<a name="install-CloudWatch-Agent-on-Google-Cloud-gke"></a>

On GKE, you install the agent through the Amazon CloudWatch Observability Helm chart. The cluster authenticates to AWS with a projected service account token that is federated to an AWS IAM role.

### Automated setup (recommended)
<a name="install-CloudWatch-Agent-on-Google-Cloud-gke-automated"></a>

The onboarding scripts automate the setup. The scripts read the cluster, install the chart, and create the AWS IAM role and trust policy. The chart installs the agent with a default OpenTelemetry configuration. This configuration enables OTel Container Insights. It also starts an OTLP receiver for metrics, logs, and traces from applications in the cluster. The agent enriches all of this telemetry and forwards it to the CloudWatch OTLP endpoints.

Run the Google Cloud step first, then the AWS trust step. The AWS trust step needs the cluster's OIDC issuer URL, which the Google Cloud step prints. Provide the role ARN that the AWS trust step creates or updates (by default, `arn:aws:iam::{{account-id}}:role/CloudWatchAgentServerRole`).

**Reusing an existing IAM role**  
Both scripts are safe to run even if the IAM role already exists. The AWS trust step merges the Google trust into the role's existing trust policy instead of replacing it, so other trust statements remain. It attaches `CloudWatchAgentServerPolicy` only if the role doesn't already have it, and leaves the role's other policies unchanged.

**To set up the agent on GKE using the onboarding scripts**

1. On a machine with the Google Cloud CLI signed in (for example, Cloud Shell), run the Google Cloud step with the role ARN and the AWS Region. The script installs the agent and prints the cluster's OIDC issuer URL.
**Tools the script needs to install the chart**  
The script installs the chart when `helm`, `kubectl`, and `gke-gcloud-auth-plugin` are all available. Otherwise it prints the commands for you to run from a shell that has them.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/gcp/setup.sh | \
     CWAGENT_PLATFORM=gcp_gke \
     CWAGENT_GCP_LOCATION={{location}} \
     CWAGENT_K8S_CLUSTER_NAME={{cluster-name}} \
     CWAGENT_AWS_ROLE_ARN={{role-arn}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

1. On a machine with AWS credentials that have IAM write access to the target account (for example, AWS CloudShell), run the AWS trust step with the OIDC issuer URL from the previous step. The script creates the role, attaches `CloudWatchAgentServerPolicy`, and federates the cluster issuer.

   ```
   curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/aws/setup.sh | \
     CWAGENT_PLATFORM=gcp_gke \
     CWAGENT_GCP_OIDC_ISSUER={{issuer-url}} \
     CWAGENT_AWS_ROLE_ARN={{role-arn}} \
     CWAGENT_AWS_REGION={{region}} \
     sh
   ```

### Manual setup
<a name="install-CloudWatch-Agent-on-Google-Cloud-gke-manual"></a>

**To find the cluster's OIDC issuer URL**
**Active Google Cloud project**  
The following `gcloud` commands act on the project that is active in the Google Cloud CLI. Confirm it with `gcloud config get-value project`, or add `--project {{project-id}}` to each command, before you run them.
**GKE serves the issuer by default**  
Every GKE cluster serves its OIDC discovery document, so there is no setting to enable. You construct the issuer URL from the project, location, and cluster name.

1. Confirm that you can read the cluster, and note its project, location, and name.

   ```
   gcloud container clusters describe {{cluster-name}} --location {{location}} --format 'value(name)'
   ```

1. Build the issuer URL in the following form. Use `locations` for both zonal and regional clusters.

   ```
   https://container.googleapis.com/v1/projects/{{project-id}}/locations/{{location}}/clusters/{{cluster-name}}
   ```

**To create the IAM role in your AWS account**

1. Register the cluster's OIDC issuer as an IAM OIDC identity provider. The audience (`--client-id-list`) is `sts.amazonaws.com`.

   ```
   aws iam create-open-id-connect-provider --url {{issuer-url}} --client-id-list sts.amazonaws.com
   ```

1. Create a trust policy that allows the agent's service account to assume the role. Save it to a file named `trust-policy.json`. Replace {{account-id}} with your AWS account ID and {{issuer-host}} with the issuer URL without the `https://` prefix.
**Reusing an existing IAM role (GKE)**  
If you reuse an existing role, merge this policy with the role's existing trust policy. Each statement is identified by its cluster-specific OIDC provider principal and its `Condition` block, not by a `Sid`, so you don't need to set or preserve one.

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

1. Configure `kubectl` to use the cluster. This command requires `gke-gcloud-auth-plugin`.

   ```
   gcloud container clusters get-credentials {{cluster-name}} --location {{location}}
   ```

1. Add the Amazon CloudWatch Observability Helm chart repository and install the chart. Set `k8sMode`, `roleArn`, `region`, and `clusterName`. Enable OTel Container Insights and assign the default OpenTelemetry configuration to the node agent.

   ```
   helm repo add aws-observability https://aws-observability.github.io/helm-charts
   helm repo update
   
   helm upgrade --install amazon-cloudwatch-observability aws-observability/amazon-cloudwatch-observability \
     --set k8sMode=GKE \
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