

# Adding, editing, or deleting entity fields
<a name="data-entities-edit-fields"></a>

**Tip**  
You can press CTRL\+Z to undo the most recent change to your entity.

1. If necessary, navigate to the entity you want to edit.

1. In the **Configuration** tab, in **Fields**, you view a table of your entity's fields. Entity fields have the following columns:
   + **Display name:** The display name is similar to a table header or form field and is viewable by application users. It can contain spaces and special characters but must be unique within an entity.
   + **System name:** The system name is a unique identifier used in code to reference a field. When mapping to a column in an Amazon Redshift table, it must match the Amazon Redshift table column name.
   + **Data type:** The type of data that will be stored within this field, such as `Integer`, `Boolean`, or `String`.

1. To add fields:

   1. To use AI to generate fields based on entity name and connected data source, choose **Generate more fields**.

   1. To add a single field, choose **\+ Add field**.

1. To edit a field:

   1. To edit the display name, enter the desired value in the **Display name** text box. If the system name of the field hasn't been edited, it will be updated to the new value of the display name.

   1. To edit the system name, enter the desired value in the **System name** text box.

   1. To edit the data type, choose the **Data type** dropdown menu and select the desired type from the list.

   1. To edit the field's properties, choose the gear icon of the field. The following list details the field properties:
      + **Required**: Enable this option if the field is required by your data source.
      + **Primary key**: Enable this option if the field is mapped to a primary key in your data source.
      + **Unique**: Enable this option if the value of this field must be unique.
      + **Use data source default**: Enable this option if the value of the field is provided by the data source, such as using auto-increment, or an event timestamp.
      + **Data type options**: Fields of certain data types can be configured with data type options such as minimum or maximum values.

1. To delete a field, choose the trash icon of the field you want to delete.