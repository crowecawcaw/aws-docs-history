# Enable and Administer Persistent Storage for

WorkSpaces Pools

WorkSpaces Pools supports home folders for persistent storage. As a WorkSpaces Pools administrator,
you must understand how to perform the following tasks to enable and administer persistent
storage for your users.

###### Contents

- [Enable and Administer Home Folders for Your WorkSpaces Pools
  Users](#home-folders "#home-folders")

## Enable and Administer Home Folders for Your WorkSpaces Pools

Users

When you enable home folders for WorkSpaces Pools, users can access a persistent storage
folder during their streaming sessions. No further conﬁguration is required for your
users to access their home folder. Data stored by users in their home folder is
automatically backed up to an Amazon Simple Storage Service bucket in your Amazon Web Services account and is made
available to those users in subsequent sessions.

Files and folders are encrypted in transit using Amazon S3's SSL endpoints. Files and
folders are encrypted at rest using Amazon S3-managed encryption keys.

Home folders are stored on WorkSpaces in WorkSpaces Pools in the following default
locations:

- For single-session, non-domain-joined Windows WorkSpaces:
  `C:\Users\PhotonUser\My Files\Home Folder`
- Domain-joined Windows WorkSpaces: `C:\Users\%username%\My Files\Home
Folder`

As an administrator, use the applicable path if you configure your applications to
save to the home folder. In some cases, your users may not be able to find their home
folder because some applications do not recognize the redirect that displays the home
folder as a top-level folder in File Explorer. If this is the case, your users can
access their home folder by browsing to the same directory in File Explorer.

###### Contents

- [Files and Directories Associated with Compute-Intensive Applications](#storage-solutions-files-directories-associated-with-compute-intensive-applications "#storage-solutions-files-directories-associated-with-compute-intensive-applications")
- [Enable Home Folders for Your WorkSpaces Pools
  Users](#enable-home-folders "#enable-home-folders")
- [Administer Your Home Folders](#home-folders-admin "#home-folders-admin")

### Files and Directories Associated with Compute-Intensive Applications

During WorkSpaces Pools streaming sessions, saving large files and directories
associated with compute-intensive applications to persistent storage can take longer
than saving files and directories required for basic productivity applications. For
example, it might take longer for applications to save a large amount of data or
frequently modify the same files than it would to save files created by applications
that perform a single write action. It might also take longer to save many small
files.

If your users save files and directories associated with compute-intensive
applications and WorkSpaces Pools persistent storage options aren't performing as
expected, we recommend that you use a Server Message Block (SMB) solution such as
Amazon FSx for Windows File Server or an AWS Storage Gateway file gateway. Following are examples of files and
directories associated with compute-intensive applications that are more suitable
for use with these SMB solutions:

- Workspace folders for integrated development environments (IDEs)
- Local database files
- Scratch space folders created by graphics simulation applications

For more information, see [File gateways](../../../storagegateway/latest/userguide/StorageGatewayConcepts.md#file-gateway-concepts "../../../storagegateway/latest/userguide/StorageGatewayConcepts.md#file-gateway-concepts") in the _AWS Storage Gateway User
Guide_.

### Enable Home Folders for Your WorkSpaces Pools

Users

Before enabling home folders, you must do the following:

- Check that you have the correct AWS Identity and Access Management (IAM) permissions for Amazon S3
  actions.
- Use an image that was created from an AWS base image released on or
  after May 18,

2017.

- Enable network connectivity to Amazon S3 from your virtual private cloud (VPC)
  by configuring internet access or a VPC endpoint for Amazon S3. For more
  information, see [Networking and Access for WorkSpaces Pools](managing-network.md "managing-network.md") and [Using Amazon S3 VPC Endpoints for
  WorkSpaces Pools Features](managing-network-vpce-iam-policy.md "managing-network-vpce-iam-policy.md").

You can enable or disable home folders while creating a directory (see [Configure SAML 2.0 and create a WorkSpaces Pools
directory](create-directory-pools.md "create-directory-pools.md")), or
after the directory is created by using the AWS Management Console for WorkSpaces Pools. For each AWS
Region, home folders are backed up by an Amazon S3 bucket.

The first time you enable home folders for an WorkSpaces Pools directory in an AWS
Region, the service creates an Amazon S3 bucket in your account in that same Region. The
same bucket is used to store the content of home folders for all users and all
directories in that Region. For more information, see [Amazon S3 Bucket Storage](#home-folders-s3 "#home-folders-s3").

###### To enable home folders while creating a directory

- Follow the steps in [Configure SAML 2.0 and create a WorkSpaces Pools
  directory](create-directory-pools.md "create-directory-pools.md"), and make sure that **Enable
  Home Folders** is selected.

###### To enable home folders for an existing directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the left navigation pane, choose **Directories**, and
   select the directory for which to enable home folders.
3. Below the directories list, choose **Storage** and select
   **Enable Home Folders**.
4. In the **Enable Home Folders** dialog box, choose
   **Enable**.

### Administer Your Home Folders

###### Contents

- [Disable Home Folders](#home-folders-admin-disabling "#home-folders-admin-disabling")
- [Amazon S3 Bucket Storage](#home-folders-s3 "#home-folders-s3")
- [Home Folder Content
  Synchronization](#home-folders-content-synchronization "#home-folders-content-synchronization")
- [Home Folder Formats](#home-folders-admin-folders "#home-folders-admin-folders")
- [Additional Resources](#home-folders-admin-additional "#home-folders-admin-additional")

#### Disable Home Folders

You can disable home folders for a directory without losing user content
already stored in home folders. Disabling home folders for a directory has the
following effects:

- Users who are connected to active streaming sessions for the directory
  receive an error message. They are informed that they can no longer
  store content in their home folder.
- Home folders do not appear for any new sessions that use the directory
  with home folders disabled.
- Disabling home folders for one directory does not disable it for other
  directories.
- Even if home folders are disabled for all directories, WorkSpaces Pools does
  not delete the user content.

To restore access to home folders for the directory, enable home folders again
by following the steps described earlier in this topic.

###### To disable home folders while creating a directory

- Follow the steps in [Configure SAML 2.0 and create a WorkSpaces Pools
  directory](create-directory-pools.md "create-directory-pools.md") and make sure that the
  **Enable Home Folders** option is cleared.

###### To disable home folders for an existing directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the left navigation pane, choose **Directories**,
   and select the directory for which to enable home folders.
3. Below the directories list, choose **Storage** and
   clear **Enable Home Folders**.
4. In the **Disable Home Folders** dialog box, type
   `CONFIRM` (case-sensitive) to confirm your choice, then
   choose **Disable**.

#### Amazon S3 Bucket Storage

WorkSpaces Pools manages user content stored in home folders by using Amazon S3 buckets
created in your account. For every AWS Region, WorkSpaces Pools creates a bucket in
your account. All user content generated from streaming sessions of directories
in that Region is stored in that bucket. The buckets are fully managed by the
service without any input or configuration from an administrator. The buckets
are named in a specific format as follows:

```
wspool-home-folder-`<region-code>`-`<account-id-without-hyphens>`-`<random-identifier>`
```

Where `<region-code>` is the AWS Region
code in which the directory is created and
`<account-id-without-hyphens>` is
your Amazon Web Services account ID, and `>random-identifier<` is a random
identifier number generated by the WorkSpaces service. The first part of the bucket name,
`wspool-home-folder-`, does not change across accounts or
Regions.

For example, if you enable home folders for directories in the US West
(Oregon) Region (us-west-2) on account number 123456789012, the service creates
an Amazon S3 bucket in that Region with the name shown. Only an administrator with
sufficient permissions can delete this bucket.

```
wspool-home-folder-us-west-2-123456789012
```

As mentioned earlier, disabling home folders for directories does not delete
any user content stored in the Amazon S3 bucket. To permanently delete user content,
an administrator with adequate access must do so from the Amazon S3 console.
WorkSpaces Pools adds a bucket policy that prevents accidental deletion of the
bucket.

#### Home Folder Content

Synchronization

When home folders are enabled, WorkSpaces Pools creates a unique folder for each
user in which to store their content. The folder is created as a unique Amazon S3
prefix that uses a hash of the user name within an S3 bucket for your Amazon Web Services
account and Region. After WorkSpaces Pools creates the home folder in Amazon S3, it copies
the accessed content in that folder from the S3 bucket to the WorkSpace. This
enables the user to access their home folder content quickly, from the WorkSpace
in the WorkSpace Pool, during their streaming session. Changes that you make to
a user’s home folder content in an S3 bucket and that the user makes to their
home folder content on a WorkSpace in the WorkSpace Pool are synchronized
between Amazon S3 and WorkSpaces Pools as follows.

1. At the beginning of a user’s WorkSpaces Pools streaming session, WorkSpaces Pools
   catalogs the home folder files that are stored for that user in the Amazon S3
   bucket for your Amazon Web Services account and Region.
2. A user’s home folder content is also stored on the WorkSpace in
   WorkSpaces Pools from which they stream. When a user accesses their home
   folder on the WorkSpace, the list of cataloged files is displayed.
3. WorkSpaces Pools downloads a file from the S3 bucket to the WorkSpace only
   after the user uses a streaming application to open the file during
   their streaming session.
4. After WorkSpaces Pools downloads the file to the WorkSpace, synchronization
   occurs after the file is accessed
5. If the user changes the file during their streaming session,
   WorkSpaces Pools uploads the new version of the file from the WorkSpace to the
   S3 bucket periodically or at the end of the streaming session. However,
   the file is not downloaded from the S3 bucket again during the streaming
   session.

The following sections describe synchronization behavior when you add,
replace, or remove a user's home folder file in Amazon S3.

###### Contents

- [Synchronization of files that you add to a user’s home folder in
  Amazon S3](#home-folders-content-synchronization-content-added-to-user-home-folder-in-S3 "#home-folders-content-synchronization-content-added-to-user-home-folder-in-S3")
- [Synchronization of files that you replace in a user’s home folder in
  Amazon S3](#home-folders-content-synchronization-content-replaced-in-user-home-folder-S3 "#home-folders-content-synchronization-content-replaced-in-user-home-folder-S3")
- [Synchronization of files that you remove from a user’s home folder in
  Amazon S3](#home-folders-content-synchronization-content-removed-from-user-home-folder-S3 "#home-folders-content-synchronization-content-removed-from-user-home-folder-S3")

##### Synchronization of files that you add to a user’s home folder in

Amazon S3

If you add a new file to a user’s home folder in an S3 bucket, WorkSpaces Pools
catalogs the file and displays it in the list of files in the user’s home
folder within a few minutes. However, the file isn’t downloaded from the S3
bucket to the WorkSpace until the user opens the file with an application
during their streaming session.

##### Synchronization of files that you replace in a user’s home folder in

Amazon S3

If a user opens a file in their home folder on the WorkSpace in the
WorkSpace Pool during their streaming session, and you replace the same
file in their home folder in an S3 bucket with a new version during that
user’s active streaming session, the new version of the file is not
immediately downloaded to the WorkSpace. The new version is downloaded from
the S3 bucket to the WorkSpace only after the user starts a new streaming
session and opens the file again.

##### Synchronization of files that you remove from a user’s home folder in

Amazon S3

If a user opens a file in their home folder on the WorkSpace in the
WorkSpace Pool during their streaming session, and you remove the file from
their home folder in an S3 bucket during that user’s active streaming
session, the file is removed from the WorkSpace after the user does either
of the following:

- Opens the home folder again
- Refreshes the home folder

#### Home Folder Formats

The hierarchy of a user folder depends on how a user launches a streaming
session, as described in the following section.

##### SAML 2.0

For sessions created using SAML federation, the user folder structure is
as follows:

```
`bucket-name`/user/federated/`user-id-SHA-256-hash`/
```

In this case, `user-id-SHA-256-hash`
is the folder name created using a lowercase SHA-256 hash hexadecimal string
generated from the `NameID` SAML attribute value passed in the
SAML federation request. To differentiate users who have the same name but
belong to two different domains, send the SAML request with
`NameID` in the format `domainname\username`. For
more information, see [Configure SAML 2.0 and create a WorkSpaces Pools
directory](create-directory-pools.md "create-directory-pools.md").

The following example folder structure applies to session access using
SAML federation with `NameID` SAMPLEDOMAIN\testuser, account ID
123456789012 in the US West (Oregon) Region:

```
wspool-home-folder-us-west-2-123456789012/user/federated/8dd9a642f511609454d344d53cb861a71190e44fed2B8aF9fde0C507012a9901
```

When part or all of the NameID string is capitalized (as the domain name
`SAMPLEDOMAIN` is in the example), WorkSpaces Pools
generates the hash value based on the capitalization used in the string.
Using this example, the hash value for SAMPLEDOMAIN\testuser is
8DD9A642F511609454D344D53CB861A71190E44FED2B8AF9FDE0C507012A9901. In the
folder for that user, this value is displayed in lowercase, as follows:
8dd9a642f511609454d344d53cb861a71190e44fed2B8aF9fde0C507012a9901.

You can identify the folder for a user by generating the SHA-256 hash
value of the `NameID` using websites or open source coding
libraries available online.

#### Additional Resources

For more information about managing Amazon S3 buckets and best practices, see the
following topics in the _Amazon Simple Storage Service User Guide_:

- You can provide offline access to user data for your users with Amazon S3
  policies. For more information, see [Amazon S3: Allows IAM Users Access to Their S3 Home Directory,
  Programmatically and In the Console](../../../IAM/latest/UserGuide/reference_policies_examples_s3_home-directory-console.md "../../../IAM/latest/UserGuide/reference_policies_examples_s3_home-directory-console.md") in the
  _IAM User Guide_.
- You can enable file versioning for content stored in Amazon S3 buckets used
  by WorkSpaces Pools. For more information, see [Using Versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md").
