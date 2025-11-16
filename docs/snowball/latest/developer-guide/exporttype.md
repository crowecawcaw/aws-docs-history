AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Jobs to export data from Amazon S3 using a Snowball Edge device

###### Note

Tags and metadata are NOT currently supported, in other words, all tags and
metadata would be removed when exporting objects from S3 buckets.

Your data source for an export job is one or more Amazon S3 buckets. After the data for a
job part is moved from Amazon S3 to an AWS Snowball Edge device, you can download a job report. This
report alerts you to any objects that failed the transfer to the device. You can find
more information in your job's success and failure logs.

You can export any number of objects for each export job, using as many devices as it
takes to complete the transfer. Each AWS Snowball Edge device for an export job's job parts is
delivered one after another, with subsequent devices shipping to you after the previous
job part enters the **In transit to AWS** status.

When you copy objects into your on-premises data destination from a device using the
Amazon S3 adapter or the NFS mount point, those objects are saved as files. If you copy objects
into a location that already holds files, any existing files with the same names are
overwritten. The export job type is also capable of local storage and compute
functionality. This functionality uses the NFS interface or Amazon S3 adapter to read and write data,
and triggers Lambda functions based off of Amazon S3 PUT object API actions running locally on
the AWS Snowball Edge device.

When AWS receives a returned device, we completely erase it, following the NIST
800-88 standards.

###### Important

Data you want to export to a Snow device must be in Amazon S3. Any data in Amazon Glacier that you plan to export to the Snow device will have to be thawed or moved into the S3 storage class before it can be exported. Do this before creating the Snow export job.

Don't change, update, or delete the exported Amazon S3 objects until you can verify
that all of your contents for the entire job have been copied to your on-premises
data destination.

When you create an export job, you can export an entire Amazon S3 bucket or a specific
range of objects keys.

## Using Amazon S3 object keys when exporting data to a Snowball Edge device

When you create an export job in the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home "https://console.aws.amazon.com/snowfamily/home") or with the job management
API, you can export an entire Amazon S3 bucket or a specific range of objects keys.
Object key names uniquely identify objects in a bucket. If you export a range, you
define the length of the range by providing either an inclusive range beginning, an
inclusive range ending, or both.

Ranges are UTF-8 binary sorted. UTF-8 binary data is sorted in the following
way:

- The numbers 0–9 come before both uppercase and lowercase English
  characters.
- Uppercase English characters come before all lowercase English
  characters.
- Lowercase English characters come last when sorted against uppercase
  English characters and numbers.
- Special characters are sorted among the other character sets.

For more information about the specifics of UTF-8, see [UTF-8 on Wikipedia](https://en.wikipedia.org/wiki/UTF-8 "https://en.wikipedia.org/wiki/UTF-8").

### Examples of using Amazon S3 object keys when exporting data to a Snowball Edge device

Assume that you have a bucket containing the following objects and prefixes,
sorted in UTF-8 binary order:

- 01
- Aardvark
- Aardwolf
- Aasvogel/apple
- Aasvogel/arrow/object1
- Aasvogel/arrow/object2
- Aasvogel/banana
- Aasvogel/banker/object1
- Aasvogel/banker/object2
- Aasvogel/cherry
- Banana
- Car

| Specified range beginning | Specified range ending | Objects in the range that will be exported                                                                                                                                                              |
| ------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (none)                    | (none)                 | All of the objects in your bucket                                                                                                                                                                       |
| (none)                    | Aasvogel               | 01<br>Aardvark<br>Aardwolf<br>Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana<br>Aasvogel/banker/object1<br>Aasvogel/banker/object2<br>Aasvogel/cherry            |
| (none)                    | Aasvogel/banana        | 01<br>Aardvark<br>Aardwolf<br>Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana                                                                                     |
| Aasvogel                  | (none)                 | Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana<br>Aasvogel/banker/object1<br>Aasvogel/banker/object2<br>Aasvogel/cherry<br>Banana<br>Car                         |
| Aardwolf                  | (none)                 | Aardwolf<br>Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana<br>Aasvogel/banker/object1<br>Aasvogel/banker/object2<br>Aasvogel/cherry<br>Banana<br>Car             |
| Aar                       | (none)                 | Aardvark<br>Aardwolf<br>Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana<br>Aasvogel/banker/object1<br>Aasvogel/banker/object2<br>Aasvogel/cherry<br>Banana<br>Car |
| car                       | (none)                 | No objects are exported, and you get an error message when you try to create the job. Note<br>that *car<br>• is sorted below<br>*Car<br>• according to<br>UTF-8 binary values.                          |
| Aar                       | Aarrr                  | Aardvark<br>Aardwolf                                                                                                                                                                                    |
| Aasvogel/arrow            | Aasvogel/arrox         | Aasvogel/arrow/object1<br>Aasvogel/arrow/object2                                                                                                                                                        |
| Aasvogel/apple            | Aasvogel/banana        | Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana                                                                                                                   |
| Aasvogel/apple            | Aasvogel/banker        | Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana<br>Aasvogel/banker/object1<br>Aasvogel/banker/object2                                                             |
| Aasvogel/apple            | Aasvogel/cherry        | Aasvogel/apple<br>Aasvogel/arrow/object1<br>Aasvogel/arrow/object2<br>Aasvogel/banana<br>Aasvogel/banker/object1<br>Aasvogel/banker/object2<br>Aasvogel/cherry                                          |

Assume you have these three buckets and want to copy all objects from **folder2**.

- s3://bucket/folder1/
- s3://bucket/folder2/
- s3://bucket/folder3/

| Specified range beginning | Specified range ending | Objects in the range that will be exported |
| ------------------------- | ---------------------- | ------------------------------------------ |
| folder2/                  | folder2/               | All of the objects in bucket **folder2**.  |

## Best practices for jobs exporting data from Amazon S3 to a Snowball Edge device

- Ensure data is in Amazon S3, batch small files before ordering the
  job
- Ensure key ranges are specified in the export job definition if you have
  millions of objects in your bucket
- Update object keys to remove slash in the name as objects with trailing
  slashes in their names (/ or \) are not transferred to Snowball Edge
- For S3 buckets, the object length limitation is 255 characters.
- For S3 buckets that are version‐enabled, only the current version of objects are exported.
- Delete markers are not exported.
