# Updating an Amazon ECS service

After you create a service, there are times when you might need to update the service
parameters, for example the number of tasks.

When you update a service that uses Amazon ECS circuit breaker, Amazon ECS creates a service
deployment and a service revision. These resources allow you to view detailed information
about the service history. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md "service-deployment.md").

## Prerequisites

Before updating a service, verify which service parameters can be changed for your
deployment type. For a complete list of changeable parameters, see [Update Amazon ECS service parameters](update-service-parameters.md "update-service-parameters.md").

## Procedure

Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the
   cluster.
3. On the cluster details page, in the **Services**
   section, select the check box next to the service, and then choose
   **Update**.
4. To have your service start a new deployment, select
   **Force new deployment**.
5. For **Task definition**, choose the task
   definition family and revision.

###### Important

The console validates that the selected task definition family
and revision are compatible with the defined compute
configuration. If you receive a warning, verify both your task
definition compatibility and the compute configuration that you
selected. 6. If you chose **Replica**, for **Desired
tasks**, enter the number of tasks to launch and
maintain in the service. 7. If you chose **Replica**, to have Amazon ECS monitor
the distribution of tasks across Availability Zones, and
redistribute them when there is an imbalance, under
**Availability Zone service rebalancing**,
select **Availability Zone service
rebalancing**. 8. For **Min running tasks**, enter the lower limit
on the number of tasks in the service that must remain in the
`RUNNING` state during a deployment, as a percentage
of the desired number of tasks (rounded up to the nearest integer).
For more information, see [Deployment configuration](service_definition_parameters.md#sd-deploymentconfiguration "service_definition_parameters.md#sd-deploymentconfiguration"). 9. For **Max running tasks**, enter the upper limit
on the number of tasks in the service that are allowed in the
`RUNNING` or `PENDING` state during a
deployment, as a percentage of the desired number of tasks (rounded
down to the nearest integer). 10. To configure how tasks are deployed for your service, expand
**Deployment options** and then configure your
options.

    1. For **Deployment controller type**,
     specify the service deployment controller. The Amazon ECS console
     supports the following controller types:
     `ECS`.
    2. For **Deployment strategy**, choose the
     strategy used by Amazon ECS to deploy new versions of the
     service.
    3. Depending on the choice of **Deployment
     strategy**, do the following:




    | Deployment strategy | Steps |
    | --- | --- |
    | **Rolling update** | 1. For **Min running tasks<br>%**, specify a minimum percentage value<br>of tasks that must run during a service<br>deployment. For more information, see [Deploy Amazon ECS services by replacing tasks](deployment-type-ecs.md "deployment-type-ecs.md").<br>2. For **Max running tasks<br>%**, specify a maximum percentage value<br>of tasks that can run during a service deployment.<br>For more information, see [Deploy Amazon ECS services by replacing tasks](deployment-type-ecs.md "deployment-type-ecs.md"). |
    | **Blue/green** | For **Bake time**, specify<br>a time duration, in minutes, that blue and green<br>service revisions should run simultaenously. For<br>more information, see [Amazon ECS blue/green deployments](deployment-type-blue-green.md "deployment-type-blue-green.md"). |
    4. To run Lambda functions for a lifecycle stage, under **Deployment lifecyce
     hooks** do the following for each unique Lambda function:


    	1. Choose **Add**.


    	Repeat for every unique function you want to run.
    	2. For **Lambda function**, enter the function name.
    	3. For **Role**, choose the role that you created in the prerequisites with the
    	 blue/green permissions.


    	For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md "blue-green-permissions.md").
    	4. For **Lifecycle stages**, select the stages the Lambda function runs.
    	5. (Optional) For **Hook details**, enter a key value pair that provides
    	 information about the hook.

11. To configure how Amazon ECS detects and handles deployment failures, expand
    **Deployment failure detection**, and then choose
    your options.
    1.  To stop a deployment when the tasks cannot start, select **Use the Amazon ECS
        deployment circuit breaker**.

    To have the software automatically roll back the deployment to the last
    completed deployment state when the deployment circuit breaker sets the
    deployment to a failed state, select **Rollback on
    failures**. 2. To stop a deployment based on application metrics, select **Use CloudWatch alarm(s)**.
    Then, from **CloudWatch alarm name**, choose the alarms. To create a new alarm,
    go to the CloudWatch console.

    To have the software automatically roll back the deployment to the last
    completed deployment state when a CloudWatch alarm sets the
    deployment to a failed state, select **Rollback on
    failures**.

