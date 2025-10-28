# Configure permissions for agents to deliver metrics

After you install agents for Network Flow Monitor, you must enable the agents to send network
metrics to the Network Flow Monitor ingestion APIs. Agents in Network Flow Monitor must have permission to access the Network Flow Monitor ingestion APIs
so that they can deliver network flow metrics that they've collected for each instance. You grant this access
by implementing IAM roles for service accounts (IRSA).

To enable agents to deliver network metrics to Network Flow Monitor, follow the steps in this section.

1. **Implement IAM roles for service accounts**

IAM roles for service accounts provides the ability to manage credentials for your applications,
similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances. Implementing IRSA is
the recommended way to provide all permissions required by Network Flow Monitor agents to successfully access
Network Flow Monitor ingestion APIs. For more information, see [IAM roles for service accounts](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md")
in the Amazon EKS User Guide.

When you set up IRSA for Network Flow Monitor agents, use the following information:

    * **ServiceAccount:** When you define your IAM role trust policy,
     for `ServiceAccount`, specify `aws-network-flow-monitor-agent-service-account`.
    * **Namespace:** For the `namespace`, specify `amazon-network-flow-monitor`.
    * **Temporary credentials deployment:** When you configure
     permissions after you have deployed Network Flow Monitor agent pods, updating the `ServiceAccount` with
     your IAM role, Kubernetes does not deploy the IAM role credentials. To ensure that the Network Flow Monitor
     agents acquire the IAM role credentials that you've specified, you must rolling out a restart of `DaemonSet`.
     For example, use a command like the following:


    `kubectl rollout restart daemonset -n amazon-network-flow-monitor aws-network-flow-monitor-agent`

2. **Confirm that the Network Flow Monitor agent is successfully accessing the Network Flow Monitor ingestion APIs**

You can check to make sure that your configuration for agents is working correctly by
using the HTTP 200 logs for Network Flow Monitor agent pods. First, search for
a Network Flow Monitor agent pod, and then search through the log files to find successful HTTP 200 requests.
For example, you can do the following:

    1. Locate a Network Flow Monitor agent pod name. For example, you can use the following command:



    ```
    RANDOM_AGENT_POD_NAME=$(kubectl get pods -o wide -A | grep amazon-network-flow-monitor | grep Running | head -n 1 | tr -s ' ' | cut -d " " -f 2)

    ```
    2. Grep all the HTTP logs for the pod name that you've located. If you've changed the NAMESPACE, make sure
     that you use the new one.



    ```
    NAMESPACE=amazon-network-flow-monitor
    kubectl logs $`RANDOM_AGENT_POD_NAME` -\-namespace ${NAMESPACE} | grep HTTP

    ```

If access has been granted successfully, you should see log entries similar to the following:

```
...
{"level":"INFO","message":"HTTP request complete","status":200,"target":"amzn_nefmon::reports::publisher_endpoint","timestamp":1737027525679}
{"level":"INFO","message":"HTTP request complete","status":200,"target":"amzn_nefmon::reports::publisher_endpoint","timestamp":1737027552827}

```

Note that the Network Flow Monitor agent publishes network flow reports every 30 seconds, by calling the Network Flow Monitor ingestion APIs.
