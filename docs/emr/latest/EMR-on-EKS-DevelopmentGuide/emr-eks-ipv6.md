

# Running EMR on EKS on IPv6 clusters
<a name="emr-eks-ipv6"></a>

You can run Amazon EMR on EKS workloads on IPv6 Amazon EKS clusters to take advantage of a significantly larger address space and avoid IPv4 address exhaustion as your Kubernetes environments scale.

For information about creating an IPv6 Amazon EKS cluster, see [IPv6 addresses for clusters, Pods, and services](https://docs.aws.amazon.com/eks/latest/userguide/cni-ipv6.html) in the *Amazon EKS User Guide*.

## Supported submission models
<a name="emr-eks-ipv6-supported-models"></a>

The following submission models are supported on IPv6 Amazon EKS clusters:
+ `StartJobRun`
+ Spark Connect Interactive Endpoints
+ Amazon SageMaker Unified Studio
+ Spark Operator
+ Flink Operator
+ Livy Operator

**Unsupported submission models**  
Jupyter Enterprise Gateway (JEG) endpoints are not supported on IPv6 clusters.

## Submission models that require no additional configuration
<a name="emr-eks-ipv6-no-config"></a>

For the following submission models, you can set up and submit Amazon EMR workloads on an IPv6 cluster the same way you do for IPv4. No additional configuration is required:
+ `StartJobRun`
+ Spark Connect Interactive Endpoints
+ Amazon SageMaker Unified Studio

## Operator-based submission models
<a name="emr-eks-ipv6-operator-config"></a>

Operator-based submission models require additional configuration for IPv6 compatibility. The following sections describe the required configuration for each operator.

### Spark Operator
<a name="emr-eks-ipv6-spark-operator"></a>

To run Spark Operator workloads on an IPv6 cluster, add the following Spark configuration to your `SparkApplication` spec. This configuration is required for all supported releases.

```
spec:
  sparkConf:
    "spark.kubernetes.driver.service.ipFamilies": "IPv6"
```

This configuration tells the Kubernetes client to create the Spark driver service with the IPv6 IP family. Without it, the driver service defaults to IPv4, which is not supported on an IPv6-only cluster.

Additionally, for `emr-7.x` releases, you must apply the following workaround by setting this environment variable on the Spark Operator deployment:

```
KUBERNETES_DISABLE_HOSTNAME_VERIFICATION=true
```

After installing the Spark operator, run the following command to set the environment variable:

```
kubectl set env deployment/{{spark-operator-deployment-name}} \
  KUBERNETES_DISABLE_HOSTNAME_VERIFICATION=true \
  -n {{spark-operator-namespace}}
```

This workaround addresses a [known issue with IPv6 hostname verification](https://github.com/square/okhttp/issues/5885) on GitHub. The `emr-7.x` releases use a version of the fabric8 Kubernetes client that depends on OkHttp 3.x, which fails TLS hostname verification when connecting to the Kubernetes API server over IPv6.

### Flink Operator
<a name="emr-eks-ipv6-flink-operator"></a>

To run Flink Operator workloads on an IPv6 cluster, you must set the following environment variable on both the Flink Operator pod and your `FlinkDeployment` job pods:

```
KUBERNETES_DISABLE_HOSTNAME_VERIFICATION=true
```

This workaround addresses the same OkHttp 3.x IPv6 hostname verification issue described in the Spark Operator section. For more information, see [IPv6 configuration](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/deployment/configuration/#ipv6-configuration) in the Apache Flink Kubernetes Operator documentation.

#### Set the environment variable on the Flink Operator pod
<a name="emr-eks-ipv6-flink-operator-pod"></a>

Set the environment variable during `helm install`:

```
helm install {{my-flink-operator}} {{chart}} \
  --set operatorPod.env[0].name=KUBERNETES_DISABLE_HOSTNAME_VERIFICATION \
  --set-string operatorPod.env[0].value=true
```

#### Set the environment variable on your FlinkDeployment job pods
<a name="emr-eks-ipv6-flink-job-pods"></a>

Inject the environment variable through a pod template in your `FlinkDeployment` YAML:

```
spec:
  podTemplate:
    spec:
      containers:
        - name: flink-main-container
          env:
            - name: KUBERNETES_DISABLE_HOSTNAME_VERIFICATION
              value: "true"
```

### Livy Operator
<a name="emr-eks-ipv6-livy-operator"></a>

To run Livy Operator workloads on an IPv6 cluster, you must configure two things:

1. **Dualstack load balancer annotation** — Add the following annotation when installing the Livy helm chart so that the AWS Load Balancer Controller provisions a dualstack Network Load Balancer:

   ```
   helm install {{my-livy}} {{chart}} \
     --set "service.annotations.service\.beta\.kubernetes\.io/aws-load-balancer-ip-address-type=dualstack"
   ```

1. **Spark driver service IPv6 configuration** — Include the `spark.kubernetes.driver.service.ipFamilies` configuration when you submit Spark jobs through Livy:

   ```
   {
     "conf": {
       "spark.kubernetes.driver.service.ipFamilies": "IPv6"
     }
   }
   ```

## Supported releases
<a name="emr-eks-ipv6-releases"></a>

The following table shows IPv6 support by submission model and Amazon EMR release. The `emr-spark-8.x` releases are Spark-only releases and do not include Flink.


| Submission model | `emr-7.14.0` and later 7.x releases | `emr-spark-8.0.0` | `emr-spark-8.1.0`\+ | 
| --- | --- | --- | --- | 
| StartJobRun | ✅ Supported | ✅ Supported | ✅ Supported | 
| Spark Connect Interactive Endpoints | ✅ Supported | ✅ Supported | ✅ Supported | 
| Amazon SageMaker Unified Studio | ✅ Supported | ✅ Supported | ✅ Supported | 
| Spark Operator | ✅ Supported1,​2 | ❌ Not supported | ✅ Supported2 | 
| Flink Operator | ✅ Supported1 | N/A | N/A | 
| Livy Operator | ✅ Supported2 | ✅ Supported2 | ✅ Supported2 | 

1 Requires the `KUBERNETES_DISABLE_HOSTNAME_VERIFICATION` workaround described in the preceding section for this submission model.

2 Requires additional configuration described in the preceding section for this submission model.

## Troubleshooting
<a name="emr-eks-ipv6-troubleshooting"></a>

The following are common errors you might encounter when running Amazon EMR on EKS workloads on IPv6 clusters.

### Error: Expected hostname or IPv6 IP enclosed in []
<a name="emr-eks-ipv6-troubleshoot-unsupported"></a>

```
java.lang.AssertionError: assertion failed: Expected hostname or
IPv6 IP enclosed in [] but got 2600:1f14:31b1:d102:d812::2
```

**Cause:** You are using an Amazon EMR release that does not support IPv6. Releases earlier than `emr-7.14.0` do not include the necessary IPv6 fixes.

**Solution:** Upgrade to `emr-7.14.0` or later. See [Supported releases](#emr-eks-ipv6-releases) for the full list of supported releases.

### Error: SSLPeerUnverifiedException hostname not verified
<a name="emr-eks-ipv6-troubleshoot-okhttp"></a>

```
javax.net.ssl.SSLPeerUnverifiedException: Hostname fd0f:f96c:1438::1
not verified
```

**Cause:** The Spark or Flink Operator pod does not have the `KUBERNETES_DISABLE_HOSTNAME_VERIFICATION=true` environment variable set. OkHttp 3.x fails TLS hostname verification when the Kubernetes API server uses an IPv6 address.

**Solution:** Set `KUBERNETES_DISABLE_HOSTNAME_VERIFICATION=true` on the operator pod. See [Spark Operator](#emr-eks-ipv6-spark-operator) or [Flink Operator](#emr-eks-ipv6-flink-operator).

### Error: Invalid value "IPv4" not configured on this cluster
<a name="emr-eks-ipv6-troubleshoot-ipfamilies"></a>

```
Service "...-driver-svc" is invalid: spec.ipFamilies[0]: Invalid
value: "IPv4": not configured on this cluster
```

**Cause:** The Spark application does not include the `spark.kubernetes.driver.service.ipFamilies=IPv6` configuration. Without this setting, Spark attempts to create the driver service with IPv4, which an IPv6-only cluster rejects.

**Solution:** Add `"spark.kubernetes.driver.service.ipFamilies": "IPv6"` to your `sparkConf` (for Spark Operator) or to the `conf` object in your Livy batch submission. See [Spark Operator](#emr-eks-ipv6-spark-operator) or [Livy Operator](#emr-eks-ipv6-livy-operator).