12. To change the compute options, expand **Compute
    configuration**, and then do the following:
    1.  For services on AWS Fargate, for **Platform
        version**, choose the new version.
    2.  For services that use a capacity provider strategy, for
        **Capacity provider strategy**, do the
        following:

            * To add an additional capacity provider, choose
             **Add more**. Then, for
             **Capacity provider**, choose the
             capacity provider.
            * To remove a capacity provider, to the right of the
             capacity provider, choose
             **Remove**.

        A service that's using an Auto Scaling group capacity provider can't be
        updated to use a Fargate capacity provider. A service
        that's using a Fargate capacity provider can't be updated
        to use an Auto Scaling group capacity provider.

13. (Optional) To configure service Auto Scaling, expand **Service auto
    scaling**, and then specify the following parameters.To use predicte auto scaling, which looks at past load data from traffic flows, configure it after you create the service. For more information, see [Use historical patterns to scale Amazon ECS services with predictive scaling](predictive-auto-scaling.md "predictive-auto-scaling.md").
    1.  To use service auto scaling, select **Service auto
        scaling**.
    2.  For **Minimum number of tasks**, enter the lower limit of
        the number of tasks for service auto scaling to use. The desired count will not go below this count.
    3.  For **Maximum number of tasks**, enter the upper
        limit of the number of tasks for service auto scaling to use. The desired count will not go above this count.
    4.  Choose the policy type. Under **Scaling policy type**, choose
        one of the following options.

    | To use this policy type | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Target tracking         | 1. For **Scaling policy<br>type**, choose **Target<br>tracking**.<br>2. For **Policy name**, enter<br>the name of the policy.<br>3. For **ECS service metric**,<br>select one of the following metrics.<br>• **ECSServiceAverageCPUUtilization** –<br>Average CPU utilization of the service.<br>• **ECSServiceAverageMemoryUtilization** –<br>Average memory utilization of the service.<br>• **ALBRequestCountPerTarget**<br>– Number of requests completed per target<br>in an Application Load Balancer target group.<br>4. For **Target value**, enter<br>the value the service maintains for the selected<br>metric.<br>5. For **Scale-out cooldown<br>period**, enter the amount of time, in seconds, after a scale-out activity (add tasks) that must pass before another scale-out activity can start.<br>6. For **Scale-in cooldown<br>period**, enter the amount of time, in seconds, after a scale-in activity (remove tasks) that must pass before another scale-in activity can start.<br>7. To prevent the policy from performing a<br>scale-in activity, select **Turn off<br>scale-in**.<br>8. • (Optional) Select \*_Turn off scale-in_<br>• if you want your scaling policy to scale out for increased traffic but don’t need it to scale in when traffic decreases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | Step scaling            | 1. For **Scaling policy<br>type**, choose **Step<br>scaling**.<br>2. For **Policy name**, enter<br>the policy name.<br>3. For **Alarm name**, enter a<br>unique name for the alarm.<br>4. For **Amazon ECS service<br>metric**, choose the metric to use for<br>the alarm.<br>5. For **Statistic**, choose<br>the alarm statistic.<br>6. For **Period**, choose the<br>period for the alarm.<br>7. For **Alarm condition**,<br>choose how to compare the selected metric to the<br>defined threshold.<br>8. For **Threshold to compare<br>metrics\*<br>• and **Evaluation period<br>to initiate alarm**, enter the threshold<br>used for the alarm and how long to evaluate the<br>threshold.<br>9. Under **Scaling actions**, do<br>the following:<br>• For **Action**,<br>select whether to add, remove, or set a<br>specific desired count for your service.<br>• If you chose to add or remove tasks,<br>for **Value**, enter the number<br>of tasks (or percent of existing tasks) to add or<br>remove when the scaling action is initiated. If<br>you chose to set the desired count, enter the<br>number of tasks. For **Type**,<br>select whether the **Value*<br>• is<br>an integer or a percent value of the existing<br>desired count.<br>• For **Lower bound** and<br>**Upper bound**, enter the lower<br>boundary and upper boundary of your step scaling<br>adjustment. By default, the lower bound for an add policy is the alarm threshold and the upper bound is positive (+) infinity. By default, the upper bound for a remove policy is the alarm threshold and the lower bound is negative (-) infinity.<br>• (Optional) Add additional scaling options.<br>Choose **Add new scaling<br>action**, and then repeat the<br>\*\*Scaling actions*<br>• steps.<br>• For **Cooldown period**, enter the amount of time, in seconds, to wait for a previous scaling activity to take effect. For an add policy, this is the time after a scale-out activity that the scaling policy blocks scale-in activities and limits how many tasks can be scale out at a time. For a remove policy, this is the time after a scale-in activity that must pass before another scale-in activity can start. |

