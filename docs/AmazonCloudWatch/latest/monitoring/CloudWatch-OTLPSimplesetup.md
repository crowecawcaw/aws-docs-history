# OpenTelemetry Collector Contrib

You can use the OpenTelemetry Collector Contrib to get started with OpenTelemetry in CloudWatch.


## Prerequisite


Make sure *Transaction Search* is enabled in CloudWatch. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md "CloudWatch-Transaction-Search.md").


## Download the OpenTelemetry Collector Contrib


Download the latest release of the  [OpenTelemetry Collector Contrib distribution](https://github.com/open-telemetry/opentelemetry-collector-releases/releases "https://github.com/open-telemetry/opentelemetry-collector-releases/releases").


## Install the OpenTelemetry Collector Contrib


Install the OpenTelemetry Collector Contrib on any operating system and platform. For more information, see [Install the Collector](https://opentelemetry.io/docs/collector/installation/ "https://opentelemetry.io/docs/collector/installation/").


## Setup AWS credentials on your Amazon EC2 or on-premise hosts


You can setup AWS credentials on your Amazon EC2 or on-premise hosts.



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
8. On the **Review and create** page, ensure that you are satisfied with the user name and that the **CloudWatchAgentServerPolicy** policy is under the **Permissions summary**.
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



## Setup AWS credentials for your Amazon EKS or Kubernetes clusters


To setup AWS credentials for your Amazon EKS or Kubernetes clusters to send telemetry to CloudWatch, follow the below procedure.



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



## Configure the OpenTelemetry Collector


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

Configure your OpenTelemetry SDKs to *always\_on* sampling configuration to reliably record 100% spans and get full visibility into your critical applications with CloudWatch Application Signals. For more information, see an [OpenTelemetry Java SDK sampler configuration](https://opentelemetry.io/docs/languages/java/sdk/#sampler "https://opentelemetry.io/docs/languages/java/sdk/#sampler") example.
 For an example on setting up OpenTelemetry Collector with X-Ray OTLP endpoint, see the [application signals demo](https://github.com/aws-observability/application-signals-demo/blob/main/scripts/opentelemetry/otel_simple_setup/opentelemetry.yaml "https://github.com/aws-observability/application-signals-demo/blob/main/scripts/opentelemetry/otel_simple_setup/opentelemetry.yaml") repository.
