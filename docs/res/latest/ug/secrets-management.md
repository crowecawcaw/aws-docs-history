# Secrets management

Research and Engineering Studio maintains the following secrets using AWS Secrets Manager. RES creates secrets
automatically during environment creation. Secrets entered by the administrator during environment
creation are entered as parameters.

| Secret name                                         | Description                                                       | RES generated | Admin entered |
| --------------------------------------------------- | ----------------------------------------------------------------- | ------------- | ------------- |
| ``<envname>`-sso-client-secret`                     | Single Sign-On OAuth2 Client Secret for environment               | ✓             |               |
| ``<envname>`-vdc-client-secret`                     | vdc ClientSecret                                                  | ✓             |               |
| ``<envname>`-vdc-client-id`                         | vdc ClientId                                                      | ✓             |               |
| ``<envname>`-vdc-gateway-certificate-private-key`   | Self-Signed certificate private key for domain                    | ✓             |               |
| ``<envname>`-vdc-gateway-certificate-certificate`   | Self-Signed certificate for domain                                | ✓             |               |
| ``<envname>`-cluster-manager-client-secret`         | cluster-manager ClientSecret                                      | ✓             |               |
| ``<envname>`-cluster-manager-client-id`             | cluster-manager ClientId                                          | ✓             |               |
| ``<envname>`-external-private-key`                  | Self-Signed certificate private key for domain                    | ✓             |               |
| ``<envname>`-external-certificate`                  | Self-Signed certificate for domain                                | ✓             |               |
| ``<envname>`-internal-private-key`                  | Self-Signed certificate private key for domain                    | ✓             |               |
| ``<envname>`-internal-certificate`                  | Self-Signed certificate for domain                                | ✓             |               |
| ``<envname>`-directoryservice-ServiceAccountUserDN` | The Distinguished Name (DN) attribute of the ServiceAccount user. | ✓             |               |

The following secret ARN values are contained in the
``<envname>`-cluster-settings` table in DynamoDB:

| Key                                                                       | Source |
| ------------------------------------------------------------------------- | ------ |
| `identity-provider.cognito.sso_client_secret`                             |        |
| `vdc.dcv_connection_gateway.certificate.certificate_secret_arn`           | stack  |
| `vdc.dcv_connection_gateway.certificate.private_key_secret_arn`           | stack  |
| `cluster.load_balancers.internal_alb.certificates.private_key_secret_arn` | stack  |
| `directoryservice.root_username_secret_arn`                               |        |
| `vdc.client_secret`                                                       | stack  |
| `cluster.load_balancers.external_alb.certificates.certificate_secret_arn` | stack  |
| `cluster.load_balancers.internal_alb.certificates.certificate_secret_arn` | stack  |
| `directoryservice.root_password_secret_arn`                               |        |
| `cluster.secretsmanager.kms_key_id`                                       |        |
| `cluster.load_balancers.external_alb.certificates.private_key_secret_arn` | stack  |
| `cluster-manager.client_secret`                                           |        |
