# Authenticating and authorizing for
 directory buckets in Local Zones

Directory buckets in Local Zones support both AWS Identity and Access Management (IAM) authorization and session-based
 authorization. For more information about authentication and authorization for
 directory buckets, see [Authenticating and authorizing requests](s3-express-authenticating-authorizing.md "s3-express-authenticating-authorizing.md").


## Resources


Amazon Resource Names (ARNs) for directory buckets contain the
 `s3express` namespace, the AWS parent Region, the AWS account ID, and
 the directory bucket name which includes the Zone ID. To access and perform actions on
 your directory bucket, you must use the following ARN format:



```
arn:aws:s3express:`region-code`:`account-id`:bucket/`bucket-base-name`--`ZoneID`--x-s3
```

For directory buckets in a Local Zone, the Zone ID is the ID of the Local Zone. For more
 information about directory buckets in Local Zones, see [Concepts for directory buckets in
 Local Zones](s3-lzs-for-directory-buckets.md "s3-lzs-for-directory-buckets.md"). For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html")
 in the *IAM User Guide*. For more information about resources, see
 [IAM JSON
 Policy Elements: Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html") in the
 *IAM User Guide*.


## Condition keys for directory buckets in
 Local Zones


In Local Zones, you can use all of these [condition keys](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3express.html#amazons3express-policy-keys "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3express.html#amazons3express-policy-keys") in your IAM policies.
 Additionally, to create a data perimeter around your Local Zone network border groups, you can
 use the condition key `s3express:AllAccessRestrictedToLocalZoneGroup` to deny
 all requests from outside the groups. 


The following condition key can be used to further refine the conditions under which an IAM policy statement applies. For a complete list of API
 operations, policy actions, and condition keys that are supported by directory buckets,
 see [Policy actions for directory buckets](s3-express-security-iam.md#s3-express-security-iam-actions "s3-express-security-iam.md#s3-express-security-iam-actions").


###### Note

The following condition key only applies to Local Zones and isn't supported in Availability Zones and AWS Regions.




| API operations | Policy actions | Description | Condition key | Description | Type |
| --- | --- | --- | --- | --- | --- |
| [Zonal
 endpoint API operations](s3-express-APIs.md "s3-express-APIs.md") | `s3express:CreateSession` | Grants permission to create a session token, which is used for
 granting access to all Zonal endpoint API operations, such as
 `CreateSession`, `HeadBucket`,
 `CopyObject`, `PutObject`, and
 `GetObject`. | `s3express:AllAccessRestrictedToLocalZoneGroup` | Filters all access to the bucket unless the request originates from the AWS Local Zone network
 border groups provided in this condition key. 
**Values:**
 Local Zone network border group value
  | `String` |


## Example policies


To
 restrict object access to requests from within a data residency boundary that you define
 (specifically, a Local Zone Group which is a set of Local Zones parented to the same
 AWS Region), you can set any of the following policies:



* The service control policy (SCP). For information about SCPs, see [Service
 control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html") in the
 *AWS Organizations User Guide*.
* The IAM identity-based policy for the IAM role.
* The VPC endpoint policy. For more information about the VPC endpoint policies,
 see [Control access to VPC
 endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html") in the
 *AWS PrivateLink Guide*.
* The S3 bucket policy.

###### Note

The condition key `s3express:AllAccessRestrictedToLocalZoneGroup` doesn't support access from an on-premises environment. 
 To support the access from an on-premises environment, you must add 
 the source IP to the policies. For more information, see [aws:SourceIp](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceip "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceip") in the IAM User Guide. 


###### Example – SCP policy


```

{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Access-to-specific-LocalZones-only",
            "Effect": "Deny",
            "Action": [
                "s3express:*",
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEqualsIfExists": {
                    "s3express:AllAccessRestrictedToLocalZoneGroup": [
                        "`local-zone-network-border-group-value`"
                    ]
                }
            }
        }
    ]
}
						
```

###### Example – IAM identity-based policy (attached to IAM role)


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": {
 "Effect": "Deny",
 "Action": "s3express:CreateSession",
 "Resource": "*",
 "Condition": {
 "StringNotEqualsIfExists": {
 "s3express:AllAccessRestrictedToLocalZoneGroup": [
 "`local-zone-network-border-group-value`"
 ] 
 }
 }
 }
}` 

```





###### Example – VPC endpoint policy


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 { 
 "Sid": "Access-to-specific-LocalZones-only",
 "Principal": "*",
 "Action": "s3express:CreateSession",
 "Effect": "Deny",
 "Resource": "*",
 "Condition": {
 "StringNotEqualsIfExists": {
 "s3express:AllAccessRestrictedToLocalZoneGroup": [
 "`local-zone-network-border-group-value`"
 ]
 } 
 }
 }
 ]
}` 

```





###### Example – bucket policy


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 { 
 "Sid": "Access-to-specific-LocalZones-only",
 "Principal": "*",
 "Action": "s3express:CreateSession",
 "Effect": "Deny",
 "Resource": "*",
 "Condition": {
 "StringNotEqualsIfExists": {
 "s3express:AllAccessRestrictedToLocalZoneGroup": [
 "`local-zone-network-border-group-value`"
 ]
 } 
 }
 }
 ]
}` 

```
