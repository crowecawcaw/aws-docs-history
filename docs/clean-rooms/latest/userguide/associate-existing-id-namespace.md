

# Associating an existing ID namespace
<a name="associate-existing-id-namespace"></a>

In this procedure, each member associates either their existing ID namespace source or their ID namespace target in the collaboration.

**To associate an existing ID namespace**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. On the **Entity resolution** tab, choose **Associate ID namespace**.

1. On the **Associate ID namespace** page, for **Entity resolution data**, choose the **AWS Entity Resolution ID namespace** source or target that you want to associate with the collaboration from the dropdown list.

1. For **Association details**, take the following steps.

   1. Enter a **Name** for the associated ID namespace.

      You can use the default name or rename this ID namespace.

   1. (Optional) Enter a **Description** of the ID namespace.

      The description helps with writing queries.

1. Specify the **AWS Clean Rooms access** permissions by selecting an option and then taking the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/associate-existing-id-namespace.html)

1. (Optional) For **Advanced ID mapping table configurations**, modify the default protections for the column that comes from the ID namepsace.

   The ID mapping table is configured by default to only allow an `INNER JOIN` on both the `sourceID` column and the `targetID` column. You can modify this configuration so that the column that comes from this ID namespace (either `sourceID` or `targetID`) can be allowed anywhere in the query.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/associate-existing-id-namespace.html)

1. (Optional) If you want to enable **Tags** for the ID namepsace resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 

1. Choose **Associate**.

1. On the **Entity resolution** tab, under the **Associated ID namespaces** table, view the associated ID namespace and verify that the ID namespace type is correct (**Source** or **Target**).

After all members in the collaboration have associated their ID namespaces, you can [create an ID mapping table](create-id-mapping-table.md) and query the data.