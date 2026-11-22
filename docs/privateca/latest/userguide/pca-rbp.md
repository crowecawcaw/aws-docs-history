

# Resource-based policies

Resource-based policies are permissions policies that you create and manually attach to a resource (in this case, a private CA) rather than to a user identity or role. Or, instead of creating your own policies, you can use AWS managed policies for AWS Private CA. Using AWS RAM to apply a resource-based policy, an AWS Private CA administrator can share access to a CA with a user in a different AWS account directly or through AWS Organizations. Alternatively, an AWS Private CA administrator can use the PCA APIs [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html), [GetPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html), and [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html), or the corresponding AWS CLI commands [put-policy](https://docs.aws.amazon.com/cli/latest/reference/acm-pca/put-policy.html), [get-policy](https://docs.aws.amazon.com/cli/latest/reference/acm-pca/get-policy.html), and [delete-policy](https://docs.aws.amazon.com/cli/latest/reference/acm-pca/delete-policy.html), to apply and manage resource-based policies.

For general information about resource-based policies, see [Identity-Based Policies and Resource-Based Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) and [Controlling Access Using Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html).

To view the list of AWS managed resource-based policies for AWS Private CA, navigate to the [Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions:) in the AWS Resource Access Manager console, and search for **CertificateAuthority**. As with any policy, before you apply it, we recommend applying the policy in a test environment to ensure that it meets your requirements.

AWS Private CA also supports RAM customer managed permissions, which allow you to define a custom combination of actions from the following set: `DescribeCertificateAuthority`, `GetCertificate`, `GetCertificateAuthorityCertificate`, `ListPermissions`, `ListTags`, `IssueCertificate`, and `RevokeCertificate`. Customer managed permissions give you the flexibility to grant least-privilege access – for example, granting read-only access to some accounts while allowing others to issue and revoke certificates. For more information, see [Customer managed permissions in RAM](pca-cmp.md).

AWS Certificate Manager (ACM) users with cross-account shared access to a private CA can issue managed certificates that are signed by the CA. When you grant permission to the `IssueCertificate` action, you can restrict the certificate templates used for certificate issuance by adding a `acm-pca:TemplateArn` Condition to the policy.

You can also add X.509 certificate condition keys to the `Allow` statement for `IssueCertificate` to restrict the certificates that cross-account principals can request. Resource-based policies don't support `Deny` statements. For more information, see [Control certificate issuance with X.509 certificate condition keys](certguard-condition-keys.md).

## Policy examples
<a name="rbp-policy-examples"></a>

This section provides example cross-account policies for various needs. In all cases, the following command pattern is used to apply a policy:

```
$ aws acm-pca put-policy \
   --region {{region}} \
   --resource-arn arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}} \
   --policy file:///{{[path]}}/{{policyN.json}}
```

In addition to specifying the ARN of a CA, the administrator provides an AWS account ID or an AWS Organizations ID that will be granted access to the CA. The JSON of each of the following policies is formatted as a file for readability, but can also be supplied as an inline CLI arguments.

**Note**  
The following policies are starting points. You can change the actions that you grant and add conditions, such as X.509 certificate condition keys, to fit your needs. For the actions that you can include, see [Customer managed permissions in RAM](pca-cmp.md).

1. **File: policy1.json – Sharing access to a CA with a user in a different account** 

   Replace {{555555555555}} with the AWS account ID that's sharing the CA.

   For the resource ARN, replace the following with your own values:
   + `{{aws}}` - The AWS partition. For example, `aws`, `aws-us-gov`, `aws-cn`, etc.
   + `{{us-east-1}}` - The AWS Region that the resource is available in, such as `us-west-1`.
   + `{{111122223333}}` - The AWS account ID of the resource owner.
   + `{{11223344-1234-1122-2233-112233445566}}` - The resource ID of the certificate authority.

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [{
               "Sid": "{{ExampleStatementID}}",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "{{555555555555}}"
               },
               "Action": [
                   "acm-pca:DescribeCertificateAuthority",
                   "acm-pca:GetCertificate",
                   "acm-pca:GetCertificateAuthorityCertificate",
                   "acm-pca:ListPermissions",
                   "acm-pca:ListTags"
               ],
               "Resource": "arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}"
           },
           {
               "Sid": "{{ExampleStatementID2}}",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "{{555555555555}}"
               },
               "Action": [
                   "acm-pca:IssueCertificate"
               ],
               "Resource": "arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}",
               "Condition": {
                   "StringEquals": {
                       "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/EndEntityCertificate/V1"
                   }
               }
           }
       ]
   }
   ```

------

1. **File: policy2.json – Sharing access to a CA through AWS Organizations**

   

   Replace {{o-a1b2c3d4z5}} with the AWS Organizations ID.

   For the resource ARN, replace the following with your own values:
   + `{{aws}}` - The AWS partition. For example, `aws`, `aws-us-gov`, `aws-cn`, etc.
   + `{{us-east-1}}` - The AWS Region that the resource is available in, such as `us-west-1`.
   + `{{111122223333}}` - The AWS account ID of the resource owner.
   + `{{11223344-1234-1122-2233-112233445566}}` - The resource ID of the certificate authority.

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "{{ExampleStatementID3}}",
               "Effect": "Allow",
               "Principal": "*",
               "Action": "acm-pca:IssueCertificate",
               "Resource":"arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}",
               "Condition": {
                   "StringEquals": {
                       "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/EndEntityCertificate/V1",
                       "aws:PrincipalOrgID": "{{o-a1b2c3d4z5}}"
                   },
                   "StringNotEquals": {
                       "aws:PrincipalAccount": "{{111122223333}}"
                   }
               }
           },
           {
               "Sid": "{{ExampleStatementID4}}",
               "Effect": "Allow",
               "Principal": "*",
               "Action": [
                   "acm-pca:DescribeCertificateAuthority",
                   "acm-pca:GetCertificate",
                   "acm-pca:GetCertificateAuthorityCertificate",
                   "acm-pca:ListPermissions",
                   "acm-pca:ListTags"
               ],
               "Resource":"arn:aws:acm-pca:{{us-east-1}}:{{123456789012}}:certificate-authority/{{CA_ID}}",
               "Condition": {
                   "StringEquals": {
                       "aws:PrincipalOrgID": "{{o-a1b2c3d4z5}}"
                   },
                   "StringNotEquals": {
                       "aws:PrincipalAccount": "{{111122223333}}"
                   }
               }
           }
       ]
   }
   ```

