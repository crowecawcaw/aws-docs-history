

# Measuring network latency
<a name="hpn-measuring-latency"></a>

To measure and validate network latency between your Amazon EC2 instances and Oracle Database@AWS databases, we recommend using **sockperf**, an open-source TCP-level latency measurement tool. sockperf provides complementary network metrics that help you:
+ Establish network performance baselines
+ Compare performance before and after infrastructure changes
+ Validate that sub-millisecond latency targets are being met

You can also use Oracle database performance tools such as [**Automatic Workload Repository (AWR)**](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/sagug/awr.html), [**Active Session History (ASH)**](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgdba/ash-report-ui.html), and [**SQL Trace**](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgsql/performing-application-tracing.html#GUID-31EF2BD5-28DB-488F-A855-8DA324F6970B) for database-level performance analysis.