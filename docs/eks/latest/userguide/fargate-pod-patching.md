**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set actions for AWS Fargate OS patching events

Amazon EKS periodically patches the OS for AWS Fargate nodes to keep them secure. As part of the patching process, we recycle the nodes to install OS patches. Updates are attempted in a way that creates the least impact on your services. However, if Pods aren’t successfully evicted, there are times when they must be deleted. The following are actions that you can take to minimize potential disruptions:

- Set appropriate Pod disruption budgets (PDBs) to control the number of Pods that are down simultaneously.
- Create Amazon EventBridge rules to handle failed evictions before the Pods are deleted.
- Manually restart your affected pods before the eviction date posted in the notification you receive.
- Create a notification configuration in AWS User Notifications.
  Amazon EKS works closely with the Kubernetes community to make bug fixes and security patches available as quickly as possible. All Fargate Pods start on the most recent Kubernetes patch version, which is available from Amazon EKS for the Kubernetes version of your cluster. If you have a Pod with an older patch version, Amazon EKS might recycle it to update it to the latest version. This ensures that your Pods are equipped with the latest security updates. That way, if there’s a critical [Common Vulnerabilities and Exposures](https://cve.mitre.org/ "https://cve.mitre.org/") (CVE) issue, you’re kept up to date to reduce security risks.

When the AWS Fargate OS is updated, Amazon EKS will send you a notification that includes your affected resources and the date of upcoming pod evictions. If the provided eviction date is inconvenient, you have the option to manually restart your affected pods before the eviction date posted in the notification. Any pods created before the time at which you receive the notification are subject to eviction. Refer to the [Kubernetes Documentation](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart") for further instructions on how to manually restart your pods.

To limit the number of Pods that are down at one time when Pods are recycled, you can set Pod disruption budgets (PDBs). You can use PDBs to define minimum availability based on the requirements of each of your applications while still allowing updates to occur. Your PDB’s minimum availability must be less than 100%. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/ "https://kubernetes.io/docs/tasks/run-application/configure-pdb/") in the Kubernetes Documentation.

Amazon EKS uses the [Eviction API](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/#eviction-api "https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/#eviction-api") to safely drain the Pod while respecting the PDBs that you set for the application. Pods are evicted by Availability Zone to minimize impact. If the eviction succeeds, the new Pod gets the latest patch and no further action is required.

When the eviction for a Pod fails, Amazon EKS sends an event to your account with details about the Pods that failed eviction. You can act on the message before the scheduled termination time. The specific time varies based on the urgency of the patch. When it’s time, Amazon EKS attempts to evict the Pods again. However, this time a new event isn’t sent if the eviction fails. If the eviction fails again, your existing Pods are deleted periodically so that the new Pods can have the latest patch.

The following is a sample event received when the Pod eviction fails. It contains details about the cluster, Pod name, Pod namespace, Fargate profile, and the scheduled termination time.

```
 {
    "version": "0",
    "id": "12345678-90ab-cdef-0123-4567890abcde",
    "detail-type": "EKS Fargate Pod Scheduled Termination",
    "source": "aws.eks",
    "account": "111122223333",
    "time": "2021-06-27T12:52:44Z",
    "region": "region-code",
    "resources": [
        "default/my-database-deployment"
    ],
    "detail": {
        "clusterName": "my-cluster",
        "fargateProfileName": "my-fargate-profile",
        "podName": "my-pod-name",
        "podNamespace": "default",
        "evictErrorMessage": "Cannot evict pod as it would violate the pod's disruption budget",
        "scheduledTerminationTime": "2021-06-30T12:52:44.832Z[UTC]"
    }
}
```

In addition, having multiple PDBs associated with a Pod can cause an eviction failure event. This event returns the following error message.

```
 "evictErrorMessage": "This pod has multiple PodDisruptionBudget, which the eviction subresource does not support",
```

You can create a desired action based on this event. For example, you can adjust your Pod disruption budget (PDB) to control how the Pods are evicted. More specifically, suppose that you start with a PDB that specifies the target percentage of Pods that are available. Before your Pods are force terminated during an upgrade, you can adjust the PDB to a different percentage of Pods. To receive this event, you must create an Amazon EventBridge rule in the AWS account and AWS Region that the cluster belongs to. The rule must use the following **Custom pattern**. For more information, see [Creating Amazon EventBridge rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.

```
 {
  "source": ["aws.eks"],
  "detail-type": ["EKS Fargate Pod Scheduled Termination"]
}
```

A suitable target can be set for the event to capture it. For a complete list of available targets, see [Amazon EventBridge targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md") in the _Amazon EventBridge User Guide_. You can also create a notification configuration in AWS User Notifications. When using the AWS Management Console to create the notification, under **Event Rules**, choose **Elastic Kubernetes Service (EKS)** for **AWS service name** and **EKS Fargate Pod Scheduled Termination** for **Event type**. For more information, see [Getting started with AWS User Notifications](../../../notifications/latest/userguide/getting-started.md "../../../notifications/latest/userguide/getting-started.md") in the AWS User Notifications User Guide.

See [FAQs: Fargate Pod eviction notice](https://repost.aws/knowledge-center/fargate-pod-eviction-notice "https://repost.aws/knowledge-center/fargate-pod-eviction-notice") in _AWS re:Post_ for frequently asked questions regarding EKS Pod Evictions.
