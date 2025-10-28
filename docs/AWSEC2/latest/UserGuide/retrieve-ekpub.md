# Retrieve the public endorsement key for an EC2 instance

You can securely retrieve the public endorsement key for an instance at any time.

AWS CLI

###### To retrieve the public endorsement key for an instance

Use the [get-instance-tpm-ek-pub](../../../cli/latest/reference/ec2/get-instance-tpm-ek-pub.md "../../../cli/latest/reference/ec2/get-instance-tpm-ek-pub.md") command.

###### Example 1

The following example gets the `rsa-2048` public endorsement key in
`tpmt` format for the specified instance.

```
aws ec2 get-instance-tpm-ek-pub \
    --instance-id `i-1234567890abcdef0` \
    --key-format tpmt \
    --key-type rsa-2048
```

The following is the example output.

```
{
    "InstanceId": "i-01234567890abcdef",
    "KeyFormat": "tpmt",
    "KeyType": "rsa-2048",
    "KeyValue": "AAEACwADALIAIINxl2dEhLEXAMPLEUal1yT9UtduBlILZPKh2hszFGmqAAYAgABDA
    EXAMPLEAAABAOiRd7WmgtdGNoV1h/AxmW+CXExblG8pEUfNm0LOLiYnEXAMPLERqApiFa/UhvEYqN4
    Z7jKMD/usbhsQaAB1gKA5RmzuhSazHQkax7EXAMPLEzDthlS7HNGuYn5eG7qnJndRcakS+iNxT8Hvf
    0S1ZtNuItMs+Yp4SO6aU28MT/JZkOKsXIdMerY3GdWbNQz9AvYbMEXAMPLEPyHfzgVO0QTTJVGdDxh
    vxtXCOu9GYf0crbjEXAMPLEd4YTbWdDdgOKWF9fjzDytJSDhrLAOUctNzHPCd/92l5zEXAMPLEOIFA
    Ss50C0/802c17W2pMSVHvCCa9lYCiAfxH/vYKovAAE="
}
```

###### Example 2

The following example gets the `rsa-2048` public endorsement key in
`der` format for the specified instance.

```
aws ec2 get-instance-tpm-ek-pub \
    --instance-id `i-1234567890abcdef0` \
    --key-format der \
    --key-type rsa-2048
```

The following is the example output.

```
{
    "InstanceId": "i-1234567890abcdef0",
    "KeyFormat": "der",
    "KeyType": "rsa-2048",
    "KeyValue": "MIIBIjANBgEXAMPLEw0BAQEFAAOCAQ8AMIIBCgKCAQEA6JF3taEXAMPLEXWH8DGZb4
    JcTFuUbykRR82bQs4uJifaKSOv5NGoEXAMPLEG8Rio3hnuMowP+6xuGxBoAHWAoDlGbO6FJrMdEXAMP
    LEnYUHvMO2GVLsc0a5ifl4buqcmd1FxqRL6I3FPwe9/REXAMPLE0yz5inhI7ppTbwxP8lmQ4qxch0x6
    tjcZ1Zs1DP0EXAMPLERUYLQ/Id/OBU7RBNMlUZ0PGG/G1cI670Zh/RytuOdx9iEXAMPLEtZ0N2A4pYX
    1+PMPK0lIOGssA5Ry03Mc8J3/3aXnOD2/ASRQ4gUBKznQLT/zTZEXAMPLEJUe8IJr2VgKIB/Ef+9gqi
    8AAQIDAQAB"
}
```

PowerShell

###### To retrieve the public endorsement key for an instance

Use the [Get-EC2InstanceTpmEkPub](../../../powershell/latest/reference/items/Get-EC2InstanceTpmEkPub.md "../../../powershell/latest/reference/items/Get-EC2InstanceTpmEkPub.md")
cmdlet.

###### Example 1

The following example gets the `rsa-2048` public endorsement key in
`tpmt` format for the specified instance.

```
Get-EC2InstanceTpmEkPub `
    -InstanceId `i-1234567890abcdef0` `
    -KeyFormat tpmt `
    -KeyType rsa-2048
```

###### Example 2

The following example gets the `rsa-2048` public endorsement key in
`der` format for the specified instance.

```
Get-EC2InstanceTpmEkPub `
    -InstanceId `i-1234567890abcdef0` `
    -KeyFormat der `
    -KeyType rsa-2048
```
