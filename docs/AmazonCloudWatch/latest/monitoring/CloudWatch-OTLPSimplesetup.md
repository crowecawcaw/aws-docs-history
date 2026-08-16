# OpenTelemetry Collector

The OpenTelemetry Collector is an open source, vendor-agnostic agent that receives,
processes, and exports telemetry data. It acts as a central pipeline between your
applications and Amazon CloudWatch, collecting metrics, logs, and traces from multiple sources
and sending them to CloudWatch using the OpenTelemetry Protocol (OTLP).

Using the OpenTelemetry Collector with CloudWatch provides the following benefits:

- Collect telemetry from multiple applications and hosts through a single agent,
  reducing the number of connections to CloudWatch.
- Process and filter telemetry before sending it to CloudWatch, including adding or
  removing attributes, batching data, and sampling traces.
- Use the same collector configuration across AWS, on-premises, and other cloud
  environments, providing a consistent telemetry pipeline regardless of where your
  applications run.
- Send metrics to CloudWatch with rich labels that are available to query using the
  Prometheus Query Language (PromQL) in CloudWatch Query Studio.

## Supported receivers

The OpenTelemetry Collector supports a wide range of receivers for ingesting
telemetry data. You can use OpenTelemetry receivers such as the OTLP receiver for
applications instrumented with OpenTelemetry SDKs, or Prometheus receivers to scrape
metrics from existing Prometheus exporters. Common Prometheus receivers used with
CloudWatch include:

- Prometheus receiver, for scraping any Prometheus-compatible endpoint
- Host Metrics receiver, for collecting system-level metrics from the host
- Kubernetes Cluster receiver, for collecting cluster-level metrics from the
  Kubernetes API server

You can configure multiple receivers in a single collector, allowing you to collect
both OpenTelemetry and Prometheus metrics and send them to CloudWatch through the same
pipeline. For the full list of available receivers, see the OpenTelemetry Collector
[repository](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver "https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver").

## Getting started

Prerequisite – If using the OTLP endpoint for tracing, make sure that
Transaction Search is enabled.

Steps:

