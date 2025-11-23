# Enable your applications on Amazon EKS clusters

CloudWatch Application Signals is supported for Java, Python, Node.js, and .NET applications. To enable Application Signals for your applications on an existing Amazon EKS cluster, you can use the AWS Management Console, AWS CDK, or CloudWatch Observability
add-on Auto monitor advanced configuration.

###### Topics

- [Enable Application Signals on an Amazon EKS cluster using the console](#CloudWatch-Application-Signals-Enable-EKS-Console "#CloudWatch-Application-Signals-Enable-EKS-Console")
- [Enable Application Signals on an Amazon EKS cluster using the CloudWatch Observability add-on advanced configuration](#CloudWatch-Application-Signals-Enable-EKS-Addon "#CloudWatch-Application-Signals-Enable-EKS-Addon")
- [Enable Application Signals on Amazon EKS using AWS CDK](#CloudWatch-Application-Signals-EKS-CDK "#CloudWatch-Application-Signals-EKS-CDK")
- [Enable Application Signals on Amazon EKS using Model Context Protocol (MCP)](#CloudWatch-Application-Signals-EKS-MCP "#CloudWatch-Application-Signals-EKS-MCP")

## Enable Application Signals on an Amazon EKS cluster using the console

To enable CloudWatch Application Signals on your applications on an existing Amazon EKS cluster, use the

instructions in this section.

###### Important

If you are already using OpenTelemetry with an application that you intend to enable for
Application Signals, see [Supported systems](CloudWatch-Application-Signals-supportmatrix.md "CloudWatch-Application-Signals-supportmatrix.md")
before you enable Application Signals.

###### To enable Application Signals for your applications on an existing Amazon EKS cluster

###### Note

If you haven't already enabled Application Signals, follow the instructions in [Enable Application Signals in your account](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md") and then follow the procedure below.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Application Signals**.
3. For **Specify platform**, choose **EKS**.
4. For **Select an EKS cluster**, select the cluster where you want to
   enable Application Signals.
5. If this cluster does not already have the Amazon CloudWatch Observability EKS add-on enabled, you are prompted
   to enable it. If this is the case, do the following:
   1. Choose **Add CloudWatch Observability EKS add-on**. The Amazon EKS console appears.
   2. Select the check box for **Amazon CloudWatch Observability**
      and choose **Next**.

   The CloudWatch Observability EKS add-on enables both Application Signals and CloudWatch Container Insights with enhanced observability
   for Amazon EKS. For more information about Container Insights, see
   [Container Insights](ContainerInsights.md "ContainerInsights.md"). 3. Select the most recent version of the add-on to install. 4. Select an IAM role to use for the add-on. If you choose **Inherit from node**,
   attach the correct permissions to the IAM role used by your worker nodes.
   Replace `my-worker-node-role` with the IAM role used by your Kubernetes worker nodes.

   ```
   aws iam attach-role-policy \
   --role-name `my-worker-node-role` \
   --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy \
   --policy-arn arn:aws:iam::aws:policy/AWSXRayWriteOnlyAccess
   ```

   5. If you want to create a service role to use the add-on, see
      [Install the CloudWatch agent with the
      Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md").
   6. Choose **Next**, confirm the information on the screen, and
      choose **Create**.
   7. In the next screen, choose **Enable CloudWatch Application Signals** to return to the CloudWatch console
      and finish the process.

6. There are two options for enabling your applications for Application Signals. For consistency, we recommend that you choose one option per cluster.
   - The **Console** option is simpler. Using this method causes your pods to
     restart immediately.
   - The **Annotate Manifest File** method gives you more control of when your
     pods restart, and can also help you manage your monitoring in a more decentralized
     way if you don’t want to centralize it.

###### Note

If you are enabling Application Signals for a Node.js application with ESM, skip to

[Setting up a Node.js application with the ESM module format](#EKS-NodeJs-ESM "#EKS-NodeJs-ESM") instead.

Console
The **Console** option uses the advanced configuration of the
Amazon CloudWatch Observability EKS add-on to setup Application Signals for your services.
For more information about the add-on, see [(Optional)
Additional configuration](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration "install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration").

If you don’t see a list of workloads and namespaces, ensure you have the right permissions to view them for this cluster.
For more information, see [Required permissions](../../../eks/latest/userguide/view-kubernetes-resources.md#view-kubernetes-resources-permissions "../../../eks/latest/userguide/view-kubernetes-resources.md#view-kubernetes-resources-permissions").

You can either monitor all service workloads by selecting the **Auto monitor** check box or selectively choose specific workloads and namespaces to monitor.

To monitor all service workload(s) with Auto monitor:

    1. Select the **Auto monitor** check box to automatically select all service workload(s) in a cluster.
    2. Choose **Auto restart** to restart all workload pods to enable Application Signals immediately with AWS Distro for OpenTelemetry auto-instrumentation (ADOT) SDKs injected into your pods.
    3. Choose **Done** . When **Auto restart** is selected, CloudWatch Observability EKS add-on will enable Application Signals immediately.
     Otherwise, Application Signals will be enabled during the next deployment of each workload.

You can monitor single workloads or entire namespaces.

To monitor a single workload:

    1. Select the check box by the workload that you want to monitor.
    2. Use the **Select language(s)** dropdown list to select the language of the workload. Select the languages that
     you want to enable Application Signals for, and then choose the check mark icon (✓) to save this selection.


    For Python applications, ensure your application follows the required prerequisites before continuing.
     For more information, see [Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").
    3. Choose **Done**. The Amazon CloudWatch Observability EKS add-on will immediately inject AWS Distro for OpenTelemetry autoinstrumentation (ADOT)
     SDKs into your pods and trigger pod restarts to enable collection of application metrics and traces.

To monitor an entire namespace:

    1. Select the check box by the namespace that you want to monitor.
    2. Use the **Select language(s)** dropdown list to select the language of the namespace. Select the languages that
     you want to enable Application Signals for, and then choose the check mark icon (✓) to save this selection. This applies it to all workloads in this namespace,
     whether they are currently deployed or will be deployed in the future.


    For Python applications, ensure your application follows the required prerequisites before continuing.
     For more information, see [Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").
    3. Choose **Done**. The Amazon CloudWatch Observability EKS add-on will immediately inject AWS Distro for OpenTelemetry autoinstrumentation (ADOT)
     SDKs into your pods and trigger pod restarts to enable collection of application metrics and traces.

To enable Application Signals in another Amazon EKS cluster, choose **Enable Application Signals** from the **Services** screen.

Annotate manifest file
In the CloudWatch console, the **Monitor Services**
section explains that you must add an annotation to a manifest YAML in the cluster.
Adding this annotation auto-instruments the application to send metrics, traces, and
logs to Application Signals.

You have two options for the annotation:

    * **Annotate Workload** auto-instruments a single workload in the cluster.
    * **Annotate Namespace** auto-instruments all workloads deployed in the selected namespace.

Choose one of those options, and follow the appropriate steps:

    * To annotate a single workload:




    	1. Choose **Annotate Workload**.
    	2. Paste one of the following lines into
    	 the `PodTemplate` section of the workload manifest file.




    		+ **For Java workloads:** `annotations: instrumentation.opentelemetry.io/inject-java: "true"`
    		+ **For Python workloads:** `annotations: instrumentation.opentelemetry.io/inject-python: "true"`


    		For Python applications, there are additional required configurations. For more information, see [Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").
    		+ **For .NET workloads**
    		`annotations: instrumentation.opentelemetry.io/inject-dotnet:
    		 "true"`


    		###### Note

    		To enable Application Signals for a .NET workload on Alpine
    		 Linux (`linux-musl-x64`) based images, add the following
    		 annotation.


    		```
    		instrumentation.opentelemetry.io/otel-dotnet-auto-runtime: "linux-musl-x64"
    		```
    		+ **For Node.js workloads:**
    		`annotations: instrumentation.opentelemetry.io/inject-nodejs:
    		 "true"`
    	3. In your terminal, enter `kubectl apply -f `your_deployment_yaml`` to
    	 apply the change.
    * To annotate all workloads in a namespace:




    	1. Choose **Annotate Namespace**.
    	2. Paste one of the following lines into the metadata section of the namespace manifest file. If

    	 the namespace includes Java, Python, and .NET workloads, paste all of the
    	 following lines into the namespace manifest file.




    		+ **If there are Java workloads in the namespace:** `annotations: instrumentation.opentelemetry.io/inject-java: "true"`
    		+ **If there are Python workloads in the namespace:** `annotations: instrumentation.opentelemetry.io/inject-python: "true"`


    		For Python applications, there are additional required configurations. For more information, see [Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").
    		+ **If there are .NET workloads in the namespace:**
    		`annotations: instrumentation.opentelemetry.io/inject-dotnet:
    		 "true"`
    		+ **If there are Node.JS workloads in the namespace:**
    		`annotations: instrumentation.opentelemetry.io/inject-nodejs:
    		 "true"`
    	3. In your terminal, enter `kubectl apply -f `your_namespace_yaml`` to
    	 apply the change.
    	4. In your terminal, enter a command to restart all pods in the namespace. An example command to
    	 restart deployment workloads
    	 is `kubectl rollout restart deployment -n `namespace_name``

7. Choose **View Services when done**. This takes you to the Application Signals Services view,
   where you can see the data that Application Signals is collecting. It might take a few minutes for data to appear.

To enable Application Signals in another Amazon EKS cluster, choose **Enable Application Signals** from the
**Services** screen.

For more information about the **Services** view, see
[Monitor the operational health of your applications with Application Signals](Services.md "Services.md").

###### Note

If you're using a WSGI server for your Python application, see [No Application Signals data for Python application that uses a WSGI server](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-Python-WSGI "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-Python-WSGI") for information to make Application Signals work.

We've also identified other considerations that you should keep in mind when enabling Python applications
for Application Signals. For more information, see
[Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").

### Setting up a Node.js application with the ESM module format

We provide limited support for Node.js applications with the ESM module format. For
details, see [Known limitations about Node.js with ESM](CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations "CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations").

For the ESM module format, enabling Application Signals through the console or by annotating the manifest file doesn’t work. Skip step 8
of the previous procedure, and do the following instead.

###### To enable Application Signals for a Node.js application with ESM

1. Install the relevant dependencies to your Node.js application for autoinstrumentation:

```
npm install @aws/aws-distro-opentelemetry-node-autoinstrumentation
npm install @opentelemetry/instrumentation@0.54.0
```

2. Add the following environmental variables to the Dockerfile for your application and build the image.

```
...
ENV OTEL_AWS_APPLICATION_SIGNALS_ENABLED=true
ENV OTEL_TRACES_SAMPLER_ARG='endpoint=http://cloudwatch-agent.amazon-cloudwatch:2000'
ENV OTEL_TRACES_SAMPLER='xray'
ENV OTEL_EXPORTER_OTLP_PROTOCOL='http/protobuf'
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT='http://cloudwatch-agent.amazon-cloudwatch:4316/v1/traces'
ENV OTEL_AWS_APPLICATION_SIGNALS_EXPORTER_ENDPOINT='http://cloudwatch-agent.amazon-cloudwatch:4316/v1/metrics'
ENV OTEL_METRICS_EXPORTER='none'
ENV OTEL_LOGS_EXPORTER='none'
ENV NODE_OPTIONS='--import @aws/aws-distro-opentelemetry-node-autoinstrumentation/register --experimental-loader=@opentelemetry/instrumentation/hook.mjs'
ENV OTEL_SERVICE_NAME='`YOUR_SERVICE_NAME`' #replace with a proper service name
ENV OTEL_PROPAGATORS='tracecontext,baggage,b3,xray'
...

# command to start the application
# for example
# CMD ["node", "index.mjs"]
```

3. Add the environmental variables `OTEL_RESOURCE_ATTRIBUTES_POD_NAME`, `OTEL_RESOURCE_ATTRIBUTES_NODE_NAME`,
   `OTEL_RESOURCE_ATTRIBUTES_DEPLOYMENT_NAME`, `POD_NAMESPACE` and `OTEL_RESOURCE_ATTRIBUTES` to the deployment yaml file for the application. For example:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodejs-app
  labels:
    app: nodejs-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nodejs-app
  template:
    metadata:
      labels:
        app: nodejs-app
      # annotations:
      # make sure this annotation doesn't exit
      #   instrumentation.opentelemetry.io/inject-nodejs: 'true'
    spec:
      containers:
      - name: nodejs-app
        image:`your-nodejs-application-image` #replace with a proper image uri
        imagePullPolicy: Always
        ports:
        - containerPort: 8000
        env:
          - name: OTEL_RESOURCE_ATTRIBUTES_POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
          - name: OTEL_RESOURCE_ATTRIBUTES_NODE_NAME
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
          - name: OTEL_RESOURCE_ATTRIBUTES_DEPLOYMENT_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.labels['app'] # Assuming 'app' label is set to the deployment name
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                fieldPath: metadata.namespace
          - name: OTEL_RESOURCE_ATTRIBUTES
            value: "k8s.deployment.name=$(OTEL_RESOURCE_ATTRIBUTES_DEPLOYMENT_NAME),k8s.namespace.name=$(POD_NAMESPACE),k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME)"
```

4. Deploy the Node.js application to the cluster.

Once you have enabled your applications on the Amazon EKS Clusters, you can monitor your application health. For more information, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md").

## Enable Application Signals on an Amazon EKS cluster using the CloudWatch Observability add-on advanced configuration

By default, OpenTelemetry (OTEL) based Application Performance Monitoring (APM) is enabled through Application Signals when installing either the
CloudWatch Observability EKS add-on (V5.0.0 or greater) or the Helm chart. You can further customize specific settings using the advanced configuration for the Amazon EKS add-on or by overriding values with the Helm chart.

###### Note

If you use any OpenTelemetry (OTEL) based APM solution, enabling Application Signals affects your existing observability setup. Review your current implementation before proceeding.
To maintain your existing APM setup after upgrading to V5.0.0 or later, see [Opt out of Application Signals](install-CloudWatch-Observability-EKS-addon.md#Opting-out-App-Signals "install-CloudWatch-Observability-EKS-addon.md#Opting-out-App-Signals").

CloudWatch Observability Add-on also provides additional fine-grained control to include or exclude specific services as needed in the new advanced configuration. For more information, see [Enabling APM through Application Signals for your Amazon EKS cluster](install-CloudWatch-Observability-EKS-addon.md#Container-Insights-setup-EKS-appsignalsconfiguration "install-CloudWatch-Observability-EKS-addon.md#Container-Insights-setup-EKS-appsignalsconfiguration")
.

## Enable Application Signals on Amazon EKS using AWS CDK

If you haven't enabled Application Signals in this account yet, you must grant Application
Signals the permissions it needs to discover your services. See [Enable Application Signals in your account](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md").

1. Enable Application Signals for your applications.

```
import { aws_applicationsignals as applicationsignals } from 'aws-cdk-lib';

const cfnDiscovery = new applicationsignals.CfnDiscovery(this,
  'ApplicationSignalsServiceRole', { }
);
```

The Discovery CloudFormation resource grants Application Signals the following permissions:

    * `xray:GetServiceGraph`
    * `logs:StartQuery`
    * `logs:GetQueryResults`
    * `cloudwatch:GetMetricData`
    * `cloudwatch:ListMetrics`
    * `tag:GetResources`

For more information about this role, see
[Service-linked role permissions for
CloudWatch Application Signals](using-service-linked-roles.md#service-linked-role-signals "using-service-linked-roles.md#service-linked-role-signals"). 2. Install the `amazon-cloudwatch-observability` add-on.

    1. Create an IAM role with the `CloudWatchAgentServerPolicy` and the OIDC associated with the cluster.


    ```
    const cloudwatchRole = new Role(this, 'CloudWatchAgentAddOnRole', {
        assumedBy: new OpenIdConnectPrincipal(cluster.openIdConnectProvider),
        managedPolicies: [ManagedPolicy.fromAwsManagedPolicyName('CloudWatchAgentServerPolicy')],
    });
    ```

3. Install the add-on with the IAM role created above.

```
new CfnAddon(this, 'CloudWatchAddon', {
    addonName: 'amazon-cloudwatch-observability',
    clusterName: cluster.clusterName,
    serviceAccountRoleArn: cloudwatchRole.roleArn
});
```

4. Add one of the following into the `PodTemplate` section of your workload manifest file.

| Language | File                                                   |
| -------- | ------------------------------------------------------ |
| Java     | instrumentation.opentelemetry.io/inject-java: "true"   |
| Python   | instrumentation.opentelemetry.io/inject-python: "true" |
| .Net     | instrumentation.opentelemetry.io/inject-dotnet: "true" |
| Node.js  | instrumentation.opentelemetry.io/inject-nodejs: "true" |

```
const deployment = {
  apiVersion: "apps/v1",
  kind: "Deployment",
  metadata: { name: "`sample-app`" },
  spec: {
    replicas: 3,
    selector: {
      matchLabels: {
        "app": "`sample-app`"
      }
    },
    template: {
      metadata: {
        labels: {
          "app": "`sample-app`"
        },
        annotations: {
          "instrumentation.opentelemetry.io/inject-`$LANG`": "true"
        }
      },
      spec: {...},
    },
  },
};

cluster.addManifest('`sample-app`', deployment)
```

## Enable Application Signals on Amazon EKS using Model Context Protocol (MCP)

You can use the CloudWatch Application Signals Model Context Protocol (MCP) server to enable Application Signals on your Amazon EKS clusters through conversational AI interactions. This provides a natural language interface for setting up Application Signals monitoring.

The MCP server automates the enablement process by understanding your requirements and generating the appropriate configuration. Instead of manually following console steps or writing CDK code, you can simply describe what you want to enable.

### Prerequisites

Before using the MCP server to enable Application Signals, ensure you have:

- A Development Environment that supports MCP (such as Kiro, Claude Desktop, VSCode with MCP extensions, or other MCP-compatible tools)
- The CloudWatch Application Signals MCP server configured in your IDE. For detailed setup instructions, see [CloudWatch Application Signals MCP Server documentation](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server").

### Using the MCP server

Once you have configured the CloudWatch Application Signals MCP server in your IDE, you can request enablement guidance using natural language prompts. While the coding assistant can infer context from your project structure, providing specific details in your prompts helps ensure more accurate and relevant guidance. Include information such as your application language, Amazon EKS cluster name, and absolute paths to your infrastructure and application code.

**Best practice prompts (specific and complete):**

```
"Enable Application Signals for my Python service running on EKS.
My app code is in /home/user/flask-api and IaC is in /home/user/flask-api/terraform"

"I want to add observability to my Node.js application on EKS cluster 'production-cluster'.
The application code is at /Users/dev/checkout-service and
the Kubernetes manifests are at /Users/dev/checkout-service/k8s"

"Help me instrument my Java Spring Boot application on EKS with Application Signals.
Application directory: /opt/apps/payment-api
CDK infrastructure: /opt/apps/payment-api/cdk"
```

**Less effective prompts:**

```
"Enable monitoring for my app"
→ Missing: platform, language, paths

"Enable Application Signals. My code is in ./src and IaC is in ./infrastructure"
→ Problem: Relative paths instead of absolute paths

"Enable Application Signals for my EKS service at /home/user/myapp"
→ Missing: programming language
```

**Quick template:**

```
"Enable Application Signals for my [LANGUAGE] service on EKS.
App code: [ABSOLUTE_PATH_TO_APP]
IaC code: [ABSOLUTE_PATH_TO_IAC]"
```

### Benefits of using the MCP server

Using the CloudWatch Application Signals MCP server offers several advantages:

- **Natural language interface:** Describe what you want to enable without memorizing commands or configuration syntax
- **Context-aware guidance:** The MCP server understands your specific environment and provides tailored recommendations
- **Reduced errors:** Automated configuration generation minimizes manual typing errors
- **Faster setup:** Get from intention to implementation more quickly
- **Learning tool:** See the generated configurations and understand how Application Signals works

For more information about configuring and using the CloudWatch Application Signals MCP server, see the [MCP server documentation](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server").
