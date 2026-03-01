# Copy a saved query between workgroups

Currently, the Athena console does not have an option to to copy a saved query from one
workgroup to another directly, but you can perform the same task manually by using the
following procedure.

###### To copy a saved query between workgroups

1. In the Athena console, from the workgroup that you want to copy the query from,
   choose the **Saved queries** tab.
2. Choose the link of the saved query that you want to copy. Athena opens the
   query in the query editor.
3. In the query editor, select the query text, and then press
   `Ctrl+C` to copy it.
4. [Switch](switching-workgroups.md "switching-workgroups.md") to the destination workgroup, or [create a
   workgroup](creating-workgroups.md "creating-workgroups.md"), and then switch to it.
5. Open a new tab in the query editor, and then press
   `Ctrl+V` to paste the text into the new tab.
6. In the query editor, choose **Save as** to save the query in
   the destination workgroup.
7. In the **Choose a name** dialog box, enter a name for the
   query and an optional description.
8. Choose **Save**.
