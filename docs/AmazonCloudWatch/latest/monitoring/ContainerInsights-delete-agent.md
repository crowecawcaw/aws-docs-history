# Deleting the CloudWatch agent and Fluent Bit

for Container Insights

If you installed Container Insights by using installing the CloudWatch Observability
add-on for Amazon EKS, you can delete Container Insights and the CloudWatch agent by entering the
following command:

###### Note

The Amazon EKS add-on now supports Container Insights on Windows worker nodes. If you
delete the Amazon EKS add-on, Container Insights for Windows is also deleted.

```
aws eks delete-addon —cluster-name my-cluster —addon-name amazon-cloudwatch-observability
```

Otherwise, to delete all resources related to the CloudWatch agent and Fluent Bit, enter
the following command. In this command, `My_Cluster_Name` is
the name of your Amazon EKS or Kubernetes cluster, and `My_Region`
is the name of the Region where the logs are published.

```
ClusterName=`My_Cluster_Name`
RegionName=`My-Region`
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-operator-rendered.yaml | sed 's/{{cluster_name}}/'${ClusterName}'/g;s/{{region_name}}/'${RegionName}'/g' | kubectl delete -f -
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-custom-resource-definitions.yaml | kubectl delete -f -
```
