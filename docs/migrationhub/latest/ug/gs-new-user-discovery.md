AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Discover on-premises resources using AWS Migration Hub

discovery tools

AWS Migration Hub (Migration Hub) provides a single place to discover your existing servers, plan
migrations, and track the status of each application migration. Before migrating you can
discover information about your on-premises server and application resources to help you
build a business case for migrating or to build a migration plan.

Discovering your servers first is an optional starting point for migrations, gathering
detailed server information, and then grouping the discovered servers into applications to
be migrated and tracked. Migration Hub also gives you the choice to start migrating right away and
to group servers during migration.

You get the data about your servers and applications into the AWS Migration Hub console by using
the following discovery tools.

- **Application Discovery Service Agentless Collector** –
  Agentless Collector is an on-premises application that collects information
  through agentless methods about your on-premises environment, including server
  profile information (for example, OS, number of CPUs, amount of RAM), database
  metadata (for example, version, edition, numbers of tables and schemas), and server
  utilization metrics. You install the Agentless Collector as a virtual
  machine (VM) in your VMware vCenter Server environment using an Open Virtualization
  Archive (OVA) file. For more information, see [Agentless Collector](../../../application-discovery/latest/userguide/agentless-collector-gs.md "../../../application-discovery/latest/userguide/agentless-collector-gs.md") in the
  _Application Discovery Service User Guide_.
- **AWS Application Discovery Agent** – The Discovery Agent is AWS
  software that you install on your on-premises servers and VMs to capture system
  configuration, system performance, running processes, and details of the network
  connections between systems. Agents support most Linux and Windows operating
  systems, and you can deploy them on physical on-premises servers, Amazon EC2 instances,
  and virtual machines. For more information, see [AWS Application Discovery Agent](../../../application-discovery/latest/userguide/discovery-agent.md "../../../application-discovery/latest/userguide/discovery-agent.md") in the
  _Application Discovery Service User Guide_.
