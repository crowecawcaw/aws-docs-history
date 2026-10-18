

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve node logs using kubectl and Amazon S3
<a name="auto-get-logs"></a>

Learn how to retrieve node logs from an Amazon EKS node that runs the EKS node monitoring agent. The agent collects log and configuration bundles from the node and uploads them to your S3 bucket.

Log collection works on any EKS node that runs the EKS node monitoring agent, regardless of how the node is provisioned. This includes EKS Auto Mode nodes, EKS managed node groups, self-managed nodes, and Karpenter-provisioned nodes. AWS Fargate doesn’t support the EKS node monitoring agent, so you can’t collect node logs this way for Fargate pods.

The agent provides the `NodeDiagnostic` custom resource that this procedure uses. EKS Auto Mode includes the agent, so the custom resource is available without any installation. For other compute types, install the EKS node monitoring agent as an EKS add-on or with Kubernetes tooling such as Helm first. For more information, see [Configure the Amazon EKS node monitoring agent](node-monitoring-agent-configure.md).

## Prerequisites
<a name="_prerequisites"></a>

Make sure you have the following:
+ An existing Amazon EKS cluster with the EKS node monitoring agent running. For more information, see [Detect node health issues and enable automatic node repair](node-health.md).
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

Identify the name of the node you want to collect logs from, as reported by `kubectl get nodes`. Depending on the compute type, this is either an EC2 instance ID or a private DNS name. Use the name exactly as `kubectl` reports it.

```
kubectl get nodes
```

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

You can check on the status of the collection by describing the `NodeDiagnostic` resource. Collection usually finishes within a few seconds.

```
kubectl describe nodediagnostics.eks.amazonaws.com/{{<node-name>}}
```

The result appears under `Status` as a capture status of type `Log`. To read just the status, use the following command.

```
kubectl get nodediagnostics.eks.amazonaws.com/{{<node-name>}} \
    -o jsonpath='{.status.captureStatuses}'
```

Interpret the `reason` field as follows:
+ A `reason` of `Success` or `SuccessWithErrors` indicates that the task completed and the logs uploaded to the provided destination (`SuccessWithErrors` indicates that some logs might be missing).
+ A `reason` of `Failure` indicates that collection or upload failed. The accompanying `message` field includes the error returned by Amazon S3. Confirm that the upload URL is well-formed and hasn’t expired, then generate a new pre-signed URL and try again.

**Important**  
The `spec` of the `NodeDiagnostic` resource stores the destination URL in full, including the pre-signed credentials. Anyone who can read the resource with `kubectl get` or `kubectl describe` can read those credentials and write to that S3 object until the URL expires. Keep the expiration short and restrict access to `NodeDiagnostic` resources accordingly.

## Step 4: Download logs from S3
<a name="_step_4_download_logs_from_s3"></a>

Wait until the `NodeDiagnostic` resource reports a `reason` of `Success` or `SuccessWithErrors`. Then, use the S3 CLI to download the logs.

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

## NodeDiagnostic `node` destination
<a name="_nodediagnostic_node_destination"></a>

Starting with version `v1.6.1-eksbuild.1` of the EKS node monitoring agent, you can set the log collection destination to `node` instead of a pre-signed URL. This collects the logs and persists them temporarily on the node for later collection, so you don’t need an S3 bucket or pre-signed URL.

```
apiVersion: eks.amazonaws.com/v1alpha1
kind: NodeDiagnostic
metadata:
    name: {{<node-name>}}
spec:
    logCapture:
        destination: node
```

The EKS node monitoring agent writes the bundle to `/var/log/support/[.replaceable]`<node-name>`-logs.tar.gz` on the node, and the `message` field in the capture status reports the path it used. This destination works on all compute types that support the agent, including EKS Auto Mode and EKS managed node groups.

The EKS node monitoring agent’s GitHub repository also includes a `kubectl` plugin that creates the `NodeDiagnostic` resource and retrieves the resulting bundles for you. For more information, see the [documentation for the `kubectl ekslogs` plugin](https://github.com/aws/eks-node-monitoring-agent/blob/main/tools/kubectl-ekslogs/README.md).

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