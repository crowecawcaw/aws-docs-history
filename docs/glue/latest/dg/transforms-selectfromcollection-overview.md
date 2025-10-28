# Overview of

_SelectFromCollection_ transform

Certain transforms have multiple datasets as their output instead of a single dataset,
for example, _SplitFields_. The _SelectFromCollection_
transform selects one dataset (`DynamicFrame`) from a collection of datasets (an
array of `DynamicFrames`). The output for the transform is the selected
`DynamicFrame`.

You must use this transform after you use a transform that creates a collection of
`DynamicFrames`, such as:

- Custom code transforms
- _SplitFields_
  If you don't add a _SelectFromCollection_ transform node to your job
  diagram after any of these transforms, you will get an error for your job.

The parent node for this transform must be a node that returns a collection of
`DynamicFrames`. If you choose a parent for this transform node that returns a
single `DynamicFrame`, such as a _Join_ transform, your job
returns an error.

Similarly, if you use a _SelectFromCollection_ node in your job
diagram as the parent for a transform that expects a single `DynamicFrame` as
input, your job returns an error.

![The screenshot shows the Node parents field on the Node properties tab of the node details panel. The selected node parent is SplitFields and the error message displayed reads "Parent node Split Fields outputs a collection, but node Drop Fields does not accept a collection."](images/screenshot-edit-splitfields-wrong-parent.png)
