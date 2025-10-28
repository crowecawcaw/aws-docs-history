End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Objects in AWS Elemental MediaStore

AWS Elemental MediaStore assets are called _objects_. You can
upload an object to a container or to a folder within the container.

In MediaStore, you can upload, download, and delete objects:

- **Upload** – Add an object to a container or folder.
  This is not the same as creating an object. You must create your objects locally
  before you can upload them to MediaStore.
- **Download** – Copy an object from MediaStore to
  another location. This does not remove the object from MediaStore.
- **Delete** – Remove an object from MediaStore
  completely. You can delete objects individually, or you can [add an object lifecycle policy](policies-object-lifecycle-add.md "policies-object-lifecycle-add.md") to
  automatically delete objects within a container after a specified duration.
  MediaStore accepts all file types.

###### Topics

- [Uploading an object](objects-upload.md "objects-upload.md")
- [Viewing a list of objects](objects-view-list.md "objects-view-list.md")
- [Viewing the details of an object](objects-view-details.md "objects-view-details.md")
- [Downloading an object](objects-download.md "objects-download.md")
- [Deleting objects](objects-delete-main.md "objects-delete-main.md")
