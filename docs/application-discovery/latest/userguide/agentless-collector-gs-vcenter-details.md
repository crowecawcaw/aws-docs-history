AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Viewing VMware data collection

details

The **VMware data collection details** page shows details about the
vCenter you set up in [Setting up the
Agentless Collector data collection module for VMware vCenter](agentless-collector-gs-vcenter.md "agentless-collector-gs-vcenter.md").

Under **Discovered vCenter servers**, the vCenter you set up is
listed with the following information about the vCenter:

- The IP address of the vCenter server.
- The number of servers in the vCenter.
- The status of the data collection.
- How long since the last update.
  Choose **Remove vCenter server** to remove the displayed vCenter
  server and return you to the **Set up VMware vCenter data collection**
  page.

If you did not choose to start data collection automatically, you can start data
collection by using the **Start data collection** button on this page.
After data collection starts, the start button changes to **Stop data
collection**.

If the **Collection status** column shows
**Collecting**, data collection has started.

You view the collected data in the AWS Migration Hub console. If you’re collecting data for
a VMware vCenter server inventory, you can access data that appears in the console
approximately 15 minutes after turning on data collection.

You can choose **View servers in Migration Hub** on this page to open the
Migration Hub console, if your access to the internet is not blocked. Whether you choose this
button or not, for information about how to access the Migration Hub console, see [Viewing your collected
data](agentless-collector-gs-view-collected-data.md "agentless-collector-gs-view-collected-data.md").

The following are the guidelines for recommended length of data collection according
to migration planning activities:

- TCO (total cost of ownership) - 2 to 4 weeks
- Migration planning - 2 to 6 weeks
