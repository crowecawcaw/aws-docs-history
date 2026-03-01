AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# The Agentless Collector dashboard

On the Application Discovery Service Agentless Collector (Agentless Collector) dashboard page
you can see the status of the collector and choose a method of data collection as
described in the following topics.

###### Topics

- [Collector status](#using-collector-status "#using-collector-status")
- [Data collection](#using-collector-data-collect "#using-collector-data-collect")

## Collector status

**Collector status** gives you status information about the
collector. The collector name, the status of the collector's connection to AWS, the
Migration Hub home Region, and the version.

If you have AWS connection issues, you might need to edit
Agentless Collector configuration settings.

To edit the collector configuration settings, choose **Edit collector
settings** and follow the instructions described in [Editing Agentless Collector settings](agentless-collector-edit-configure.md "agentless-collector-edit-configure.md").

## Data collection

Under **Data collection** you can choose a data collection
method. Application Discovery Service Agentless Collector (Agentless Collector) currently
supports data collection from VMware VMs and from database and analytics servers.
Future modules will support collection from additional virtualization platforms, and
operating system level collection.

###### Topics

- [VMware vCenter data collection](#using-collector-data-collect-vcenter "#using-collector-data-collect-vcenter")
- [Database and analytics data collection](#using-collector-data-collect-database-analytics "#using-collector-data-collect-database-analytics")

### VMware vCenter data collection

To collect server inventory, profile, and utilization data from your VMware
VMs, set up connections to your vCenter servers. To set up the connections,
choose **Set up** in the **VMware vCenter**
section and follow the instructions described in [Using the VMware vCenter Agentless Collector data collection module](agentless-collector-gs-data-collection-vcenter.md "agentless-collector-gs-data-collection-vcenter.md").

After you set up vCenter data collection, from the dashboard you can perform
the following:

- View data collection status
- Start data collection
- Stop data collection

###### Note

On the dashboard page, after you set up vCenter data collection, the
**Set up** button in the **VMware
vCenter** section is replaced with data collection status
information, a **Stop data collection** button, and a
**View and edit** button.

### Database and analytics data collection

You can run your database and analytics data collection module in the
following two modes.

**Metadata and database capacity**

The data collection module collects such information as schemas,
versions, editions, CPU, memory, and disk capacity from your
database and analytics servers. You can use this collected
information to compute target recommendations in the AWS DMS console.
If your source database is overprovisioned or underprovisioned, then
the target recommendations also will be overprovisioned or
underprovisioned.

This is the default mode.

**Metadata, database capacity, and resource utilization**

In addition to metadata and database capacity information, the
data collection module collects actual utilization metrics of CPU,
memory, and disk capacity for the databases and analytics servers.
This mode provides more accurate target recommendations than the
default mode because the recommendations are based on the actual
database workloads. In this mode, the data collection module
collects performance metrics every minute.

###### To start collecting metadata and performance metrics from your database and analytics servers

1. On the **Database and analytics collector** page,
   choose **Data collection** in the navigation
   pane.
2. From the **Database inventory** list, select the
   database and analytics servers for which you want to collect metadata
   and performance metrics.
3. Choose **Run data collection**. The **Data
   collection type** dialog box opens.
4. Choose how to collect data for analysis.

If you choose the **Metadata, database capacity, and resource
utilization** option, then set the period of data
collection. You can collect data during the **Next 7
days** or set the **Custom range** of
1–60 days. 5. Choose **Run data collection**. The **Data
collection** page opens. 6. Choose the **Collection health** tab to see the
status of data collection.

After completing the data collection, your data collection module uploads
collected data to your Amazon S3 bucket. Then, you can view this collected data as
described in [Viewing your collected data](agentless-collector-gs-view-collected-data.md "agentless-collector-gs-view-collected-data.md").
