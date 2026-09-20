

# Editing ID namespace associations
<a name="edit-id-namespace-association"></a>

As a collaboration member, you can edit the ID namespace associations that you have created.

**To edit an ID namespace association**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose the **Entity resolution** tab.

1. For **Associated ID namespaces**, choose an ID namespace.

1. On the ID namespace details page, scroll down to view the **ID namespace association details**.

1. Choose **Edit**.

1. On the **Edit ID namespace associations** page, edit any of the following:

   

   1. For **Association details**, update the **Name** or the **Description**.

   1. (Optional) For **Advanced ID mapping table configurations**, modify the default protections for the column that comes from the ID namepsace.

      The ID mapping table is configured by default to only allow an `INNER JOIN` on both the `sourceID` column and the `targetID` column. You can modify this configuration so that the column that comes from this ID namespace (either `sourceID` or `targetID`) can be allowed anywhere in the query.


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Categorize the column as a "join column" and only allow it in an <code>INNER JOIN</code> clause</td><td><b>Yes</b></td></tr>
  <tr><td>Categorize the column as a "dimension column" and allow it anywhere in the query, including a <code>JOIN</code> clause, <code>SELECT</code>, <code>WHERE</code> and <code>GROUP BY</code> statements of the query.</td><td><b>No, allow anywhere in the query</b></td></tr>
</tbody>
</table>


1. Choose **Save changes**.