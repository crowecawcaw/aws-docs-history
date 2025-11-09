# Amazon EMR 7.7.0 - Tez

release notes

## Amazon EMR 7.7.0 -

Tez changes

| Type        | Description                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Improvement | The `tez.task.relaxed.locality` property in Apache Tez controls whether task scheduling strictly follows data locality<br>constraints (rack and node locality). When set to `true` (default in EMR-7.6+), Tez does not enforce locality, allowing tasks to be<br>assigned to any available container, which improves resource utilization and reduces wait times in busy clusters. |