14. (Optional) To use Service Connect, select **Turn on
    Service Connect**, and then specify the
    following:
    1.  Under **Service Connect configuration**,
        specify the client mode.
        - If your service runs a network client application
          that only needs to connect to other services in the
          namespace, choose **Client side
          only**.
        - If your service runs a network or web service
          application and needs to provide endpoints for this
          service, and connects to other services in the
          namespace, choose **Client and
          server**.

    2.  To use a namespace that is not the default cluster
        namespace, for **Namespace**, choose the
        service namespace. This can be a namespace created separately in the same AWS Region in your
        AWS account or a namespace in the same Region that is shared with your
        account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see [Cross-account AWS Cloud Map namespace
        sharing](../../../cloud-map/latest/dg/sharing-namespaces.md "../../../cloud-map/latest/dg/sharing-namespaces.md") in the _AWS Cloud Map Developer Guide_
    3.  (Optional) Specify a log configuration. Select **Use log
        collection**. The default option sends container logs to
        CloudWatch Logs. The other log driver options are configured using AWS FireLens.
        For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

    The following describes each container log destination in more
    detail.

        * **Amazon CloudWatch** – Configure the task to
         send container logs to CloudWatch Logs. The default log driver options are
         provided, which create a CloudWatch log group on your behalf. To
         specify a different log group name, change the driver option
         values.
        * **Amazon Data Firehose** – Configure the task to
         send container logs to Firehose. The default log driver options are
         provided, which send logs to a Firehose delivery stream. To specify
         a different delivery stream name, change the driver option
         values.
        * **Amazon Kinesis Data Streams** – Configure the task to
         send container logs to Kinesis Data Streams. The default log driver options are
         provided, which send logs to an Kinesis Data Streams stream. To specify a
         different stream name, change the driver option values.
        * **Amazon OpenSearch Service** – Configure the task to
         send container logs to an OpenSearch Service domain. The log driver options
         must be provided.
        * **Amazon S3** – Configure the task to send
         container logs to an Amazon S3 bucket. The default log driver options
         are provided, but you must specify a valid Amazon S3 bucket
         name.

    4.  To enable access logs, follow these steps:
        1. Expand **Access log configuration**. For **Format**, choose either **JSON** or `TEXT`.
        2. To include query parameters in access logs, select **Include query parameters**.###### Note

    To disable access logs, for **Format**, choose **None**.

15. If your task uses a data volume that's compatible with
    configuration at deployment, you can configure the volume by
    expanding **Volume**.

The volume name and volume type are configured when you create a
task definition revision and can't be changed when you update a
service. To update the volume name and type, you must create a new
task definition revision and update the service by using the new
revision.

