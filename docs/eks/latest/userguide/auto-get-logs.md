**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve node logs for a managed node using kubectl and S3

Learn how to retrieve node logs for an Amazon EKS managed node that has the node monitoring agent.

## Prerequisites

Make sure you have the following:

- An existing Amazon EKS cluster with the node monitoring agent. For more information, see [Enable node auto repair and investigate node health issues](node-health.md "node-health.md").
- The `kubectl` command-line tool installed and configured to
  communicate with your cluster.
- The AWS CLI installed and logged in with sufficent permissions to
  create S3 buckets and objects.
- A recent version of Python 3 installed
- The AWS SDK for Python 3, Boto 3, installed.

## Step 1: Create S3 bucket destination (optional)

If you don’t already have an S3 bucket to store the logs, create one. Use the following AWS CLI command. The bucket defaults to the `private` access control list. Replace `bucket-name` with your chosen unique bucket name.

```
aws s3api create-bucket --bucket `<bucket-name>`

```

## Step 2: Create pre-signed S3 URL for HTTP Put

Amazon EKS returns the node logs by doing a HTTP PUT operation to a URL you specify. In this tutorial, we will generate a pre-signed S3 HTTP PUT URL.

The logs will be returned as a gzip tarball, with the `.tar.gz` extension.

###### Note

You must use the AWS API or a SDK to create the pre-signed S3 upload URL for EKS to upload the log file. You cannot create a pre-signed S3 upload URL using the AWS CLI.

1. Determine where in the bucket you want to store the logs. For example, you might use `2024-11-12/logs1.tar.gz` as the key.
2. Save the following Python code to the file `presign-upload.py`. Replace `<bucket-name>` and `<key>`. The key should end with `.tar.gz`.

```
import boto3; print(boto3.client('s3').generate_presigned_url(
   ClientMethod='put_object',
   Params={'Bucket': '[.replaceable]`<bucket-name>`', 'Key': '[.replaceable]`<key>`'},
   ExpiresIn=`1000`
))
```

3. Run the script with

```
python presign-upload.py
```

4. Note the URL output. Use this value in the next step as the `http-put-destination`.

For more information, see [Generate a presigned URL to upload a file](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file") in the AWS Boto3 SDK for Python Documentation.

## Step 3: Create NodeDiagnostic resource

Identify the name of the node you want to collect logs from.

Create a `NodeDiagnostic` manifest that uses the name of the node as the
resource’s name, and providing a HTTP PUT URL destination.

```
apiVersion: eks.amazonaws.com/v1alpha1
kind: NodeDiagnostic
metadata:
    name: `<node-name>`
spec:
    logCapture:
        destination: `http-put-destination`

```

Apply the manifest to the cluster.

```
kubectl apply -f nodediagnostic.yaml
```

You can check on the Status of the collection by describing the
`NodeDiagnostic` resource:

- A status of `Success` or `SuccessWithErrors` indicates that the task
  completed and the logs uploaded to the provided destination
  (`SuccessWithErrors` indicates that some logs might be missing)
- If the status is Failure, confirm the upload URL is well-formed and not expired.

```
kubectl describe nodediagnostics.eks.amazonaws.com/`<node-name>`

```

## Step 4: Download logs from S3

Wait approximately one minute before attempting to download the logs. Then, use the S3 CLI to download the logs.

```
# Once NodeDiagnostic shows Success status, download the logs
aws s3 cp s3://`<bucket-name>`/`key` ./`<path-to-node-logs>`.tar.gz
```

## Step 5: Clean up NodeDiagnostic resource

- `NodeDiagnostic` resources do not get automatically deleted. You
  should clean these up on your own after you have obtained your log
  artifacts

```
# Delete the NodeDiagnostic resource
kubectl delete nodediagnostics.eks.amazonaws.com/`<node-name>`

```
