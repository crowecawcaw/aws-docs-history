The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Quotas for the AWS Partner Central Channel API

The AWS Partner Central Channel API has the following quotas.

## Request quotas

Request quotas| API operations | Quota (per AWS account) |
| --- | --- |
| CreateProgramManagementAccount | 3 per second |
| UpdateProgramManagementAccount | 3 per second |
| ListProgramManagementAccounts | 5 per second |
| DeleteProgramManagementAccount | 3 per second |
| CreateChannelHandshake | 3 per second |
| ListChannelHandshakes | 5 per second |
| AcceptChannelHandshake | 3 per second |
| RejectChannelHandshake | 3 per second |
| CancelChannelHandshake | 3 per second |
| CreateRelationship | 3 per second |
| GetRelationship | 5 per second |
| ListRelationships | 5 per second |
| UpdateRelationship | 3 per second |
| DeleteRelationship | 3 per second |

## Additional quotas

Additional quotas| Display name | Catalog | Description | Default value |
| --- | --- | --- | --- |
| Program management accounts | AWS | The maximum number of program management accounts you can create in the AWS catalog | 50 |
| Relationships per program management account | AWS | The maximum number of relationships you can establish per program management account in the AWS catalog | 1,000 |
| Program management account handshakes per account | AWS | The maximum number of active program management account handshakes in the AWS catalog | 100 |
| Start service period handshakes per account | AWS | The maximum number of active handshakes for establishing service periods in the AWS catalog | 200 |
| Revoke service period handshakes per account | AWS | The maximum number of active handshakes for revoking service periods in the AWS catalog | 200 |
| Rate of program management account handshakes per day | AWS | The maximum number of program management account handshakes you can send to the same AWS account per day in the AWS catalog | 5 |
| Rate of start service period handshakes per day | AWS | The maximum number of start service period handshakes you can send to the same AWS account per day in the AWS catalog | 5 |
| Rate of revoke service period handshakes per day | AWS | The maximum number of revoke service period handshakes you can send to the same AWS account per day in the AWS catalog | 5 |
| Program management accounts | Sandbox | The maximum number of program management accounts you can create in the Sandbox catalog | 50 |
| Relationships per program management account | Sandbox | The maximum number of relationships you can establish per program management account in the Sandbox catalog | 1,000 |
| Program management account handshakes per account | Sandbox | The maximum number of active program management account handshakes in the Sandbox catalog | 100 |
| Start service period handshakes per account | Sandbox | The maximum number of active handshakes for establishing service periods in the Sandbox catalog | 200 |
| Revoke service period handshakes per account | Sandbox | The maximum number of active handshakes for revoking service periods in the Sandbox catalog | 200 |
| Rate of program management account handshakes per day | Sandbox | The maximum number of program management account handshakes you can send to the same AWS account per day in the Sandbox catalog | 5 |
| Rate of start service period handshakes per day | Sandbox | The maximum number of start service period handshakes you can send to the same AWS account per day in the Sandbox catalog | 5 |
| Rate of revoke service period handshakes per day | Sandbox | The maximum number of revoke service period handshakes you can send to the same AWS account per day in the Sandbox catalog | 5 |

## Understanding and managing quotas

### Rate limiting

When an API rate limit is reached, the service will respond with a
ThrottlingException. To better handle rate limiting, AWS recommends implementing exponential backoff and retry strategies in your application.

### Requesting a quota increase

If the default quotas do not meet your requirements, you can request a quota
increase through the [Service Quotas page](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard"). The Service Quotas console is a browser-based
interface that you can use to view and manage your service quotas. You can access
Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or
by searching for Service Quotas in the AWS Management Console.
