

# Amazon EMR 7.7.0 - Tez release notes
<a name="Tez-release-history-770"></a>

## Amazon EMR 7.7.0 - Tez changes
<a name="Tez-release-history-changes-770"></a>


| Type | Description | 
| --- | --- | 
| Improvement | The tez.task.relaxed.locality property in Apache Tez controls whether task scheduling strictly follows data locality constraints (rack and node locality). When set to true (default in EMR-7.6\+), Tez does not enforce locality, allowing tasks to be assigned to any available container, which improves resource utilization and reduces wait times in busy clusters. | 