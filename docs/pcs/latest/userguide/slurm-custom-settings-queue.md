

# Custom Slurm settings for AWS PCS queues
<a name="slurm-custom-settings-queue"></a>

The following custom Slurm settings are supported at the queue level:

**Important**  
QOS values referenced in `AllowQos`, `DenyQos`, or `QOS` settings must already exist in the Slurm accounting database. Otherwise, Slurm might fail to apply the configuration. For more information about Slurm accounting, see [Slurm accounting in AWS PCS](slurm-accounting.md).
+ [AllowAccounts](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowAccounts)
+ [AllowQos](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowQoS)
+ [Default](https://slurm.schedmd.com/slurm.conf.html#OPT_Default)
+ [DefaultTime](https://slurm.schedmd.com/slurm.conf.html#OPT_DefaultTime)
+ [DenyAccounts](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyAccounts)
+ [DenyQos](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyQoS)
+ [ExclusiveUser](https://slurm.schedmd.com/slurm.conf.html#OPT_ExclusiveUser)
+ [GraceTime](https://slurm.schedmd.com/slurm.conf.html#OPT_GraceTime)
+ [MaxTime](https://slurm.schedmd.com/slurm.conf.html#OPT_MaxTime)
+ [OverSubscribe](https://slurm.schedmd.com/slurm.conf.html#OPT_OverSubscribe)
+ [OverTimeLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit)
+ [PowerDownOnIdle](https://slurm.schedmd.com/slurm.conf.html#OPT_PowerDownOnIdle)
+ [PreemptMode](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode)
+ [PriorityJobFactor](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityJobFactor)
+ [PriorityTier](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityTier)
+ [QOS](https://slurm.schedmd.com/slurm.conf.html#OPT_QOS)
+ [TRESBillingWeights](https://slurm.schedmd.com/slurm.conf.html#OPT_TRESBillingWeights)