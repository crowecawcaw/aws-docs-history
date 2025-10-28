End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Deleting a folder

You can delete folders only if the folder is empty; you can’t delete folders that
contain objects.

AWS Elemental MediaStore automatically deletes a folder when you delete the last object in that folder.
The service also deletes any empty folders above that folder. For example, suppose that
you have a folder named `premium` that doesn’t contain any files but
does contain one subfolder named `canada`. The
`canada` subfolder contains one file named
`mlaw.ts`. If you delete the file `mlaw.ts`,
the service deletes both the `premium` and
`canada` folders. This automatic deletion applies only to
folders. The service does not delete empty containers.

For more information, see [Deleting an object](objects-delete.md "objects-delete.md").
