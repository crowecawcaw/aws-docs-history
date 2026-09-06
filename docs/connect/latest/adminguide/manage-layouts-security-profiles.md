

# Security profiles needed to manage layouts
<a name="manage-layouts-security-profiles"></a>

Access to Manage layouts is controlled by the same Profile explorer permissions described in [Enable Profile explorer](enabling-profile-explorer.md). The following permissions determine what a user can do:
+ **Profile explorer - View**: Required to open Profile explorer and view the currently active default layout.
+ **Profile explorer - Edit**: Required to see and open the **Manage layouts** button, access the **Profile layouts** page, and use the **Delete** and **Make default** actions on that page. This permission is also required, along with **Profile explorer - Create**, to see the layout editor toolbar (**Edit tabs**, **Add widget**, and **Save layout**).
+ **Profile explorer - Create**: Required to see and choose the **Create layout** button on the **Profile layouts** page.

**Note**  
There's no separate permission for deleting a layout or setting a layout as default—both actions are controlled by **Profile explorer - Edit**.

For instructions on assigning these permissions, see [Enable administrators to define a layout](enabling-profile-explorer.md#enable-administrators-define-layout).