# Improving query performance using adaptive

join

## Overview

Adaptive join is a preview feature in Aurora PostgreSQL 17.4 that helps improve query
performance. This feature is disabled by default, but you can enable it using Global User
Configuration (GUC) parameters. Since this is a preview feature, the default parameter
values might change. When enabled, adaptive join helps optimize query performance by
dynamically switching from a nested loop join to a hash join at runtime. This switch
occurs when the PostgreSQL optimizer has incorrectly chosen a nested loop join due to
inaccurate cardinality estimates.

## Configuring adaptive join

You can control adaptive join using these three GUC parameters:

| Adaptive join configuration parameters | GUC parameter                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                       | Default and configuration options |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| apg_adaptive_join_crossover_multiplier | This multiplier works with the \*row crossover point<br>• to determine when to switch from a nested loop to a hash join.<br>The row crossover point is where the SQL optimizer estimates that nested loop and hash join operations have equal cost.<br>A higher multiplier value reduces the likelihood of adaptive join switching to a hash join.           | Controls whether Adaptive Join is enabled<br>• Default value: -1 (disabled)<br>• Valid range: -1 to DBL_MAX<br>• To enable: Set to >= 1                                                                                                                                                                                                           |
| apg_adaptive_join_cost_threshold       | This parameter sets a minimum query cost threshold. Adaptive join automatically disables itself for queries below this threshold. This prevents performance overhead<br>in simple queries where the cost of planning an adaptive join could exceed the benefits of switching from nested loop to hash join.                                                  | Sets minimum cost threshold for the query<br>• Default value: 100<br>• Valid range: 0 to DBL_MAX                                                                                                                                                                                                                                                  |
| apg_enable_parameterized_adaptive_join | This parameter extends adaptive join functionality to parameterized nested loop joins when enabled. By default, adaptive join works only with unparameterized nested loop joins,<br>as these are more likely to benefit from switching to hash join. Parameterized nested loop joins typically perform better, making the switch to hash join less critical. | Controls adaptive join behavior for nested loop joins<br>• Default value: false<br>• Valid values: true/false<br>+ When false: Works only with unparameterized nested loop joins<br>+ When true: Works with both parameterized and unparameterized nested loop joins<br>NoteRequires `apg_adaptive_join_crossover_multiplier` to be enabled first |
