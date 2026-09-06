

# Known issues
<a name="known-issues"></a>

The Amazon DCV Access Console has the following known issues.

## Cannot delete users from UI
<a name="cannot-delete-users"></a>

To prevent users from logging into the UI, users can be disabled. To disable users, import the users with the `disabled` column set to true for the user.

## Cannot manage Amazon DCV host servers
<a name="cannot-manage-host-servers"></a>

While the Access Console allows administrators to view the underlying hosts they have the Amazon DCV sessions installed on. However, it does not allow administrators to manage those resources directly. If you wish to start, terminate, or reboot your hosts, you must do so from your cloud or on-premise environment directly. 