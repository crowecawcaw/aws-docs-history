# Retrieve the AWS Marketplace product code from your instance

You can retrieve the AWS Marketplace product code for your instance using its instance metadata.
If the instance has a product code, Amazon EC2 returns it. For more information about
retrieving metadata, see [Access instance metadata for an EC2 instance](instancedata-data-retrieval.md "instancedata-data-retrieval.md").

IMDSv2

###### Linux

Run the following command from your Linux instance.

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/product-codes
```

###### Windows

Run the following cmdlets from your Windows instance.

```
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/product-codes
```

IMDSv1

###### Linux

Run the following command from your Linux instance.

```
curl http://169.254.169.254/latest/meta-data/product-codes
```

###### Windows

Run the following command from your Windows instance.

```
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/product-codes
```
