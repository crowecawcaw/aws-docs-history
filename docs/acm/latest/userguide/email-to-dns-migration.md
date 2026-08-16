# Migrating from email to DNS validation

You can migrate an existing email-validated public AWS Certificate Manager (ACM) certificate to
DNS validation. The certificate ARN does not change during migration. Your existing
infrastructure references—such as load balancer configurations and CI/CD pipelines—
continue to work without modification.

DNS-validated certificates can be renewed automatically by ACM. Email-validated
certificates require you to manually approve a validation email for every renewal. As
certificate validity periods decrease, migrating to DNS validation reduces the
operational overhead of certificate renewal.