------

## Allow connector creation when you use X.509 certificate condition keys
<a name="connector-permission-check-condition-keys"></a>

When you create a connector with Connector for AD or Connector for SCEP, the connector checks its permissions by sending a test certificate request to `acm-pca:IssueCertificate`, once as its service principal and once with your identity through `aws:CalledVia`. AWS Private CA evaluates your policies for this request and then rejects it by design, so it doesn't issue a certificate. AWS CloudTrail records both test requests as `IssueCertificate` events that failed with a `ValidationException`. These errors are expected. If either request is denied, the event shows an `AccessDenied` error code instead.

The simplest way to keep connector creation working is to grant `acm-pca:IssueCertificate` to the connector without X.509 certificate condition keys (`acm-pca:x509*`). The AWS RAM managed permissions for connectors and the policies in the connector setup topics do this. If you do add these condition keys to a policy that applies to either request, the conditions must permit the values in the following table. Otherwise, connector creation fails with `PRIVATECA_ACCESS_DENIED`. If a `Deny` statement in an SCP, RCP, or identity-based policy applies to the connector's requests, scope it as described in [Before you deploy a policy](certguard-before-you-deploy.md). For information about these keys, see [Control certificate issuance with X.509 certificate condition keys](certguard-condition-keys.md).


| Condition key | Connector for AD | Connector for SCEP | 
| --- | --- | --- | 
| acm-pca:TemplateArn | arn:aws:acm-pca:::template/BlankEndEntityCertificate\_APIPassthrough/V1 | arn:aws:acm-pca:::template/BlankEndEntityCertificate\_APICSRPassthrough/V1 | 
| acm-pca:x509Subject/CN (use a set operator such as ForAllValues:StringEquals) | AWS Private CA Connector for Active Directory permission check | AWS Private CA Connector for SCEP permission check | 
| acm-pca:x509Signature/algorithm | The signing algorithm that the connector uses for your CA key type, for example sha256WithRSAEncryption for an RSA CA | The signing algorithm that the connector uses for your CA key type, for example sha256WithRSAEncryption for an RSA CA | 
| acm-pca:x509Key/algorithm | RSA | RSA | 
| acm-pca:x509Key/size | 2048 | 2048 | 
| acm-pca:x509Validity/durationDays | 1 | 1 | 
| acm-pca:x509Validity/durationHours | 25 (AWS Private CA sets notBefore to 60 minutes before issuance, so the one-day validity period spans 25 hours) | 25 (AWS Private CA sets notBefore to 60 minutes before issuance, so the one-day validity period spans 25 hours) | 
| acm-pca:x509SAN/present | false | false | 
| acm-pca:x509Ext/KeyUsage/present | false | false | 
| acm-pca:x509Ext/ExtendedKeyUsage/present | false | false | 
| acm-pca:x509Ext/BasicConstraints/present | true | true | 
| acm-pca:x509Ext/BasicConstraints/CA | false | false | 
| acm-pca:x509Ext/BasicConstraints/critical | false | false | 

