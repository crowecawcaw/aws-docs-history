# AWS CloudHSM Client SDK 3 configuration parameters

The following is a list of parameters to configure AWS CloudHSM Client SDK 3.



**-h | --help**

Displays command syntax.


Required: Yes



**-a `<ENI IP address>`**

Adds the specified HSM elastic network interface (ENI) IP address to AWS CloudHSM
 configuration files. Enter the ENI IP address of any one of the HSMs in the cluster. It
 does not matter which one you select. 


To get the ENI IP addresses of the HSMs in your cluster, use the [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") operation, the
 [describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html "https://docs.aws.amazon.com/cli/latest/reference/cloudhsmv2/describe-clusters.html")
 AWS CLI command, or the [Get-HSM2Cluster](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-HSM2Cluster.html "https://docs.aws.amazon.com/powershell/latest/reference/items/Get-HSM2Cluster.html") PowerShell cmdlet. 


###### Note

Before running the  `-a`
**configure** command, stop the AWS CloudHSM client. Then, when the
 `-a` command completes, restart the AWS CloudHSM client. For details, [see the examples](configure-tool-examples.md "configure-tool-examples.md"). 


This parameter edits the following configuration files:



* `/opt/cloudhsm/etc/cloudhsm_client.cfg`: Used by AWS CloudHSM client
 and [key\_mgmt\_util](key_mgmt_util.md "key_mgmt_util.md").
* `/opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`: Used by [cloudhsm\_mgmt\_util](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md").

When the AWS CloudHSM client starts, it uses the ENI IP address in its configuration file
 to query the cluster and update the `cluster.info` file
 (`/opt/cloudhsm/daemon/1/cluster.info`) with the correct ENI IP
 addresses for all HSMs in the cluster. 


Required: Yes



**-m**

Updates the HSM ENI IP addresses in the configuration file that CMU uses. 


###### Note

The `-m` parameter is for use with CMU from Client SDK 3.2.1 and earlier. For CMU
 from Client SDK 3.3.0 and later, see `--cmu` parameter, which simplifies
 the process of updating HSM data for CMU.


When you update the `-a` parameter of **configure** and
 then start the AWS CloudHSM client, the client daemon queries the cluster and updates the
 `cluster.info` files with the correct HSM IP addresses for all HSMs
 in the cluster. Running the `-m`
**configure** command completes the update by copying the HSM IP
 addresses from the `cluster.info` to the
 `cloudhsm_mgmt_util.cfg` configuration file that cloudhsm\_mgmt\_util uses. 


Be sure to run `-a`
**configure** command and restart the AWS CloudHSM client before running the
 `-m` command. This ensures that the data copied into
 `cloudhsm_mgmt_util.cfg` from `cluster.info` is
 complete and accurate. 


Required: Yes



**-i**

Specifies an alternate client daemon. The default value represents the AWS CloudHSM
 client.


Default: `1`


Required: No



**--ssl**

Replaces the SSL key and certificate for the cluster with the specified private key
 and certificate. When you use this parameter, the `--pkey` and
 `--cert` parameters are required. 


Required: No



**--pkey**

Specifies the new private key. Enter the path and file name of the file that
 contains the private key.


Required: Yes if **--ssl** is specified. Otherwise, this should not be used.



**--cert**

Specifies the new certificate. Enter the path and file name of the file that
 contains the certificate. The certificate should chain up to the
 `customerCA.crt` certificate, the self-signed certificate used to
 initialize the cluster. For more information, see [Initialize the Cluster](initialize-cluster.md#sign-csr "initialize-cluster.md#sign-csr"). 


Required: Yes if **--ssl** is specified. Otherwise, this should not be used.



**--cmu `<ENI IP address>`**

Combines the `-a` and `-m` parameters into one parameter. Adds
 the specified HSM elastic network interface (ENI) IP address to AWS CloudHSM configuration
 files and then updates the CMU configuration file. Enter an IP address from any HSM in
 the cluster. For Client SDK 3.2.1 and earlier, see [Using
 CMU with Client SDK 3.2.1 and Earlier](understand-users.md#downlevel-cmu "understand-users.md#downlevel-cmu").


Required: Yes
