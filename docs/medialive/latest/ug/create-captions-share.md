# Creating a captions encode by

sharing

You can create one captions encode and share it among several outputs. Follow the
[earlier procedure](create-captions-scratch.md "create-captions-scratch.md") to create the
encode once. Then set up the encode for the other outputs using the following
steps.

Note that the procedure for sharing a captions encode is nearly identical to the
procedure for sharing a video encode or captions encode.

1. On the **Create channel** page, find the output group
   that you [created](creating-a-channel-step4.md "creating-a-channel-step4.md").
2. Under that output group, find the output where you want to set up a
   captions encode.
3. The output might contain a captions encode that MediaLive has automatically
   added. If you don't plan to use this captions encode, remove it. Choose the
   captions encode and choose **Remove captions**.
4. Create a new captions. Choose **Add captions**. A menu
   appears that includes the option **Use an existing captions
   description**, followed by a list of the captions that
   currently exist in the entire channel. Choose the captions that you want to
   use.
5. On the dialog that appears, choose **Share the existing
   settings**.

The fields for this encode appear. Above the first field is an information
message that lists all the outputs that share this encode.

You might want to change the captions description to include the term
_shared_, as a reminder to
yourself.

Keep in mind that there is only one instance of this encode in the
channel. Therefore, if you change a field, you will change the field in all
the other outputs that use this encode.

Remember this rule if you change the **Captions selector
name** field. If you specify a different selector in the encode
in one output, you change it in all the outputs that share this encode. If
you actually want to specify a different selector, you might need to clone
the encode instead of sharing it.