The test request also has `acm-pca:x509Subject/empty` set to `false`, and `acm-pca:x509Validity/notBefore` and `acm-pca:x509Validity/notAfter` dates that depend on when you create the connector. It has no other X.509 certificate condition keys. For how absent keys affect `Deny` statements, see [How condition key values are evaluated](certguard-evaluation.md).

The following identity-based policy statement permits the test request that Connector for AD sends with your identity. Replace the CA ARN with your own. For Connector for SCEP, use the SCEP template, common name, and `pca-connector-scep.amazonaws.com`:

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowConnectorPermissionCheck",
            "Effect": "Allow",
            "Action": "acm-pca:IssueCertificate",
            "Resource": "arn:{{aws}}:acm-pca:{{us-east-1}}:{{111122223333}}:certificate-authority/{{11223344-1234-1122-2233-112233445566}}",
            "Condition": {
                "ArnLike": {
                    "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/BlankEndEntityCertificate_APIPassthrough/V*"
                },
                "ForAllValues:StringEquals": {
                    "acm-pca:x509Subject/CN": "AWS Private CA Connector for Active Directory permission check"
                },
                "Null": {
                    "acm-pca:x509Subject/CN": "false"
                },
                "StringEquals": {
                    "acm-pca:x509Key/algorithm": "RSA"
                },
                "NumericEquals": {
                    "acm-pca:x509Key/size": "2048"
                },
                "Bool": {
                    "acm-pca:x509SAN/present": "false",
                    "acm-pca:x509Ext/BasicConstraints/CA": "false",
                    "acm-pca:x509Ext/KeyUsage/present": "false",
                    "acm-pca:x509Ext/ExtendedKeyUsage/present": "false"
                },
                "NumericLessThanEquals": {
                    "acm-pca:x509Validity/durationDays": "1"
                },
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": "pca-connector-ad.amazonaws.com"
                }
            }
        }
    ]
}
```

The resource-based policy on your CA, which you manage with AWS RAM, authorizes the test request that uses the connector's service principal. Every certificate that the connector issues after it's created also uses the service principal. If you add X.509 certificate condition keys to a AWS RAM customer managed permission or an RCP, the conditions must permit both the values in the preceding table and the certificates that your connector issues.