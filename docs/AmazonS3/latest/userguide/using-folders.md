# Organizing objects in the Amazon S3 console by using folders

In Amazon S3 general purpose buckets, objects are the primary resources, and objects are stored in buckets.
Amazon S3 general purpose buckets have a flat structure instead of a hierarchy like you would see in a file system. However,
for the sake of organizational simplicity, the Amazon S3 console supports the _folder_ concept as a means of grouping objects. The console does this by using a
shared name _prefix_ for the grouped objects. In other words,
the grouped objects have names that begin with a common string. This common string, or shared
prefix, is the folder name. Object names are also referred to as _key
names_.

For example, you can create a folder in a general purpose bucket in the console named `photos` and store an
object named `myphoto.jpg` in it. The object is then stored with the key name
`photos/myphoto.jpg`, where `photos/` is the prefix.

Here are two more examples:

- If you have three objects in your general purpose bucket—`logs/date1.txt`,
  `logs/date2.txt`, and `logs/date3.txt`—the console will show a
  folder named `logs`. If you open the folder in the console, you will see three
  objects: `date1.txt`, `date2.txt`, and `date3.txt`.
- If you have an object named `photos/2017/example.jpg`, the console shows you
  a folder named `photos` that contains the folder `2017`. The folder
  `2017` contains the object `example.jpg`.
  You can have folders within folders, but not buckets within buckets. You can upload and copy
  objects directly into a folder. Folders can be created, deleted, and made public, but they can't
  be renamed. Objects can be copied from one folder to another.

###### Important

When you create a folder in Amazon S3 console, S3 creates a 0-byte object. This object key is set to the folder name that you provided plus a trailing forward slash (`/`) character. For example, in Amazon S3 console, if you create a folder named
`photos` in your bucket, the Amazon S3 console creates a 0-byte object with the key
`photos/`. The console creates this object to support the idea of folders.

Also, any pre-existing object that's named with a trailing forward slash character (`/`) appears as a folder in the Amazon S3
console. For example,
an object with the key name `examplekeyname/` appears as a folder in Amazon S3 console and not as an object. Otherwise, it behaves like any other object and can be viewed and manipulated through the AWS Command Line Interface (AWS CLI), AWS SDKs, or REST API. Additionally, you can't upload an object that has a key name with a
trailing forward slash character (`/`) by using the Amazon S3 console. However, you can upload objects
that are named with a trailing forward slash (`/`) character by using the AWS Command Line Interface
(AWS CLI), AWS SDKs, or REST API.

Moreover, the Amazon S3 console doesn't display the content and metadata for folder objects like it does for other objects. When
you use the console to copy an object named with a trailing forward slash character (`/`), a new folder is
created in the destination location, but the object's data and metadata aren't copied. Also, a forward slash (`/`) in object key names might require special handling. For more information, see [Naming Amazon S3 objects](object-keys.md "object-keys.md").

To create folders in directory buckets, upload a folder. For more information, see [Uploading objects to a directory
bucket](directory-buckets-objects-upload.md "directory-buckets-objects-upload.md").

###### Topics

- [Creating a folder](#create-folder "#create-folder")
- [Making folders public](#public-folders "#public-folders")
- [Calculating folder size](#calculate-folder "#calculate-folder")
- [Deleting folders](#delete-folders "#delete-folders")

## Creating a folder

This section describes how to use the Amazon S3 console to create a folder.

###### Important

If your bucket policy prevents uploading objects to this bucket without tags, metadata,
or access control list (ACL) grantees, you can't create a folder by using the following
procedure. Instead, upload an empty folder and specify the following settings in the upload
configuration.

###### To create a folder

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that you want
   to create a folder in.
4. On the **Objects** tab, choose **Create
   folder**.
5. Enter a name for the folder (for example, `favorite-pics`).

###### Note

Folder names are subject to certain limitations and guidelines, and are considered
part of an object's object key name, which is limited to 1,024 bytes. For more
information, see [Naming Amazon S3 objects](object-keys.md "object-keys.md"). 6. (Optional) If your bucket policy requires objects to be encrypted with a specific
encryption key, under **Server-side encryption**, you must choose
**Specify an encryption key** and specify the same encryption key when
you create a folder. Otherwise, folder creation will fail. 7. Choose **Create folder**.

## Making folders public

We recommend blocking all public access to your Amazon S3 folders and buckets unless you
specifically require a public folder or bucket. When you make a folder public, anyone on the
internet can view all the objects that are grouped in that folder.

In the Amazon S3 console, you can make a folder public. You can also make a folder public by
creating a bucket policy that limits data access by prefix. For more information, see [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").

###### Warning

After you make a folder public in the Amazon S3 console, you can't make it private again.
Instead, you must set permissions on each individual object in the public folder so that the
objects have no public access. For more information, see [Configuring ACLs](managing-acls.md "managing-acls.md").

###### Topics

- [Calculating folder size](#calculate-folder "#calculate-folder")
- [Deleting folders](#delete-folders "#delete-folders")

## Calculating folder size

This section describes how to use the Amazon S3 console to calculate a folder's size.

###### To calculate a folder's size

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose
   buckets**.
3. In the **General purpose buckets** list, choose the name of the
   bucket in which your folder is stored.
4. In the **Objects** list, select the checkbox next to the name of the
   folder.
5. Choose **Actions**, and then choose **Calculate total
   size**.

###### Note

When you navigate away from the page, the folder information (including the total size) is no
longer available. You must calculate the total size again if you want to see it again.

###### Important

When you use the **Calculate total size** action on specified objects or
folders within your bucket, Amazon S3 calculates the total number of objects and the total
storage size. However, incomplete or in-progress multipart uploads and previous or
noncurrent versions aren't calculated in the total number of objects or the total size. This
action calculates only the total number of objects and the total size for the current or
newest version of each object that's stored in the bucket.

For example, if there are two versions of an object in your bucket, then the storage
calculator in Amazon S3 counts them as only one object. As a result, the total number of objects
that's calculated in the Amazon S3 console can differ from the **Object Count**
metric shown in S3 Storage Lens and from the number reported by the Amazon CloudWatch metric,
`NumberOfObjects`. Likewise, the total storage size can also differ from the
**Total Storage** metric shown in S3 Storage Lens and from the
`BucketSizeBytes` metric shown in CloudWatch.

## Deleting folders

This section explains how to use the Amazon S3 console to delete folders from an S3 bucket.

For information about Amazon S3 features and pricing, see [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/").

###### To delete folders from an S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the **General purpose buckets** list, choose the name of the bucket
   that you want to delete folders from.
4. In the **Objects** list, select the checkboxes next to the folders and
   objects that you want to delete.
5. Choose **Delete**.
6. On the **Delete objects** page, verify that the names of the folders
   and objects that you selected for deletion are listed under **Specified
   objects**.
7. In the **Delete objects** box, enter `delete`, and choose **Delete objects**.

###### Warning

This action deletes all specified objects. When deleting folders, wait for the delete action to finish before adding new objects to the folder.
Otherwise, new objects might be deleted as well.
