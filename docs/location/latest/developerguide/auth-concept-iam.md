

# IAM concepts
<a name="auth-concept-iam"></a>

AWS Identity and Access Management provides fine-grained access control for Amazon Location Service resources. Use IAM for server-side applications, backend services, and administrative tasks where you need full control over permissions.

**IAM policy**  
A JSON document that defines permissions for Amazon Location Service actions and resources. Policies specify which API operations are allowed or denied and can include conditions such as source IP address or request Region.

**IAM role**  
An identity with specific permissions that can be assumed by AWS services, applications, or users. Roles provide temporary credentials and are the recommended approach for applications running on AWS compute services.

**Resource ARN**  
The Amazon Resource Name that uniquely identifies an Amazon Location Service resource in IAM policies. For standalone APIs (Maps, Places, Routes), the resource ARN follows the format `arn:aws:geo-maps:{{region}}::provider/default`. For legacy resources (trackers, geofence collections), it includes the account ID and resource name.

**SigV4 signing**  
The AWS Signature Version 4 process used to authenticate IAM and Amazon Cognito requests. The AWS SDKs handle SigV4 signing automatically. API keys bypass SigV4 signing entirely.