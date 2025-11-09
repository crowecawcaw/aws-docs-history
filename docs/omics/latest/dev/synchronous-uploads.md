# Direct upload to a HealthOmics sequence store

We recommend that you use the HealthOmics Transfer Manager to add files to your sequence store. For more information
about using Transfer Manager, see this [GitHub
Repository](https://github.com/awslabs/amazon-omics-tools/ "https://github.com/awslabs/amazon-omics-tools/"). You can also upload your read sets directly to a sequence store through the direct upload API
operations.

Direct upload read sets exist first in `PROCESSING_UPLOAD` state. This
means that the file parts are currently being uploaded, and you can access the read
set metadata. After the parts are uploaded and the checksums are validated, the read
set becomes `ACTIVE` and behaves the same as an imported read set.

If the direct upload fails, the read set status is shown as `UPLOAD_FAILED`. You can configure an
Amazon S3 bucket as a fallback location for files that fail to upload. Fallback locations are available for sequence
stores created after May 15, 2023.

###### Topics

- [Direct upload to a sequence store using the AWS CLI](#synchronous-uploads-api "#synchronous-uploads-api")
- [Configure a fallback location](#synchronous-uploads-fallback "#synchronous-uploads-fallback")

## Direct upload to a sequence store using the AWS CLI

To begin, start a multipart upload. You can do this by using the AWS CLI, as shown
in the following example.

###### To direct upload using AWS CLI commands

1. Create the parts by separating your data, as shown in the following example.

```
 split -b 100MiB SRR233106_1.filt.fastq.gz source1_part_
```

2. After your source files are in parts, create a multipart read set upload, as shown in the following
   example. Replace `sequence store ID` and the other parameters with your
   sequence store ID and other values.

```
aws omics create-multipart-read-set-upload \
--sequence-store-id ``sequence store ID`` \
--name ``upload name`` \
--source-file-type ``FASTQ`` \
--subject-id ``subject ID`` \
--sample-id ``sample ID`` \
--description "FASTQ for HG00146" ``"description of upload"`` \
--generated-from "1000 Genomes"``"source of imported files"``
```

You get the `uploadID` and other metadata in the response. Use the `uploadID`
for the next step of the upload process.

```
{
"sequenceStoreId": "1504776472",
"uploadId": "7640892890",
"sourceFileType": "FASTQ",
"subjectId": "mySubject",
"sampleId": "mySample",
"generatedFrom": "1000 Genomes",
"name": "HG00146",
"description": "FASTQ for HG00146",
"creationTime": "2023-11-20T23:40:47.437522+00:00"
}
```

3. Add your read sets to the upload. If your file is small enough, you only have to perform this step once.
   For larger files, you perform this step for each part of your file. If you upload a new part by using a
   previously used part number, it overwrites the previously uploaded part.

In the following example, replace `sequence store ID`,
`upload ID`, and the other parameters with your values.

```
aws omics upload-read-set-part \
--sequence-store-id ``sequence store ID`` \
--upload-id ``upload ID`` \
--part-source ``SOURCE1`` \
--part-number ``part number`` \
--payload  source1/source1_part_aa.fastq.gz
```

The response is an ID that you can use to verify that the uploaded file matches the file you
intended.

```
{
"checksum": "984979b9928ae8d8622286c4a9cd8e99d964a22d59ed0f5722e1733eb280e635"
}
```

4. Continue uploading the parts of your file, if necessary. To verify that your read sets have been
   uploaded, use the **list-read-set-upload-parts** API operation, as shown in the following. In the
   following example, replace `sequence store ID` , `upload
ID`, and the `part source` with your own
   input.

```
aws omics list-read-set-upload-parts \
 --sequence-store-id ``sequence store ID`` \
 --upload-id ``upload ID`` \
 --part-source ``SOURCE1``
```

The response returns the number of read sets, the size, and the timestamp for when
it was most recently updated.

```
{
"parts": [
    {
        "partNumber": 1,
        "partSize": 104857600,
        "partSource": "SOURCE1",
        "checksum": "MVMQk+vB9C3Ge8ADHkbKq752n3BCUzyl41qEkqlOD5M=",
        "creationTime": "2023-11-20T23:58:03.500823+00:00",
        "lastUpdatedTime": "2023-11-20T23:58:03.500831+00:00"
    },
    {
        "partNumber": 2,
        "partSize": 104857600,
        "partSource": "SOURCE1",
        "checksum": "keZzVzJNChAqgOdZMvOmjBwrOPM0enPj1UAfs0nvRto=",
        "creationTime": "2023-11-21T00:02:03.813013+00:00",
        "lastUpdatedTime": "2023-11-21T00:02:03.813025+00:00"
    },
    {
        "partNumber": 3,
        "partSize": 100339539,
        "partSource": "SOURCE1",
        "checksum": "TBkNfMsaeDpXzEf3ldlbi0ipFDPaohKHyZ+LF1J4CHk=",
        "creationTime": "2023-11-21T00:09:11.705198+00:00",
        "lastUpdatedTime": "2023-11-21T00:09:11.705208+00:00"
    }
]
}
```

5. To view all active multipart read set uploads, use
   **list-multipart-read-set-uploads,** as shown in the following. Replace
   `sequence store ID` with the ID for your own sequence store.

```
aws omics list-multipart-read-set-uploads --sequence-store-id ``sequence store ID``

```

This API only returns multipart read set uploads that are in progress. After the ingested read sets
are `ACTIVE`, or if the upload has failed, the upload will not be returned in the response to the
**list-multipart-read-set-uploads** API. To view active read sets, use the
**list-read-sets** API. An example response for
**list-multipart-read-set-uploads** is shown in the following.

```
{
"uploads": [
    {
        "sequenceStoreId": "1234567890",
        "uploadId": "8749584421",
        "sourceFileType": "FASTQ",
        "subjectId": "mySubject",
        "sampleId": "mySample",
        "generatedFrom": "1000 Genomes",
        "name": "HG00146",
        "description": "FASTQ for HG00146",
        "creationTime": "2023-11-29T19:22:51.349298+00:00"
    },
    {
        "sequenceStoreId": "1234567890",
        "uploadId": "5290538638",
        "sourceFileType": "BAM",
        "subjectId": "mySubject",
        "sampleId": "mySample",
        "generatedFrom": "1000 Genomes",
        "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/8168613728/reference/2190697383",
        "name": "HG00146",
        "description": "BAM for HG00146",
        "creationTime": "2023-11-29T19:23:33.116516+00:00"
    },
    {
        "sequenceStoreId": "1234567890",
        "uploadId": "4174220862",
        "sourceFileType": "BAM",
        "subjectId": "mySubject",
        "sampleId": "mySample",
        "generatedFrom": "1000 Genomes",
        "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/8168613728/reference/2190697383",
        "name": "HG00147",
        "description": "BAM for HG00147",
        "creationTime": "2023-11-29T19:23:47.007866+00:00"
    }
]
}
```

6. After you upload all parts of your file, use **complete-multipart-read-set-upload** to
   conclude the upload process, as shown in the following example. Replace `sequence store
ID`, `upload ID`, and the parameter for parts
   with your own values.

```
aws omics complete-multipart-read-set-upload \
--sequence-store-id ``sequence store ID`` \
--upload-id ``upload ID`` \
--parts ``'[{"checksum":"gaCBQMe+rpCFZxLpoP6gydBoXaKKDA/Vobh5zBDb4W4=","partNumber":1,"partSource":"SOURCE1"}]'``
```

The response for **complete-multipart-read-set-upload** is the
read set IDs for your imported read sets.

```
{
"readSetId": "0000000001"
}
```

7. To stop the upload, use **abort-multipart-read-set-upload** with the upload ID to end
   the upload process. Replace `sequence store ID` and
   `upload ID` with your own parameter values.

```
aws omics abort-multipart-read-set-upload \
--sequence-store-id ``sequence store ID`` \
--upload-id ``upload ID``
```

8. After the upload is complete, retrieve your data from the read set by using
   **get-read-set**, as shown in the following. If the upload is still processing,
   **get-read-set** returns limited metadata, and the generated index files are unavailable.
   Replace `sequence store ID` and the other parameters with your own
   input.

```
aws omics get-read-set
 --sequence-store-id ``sequence store ID`` \
 --id ``read set ID`` \
 --file ``SOURCE1`` \
 --part-number 1 ``myfile.fastq.gz``
```

9. To check the metadata, including the status of your upload, use the
   **get-read-set-metadata** API operation.

```
aws omics get-read-set-metadata --sequence-store-id ``sequence store ID`` --id ``read set ID``
```

The response includes metadata details such as the file type, the reference ARN, the number of files,
and the length of the sequences. It also includes the status. Possible statuses are
`PROCESSING_UPLOAD`, `ACTIVE`, and `UPLOAD_FAILED`.

```
{
"id": "0000000001",
"arn": "arn:aws:omics:us-west-2:555555555555:sequenceStore/0123456789/readSet/0000000001",
"sequenceStoreId": "0123456789",
"subjectId": "mySubject",
"sampleId": "mySample",
"status": "PROCESSING_UPLOAD",
"name": "HG00146",
"description": "FASTQ for HG00146",
"fileType": "FASTQ",
"creationTime": "2022-07-13T23:25:20Z",
"files": {
    "source1": {
        "totalParts": 5,
        "partSize": 123456789012,
        "contentLength": 6836725,

    },
    "source2": {
        "totalParts": 5,
        "partSize": 123456789056,
        "contentLength": 6836726
    }
},
'creationType": "UPLOAD"
}
```

## Configure a fallback location

When you create or update a sequence store, you can configure an Amazon S3 bucket as the fallback location for
files that fail to upload. The file parts for those read sets are transferred to the fallback location. Fallback
locations are available for sequence stores created after May 15, 2023.

Create an Amazon S3 bucket policy to grant HealthOmics write access to the Amazon S3 fallback location, as shown in the following
example:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "omics.amazonaws.com"
    },
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
}
```

If the Amazon S3 bucket for fallback or access logs uses a customer managed key, add the following permissions
to the key policy:

```
 {
    "Sid": "Allow use of key",
    "Effect": "Allow",
    "Principal": {
        "Service": "omics.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*"
}
```
