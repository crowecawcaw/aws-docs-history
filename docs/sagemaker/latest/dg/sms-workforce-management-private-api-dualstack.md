# Enable a dual-stack

workforce

You can enable a dual-stack workforce by using the [CreateWorkforce](../APIReference/API_CreateWorkforce.md "../APIReference/API_CreateWorkforce.md") and [UpdateWorkforce](../APIReference/API_UpdateWorkforce.md "../APIReference/API_UpdateWorkforce.md") API operations. Creating a dual-stack workforce, updating
an existing workforce to dual-stack, and changing a workforce from dual-stack back to
IPv4 are not supported in AWS Management Console.

###### Important

A workforce without a defined `IpAddressType` defaults to
`IPv4`.

## Create a

dual-stack workforce

The process for creating a dual-stack workforce is similar to creating an
IPv4-only workforce, with the exceptions noted below. For more information, see
[CreateWorkforce](../APIReference/API_CreateWorkforce.md "../APIReference/API_CreateWorkforce.md").

- To attach a VPC to the private workforce, ensure the VPC is also
  dual-stack, with IPv6 CIDR blocks associated with the VPC's subnets.
- To use the `SourceIpConfig` parameter to restrict traffic to a
  specific IP address range, ensure that IPv6 CIDR blocks are also included in
  the list.
- To implement policies with `SourceIp` conditions on S3 buckets
  accessed by your tasks, ensure those policies are updated to be dual-stack
  compatible.
- Your identity provider authentication endpoint supports dual-stack. For
  more information, see [Authentication flow](../../../elasticloadbalancing/latest/application/listener-authenticate-users.md#authentication-flow "../../../elasticloadbalancing/latest/application/listener-authenticate-users.md#authentication-flow").

**Example `CreateWorkforce` SDK call using
boto3**

For more information, see [create_workforce](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_workforce.html#SageMaker.Client.create_workforce "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_workforce.html#SageMaker.Client.create_workforce").

```
import boto3

client = boto3.resource('sagemaker')

# IpAddressType = 'dualstack'|'ipv4'
client.create_workforce(
    WorkforceName='string',
    IpAddressType='dualstack',
    WorkforceConfig={
        'CognitoConfig': {
            'UserPool': 'string',
            'Client': 'string'
        }
    }
)
```

## Update a

dual-stack workforce

When updating an existing workforce to be dual-stack, note the following. For more
information, see [UpdateWorkforce](../APIReference/API_UpdateWorkforce.md "../APIReference/API_UpdateWorkforce.md") and [IPv6 support for your
VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md").

- If a VPC is attached to the workforce, you must update the VPC to be
  dual-stack. Also ensure that any security groups for the VPC allow IPv6
  traffic.
- If you're using the `SourceIpConfig` parameter, update it to include IPv6
  CIDR blocks.
- To implement policies with `SourceIp` conditions on S3 buckets
  accessed by your tasks, ensure those policies are updated to be dual-stack
  compatible.
- Your identity provider authentication endpoint supports dual-stack. For
  more information, see [Authentication flow](../../../elasticloadbalancing/latest/application/listener-authenticate-users.md#authentication-flow "../../../elasticloadbalancing/latest/application/listener-authenticate-users.md#authentication-flow").

**Example `UpdateWorkforce` SDK call using
boto3**

For more information, see [update_workforce](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_workforce.html#SageMaker.Client.update_workforce "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_workforce.html#SageMaker.Client.update_workforce").

```
import boto3

client = boto3.resource('sagemaker')

# IpAddressType = 'dualstack'|'ipv4'
client.update_workforce(
    WorkforceName='string',
    IpAddressType='dualstack'
)
```
