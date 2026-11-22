

# Custom Slurm settings for AWS PCS queues

The following custom Slurm settings are supported at the queue level:

**Important**  
QOS values referenced in `AllowQos`, `DenyQos`, or `QOS` settings must already exist in the Slurm accounting database. Otherwise, Slurm might fail to apply the configuration. For more information about Slurm accounting, see [Slurm accounting in AWS PCS](slurm-accounting.md).
+ [AllowAccounts](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowAccounts)
+ [AllowQos](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowQoS)
+ [Default](https://slurm.schedmd.com/slurm.conf.html#OPT_Default)
+ [DefaultTime](https://slurm.schedmd.com/slurm.conf.html#OPT_DefaultTime)
+ [DenyAccounts](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyAccounts)
+ [DenyQos](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyQoS)
+ [Exclusive](https://slurm.schedmd.com/slurm.conf.html#OPT_Exclusive)
**Note**  
`Exclusive` replaces `ExclusiveUser` and `OverSubscribe=EXCLUSIVE`. `Exclusive=NODE` and `Exclusive=TOPO` imply `OverSubscribe=NO`.
+ [ExclusiveUser](https://slurm.schedmd.com/slurm.conf.html#OPT_ExclusiveUser)
**Note**  
Slurm deprecates `ExclusiveUser` from version 26.05 in favor of `Exclusive`. AWS PCS continues to support it, but we recommend that you migrate to `Exclusive`.
+ [GraceTime](https://slurm.schedmd.com/slurm.conf.html#OPT_GraceTime)
+ [MaxTime](https://slurm.schedmd.com/slurm.conf.html#OPT_MaxTime)
+ [OverSubscribe](https://slurm.schedmd.com/slurm.conf.html#OPT_OverSubscribe)
+ [OverTimeLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit)
+ [PowerDownOnIdle](https://slurm.schedmd.com/slurm.conf.html#OPT_PowerDownOnIdle)
+ [PreemptMode](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode)
+ [PriorityJobFactor](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityJobFactor)
+ [PriorityTier](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityTier)
+ [QOS](https://slurm.schedmd.com/slurm.conf.html#OPT_QOS)
+ [SelectTypeParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters_1)
**Note**  
AWS PCS supports the `CR_Core`, `CR_Core_Memory`, `CR_Socket`, and `CR_Socket_Memory` values. AWS PCS supports the `CR_Socket` and `CR_Socket_Memory` values on Slurm version 25.11 and later.  
Slurm uses the queue value only when the cluster-level `SelectTypeParameters` value is `CR_Core`, `CR_Core_Memory`, `CR_Socket`, or `CR_Socket_Memory`. If the cluster-level value is `CR_CPU` (the default) or `CR_CPU_Memory`, Slurm ignores the queue value.
+ [TRESBillingWeights](https://slurm.schedmd.com/slurm.conf.html#OPT_TRESBillingWeights)