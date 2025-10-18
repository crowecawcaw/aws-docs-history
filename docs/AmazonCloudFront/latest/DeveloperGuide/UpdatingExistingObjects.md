# Use file versioning to update or remove
 content with a CloudFront distribution

To update existing content that CloudFront is set up to distribute for you, we recommend that you use a version identifier in file names or in folder names. This helps give you 
 control over managing the content that CloudFront serves.


## Update existing files using versioned file names


When you update existing files in a CloudFront distribution, we recommend that you include
 some sort of version identifier either in your file names or in your directory names to
 give yourself better control over your content. This identifier might be a date-time stamp,
 a sequential number, or some other method of distinguishing two versions of the same object. 


For example, instead of naming a graphic file image.jpg, you might call it image\_1.jpg.
 When you want to start serving a new version of the file, you'd name the new file
 image\_2.jpg, and you'd update the links in your web application or website to point to
 image\_2.jpg. Alternatively, you might put all graphics in an images\_v1 directory and, when
 you want to start serving new versions of one or more graphics, you'd create a new images\_v2
 directory, and you'd update your links to point to that directory. With versioning, you
 don't have to wait for an object to expire before CloudFront begins to serve a new version of it,
 and you don't have to pay for object invalidation.


Even if you version your files, we still recommend that you set an expiration date.
 For more information, see [Manage how long content stays in the cache
 (expiration)](Expiration.md "Expiration.md").


###### Note

Specifying versioned file names or directory names is not related to Amazon S3 object
 versioning.


## Remove content so CloudFront won’t distribute it


You can remove files from your origin that you no longer want to be included in your CloudFront
 distribution. However, CloudFront will continue to show viewers content from the edge
 cache until the files expire. 
 


If you want to remove a file right away, you must do one of the following:



* **Use file versioning.** When you use versioning, 
 different versions of a file have different names that you can use in your CloudFront distribution, 
 to change which file is returned to viewers. For more information, see [Update existing files using versioned file names](#ReplacingObjects "#ReplacingObjects").
* **Invalidate the file.** For more information, 
 see [Invalidate files to remove content](Invalidation.md "Invalidation.md").
