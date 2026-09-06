

# Troubleshooting
<a name="jobruns-flink-troubleshoot"></a>

This section describes how to troubleshoot problems with Amazon EMR on EKS. For information on how to troubleshoot general problems with Amazon EMR, see [Troubleshoot a cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot.html) in the *Amazon EMR Management Guide*.
+ [Troubleshooting jobs that use PersistentVolumeClaims (PVC)](permissions-for-pvc.md)
+ [Troubleshooting Amazon EMR on EKS vertical autoscaling](troubleshooting-vas.md)
+ [Troubleshooting Amazon EMR on EKS Spark operator](troubleshooting-sparkop.md)

## Troubleshooting Apache Flink on Amazon EMR on EKS
<a name="jobruns-flink-troubleshooting-apache-flink"></a>

### Resource mapping not found when installing the Helm chart
<a name="w2aac21c21b7b7b3"></a>

You might encounter the following error message when you install the Helm chart.

```
Error: INSTALLATION FAILED: pulling from host 1234567890.dkr.ecr.us-west-2.amazonaws.com failed with status code [manifests 6.13.0]: 403 Forbidden Error: INSTALLATION FAILED: unable to build kubernetes objects from release manifest: [resource mapping not found for name: "flink-operator-serving-cert" namespace: "<the namespace to install your operator>" from "": no matches for kind "Certificate" in version "cert-manager.io/v1"

ensure CRDs are installed first, resource mapping not found for name: "flink-operator-selfsigned-issuer" namespace: "<the namespace to install your operator>" " from "": no matches for kind "Issuer" in version "cert-manager.io/v1"

ensure CRDs are installed first].
```

To resolve this error, install cert-manager to enable adding the webhook component. You must install cert-manager to each Amazon EKS cluster that you use.

```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0
```

### AWS service access denied error
<a name="jobruns-flink-troubleshooting-access-denied"></a>

If you see an *access denied* error, confirm that the IAM role for `operatorExecutionRoleArn` in the Helm chart `values.yaml` file has the correct permissions. Also ensure the IAM role under `executionRoleArn` in your `FlinkDeployment` specification has the correct permissions.

### `FlinkDeployment` is stuck
<a name="jobruns-flink-troubleshooting-stuck"></a>

If your `FlinkDeployment` stalls in an arrested state, use the following steps to force delete the deployment:

1. Edit the deployment run.

   ```
   kubectl edit -n {{Flink Namespace}} flinkdeployments/{{App Name}}
   ```

1. Remove this finalizer.

   ```
   finalizers:
     - flinkdeployments.flink.apache.org/finalizer
   ```

1. Delete the deployment.

   ```
   kubectl delete -n {{Flink Namespace}} flinkdeployments/{{App Name}}
   ```

### s3a AWSBadRequestException issue when running a Flink application in an opt-in AWS Region
<a name="jobruns-flink-troubleshooting-optin-region"></a>

