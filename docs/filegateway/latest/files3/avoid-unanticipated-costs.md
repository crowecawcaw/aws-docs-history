# Avoiding unanticipated costs when uploading

gateway data

When a file is written to the File Gateway by an NFS client, the File Gateway
uploads the file's data to Amazon S3 followed by its metadata. Uploading the file data
creates an S3 object, and uploading the metadata for the file updates the metadata for
the S3 object. This process creates an additional version of the object. If S3
versioning is turned on, both versions are stored.

If you change the metadata of a file that's stored in your File Gateway, a new S3
object is created and replaces the existing S3 object. This behavior is different from
editing a file in a file system, where editing a file does not result in a new file
being created. Test all file operations that you plan to use with AWS Storage Gateway so that
you understand how each file operation interacts with Amazon S3 storage.

Carefully consider the use of S3 versioning and Cross-Region replication (CRR) in Amazon S3
when you're uploading data from your File Gateway. Uploading files from your
File Gateway to Amazon S3 when S3 versioning is turned on results in at least two versions
of an S3 object.

Certain workflows involving large files and file-writing patterns such as file uploads
that are performed in several steps can increase the number of stored S3 object
versions. If the File Gateway cache needs to free up space due to high file-write
rates, multiple S3 object versions might be created. These scenarios increase S3 storage
if S3 Versioning is turned on and increase the transfer costs associated with CRR. Test
all file operations that you plan to use with Storage Gateway so that you understand how
each file operation interacts with Amazon S3 storage.

Using the Rsync utility with your File Gateway results in the creation of temporary
files in the cache and the creation of temporary S3 objects in Amazon S3. This situation
results in early deletion charges in the S3 Standard-Infrequent Access (S3 Standard-IA)
storage class.
