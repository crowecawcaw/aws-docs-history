# Facets

In NoSQL Workbench, _Facets_ give you a way to view a subset of the data in a table, without having to see records that don't meet the constraints of the facet.
Facets are considered a visual data modeling tool, and don't exist as a usable construct in DynamoDB, as they are purely an aid to modeling of access patterns.

###### Note

We recommend you use [Adding and validating access patterns](workbench.Modeler.md "workbench.Modeler.md") to visualize how your application will access data in DynamoDB instead of Facets.
Access patterns mirror your actual database interactions and help you build the correct data model for your use case, while facets are non-functional visualizations.

###### To create a facet

1. In the resource selector panel, choose a **Table** you wish to edit
2. In the top bar, click the **Edit** action icon.
3. Scroll down to the **Facet filters** section.
4. Choose **Add facet**. Specify the following:
   - The **Facet name**.
   - A **Partition key alias** to help distinguish this facet view.
   - A **Sort key alias** if you provided a **Sort key** for the table.
   - Choose the **Attributes** that are part of this facet.

Repeat this step if you want to add more facets.
