# Remove a tag from a profiling

group

You can remove one or more tags associated with a profiling group. You can also change the
name of the key, which is equivalent to removing the current tag and adding a different one
with the new name and the same value as the other key. Removing a tag does not delete the tag
from other AWS resources that are associated with that tag.

###### Important

Removing tags for a profiling group can impact access to that profiling group. Before
you remove a tag from a profiling group, make sure to review any IAM policies that might
use the key or value for a tag to control access to resources such as profiling
groups.

## Remove a tag from a profiling

group

You can use the CodeGuru Profiler console to remove the association between a tag and a profiling
group.

1. In **Profiling groups**, choose the name of the profiling group
   where you want to remove tags.
2. Choose **Actions**. Choose **Edit profiling group**.
3. Choose the **Tags** tab.
4. Find the tag you want to remove, and then choose **Remove**.
5. When you have finished removing tags, choose **Save**.
