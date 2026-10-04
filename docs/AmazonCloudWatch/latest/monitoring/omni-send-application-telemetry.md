

# Send application telemetry
<a name="omni-send-application-telemetry"></a>

Deploy the CloudWatch agent where your application runs on Amazon EC2, Amazon ECS, Amazon EKS, an Azure VM, or Azure Kubernetes Service, point the application's OpenTelemetry exporter at it, and confirm data arrives in your space. If the application is not instrumented yet, add OpenTelemetry for Python, Node.js, Java, or .NET in the last step. The agent receives OTLP from your application and forwards metrics, traces, and logs to CloudWatch.

If you are monitoring an AI agent, see [Send AI agent telemetry](omni-send-ai-agent-telemetry.md). If your application runs on AWS Lambda, see [Send application telemetry from AWS Lambda](omni-send-application-telemetry-from-aws-lambda.md); Lambda has no collector to deploy.

Steps 1 and 2 show one environment at a time: expand the section for where your application runs in each step. Sections are collapsed so you can see the whole page; open only yours.

**If your application already uses OpenTelemetry**, do Steps 1 to 3 and stop; Step 4 is only for applications that are not instrumented yet. If you already run your own OpenTelemetry collector or the ADOT SDK, you need only an endpoint: see "Choose an endpoint" in [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

**Note**  
**Assisted setup.** The **Add source** wizard in the Omni web UI (**Settings › Ingestion**) generates these commands for your selections. From your coding agent, the Omni skills in the Agent Toolkit for AWS do the same; see [Use Omni skills](omni-use-omni-skills.md). The rest of this page is the manual path.

**Prerequisites**
+ **Transaction Search is enabled** in the account and Region that receive traces. Traces sent before it is enabled are not searchable. See [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).
+ You can attach IAM policies to the role your compute uses: an instance role, a task role, the agent's service account role, or the federated role on Azure.
+ For Step 4, your application's language is one of Python, Node.js, Java, or .NET. Frameworks with zero-code instrumentation are listed in [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md); others still work with the custom-instrumentation snippets.

**Step 1: Deploy the CloudWatch agent (platform team or administrator)**

Expand the environment your application runs on. Each section gives the install commands and the same resources as infrastructure as code, as tabs.

## Amazon EC2
<a name="omni-send-application-telemetry-amazon-ec2"></a>

On Amazon EC2, you attach a managed policy to the instance role, install the agent with the OTLP preset (per instance, or fleet-wide with a State Manager association), then continue to Step 2.

**Grant permissions**

The instance role needs `CloudWatchAgentServerPolicy`, which covers metrics, logs, and traces, bound to the instance through an instance profile.

**Install the agent and enable OTLP**

------
#### [ Install the agent ]

```
# 1. Connect (SSH, or Session Manager — no key or open port needed)
aws ssm start-session --target <instanceId>

# 2. Install the CloudWatch agent from Amazon S3
curl -fsSL -o /tmp/amazon-cloudwatch-agent.rpm \
  https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
sudo rpm -Uvh /tmp/amazon-cloudwatch-agent.rpm

# 3. Enable OTLP
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config -c default:otel -s
```
+ Install version 1.300071.0 or later, the first with OTLP support. The agent is available from Amazon S3, Systems Manager, and Amazon ECR, but not from the Amazon Linux yum repository.
+ `default:otel` turns on the OTLP receiver plus host metrics and span metrics.

**Important**  
A manual install does not scale. New or auto-replaced instances launch without a collector. For any Auto Scaling group, keep the agent installed with a State Manager association (in the CDK, Terraform, and CloudFormation tabs), EC2 user data, or a golden AMI.

------
#### [ CDK TypeScript ]

```
import { Role, ServicePrincipal, ManagedPolicy, InstanceProfile } from 'aws-cdk-lib/aws-iam';
import { CfnAssociation } from 'aws-cdk-lib/aws-ssm';

const role = new Role(this, 'OmniEC2TelemetryRole', {
  assumedBy: new ServicePrincipal('ec2.amazonaws.com'),
  managedPolicies: [
    ManagedPolicy.fromAwsManagedPolicyName('CloudWatchAgentServerPolicy'),
  ],
});
new InstanceProfile(this, 'OmniEC2TelemetryProfile', { role });
new CfnAssociation(this, 'OmniCollectorAssociation', {
  name: 'AWS-ConfigureAWSPackage',
  associationName: 'omni-cloudwatch-agent',
  targets: [{ key: 'tag:omni:monitor', values: ['true'] }],
  parameters: { action: ['Install'], name: ['AmazonCloudWatchAgent'] },
  scheduleExpression: 'rate(30 days)',
});
```

------
#### [ CDK Python ]

With the AWS CDK in Python or Java, build the same resources: an IAM role assumable by `ec2.amazonaws.com` with the managed policy `CloudWatchAgentServerPolicy`, an instance profile bound to that role, and a `CfnAssociation` with the same properties as the CloudFormation example.

------
#### [ Terraform ]

```
resource "aws_ssm_association" "omni_collector" {
  name             = "AWS-ConfigureAWSPackage"
  association_name = "omni-cloudwatch-agent"
  targets {
    key    = "tag:omni:monitor"
    values = ["true"]
  }
  parameters = { action = "Install", name = "AmazonCloudWatchAgent" }
  schedule_expression = "rate(30 days)"
}

resource "aws_instance" "app" {
  # …
  iam_instance_profile = aws_iam_instance_profile.app.name
  user_data = <<-EOF
    #!/bin/bash
    T=$(curl -sS -X PUT http://169.254.169.254/latest/api/token -H "X-aws-ec2-metadata-token-ttl-seconds: 600")
    until curl -sf -H "X-aws-ec2-metadata-token: $T" http://169.254.169.254/latest/meta-data/iam/security-credentials/ | grep -q .; do sleep 5; done
    curl -fsSL -o /tmp/cwa.rpm https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
    rpm -Uvh /tmp/cwa.rpm
    /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -c default:otel -s
    systemctl enable amazon-cloudwatch-agent
  EOF
}
```
+ An instance profile created in the same apply can take a minute to reach the instance metadata service. The user data waits for the role before `fetch-config`, because an agent that starts without credentials never sends telemetry.

------
#### [ CloudFormation ]

```
Resources:
  OmniEC2TelemetryRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement: [{ Effect: Allow, Action: sts:AssumeRole, Principal: { Service: ec2.amazonaws.com } }]
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
  OmniEC2TelemetryProfile:
    Type: AWS::IAM::InstanceProfile
    Properties: { Roles: [!Ref OmniEC2TelemetryRole] }
  OmniCollectorAssociation:
    Type: AWS::SSM::Association
    Properties:
      Name: AWS-ConfigureAWSPackage
      AssociationName: omni-cloudwatch-agent
      Targets: [{ Key: tag:omni:monitor, Values: ["true"] }]
      Parameters: { action: [Install], name: [AmazonCloudWatchAgent] }
      ScheduleExpression: rate(30 days)
```

------

For the full agent configuration reference, see [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPCloudWatchAgent.html) in the Amazon CloudWatch User Guide.

## Amazon ECS
<a name="omni-send-application-telemetry-amazon-ecs"></a>

On Amazon ECS (Fargate), you attach a managed policy to the task role, add the agent as a second container in the same task with the application depending on it, then continue to Step 2. Your application sends OTLP to `localhost`; the task shares one network namespace.

**Grant permissions and egress**

The task role needs `CloudWatchAgentServerPolicy`; the execution role needs `AmazonECSTaskExecutionRolePolicy`. The task needs egress to pull the agent image and reach the OTLP endpoints: a public IP in a public subnet, a NAT gateway, or VPC endpoints.

**Important**  
The application container must depend on the agent container with condition `START`. The agent image has no health check, so condition `HEALTHY` hangs startup.

**Add the sidecar to the task definition**

------
#### [ Setup script ]

```
curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/aws/setup.sh | \
  CWAGENT_PLATFORM=aws_ecs \
  CWAGENT_AWS_REGION=<region> \
  CWAGENT_AWS_ENABLE_TRANSACTION_SEARCH=true \
  sh
```
+ The script creates the task role and prints the agent container definition and the task role ARN. Paste both into your task definition.
+ It defaults to the Fargate launch type. For the EC2 launch type, set `CWAGENT_AWS_ECS_LAUNCH_TYPE=ec2`; the printed definition then adds host port mappings and container links.

------
#### [ CDK TypeScript ]

```
const agent = taskDef.addContainer('cwagent', {
  image: ecs.ContainerImage.fromRegistry('public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest'),
  environment: { CW_CONFIG_CONTENT: JSON.stringify({ opentelemetry: { collect: { otlp: {} } } }) },
  logging: ecs.LogDrivers.awsLogs({ streamPrefix: 'cwagent' }),
});
app.addContainerDependencies({ container: agent, condition: ecs.ContainerDependencyCondition.START });
taskDef.taskRole.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName('CloudWatchAgentServerPolicy'));
```

------
#### [ CDK Python ]

```
agent = task_def.add_container("cwagent",
    image=ecs.ContainerImage.from_registry("public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest"),
    environment={"CW_CONFIG_CONTENT": json.dumps({"opentelemetry": {"collect": {"otlp": {}}}})},
    logging=ecs.LogDrivers.aws_logs(stream_prefix="cwagent"))
app.add_container_dependencies(
    ecs.ContainerDependency(container=agent, condition=ecs.ContainerDependencyCondition.START))
task_def.task_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchAgentServerPolicy"))
```

With the AWS CDK (Java), add a second container with image `public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest` and environment variable `CW_CONFIG_CONTENT` set to `{"opentelemetry":{"collect":{"otlp":{}}}}`, make the application container depend on it with condition `START`, and attach `CloudWatchAgentServerPolicy` to the task role.

------
#### [ Terraform ]

```
container_definitions = jsonencode([
  { name = "cwagent", image = "public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest",
    environment = [{ name = "CW_CONFIG_CONTENT", value = "{\"opentelemetry\":{\"collect\":{\"otlp\":{}}}}" }],
    logConfiguration = { logDriver = "awslogs", options = { "awslogs-group" = "/ecs/cwagent", "awslogs-region" = "<region>", "awslogs-stream-prefix" = "cwagent" } } },
  { name = "app", image = "<your-image>",
    dependsOn = [{ containerName = "cwagent", condition = "START" }] }
])
```

------
#### [ CloudFormation ]

```
ContainerDefinitions:
  - Name: cwagent
    Image: public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest
    Environment:
      - { Name: CW_CONFIG_CONTENT, Value: '{"opentelemetry":{"collect":{"otlp":{}}}}' }
  - Name: app
    Image: <your-image>
    DependsOn: [{ ContainerName: cwagent, Condition: START }]
```

------

For the agent configuration reference, see [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPCloudWatchAgent.html).

## Amazon EKS
<a name="omni-send-application-telemetry-amazon-eks"></a>

On Amazon EKS, you install the CloudWatch Observability add-on with OTLP enabled and give its agent credentials, then continue to Step 2. The add-on runs the agent as a DaemonSet and exposes a `cloudwatch-agent` Service in the `amazon-cloudwatch` namespace; your pods send OTLP to that Service over cluster DNS, not to `localhost`. The add-on is installed with the AWS CLI regardless of how you deploy your application, so there is one installation path here.

```
curl -fsSL https://raw.githubusercontent.com/aws/amazon-cloudwatch-agent/main/scripts/aws/setup.sh | \
  CWAGENT_PLATFORM=aws_eks \
  CWAGENT_K8S_CLUSTER_NAME=<my-cluster> \
  CWAGENT_AWS_REGION=<region> \
  CWAGENT_AWS_ENABLE_TRANSACTION_SEARCH=true \
  sh
```
+ The script installs the EKS Pod Identity Agent, creates the agent role with a Pod Identity association, and installs the add-on with OTLP enabled. Pod Identity supplies the agent's credentials, so you do not annotate the service account for IAM roles for service accounts (IRSA).

Three settings must be right or telemetry never arrives, with no error in the agent log:
+ The OTLP receiver must be bound to `0.0.0.0`, not the default `localhost`, or it refuses cross-pod traffic. If application OTLP is refused after the script runs, apply the override and restart the DaemonSet:

```
aws eks update-addon --cluster-name <my-cluster> --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"agent":{"config":{"opentelemetry":{"collect":{"otlp":{"grpc_endpoint":"0.0.0.0:4317","http_endpoint":"0.0.0.0:4318"}}}}}}'
kubectl -n amazon-cloudwatch rollout restart daemonset/cloudwatch-agent
```
+ The agent must have credentials through Pod Identity (the script) or an IRSA-annotated service account. The add-on's `--service-account-role-arn` flag does not annotate the service account; without the annotation the agent falls back to the node role and its exports are rejected.
+ Application logs are in the cluster-scoped log group `/aws/cwagent/<my-cluster>/otlp`, not in `/aws/cwagent/otlp`.

For a manual install with IRSA and the add-on configuration reference, see [Install the CloudWatch Observability add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html) in the Amazon CloudWatch User Guide.

## Azure VM
<a name="omni-send-application-telemetry-azure-vm"></a>

On an Azure VM, you federate the VM's managed identity to an IAM role and install the CloudWatch agent on the VM, then continue to Step 2. The agent sends telemetry with temporary AWS credentials instead of a stored key; your application sends OTLP to `localhost`.

The complete procedure, including the OpenID Connect (OIDC) federation, the IAM role trust policy, and the onboarding script, is in [Install the CloudWatch agent on Azure](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-Azure.html) in the Amazon CloudWatch User Guide. Follow the VM section there, then return to Step 2.

## Azure AKS
<a name="omni-send-application-telemetry-azure-aks"></a>

On Azure Kubernetes Service, you federate workload identity for the `cloudwatch-agent` service account to an IAM role and install the CloudWatch Observability Helm chart, then continue to Step 2. Pods send OTLP to the `cloudwatch-agent` Service over cluster DNS.

The complete procedure, including the OIDC federation and the Helm values, is in [Install the CloudWatch agent on Azure](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-Azure.html) in the Amazon CloudWatch User Guide. Follow the AKS section there, then return to Step 2.

**Note**  
Unlike the EKS add-on, the AKS Helm chart's OTLP receiver accepts cross-pod traffic by default; no `0.0.0.0` override is needed.

**Step 2: Point your application at the agent (developer)**

Set these environment variables on the application, never on the agent: one agent serves many services and already enriches telemetry with infrastructure attributes. The endpoint and the place the variables live depend on your environment, and the port and protocol depend on your language; expand the same section you chose in Step 1, then choose your language.

## Amazon EC2
<a name="omni-send-application-telemetry-amazon-ec2-2"></a>

On Amazon EC2, set these in the application's service unit or start script, for example `Environment=` lines in a systemd unit:

------
#### [ Python, Java, .NET ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------
#### [ Node.js ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------

## Amazon ECS
<a name="omni-send-application-telemetry-amazon-ecs-2"></a>

On Amazon ECS, set these in the application container's `environment` block:

------
#### [ Python, Java, .NET ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------
#### [ Node.js ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------

## Amazon EKS
<a name="omni-send-application-telemetry-amazon-eks-2"></a>

On Amazon EKS, set these in the container's `env` block in the pod spec:

------
#### [ Python, Java, .NET ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://cloudwatch-agent.amazon-cloudwatch.svc.cluster.local:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------
#### [ Node.js ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://cloudwatch-agent.amazon-cloudwatch.svc.cluster.local:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------

## Azure VM
<a name="omni-send-application-telemetry-azure-vm-2"></a>

On an Azure VM, set these in the application's service unit or start script:

------
#### [ Python, Java, .NET ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------
#### [ Node.js ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------

## Azure AKS
<a name="omni-send-application-telemetry-azure-aks-2"></a>

On Azure Kubernetes Service, set these in the container's `env` block in the pod spec:

------
#### [ Python, Java, .NET ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://cloudwatch-agent.amazon-cloudwatch.svc.cluster.local:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------
#### [ Node.js ]

```
OTEL_SERVICE_NAME=<checkout-api>
OTEL_RESOURCE_ATTRIBUTES=service.namespace=<checkout>
OTEL_EXPORTER_OTLP_ENDPOINT=http://cloudwatch-agent.amazon-cloudwatch.svc.cluster.local:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
```

------

**Step 3: Verify**

Use the automated verification in the Omni web UI. In your space, open **Settings › Ingestion** and choose your source: the **Add source** flow's verification step confirms the agent is reporting and your application's telemetry is arriving, and points at the failing setting when it is not. Run it after every deployment change.

If verification fails, see the "Troubleshoot missing telemetry" section of this page.

## Verify manually
<a name="omni-send-application-telemetry-verify-manually"></a>

**The agent is reporting**

------
#### [ Amazon EC2 ]

On Amazon EC2, `sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status` reports `running`. In your space, host metrics for the instance appear within about five minutes.

------
#### [ Amazon ECS ]

On Amazon ECS, the task shows both containers `RUNNING`. In your space, container metrics for the task appear within about five minutes.

------
#### [ Amazon EKS ]

On Amazon EKS, `kubectl -n amazon-cloudwatch get daemonset cloudwatch-agent` shows all pods ready. In your space, container metrics for the cluster appear within about five minutes.

------
#### [ Azure VM ]

On an Azure VM, `amazon-cloudwatch-agent-ctl -a status` reports `running`. In your space, host metrics for the VM appear within about five minutes.

------
#### [ Azure AKS ]

On Azure Kubernetes Service, `kubectl -n amazon-cloudwatch get daemonset cloudwatch-agent` shows all pods ready. In your space, container metrics for the cluster appear within about five minutes.

------

**Your application appears**

If you run your own OpenTelemetry Collector instead of the CloudWatch agent, this is your check. If your application is not instrumented yet, do Step 4 first, then return to this check. Restart the application, then open your space. In **Application map**, the service appears under the `service.name` you set. In **Trace Explorer**, a trace for a recent request shows the entry span for your service with the resource attributes you set. Application logs are in `/aws/cwagent/otlp` on EC2, ECS, and Azure VMs, or `/aws/cwagent/<cluster>/otlp` on EKS and AKS. A custom metric is queryable with PromQL by its OpenTelemetry name, for example `sum({__name__="orders.placed"})`.

**Step 4 (optional): Instrument your application with OpenTelemetry (developer)**

Choose your language. The choice applies to every code sample below and is remembered on the other pages in this guide. Most HTTP frameworks, database clients, and messaging libraries are traced with no code changes; the table in each tab lists the frameworks with documented notes, and the OpenTelemetry registry lists the rest. For a framework not covered, the custom-instrumentation snippet still works.

**Install the OpenTelemetry SDK**

------
#### [ Python ]

```
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
```
+ In a container, both commands belong in the Dockerfile.
+ On a host running Amazon Linux 2023, the default `python3` is 3.9 and the CloudWatch plugin requires Python 3.10 or later: install and use `python3.11` (`dnf install -y python3.11 python3.11-pip`).

------
#### [ Node.js ]

```
npm install @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node \
  @opentelemetry/exporter-trace-otlp-grpc @opentelemetry/api @opentelemetry/api-logs
```

------
#### [ Java ]

```
curl -L -o opentelemetry-javaagent.jar \
  https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar
```
+ The agent does not put the OpenTelemetry API on your compile classpath. To add custom instrumentation, add `io.opentelemetry:opentelemetry-api` at compile scope, not `provided`, because the agent bridges to the application's own API classes at runtime.

------
#### [ .NET ]

```
# Console application
dotnet add package OpenTelemetry
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol

# ASP.NET Core or gRPC service
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Http
```

------

**Add the CloudWatch plugin for OpenTelemetry with the SDK.** The plugin generates the request, error, and duration span metrics that power the service views (including the **Errors** metric), and it meters every span before sampling, so those metrics reflect all requests rather than the sampled subset. It is available for Python, Node.js, Java, and .NET. The following table lists the package names and links. The plugin needs a metrics pipeline to emit into. If your application exports traces but no metrics, the plugin stays inert and **Errors** remains unpopulated. Configure a metrics exporter alongside your trace exporter.

If you instrument with the ADOT SDK instead and sample, your span metrics are computed from the sampled spans only.


| Language | Package | Documentation | 
| --- | --- | --- | 
| Java | software.amazon.opentelemetry:cloudwatch-plugin-otel | [Java plugin README](https://github.com/aws-observability/aws-otel-java-instrumentation/blob/main/cloudwatch-plugin-otel/README.md) | 
| Python | cloudwatch-plugin-otel | [Python plugin README](https://github.com/aws-observability/aws-otel-python-instrumentation/blob/main/cloudwatch-plugin-otel/README.md) | 
| Node.js | @aws/cloudwatch-plugin-otel | [Node.js plugin README](https://github.com/aws-observability/aws-otel-js-instrumentation/blob/main/cloudwatch-plugin-otel/README.md) | 
| .NET | AWS.OpenTelemetry.CloudWatchPluginOtel | [.NET plugin README](https://github.com/aws-observability/aws-otel-dotnet-instrumentation/blob/main/src/AWS.OpenTelemetry.CloudWatch.Plugin/README.md) | 

**Enable auto-instrumentation**

Run the application under the auto-instrumentation agent for its language. Framework, HTTP, and database calls are traced with no code changes.

------
#### [ Python ]

```
opentelemetry-instrument python <app.py>
# FastAPI
opentelemetry-instrument uvicorn <app:app> --host 0.0.0.0 --port 8000
```
+ `opentelemetry-instrument` wraps the process, so it replaces your entry point. For FastAPI under uvicorn, wrap `uvicorn`, not `python app.py`.
+ For Django, set `DJANGO_SETTINGS_MODULE` in the environment and run with `--noreload`.
+ Python exports logs only when `OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true` is also set in the environment.

------
#### [ Node.js ]

```
node --require @opentelemetry/auto-instrumentations-node/register <app.js>
```

------
#### [ Java ]

```
java -javaagent:./opentelemetry-javaagent.jar -jar <app.jar>
```

------
#### [ .NET ]

```
# ASP.NET Core or gRPC: install and enable the profiler
curl -sSfL https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest/download/otel-dotnet-auto-install.sh -o install.sh && sh install.sh
. $HOME/.otel-dotnet-auto/instrument.sh
dotnet <MyService.dll>
```

```
// Console application: bootstrap once at startup
using var tracerProvider = Sdk.CreateTracerProviderBuilder().AddSource("checkout").AddOtlpExporter().Build();
using var meterProvider  = Sdk.CreateMeterProviderBuilder().AddMeter("checkout").AddOtlpExporter().Build();
```

------

**Add custom instrumentation**

Set business attributes on the active span, mark your entry span as a server span so it counts in request metrics, and record a custom metric. These snippets assume the SDK is initialized by the step above.

------
#### [ Python ]

```
from opentelemetry import trace, metrics
from opentelemetry.trace import SpanKind

tracer = trace.get_tracer("checkout")
orders = metrics.get_meter("checkout").create_counter("orders.placed")

def place_order(cart):
    with tracer.start_as_current_span("place_order", kind=SpanKind.SERVER) as span:
        span.set_attribute("cart.items", len(cart))
        orders.add(1)
```


| Framework | Notes | 
| --- | --- | 
| FastAPI | Traced automatically under opentelemetry-instrument uvicorn. | 
| Flask | Traced automatically under opentelemetry-instrument python. | 
| Django | Views are traced automatically when DJANGO\_SETTINGS\_MODULE is set in the environment; run with --noreload. | 

------
#### [ Node.js ]

```
const { trace, metrics } = require('@opentelemetry/api');
const { logs } = require('@opentelemetry/api-logs');
const orders = metrics.getMeter('checkout').createCounter('orders.placed');
const logger = logs.getLogger('checkout');

function placeOrder(cart) {
  trace.getActiveSpan()?.setAttribute('cart.items', cart.length);
  orders.add(1);
  logger.emit({ body: 'order placed', attributes: { 'cart.items': cart.length } });
}
```
+ Logs must go through the OpenTelemetry logs API, as `logger.emit()` does here. Setting `OTEL_LOGS_EXPORTER=otlp` alone produces no records.


| Framework | Notes | 
| --- | --- | 
| Express | Traced automatically by the auto-instrumentations package. | 
| gRPC | Server and client calls are traced automatically. | 

------
#### [ Java ]

```
static final LongCounter ORDERS =
    GlobalOpenTelemetry.getMeter("checkout").counterBuilder("orders.placed").build();

@WithSpan(kind = SpanKind.SERVER)
public void placeOrder(List<Item> cart) {
  Span.current().setAttribute("cart.items", cart.size());
  ORDERS.add(1);
}
```
+ `@WithSpan` needs `io.opentelemetry.instrumentation:opentelemetry-instrumentation-annotations`, whose version tracks the agent release, not the API version.


| Framework | Notes | 
| --- | --- | 
| Spring Boot | Controllers are traced by the Java agent; annotate service methods with @WithSpan for business spans. | 
| gRPC | Calls are traced by the Java agent. | 

------
#### [ .NET ]

```
static readonly Meter Meter = new("checkout");
static readonly Counter<long> Orders = Meter.CreateCounter<long>("orders.placed");

Activity.Current?.SetTag("cart.items", cart.Count);
Orders.Add(1);
```
+ Register the `Meter` on the metrics builder with `AddMeter("checkout")`. Without it the counter is dropped.


| Framework | Notes | 
| --- | --- | 
| ASP.NET Core | Requests are traced by the profiler or AddAspNetCoreInstrumentation(). Add builder.Logging.AddOpenTelemetry(o => o.AddOtlpExporter()) for logs. | 
| gRPC | Client instrumentation is a separate prerelease package (OpenTelemetry.Instrumentation.GrpcNetClient); .AddHttpClientInstrumentation() covers the HTTP transport meanwhile. | 

------

Query custom metrics with PromQL by their OpenTelemetry name, for example `sum({__name__="orders.placed"})`. Restart the application and repeat Step 3.

**Troubleshoot missing telemetry**


| Symptom | Cause and fix | 
| --- | --- | 
| Logs and spans arrive, metrics do not | A metric attribute value is longer than 1024 characters; the CloudWatch OTLP metrics endpoint rejects the whole batch with HTTP 400. Trim the attribute. For Java, the usual cause is process.command\_args on a long classpath: set OTEL\_JAVA\_DISABLED\_RESOURCE\_PROVIDERS=io.opentelemetry.instrumentation.resources.ProcessResourceProvider. | 
| Nothing arrives; the SDK logs connection errors | Port and protocol do not match: 4317 is gRPC and 4318 is HTTP. Set OTEL\_EXPORTER\_OTLP\_PROTOCOL to match the port. | 
| Nothing arrives on ECS; the task hangs at startup | The application container depends on the agent with condition HEALTHY. Use START. | 
| Nothing arrives on ECS; the agent logs AccessDenied or times out | The task role lacks CloudWatchAgentServerPolicy, or the task has no egress to the OTLP endpoints. Attach the policy; add a public IP, NAT gateway, or VPC endpoints. | 
| Nothing arrives on EKS; no agent errors | The receiver is bound to localhost, or the agent service account has no credentials. Apply the 0.0.0.0 override; use Pod Identity or annotate the service account for IRSA, then restart the DaemonSet. | 
| Nothing arrives from a new EC2 instance | The agent started before the instance profile reached the instance metadata service. Wait for the role in user data before fetch-config, or restart the agent. | 
| Nothing arrives from an Azure VM or AKS | The federation is not complete: the IAM role trust policy does not match the identity, or the service account is not annotated. Recheck the federation steps in [Install the CloudWatch agent on Azure](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-Azure.html). | 
| The service appears under the agent's name | OTEL\_SERVICE\_NAME is set on the agent, not the application. Move it to the application. | 
| A Python service shows one process span and no route spans | opentelemetry-instrument wrapped python instead of the server. Wrap uvicorn or gunicorn. | 
| Traces exist but are not searchable | Transaction Search was enabled after the traces were sent. Enable it, then send new traces. | 
| Only some requests appear in the trace list | Transaction Search indexes 1 percent of spans by default for the trace list; the spans themselves are all stored. Raise the indexing percentage in Transaction Search settings. | 