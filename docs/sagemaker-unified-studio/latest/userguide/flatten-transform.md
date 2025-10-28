# Flatten transform

You can flatten the fields of nested structs in the data so they become top level
fields. The new fields are named using the field name prefixed with the names of the struct
fields to reach it, separated by dots.

For example, if the data has a field of type Struct named “phone_numbers”, which among
other fields has one of type “Struct” named “home_phone” with two fields: “country_code” and
“number”. After they are flattened, these two fields will become top level fields named
“phone_numbers.home_phone.country_code” and “phone_numbers.home_phone.number”
respectively.

###### To add a Flatten transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Flatten**.
4. Select the diagram to add the node to your visual ETL job.
5. Select the node on the diagram to view details about the transform.
6. Under **Max levels to flatten**, enter the a maximum limit.
7. Under **Separator**, enter a character to use in the new column
   names to separate the different levels.
