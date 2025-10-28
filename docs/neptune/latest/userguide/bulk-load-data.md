# Example: Loading Data into a Neptune DB Instance

This example shows how to load data into Amazon Neptune. Unless stated otherwise, you must
follow these steps from an Amazon Elastic Compute Cloud (Amazon EC2) instance in the same Amazon Virtual Private Cloud (VPC) as your
Neptune DB instance.

## Prerequisites for the Data Loading Example

Before you begin, you must have the following:

- A Neptune DB instance.

For information about launching a Neptune DB instance, see [Creating an Amazon Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md").

- An Amazon Simple Storage Service (Amazon S3) bucket to put the data files in.

You can use an existing bucket. If you don't have an S3 bucket, see [Create a Bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the _[Amazon S3 Getting Started Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")_.

- Graph data to load, in one of the formats supported by the Neptune loader:

If you are using Gremlin to query your graph, Neptune can load data
in a comma-separated-values (`CSV`) format, as described in
[Gremlin load data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md").

If you are using openCypher to query your graph, Neptune can also
load data in an openCypher-specific `CSV` format, as described
in [Load format for openCypher data](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md").

If you are using SPARQL, Neptune can load data in a number of RDF
formats, as described in [RDF load data formats](bulk-load-tutorial-format-rdf.md "bulk-load-tutorial-format-rdf.md").

- An IAM role for the Neptune DB instance to assume that has an IAM policy that allows
  access to the data files in the S3 bucket. The policy must grant Read and List
  permissions.

For information about creating a role that has access to Amazon S3 and then associating
it with a Neptune cluster, see [Prerequisites: IAM Role and Amazon S3 Access](bulk-load-tutorial-IAM.md "bulk-load-tutorial-IAM.md").

###### Note

The Neptune `Load` API needs read access to the data files only. The
IAM policy doesn't need to allow write access or access to the entire bucket.

- An Amazon S3 VPC endpoint. For more information, see the [Creating an Amazon S3 VPC Endpoint](#bulk-load-prereqs-s3 "#bulk-load-prereqs-s3") section.

### Creating an Amazon S3 VPC Endpoint

The Neptune loader requires a VPC endpoint for Amazon S3.

###### To set up access for Amazon S3

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left navigation pane, choose
   **Endpoints**.
3. Choose **Create Endpoint**.
4. Choose the **Service Name**
   `com.amazonaws.`region`.s3`.

###### Note

If the Region here is incorrect, make sure that the console Region is correct. 5. Choose the VPC that contains your Neptune DB instance. 6. Select the check box next to the route tables that are associated with the subnets
related to your cluster. If you only have one route table, you must select that
box. 7. Choose **Create Endpoint**.

For information about creating the endpoint, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md#create-vpc-endpoint "../../../vpc/latest/userguide/vpc-endpoints.md#create-vpc-endpoint") in the
_Amazon VPC User Guide_. For information about the limitations of VPC
endpoints, [VPC Endpoints for
Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md").

###### To load data into a Neptune DB instance

1. Copy the data files to an Amazon S3 bucket. The S3 bucket must be in the same AWS Region as
   the cluster that loads the data.

You can use the following AWS CLI command to copy the files to the bucket.

###### Note

This command does not need to be run from the Amazon EC2 instance.

```
aws s3 cp `data-file-name` s3://`bucket-name`/`object-key-name`
```

###### Note

In Amazon S3, an **object key name** is the entire path of a
file, including the file name.

_Example:_ In the command `aws s3 cp
 datafile.txt s3://examplebucket/mydirectory/datafile.txt`, the object key name is
**`mydirectory/datafile.txt`**.

Alternatively, you can use the AWS Management Console to upload files to the S3 bucket. Open the
Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"), and
choose a bucket. In the upper-left corner, choose **Upload** to upload
files. 2. From a command line window, enter the following to run the Neptune loader, using the
correct values for your endpoint, Amazon S3 path, format, and IAM role ARN.

The `format` parameter can be any of the following values: `csv`
for Gremlin, `opencypher` for openCypher, or `ntriples`,
`nquads`, `turtle`, and `rdfxml` for RDF. For information
about the other parameters, see [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md").

For information about finding the hostname of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md")
section.

The Region parameter must match the Region of the cluster and the S3 bucket.

Amazon Neptune is available in the following AWS Regions:

    * US East (N. Virginia):   `us-east-1`
    * US East (Ohio):   `us-east-2`
    * US West (N. California):   `us-west-1`
    * US West (Oregon):   `us-west-2`
    * Canada (Central):   `ca-central-1`
    * Canada West (Calgary):   `ca-west-1`
    * South America (São Paulo):   `sa-east-1`
    * Europe (Stockholm):   `eu-north-1`
    * Europe (Spain):   `eu-south-2`
    * Europe (Ireland):   `eu-west-1`
    * Europe (London):   `eu-west-2`
    * Europe (Paris):   `eu-west-3`
    * Europe (Frankfurt):   `eu-central-1`
    * Middle East (Bahrain):   `me-south-1`
    * Middle East (UAE):   `me-central-1`
    * Israel (Tel Aviv):   `il-central-1`
    * Africa (Cape Town):   `af-south-1`
    * Asia Pacific (Hong Kong):   `ap-east-1`
    * Asia Pacific (Tokyo):   `ap-northeast-1`
    * Asia Pacific (Seoul):   `ap-northeast-2`
    * Asia Pacific (Osaka):   `ap-northeast-3`
    * Asia Pacific (Singapore):   `ap-southeast-1`
    * Asia Pacific (Sydney):   `ap-southeast-2`
    * Asia Pacific (Jakarta):   `ap-southeast-3`
    * Asia Pacific (Melbourne):   `ap-southeast-4`
    * Asia Pacific (Malaysia):   `ap-southeast-5`
    * Asia Pacific (Mumbai):   `ap-south-1`
    * China (Beijing):   `cn-north-1`
    * China (Ningxia):   `cn-northwest-1`
    * AWS GovCloud (US-West):   `us-gov-west-1`
    * AWS GovCloud (US-East):   `us-gov-east-1`

```
curl -X POST \
    -H 'Content-Type: application/json' \
    https://`your-neptune-endpoint`:`port`/loader -d '
    {
      "source" : "s3://`bucket-name`/`object-key-name`",
      "format" : "`format`",
      "iamRoleArn" : "arn:aws:iam::`account-id`:role/`role-name`",
      "region" : "`region`",
      "failOnError" : "FALSE",
      "parallelism" : "MEDIUM",
      "updateSingleCardinalityProperties" : "FALSE",
      "queueRequest" : "TRUE",
      "dependencies" : [`"load_A_id", "load_B_id"`]
    }'
```

For information about creating and associating an IAM role with a Neptune cluster,
see [Prerequisites: IAM Role and Amazon S3 Access](bulk-load-tutorial-IAM.md "bulk-load-tutorial-IAM.md").

###### Note

See [Neptune Loader Request Parameters](load-api-reference-load.md#load-api-reference-load-parameters "load-api-reference-load.md#load-api-reference-load-parameters")) for detailed information
about load request parameters. In brief:

The `source` parameter accepts an Amazon S3 URI that points to either a single
file or a folder. If you specify a folder, Neptune loads every data file in the
folder.

The folder can contain multiple vertex files and multiple edge files.

The URI can be in any of the following formats.

    * `s3://`bucket_name`/`object-key-name``
    * `https://s3.amazonaws.com/`bucket_name`/`object-key-name``
    * `https://s3-us-east-1.amazonaws.com/`bucket_name`/`object-key-name``The `format` parameter can be one of the following:



    * Gremlin CSV format (`csv`) for Gremlin property graphs
    * openCypher CSV format (`opencypher`) for openCypher property graphs
    * N -Triples (`ntriples`) format for RDF / SPARQL
    * N-Quads (`nquads`) format for RDF / SPARQL
    * RDF/XML (`rdfxml`) format for RDF / SPARQL
    * Turtle (`turtle`) format for RDF / SPARQLThe optional `parallelism` parameter lets you restrict the number of threads

used in the bulk load process. It can be set to `LOW`, `MEDIUM`,
`HIGH`, or `OVERSUBSCRIBE`.

When `updateSingleCardinalityProperties` is set to `"FALSE"`,
the loader returns an error if more than one value is provided in a source file being loaded
for an edge or single-cardinality vertex property.

Setting `queueRequest` to `"TRUE"` causes the load request to
be placed in a queue if there is already a load job running.

The `dependencies` parameter makes execution of the load request
contingent on the successful completion of one or more load jobs that have already
been placed in the queue. 3. The Neptune loader returns a job `id` that allows you to check the status
or cancel the loading process; for example:

```
{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "`ef478d76-d9da-4d94-8ff1-08d9d4863aa5`"
    }
}
```

4. Enter the following to get the status of the load with the `loadId` from
   **Step 3**:

```
curl -G 'https://`your-neptune-endpoint`:`port`/loader/`ef478d76-d9da-4d94-8ff1-08d9d4863aa5`'
```

If the status of the load lists an error, you can request more detailed status and a
list of the errors. For more information and examples, see [Neptune Loader Get-Status API](load-api-reference-status.md "load-api-reference-status.md"). 5. (Optional) Cancel the `Load` job.

Enter the following to `Delete` the loader job with the job `id`
from **Step 3**:

```
curl -X DELETE 'https://`your-neptune-endpoint`:`port`/loader/`ef478d76-d9da-4d94-8ff1-08d9d4863aa5`'
```

The `DELETE` command returns the HTTP code `200 OK` upon
successful cancellation.

The data from files from the load job that has finished loading is not rolled back.
The data remains in the Neptune DB instance.
