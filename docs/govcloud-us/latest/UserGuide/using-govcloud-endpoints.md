# Service Endpoints

If you access AWS GovCloud (US-West) or AWS GovCloud (US-East) by using the command line interface (CLI) or programmatically by using the APIs, you need the AWS GovCloud (US-West) or AWS GovCloud (US-East) Region endpoints. These HTTPS endpoints are referred to as the control plane used to configure AWS services.

If you require FIPS 140-3 compliance you should use the FIPS Endpoints linked in the following section. For more information about FIPS 140-3, see "Cryptographic Module Validation Program" on the NIST Computer Security Resource Center website.

If you require the use of FIPS 140-3 validated modules for TLS termination performed on the data plane of the Application Load Balancer HTTPS Listeners, have your account team reach out to the Elastic Load Balancing team.

FIPS-140-3 validated modules in the data plane of Amazon Relational Database Service (Amazon RDS) SSL can be configured for certain database engines. For more information about RDS SSL, see the [Amazon RDS User Guide](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md").

**FIPS Endpoints for the AWS GovCloud (US) Regions**

For a list of all GovCloud AWS FIPS endpoints, see _AWS GovCloud (US)_ in [FIPS Endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service").

**Endpoints for AWS Services**

For a list of AWS endpoints, see [View the service endpoints](../../../general/latest/gr/rande.md#view-service-endpoints "../../../general/latest/gr/rande.md#view-service-endpoints") in the _AWS General Reference_ .

**Regions for AWS Services**

For a list of AWS Regions, see [Regional endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in the _AWS General Reference_ .

For information about giving federated users single sign-on access to the AWS Management Console, see [Giving Federated Users Direct Access to the AWS Management Console](../../../STS/latest/UsingSTS/STSMgmtConsole.md "../../../STS/latest/UsingSTS/STSMgmtConsole.md").
