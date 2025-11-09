# Creating a HealthOmics reference store

A reference store in HealthOmics is a data store for the storage of reference genomes.
You can have a single reference store in each AWS account and Region.
You can create a reference store using the console or CLI.

###### Topics

- [Creating a reference
  store using the console](#console-create-reference-store "#console-create-reference-store")
- [Creating a reference
  store using the CLI](#api-create-reference-store "#api-create-reference-store")

## Creating a reference

store using the console

###### To create a reference store

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Reference store**.
3. Choose **Reference
   genomes** from the Genomics data storage options.
4. You can either choose a previously imported reference genome or import
   a new one. If you haven't imported a reference genome,choose
   **Import reference genome** in the top
   right.
5. On the **Create reference genome import job** page,
   choose either the **Quick create** or **Manual
   create** option to create a reference store, and then
   provide the following information.
   - **Reference genome name** - A unique name for
     this store.
   - **Description** (optional) - A description of
     this reference store.
   - **IAM Role** - Select a role with access to
     your reference genome.
   - **Reference from Amazon S3** - Select your
     reference sequence file in an Amazon S3 bucket.
   - **Tags** (optional) - Provide up to 50 tags
     for this reference store.

## Creating a reference

store using the CLI

The following example shows you how to create a reference store by using the AWS CLI. You can have one
reference store per AWS Region.

Reference stores support storage of FASTA files with the extensions `.fasta`, `.fa`,
`.fas`, `.fsa`, `.faa`, `.fna`, `.ffn`,
`.frn`, `.mpfa`, `.seq`, `.txt`. The `bgzip` version
of these extensions is also supported.

In the following example, replace `reference store name` with the
name you've chosen for your reference store.

```
aws omics create-reference-store --name ``"reference store name"``
```

You receive a JSON response with the reference store ID and name, the ARN, and the
timestamp of when your reference store was created.

```
{
    "id": "3242349265",
    "arn": "arn:aws:omics:us-west-2:555555555555:referenceStore/3242349265",
    "name": "MyReferenceStore",
    "creationTime": "2022-07-01T20:58:42.878Z"
}
```

You can use the reference store ID in additional AWS CLI commands. You can retrieve the list of
reference store IDs linked to your account by using the **list-reference-stores** command, as
shown in the following example.

```
aws omics list-reference-stores
```

In response, you receive the name of your newly created reference store.

```
{
    "referenceStores": [
        {
              "id": "3242349265",
              "arn": "arn:aws:omics:us-west-2:555555555555:referenceStore/3242349265",
              "name": "MyReferenceStore",
             "creationTime": "2022-07-01T20:58:42.878Z"
         }
     ]
}
```

After you create a reference store, you can create import jobs to load genomic reference files into
it. To do so, you must use or create an IAM role to access the data. The following is an example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetBucketLocation"

 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket1",
 "arn:aws:s3:::amzn-s3-demo-bucket1/*"
 ]
 }
 ]
}`

```

You must also have a trust policy similar to the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "omics.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You can now import a reference genome. This example uses Genome Reference Consortium Human Build 38
(hg38), which is open access and available from the [Registry of Open
Data on AWS](https://registry.opendata.aws/ "https://registry.opendata.aws/"). The bucket that hosts this data is based in US East (Ohio). To use buckets in other
AWS Regions, you can copy the data to an Amazon S3 bucket hosted in your Region. Use the following AWS CLI command to
copy the genome to your Amazon S3 bucket.

```
aws s3 cp s3://broad-references/hg38/v0/Homo_sapiens_assembly38.fasta s3://amzn-s3-demo-bucket
```

You can then begin your import job. Replace `reference store
 ID`, `role ARN`, and `source file
 path` with your own input.

```
aws omics start-reference-import-job --reference-store-id ``reference store ID`` --role-arn ``role ARN`` --sources ``source file path``
```

After the data is imported, you receive the following response in JSON.

```
{
        "id": "7252016478",
        "referenceStoreId": "3242349265",
        "roleArn": "arn:aws:iam::111122223333:role/OmicsReferenceImport",
        "status": "CREATED",
        "creationTime": "2022-07-01T21:15:13.727Z"
}
```

You can monitor the status of a job by using the following command. In the following example, replace
`reference store ID` and `job
 ID` with your reference store ID and the job ID that you want to learn more about.

```
aws omics get-reference-import-job --reference-store-id ``reference store ID`` --id ``job ID``
```

In response, you receive a response with the details for that reference store and
its status.

```
{
    "id": "7252016478",
    "referenceStoreId": "3242349265",
    "roleArn": "arn:aws:iam::555555555555:role/OmicsReferenceImport",
    "status": "RUNNING",
    "creationTime": "2022-07-01T21:15:13.727Z",
    "sources": [
        {
            "sourceFile": "s3://amzn-s3-demo-bucket/Homo_sapiens_assembly38.fasta",
            "status": "IN_PROGRESS",
            "name": "MyReference"
        }
    ]
}
```

You can also find the reference that was imported by listing your references and filtering them based
on the reference name. Replace `reference store ID` with your reference
store ID, and add an optional filter to narrow the list.

```
aws omics list-references --reference-store-id ``reference store ID`` --filter name=`MyReference`
```

In response, you receive the following information.

```
{
    "references": [
        {
            "id": "1234567890",
            "arn": "arn:aws:omics:us-west-2:555555555555:referenceStore/1234567890/reference/1234567890",
            "referenceStoreId": "12345678",
            "md5": "7ff134953dcca8c8997453bbb80b6b5e",
            "status": "ACTIVE",
            "name": "MyReference",
            "creationTime": "2022-07-02T00:15:19.787Z",
            "updateTime": "2022-07-02T00:15:19.787Z"
        }
    ]
}
```

To learn more about the reference metadata, use the **get-reference-metadata** API
operation. In the following example, replace `reference store ID` with
your reference store ID and `reference ID` with the reference ID that you
want to learn more about.

```
aws omics get-reference-metadata --reference-store-id ``reference store ID`` --id ``reference ID``
```

You receive the following information in response.

```
{
    "id": "1234567890",
    "arn": "arn:aws:omics:us-west-2:555555555555:referenceStore/referencestoreID/reference/referenceID",
    "referenceStoreId": "1234567890",
    "md5": "7ff134953dcca8c8997453bbb80b6b5e",
    "status": "ACTIVE",
    "name": "MyReference",
    "creationTime": "2022-07-02T00:15:19.787Z",
    "updateTime": "2022-07-02T00:15:19.787Z",
    "files": {
        "source": {
            "totalParts": 31,
            "partSize": 104857600,
            "contentLength": 3249912778
        },
        "index": {
            "totalParts": 1,
            "partSize": 104857600,
            "contentLength": 160928
        }
    }
}
```

You can also download parts of the reference file by using **get-reference**. In the
following example, replace `reference store ID` with your reference store
ID and `reference ID` with the reference ID that you want to download
from.

```
aws omics get-reference --reference-store-id ``reference store ID`` --id ``reference ID`` --part-number 1 outfile.fa
```
