After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 2: Add code

You can load q code onto your kdb cluster so that you can run it when the
cluster is running. Additionally, you can configure your cluster to automatically run a
particular q command script on cluster startup. By default, q writes files uncompressed.
You can pass command line arguments to set compression defaults `.z.d` at the
time of creating a cluster from the console or through CLI, which can be updated
later.

###### Note

This step is required for the **Gateway** and
**Tickerplant** cluster type.

On the **Add code** page, add the following details of
your custom code that you want to use when analyzing the data in the cluster.

1. (Optional) Specify the **S3 URI** and the
   **Object version**. You can choose the
   _.zip_ file that contains code that should be
   available on the cluster.
2. (Optional) For **Initialization script**, enter the
   relative path that contains a q program script that will run at the launch of a
   cluster. If you choose to load the database by using the initialization script, it
   will autoload on startup. If you add a changeset that has a missing sym file, the
   cluster creation fails.

###### Note

This step is optional. If you choose to enter the initialization
script, you must also provide the S3 URI. 3. (Optional) Enter key-value pairs as command-line arguments to configure
the behavior of clusters. You can use the command-line arguments to set [zip defaults](https://code.kx.com/q/ref/dotz/#zzd-zip-defaults "https://code.kx.com/q/ref/dotz/#zzd-zip-defaults") for
your clusters. For this, pass the following key-value pair:

    * **Key**: `AWS_ZIP_DEFAULT`
    * **Value**: `17,2,6`


    The value consists of comma separated three numbers that represent logical
     block size, algorithm, and compression level respectively. For more
     information, see [compression parameters](https://code.kx.com/q/kb/file-compression/#compression-parameters "https://code.kx.com/q/kb/file-compression/#compression-parameters"). You can also add the key-value pair when
     you [update code configuration on a
     cluster](update-cluster-code.md "update-cluster-code.md").

###### Note

You can only add up to 50 key-value pairs.

To set compression default using AWS CLI, use the following command:

```
aws finspace create-kx-cluster \
    ...
    --command-line-arguments '[{"key": "AWS_ZIP_DEFAULT", "value":"17,2,6"}]' \
    ...
```

4. Choose **Next**.

###### Note

In case of failure, to stop cluster creation from an initialization script, use the `.aws.stop_current_kx_cluster_creation` function in the script.
