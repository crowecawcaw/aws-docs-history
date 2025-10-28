After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Updating code configurations on a running cluster

Amazon FinSpace allows you to update code configurations on a running cluster. You can either use
the console or the [UpdateKxClusterCodeConfiguration](../management-api/API_UpdateKxClusterCodeConfiguration.md "../management-api/API_UpdateKxClusterCodeConfiguration.md") API to update the code. Both console and API allow
you to choose how you want to update the code on a cluster by using different deployment modes.
Based on the option you choose, you can reduce the time it takes to update the code on to a
cluster. You can also add or delete default compression parameters for your files by using
command-line arguments.

###### Note

The configuration that you update will override any existing configurations on the cluster.

###### To update code configurations on a cluster by using the console

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the list of environments, choose a kdb environment.
4. On the environment details page, choose the **Clusters** tab.
5. From the list of clusters, choose the one where you want to update the code. The cluster details page opens.
6. On the cluster details page, choose the **Details** tab.
7. Under **Code** section, choose
   **Edit**.

###### Note

This button is only available for an **Active** environment and when the
cluster is in a **Running** state. 8. On the **Edit code configuration** page, choose how you want to update a
cluster by choosing a deployment mode. The following options are available.

    * **Rolling** – (Default) Loads the code by stopping the exiting q
     process and starting a new q process with updated configuration.
    * **Quick** – Loads the code by stopping all the running nodes
     immediately.

9. Specify the **S3 URI** and the **Object version**. This
   allows you to choose the _.zip_ file containing code that should be available
   on the cluster.
10. For **Initialization script**, enter the relative path that contains a q
    program script that will run at the launch of a cluster.
11. (Optional) Add or update the key-value pairs as command line arguments to configure the
    behavior of clusters.

You can use the command-line arguments to set [zip defaults](https://code.kx.com/q/ref/dotz/#zzd-zip-defaults "https://code.kx.com/q/ref/dotz/#zzd-zip-defaults") for your
cluster. The cluster has to be restarted for the changes to take effect. For this, pass the
following key-value pair:

    * **Key**: `AWS_ZIP_DEFAULT`
    * **Value**: `17,2,6`


    The value consists of comma separated three numbers that represent logical block
     size, algorithm, and compression level respectively. For more information, see [compression
     parameters](https://code.kx.com/q/kb/file-compression/#compression-parameters "https://code.kx.com/q/kb/file-compression/#compression-parameters").


    To update the compression default using AWS CLI, use the following command:



    ```
    aws finspace update-kx-cluster-code-configuration \
        ...
        --command-line-arguments '[{"key": "AWS_ZIP_DEFAULT", "value":"17,3,0"}]' \
        --deploymentConfiguration deploymentStrategy=ROLLING|FORCE
        ...
    ```

12. Choose **Save changes**. The cluster details page opens and the updated code
    configuration is displayed once the cluster updates successfully.
