# Viewing object properties in the Amazon S3 console

You can use the Amazon S3 console to view the properties of an object, including storage class,
encryption settings, tags, and metadata.

###### To view the properties of an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets** or **Directory buckets**.
3. In the bucket list, choose the name of the bucket that
   contains the object.
4. In the **Objects** list, choose the name of the object you want to view
   properties for.

The **Object overview** for your object opens. You can scroll down to
view the object properties. 5. On the **Object overview** page, you can view or configure the following
properties for the object.

###### Note

    * If you change the **Storage Class**,  **Encryption**, or **Metadata**
     properties, a new object is created to replace the old one. If S3 Versioning is
     enabled, a new version of the object is created, and the existing object becomes an
     older version. The role that changes the property also becomes the owner of the new
     object or (object version).
    * If you change the **Storage Class**,
     **Encryption**, or **Metadata** properties for an
     object that has user-defined tags, you must have the `s3:GetObjectTagging`
     permission. If you're changing these properties for an object that doesn't have
     user-defined tags but is over 16 MB in size, you must also have the
     `s3:GetObjectTagging` permission.


    If the destination bucket policy denies the `s3:GetObjectTagging`
     action, these properties for the object will be updated, but the user-defined tags
     will be removed from the object, and you will receive an error.
    1. **Storage class** – Each object in Amazon S3 has a storage class
     associated with it. The storage class that you choose to use depends on how frequently
     you access the object. The default storage class for S3 objects in general purpose buckets is STANDARD. The default storage class for S3 objects in directory buckets is S3 Express One Zone. You choose
     which storage class to use when you upload an object. For more information about storage
     classes, see [Understanding and managing Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md").


    To change the storage class after you upload an object to a general purpose bucket, choose **Storage
     class**. Choose the storage class that you want, and then choose
     **Save**.


    ###### Note

    Storage class of objects in a directory bucket cannot be changed.
    2. **Server-side encryption settings** – You can use server-side
     encryption to encrypt your S3 objects. For more information, see [Specifying server-side encryption with AWS KMS
     (SSE-KMS)](specifying-kms-encryption.md "specifying-kms-encryption.md") or [Specifying server-side encryption with Amazon S3 managed
     keys (SSE-S3)](specifying-s3-encryption.md "specifying-s3-encryption.md").
    3. **Metadata** – Each object in Amazon S3 has a set of name-value
     pairs that represents its metadata. For information about adding metadata to an S3
     object, see [Editing object metadata in the Amazon S3 console](add-object-metadata.md "add-object-metadata.md").
    4. **Tags** – You categorize storage by adding tags to an S3
     object in a general purpose bucket. For more information, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").
    5. **Object lock legal hold and retention** – You can prevent an
     object in a general purpose bucket from being deleted. For more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").
