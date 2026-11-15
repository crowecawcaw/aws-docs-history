

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Get started with sandboxes
<a name="sandboxing-getting-started"></a>

Get started by running your first isolated pod, then move to confidential pods when you need to protect workload data from the node. Use resource isolation to cap the host resources a single sandbox consumes.

Before you benchmark a workload, raise the default network limits so they do not cap request-heavy services. For more information, see [Raising network bandwidth](sandboxing-resource-isolation.md#sandboxing-raise-bandwidth).

To learn more about getting started, see [Sandboxing blueprints](https://aws-samples.github.io/sample-eks-nitro-sandbox). They are runnable, end-to-end examples for AI coding agents, warm pools, CI/CD runners, storage, network policy, and confidential pods. Each one includes the manifests, scripts, and step-by-step instructions to run it in your own cluster.

**Topics**
+ [Run a pod in isolated mode](sandboxing-isolated-setup.md)
+ [Run a pod in confidential mode](sandboxing-confidential-setup.md)
+ [Resource isolation and throttling](sandboxing-resource-isolation.md)