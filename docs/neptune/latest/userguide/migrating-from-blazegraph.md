# Migrating from Blazegraph to Amazon Neptune

If you have a graph in the open-source [Blazegraph](https://blazegraph.com/ "https://blazegraph.com/")
RDF triplestore, you can migrate to your graph data to Amazon Neptune using the following steps:

- _Provision AWS infrastructure._ Begin by provisioning
  the required Neptune infrastructure using an AWS CloudFormation template (see
  [Create Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md") ).
- _Export data from Blazegraph._ There are two main
  methods for exporting data from Blazegraph, namely using SPARQL CONSTRUCT queries
  or using the Blazegraph Export utility.
- _Import the data into Neptune._ You can then
  load the exported data files into Neptune using the [Neptune workbench](graph-notebooks.md "graph-notebooks.md") and [Neptune Bulk Loader](bulk-load.md "bulk-load.md").
  This approach is also generally applicable for migrating from other RDF triplestore
  databases.

## Blazegraph to Neptune compatibility

Before migrating your graph data to Neptune, there are several significant differences
between Blazegraph and Neptune that you should be aware of. These
differences can require changes to queries, the application architecture, or both,
or even make migration impractical:

- **`Full-text search`**   –  
  In Blazegraph, you can either use internal full-text search or external full-text
  search capabilities through an integration with Apache Solr. If you use either
  of these features, stay informed about the latest updates on the full-text
  search features that Neptune supports. See [Neptune full text search](full-text-search.md "full-text-search.md").
- **`Query hints`**   –  
  Both Blazegraph and Neptune extend SPARQL using the concept of query hints.
  During a migration, you need to migrate any query hints you use. For information
  about the latest query hints Neptune supports, see [SPARQL query hints](sparql-query-hints.md "sparql-query-hints.md").
- **Inference**   –  
  Blazegraph supports inference as a configurable option in triples mode,
  but not in quads mode. Neptune does not yet support inference.
- **Geospatial search**   –  
  Blazegraph supports the configuration of namespaces that enable geospatial support.
  This feature is not yet available in Neptune.
- **Multi-tenancy**   –  
  Blazegraph supports multi-tenancy within a single database. In Neptune, multi-tenancy
  is supported either by storing data in named graphs and using the USING NAMED clauses
  for SPARQL queries, or by creating a separate database cluster for each tenant.
- **Federation**   –  
  Neptune currently supports SPARQL 1.1 federation to locations accessible to the Neptune
  instance, such as within the private VPC, across VPCs, or to external internet endpoints.
  Depending on the specific setup and required federation endpoints, you may need
  some additional network configuration.
- **Blazegraph standards extensions**   –  
  Blazegraph includes multiple extensions to both the SPARQL and REST API standards,
  whereas Neptune is only compatible with the standards specifications themselves.
  This may require changes to your application, or make migration difficult.

## Provisioning AWS infrastructure for Neptune

Although you can construct the required AWS infrastructure manually through
the AWS Management Console or AWS CLI, it's often more convenient to use a CloudFormation template
instead, as described below:

###### Provisioning Neptune using a CloudFormation template:

1. Navigate to [Creating an Amazon Neptune cluster using AWS CloudFormation](get-started-cfn-create.md "get-started-cfn-create.md").
2. Choose **Launch Stack** in your preferred region.
3. Set the required parameters (stack name and `EC2SSHKeyPairName`).
   Also set the following optional parameters to ease the migration process:
   - Set `AttachBulkloadIAMRoleToNeptuneCluster` to true.
     This parameter allows for creating and attaching the appropriate IAM role to
     your cluster to allow for bulk loading data.
   - Set `NotebookInstanceType` to your preferred instance type.
     This parameter creates a Neptune workbook that you use to run the bulk load
     into Neptune and validate the migration.

4. Choose **Next**.
5. Set any other stack options you want.
6. Choose **Next**.
7. Review your options and select both check boxes to acknowledge that
   AWS CloudFormation may require additional capabilities.
8. Choose **Create stack**.

The stack creation process can take a few minutes.

## Exporting data from Blazegraph

The next step is to export data out of Blazegraph in a [format that is compatible with the Neptune
bulk loader](bulk-load-tutorial-format-rdf.md "bulk-load-tutorial-format-rdf.md").

Depending on how the data is stored in Blazegraph (triples or quads) and how
many named graphs are in use, Blazegraph may require that you perform the export
process multiple times and generate multiple data files:

- If the data is stored as triples, you need to run one export for each named
  graph.
- If the data is stored as quads, you may choose to either export data
  in N-Quads format or export each named graph in a triples format.

Below we assume that you export a single namespace as N-Quads, but you can repeat
the process for additional namespaces or desired export formats.

If you need Blazegraph to be online and available during the migration, use
SPARQL CONSTRUCT queries. This requires that you install, configure, and run a
Blazegraph instance with an accessible SPARQL endpoint.

If you don't need Blazegraph to be online, use [the BlazeGraph
Export utility](https://github.com/blazegraph/database/wiki/DataMigration#export "https://github.com/blazegraph/database/wiki/DataMigration#export"). To do this you must download Blazegraph, and the data file
and configuration files need to be accessible, but the server doesn’t need to be running.

### Exporting data from Blazegraph using SPARQL CONSTRUCT

SPARQL CONSTRUCT is a feature of SPARQL that returns an RDF graph matching the
a specified query template. For this use case, you use it to export your data one
namespace at a time, using a query like the following:

```
CONSTRUCT WHERE { hint:Query hint:analytic "true" . hint:Query hint:constructDistinctSPO "false" . ?s ?p ?o }
```

Although other RDF tools exist to export this data, the easiest way to run this
query is by using the REST API endpoint provided by Blazegraph. The following script
demonstrates how to use a Python (3.6+) script to export data as N-Quads:

```
import requests

# Configure the URL here: e.g. http://localhost:9999/sparql
url = "http://localhost:9999/sparql"
payload = {'query': 'CONSTRUCT WHERE { hint:Query hint:analytic "true" . hint:Query hint:constructDistinctSPO "false" . ?s ?p ?o }'}
# Set the export format to be n-quads
headers = {
'Accept': 'text/x-nquads'
}
# Run the http request
response = requests.request("POST", url, headers=headers, data = payload, files = [])
#open the file in write mode, write the results, and close the file handler
f = open("export.nq", "w")
f.write(response.text)
f.close()
```

If the data is stored as triples, you need to change the `Accept` header
parameter to export data in an appropriate format (N-Triples, RDF/XML, or Turtle) using
the values specified on the [Blazegraph GitHub repo](https://github.com/blazegraph/database/wiki/REST_API#rdf-data "https://github.com/blazegraph/database/wiki/REST_API#rdf-data").

### Using the Blazegraph export utility to export data

Blazegraph contains a utility method to export data, namely the `ExportKB`
class. `ExportKB` facilitates exporting data from Blazegraph, but unlike
the previous method, requires that the server be offline while the export is running.
This makes it the ideal method to use when you can take Blazegraph offline during
migration, or the migration can occur from a backup of the data.

You run the utility from a Java command line on a machine that has Blazegraph
installed but not running. The easiest way to run this command is to download the
latest [blazegraph.jar](https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_2_1_6_RC/blazegraph.jar "https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_2_1_6_RC/blazegraph.jar") release located on GitHub. Running this command requires
several parameters:

- **`log4j.primary.configuration`**   –  
  The location of the log4j properties file.
- **`log4j.configuration`**   –  
  The location of the log4j properties file.
- **`output`**   –  
  The output directory for the exported data. Files are located as a `tar.gz`
  in a subdirectory named as documented in the knowledge base.
- **`format`**   –  
  The desired output format followed by the location of the `RWStore.properties`
  file. If you’re working with triples, you need to change the `-format` parameter
  to `N-Triples`, `Turtle`, or `RDF/XML`.

For example, if you have the Blazegraph journal file and properties files, export data as
N-Quads using the following code:

```
java -cp blazegraph.jar \
    com.bigdata.rdf.sail.ExportKB \
    -outdir ~/temp/ \
    -format N-Quads \
    ./RWStore.properties
```

If the export is successful, you see output like this:

```
Exporting kb as N-Quads on /home/ec2-user/temp/kb
Effective output directory: /home/ec2-user/temp/kb
Writing /home/ec2-user/temp/kb/kb.properties
Writing /home/ec2-user/temp/kb/data.nq.gz
Done
```

## Create an Amazon Simple Storage Service (Amazon S3) bucket and copy the exported data into it

Once you have exported your data from Blazegraph, create an Amazon Simple Storage Service (Amazon S3) bucket
in the same Region as the target Neptune DB cluster for the Neptune bulk loader to
use to import the data from.

For instructions on how to create an Amazon S3 bucket, see [How do I create an S3 Bucket?](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the
[Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md"), and [Examples of creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-get-location-example.md "../../../AmazonS3/latest/userguide/create-bucket-get-location-example.md") in the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").

For instructions about how to copy the data files you have exported into the new
Amazon S3 bucket, see [Uploading an object to a bucket](../../../AmazonS3/latest/userguide/PuttingAnObjectInABucket.md "../../../AmazonS3/latest/userguide/PuttingAnObjectInABucket.md") in the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md"), or [Using high-level (s3) commands
with the AWS CLI](../../../cli/latest/userguide/cli-services-s3-commands.md "../../../cli/latest/userguide/cli-services-s3-commands.md"). You can also use Python code like the following to copy
the files one by one:

```
import boto3

region = '`region name`'
bucket_name = '`bucket name`'
s3 = boto3.resource('s3')
s3.meta.client.upload_file('export.nq', bucket_name, 'export.nq')
```

## Use the Neptune bulk loader to import the data into Neptune

After exporting your data from Blazegraph and copying it into an Amazon S3 bucket, you
are ready to import the data into Neptune. Neptune has a bulk loader that loads data
faster and with less overhead than performing load operations using SPARQL. The bulk
loader process is started by a call to the loader endpoint API to load data stored in
the identified S3 bucket into Neptune.

Although you could do this with a direct call to the loader REST endpoint, you must
have access to the private VPC in which the target Neptune instance runs. You could set
up a bastion host, SSH into that machine, and run the cURL command, but using [Neptune Workbench](graph-notebooks.md "graph-notebooks.md") is easier.

Neptune Workbench is a preconfigured Jupyter notebook running as an Amazon SageMaker
notebook, with several Neptune-specific notebook magics installed. These magics simplify
common Neptune operations such as checking the cluster status, running SPARQL and Gremlin
traversals, and running a bulk loading operation.

To start the bulk load process use the `%load` magic, which provides an
interface to run the [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md"):

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Select **aws-neptune-blazegraph-to-neptune**.
3. Choose **Open notebook**.
4. In the running instance of Jupyter, either select an existing notebook
   or create a new one using the Python 3 kernel.
5. In your notebook, open a cell, enter `%load`, and run the cell.
6. Set the parameters for the bulk loader:
   1. For **Source**, enter the location of a source
      file to import: `s3://{bucket_name}/{file_name}`.
   2. For **Format**, choose the appropriate format,
      which in this example is `nquads`.
   3. For **Load ARN**, enter the ARN for the
      `IAMBulkLoad` role (this information is located on the
      IAM console under **Roles**).

7. Choose **Submit**.

The result contains the status of the request. Bulk loads are often
long-running processes, so the response doesn't mean the that the load
has completed, only that it has begun. This status information is updated
periodically until it reports that the job is complete.

###### Note

This information is also available in the blog post, [Moving
to the cloud: Migrating Blazegraph to Amazon Neptune](https://aws.amazon.com/blogs/database/moving-to-the-cloud-migrating-blazegraph-to-amazon-neptune/ "https://aws.amazon.com/blogs/database/moving-to-the-cloud-migrating-blazegraph-to-amazon-neptune/").