| To configure this volume type | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon EBS                    | 1. For **EBS volume type**, choose<br>the type of EBS volume that you want<br>to attach to your task.<br>2. For **Size (GiB)**, enter a valid<br>value for the volume size in gibibytes (GiB). You<br>can specify a minimum of 1 GiB and a maximum of<br>16,384 GiB volume size. This value is required<br>unless you provide a snapshot ID.<br>3. For **IOPS**, enter the maximum<br>number of input/output operations (IOPS) that the<br>volume should provide. This value is configurable<br>only for `io1`,`io2`, and<br>`gp3` volume types.<br>4. For **Throughput (MiB/s)**, enter<br>the throughput that the volume should provide, in<br>mebibytes per second (MiBps, or MiB/s). This value<br>is configurable only for the `gp3` volume<br>type.<br>5. For **Snapshot ID**, choose an<br>existing Amazon EBS volume snapshot or enter the ARN of a<br>snapshot if you want to create a volume from a<br>snapshot. You can also create a new, empty volume by<br>not choosing or entering a snapshot<br>ID.<br>6. If you specify a **Snapshot ID**, you<br>can specify a **Volume initialization rate<br>(MiB/s)**. Enter a value between 100 and<br>300, in MiB/s, that will determine how fast data is<br>loaded from the snapshot specified using<br>**Snapshot ID\*<br>• for volume<br>creation.<br>7. For **File system type**, choose<br>the type of file system that will be used for data<br>storage and retrieval on the volume. You can choose<br>either the operating system default or a specific<br>file system type. The default for Linux is<br>`XFS`. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start.<br>8. For **Infrastructure role**,<br>choose an IAM role with the necessary permissions<br>that allow Amazon ECS to manage Amazon EBS volumes for tasks.<br>You can attach the<br>`AmazonECSInfrastructureRolePolicyForVolumes`<br>managed policy to the role, or you can use the<br>policy as a guide to create and attach an your own<br>policy with permissions that meet your specific<br>needs. For more information about the necessary<br>permissions,<br>see<br>[Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").<br>9. For **Encryption**, choose<br>**Default*<br>• if you want to use<br>the Amazon EBS encryption by default settings. If your<br>account has [Encryption by default](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md") configured, the<br>volume will be encrypted with the AWS Key Management Service (AWS KMS)<br>key that's specified in the setting. If you choose<br>\*\*Default*<br>• and Amazon EBS default<br>encryption isn't turned on, the volume will be<br>unencrypted.<br>If you choose **Custom**, you can<br>specify an AWS KMS key of your choice for volume<br>encryption.<br>If you choose **None**, the<br>volume will be unencrypted unless you have<br>encryption by default configured,<br>or<br>if you create a volume from an encrypted<br>snapshot.<br>10. If you've chosen **Custom\*<br>• for<br>**Encryption**, you must specify<br>the AWS KMS key that you want to use. For<br>**KMS key**, choose an<br>AWS KMS key or enter a key ARN. If you choose to<br>encrypt your volume by using a symmetric customer managed key,<br>make sure that you have the right permissions<br>defined in your AWS KMS key policy. For more<br>information, see [Data encryption for Amazon EBS volumes](ebs-volumes.md#ebs-kms-encryption "ebs-volumes.md#ebs-kms-encryption").<br>11. (Optional) Under **Tags**, you can<br>add tags to your Amazon EBS volume by either propagating tags<br>from the task definition or service, or by providing your own<br>tags.<br>If you want to propagate tags from the task<br>definition, choose **Task definition**<br>for **Propagate tags from**. If you want to propagate tags from the service, choose **Service**<br>for **Propagate tags from**. If you<br>choose **Do not propagate**, or if you<br>don't choose a value, the tags aren't propagated.<br>If you want to provide your own tags, choose<br>**Add tag\*<br>• and then provide the<br>key and value for each tag you add.<br>For more information about tagging Amazon EBS volumes, see<br>[Tagging Amazon EBS volumes](specify-ebs-config.md#ebs-volume-tagging "specify-ebs-config.md#ebs-volume-tagging"). |

16. (Optional) To help identify your service, expand the
    **Tags** section, and then configure your
    tags.
    - [Add a tag] Choose **Add tag**, and do
      the following:
      - For **Key**, enter the key
        name.
      - For **Value**, enter the key
        value.

    - [Remove a tag] Next to the tag, choose **Remove
      tag**.

17. Choose **Update**.

AWS CLI

- Run `update-service`. For information about running the
  command, see [update-service](../../../cli/latest/reference/ecs/update-service.md "../../../cli/latest/reference/ecs/update-service.md") in the AWS Command Line Interface Reference.

The following `update-service` example updates the
desired task count of the service `my-http-service` to 2.

Replace the `user-input` with your
values.

```
aws ecs update-service \
    --cluster `MyCluster` \
    --service `my-http-service` \
    --desired-count 2
```

## Next steps

Track your deployment and view your service history for services that Amazon ECS circuit
breaker. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md "service-deployment.md").
