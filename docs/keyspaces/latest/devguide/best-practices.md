# Best practices for designing and architecting with Amazon Keyspaces (for Apache Cassandra)

Use this section to quickly find recommendations for maximizing performance and minimizing
throughput costs when working with Amazon Keyspaces.

###### Contents

- [Key differences and design principles of NoSQL design](bp-general-nosql-design.md "bp-general-nosql-design.md")
  - [Differences between relational data
    design and NoSQL](bp-general-nosql-design.md#bp-general-nosql-design-vs-relational "bp-general-nosql-design.md#bp-general-nosql-design-vs-relational")
  - [Two key concepts for NoSQL design](bp-general-nosql-design.md#bp-general-nosql-design-concepts "bp-general-nosql-design.md#bp-general-nosql-design-concepts")
  - [Approaching NoSQL design](bp-general-nosql-design.md#bp-general-nosql-design-approach "bp-general-nosql-design.md#bp-general-nosql-design-approach")

- [Optimize client driver connections for the serverless environment](connections.md "connections.md")
  - [How connections work in Amazon Keyspaces](connections.md#connections.howtheywork "connections.md#connections.howtheywork")
  - [How to configure connections in Amazon Keyspaces](connections.md#connections.howtoconfigure "connections.md#connections.howtoconfigure")
  - [How to configure the retry policy for connections in Amazon Keyspaces](connections.md#connections.retry-policies "connections.md#connections.retry-policies")
  - [How to configure connections over VPC endpoints in Amazon Keyspaces](connections.md#connections.VPCendpoints "connections.md#connections.VPCendpoints")
  - [How to monitor connections in Amazon Keyspaces](connections.md#connections.howtomonitor "connections.md#connections.howtomonitor")
  - [How to handle connection errors in Amazon Keyspaces](connections.md#connections.errorhandling "connections.md#connections.errorhandling")

- [Data modeling best practices: recommendations for designing data models](data-modeling.md "data-modeling.md")
  - [How to use partition keys effectively in Amazon Keyspaces](bp-partition-key-design.md "bp-partition-key-design.md")
    - [Use write sharding to evenly distribute workloads across partitions](bp-partition-key-sharding.md "bp-partition-key-sharding.md")
      - [Sharding using compound partition keys and random values](bp-partition-key-sharding.md#bp-partition-key-sharding-random "bp-partition-key-sharding.md#bp-partition-key-sharding-random")
      - [Sharding using compound partition keys and calculated values](bp-partition-key-sharding.md#bp-partition-key-sharding-calculated "bp-partition-key-sharding.md#bp-partition-key-sharding-calculated")

- [Optimizing costs of Amazon Keyspaces tables](bp-cost-optimization.md "bp-cost-optimization.md")
  - [Evaluate your costs at the table level](CostOptimization_TableLevelCostAnalysis.md "CostOptimization_TableLevelCostAnalysis.md")
    - [How to view the costs of a
      single Amazon Keyspaces table](CostOptimization_TableLevelCostAnalysis.md#CostOptimization_TableLevelCostAnalysis_ViewInfo "CostOptimization_TableLevelCostAnalysis.md#CostOptimization_TableLevelCostAnalysis_ViewInfo")
    - [Cost Explorer's default
      view](CostOptimization_TableLevelCostAnalysis.md#CostOptimization_TableLevelCostAnalysis_CostExplorer "CostOptimization_TableLevelCostAnalysis.md#CostOptimization_TableLevelCostAnalysis_CostExplorer")
    - [How to use and apply table
      tags in Cost Explorer](CostOptimization_TableLevelCostAnalysis.md#CostOptimization_TableLevelCostAnalysis_Tagging "CostOptimization_TableLevelCostAnalysis.md#CostOptimization_TableLevelCostAnalysis_Tagging")

  - [Evaluate your table's capacity mode](CostOptimization_TableCapacityMode.md "CostOptimization_TableCapacityMode.md")
    - [What table capacity modes are
      available](CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_Overview "CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_Overview")
    - [When to select on-demand
      capacity mode](CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_OnDemand "CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_OnDemand")
    - [When to select provisioned
      capacity mode](CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_Provisioned "CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_Provisioned")
    - [Additional factors to
      consider when choosing a table capacity mode](CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_AdditionalFactors "CostOptimization_TableCapacityMode.md#CostOptimization_TableCapacityMode_AdditionalFactors")

  - [Evaluate your table's Application Auto Scaling
    settings](CostOptimization_AutoScalingSettings.md "CostOptimization_AutoScalingSettings.md")
    - [Understanding
      your Application Auto Scaling settings](CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_UnderProvisionedTables "CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_UnderProvisionedTables")
    - [How to identify
      tables with low target utilization (<=50%)](CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_IdentifyLowUtilization "CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_IdentifyLowUtilization")
    - [How to address
      workloads with seasonal variance](CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_SeasonalVariance "CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_SeasonalVariance")
    - [How to address spiky
      workloads with unknown patterns](CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_UnknownPatterns "CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_UnknownPatterns")
    - [How to address workloads
      with linked applications](CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_BetweenRanges "CostOptimization_AutoScalingSettings.md#CostOptimization_AutoScalingSettings_BetweenRanges")

  - [Identify your unused resources to optimize costs in Amazon Keyspaces](CostOptimization_UnusedResources.md "CostOptimization_UnusedResources.md")
    - [How to identify unused
      resources](CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Identifying "CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Identifying")
    - [Identifying unused table
      resources](CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Tables "CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Tables")
    - [Cleaning up unused table
      resources](CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Tables_Cleanup "CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Tables_Cleanup")
    - [Cleaning up unused
      point-in-time recovery (PITR) backups](CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Backups "CostOptimization_UnusedResources.md#CostOptimization_UnusedResources_Backups")

  - [Evaluate your table usage patterns to optimize performance and cost](CostOptimization_TableUsagePatterns.md "CostOptimization_TableUsagePatterns.md")
    - [Perform fewer
      strongly-consistent read operations](CostOptimization_TableUsagePatterns.md#CostOptimization_TableUsagePatterns_StronglyConsistentReads "CostOptimization_TableUsagePatterns.md#CostOptimization_TableUsagePatterns_StronglyConsistentReads")
    - [Enable Time to Live (TTL)](CostOptimization_TableUsagePatterns.md#CostOptimization_TableUsagePatterns_TTL "CostOptimization_TableUsagePatterns.md#CostOptimization_TableUsagePatterns_TTL")

  - [Evaluate your provisioned capacity for
    right-sized provisioning](CostOptimization_RightSizedProvisioning.md "CostOptimization_RightSizedProvisioning.md")
    - [How to retrieve
      consumption metrics from your Amazon Keyspaces tables](CostOptimization_RightSizedProvisioning.md#CostOptimization_RightSizedProvisioning_ConsumptionMetrics "CostOptimization_RightSizedProvisioning.md#CostOptimization_RightSizedProvisioning_ConsumptionMetrics")
    - [How to
      identify under-provisioned Amazon Keyspaces tables](CostOptimization_RightSizedProvisioning.md#CostOptimization_RightSizedProvisioning_UnderProvisionedTables "CostOptimization_RightSizedProvisioning.md#CostOptimization_RightSizedProvisioning_UnderProvisionedTables")
    - [How to
      identify over-provisioned Amazon Keyspaces tables](CostOptimization_RightSizedProvisioning.md#CostOptimization_RightSizedProvisioning_OverProvisionedTables "CostOptimization_RightSizedProvisioning.md#CostOptimization_RightSizedProvisioning_OverProvisionedTables")
