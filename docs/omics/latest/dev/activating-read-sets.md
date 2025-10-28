AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Activating read sets in HealthOmics

You can activate read sets that are archived with the **start-read-set-activation-job**
API operation, or through the AWS CLI, as shown in the following example. Replace the `sequence
 store ID` and `read set id` with your sequence store
ID and read set IDs.

```
aws omics start-read-set-activation-job
     --sequence-store-id ``sequence store ID`` \
     --sources ``readSetId=read set ID`` ``readSetId=read set id_1`` ``read set id_2``
```

You receive a response that contains the activation job information, as shown in the following.

```
{
    "id": "12345678",
    "sequenceStoreId": "1234567890",
    "status": "SUBMITTED",
    "creationTime": "2022-10-22T00:50:54.670000+00:00"
}
```

After the activation job starts, you can monitor its progress with the
**get-read-set-activation-job** API operation. The following is an
example of how to use the AWS CLI to check your activation job status. Replace
`job ID` and `sequence
 store ID` with your sequence store ID and job IDs,
respectively.

```
aws omics get-read-set-activation-job --id ``job ID`` --sequence-store-id ``sequence store ID``
```

The response summarizes the activation job, as shown in the following.

```
{
    "id": 123567890,
    "sequenceStoreId": 123467890,
    "status": "SUBMITTED",
    "statusUpdateReason": "The job is submitted and will start soon.",
    "creationTime": "2022-10-22T00:50:54.670000+00:00",
    "sources": [
        {
            "readSetId": <reads set id_1>,
            "status": "NOT_STARTED",
            "statusUpdateReason": "The source is queued for the job."
        },
        {
            "readSetId": <read set id_2>,
            "status": "NOT_STARTED",
            "statusUpdateReason": "The source is queued for the job."
        }
    ]
}
```

You can check the status of an activation job with the **get-read-set-metadata** API
operation. Possible statuses are `ACTIVE`, `ACTIVATING`, and `ARCHIVED`. In the
following example, replace `sequence store ID` with your sequence store ID,
and replace `read set ID` with your read set ID.

```
aws omics get-read-set-metadata --sequence-store-id ``sequence store ID`` --id ``read set ID``
```

The following response shows you that the read set is active.

```
{
    "id": "12345678",
    "arn": "arn:aws:omics:us-west-2:555555555555:sequenceStore/1234567890/readSet/12345678",
    "sequenceStoreId": "0123456789",
    "subjectId": "mySubject",
    "sampleId": "mySample",
    "status": "ACTIVE",
    "name": "HG00100",
    "description": "HG00100 aligned to HG38 BAM",
    "fileType": "BAM",
    "creationTime": "2022-07-13T23:25:20Z",
    "sequenceInformation": {
        "totalReadCount": 1513467,
        "totalBaseCount": 163454436,
        "generatedFrom": "Pulled from SRA",
        "alignment": "ALIGNED"
    },
    "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/0123456789/reference/0000000001",
    "files": {
        "source1": {
            "totalParts": 2,
            "partSize":  10485760,
            "contentLength": 17112283,
            "s3Access": {
        "s3Uri": "s3://accountID-sequence store ID-ajdpi90jdas90a79fh9a8ja98jdfa9jf98-s3alias/592761533288/sequenceStore/2015356892/readSet/9515444019/import_source1.fastq.gz"
},
         },
        "index": {
            "totalParts": 1,
            "partSize": 53216,
            "contentLength": 10485760
            "s3Access": {
        "s3Uri": "s3://accountID-sequence store ID-ajdpi90jdas90a79fh9a8ja98jdfa9jf98-s3alias/592761533288/sequenceStore/2015356892/readSet/9515444019/import_source1.fastq.gz"
},
        }
    },
    "creationType": "IMPORT",
    "etag": {
        "algorithm": "BAM_MD5up",
        "source1": "d1d65429212d61d115bb19f510d4bd02"
    }
}
```

You can view all read set activation jobs by using **list-read-set-activation-jobs**, as
shown in the following example. In the following example, replace `sequence store
 ID` with your sequence store ID.

```
aws omics list-read-set-activation-jobs --sequence-store-id ``sequence store ID``
```

You receive the following response.

```
{
    "activationJobs": [
        {
            "id": 1234657890,
            "sequenceStoreId": "1234567890",
            "status": "COMPLETED",
            "creationTime": "2022-10-22T01:33:38.079000+00:00",
            "completionTime": "2022-10-22T01:34:28.941000+00:00"
        }
    ]
}
```
