

# Amazon EMR 7.6.0 - Tez release notes
<a name="Tez-release-history-760"></a>

## Amazon EMR 7.6.0 - Tez changes
<a name="Tez-release-history-changes-760"></a>


| Type | Description | 
| --- | --- | 
| Improvement | Rack and node locality constraints won't be considered while requesting container for a task by changing default of tez.task.relaxed.locality to false | 
| Improvement | Tune configs to disable delay due to locality and allow non-local fallback | 
| Improvement | [TEZ-4547](https://issues.apache.org/jira/browse/TEZ-4547): Add Tez AM JobID to the JobConf | 