# Upgrading to Container Insights
 with enhanced observability for Amazon EKS in CloudWatch

###### Important

If you are upgrading or installing Container Insights on an Amazon EKS cluster, we
 recommend that you use the Amazon CloudWatch Observability EKS add-on for the installation,
 instead of using the instructions in this section. Additionally, to retrieve
 accelerated computing metrics, you must use the Amazon CloudWatch Observability EKS
 add-on. For more information and instructions, see [Quick start with the Amazon CloudWatch
 Observability EKS add-on](Container-Insights-setup-EKS-addon.md "Container-Insights-setup-EKS-addon.md").

Container Insights with enhanced observability for Amazon EKS is the newest version of
 Container Insights. It collects detailed metrics from clusters running Amazon EKS and offers
 curated, immediately usable dashboards to drill down into application and infrastructure
 telemetry. For more information about this version of Container Insights, see [Container Insights with enhanced
 observability for Amazon EKS](container-insights-detailed-metrics.md "container-insights-detailed-metrics.md").

If you have installed the original version of Container Insights in an Amazon EKS cluster
 and you want to upgrade it to the newer version with enhanced observability, follow the
 instructions in this section.

###### Important

Before completing the steps in this section, you must have verified the
 prerequisites including cert-manager. For more information, see [Quick Start with
 the CloudWatch agent operator and Fluent Bit](Container-Insights-setup-EKS-quickstart.md#Container-Insights-setup-EKS-quickstart-FluentBit "Container-Insights-setup-EKS-quickstart.md#Container-Insights-setup-EKS-quickstart-FluentBit").

###### To upgrade an Amazon EKS cluster to Container Insights with enhanced observability for
 Amazon EKS

1. Install the CloudWatch agent operator by entering the following command. Replace
 `my-cluster-name` with the name of your Amazon EKS or
 Kubernetes cluster, and replace `my-cluster-region` with
 the name of the Region where the logs are published. We recommend that you use the
 same Region where your cluster is deployed to reduce the AWS outbound data
 transfer costs.



```
ClusterName=`my-cluster-name`
RegionName=`my-cluster-region`
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-operator-rendered.yaml | sed 's/{{cluster_name}}/'${ClusterName}'/g;s/{{region_name}}/'${RegionName}'/g' | kubectl apply -f -
```

If you notice a failure caused by conflicting resources, it is likely because
 you already have the CloudWatch agent and Fluent Bit with its associated components such
 as the ServiceAccount, the ClusterRole and the ClusterRoleBinding installed on the
 cluster. When the CloudWatch agent operator tries to install the CloudWatch agent and its
 associated components, if it detects any change in the contents, it by default fails
 the installation or update to avoid overwriting the state of the resources on the
 cluster. We recommend that you delete any existing CloudWatch agent with Container
 Insights setup that you had previously installed on the cluster, and then install
 the CloudWatch agent operator.
2. (Optional) To apply an existing custom Fluent Bit configuration, you must update
 the configmap associated with the Fluent Bit daemonset. The CloudWatch agent operator
 provides a default configuration for Fluent Bit, and you can override or modify the
 default configuration as needed. To apply a custom configuration, follow these
 steps.


	1. Open the existing configuration by entering the following command.
	
	
	
	```
	kubectl edit cm fluent-bit-config -n amazon-cloudwatch
	```
	2. Make your changes in the file, then enter `:wq` to save the file
	 and exit edit mode.
	3. Restart Fluent Bit by entering the following command.
	
	
	
	```
	kubectl rollout restart ds fluent-bit -n amazon-cloudwatch
	```
