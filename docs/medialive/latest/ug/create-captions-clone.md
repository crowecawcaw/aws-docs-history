# Creating a captions encode by

cloning

You can create one captions encode and clone it among several outputs. The
_source_ encode could be an encode that you
created from scratch, or it could be an encode that was itself created by cloning.
For example, create _captions-1_, then clone it to
_captions-2_, then clone _captions-2_ to _captions-3_.

Note that the procedure for cloning a captions encode is nearly identical to the
procedure for cloningg a video encode or captions encode.

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
5. Choose the captions encode that you want to use as the source for the new
   captions encode.
6. On the dialog that appears, choose **Clone the existing
   settings**. The fields for the encode appear, with the fields
   showing the values from the source encode.
7. Complete other fields as appropriate, to configure the captions encode.
   For detailed information about setting up captions encodes, see [Create captions encodes](create-captions-encodes.md "create-captions-encodes.md").
8. Keep in mind that this cloned encode is a new encode instance. If you
   change fields, you don't affect the source encode.
