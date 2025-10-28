# Using a database inventory for analysis in AWS DMS

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

To view a list of all databases on all the discovered servers within your network
from which data was collected, use the following procedure.

###### To view a list of databases on your network servers that data was

collected from

1. Choose **Inventory** on the console.

The **Inventory** page opens. 2. Choose the **Databases** tab.

A list of discovered databases appears.

![Database inventory.](images/datarep-dmsstudio-inv-db.png) 3. Choose **Analyze inventories** to determine schema
properties, such as similarity and complexity. The amount of time the process
takes depends on the number of objects to analyze, but it won't take more
than one hour. Results from the analysis are found on the
**Schemas** tab located on the
**Inventory** page.

DMS Fleet Advisor analyzes schemas across all discovered databases to deﬁne the
intersection of their objects. The analysis result is expressed in percentage.
DMS Fleet Advisor considers schemas with intersections of more than 50 percent as
duplicates. Original schema is identified as the schema to which there are
duplicates found. This helps to identify original schemas to convert or migrate
first.

The entire inventory is analyzed together to identify duplicate
schemas.