- **Migration Evaluator Collector** – Migration Evaluator is a
  migration assessment service that helps you create a directional business case for
  AWS cloud planning and migration. The information that the Migration Evaluator
  collects includes server profile information (for example, OS, number of CPUs,
  amount of RAM), SQL Server metadata (for example, version and edition), utilization
  metrics, and network connections. For more information, see [Migration Evaluator](https://aws.amazon.com/migration-evaluator/ "https://aws.amazon.com/migration-evaluator/").
- **Migration Hub import** – With Migration Hub import, you can
  import information about your on-premises servers and applications into Migration Hub,
  including server specifications and utilization data. You can also use this data to
  track the status of application migrations. For more information, see [Migration Hub
  import](../../../application-discovery/latest/userguide/discovery-import.md "../../../application-discovery/latest/userguide/discovery-import.md") in the _Application Discovery Service User Guide_.

###### Topics

- [Step 1: Choose an AWS discovery tool](#gs-discovery-tools "#gs-discovery-tools")
- [Step 2: View server details and
  dependencies](#gs-discovery-view-servers "#gs-discovery-view-servers")
- [Step 3: Group servers as
  applications](#gs-discovery-group-as-applications "#gs-discovery-group-as-applications")

## Step 1: Choose an AWS discovery tool

You get the data about your servers and applications into the AWS Migration Hub console by
using the AWS discovery tools.

###### To use the discovery tools

1. In the Migration Hub console navigation pane, choose **Discover**
   and then choose **Tools**.
2. On the **Discovery Tools** page, you can choose to import
   data, download the Agentless Collector or a Discovery Agent, or you can choose
   to use the Migration Evaluator Collector.

To help you decide which tool to use, choose **Compare AWS discovery
tools**. The following topics provide information about how to use each of
the discovery tools:

- [Discovery using
  Agentless Collector](#gs-agentless-collector "#gs-agentless-collector")
- [Discovery using the AWS Application Discovery Agent](#gs-discovery-agent "#gs-discovery-agent")
- [Discovery using Migration Evaluator Collector](#gs-me-collector "#gs-me-collector")
- [Using Migration Hub import](#gs-import "#gs-import")

### Discovery using

Agentless Collector

The following procedure describes the discovery process using
Agentless Collector for collecting data about your on-premises
resources.

###### To discover resources using the Agentless Collector

1. In the Migration Hub console navigation pane, under
   **Discover**, choose **Tools**, and
   then choose **Download collector** on the
   **Agentless Collector** card.
2. Following the instructions in [Getting started with Agentless Collector](../../../application-discovery/latest/userguide/agentless-collector-gs.md "../../../application-discovery/latest/userguide/agentless-collector-gs.md") in the
   _Application Discovery Service User Guide_.

### Discovery using the AWS Application Discovery Agent

The following procedure describes the discovery process for collecting data about
your on-premises resources using an AWS Application Discovery Agent.

You can install Discovery Agent agents on both your VMs and physical servers to not only
discover your on-premises servers, but also to capture technical specifications,
system performance, network dependencies, and to process information. Network
dependency and process information is available, but only for export. Use the
Application Discovery Service CLI to export the data and analyze it outside of the Migration Hub. For more
information, see [describe-export-tasks](../../../cli/latest/reference/discovery/describe-export-tasks.md "../../../cli/latest/reference/discovery/describe-export-tasks.md").

The beneﬁt of using Discovery Agent is that it provides more detailed information than
using Application Discovery Service Agentless Collector(Agentless Collector). This
information includes system performance and resource utilization. By contrast, the
beneﬁt of using Agentless Collector is that it provides a more efficient
and faster on-premises infrastructure assessment.

###### To discover resources using an agent

1. In the Migration Hub console navigation pane, under
   **Discover**, choose **Tools**, and
   then choose **Download agent** on the **AWS
   Discovery Agent** card.
2. In the **Download agent** dropdown list, choose one of
   the download options.
3. Deploy and configure the agent by following the instructions in [AWS Application Discovery Agent](../../../application-discovery/latest/userguide/discovery-agent.md "../../../application-discovery/latest/userguide/discovery-agent.md") in the _AWS Application Discovery Service User
   Guide_.
4. After you have successfully installed the agent, return to the in the
   Migration Hub console navigation pane, under **Discover** choose
   **Data Collectors**. Then, refresh your internet
   browser.
5. On the **Agents** tab, select the agent(s) that you want
   to start.
6. Choose **Start data collection**.

To install additional agents, repeat the procedure.

### Discovery using Migration Evaluator Collector

The following procedure describes the discovery process using Migration Evaluator Collector for
collecting data about your on-premises resources.

###### To discover resources using Migration Evaluator Collector

1. In the Migration Hub console navigation pane, under
   **Discover**, choose **Tools**, and
   then choose **Request assessment** on the
   **Migration Evaluator Collector** card.
2. Following the instructions in [Getting started with
   Migration Evaluator](https://aws.amazon.com/migration-evaluator/getting-started/ "https://aws.amazon.com/migration-evaluator/getting-started/").

### Using Migration Hub import

If you have already performed discovery using an AWS Migration Partner discovery
tool or have existing data from data sources such as a Configuration Management
Database (CMDB) or IT Asset Management System (ITAM), you can use Migration Hub import to
upload this data. For more information, see [Migration Hub
Import](../../../application-discovery/latest/userguide/discovery-import.md "../../../application-discovery/latest/userguide/discovery-import.md") in the _Application Discovery Service User Guide_.

## Step 2: View server details and

dependencies

The following procedures describe how to view detailed information about servers
discovered with AWS discovery tools.

### Viewing server details

The following procedure describes how to view information about the servers
discovered by using any of the AWS discovery tools.

###### To view details about a discovered server

1. In the navigation pane, under **Discover**, choose
   **Servers**.
2. To view details about the server, choose the hostname of the server from
   the **Server info** column. The server's detail page
   displays information about the server, such as hostname, IP address,
   performance metrics, and so on.

### Exploring server network

connections

If you use AWS Application Discovery Agent or Migration Evaluator Collector for discovery, you can explore server
network connections by using the network diagram in AWS Migration Hub.

Start exploring by choosing a single server or by choosing multiple servers at the
same time. Use the network diagram to explore your discovered servers and their
connections to help you decide on how to group them together to assist in your
migration planning.

###### To explore network connections starting with a single server

1. In the navigation pane, under **Discover**, choose
   **Servers**.
2. To view details about the server, choose the hostname of the server from
   the **Server info** column. The server's detail page
   displays information about the server, such as hostname, IP address,
   performance metrics, and so on.
3. Choose **Network**. The icon for the server you choose is
   centered in the network diagram. Connections fan out from the center server
   to servers that are directly connected to the server you choose.
4. Choose a server icon to see details about the server. For information
   about how to work with the network diagram, see [Viewing network connections in AWS Migration Hub](network-diagram.md "network-diagram.md").

###### To explore network connections starting with multiple servers

1. In the navigation pane, under **Discover**, choose
   **Servers**.
2. To see the network connections for multiple servers, select the check box
   for each of the servers you want in the network diagram, and then choose
   **Visualize network**.
3. You can modify the network diagram for the servers you chose. For
   information on how to work with the network diagram, see [Viewing network connections in AWS Migration Hub](network-diagram.md "network-diagram.md").

## Step 3: Group servers as

applications

The following procedures describe how to group servers as applications. Because
applications can have multiple servers, it can help simplify migration tracking to group
them into logical units.

### Grouping servers as

applications from the servers list

The following procedure shows you how to select the servers you want to group for
your application, how to create your application and name it, and how to add
identifying tags.

###### Tip

You can import application groups in bulk using the AWS CLI for Application Discovery Service and
calling the `CreateApplication` API. For more information, see [CreateApplication](../../../application-discovery/latest/APIReference/API_CreateApplication.md "../../../application-discovery/latest/APIReference/API_CreateApplication.md") in the
_Application Discovery Service API Reference_.

###### To group servers into a new or existing application from the servers

list

1. In the navigation pane, choose **Servers**.
2. In the servers list, select the check box for each of the servers that you
   want to group into a new or existing application.
   1. You can also search and filter on any of the criteria specified in
      the headers of the server list. In the search box choose an item
      from the dropdown, then choose an operator from the next dropdown,
      and then type in your criteria.
   2. Optionally, for each selected server, you can add a descriptive
      tag by choosing **Add tag** from the
      **Actions** menu. Doing so shows a dialog box
      where you can type a value for **Key**, and
      optionally a value for **Value**.

3. To create your application, or add to an existing one, choose
   **Group as application**.
4. In the **Group as application** dialog box, choose either
   **Group as a new application** or **Add to an
   existing application**.
   1. If you chose **Group as a new application**, type
      a name in the **Application name** field.
      Optionally, you can type a description in the **Application
      description** field.
   2. If you chose **Add to an existing application**,
      choose an application from the **Choose existing
      application** dropdown menu.

5. Choose **Group**.

### Grouping servers as

applications from the network diagram

You must select the servers in the network diagram that you want to group into a
new or existing application.

The following procedure shows you how to select the servers you want to group for
your application from the network diagram, how to create your application and name
it, and how to add identifying tags.

###### To group servers into a new or existing application from the network

diagram

1.  Set up a network diagram following one of the procedures in the [Exploring server network
    connections](#gs-discovery-view-servers-network "#gs-discovery-view-servers-network") section.
2.  You can use the following options to select servers from the network
    diagram:

        * Choose a server node icon. Details about the server show in the
         server details pane, where you choose **Select
         server**.
        * Open the context (right-click) menu on the server node icon, and
         then choose **Select server**.
        * Choose **Select all** to select all the servers
         for grouping that are in your diagram. Only the servers with the
         Discovery Agent running on them or are being monitored by the Migration Evaluator Collector
         can be selected.
        * Hold **shift** to select multiple servers at the
         same time.

    Selected servers are shown in a list in the same pane as the server
    details. You can toggle back and forth between the server details view and
    the selected server list view by choosing the server icon.

3.  After you select one or more servers, create your application, or add to
    an existing one, by choosing **Group as
    application**.
4.  In the **Group as application** dialog box, choose either
    **Group as a new application** or **Add to an
    existing application**.
    1. If you chose **Group as a new application**, type
       a name in the **Application name** field. The
       servers that are members of the group are labeled on the diagram
       with the application name.

    Optionally, you can type a description for **Application
    description**. 2. If you chose **Add to an existing application**,
    choose an application from the **Choose existing
    application** dropdown menu.

5.  Choose **Group**.
6.  Optionally, you can add a descriptive tag to the selected servers by
    choosing **Add tag** from the **Actions**
    menu. Doing so shows a dialog box where you can type a value for
    **Key**, and optionally a value for
    **Value**.