If you run a Flink application in an [opt-in AWS Region](https://docs.aws.amazon.com/controltower/latest/userguide/opt-in-region-considerations.html), you might see the following errors:

```
Caused by: org.apache.hadoop.fs.s3a.AWSBadRequestException: getFileStatus on 
s3://flink.txt: com.amazonaws.services.s3.model.AmazonS3Exception: Bad Request 
(Service: Amazon S3; Status Code: 400; Error Code: 400 Bad Request; Request ID: ABCDEFGHIJKL; S3 Extended Request ID:
ABCDEFGHIJKLMNOP=; Proxy: null), S3 Extended Request ID: ABCDEFGHIJKLMNOP=:400 Bad Request: Bad Request 
(Service: Amazon S3; Status Code: 400; Error Code: 400 Bad Request; Request ID: ABCDEFGHIJKL; S3 Extended Request ID: ABCDEFGHIJKLMNOP=; Proxy: null)
```

```
Caused by: org.apache.hadoop.fs.s3a.AWSBadRequestException: getS3Region on flink-application: software.amazon.awssdk.services.s3.model.S3Exception: null 
(Service: S3, Status Code: 400, Request ID: ABCDEFGHIJKLMNOP, Extended Request ID: ABCDEFGHIJKLMNOPQRST==):null: null 
(Service: S3, Status Code: 400, Request ID: ABCDEFGHIJKLMNOP, Extended Request ID: AHl42uDNaTUFOus/5IIVNvSakBcMjMCH7dd37ky0vE6jhABCDEFGHIJKLMNOPQRST==)
```

To fix these errors, use the following configuration in your `FlinkDeployment` definition file.

```
spec:
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
    fs.s3a.endpoint.region: {{OPT_IN_AWS_REGION_NAME}}
```

We also recommend that you use the SDKv2 credentials provider:

```
fs.s3a.aws.credentials.provider: software.amazon.awssdk.auth.credentials.WebIdentityTokenFileCredentialsProvider
```

If you want to use the SDKv1 credentials provider, make sure that your SDK supports your opt-in Region. For more information, see the [aws-sdk-java GitHub repository](https://github.com/aws/aws-sdk-java).

If you get `S3 AWSBadRequestException` when you run Flink SQL statements in an opt-in Region, make sure that you set the configuration `fs.s3a.endpoint.region: {{OPT_IN_AWS_REGION_NAME}}` in your flink configuration spec.

### S3A AWSBadRequestException when running a Flink session job in CN regions
<a name="jobruns-flink-troubleshooting-optin-region"></a>

For Amazon EMR releases 6.15.0 - 7.2.0, you might encounter the following error messages when you run a Flink session job in CN regions. These include China (Beijing) and China (Ningxia):

```
Error:  {"type":"org.apache.flink.kubernetes.operator.exception.ReconciliationException","message":"org.apache.hadoop.fs.s3a.AWSBadRequestException: 
                    getFileStatus on s3://ABCDPath: software.amazon.awssdk.services.s3.model.S3Exception: null (Service: S3, Status Code: 400, Request ID: ABCDEFGH, Extended Request ID: 
                    ABCDEFGH:null: null (Service: S3, Status Code: 400, Request ID: ABCDEFGH, Extended Request ID: ABCDEFGH","additionalMetadata":{},"throwableList":
                    [{"type":"org.apache.hadoop.fs.s3a.AWSBadRequestException","message":"getFileStatus on s3://ABCDPath: software.amazon.awssdk.services.s3.model.S3Exception: 
                    null (Service: S3, Status Code: 400, Request ID: ABCDEFGH, Extended Request ID: ABCDEFGH:null: null (Service: S3, Status Code: 400, Request ID: ABCDEFGH, 
                    Extended Request ID: ABCDEFGH","additionalMetadata":{}},{"type":"software.amazon.awssdk.services.s3.model.S3Exception","message":"null (Service: S3, Status Code: 400, 
                    Request ID: ABCDEFGH, Extended Request ID: ABCDEFGH","additionalMetadata":{}}]}
```

There is an awareness of this issue. The team is working on patching the flink operators for all of these release versions. However, before we finish the patch, to fix this error, you need to download the flink operator helm chart, untar it (extract the compressed file) and make configuration changes in the helm chart.

The specific steps are the following:

1. Change to, specifically change directories to, your local folder for the helm chart, and run the following command line to pull the helm chart and untar (extract) it.

   ```
   helm pull oci://public.ecr.aws/emr-on-eks/flink-kubernetes-operator \
   --version $VERSION \
   --namespace $NAMESPACE
   ```

   ```
   tar -zxvf flink-kubernetes-operator-$VERSION.tgz
   ```

1. Go into the helm chart folder and find the `templates/flink-operator.yaml` file.

1. Find the `flink-operator-config` ConfigMap and add the following `fs.s3a.endpoint.region` configuration in the `flink-conf.yaml`. For example:

   ```
   {{- if .Values.defaultConfiguration.create }}
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: flink-operator-config
     namespace: {{ .Release.Namespace }}
     labels:
       {{- include "flink-operator.labels" . | nindent 4 }}
   data:
     flink-conf.yaml: |+
   fs.s3a.endpoint.region: {{ .Values.emrContainers.awsRegion }}
   ```

1. Install the local helm chart and run your job.