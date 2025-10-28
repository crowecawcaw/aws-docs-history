# Using SPARQL UPDATE LOAD

to import data into Neptune

The syntax of the SPARQL UPDATE LOAD command is specified in the [SPARQL 1.1 Update
recommendation](https://www.w3.org/TR/sparql11-update/#load "https://www.w3.org/TR/sparql11-update/#load"):

```
LOAD SILENT `(URL of data to be loaded)` INTO GRAPH `(named graph into which to load the data)`
```

- **`SILENT`**   –  
  (_Optional_) Causes the operation to return success even if
  there was an error during processing.

This can be useful when a single transaction contains multiple statements
like `"LOAD ...; LOAD ...; UNLOAD ...; LOAD ...;"` and you want the
transaction to complete even if some of the remote data could not be processed.

- `URL of data to be loaded`   –  
  (_Required_) Specifies a remote data file containing data to be
  loaded into a graph.

The remote file must have one of the following extensions:

    + `.nt` for NTriples.
    + `.nq` for NQuads.
    + `.trig` for Trig.
    + `.rdf` for RDF/XML.
    + `.ttl` for Turtle.
    + `.n3` for N3.
    + `.jsonld` for JSON-LD.

- **`INTO GRAPH`**`(named graph
into which to load the data)`   –  
  (_Optional_) Specifies the graph into which the data
  should be loaded.

Neptune associates every triple with a named graph. You can specify the
default named graph using the fallback named-graph URI,
`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`, like this:

```
INTO GRAPH <http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph>
```

###### Note

When you need to load a lot of data, we recommend that you use
the Neptune bulk loader rather than UPDATE LOAD. For more information about the
bulk loader, see [Using the Amazon Neptune bulk loader to ingest data](bulk-load.md "bulk-load.md").

You can use `SPARQL UPDATE LOAD` to load data directly from Amazon S3,
or from files obtained from a self-hosted web server. The resources to be
loaded must reside in the same region as the Neptune server, and the endpoint
for the resources must be allowed in the VPC. For information about
creating an Amazon S3 endpoint, see [Creating an Amazon S3 VPC Endpoint](bulk-load-data.md#bulk-load-prereqs-s3 "bulk-load-data.md#bulk-load-prereqs-s3").

All `SPARQL UPDATE LOAD` URIs must start with `https://`.
This includes Amazon S3 URLs.

In contrast to the Neptune bulk loader, a call to `SPARQL UPDATE LOAD`
is fully transactional.

###### Loading files directly from Amazon S3 into Neptune using SPARQL UPDATE LOAD

Because Neptune does not allow you to pass an IAM role to Amazon S3 when using
SPARQL UPDATE LOAD, either the Amazon S3 bucket in question must be public or you must use a [pre-signed Amazon S3 URL](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md") in the LOAD
query.

To generate a pre-signed URL for an Amazon S3 file, you can use an AWS CLI command
like this:

```
aws s3 presign --expires-in `(number of seconds)` s3://`(bucket name)`/`(path to file of data to load)`
```

Then you can use the resulting pre-signed URL in your `LOAD` command:

```
curl https://`(a Neptune endpoint URL)`:8182/sparql \
  --data-urlencode 'update=load `(pre-signed URL of the remote Amazon S3 file of data to be loaded)` \
                           into graph `(named graph)`'
```

For more information, see [Authenticating Requests: Using Query Parameters](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md"). The [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html")
shows how to use a Python script to generate a presigned URL.

Also, the content type of the files to be loaded must be set correctly.

1. Set the content type of files when you upload them into Amazon S3 by using the
   `-metadata` parameter, like this:

```
aws s3 cp test.nt s3://`bucket-name/my-plain-text-input`/test.nt --metadata Content-Type=text/plain
aws s3 cp test.rdf s3://`bucket-name/my-rdf-input`/test.rdf --metadata Content-Type=application/rdf+xml
```

2. Confirm that the media-type information is actually present. Run:

```
curl -v `bucket-name/folder-name`
```

The output of this command should show the media-type information that
you set when uploading the files. 3. Then you can use the `SPARQL UPDATE LOAD` command to import these
files into Neptune:

```
curl https://`your-neptune-endpoint`:`port`/sparql \
  -d "update=LOAD <https://s3.amazonaws.com/`bucket-name`/`my-rdf-input/test.rdf`>"
```

The steps above work only for a public Amazon S3 bucket, or for a bucket that you access
using a [pre-signed Amazon S3 URL](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md")
in the LOAD query.

You can also set up a web proxy server to load from a private Amazon S3
bucket, as shown below:

###### Using a web server to load files into Neptune with SPARQL UPDATE LOAD

1. Install a web server on a machine running within the VPC that is
   hosting Neptune and the files to be loaded. For example, using
   Amazon Linux, you might install Apache as follows:

```
sudo yum install httpd mod_ssl
sudo /usr/sbin/apachectl start
```

2. Define the MIME type(s) of the RDF file-content that you are going
   to load. SPARQL uses the `Content-type` header sent
   by the web server to determine the input format of the content, so
   you must define the relevant MIME types for the web Server.

For example, suppose you use the following file extensions
to identify file formats:

    * `.nt` for NTriples.
    * `.nq` for NQuads.
    * `.trig` for Trig.
    * `.rdf` for RDF/XML.
    * `.ttl` for Turtle.
    * `.n3` for N3.
    * `.jsonld` for JSON-LD.

If you are using Apache 2 as the web server, you would edit the file
`/etc/mime.types` and add the following types:

```
 text/plain nt
 application/n-quads nq
 application/trig trig
 application/rdf+xml rdf
 application/x-turtle ttl
 text/rdf+n3 n3
 application/ld+json jsonld
```

3. Confirm that the MIME-type mapping works. Once you have your
   web server up and running and hosting RDF files in the format(s)
   of your choice, you can test the configuration by sending a
   request to the web server from your local host.

For instance, you might send a request such as this:

```
curl -v http://localhost:80/test.rdf
```

Then, in the detailed output from `curl`, you
should see a line such as:

```
Content-Type: application/rdf+xml
```

This shows that the content-type mapping was defined successfully. 4. You are now ready to load data using the SPARQL UPDATE command:

```
curl https://`your-neptune-endpoint`:`port`/sparql \
    -d "update=LOAD <http://`web_server_private_ip`:80/test.rdf>"
```

###### Note

Using `SPARQL UPDATE LOAD` can trigger a timeout on the web server
when the source file being loaded is large. Neptune processes the file data as
it is streamed in, and for a big file that can take longer than the timeout configured
on the server. This in turn may cause the server to close the connection, which can
result in the following error message when Neptune encounters an unexpected EOF
in the stream:

```
{
  "detailedMessage":"Invalid syntax in the specified file",
  "code":"InvalidParameterException"
}
```

If you receive this message and don't believe your source file contains
invalid syntax, try increasing the timeout settings on the web server.
You can also diagnose the problem by enabling debug logs on the server
and looking for timeouts.
