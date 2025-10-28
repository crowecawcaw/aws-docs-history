# Best practice 16.3 – Identify

performance trends using data

After baselines for performance are established, system administrators must monitor
trends over time to see if KPIs remain stable within preferred norms. If the performance
data indicates a trend toward unacceptable values of the KPI, system administrators can
then take steps to avoid or mitigate performance impacts.

**Suggestion 16.3.1 – Conduct regular reviews of SAP system
performance**

Periodic reviews of KPIs by system administrators can help identify trends in
performance-related data as well as determine which alerts might be most beneficial. These
alerts can then be used to automate notifications should the trend continue as well as put
in place auto-remediation measures to address the potential performance issue (for
example, dynamically changing SAP parameters in response to performance indicators).
Examples of KPIs and related trends can be found in SAP EarlyWatch Alert reports, which in
some cases can be customized with additional useful metrics. SAP service level reporting
can also be useful if you have Service Level Agreements (SLAs) in place for your SAP
workloads.

- SAP Documentation: [Service Level
  Reporting](http://support.sap.com/slr "http://support.sap.com/slr")
- SAP Note: [1040343

* SAP EarlyWatch Alert](https://launchpad.support.sap.com/#/notes/1040343 "https://launchpad.support.sap.com/#/notes/1040343") [Requires SAP Portal Access]

- SAP Note: [1829914

* Customize EWA Reports](https://launchpad.support.sap.com/#/notes/1829914 "https://launchpad.support.sap.com/#/notes/1829914") [Requires SAP Portal Access]

**Suggestion 16.3.2 – Retain historical data to identify
trends**

You should retain performance data and associated logs for a predetermined period of
time to understand trends in system behavior. Performance tuning of any SAP system will
depend on the ability to look back over historical periods of days, weeks, and months to
understand what constitutes a performance trend or cyclical performance event. Common
events that require retention of data to observe performance impacts include:

- Month-end and year-end financial processing
- Increased reporting requirements around business milestones (for example, after a
  large semi-annual sales kick-off)
- On-boarding of a large new SAP user population within the business
- Technology changes, such as infrastructure sizing, database patches, operating
  system version updates, or SAP software upgrades
