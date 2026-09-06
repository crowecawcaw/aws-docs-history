

# Get the mTLS enforcement level with CloudHSM CLI
<a name="cloudhsm_cli-cluster-mtls-get-enforcement"></a>

Use the **cluster mtls get-enforcement** command in CloudHSM CLI to get the enforcement level of the usage of mutual TLS between client and AWS CloudHSM.

## User type
<a name="cluster-mtls-get-enforcement-userType"></a>

The following users can run this command.
+ Admin
+ Crypto users (CUs)

## Requirements
<a name="cluster-mtls-get-enforcement-requirements"></a>
+ To run this command, you must be logged in as a admin user or crypto user (CUs).

## Syntax
<a name="cluster-mtls-get-enforcement-syntax"></a>

```
aws-cloudhsm > help cluster mtls get-enforcement
            
Get the status of mtls enforcement in the cluster

Usage: cluster mtls get-enforcement [OPTIONS]

Options:
      --cluster-id {{<CLUSTER_ID>}}  Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
  -h, --help                     Print help
```

## Example
<a name="cluster-mtls-get-enforcement-examples"></a>

**Example**  
In the following example, this command lists the mtls enforcement level of the AWS CloudHSM.  

```
aws-cloudhsm > cluster mtls get-enforcement
                
{
  "error_code": 0,
  "data": {
    "mtls-enforcement-level": "none"
  }
}
```

## Arguments
<a name="cluster-mtls-get-enforcement-arguments"></a>

**{{<CLUSTER\_ID>}}**  
The ID of the cluster to run this operation on.  
Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md)

## Related topics
<a name="cluster-mtls-get-enforcement-seealso"></a>
+  [cluster mtls set-enforcement](cloudhsm_cli-cluster-mtls-set-enforcement.md) 
+  [Setup mTLS (recommended)](getting-started-setup-mtls.md) 