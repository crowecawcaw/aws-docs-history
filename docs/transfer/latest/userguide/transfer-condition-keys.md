

# IAM condition keys for organizational governance
<a name="transfer-condition-keys"></a>

AWS Transfer Family provides IAM condition keys that allow you to restrict resource configurations in any IAM policy. These condition keys can be used in identity-based policies attached to users or roles, or Service Control Policies (SCPs) for organizational governance.

Service Control Policies are IAM policies that apply to an entire AWS organization, providing preventative guardrails across multiple accounts. When used in SCPs, these condition keys help enforce security and compliance requirements organization-wide.

**See also**
+ [Actions, resources, and condition keys for Transfer Family](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstransferfamily.html)
+ [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
+ Video describing how to enforce preventive guardrails using service control policies  
[![AWS Videos](http://img.youtube.com/vi/mEO05mmbSms/0.jpg)](http://www.youtube.com/watch?v=mEO05mmbSms)

## Available condition keys
<a name="scp-condition-keys"></a>

AWS Transfer Family supports the following condition keys for use in IAM policies:

`transfer:RequestServerEndpointType`  
Restricts server creation and updates based on endpoint type (PUBLIC, VPC, VPC\_ENDPOINT). Commonly used to prevent public-facing endpoints.

`transfer:RequestServerProtocols`  
Restricts server creation and updates based on supported protocols (SFTP, FTPS, FTP, AS2).

`transfer:RequestServerDomain`  
Restricts server creation based on domain type (S3, EFS).

`transfer:RequestConnectorProtocol`  
Restricts connector creation based on protocol (AS2, SFTP).

## Supported actions
<a name="scp-supported-actions"></a>

The condition keys can be applied to the following AWS Transfer Family actions:
+ `CreateServer`: Supports `RequestServerEndpointType`, `RequestServerProtocols`, and `RequestServerDomain` condition keys
+ `UpdateServer`: Supports `RequestServerEndpointType` and `RequestServerProtocols` condition keys
+ `CreateConnector`: Supports `RequestConnectorProtocol` condition key

## Example SCP policy
<a name="scp-example-policy"></a>

The following example SCP prevents the creation of public AWS Transfer Family servers across your organization:

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
        "Sid": "DenyPublicTransferServers",
        "Effect": "Deny",
        "Action": ["transfer:CreateServer", "transfer:UpdateServer"],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "transfer:RequestServerEndpointType": "PUBLIC"
            }
        }
    }]
}
```