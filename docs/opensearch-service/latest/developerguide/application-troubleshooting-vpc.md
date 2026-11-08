

# Resolving VPC connectivity problems in OpenSearch UI
<a name="application-troubleshooting-vpc"></a>

When an OpenSearch UI application cannot reach a domain in a VPC, the cause is usually a missing VPC endpoint authorization, a security group that blocks port 443, or DNS attributes that are turned off on the VPC. The following table lists the symptoms and likely causes of VPC connectivity problems, so that you can identify where to start.


| Symptom | Likely cause | 
| --- | --- | 
| The data source reports that it is unavailable | VPC endpoint access is not authorized | 
| The data source reports that it is unhealthy | A security group is blocking traffic | 
| The application cannot reach the domain | DNS resolution is not enabled on the VPC | 
| Connectivity works intermittently | The domain is processing a change, or the endpoint is being reprovisioned | 

## Authorizing VPC endpoint access
<a name="application-troubleshooting-vpc-authorization"></a>

The most common VPC problem is that the OpenSearch UI service is not authorized to access the VPC endpoint. Check whether the authorization exists:

```
aws opensearch list-vpc-endpoint-access \
    --domain-name {{domain-name}} \
    --region {{region}}
```

If the response does not include `application.opensearchservice.amazonaws.com`, authorize it:

```
aws opensearch authorize-vpc-endpoint-access \
    --domain-name {{domain-name}} \
    --service application.opensearchservice.amazonaws.com \
    --region {{region}}
```

Allow 5 to 10 minutes for the authorization to propagate, and then check the data source health in your application.

Serverless collections use a network policy instead of endpoint authorization. The policy must list the OpenSearch UI service in `SourceServices`. To review the policies that exist, run `aws opensearchserverless list-security-policies --type network`.

## Allowing traffic through a security group
<a name="application-troubleshooting-vpc-securitygroup"></a>

Even when endpoint access is authorized, the security group of the domain must allow inbound traffic on TCP port 443. The following commands find the security group and review its inbound rules. Replace the {{placeholder values}} with your own information:

```
aws opensearch describe-domain \
    --domain-name {{domain-name}} \
    --region {{region}} \
    --query 'DomainStatus.VPCOptions.SecurityGroupIds'

aws ec2 describe-security-groups \
    --group-ids {{security-group-id}} \
    --region {{region}} \
    --query 'SecurityGroups[0].IpPermissions'
```

To add an inbound rule, specify either your VPC CIDR block or, for tighter control, the security group of the VPC endpoint as the source:

```
aws ec2 authorize-security-group-ingress \
    --group-id {{security-group-id}} \
    --protocol tcp \
    --port 443 \
    --source-group {{endpoint-security-group-id}} \
    --region {{region}}
```

The following table lists common security group mistakes.


| Mistake | Why it fails | Resolution | 
| --- | --- | --- | 
| Allowing only port 9200 | OpenSearch UI uses HTTPS on port 443 | Add an inbound rule for TCP 443 | 
| Restricting the source to a specific IP address | The IP address of the VPC endpoint can change | Use a CIDR block, or reference a security group | 
| No outbound rules | Responses cannot reach the endpoint | Allow outbound traffic | 
| The wrong VPC CIDR block | The source range does not match the endpoint subnet | Use the CIDR block of the VPC that holds the endpoint | 

## Enabling DNS resolution
<a name="application-troubleshooting-vpc-dns"></a>

VPC endpoints rely on DNS to route traffic. Both `enableDnsSupport` and `enableDnsHostnames` must be `true` on the VPC. The following commands check each attribute and enable it if required. Replace the {{placeholder values}} with your own information:

```
aws ec2 describe-vpc-attribute \
    --vpc-id {{vpc-id}} \
    --attribute enableDnsSupport \
    --region {{region}}

aws ec2 modify-vpc-attribute \
    --vpc-id {{vpc-id}} \
    --enable-dns-support '{"Value": true}' \
    --region {{region}}

aws ec2 describe-vpc-attribute \
    --vpc-id {{vpc-id}} \
    --attribute enableDnsHostnames \
    --region {{region}}

aws ec2 modify-vpc-attribute \
    --vpc-id {{vpc-id}} \
    --enable-dns-hostnames '{"Value": true}' \
    --region {{region}}
```

If you use Route 53 private hosted zones, confirm that they do not override the DNS entries of the VPC endpoint. A custom DNS configuration can interfere with the resolution that VPC endpoints rely on.

## Resolving intermittent OpenSearch UI VPC connectivity
<a name="application-troubleshooting-vpc-intermittent"></a>

Intermittent connectivity usually reflects a transient condition rather than a configuration error. Common causes include the following:
+ A domain that is processing a configuration change.
+ A security group that someone modified.
+ A VPC endpoint that OpenSearch UI is reprovisioning after a domain change.
+ Resource pressure on the domain.

Check whether the domain is processing a change:

```
aws opensearch describe-domain \
    --domain-name {{domain-name}} \
    --query 'DomainStatus.Processing'
```

If the value is `true`, wait for the change to finish. You can also review the `CPUUtilization` metric for the domain in Amazon CloudWatch.

## Checking VPC connectivity requirements
<a name="application-troubleshooting-vpc-checklist"></a>
+ VPC endpoint access is authorized for `application.opensearchservice.amazonaws.com`.
+ The security group allows inbound TCP 443, and allows outbound traffic.
+ The VPC has DNS support and DNS hostnames enabled.
+ The domain is active, and is not processing a change.
+ The access policy of the domain allows the OpenSearch UI service principal.
+ For a serverless collection, the network policy lists the service in `SourceServices`, and the data access policy grants read permissions.
+ No conflicting Route 53 private hosted zone overrides the endpoint DNS.