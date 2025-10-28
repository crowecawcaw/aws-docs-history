# Understanding IPv6 support in

Amazon Connect Customer Profiles

## Public Connectivity

All Amazon Connect Customer Profiles APIs fully support IPv4 and IPv6 calls.

```
profile.`Region`.api.aws
```

**For example:**

```
profile.us-east-1.api.aws
```

For AWS CLI, you'll need to use these endpoints explicitly:

```
aws customer-profiles list-domains \
    --endpoint https://profile.us-east-1.api.aws \
    --region us-east-1
```

The old APIs are still available as backward compatibility. They only support
IPv4 calls.

```
profile.`Region`.amazonaws.com
```

**For example:**

```
profile.us-east-1.amazonaws.com
```

## Private Connectivity

You can create a VPC endpoint for the Amazon Connect Customer Profiles service using either the Amazon
VPC console or the AWS Command Line Interface (AWS CLI). For more information,
see [Creating an
interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the AWS PrivateLink Guide.

Create a VPC endpoint for Amazon Connect Customer Profiles using the following service name:

```
com.amazonaws.`Region`.profile
```

**For example:**

```
com.amazonaws.us-east-1.profile
```

If you enable private DNS for the endpoint, you can make API requests to
Amazon Connect Customer Profiles using its IPv4 and IPv6 supported DNS name for the Region, for example,
profile.us-east-1.api.aws.

Alternatively, old DNS name for the region is also supported as IPv4
only.

**For example:**

```
profile.us-east-1.amazonaws.com
```
