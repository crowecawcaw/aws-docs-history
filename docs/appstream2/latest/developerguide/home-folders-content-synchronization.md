# Home Folder Content Synchronization

When home folders are enabled, WorkSpaces Applications creates a unique folder for each user in
which to store their content. The folder is created as a unique Amazon S3 prefix that
uses a hash of the user name within an S3 bucket for your Amazon Web Services account and
Region. After WorkSpaces Applications creates the home folder in Amazon S3, it copies the accessed
content in that folder from the S3 bucket to the fleet instance. This enables
the user to access their home folder content quickly, from the fleet instance,
during their streaming session. Changes that you make to a user’s home folder
content in an S3 bucket and that the user makes to their home folder content on
a fleet instance are synchronized between Amazon S3 and WorkSpaces Applications as follows.

1. At the beginning of a user’s WorkSpaces Applications streaming session, WorkSpaces Applications catalogs
   the home folder files that are stored for that user in the Amazon S3 bucket
   for your Amazon Web Services account and Region.
2. A user’s home folder content is also stored on the WorkSpaces Applications fleet
   instance from which they stream. When a user accesses their home folder
   on the WorkSpaces Applications fleet instance, the list of cataloged files is displayed.
3. WorkSpaces Applications downloads a file from the S3 bucket to the fleet instance only
   after the user uses a streaming application to open the file during
   their streaming session.
4. After WorkSpaces Applications downloads the file to the fleet instance, synchronization
   occurs after the file is accessed
5. If the user changes the file during their streaming session, WorkSpaces Applications uploads the new version of the file from the fleet instance to the
   S3 bucket periodically or at the end of the streaming session. However,
   the file is not downloaded from the S3 bucket again during the streaming
   session.
   The following sections describe synchronization behavior when you add,
   replace, or remove a user's home folder file in Amazon S3.

###### Contents

- [Synchronization of files that you add to a user’s home folder in Amazon S3](#home-folders-content-synchronization-content-added-to-user-home-folder-in-S3 "#home-folders-content-synchronization-content-added-to-user-home-folder-in-S3")
- [Synchronization of files that you replace in a user’s home folder in Amazon S3](#home-folders-content-synchronization-content-replaced-in-user-home-folder-S3 "#home-folders-content-synchronization-content-replaced-in-user-home-folder-S3")
- [Synchronization of files that you remove from a user’s home folder in Amazon S3](#home-folders-content-synchronization-content-removed-from-user-home-folder-S3 "#home-folders-content-synchronization-content-removed-from-user-home-folder-S3")

## Synchronization of files that you add to a user’s home folder in Amazon S3

If you add a new file to a user’s home folder in an S3 bucket, WorkSpaces Applications
catalogs the file and displays it in the list of files in the user’s home
folder within a few minutes. However, the file isn’t downloaded from the S3
bucket to the fleet instance until the user opens the file with an
application during their streaming session.

## Synchronization of files that you replace in a user’s home folder in Amazon S3

If a user opens a file in their home folder on the fleet instance during
their streaming session, and you replace the same file in their home folder
in an S3 bucket with a new version during that user’s active streaming
session, the new version of the file is not immediately downloaded to the
fleet instance. The new version is downloaded from the S3 bucket to the
fleet instance only after the user starts a new streaming session and opens
the file again.

## Synchronization of files that you remove from a user’s home folder in Amazon S3

If a user opens a file in their home folder on the fleet instance during
their streaming session, and you remove the file from their home folder in
an S3 bucket during that user’s active streaming session, the file is
removed from the fleet instance after the user does either of the following:

- Opens the home folder again
- Refreshes the home folder
