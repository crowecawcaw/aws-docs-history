# Performance Insights for counter metrics

Counter metrics are operating system metrics in the Performance Insights dashboard. To
help identify and analyze performance problems, you can correlate counter metrics with
DB load.

## Performance Insights operating system counters

The following operating system counters are available with Amazon DocumentDB Performance
Insights.

| Counter    | Type              | Metric                       |
| ---------- | ----------------- | ---------------------------- |
| active     | memory            | os.memory.active             |
| buffers    | memory            | os.memory.buffers            |
| cached     | memory            | os.memory.cached             |
| dirty      | memory            | os.memory.dirty              |
| free       | memory            | os.memory.free               |
| inactive   | memory            | os.memory.inactive           |
| mapped     | memory            | os.memory.mapped             |
| pageTables | memory            | os.memory.pageTables         |
| slab       | memory            | os.memory.slab               |
| total      | memory            | os.memory.total              |
| writeback  | memory            | os.memory.writeback          |
| idle       | cpuUtilization    | os.cpuUtilization.idle       |
| system     | cpuUtilization    | os.cpuUtilization.system     |
| total      | cpuUtilization    | os.cpuUtilization.total      |
| user       | cpuUtilization    | os.cpuUtilization.user       |
| wait       | cpuUtilization    | os.cpuUtilization.wait       |
| one        | loadAverageMinute | os.loadAverageMinute.one     |
| fifteen    | loadAverageMinute | os.loadAverageMinute.fifteen |
| five       | loadAverageMinute | os.loadAverageMinute.five    |
| cached     | swap              | os.swap.cached               |
| free       | swap              | os.swap.free                 |
| in         | swap              | os.swap.in                   |
| out        | swap              | os.swap.out                  |
| total      | swap              | os.swap.total                |
| rx         | network           | os.network.rx                |
| tx         | network           | os.network.tx                |
| numVCPUs   | general           | os.general.numVCPUs          |
