

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review alerts on source servers in a wave
<a name="wave-source-server-migration-metrics-alerts"></a>

The source server **Alerts** metric provides an aggregated overview of the alerts related to the wave's associated servers. You can look up an individual source server **Alerts** status in the **Source servers** table.

![Pie chart showing server alerts: 2 servers healthy (66.7%), 1 server launched (33.3%).](http://docs.aws.amazon.com/mgn/latest/ug/images/app-7.png)

+ A healthy server for which a test or cutover instance has not been launched will display a **Healthy** status. 
+ A healthy server for which a test or cutover instance has been launched will display a **Healthy** status. 
+ A server that is experiencing a temporary issue such as a lag or backlog will display a **Lagging** status. 
+ A server that is experiencing significant issues, such as a stall, will display a **Stalled** status. 