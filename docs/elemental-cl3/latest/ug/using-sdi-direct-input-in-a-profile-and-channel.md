# Use case:

Using SDI direct input in a profile and channel

You might want to specify an SDI direct input in your profile and
channel. When you choose this type of input, two supplementary fields
appear—the **Device ID** field and the optional
**Device Settings**.

The **Device ID** field must be set up as a channel
parameter. You can't enter a real ID.

To set up this field, follow this procedure. This procedure assumes
that you have already read [Working with
channel parameters in a profile](creating-a-profile-with-channel-parameters.md "creating-a-profile-with-channel-parameters.md").

1. When you create the profile, complete the following fields in this
   way:
   - **Input Type**: Choose **SDI Direct
     Input**.

   - **Device ID**: For the value, create a channel
     parameter as described in the section [Working with
     channel parameters in a profile](creating-a-profile-with-channel-parameters.md "creating-a-profile-with-channel-parameters.md").

   Assign any name, but do not create a name consisting only of a
   number. For example, create a channel parameter with the name
   `SDI_direct_input`.

   In the **Parameters** panel, leave the validation
   value empty. A validation value is not required for the **Device
   ID** field.
   - **Device Settings**: Always leave this field
     empty.

2. When you create the channel, complete the following fields in this
   way:
   - **Node**: Choose a node that has an SDI direct
     input attached to it.
   - **SDI Direct Input Device
     Id**: Note that the field name appears
     with this label. It doesn't appear with the label **Device
     ID**.

   From the list, choose one of the SDI interfaces that is attached to
   the node that you chose.
   - **Device Settings**: Choose a value, if one is
     applicable to this input.
