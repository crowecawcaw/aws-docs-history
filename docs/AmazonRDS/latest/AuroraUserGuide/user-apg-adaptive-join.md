

# Improving query performance using adaptive join
<a name="user-apg-adaptive-join"></a>

## Overview
<a name="user-apg-adaptive-join-intro"></a>

Adaptive join is a preview feature in Aurora PostgreSQL 17.4 that helps improve query performance. This feature is disabled by default, but you can enable it using Global User Configuration (GUC) parameters. Since this is a preview feature, the default parameter values might change. When enabled, adaptive join helps optimize query performance by dynamically switching from a nested loop join to a hash join at runtime. This switch occurs when the PostgreSQL optimizer has incorrectly chosen a nested loop join due to inaccurate cardinality estimates.

## Configuring adaptive join
<a name="user-apg-adaptive-join-config"></a>

You can control adaptive join using these three GUC parameters:


**Adaptive join configuration parameters**  

| GUC parameter | Description | Default and configuration options | 
| --- | --- | --- | 
| apg\_adaptive\_join\_crossover\_multiplier | This multiplier works with the row crossover point to determine when to switch from a nested loop to a hash join. The row crossover point is where the SQL optimizer estimates that nested loop and hash join operations have equal cost. A higher multiplier value reduces the likelihood of adaptive join switching to a hash join. | Controls whether Adaptive Join is enabled+  Default value: -1 (disabled) <br />+  Valid range: -1 to DBL\_MAX <br />+  To enable: Set to >= 1  | 
| apg\_adaptive\_join\_cost\_threshold | This parameter sets a minimum query cost threshold. Adaptive join automatically disables itself for queries below this threshold. This prevents performance overhead in simple queries where the cost of planning an adaptive join could exceed the benefits of switching from nested loop to hash join. |  +  Default value: 100 <br />+  Valid range: 0 to DBL\_MAX   | 
| apg\_enable\_parameterized\_adaptive\_join | This parameter extends adaptive join functionality to parameterized nested loop joins when enabled. By default, adaptive join works only with unparameterized nested loop joins, as these are more likely to benefit from switching to hash join. Parameterized nested loop joins typically perform better, making the switch to hash join less critical. |  +  Default value: false <br />+  Valid values: true/false  When false: Works only with unparameterized nested loop joins When true: Works with both parameterized and unparameterized nested loop joins   Requires `apg_adaptive_join_crossover_multiplier` to be enabled first  | 