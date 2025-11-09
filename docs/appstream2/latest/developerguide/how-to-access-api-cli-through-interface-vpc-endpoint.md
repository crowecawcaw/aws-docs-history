# Use an Interface Endpoint to Access WorkSpaces Applications API Operations and CLI Commands

After the status of the interface VPC endpoint that you create changes to
**Available**, you can use the endpoint to access WorkSpaces Applications API
operations and CLI commands. To do so, specify the `endpoint-url` parameter with
the DNS name of the interface endpoint when you use these operations and commands. The DNS name
is publicly resolvable, but it only successfully routes traffic in your VPC.

The following example shows how to specify the DNS name of the interface endpoint when you use the **describe-fleets** CLI command:

```
aws appstream describe-fleets --endpoint-url <vpc-endpoint-id>.api.appstream.<aws-region>.vpce.amazonaws.com
```

The following example shows how to specify the DNS name of the interface endpoint when you instantiate the WorkSpaces Applications Boto3 Python client:

```
appstream2client = boto3.client('appstream',region_name='<aws-region>',endpoint_url='<vpc-endpoint-id>.api.appstream.<aws-region>.vpce.amazonaws.com'
```

Subsequent commands using the `appstream2client` object automatically use the interface endpoint that you specified.

If you enabled the private DNS host names on the interface endpoint, you don’t need to specify the endpoint URL. The WorkSpaces Applications API DNS host name that the API and CLI use by default resolves within your VPC. For more information about private DNS host names, see [Private DNS](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns") in the _Amazon VPC User Guide_.
