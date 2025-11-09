# Step 6: Review configuration settings for the Amazon EMR cluster

Configuration settings specify details about how a cluster runs, such as how many times to retry a task and how much memory is available for sorting. When you launch a cluster using Amazon EMR, there are Amazon EMR-specific settings in addition to the standard Hadoop configuration settings. The configuration settings are stored on the master node of the cluster. You can check the configuration settings to ensure that your cluster has the resources it requires to run efficiently.

Amazon EMR defines default Hadoop configuration settings that it uses to launch a cluster. The values are based on the AMI and the instance type you specify for the cluster. You can modify the configuration settings from the default values using a bootstrap action or by specifying new values in job execution parameters. For more information, see [Create bootstrap actions to install additional
software with an Amazon EMR cluster](emr-plan-bootstrap.md "emr-plan-bootstrap.md"). To determine whether a bootstrap action changed the configuration settings, check the bootstrap action logs.

Amazon EMR logs the Hadoop settings used to execute each job. The log data is stored in a file named `job_`job-id`_conf.xml` under the `/mnt/var/log/hadoop/history/` directory of the master node, where `job-id` is replaced by the identifier of the job. If you've enabled log archiving, this data is copied to Amazon S3 in the `logs/`date`/`jobflow-id`/jobs` folder, where `date` is the date the job ran, and `jobflow-id` is the identifier of the cluster.

The following Hadoop job configuration settings are especially useful for investigating performance issues. For more information about the Hadoop configuration settings and how they affect the behavior of Hadoop, go to [http://hadoop.apache.org/docs/](http://hadoop.apache.org/docs/ "http://hadoop.apache.org/docs/").

###### Warning

1. Setting `dfs.replication` to 1 on clusters with fewer than
   four nodes can lead to HDFS data loss if a single node goes down. We
   recommend you use a cluster with at least four core nodes for production
   workloads.
2. Amazon EMR will not allow clusters to scale core nodes below
   `dfs.replication`. For example, if `dfs.replication
= 2`, the minimum number of core nodes is 2.
3. When you use Managed Scaling, Auto-scaling, or choose to manually resize
   your cluster, we recommend that you to set `dfs.replication` to 2 or
   higher.

| Configuration setting                     | Description                                                                                                                                                                                                                                   |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dfs.replication                           | The number of HDFS nodes to which a single block (like the hard drive<br>block) is copied to in order to produce a RAID-like environment.<br>Determines the number of HDFS nodes which contain a copy of the<br>block.                        |
| io.sort.mb                                | Total memory available for sorting. This value should be 10x<br>io.sort.factor. This setting can also be used to calculate total memory<br>used by task node by figuring io.sort.mb multiplied by<br>mapred.tasktracker.ap.tasks.maximum.     |
| io.sort.spill.percent                     | Used during sort, at which point the disk will start to be used<br>because the allotted sort memory is getting full.                                                                                                                          |
| mapred.child.java.opts                    | Deprecated. Use mapred.map.child.java.opts and<br>mapred.reduce.child.java.opts instead. The Java options TaskTracker uses<br>when launching a JVM for a task to execute within. A common parameter is<br>"-Xmx" for setting max memory size. |
| mapred.map.child.java.opts                | The Java options TaskTracker uses when launching a JVM for a map task<br>to execute within. A common parameter is "-Xmx" for setting max memory<br>heap size.                                                                                 |
| mapred.map.tasks.speculative.execution    | Determines whether map task attempts of the same task may be launched<br>in parallel.                                                                                                                                                         |
| mapred.reduce.tasks.speculative.execution | Determines whether reduce task attempts of the same task may be<br>launched in parallel.                                                                                                                                                      |
| mapred.map.max.attempts                   | The maximum number of times a map task can be attempted. If all fail,<br>then the map task is marked as failed.                                                                                                                               |
| mapred.reduce.child.java.opts             | The Java options TaskTracker uses when launching a JVM for a reduce<br>task to execute within. A common parameter is "-Xmx" for setting max<br>memory heap size.                                                                              |
| mapred.reduce.max.attempts                | The maximum number of times a reduce task can be attempted. If all<br>fail, then the map task is marked as failed.                                                                                                                            |
| mapred.reduce.slowstart.completed.maps    | The amount of maps tasks that should complete before reduce tasks are<br>attempted. Not waiting long enough may cause "Too many fetch-failure"<br>errors in attempts.                                                                         |
| mapred.reuse.jvm.num.tasks                | A task runs within a single JVM. Specifies how many tasks may reuse<br>the same JVM.                                                                                                                                                          |
| mapred.tasktracker.map.tasks.maximum      | The max amount of tasks that can execute in parallel per task node<br>during mapping.                                                                                                                                                         |
| mapred.tasktracker.reduce.tasks.maximum   | The max amount of tasks that can execute in parallel per task node<br>during reducing.                                                                                                                                                        |

If your cluster tasks are memory-intensive, you can enhance performance by using fewer tasks per core node and reducing your job tracker heap size.
