

# Frame capture destination
<a name="framecapture-destinations"></a>

The following fields configure the location and names of the frame capture files (the destination).
+ **Output group** – **Frame capture group destination** section
+ **Output group** – **Frame capture settings** – **CDN settings**

  **Output settings** – **Name modifier**

You must design the destination path or paths for the output. You must then enter the different portions of the path into the appropriate fields on the console.

## Design the path for the output destination
<a name="framecapture-about-destination-path"></a>

**To design the path**
+ Design the destination path or paths, following this syntax:

  `protocol bucket folders baseFilename nameModifier counter extension`

  For example, for a standard channel:

  `s3ssl://amzn-s3-demo-bucket1/sports-thumbnails/delivery/curling-20180820.00000.jpg`

  `s3ssl://amzn-s3-demo-bucket1/sports-thumbnails/backup/curling-20180820.00000.jpg`

If you have two destinations, the destination paths must be different from each other in some way. At least one of the portions of one path must be different from the other. It is acceptable for all the portions to be different.

The following table maps each portion in the example to the portion in the syntax.


| Portion of the URL | Example | Comment | 
| --- | --- | --- | 
| protocol | s3ssl:// | The protocol is always s3ssl:// because the destination for a Frame capture output is always an S3 bucket. | 
| bucket portion of the path | amzn-s3-demo-bucket1 | With MediaLive, the S3 bucket name must not use dot notation, which means it mustn't use . (dot) between the words in the bucket name.  | 
| folders portion of the path | sports-thumbnails/delivery/ | The folders can be present or not, and can be as long as you want.The folders must always end with a slash. | 
| baseFilename | curling | Don't terminate the file name with a slash. | 
| nameModifier | -20180820 | The modifier is optional for an Frame capture output. | 
| delimiter before the counter | . | MediaLive automatically inserts this delimiter. | 
| counter | 00000 | MediaLive automatically generates this counter. Initially, this is a five-digit number starting at 00000, and increasing by 1. So 00000, 00001, 00002 and so on. After 99999, the next number is 100000 (six digits), then 100001, 100002, and so on. Then from 999999 to 1000000 (seven digits), and so on. | 
| dot before the extension | . | MediaLive automatically inserts this dot. | 
| extension | jpg | Always jpg. | 

## Complete the fields on the console
<a name="framecapture-specify-destination"></a>

**To specify the location for the output**

1. Enter the different portions of the destination in the appropriate fields.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/framecapture-destinations.html)

1. Leave the **Credentials** section blank in both the **Frame capture group destinations** sections. MediaLive has permission to write to the S3 bucket via the trusted entity. Someone in your organization should have already set up these permissions. For more information, see [Access requirements for the trusted entity](trusted-entity-requirements.md).

1. Complete the **CDN settings** field only if MediaLive must set a canned ACL whenever it sends this output to the Amazon S3 bucket.

   Use of a canned ACL typically only applies if your organization is not the owner of the Amazon S3 bucket. You should have discussed the use of a canned ACL with the bucket owner when you discussed the [destination for the output](archive-op-origin-server-s3.md#setting-dss-archive-canned-acl).