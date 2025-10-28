# Edit tags for a profiling group

You can change the value for a tag associated with a profiling group. While you can't
change the key, you can deleting a tag and creating a new one with the updated key. Keep in
mind that there are limits on the characters you can use in the key and value fields.

###### Important

Editing tags for a profiling group can impact access to that profiling group. Before you
edit the name (key) or value of a tag for a profiling group, make sure to review any IAM
policies that might use the key or value for a tag to control access to resources such as
profiling groups.

## Edit a tag for a profiling

group

You can use the CodeGuru Profiler console to edit the tags associated with a profiling group.

1. In **Profiling groups**, choose the name of the profiling group
   where you want to edit tags.
2. Choose **Actions**. Choose **Edit profiling group**.
3. Choose the **Tags** tab. To change the tag, enter a new name in the
   **Value**. You cannot change the key of a tag.
4. Do one of the following:
   - To change the value of a tag, enter a new value. If you want to change the value
     to nothing, delete the current value and leave the field blank.
   - If you want to change the key of a tag, you can remove a tag and add a new one
     with the updated key name. Find the tag you want to remove, then choose
     **Remove**. Choose **Add a new tag**. In
     **Key**, enter a name for the tag. You can add an optional value
     for the tag in **Value**.

5. When you have finished editing tags, choose **Save**.
