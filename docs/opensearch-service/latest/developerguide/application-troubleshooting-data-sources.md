

# Resolving data source health and access errors in OpenSearch UI
<a name="application-troubleshooting-data-sources"></a>

Each data source that you associate with an OpenSearch UI application reports a health status.


| Status | Meaning | Action required | 
| --- | --- | --- | 
| Green, or healthy | Connected and operational | None | 
| Yellow | Connected but degraded, because replica shards are unassigned | Monitor. This can resolve on its own | 
| Red, or unhealthy | Connected, but primary shards are unavailable | Investigate the health of the domain | 
| Unavailable | A connection cannot be established | Check permissions, VPC configuration, and the domain status | 

## The domain cannot be found
<a name="application-troubleshooting-data-sources-notfound"></a>

When `update-application` reports that the domain does not exist, check the following:
+ The domain is in a different AWS Region than the application. List the domains in each Region with `aws opensearch list-domain-names --region {{region}}`.
+ The domain is in a different AWS account. For more information about cross-account access, see [Cross-Region and cross-account data access](application-cross-region-cross-account.md).
+ The ARN contains an incorrect domain name.
+ The domain was deleted. Confirm with `aws opensearch describe-domain --domain-name {{domain-name}}`.

## Access is denied when you associate a data source
<a name="application-troubleshooting-data-sources-denied"></a>

Confirm which principal you are using with `aws sts get-caller-identity`, and confirm that it has the following permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "es:UpdateApplication",
                "es:DescribeDomain",
                "es:DescribeDomains"
            ],
            "Resource": "*"
        }
    ]
}
```

Then review the access policy of the domain:

```
aws opensearch describe-domain-config \
    --domain-name {{domain-name}} \
    --query 'DomainConfig.AccessPolicies' \
    --region {{region}}
```

The access policy of the domain must allow the OpenSearch UI service principal.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "application.opensearchservice.amazonaws.com"
            },
            "Action": "es:ESHttp*",
            "Resource": "arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}/*"
        }
    ]
}
```

## The data source ARN is rejected
<a name="application-troubleshooting-data-sources-arn"></a>

The following table lists the ARN format that each kind of data source requires.


| Data source type | ARN format | 
| --- | --- | 
| Managed domain | arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}} | 
| Serverless collection | arn:aws:aoss:{{region}}:{{account-id}}:collection/{{collection-id}} | 

**Note**  
Serverless collections use `aoss` rather than `es`, and they use the collection ID rather than the collection name. To find the ID, run `aws opensearchserverless list-collections`.

## A cross-account data source is pending or unavailable
<a name="application-troubleshooting-data-sources-crossaccount"></a>

If a connection remains pending, no one has accepted it yet. List the pending connections and accept the one that you expect:

```
aws opensearch describe-inbound-connections \
    --filters '[{"Name":"connection-status","Values":["PENDING_ACCEPTANCE"]}]' \
    --region {{region}}

aws opensearch accept-inbound-connection \
    --connection-id {{connection-id}} \
    --region {{region}}
```

If a cross-account domain reports that it is unavailable, confirm that the cross-cluster connection is active, that the access policy of the remote domain includes the source account, and, for VPC domains, that VPC endpoint access is authorized for the OpenSearch UI service principal:

```
aws opensearch authorize-vpc-endpoint-access \
    --domain-name {{domain-name}} \
    --service application.opensearchservice.amazonaws.com \
    --region {{region}}
```

## A data source reports that it is unhealthy
<a name="application-troubleshooting-data-sources-unhealthy"></a>

An unhealthy data source means that the application can connect, but the domain itself has a problem.


| Cause | Symptoms | Resolution | 
| --- | --- | --- | 
| Red cluster status | Primary shards are unavailable | Check disk space and node health | 
| The domain is processing a change | A configuration change is in progress | Wait for processing to finish | 
| High JVM memory pressure | Slow queries and timeouts | Scale up the instance type, or add nodes | 
| Disk space is full | Write rejections | Delete old indexes, or increase storage | 
| Too many shards | Cluster instability | Reduce the shard count, and use Index State Management policies | 

## A serverless collection cannot be reached
<a name="application-troubleshooting-data-sources-serverless"></a>

If a collection does not appear in the data source list, confirm that it exists and is active, that it is in the same AWS Region as the application, and that your IAM permissions include `aoss:BatchGetCollection`.

A collection that reports access denied requires both a network policy, which allows the service to connect, and a data access policy, which allows the service to read data. The network policy must list the OpenSearch UI service in `SourceServices`:

```
[{
    "Rules": [{
        "ResourceType": "collection",
        "Resource": ["collection/{{collection-name}}"]
    }],
    "SourceServices": ["application.opensearchservice.amazonaws.com"]
}]
```

To review the policies that already exist, run `aws opensearchserverless list-security-policies --type network` and `aws opensearchserverless list-access-policies --type data`.

## A data source that was healthy becomes unavailable
<a name="application-troubleshooting-data-sources-reconnect"></a>

Check the following, in order:

1. Whether the domain is undergoing a configuration change.

1. Whether someone modified the access policy of the domain.

1. Whether someone revoked VPC endpoint authorization.

1. Whether someone changed the security group rules.

No action reconnects a data source. To re-establish the connection, remove the data source, wait two to three minutes, and add it again.

**Important**  
The `update-application` command replaces the entire data source list. Include every data source that you want to keep.