# Model Registry Collections

You can use Collections to group registered models that are related to each other and
organize them in hierarchies to improve model discoverability at scale. With
Collections, you can organize registered models that are associated with one another.
For example, you could categorize your models based on the domain of the problem they
solve as Collections titled _NLP-models_, _CV-models_, or _Speech-recognition-models_. To organize your registered models in a tree
structure, you can nest Collections within each other. Any operations you perform on a
Collection, such as create, read, update, or delete, will not alter your registered
models. You can use the Amazon SageMaker Studio UI or the Python SDK to manage
your Collections.

The **Collections** tab in the Model Registry displays a list of all the
Collections in your account. The following sections describe how you can use options in
the **Collections** tab to do the following:

- Create Collections
- Add Model Groups to a Collection
- Move Model Groups between Collections
- Remove Model Groups or Collections from other Collections
  Any operation you perform on your Collections does not affect the integrity of the
  individual Model Groups they contain—the underlying Model Group artifacts in Amazon S3
  and Amazon ECR are not modified.

While Collections provide greater flexibility in organizing your models, the internal
representation imposes some constraints on the size of your hierarchy. For a summary of
these constraints, see [Constraints](modelcollections-limitations.md "modelcollections-limitations.md").

The following topics show you how to create and work with Collections in the
Model Registry.

###### Topics

- [Set up prerequisite
  permissions](modelcollections-permissions.md "modelcollections-permissions.md")
- [Create a Collection](modelcollections-create.md "modelcollections-create.md")
- [Add Model Groups to a
  Collection](modelcollections-add-models.md "modelcollections-add-models.md")
- [Remove Model Groups or Collections
  from a Collection](modelcollections-remove-models.md "modelcollections-remove-models.md")
- [Move a Model Group Between
  Collections](modelcollections-move-models.md "modelcollections-move-models.md")
- [View a Model Group's Parent
  Collection](modelcollections-view-parent.md "modelcollections-view-parent.md")
- [Constraints](modelcollections-limitations.md "modelcollections-limitations.md")
