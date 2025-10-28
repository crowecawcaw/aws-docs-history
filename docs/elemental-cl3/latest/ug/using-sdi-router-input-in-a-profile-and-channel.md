# Use case:

Using SDI router input in a profile and channel

You might want to specify an SDI router input in your profile and
channel. This type of input goes through a router, and is only applicable if
there is at least one node in the cluster that is configured with a router.
When you choose this type of input, a supplementary field appears—the
**Router Input ID** field.

The **Router Input ID** field must be set up as a
channel parameter. You can't enter a real ID.

To set up this field, follow this procedure. This procedure assumes
that you have already read [Working with
channel parameters in a profile](creating-a-profile-with-channel-parameters.md "creating-a-profile-with-channel-parameters.md").

1. When you create the profile, complete the following fields in this
   way:
   - **Input Type**: Choose **SDI Router
     Input**.

   - **Router Input ID**: For the value, create a
     channel parameter as described in the section [Working with
     channel parameters in a profile](creating-a-profile-with-channel-parameters.md "creating-a-profile-with-channel-parameters.md").

   Assign any name, but do not create a name consisting only of a
   number. For example, create a channel parameter with the name
   `SDI_router_ID`.

   In the **Parameters** panel, enter a validation
   value.

2. When you create the channel, complete the following fields in this
   way:
   - **Node**: Choose a node that has an SDI router
     attached to it.
   - **SDI Router Input Router Input ID**: Note that
     the field name appears with this label. It doesn't appear with the label
     **Router Input ID**.

   From the list, choose one of the inputs on the router. This router
   is attached to the node that you chose.