1. Download the latest release of the OpenTelemetry Collector distribution.
   For more information, see the OpenTelemetry Collector
   [releases](https://github.com/open-telemetry/opentelemetry-collector-releases/releases "https://github.com/open-telemetry/opentelemetry-collector-releases/releases").
2. Install the OpenTelemetry Collector on your host. The collector runs on any
   operating system and platform. For more information, see
   [Install the Collector](https://opentelemetry.io/docs/collector/installation/ "https://opentelemetry.io/docs/collector/installation/").
3. Configure AWS credentials on your Amazon EC2 or on-premises host. The
   collector uses these credentials to authenticate with CloudWatch when sending
   telemetry data. See below for details.

Setup IAM permissions for Amazon EC2

###### Follow the below procedure to attach the `CloudWatchAgentServerPolicy` IAM policy to the IAM role of your Amazon EC2 instance.

    1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. Choose **Roles** and find and select the role used by your Amazon EC2 instance.
    3. Under the **Permissions** tab, choose **Add permissions**, **Attach policies**.
    4. Using the search box, search for `CloudWatchAgentServerPolicy` policy.
    5. Select the **CloudWatchAgentServerPolicy** policy and choose **Add permissions**.

Setup IAM permissions for on-premise hosts

###### You can create an IAM user that can be used to provide permissions to your on-premise hosts.

    1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. Choose **Users**, **Create User**.
    3. Under **User details**,for **User name**, enter a name for the new IAM user. This is the sign-in name for AWS that will be used to authenticate your host.
    4. Choose **Next**.
    5. On the **Set permissions** page, under **Permissions options**, select **Attach policies directly**.
    6. From the **Permissions policies** list, select the **CloudWatchAgentServerPolicy** policy to add to your user.
    7. Choose **Next**.
    8. On the **Review and create** page, make sure that you are satisfied with the user name and that the **CloudWatchAgentServerPolicy** policy is under the **Permissions summary**.
    9. Choose **Create user**.
    10. **Create and retrieve your AWS access key and secret key** – In the navigation pane in the IAM console, choose **Users** and then select the user name of the user that you created in the previous step.
    11. On the user's page, choose the **Security credentials** tab.
    12. Under the **Access keys** section, choose **Create access key**.
    13. For **Create access key Step 1**, choose **Command Line Interface (CLI)**.
    14. For **Create access key Step 2**, optionally enter a tag and then choose **Next**.
    15. For **Create access key Step 3,** select **Download .csv file** to save a .csv file with your IAM user's access key and secret access key. You need this information for the next steps.
    16. Choose **Done**.
    17. Configure your AWS credentials in your on-premises host by entering the following command. Replace *ACCESS\_KEY\_ID*  and *SECRET\_ACCESS\_ID*  with your newly generated access key and secret access key from the .csv file that you downloaded in the previous step.



    ```

    $ aws configure
    AWS Access Key ID [None]: `ACCESS_KEY_ID`
    AWS Secret Access Key [None]: `SECRET_ACCESS_ID`
    Default region name [None]: MY_REGION
    Default output format [None]: json

    ```

###### Tip

For on-premises hosts that only need to send metrics or logs, you can use
bearer token authentication as a simpler alternative to configuring AWS
access keys. Bearer tokens don't require the `aws configure`
step or credential files on the host. For more information, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md"). 4. Setup AWS credentials for your Amazon EKS or Kubernetes clusters.
The easiest way to get started with Amazon EKS is to use the EKS OTel Container
Insights add-on. If you prefer to use the OpenTelemetry Collector directly, follow
the procedure below to set up AWS credentials for your Amazon EKS or Kubernetes
clusters to send telemetry to CloudWatch.

Setup IAM permissions for Amazon EKS

    1. Create an IAM OIDC identity provider for your cluster using the following command.





    ```
    eksctl utils associate-iam-oidc-provider --cluster ${`CLUSTER_NAME}` --region ${`REGION`} --approve
    ```
    2. Assign IAM roles to Kubernetes service account for OTel Collector using the following command.



    ```

    eksctl create iamserviceaccount \
    --name ${`COLLECTOR_SERVICE_ACCOUNT`}\
    --namespace ${`NAMESPACE`} \
    --cluster ${`CLUSTER_NAME`} \
    --region ${REGION} \
    --attach-policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy \
    --approve \
    --override-existing-serviceaccounts

    ```

Setup IAM permissions for Kubernetes

    1. Configure your AWS credentials in your on-premises host by entering the following command. Replace `ACCESS_KEY_ID` and `SECRET_ACCESS_ID` with your newly generated access key and secret access key from the .csv file that you downloaded in
     the previous step. By default, the credential file is saved under */home/user/.aws/credentials.*.



    ```

    aws configure
    AWS Access Key ID [None]: `ACCESS_KEY_ID`
    AWS Secret Access Key [None]: `SECRET_ACCESS_ID`
    Default region name [None]: `MY_REGION`
    Default output format [None]: json

    ```
    2. Edit OpenTelemetry Collector resource to add the newly created AWS credentials secret by using the command:
     `kubectl edit OpenTelemetryCollector `otel_collector``
    3. Using the file editor, add the AWS credentials into the OpenTelemetryCollector container by adding the following configuration to the top of the deployment. Replace the path `/home/user/.aws/credentials` with the location of your local AWS credentials file.




    ```

                         spec:
                        volumeMounts:
                        - mountPath: /rootfs
                        volumeMounts:
                        - name: aws-credentials
                        mountPath: /root/.aws
                        readOnly: true
                        volumes:
                        - hostPath:
                        path: /home/user/.aws/credentials
                        name: aws-credentials

    ```

5. Configure the OTLP exporter in your collector configuration to send
telemetry to the CloudWatch endpoint. See examples below.

## Authenticate with a bearer token (API key)

If you don't need to configure AWS credentials on the host – for
example, when running on non-AWS infrastructure, other cloud providers, or
CI/CD pipelines – you can use bearer token authentication instead of
SigV4. Bearer tokens are supported for the metrics and logs endpoints (separate
API keys are required for each service). Bearer token authentication is not
supported for traces.

For setup instructions, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md"). For logs, see [Setting up bearer token authentication for Logs](../logs/CWL_HTTP_Endpoints_BearerTokenAuth.md "../logs/CWL_HTTP_Endpoints_BearerTokenAuth.md").

For a collector configuration example using bearer tokens, see the bearer token
metrics example in the collector configuration examples below.

## Collector configuration examples

Copy and paste the content below to configure your collector to send logs and traces to the OTLP endpoints.

```
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  otlphttp/logs:
    compression: gzip
    logs_endpoint: `logs_otlp_endpoint`
    headers:
      x-aws-log-group: ency_log_group
      x-aws-log-stream: default
    auth:
      authenticator: sigv4auth/logs

  otlphttp/traces:
    compression: gzip
    traces_endpoint: `traces_otlp_endpoint`
    auth:
      authenticator: sigv4auth/traces

extensions:
  sigv4auth/logs:
    region: "`region`"
    service: "logs"
  sigv4auth/traces:
    region: "`region`"
    service: "xray"

service:
  telemetry:
  extensions: [sigv4auth/logs, sigv4auth/traces]
  pipelines:
    logs:
      receivers: [**otlp**]
      exporters: [**otlphttp**/**logs**]
    traces:
      receivers: [**otlp**]
      exporters: [**otlphttp**/**traces**]


```

The following is an example to send logs and traces using sigv4 to us-east-1.

```
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  otlphttp/logs:
    compression: gzip
    logs_endpoint: https://logs.us-east-1.amazonaws.com/v1/logs
    headers:
      x-aws-log-group: MyApplicationLogs
      x-aws-log-stream: default
    auth:
      authenticator: sigv4auth/logs

  otlphttp/traces:
    compression: gzip
    traces_endpoint: https://xray.us-east-1.amazonaws.com/v1/traces
    auth:
      authenticator: sigv4auth/traces

extensions:
  sigv4auth/logs:
    region: "**us-east-1**"
    service: "**logs**"
  sigv4auth/traces:
    region: "**us-east-1**"
    service: "**xray**"

service:
  telemetry:
  extensions: [sigv4auth/logs, sigv4auth/traces]
  pipelines:
    logs:
     receivers: [**otlp**]
      exporters: [**otlphttp**/**logs**]
    traces:
      receivers: [**otlp**]
      exporters: [**otlphttp**/**traces**]



```

###### Note

Configure your OpenTelemetry SDKs to _always\_on_ sampling configuration to reliably record 100% spans and get full visibility into your critical applications with CloudWatch Application Signals. For more information, see an [OpenTelemetry Java SDK sampler configuration](https://opentelemetry.io/docs/languages/java/sdk/#sampler "https://opentelemetry.io/docs/languages/java/sdk/#sampler") example.
For an example on setting up OpenTelemetry Collector with X-Ray OTLP endpoint, see the [application signals demo](https://github.com/aws-observability/application-signals-demo/blob/main/scripts/opentelemetry/otel_simple_setup/opentelemetry.yaml "https://github.com/aws-observability/application-signals-demo/blob/main/scripts/opentelemetry/otel_simple_setup/opentelemetry.yaml") repository.

Copy and paste the content below to configure your collector to send metrics to the OTLP endpoints.

```
receivers:
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:
  batch:
    send_batch_size: 200
    timeout: 10s

exporters:
  otlphttp:
    tls:
      insecure: false
    endpoint: `metrics_otlp_endpoint`
    auth:
      authenticator: sigv4auth

extensions:
  sigv4auth:
    service: "monitoring"
    region: "`region`"

service:
  extensions: [sigv4auth]
  pipelines:
    metrics:
      receivers: [**otlp**]
      processors: [**batch**]
      exporters: [**otlphttp**]

```

The following is an example to send metrics using sigv4 to us-east-1.

```
receivers:
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:
  batch:
    send_batch_size: 200
    timeout: 10s

exporters:
  otlphttp:
    tls:
      insecure: false
    endpoint: "https://monitoring.us-east-1.amazonaws.com/v1/metrics:443"
    auth:
      authenticator: sigv4auth

extensions:
  sigv4auth:
    service: "**monitoring**"
    region: "**us-east-1**"

service:
  extensions: [sigv4auth]
  pipelines:
    metrics:
      receivers: [**otlp**]
      processors: [**batch**]
      exporters: [**otlphttp**]

```

**Metrics with bearer token authentication**

The following is an example to send metrics using a bearer token to us-east-1.
For setup instructions and security best practices, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md").

```
extensions:
  bearertokenauth:
    filename: "/etc/otel/cw-api-key"

receivers:
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:
  batch:
    send_batch_size: 200
    timeout: 10s

exporters:
  otlphttp:
    tls:
      insecure: false
    endpoint: "https://monitoring.us-east-1.amazonaws.com/v1/metrics"
    auth:
      authenticator: bearertokenauth

service:
  extensions: [bearertokenauth]
  pipelines:
    metrics:
      receivers: [**otlp**]
      processors: [**batch**]
      exporters: [**otlphttp**]

```

###### Important

Never hardcode API keys directly in collector configuration files. Use
`filename` to read from a mounted secret, or `${env:VAR}`
to read from an environment variable injected by your secrets manager.

###### Note

Unlike SigV4, bearer tokens don't require AWS credentials files, IAM
roles, or IRSA configuration. The collector can run on any platform without
AWS SDK dependencies.
