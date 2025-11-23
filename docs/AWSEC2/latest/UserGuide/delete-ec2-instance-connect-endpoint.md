# Delete an EC2 Instance Connect Endpoint

When you are finished with an EC2 Instance Connect Endpoint, you can delete it.

You must have the required IAM permissions to create an EC2 Instance Connect Endpoint. For more
information, see [Permissions to create, describe,
modify, and delete EC2 Instance Connect Endpoints](permissions-for-ec2-instance-connect-endpoint.md#iam-CreateInstanceConnectEndpoint "permissions-for-ec2-instance-connect-endpoint.md#iam-CreateInstanceConnectEndpoint").

When you delete an EC2 Instance Connect Endpoint using the console, it enters the
**Deleting** state. If deletion is successful, the deleted endpoint
no longer appears. If deletion fails, the state is **delete-failed**
and **Status message** provides the failure reason.

When you delete an EC2 Instance Connect Endpoint using the AWS CLI, it enters the
`delete-in-progress` state. If deletion is successful, it enters the
`delete-complete` state. If deletion fails, the state is
`delete-failed` and `StateMessage` provides the failure
reason.

Console

###### To delete an EC2 Instance Connect Endpoint

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left navigation pane, choose
   **Endpoints**.
3. Select the endpoint.
4. Choose **Actions**, **Delete VPC
   endpoints**.
5. When prompted for confirmation, enter
   `delete`.
6. Choose **Delete**.

AWS CLI

###### To delete an EC2 Instance Connect Endpoint

Use the [delete-instance-connect-endpoint](../../../cli/latest/reference/ec2/delete-instance-connect-endpoint.md "../../../cli/latest/reference/ec2/delete-instance-connect-endpoint.md") command
and specify the ID of the EC2 Instance Connect Endpoint to delete.

```
aws ec2 delete-instance-connect-endpoint --instance-connect-endpoint-id `eice-03f5e49b83924bbc7`
```

The following is example output.

```
{
    "InstanceConnectEndpoint": {
        "OwnerId": "`111111111111`",
        "InstanceConnectEndpointId": "`eice-0123456789example`",
        "InstanceConnectEndpointArn": "arn:aws:ec2:`us-east-1`:`111111111111`:instance-connect-endpoint/`eice-0123456789example`",
        "State": "`delete-in-progress`",
        "StateMessage": "",
        "NetworkInterfaceIds": [],
        "VpcId": "`vpc-0123abcd`",
        "AvailabilityZone": "`us-east-1d`",
        "AvailabilityZoneId": "`use1-az2`",
        "CreatedAt": "`2023-02-07T12:05:37+00:00`",
        "SubnetId": "`subnet-0123abcd`"
    }
}
```

PowerShell

###### To delete an EC2 Instance Connect Endpoint

Use the [Remove-EC2InstanceConnectEndpoint](../../../cli/latest/reference/ec2/delete-instance-connect-endpoint.md "../../../cli/latest/reference/ec2/delete-instance-connect-endpoint.md") cmdlet
and specify the ID of the EC2 Instance Connect Endpoint to delete.

```
Remove-EC2InstanceConnectEndpoint -InstanceConnectEndpointId `eice-03f5e49b83924bbc7`
```

The following is example output.

```
@{
    InstanceConnectEndpoint = @{
        OwnerId = "`111111111111`"
        InstanceConnectEndpointId = "`eice-0123456789example`"
        InstanceConnectEndpointArn = "arn:aws:ec2:`us-east-1`:`111111111111`:instance-connect-endpoint/`eice-0123456789example`"
        State = "`delete-in-progress`"
        StateMessage = ""
        NetworkInterfaceIds = @()
        VpcId = "`vpc-0123abcd`"
        AvailabilityZone = "`us-east-1d`"
        AvailabilityZoneId = "`use1-az2`"
        CreatedAt = "2023-02-07T12:05:37+00:00"
        SubnetId = "`subnet-0123abcd`"
    }
}

```
