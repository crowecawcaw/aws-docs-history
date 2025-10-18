# Invalidate files to remove content

If you need to remove a file from CloudFront edge caches before it expires, you can do one
 of the following:


* Invalidate the file from edge caches. The next time a viewer requests the
 file, CloudFront returns to the origin to fetch the latest version of the file.
* Use file versioning to serve a different version of the file that has a
 different name. For more information, see [Update existing files using versioned file names](UpdatingExistingObjects.md#ReplacingObjects "UpdatingExistingObjects.md#ReplacingObjects").
###### Topics

* [Choose between invalidating files and
 using versioned file names](#Invalidation_Expiration "#Invalidation_Expiration")
* [Determine which files to
 invalidate](invalidation-access-logs.md "invalidation-access-logs.md")
* [What you need to know when invalidating files](invalidation-specifying-objects.md "invalidation-specifying-objects.md")
* [Invalidate files](Invalidation_Requests.md "Invalidation_Requests.md")
* [Concurrent invalidation request maximum](InvalidationLimits.md "InvalidationLimits.md")
* [Pay for file invalidation](PayingForInvalidation.md "PayingForInvalidation.md")

## Choose between invalidating files and
 using versioned file names


To control the versions of files that are served from your distribution, you can
 either invalidate files or give them versioned file names. If you want to update
 your files frequently, we recommend that you primarily use file versioning for the
 following reasons:



* Versioning enables you to control which file a request returns even when
 the user has a version cached either locally or behind a corporate caching
 proxy. If you invalidate the file, the user might continue to see the old
 version until it expires from those caches.
* CloudFront access logs include the names of your files, so versioning makes it
 easier to analyze the results of file changes.
* Versioning provides a way to serve different versions of files to
 different users.
* Versioning simplifies rolling forward and back between file
 revisions.
* Versioning is less expensive. You still have to pay for CloudFront to transfer
 new versions of your files to edge locations, but you don't have to pay for
 invalidating files.

For more information about file versioning, see [Update existing files using versioned file names](UpdatingExistingObjects.md#ReplacingObjects "UpdatingExistingObjects.md#ReplacingObjects").
