# Custom Slurm settings for AWS PCS clusters

The following custom Slurm settings are supported at the cluster level:

- [AccountingStorageEnforce](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageEnforce "https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageEnforce")
- [AccountingStorageTRES](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageTRES "https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageTRES")
- [AccountingStoreFlags](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStoreFlags "https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStoreFlags")
- [AuthAltParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_AuthAltParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_AuthAltParameters")
- [CliFilterParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterParameters")

###### Note

For more information on CLI Filters in AWS PCS, see [Configure Slurm CLI Filter Plugins on an AWS PCS cluster](slurm-cli-filter-plugins-configure.md "slurm-cli-filter-plugins-configure.md").

- [CliFilterPlugins](https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterPlugins "https://slurm.schedmd.com/slurm.conf.html#OPT_CliFilterPlugins")

###### Note

For more information on CLI Filters in AWS PCS, see [Configure Slurm CLI Filter Plugins on an AWS PCS cluster](slurm-cli-filter-plugins-configure.md "slurm-cli-filter-plugins-configure.md").

- [CommunicationParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_CommunicationParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_CommunicationParameters")

###### Important

AWS PCS disables the HTTP endpoint by default. To enable it, specify `enable_http`.

- [DefMemPerCPU](https://slurm.schedmd.com/slurm.conf.html#OPT_DefMemPerCPU "https://slurm.schedmd.com/slurm.conf.html#OPT_DefMemPerCPU")
- [Epilog](https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1 "https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1")
- [EnforcePartLimits](https://slurm.schedmd.com/slurm.conf.html#OPT_EnforcePartLimits "https://slurm.schedmd.com/slurm.conf.html#OPT_EnforcePartLimits")
- [FairShareDampeningFactor](https://slurm.schedmd.com/slurm.conf.html#OPT_FairShareDampeningFactor "https://slurm.schedmd.com/slurm.conf.html#OPT_FairShareDampeningFactor")
- [FirstJobId](https://slurm.schedmd.com/slurm.conf.html#OPT_FirstJobId "https://slurm.schedmd.com/slurm.conf.html#OPT_FirstJobId")
- [HealthCheckInterval](https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckInterval "https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckInterval")
- [HealthCheckNodeState](https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckNodeState "https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckNodeState")
- [HealthCheckProgram](https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckProgram "https://slurm.schedmd.com/slurm.conf.html#OPT_HealthCheckProgram")
- [JobRequeue](https://slurm.schedmd.com/slurm.conf.html#OPT_JobRequeue "https://slurm.schedmd.com/slurm.conf.html#OPT_JobRequeue")
- [LaunchParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_LaunchParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_LaunchParameters")
- [Licenses](https://slurm.schedmd.com/slurm.conf.html#OPT_Licenses "https://slurm.schedmd.com/slurm.conf.html#OPT_Licenses")
- [MetricsType](https://slurm.schedmd.com/slurm.conf.html#OPT_MetricsType "https://slurm.schedmd.com/slurm.conf.html#OPT_MetricsType")

###### Note

For more information on Metrics in AWS PCS, see [Slurm metrics in AWS PCS](slurm-metrics.md "slurm-metrics.md").

- [MinJobAge](https://slurm.schedmd.com/slurm.conf.html#OPT_MinJobAge "https://slurm.schedmd.com/slurm.conf.html#OPT_MinJobAge")

###### Note

AWS PCS supports a minimum value of 5 seconds for `MinJobAge`.

- [OverTimeLimit](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit "https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit")
- [PreemptExemptTime](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptExemptTime "https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptExemptTime")
- [PreemptMode](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode "https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode")
- [PreemptParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptParameters")
- [PreemptType](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptType "https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptType")
- [PriorityCalcPeriod](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityCalcPeriod "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityCalcPeriod")
- [PriorityDecayHalfLife](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityDecayHalfLife "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityDecayHalfLife")
- [PriorityFavorSmall](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFavorSmall "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFavorSmall")
- [PriorityFlags](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFlags "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFlags")
- [PriorityMaxAge](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityMaxAge "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityMaxAge")
- [PriorityUsageResetPeriod](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityUsageResetPeriod "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityUsageResetPeriod")
- [PriorityWeightAge](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAge "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAge")
- [PriorityWeightAssoc](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAssoc "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightAssoc")
- [PriorityWeightFairshare](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightFairshare "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightFairshare")
- [PriorityWeightJobSize](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightJobSize "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightJobSize")
- [PriorityWeightPartition](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightPartition "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightPartition")
- [PriorityWeightQOS](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightQOS "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightQOS")
- [PriorityWeightTRES](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightTRES "https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityWeightTRES")
- [Prolog](https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1 "https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1")
- [PrologFlags](https://slurm.schedmd.com/slurm.conf.html#OPT_PrologFlags "https://slurm.schedmd.com/slurm.conf.html#OPT_PrologFlags")
- [RequeueExit](https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExit "https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExit")
- [RequeueExitHold](https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExitHold "https://slurm.schedmd.com/slurm.conf.html#OPT_RequeueExitHold")
- [SchedulerParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_SchedulerParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_SchedulerParameters")
- [SelectTypeParameters](https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters "https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters")

###### Note

AWS PCS supports the `CR_Socket` and `CR_Socket_Memory` values on Slurm version 25.11 and later.

- [SrunPortRange](https://slurm.schedmd.com/slurm.conf.html#OPT_SrunPortRange "https://slurm.schedmd.com/slurm.conf.html#OPT_SrunPortRange")
- [TaskEpilog](https://slurm.schedmd.com/slurm.conf.html#OPT_TaskEpilog "https://slurm.schedmd.com/slurm.conf.html#OPT_TaskEpilog")
- [TaskPluginParam](https://slurm.schedmd.com/slurm.conf.html#OPT_TaskPluginParam "https://slurm.schedmd.com/slurm.conf.html#OPT_TaskPluginParam")
- [TaskProlog](https://slurm.schedmd.com/slurm.conf.html#OPT_TaskProlog "https://slurm.schedmd.com/slurm.conf.html#OPT_TaskProlog")
- [TrackWCKey](https://slurm.schedmd.com/slurm.conf.html#OPT_TrackWCKey "https://slurm.schedmd.com/slurm.conf.html#OPT_TrackWCKey")
- [UnkillableStepProgram](https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepProgram "https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepProgram")
- [UnkillableStepTimeout](https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepTimeout "https://slurm.schedmd.com/slurm.conf.html#OPT_UnkillableStepTimeout")
