# Access Amazon EMR WAL through

AWS PrivateLink

If you want to keep your connection within the AWS network, Amazon EMR WAL offers
AWS PrivateLink support. To set up AWS PrivateLink, use the AWS Management Console or AWS Command Line Interface (AWS CLI)
to create an interface VPC endpoint that connects to Amazon EMR WAL. For more information,
see [Access an AWS service
using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_AWS PrivateLink Guide_.

The basic steps are as follows:

1. Use the Amazon VPC Console to [create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws"). Select **Endpoints** and
   then **Create endpoint**.
2. Keep the Service category as **AWS services**.
3. In the search bar for the **Services** panel, type
   `emrwal`, and then select the service labeled
   `com.amazonaws.`region`.emrwal.prod`.
4. Select your VPC and save the endpoint. Make sure that you attach the same
   security groups to the VPC endpoint that you attach to the EMR cluster.
5. If you want to, you can now enable private DNS hostnames for your new
   endpoint. Set **Enable DNS hostnames** and **Enable DNS
   Support** to `true` for your VPC. Then, select your
   endpoint ID, choose **Edit VPC settings** from the
   **Actions** menu, and enable private DNS names.
   - The private DNS hostnames for the endpoint will follow the format
     `prod.emrwal.`region`.amazonaws.com`.
   - If you don't enable private DNS hostnames, Amazon VPC provides a DNS
     endpoint name for you in the format
     ``endpointID`.prod.emrwal.`region`.vpce.amazonaws.com`.

6. To use your AWS PrivateLink endpoint, modify the
   `emr.wal.client.endpoint` configuration when you create your
   [Amazon EMR WAL enabled cluster](emr-hbase-wal-enabling.md "emr-hbase-wal-enabling.md") as
   shown in the following example:

```
[
    {
        "Classification": "hbase-site",
        "Properties": {
            "hbase.rootdir": "s3://`amzn-s3-demo-bucket`/`MyHBaseStore`",
            "emr.wal.workspace": "`customWorkspaceName`",
            "emr.wal.client.endpoint": "https://prod.emrwal.`region`.amazonaws.com"
        }
    },
    {
        "Classification": "hbase",
        "Properties": {
            "hbase.emr.storageMode": "s3",
            "hbase.emr.wal.enabled": "true"
        }
    }
]
```

You can also use VPCE policy to allow or restrict access to the Amazon EMR WAL APIs. For
more information, see [Control access to VPC
endpoints using endpoint policies](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_AWS PrivateLink Guide_.
