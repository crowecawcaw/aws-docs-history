# Tagging key combinations

To better help you find your tagging values, consider the following questions:

- What AWS service will be the destination for your migration?
- What is in the license agreement of your databases?
- Where is the source of your migration (on-prem or already in AWS as Amazon EC2A)?
- Are your workloads in the specialized workload list such as SAP or Oracle workloads?
  Use the tagging decision tree shown in the following diagram to help you assign the tag value for your migrated
  workloads. For a complete list of services that are included in MAP 2.0, see the MAP 2.0 Included
  Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**.

The following diagram shows the decision tree for selecting the appropriate tag value:

![Decision tree flowchart for selecting MAP 2.0 tag values based on migration source, destination, and workload type](images/MAP-tagging-flowchart.png)

###### To get started

- Where are you migrating to?

  - **Services included in the Service list**
  - **SAP included in the Service list**
  - **Oracle included in the Service list**
  - **Database and analytics included in the Service list**: For more information, see [Database and analytics tags](DBA-tags.md "DBA-tags.md").

###### Note

Use lowercase letters for the `mig`, `sap`, and `oracle`
prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information
about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").

`mig`5-digit MPE ID``

_Example:_ `mig12345`

`mig`10 alphanumeric MPE ID characters``

_Example:_ `migABCDE12345`

`sap`5-digit MPE ID``

_Example:_ `sap12345`

`sap`10 alphanumeric MPE ID characters``

_Example:_ `sapABCDE12345`

`oracle`5-digit MPE ID``

_Example:_ `oracle12345`

`oracle`10 alphanumeric MPE ID characters``

_Example:_ `oracleABCDE12345`
