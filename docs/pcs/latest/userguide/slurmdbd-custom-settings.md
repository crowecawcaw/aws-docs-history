

# Configuring custom SlurmDBD settings in AWS PCS
<a name="slurmdbd-custom-settings"></a>

Slurm's database daemon (slurmdbd) manages accounting data, data retention policies, and privacy controls. AWS PCS lets you customize `slurmdbd.conf` settings at the cluster level through the `SlurmdbdCustomSettings` property of `SlurmConfiguration` during cluster creation or update.

## Configuring slurmdbd settings
<a name="slurmdbd-custom-settings-configure"></a>

Slurmdbd custom settings can be configured through the AWS Console, CLI, or SDKs during cluster creation or modified later through update operations.

------
#### [ AWS Management Console ]

Navigate to **Additional scheduler settings** in the create or edit page for a cluster resource.

**To add a new setting**

1. Choose **Add new setting**.

1. Select a **Parameter** name from the dropdown (which includes brief parameter descriptions).

1. Provide the corresponding value.

**To unset a custom setting**

1. Choose **Remove** next to the relevant parameter/value pair.

1. Create or update the resource.

------
#### [ AWS CLI ]

For programmatic management of slurmdbd settings, use the `SlurmdbdCustomSettings` field in create or update cluster operations.

**Example – Setting `TrackWCKey` on a cluster**  

```
aws pcs update-cluster --cluster-identifier {{my-cluster}} \
--slurm-configuration \
'SlurmdbdCustomSettings=[{parameterName=TrackWCKey,parameterValue="yes"}]'
```

------

## Supported slurmdbd settings for clusters
<a name="slurmdbd-custom-settings-cluster"></a>

The following custom slurmdbd settings are supported at the cluster level:
+ [AllowNoDefAcct](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_AllowNoDefAcct)
+ [AllResourcesAbsolute](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_AllResourcesAbsolute)
+ [CommitDelay](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_CommitDelay)
+ [DefaultQOS](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_DefaultQOS)
+ [MaxQueryTimeRange](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_MaxQueryTimeRange)
+ [Parameters](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_Parameters)
+ [PrivateData](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PrivateData)
+ [PurgeEventAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeEventAfter)
+ [PurgeJobAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeJobAfter)
+ [PurgeResvAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeResvAfter)
+ [PurgeStepAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeStepAfter)
+ [PurgeSuspendAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeSuspendAfter)
+ [PurgeTXNAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeTXNAfter)
+ [PurgeUsageAfter](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_PurgeUsageAfter)
+ [TrackWCKey](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_TrackWCKey)