# Updating an Amazon ECS

cluster

You can modify the following cluster properties:

- Set a default capacity provider

Each cluster can have one or more capacity providers and an optional capacity
provider strategy. The capacity provider strategy determines how the tasks are
spread across the cluster's capacity providers. When you run a standalone task or
create a service, you either use the cluster's default capacity provider strategy or
a capacity provider strategy that overrides the default one.

- Turn on Container Insights.

CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your
containerized applications and microservices. Container Insights also provides diagnostic
information, such as container restart failures, that you use to isolate issues and
resolve them quickly. For more information, see [Monitor Amazon ECS containers using Container Insights with
enhanced observability](cloudwatch-container-insights.md "cloudwatch-container-insights.md").

- Add tags to help you identify your clusters.

###### Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the cluster.
4. On the **Cluster : `name`** page, choose
   **Update cluster**.
5. To set the default capacity provider, under **Default capacity provider
   strategy**, choose **Add more**.
   1. For **Capacity provider**, choose the capacity
      provider.
   2. (Optional) For **Base**, enter the minimum number of
      tasks that run on the capacity provider.

   You can only set a **Base** value for one capacity
   provider. 3. (Optional) For **Weight**, enter the relative percentage
   of the total number of launched tasks that use the specified capacity
   provider. 4. (Optional) Repeat the steps for any additional capacity providers.

6. To turn on or off Container Insights, expand **Monitoring**, and then turn on
   **Use Container Insights**.
7. To help identify your cluster, expand **Tags**, and then
   configure your tags.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

[Remove a tag] Choose **Remove** to the right of the tag’s Key
and Value. 8. Choose **Update**.
