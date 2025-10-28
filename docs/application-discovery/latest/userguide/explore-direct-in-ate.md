AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Exploring data directly in Amazon Athena

After you turn on data exploration in Amazon Athena, you can begin exploring and working
with detailed current data that was discovered by your agents by querying the data
directly in Athena. You can use the data to generate spreadsheets, run a cost analysis,
port the query to a visualization program to diagram network dependencies, and
more.

The following instructions explain how to explore your agent data directly in the
Athena console. If you don’t have any data in Athena or have not enabled data exploration
in Amazon Athena, you will be prompted by a dialog box to enable data exploration in
Amazon Athena , as explained in [Turning on data exploration in Amazon Athena](ce-prep-agents.md "ce-prep-agents.md").

###### To explore agent-discovered data directly in Athena

1. In the AWS Migration Hub console, choose **Servers** in the
   navigation pane.
2. To open the Amazon Athena console, choose **Explore data in
   Amazon Athena**.
3. On the **Query Editor** page, in the navigation pane under
   **Database**, make sure that
   **application_discovery_service_database** is
   selected.

###### Note

Under **Tables** the following tables represent the
datasets grouped by the agents.

    * **os\_info\_agent**
    * **network\_interface\_agent**
    * **sys\_performance\_agent**
    * **processes\_agent**
    * **inbound\_connection\_agent**
    * **outbound\_connection\_agent**
    * **id\_mapping\_agent**

4. Query the data in the Amazon Athena console by writing and running SQL queries in
   the Athena Query Editor. For example, you can use the following query to see all
   of the discovered server IP addresses.

```
SELECT * FROM network_interface_agent;
```

For more example queries, see [Using predefined queries in Amazon Athena](predefined-queries.md "predefined-queries.md").
