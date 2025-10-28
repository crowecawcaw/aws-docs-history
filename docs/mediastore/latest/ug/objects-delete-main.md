End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Deleting objects

AWS Elemental MediaStore offers different options for deleting objects from
containers:

- [Delete an individual object](objects-delete.md "objects-delete.md"). No charges
  apply.
- [Empty a container](objects-empty-container.md "objects-empty-container.md") to delete all
  objects within a container at once. Because this process uses API calls, normal
  API charges apply.
- [Add an object lifecycle
  policy](policies-object-lifecycle-add.md "policies-object-lifecycle-add.md") to delete objects when they reach a certain age. No charges
  apply.
