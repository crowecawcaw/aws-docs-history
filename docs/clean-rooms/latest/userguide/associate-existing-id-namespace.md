

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


<table>
<thead>
  <tr><th>Option</th><th>Recommended action</th></tr>
</thead>
<tbody>
  <tr><td><b>Allow AWS Clean Rooms to add and manage permission policy</b></td><td>AWS Clean Rooms creates a service role with the required policy for this association.</td></tr>
  <tr><td><b>Add and manage permissions manually</b></td><td>Do one of the following:<ul><li> Review the <b>Resource policy</b> and add necessary permissions to the policy. </li><li> Use an existing policy by choosing <b>Add policy statement</b>. </li></ul>You must have permissions to modify roles and create policies. If you can’t modify the role policy, you receive an error message stating that AWS Clean Rooms couldn't ﬁnd the policy for the service role. </td></tr>
</tbody>
</table>


1. (Optional) For **Advanced ID mapping table configurations**, modify the default protections for the column that comes from the ID namepsace.

   The ID mapping table is configured by default to only allow an `INNER JOIN` on both the `sourceID` column and the `targetID` column. You can modify this configuration so that the column that comes from this ID namespace (either `sourceID` or `targetID`) can be allowed anywhere in the query.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Categorize the column as a "join column" and only allow it in an <code>INNER JOIN</code> clause.</td><td><b>Yes</b></td></tr>
  <tr><td>Categorize the column as a "dimension column" and allow it anywhere in the query, including a <code>JOIN</code> clause, <code>SELECT</code>, <code>WHERE</code>, and <code>GROUP BY</code> statements of the query.</td><td><b>No, allow anywhere in the query</b></td></tr>
</tbody>
</table>


1. (Optional) If you want to enable **Tags** for the ID namepsace resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 

1. Choose **Associate**.

1. On the **Entity resolution** tab, under the **Associated ID namespaces** table, view the associated ID namespace and verify that the ID namespace type is correct (**Source** or **Target**).

After all members in the collaboration have associated their ID namespaces, you can [create an ID mapping table](create-id-mapping-table.md) and query the data.