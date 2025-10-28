# Enabling permissions on ServiceNow

Platform

For AWS products to display under AWS portfolios as sub-categories in the
ServiceNow Service Catalog, you need to modify the Application Access form for
Catalog Item Category tables. This action is necessary because a ServiceNow
scoped API is not available for the Catalog Item Category table.

###### To view AWS Service Catalog products (Catalog Item Category)

1. Enter `Tables` in the Navigator and choose
   **System Definition**, then choose
   **Tables**.
2. In the list of tables, search for a table with label **Catalog Item Category** (or with the name
   `sc_cat_item_category`). The list of tables displays.
3. Choose **Category** to view the form defining the
   table.
4. Choose the **Application Access** tab on
   the form and select **Can Create**,
   **Can Update**, and **Can Delete** on the form.
5. Choose **Update**.

###### To enable the connector to control visibility of Service Catalog products on Service Portal

through Allowed Groups

###### Note

This step is only required if the Application Access is not already enabled in your ServiceNow instance.
Additionally, Service Management Connector recommends that you enable the `User Criteria Scope API` plugin.

1. Enter `Tables` in the Navigator and choose
   **System Definition**, then choose
   **Tables**.
2. In the list of tables, search for a table with label **Catalog Item Available for** (or with the name
   `sc_cat_item_user_criteria_mtom`). The list of tables displays.
3. Choose **Category** to view the form defining the
   table.
4. Choose the **Application Access** tab on
   the form and select **Can Create** and
   **Can Update** on the form.
5. Choose **Update**.
