# Configuring custom Slurm settings in AWS PCS

Use custom Slurm settings to configure additional Slurm parameters across Cluster, Queue, and Compute Node Group resources. This release adds support for Slurm settings on Queue resources, providing granular control over partition-specific behaviors.

## Benefits of custom Slurm settings

Custom Slurm settings provide sophisticated control over your AWS PCS-based HPC environment. You can implement detailed accounting, enforce access controls, and optimize workload execution through quality-of-service configurations and preemption policies. These capabilities ensure critical jobs receive necessary resources while maintaining efficient cluster utilization. Whether you manage GPU-accelerated workloads, implement fair-share scheduling, or control job lifecycles, custom settings help align your HPC infrastructure with operational requirements and research objectives.

## Configuring custom settings

Custom Slurm settings can be configured through the AWS Console, CLI, or SDKs during resource creation or modified later through update operations.

AWS Management Console
Navigate to **Additional scheduler settings** in the create
or edit page for any resource type (cluster, queue, or compute node group).

######

To add a new setting

1. Choose **Add new setting**.
2. Select a **Parameter** name from the dropdown (which includes brief parameter descriptions).
3. Provide the corresponding value.

######

To unset a custom setting

1. Choose **Remove** next to the relevant parameter/value pair.
2. Create or update the resource.

AWS CLI
For programmatic management of custom settings, use the `SlurmCustomSettings` field in create or update operations.

###### Example – Updating the `Prolog` parameter on a cluster

```
aws pcs update-cluster --cluster-identifier `my-cluster` \
--slurm-configuration \
'SlurmCustomSettings=[{parameterName=Prolog,parameterValue="`/path/to/prolog.sh`"}]'
```

###### Example – Setting a queue to be the `Default` on a cluster

```
aws pcs update-queue \
    --cluster-identifier `my-cluster` \
    --queue-identifier `my-queue` \
    --slurm-configuration 'SlurmCustomSettings=[{parameterName=Default,parameterValue=YES}]'
```

###### Example – Setting custom `Features` on a compute node group

```
aws pcs update-compute-node-group \
    --cluster-identifier `my-cluster` \
    --compute-node-group-identifier `my-cng-1` \
    --slurm-configuration \
    'SlurmCustomSettings=[{parameterName=Features,parameterValue="`gpu,nvme`"}]'
```

## Validation and error handling

AWS PCS implements a multi-layered validation process for custom Slurm settings. During both create and update operations, we perform synchronous validations that include:

- Field-level checks: We validate individual settings for correct data types, allowed values, and format requirements. For example, we ensure time values are in the correct Slurm format and boolean values use accepted Slurm boolean representations.
- Context-aware validations: Some settings are checked against the broader configuration context. For instance, certain parameters are only valid when Slurm accounting is enabled.
- Inter-setting consistency: We verify that mutually exclusive options aren't set together and that interdependent settings are configured correctly.

If validation fails, you'll receive a `ValidationException` with a specific error code (e.g., InvalidInput), a clear error message describing the issue, and a list of the invalid fields and their respective error details.

While many issues are caught during this initial validation, some complex interactions between settings may only become apparent when applying the configuration. In such cases, the operation will fail with an informative error message, and any partial changes will be rolled back.

## Limitations

AWS PCS implements an allow-list approach to protect service security and operational stability. Settings that could compromise service account security or interfere with managed service capabilities are restricted. However, we continuously evaluate customer needs and can add support for additional settings based on customer feedback.

###### Topics

- [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md "slurm-custom-settings-cluster.md")
- [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md")
- [Custom Slurm settings for AWS PCS queues](slurm-custom-settings-queue.md "slurm-custom-settings-queue.md")
- [Troubleshooting custom Slurm settings in AWS PCS](slurm-custom-settings-troubleshooting.md "slurm-custom-settings-troubleshooting.md")
