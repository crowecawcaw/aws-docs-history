AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# View collected data using the Migration Hub console

For both the Application Discovery Service Agentless Collector (Agentless Collector) and AWS
Discovery Agent (Discovery Agent), after the data collection process starts, you can use the console to
view their collected data about your servers and VMs. Data appears in the console
approximately 15 minutes after data collection starts. You can also view this data in CSV
format by exporting the collected data by making API calls using the AWS CLI.

To view collected data about discovered servers in the console, follow the steps in [Viewing servers in the AWS Migration Hub console](view-servers.md "view-servers.md"). To learn more about using the console to view, sort, and tag servers discovered by your
Agentless Collectors or Discovery Agents, see [Discovering data with the AWS Migration Hub console](console-walkthrough.md "console-walkthrough.md").

The Agentless Collector database and analytics data collection module uploads the
collected data to the Amazon S3 bucket. You can view the data from this bucket in the AWS DMS
console. To view collected data about discovered database and analytics servers, follow the
steps in [Viewing your collected data](agentless-collector-gs-view-collected-data.md "agentless-collector-gs-view-collected-data.md").

## Matching logic for discovered servers and applications

AWS Application Discovery Service (Application Discovery Service) has built-in matching logic that identifies when servers that it
discovers match existing entries. When this logic finds a match, it updates the information
for the already-existing discovered server with new values.

This matching logic handles duplicate servers from multiple sources including AWS Migration Hub
(Migration Hub) import, Application Discovery Service Agentless Collector (Agentless Collector),
AWS Application Discovery Agent (Discovery Agent), and other migration tools. For more information about Migration Hub import,
see [Migration Hub Import](../../../migrationhub/latest/ug/migration-hub-import.md "../../../migrationhub/latest/ug/migration-hub-import.md").

When server discovery occurs, each entry is cross-checked with previously imported records
to ensure that the imported server does not already exist. If no match is found, a new
record is created and a new unique server identifier is assigned. If a match is found, then
a new entry is still created, but it's assigned the same unique server identifier as the
existing server. When viewing this server in the Migration Hub console, you only find one unique
entry for the server.

Server attributes associated with this entry are merged to show attribute values from a
previously available record as well as the newly imported record. If there is more than one
value for a given server attribute from multiple sources, e.g., two different values within
for `Total RAM` associated with a given server discovered using import and also
by the Discovery Agent, then the value that was most recently updated is shown in the
matched record for the server.

### Matching fields

The following fields are used to match servers when discovery tools are used.

- **ExternalId** – This is the primary field
  used to match servers. If the value in this field is identical to another
  `ExternalId` in another entry, then Application Discovery Service matches the two
  entries, regardless of whether the other fields match or not.
- **IPAddress**
- **HostName**
- **MacAddress**
- **VMware.MoRefId** and **VMware.vCenterId** – Both of these values must be identical
  to the respective fields in another entry for Application Discovery Service to perform a
  match.
