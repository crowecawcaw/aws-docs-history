

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve node logs for a managed node using kubectl and S3
<a name="auto-get-logs"></a>

Learn how to retrieve node logs for an Amazon EKS managed node that has the node monitoring agent.

## Prerequisites
<a name="_prerequisites"></a>

Make sure you have the following:
+ An existing Amazon EKS cluster with the node monitoring agent. For more information, see [Detect node health issues and enable automatic node repair](node-health.md).
+ The `kubectl` command-line tool installed and configured to communicate with your cluster.
+ The AWS CLI installed and logged in with sufficient permissions to create S3 buckets and objects.
+ A recent version of Python 3 installed
+ The AWS SDK for Python 3, Boto 3, installed.

## Step 1: Create S3 bucket destination (optional)
<a name="_step_1_create_s3_bucket_destination_optional"></a>

If you don’t already have an S3 bucket to store the logs, create one. Use the following AWS CLI command. The bucket defaults to the `private` access control list. Replace {{bucket-name}} with your chosen unique bucket name.

```
aws s3api create-bucket --bucket {{<bucket-name>}}
```

## Step 2: Create pre-signed S3 URL for HTTP Put
<a name="_step_2_create_pre_signed_s3_url_for_http_put"></a>

Amazon EKS returns the node logs by doing a HTTP PUT operation to a URL you specify. In this tutorial, we will generate a pre-signed S3 HTTP PUT URL.

The logs will be returned as a gzip tarball, with the `.tar.gz` extension.

**Note**  
You must use the AWS API or a SDK to create the pre-signed S3 upload URL for EKS to upload the log file. You cannot create a pre-signed S3 upload URL using the AWS CLI.

1. Determine where in the bucket you want to store the logs. For example, you might use {{2024-11-12/logs1.tar.gz}} as the key.

1. Save the following Python code to the file {{presign-upload.py}}. Replace {{<bucket-name>}} and {{<key>}}. The key should end with `.tar.gz`.

   ```
   import boto3; print(boto3.client('s3').generate_presigned_url(
      ClientMethod='put_object',
      Params={'Bucket': '<bucket-name>', 'Key': '<key>'},
      ExpiresIn=1000
   ))
   ```

1. Run the script with

   ```
   python presign-upload.py
   ```

1. Note the URL output. Use this value in the next step as the {{http-put-destination}}.

For more information, see [Generate a presigned URL to upload a file](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file) in the AWS Boto3 SDK for Python Documentation.

## Step 3: Create NodeDiagnostic resource
<a name="_step_3_create_nodediagnostic_resource"></a>

Identify the name of the node you want to collect logs from.

Create a `NodeDiagnostic` manifest that uses the name of the node as the resource’s name, and providing a HTTP PUT URL destination.

```
apiVersion: eks.amazonaws.com/v1alpha1
kind: NodeDiagnostic
metadata:
    name: {{<node-name>}}
spec:
    logCapture:
        destination: {{http-put-destination}}
```

Apply the manifest to the cluster.

```
kubectl apply -f nodediagnostic.yaml
```

You can check on the Status of the collection by describing the `NodeDiagnostic` resource:
+ A status of `Success` or `SuccessWithErrors` indicates that the task completed and the logs uploaded to the provided destination (`SuccessWithErrors` indicates that some logs might be missing)
+ If the status is Failure, confirm the upload URL is well-formed and not expired.

```
kubectl describe nodediagnostics.eks.amazonaws.com/{{<node-name>}}
```

## Step 4: Download logs from S3
<a name="_step_4_download_logs_from_s3"></a>

Wait approximately one minute before attempting to download the logs. Then, use the S3 CLI to download the logs.

```
# Once NodeDiagnostic shows Success status, download the logs
aws s3 cp s3://{{<bucket-name>}}/{{key}} ./{{<path-to-node-logs>}}.tar.gz
```

## Step 5: Clean up NodeDiagnostic resource
<a name="_step_5_clean_up_nodediagnostic_resource"></a>
+  `NodeDiagnostic` resources do not get automatically deleted. You should clean these up on your own after you have obtained your log artifacts

```
# Delete the NodeDiagnostic resource
kubectl delete nodediagnostics.eks.amazonaws.com/{{<node-name>}}
```

## NodeDiagnostic `node` Destination
<a name="_nodediagnostic_node_destination"></a>

Starting with version `v1.6.1-eksbuild.1` of the Node Monitoring Agent, there is an option to set the log collection destination to `node`. Using this destination will lead to the collection and temporary persistence of logs on the node for later collection. In addition to this functionality, within the Node Monitoring Agent’s GitHub repository is a `kubectl` plugin you can install for easy interaction and log collection. For more information, see the [documentation for the `kubectl ekslogs` plugin](https://github.com/aws/eks-node-monitoring-agent/blob/main/tools/kubectl-ekslogs/README.md).

## Example Usage
<a name="_example_usage"></a>

```
# Collect NodeDiagnostic logs from a single node
kubectl ekslogs <node-name>

# Collect NodeDiagnostic logs from multiple nodes
kubectl ekslogs <node-name-1> <node-name-2> <node-name-3>

# Collect NodeDiagnostic logs from all nodes with a specific label
kubectl ekslogs -l <key>=<value>
```