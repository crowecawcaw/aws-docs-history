

# Secrets management
<a name="secrets-management"></a>

Research and Engineering Studio maintains the following secrets using AWS Secrets Manager. RES creates secrets automatically during environment creation. Secrets entered by the administrator during environment creation are entered as parameters.


| Secret name |  Description  |  RES generated | Admin entered | 
| --- | --- | --- | --- | 
| {{<envname>}}-sso-client-secret | Single Sign-On OAuth2 Client Secret for environment | ✓ |  | 
| {{<envname>}}-vdc-client-secret | VDC ClientSecret | ✓ |  | 
| {{<envname>}}-vdc-client-id | VDC ClientId | ✓ |  | 
| {{<envname>}}-vdc-gateway-certificate-private-key | Self-Signed certificate private key for domain | ✓ |  | 
| {{<envname>}}-vdc-gateway-certificate-certificate | Self-Signed certificate for domain | ✓ |  | 
| {{<envname>}}-cluster-manager-client-secret | cluster-manager ClientSecret | ✓ |  | 
| {{<envname>}}-cluster-manager-client-id | cluster-manager ClientId | ✓ |  | 
| {{<envname>}}-external-private-key | Self-Signed certificate private key for domain | ✓ |  | 
| {{<envname>}}-external-certificate | Self-Signed certificate for domain | ✓ |  | 
| {{<envname>}}-internal-private-key | Self-Signed certificate private key for domain | ✓ |  | 
| {{<envname>}}-internal-certificate | Self-Signed certificate for domain | ✓ |  | 
| {{<envname>}}-directoryservice-ServiceAccountUserDN | The Distinguished Name (DN) attribute of the ServiceAccount user. | ✓ |  | 

The following secret ARN values are contained in the `{{<envname>}}-cluster-settings` table in DynamoDB:


| Key | Source | 
| --- | --- | 
| identity-provider.cognito.sso\_client\_secret |  | 
| vdc.dcv\_connection\_gateway.certificate.certificate\_secret\_arn | stack | 
| vdc.dcv\_connection\_gateway.certificate.private\_key\_secret\_arn | stack | 
| cluster.load\_balancers.internal\_alb.certificates.private\_key\_secret\_arn | stack | 
| directoryservice.root\_username\_secret\_arn |  | 
| vdc.client\_secret | stack | 
| cluster.load\_balancers.external\_alb.certificates.certificate\_secret\_arn | stack | 
| cluster.load\_balancers.internal\_alb.certificates.certificate\_secret\_arn | stack | 
| directoryservice.root\_password\_secret\_arn |  | 
| cluster.secretsmanager.kms\_key\_id |  | 
| cluster.load\_balancers.external\_alb.certificates.private\_key\_secret\_arn | stack | 
| cluster-manager.client\_secret |  | 