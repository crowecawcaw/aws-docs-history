# AWS ParallelCluster Python library API

Starting with AWS ParallelCluster version 3.5.0, you can access AWS ParallelCluster with the AWS ParallelCluster Python library. You can access the
AWS ParallelCluster library in your `pcluster` environment or from within an AWS Lambda runtime. Learn how to access the AWS ParallelCluster
API by using the AWS ParallelCluster Python library. The AWS ParallelCluster Python library offers the same functionality that the AWS ParallelCluster API
delivers.

The AWS ParallelCluster Python library operations and parameters mirror those of the API parameters when converted to `snake_case` with no capital
letters.

###### Topics

- [AWS ParallelCluster Python library authorization](#pc-py-lib-auth "#pc-py-lib-auth")
- [Install the AWS ParallelCluster Python library](#pc-py-lib-install "#pc-py-lib-install")
- [Cluster API operations](pc-py-lib-api-cluster.md "pc-py-lib-api-cluster.md")
- [Compute fleet API operations](pc-py-lib-api-fleet.md "pc-py-lib-api-fleet.md")
- [Cluster and stack log operations](pc-py-lib-api-logs-cluster-stack.md "pc-py-lib-api-logs-cluster-stack.md")
- [Image API operations](pc-py-lib-api-image.md "pc-py-lib-api-image.md")
- [Image and stack log operations](pc-py-lib-api-logs-image-stack.md "pc-py-lib-api-logs-image-stack.md")
- [Example](pc-py-lib-api-examples.md "pc-py-lib-api-examples.md")
- [AWS Lambda for the AWS ParallelCluster Python library](#lambda-py-v3 "#lambda-py-v3")

## AWS ParallelCluster Python library authorization

Specify credentials by using any of the standard ways that are valid for boto3. For more information,
see the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration").

## Install the AWS ParallelCluster Python library

1. Install `pcluster` CLI version 3.5.0 or later by following the instructions given in [Setting up AWS ParallelCluster](install-v3.md "install-v3.md").
2. Import the `pcluster` module and start using the library, as shown in the following example:

```
import pcluster.lib as `pc`
pc.create_cluster(cluster_name=`"mycluster"`, cluster_configuration=`"config.yaml"`
```

## AWS Lambda for the AWS ParallelCluster Python library

You can deploy a Lambda layer and runtime to access to the AWS ParallelCluster Python library. We host AWS ParallelCluster zip
files that you can use by entering the link to the zip file as described in the following steps. Lambda uses the zip files to prepare the runtime environment
to support access to the Python library. The AWS ParallelCluster Python library is added with AWS ParallelCluster version 3.5.0. You can only use
the library for versions 3.5.0 and later.

The hosted zip file URL is in the format:
`s3://`aws-region-id`-aws-parallelcluster/parallelcluster/`3.14.1`/layers/aws-parallelcluster/lambda-layer.zip`.
(Replace `3.14.1` with the AWS ParallelCluster version you want to use in
the following step.)

### Get started accessing the AWS ParallelCluster Python library with AWS Lambda

###### Create a Lambda layer

1. Log in to the AWS Management Console and navigate to the AWS Lambda console.
2. In the navigation pane, select **Layers**, then **Create layer**.
3. Enter a name for your layer and select **Upload a file from Amazon S3**.
4. Enter the URL to the zip file: s3://`aws-region-id`-aws-parallelcluster/parallelcluster/`3.14.1`/layers/aws-parallelcluster/lambda-layer.zip.
5. For **Compatible architectures**, choose the **x86_64** architecture.
6. For **Compatible runtimes**, choose the **Python 3.12** runtime.
7. Choose **Create**.

###### Use your Lambda layer

1. In the Lambda console navigation pane, select **Functions**, then **Create function**.
2. Enter a name for your function.
3. For **Runtime**, choose the **Python 3.12** runtime.
4. For **Architecture**, choose the **x86_64** architecture.
5. Choose **Create function**.
6. After the function is created, choose **Layers** and select **Add a layer**.
7. Select **Custom layers** and choose the layer you created in previous steps.
8. Choose the layer version.
9. Choose **Add**.
10. Your Lambda needs permissions to manage clusters created with AWS ParallelCluster. Create a Lambda role with the permissions listed in
    [Base AWS ParallelCluster pcluster user policy](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-base-user-policy "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-base-user-policy").

You can now access AWS ParallelCluster from the Python library as described in [AWS ParallelCluster Python library API](pc-py-library-v3.md "pc-py-library-v3.md").
