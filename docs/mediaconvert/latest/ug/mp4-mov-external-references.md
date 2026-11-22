

# External references in MP4 and MOV inputs

The MP4 and MOV container formats allow a file to store its media data outside of the file itself. In place of the media data, the file contains a data reference entry that identifies where the media data is stored. A file built this way isn't self-contained. Authoring and editing applications create these files, sometimes called reference movies, so that large media files aren't duplicated on disk.

When your input contains a data reference entry that points outside of the file, MediaConvert reads the referenced media and includes it in your output. MediaConvert doesn't validate or restrict the location that the entry points to, and doesn't limit it to the bucket or prefix of your input file. When the referenced location is an Amazon S3 object, MediaConvert reads it using the MediaConvert service role that you specify for your job. For more information about the service role, see [Setting up IAM permissions](iam-role.md).

## Security considerations for inputs from other sources
<a name="mp4-mov-external-references-security"></a>

Whoever creates an input file chooses its data reference entries. The person who submits the job doesn't. If your application transcodes files that you receive from your customers, or from any other source that you don't control, the creator of a file can cause MediaConvert to read media from a location that you didn't choose.

When you transcode files from sources that you don't control, we recommend the following:
+ Before you submit a file, check whether it contains data reference entries that point outside of the file. Reject these files, or convert them to self-contained files first. A tool that converts the file resolves the same references, so run it in an environment that doesn't have access to your private resources.
+ Scope your MediaConvert service role to only the Amazon S3 locations that your workflow requires. A data reference entry can still point to any object that the role can read, including other files in your input location.
+ Use a separate service role for jobs that process files from other sources, and don't grant that role access to your own content.