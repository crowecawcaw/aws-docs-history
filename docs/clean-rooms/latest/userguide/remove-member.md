

# Removing members from a collaboration
<a name="remove-member"></a>

**Note**  
Before you begin, note that removing a member:   
Removes all of their associated datasets from the collaboration
If the [member pays for query compute costs](glossary.md#glossary-member-paying-for-query-compute), this action stops all query execution in the collaboration.
Removing a member also removes all of their associated datasets from the collaboration.

**Prerequisites**
+ You must be a collaboration creator 
+ You can't remove your own account 

**To remove a member from a collaboration**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Select the collaboration you want to modify.

1. Choose the **Members** tab.

1. Select the option button next to the member you want to remove.

1. Choose **Remove**.

1. In the confirmation dialog box, type **confirm** to verify the removal.

**Note**  
After you remove a member, all datasets associated with their account are also removed from the collaboration. 

**Important**  
If you remove the member who pays for query compute costs, no further queries can run in the collaboration until you designate a new paying member. 