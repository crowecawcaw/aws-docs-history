

# Service Endpoints
<a name="using-govcloud-endpoints"></a>

If you access AWS GovCloud (US-West) or AWS GovCloud (US-East) by using the command line interface (CLI) or programmatically by using the APIs, you need the AWS GovCloud (US-West) or AWS GovCloud (US-East) Region endpoints. These HTTPS endpoints are referred to as the control plane used to configure AWS services.

If you require FIPS 140-3 compliance you should use the FIPS Endpoints linked in the following section. For more information about FIPS 140-3, see "Cryptographic Module Validation Program" on the NIST Computer Security Resource Center website.

If you require the use of FIPS 140-3 validated modules for TLS termination performed on the data plane of the Application Load Balancer HTTPS Listeners, have your account team reach out to the Elastic Load Balancing team.

FIPS-140-3 validated modules in the data plane of Amazon Relational Database Service (Amazon RDS) SSL can be configured for certain database engines. For more information about RDS SSL, see the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html).

 **FIPS Endpoints for the AWS GovCloud (US) Regions** 

For a list of all GovCloud AWS FIPS endpoints, see * AWS GovCloud (US) * in [FIPS Endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service).

 **Endpoints for AWS Services** 

For a list of AWS endpoints, see [View the service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#view-service-endpoints) in the * AWS General Reference *.

 **Regions for AWS Services** 

For a list of AWS Regions, see [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) in the * AWS General Reference *.

For information about giving federated users single sign-on access to the AWS Management Console, see [Giving Federated Users Direct Access to the AWS Management Console](https://docs.aws.amazon.com/STS/latest/UsingSTS/STSMgmtConsole.html).