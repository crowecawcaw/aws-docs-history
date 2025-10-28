# Retrieve the instance identity document for an EC2 instance

The instance identity document for an Amazon EC2 instance uses a plaintext JSON format. For a description of the
contents of an instance identity document, see [Instance identity documents for Amazon EC2 instances](instance-identity-documents.md "instance-identity-documents.md").

The instance identity document is stored in the instance metadata for the instance, in the `instance-identity/document`
dynamic data category. You access the instance identity document for an instance by connecting to the instance
and retrieving it from the instance metadata.

You can access instance metadata using the IPv4 address 169.254.169.254 or
the IPv6 address fd00:ec2::254. These are [Link-local addresses](using-instance-addressing.md#link-local-addresses "using-instance-addressing.md#link-local-addresses"), meaning that
you can access them only from the instance. The examples on this page use the IPv4
address of the IMDS: 169.254.169.254. To retrieve instance
metadata for EC2 instances over IPv6, use fd00:ec2::254.

To verify the authenticity of an instance identity document after you retrieve it, see [Verify instance identity document](verify-iid.md "verify-iid.md").

IMDSv2

###### Linux

Run the following command from your Linux instance to retrieve the
instance identity document.

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document
```

###### Windows

Run the following cmdlet from your Windows instance to retrieve the
instance identity document.

```
[string]$token = (Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token-ttl-seconds' = '21600'} `
    -Method PUT -Uri 'http://169.254.169.254/latest/api/token' -UseBasicParsing).Content
```

```
(Invoke-WebRequest -Headers @{'X-aws-ec2-metadata-token' = $token} `
    -Uri 'http://169.254.169.254/latest/dynamic/instance-identity/document' -UseBasicParsing).Content
```

IMDSv1

###### Linux

Run the following command from your Linux instance to retrieve the
instance identity document.

```
curl http://169.254.169.254/latest/dynamic/instance-identity/document
```

###### Windows

Run the following cmdlet from your Windows instance to retrieve the
instance identity document.

```
(Invoke-WebRequest http://169.254.169.254/latest/dynamic/instance-identity/document).Content
```

The following is example output.

```
{
    "devpayProductCodes" : null,
    "marketplaceProductCodes" : [ "1abc2defghijklm3nopqrs4tu" ],
    "availabilityZone" : "us-west-2b",
    "privateIp" : "10.158.112.84",
    "version" : "2017-09-30",
    "instanceId" : "i-1234567890abcdef0",
    "billingProducts" : null,
    "instanceType" : "t2.micro",
    "accountId" : "123456789012",
    "imageId" : "ami-5fb8c835",
    "pendingTime" : "2016-11-19T16:32:11Z",
    "architecture" : "x86_64",
    "kernelId" : null,
    "ramdiskId" : null,
    "region" : "us-west-2"
}
```
