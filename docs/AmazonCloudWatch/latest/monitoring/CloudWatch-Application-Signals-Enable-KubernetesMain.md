# Enable your applications on Kubernetes

Enable CloudWatch Application Signals on Kubernetes by using the custom setup steps described in this section.

For applications running on Kubernetes, you install and configure the CloudWatch agent and AWS Distro for OpenTelemetry yourself. On these architectures enabled with a custom Application Signals setup, Application Signals
doesn't autodiscover the names of your services or the hosts or clusters they run on. You must specify these names during the custom setup, and the names that you specify are what is displayed on Application Signals dashboards.

**Requirements**

- You have admininstrator permission on the Kubernetes cluster where you are enabling
  Application Signals.
- You must have the AWS CLI installed on the environment where your Kubernetes cluster is running. For more information about installing the AWS CLI, see
  [Install or update the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- You have kubectl and helm installed on your local terminal. For more information, see
  the [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl "https://kubernetes.io/docs/tasks/tools/#kubectl") and [Helm](https://helm.sh/ "https://helm.sh/") documentation.

## Step 1: Enable Application Signals in your account

You must first enable Application Signals in your account. If you haven't, see [Enable Application Signals in your account](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md").

## Step 2: Install the CloudWatch agent operator in your cluster

Installing the CloudWatch agent operator installs the operator, the CloudWatch agent, and other auto-instrumentation
into your cluster. To do so, enter the following command. Replace `$REGION` with your AWS Region.
Replace `$YOUR_CLUSTER_NAME` with the name that you want to appear for your cluster in Application Signals
dashboards.

```
helm repo add aws-observability https://aws-observability.github.io/helm-charts
helm install amazon-cloudwatch-operator aws-observability/amazon-cloudwatch-observability \
--namespace amazon-cloudwatch --create-namespace \
--set region=`$REGION` \
--set clusterName=`$YOUR_CLUSTER_NAME`
```

For more information, see [amazon-cloudwatch-observability](https://github.com/aws-observability/helm-charts/tree/main/charts/amazon-cloudwatch-observability "https://github.com/aws-observability/helm-charts/tree/main/charts/amazon-cloudwatch-observability") on GitHub.

## Step 3: Set up AWS credentials for your Kubernetes clusters

###### Important

If your Kubernetes cluster is hosted on Amazon EC2, you can skip this section and proceed to
[Step 4: Add annotations](#Application-Signals-Enable-Kubernetes-annotations "#Application-Signals-Enable-Kubernetes-annotations").

If your Kubernetes cluster is hosted on-premises, you must use the instructions in this section
to add AWS credentials to your Kubernetes environment.

###### To set up permissions for an on-premises Kubernetes cluster

1. Create the IAM user to be used to provide permissions to your on-premises host:
   1. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. Choose **Users**, **Create User**.
   3. In **User details**, for **User name**, enter a name for the new IAM user. This is the sign-in name for AWS that will be used to authenticate your host. Then
      choose **Next**
   4. On the **Set permissions** page, under **Permissions options**, select **Attach policies directly**.
   5. From the **Permissions policies** list, select the **CloudWatchAgentServerPolicy** policy to add to your user. Then choose **Next**.
   6. On the **Review and create** page, ensure that you are satisfied with the user name and that the **CloudWatchAgentServerPolicy** policy is in the **Permissions summary**.
   7. Choose **Create user**

2. Create and retrieve your AWS access key and secret key:
   1. In the navigation pane in the IAM console, choose **Users** and then select the user name of the user that you created in the previous step.
   2. On the user's page, choose the **Security credentials** tab. Then, in the **Access keys** section, choose **Create access key**.
   3. For **Create access key Step 1**, choose **Command Line Interface (CLI)**.
   4. For **Create access key Step 2**, optionally enter a tag and then choose **Next**.
   5. For **Create access key Step 3**, select **Download .csv file** to save a .csv file with your IAM user's access key and secret access key. You need this information for the next steps.
   6. Choose **Done**.

3. Configure your AWS credentials in your on-premises host by entering the following command. Replace `ACCESS_KEY_ID` and `SECRET_ACCESS_ID`
   with your newly generated access key and secret access key from the .csv file that you downloaded in the previous step. By default, the credential file is saved in
   `/home/`user`/.aws/credentials.`

```
$ aws configure --profile AmazonCloudWatchAgent
AWS Access Key ID [None]: `ACCESS_KEY_ID`
AWS Secret Access Key [None]: `SECRET_ACCESS_ID`
Default region name [None]: `MY_REGION`
Default output format [None]: json
```

4. Edit the custom resource that the CloudWatch agent installed using the Helm chart to add the
   newly created AWS credentials secret.

```
kubectl edit amazoncloudwatchagent cloudwatch-agent -n amazon-cloudwatch
```

5. While your file editor is open mount the AWS credentials into the CloudWatch agent container by adding the
   following configuration to the top of the deployment. Replace the path `/home/`user`/.aws/credentials` with
   the location of your local AWS credentials file.

```
apiVersion: cloudwatch.aws.amazon.com/v1alpha1
kind: AmazonCloudWatchAgent
metadata:
  name: cloudwatch-agent
  namespace: amazon-cloudwatch
spec:
  volumeMounts:
  - mountPath: /rootfs
    volumeMounts:
    - name: aws-credentials
      mountPath: /root/.aws
      readOnly: true
    volumes:
    - hostPath:
      path: /home/`user`/.aws/credentials
    name: aws-credentials
---
```

## Step 4: Add annotations

###### Note

If you are enabling Application Signals for a Node.js application with ESM, skip the steps in this section and see

[Setting up a Node.js application with the ESM module format](#Kubernetes-NodeJs-ESM "#Kubernetes-NodeJs-ESM") instead.

The next step is to instrument your application for CloudWatch Application Signals by adding a language-specific
[annotation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/ "https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/") to your Kubernetes
[workload](https://kubernetes.io/docs/concepts/workloads/ "https://kubernetes.io/docs/concepts/workloads/")
or [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/"). This annotation auto-instruments your application to send metrics,
traces, and logs to Application Signals.

###### To add the annotations for Application Signals

1.  You have two options for the annotation:

        * **Annotate Workload** auto-instruments a single workload in a cluster.
        * **Annotate Namespace** auto-instruments all workloads deployed in the selected namespace.

    Choose one of those options, and follow the appropriate steps.

2.  To annotate a single workload, enter one of the following commands. Replace
    `$WORKLOAD_TYPE` and
    `$WORKLOAD_NAME` with the values for your workload.
    - For Java workloads:

    ```
    kubectl patch `$WORKLOAD_TYPE` `$WORKLOAD_NAME` -p '{"spec": {"template": {"metadata": {"annotations": {"instrumentation.opentelemetry.io/inject-java": "true"}}}}}'
    ```

    - For Python workloads:

    ```
    kubectl patch `$WORKLOAD_TYPE` `$WORKLOAD_NAME` -p '{"spec": {"template": {"metadata": {"annotations": {"instrumentation.opentelemetry.io/inject-python": "true"}}}}}'
    ```

    For Python applications, there are additional required configurations. For more information, see [Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").
    - For .NET workloads:

    ```
    kubectl patch `$WORKLOAD_TYPE` `$WORKLOAD_NAME` -p '{"spec": {"template": {"metadata": {"annotations": {"instrumentation.opentelemetry.io/inject-dotnet": "true"}}}}}'
    ```

    ###### Note

    To enable Application Signals for a .NET workload on Alpine Linux
    (`linux-musl-x64`) based images, add the following additional
    annotation.

    ```
    instrumentation.opentelemetry.io/otel-dotnet-auto-runtime: "linux-musl-x64"
    ```

    - For Node.js workloads:

    ```
    kubectl patch `$WORKLOAD_TYPE` `$WORKLOAD_NAME` -p '{"spec": {"template": {"metadata": {"annotations": {"instrumentation.opentelemetry.io/inject-nodejs": "true"}}}}}'
    ```

3.  To annotate all workloads in a namespace, enter enter one of the following commands. Replace `$NAMESPACE`
    with the name of your namespace.

If the namespace includes Java, Python, and .NET workloads, add all
annotations to the namespace.

    * For Java workloads in the namespace:



    ```
    kubectl annotate ns `$NAMESPACE` instrumentation.opentelemetry.io/inject-java=true
    ```
    * For Python workloads in the namespace:



    ```
    kubectl annotate ns `$NAMESPACE` instrumentation.opentelemetry.io/inject-python=true
    ```

    For Python applications, there are additional required configurations. For more information, see [Python application doesn't start after Application Signals is enabled](CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python "CloudWatch-Application-Signals-Enable-Troubleshoot.md#Application-Signals-troubleshoot-starting-Python").
    * For .NET workloads in the namespace:



    ```
    kubectl annotate ns `$NAMESPACE` instrumentation.opentelemetry.io/inject-dotnet=true
    ```
    * For Node.js workloads in the namespace:



    ```
    kubectl annotate ns `$NAMESPACE` instrumentation.opentelemetry.io/inject-nodejs=true
    ```

After adding the annotations, restart all pods in the namespace by entering the following command:

```
kubectl rollout restart
```

4. When the previous steps are completed, in the CloudWatch console, choose **Application Signals**,
   **Services**. This opens the dashboards where you can see the data that Application Signals collects. It might take a few
   minutes for data to appear.

For more information about the **Services** view, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md").

### Setting up a Node.js application with the ESM module format

We provide limited support for Node.js applications with the ESM module format. For
details, see [Known limitations about Node.js with ESM](CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations "CloudWatch-Application-Signals-supportmatrix.md#ESM-limitations").

For the ESM module format, enabling Application Signals by annotating the manifest file doesn’t work. Skip the previous
procedure and do the following instead:

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
ENV OTEL_SERVICE_NAME='YOUR_SERVICE_NAME' #replace with a proper service name
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
        image:`your-nodejs-application-image` #replace it with a proper image uri
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

4. Deploy the Node.js application to the Kubernetes cluster.

## (Optional) Step 5: Monitor your application health

Once you have enabled your applications on Kubernetes, you can monitor your application health. For more information, see [Monitor the operational health of your applications with Application Signals](Services.md "Services.md").
