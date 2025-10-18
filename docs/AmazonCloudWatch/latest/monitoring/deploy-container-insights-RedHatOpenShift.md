# Setting up Container Insights on
 RedHat OpenShift on AWS (ROSA)

CloudWatch Container Insights with enhanced observability supports RedHat OpenShift on AWS
 (ROSA). This version supports enhanced observability for ROSA clusters. After you install
 the CloudWatch agent operator Helm chart, Container Insights auto-collects detailed infrastructure
 telemetry from the cluster level down to the container level in your environment. It then
 displays this performance data in curated dashboards removing the heavy lifting in
 observability setup. 

###### Note

For RedHat for OpenShift on AWS (ROSA), when you install the CloudWatch agent operator
 using helm charts, the CloudWatch agent is by default also enabled to receive both metrics and
 traces from your applications that are instrumented for Application Signals. If you would
 like to optionally pass in custom configuration rules, you can do so by passing in a
 custom agent configuration by using the Helm chart, as outlined in (Optional) [Additional
 configuration], as outlined in [(Optional)
 Additional configuration](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration "install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration").

###### To install Container Insights with enhanced observability on a RedHat OpenShift on
 AWS (ROSA) cluster

1. If necessary, install Helm. For more information, see [Quickstart Guide](https://helm.sh/docs/intro/quickstart/ "https://helm.sh/docs/intro/quickstart/") in the Helm
 documentation.
2. Install the CloudWatch agent operator by entering the following commands. Replace
 `my-cluster-name` with the name of your cluster, and replace
 `my-cluster-region` with the Region that the cluster runs
 in.



```
helm repo add aws-observability https://aws-observability.github.io/helm-charts
helm repo update aws-observability
helm install --wait --create-namespace \
    --namespace amazon-cloudwatch amazon-cloudwatch-observability \
    aws-observability/amazon-cloudwatch-observability \
    --set clusterName=`my-cluster-name` \
    --set region=`my-cluster-region` \
    --set k8sMode=ROSA
```
3. Set up authorization for the agent operator by following the steps in Option 1,
 Option 2, or Option 3 in [Install the CloudWatch agent with the
 Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md").
