# Create a limit

You create a limit using the Deadline Cloud console or the [CreateLimit operation in the
 Deadline Cloud API](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLimit.html "https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLimit.html"). Limits are defined for a farm, but associated with queues. After you
 create a limit, you can associate it with one or more queues.

###### To create a limit

1. From the Deadline Cloud console ([https://console.aws.amazon.com/deadlinecloud/home](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home")) dashboard, select the farm
 that you want to create a queue for.
2. Choose the farm to add the limit to, choose the **Limits**  tab,
 and then choose **Create limit**.
3. Provide the details for the limit. The **Amount requirement name**
 is the name used in the job template to identify the limit. It must begin with the
 prefix `amount.` followed by the amount name. The amount
 requirement name must be unique in queues associated with the limit.
4. If you choose **Set a maximum amount**, that is the total number of
 resources allowed by this limit. If you choose **No maximum amount**,
 resource usage isn't limited. Even when resource usage isn't limited, the
 `CurrentCount` Amazon CloudWatch metric is emitted so that you can track usage. For
 more information, see [CloudWatch
 metrics](cloudwatch-metrics.md "cloudwatch-metrics.md") in the *Deadline Cloud Developer Guide*.
5. If you already know the queues that should use the limit, you can choose them now.
 You don't need to associate a queue to create a limit.
6. Choose **Create limit**.
