

# VPC endpoint policies for syslog
<a name="CWL_Syslog_VPCEndpointPolicies"></a>

You can attach a VPC endpoint policy to your syslog VPC endpoint to control what traffic is allowed through it. This provides an additional layer of access control beyond security groups and resource policies.

By default, a VPC endpoint has a full-access policy that allows all traffic. You can restrict this by attaching a custom policy. For more information about VPC endpoint policies, see [Control access using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Important**  
Syslog traffic arrives as an anonymous principal (no IAM identity on the wire). Policies must use `"Principal": "*"` and scope access using action, resource, or VPC condition keys. Principal-scoped policies (for example, policies that allow only a specific IAM role) will deny all syslog traffic.

## Supported condition keys
<a name="CWL_Syslog_VPCEndpointPolicies_ConditionKeys"></a>

The following condition keys are supported in VPC endpoint policies for syslog:


| Condition key | Description | Example value | 
| --- | --- | --- | 
| aws:SourceVpc | The VPC from which the traffic originates. | vpc-111bbb22 | 
| aws:SourceVpce | The VPC endpoint through which the traffic arrives. | vpce-0abc123def456 | 
| aws:VpcSourceIp | The private IP address of the sender within the VPC. | 10.0.1.50 | 
| aws:ResourceAccount | The account that owns the target log group. | 123456789012 | 
| aws:ResourceOrgID | The organization ID of the account that owns the target log group. | o-aa111bb222 | 
| aws:ResourceOrgPaths | The organizational unit path of the account that owns the target log group. | o-aa111bb222/r-ab12/ou-ab12-11111111/\* | 

The following condition keys are **not supported** because syslog traffic has no IAM principal identity:
+ `aws:PrincipalArn`
+ `aws:PrincipalAccount`
+ `aws:PrincipalOrgID`
+ `aws:PrincipalOrgPaths`
+ `aws:PrincipalTag/*`

Policies that use unsupported condition keys will result in an implicit deny, blocking all syslog traffic through the endpoint.

## Restrict to a specific log group
<a name="CWL_Syslog_VPCEndpointPolicies_RestrictLogGroup"></a>

The following policy allows syslog traffic only to a specific log group:

```
aws ec2 modify-vpc-endpoint \
  --vpc-endpoint-id $VPCE_ID \
  --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "logs:PutLogEvents",
      "Resource": "arn:aws:logs:{{Region}}:{{account-id}}:log-group:/syslog/my-devices"
    }
  ]
}' \
  --region $REGION
```

## Deny all traffic
<a name="CWL_Syslog_VPCEndpointPolicies_DenyAll"></a>

The following policy blocks all syslog traffic through the endpoint. This is useful for temporarily stopping ingestion without deleting the endpoint:

```
aws ec2 modify-vpc-endpoint \
  --vpc-endpoint-id $VPCE_ID \
  --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "*"
    }
  ]
}' \
  --region $REGION
```

## Reset to default policy
<a name="CWL_Syslog_VPCEndpointPolicies_Reset"></a>

To restore the default allow-all policy:

```
aws ec2 modify-vpc-endpoint \
  --vpc-endpoint-id $VPCE_ID \
  --reset-policy \
  --region $REGION
```

## Policy propagation
<a name="CWL_Syslog_VPCEndpointPolicies_Propagation"></a>

After you create or modify a VPC endpoint policy, it can take up to several minutes for the policy change to take effect. During this propagation period, the previous policy (or default policy) continues to apply.

If a VPC endpoint policy denies syslog traffic, you will see the following indicators:
+ TCP connections are closed immediately after the policy evaluation.
+ UDP datagrams are dropped.
+ The `SyslogMessagesDropped` metric with `Reason=VpcePolicyDenied` is emitted.
+ The `SyslogConnectionsRejected` metric with `Reason=VpcePolicyDenied` is emitted for TCP connections.