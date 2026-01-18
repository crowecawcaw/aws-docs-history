# Mapping new data types in the AWS Schema Conversion Tool

You can create multiple mapping rules in a single project. AWS SCT saves mapping rules
as part of your project. With your project open, use the following procedure
to add a new mapping rule.

###### To create mapping rules

1. On the **View** menu, choose **Mapping
   view**.
2. In the left panel, choose a schema or a database to add to the mapping rule.
3. In the right panel, choose a target database platform for the selected
   source schema or database.

You can choose a virtual database platform as a target. For more information,
see [Mapping to virtual targets in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md"). 4. Choose **Create mapping**.

AWS SCT adds this new mapping rule to the
**Server mappings** list.
Add mapping rules for all conversion pairs. To create an assessment report or convert
database schemas, choose **Main view** on the **View**
menu.

AWS SCT highlights in bold all schema objects that are part of a mapping rule.
