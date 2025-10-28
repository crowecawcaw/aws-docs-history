# SEC09-BP03 Authenticate network communications

Verify the identity of communications by using protocols that
support authentication, such as Transport Layer Security (TLS) or
IPsec.

Design your workload to use secure, authenticated network protocols whenever communicating between services, applications, or to users. Using network protocols that support authentication and authorization provides stronger control over network flows and reduces the impact of unauthorized access.

**Desired outcome:** A workload with well-defined data plane and control plane traffic flows between services. The traffic flows use authenticated and encrypted network protocols where technically feasible.

**Common anti-patterns:**

- Unencrypted or unauthenticated traffic flows within your workload.
- Reusing authentication credentials across multiple users or entities.
- Relying solely on network controls as an access control mechanism.
- Creating a custom authentication mechanism rather than relying on industry-standard authentication mechanisms.
- Overly permissive traffic flows between service components or other resources in the VPC.

**Benefits of establishing this best practice:**

- Limits the scope of impact for unauthorized access to one part of the workload.
- Provides a higher level of assurance that actions are only performed by authenticated entities.
- Improves decoupling of services by clearly defining and enforcing intended data transfer interfaces.
- Enhances monitoring, logging, and incident response through request attribution and well-defined communication interfaces.
- Provides defense-in-depth for your workloads by combining network controls with authentication and authorization controls.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Your workload’s network traffic patterns can be characterized into two categories:

- _East-west traffic_ represents traffic flows between services that make up a workload.
- _North-south traffic_ represents traffic flows between your workload and consumers.

While it is common practice to encrypt north-south traffic, securing east-west traffic using authenticated protocols is less common. Modern security practices recommend that network design alone does not grant a trusted relationship between two entities. When two services may reside within a common network boundary, it is still best practice to encrypt, authenticate, and authorize communications between those services.

As an example, AWS service APIs use the [AWS Signature Version 4 (SigV4)](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") signature protocol to authenticate the caller, no matter what network the request originates from. This authentication ensures that AWS APIs can verify the identity that requested the action, and that identity can then be combined with policies to make an authorization decision to determine whether the action should be allowed or not.

Services such as [Amazon VPC Lattice](../../../vpc-lattice/latest/ug/access-management-overview.md "../../../vpc-lattice/latest/ug/access-management-overview.md") and [Amazon API Gateway](../../../apigateway/latest/developerguide/permissions.md "../../../apigateway/latest/developerguide/permissions.md") allow you use the same SigV4 signature protocol to add authentication and authorization to east-west traffic in your own workloads. If resources outside of your AWS environment need to communicate with services that require SigV4-based authentication and authorization, you can use [AWS Identity and Access Management (IAM) Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") on the non-AWS resource to acquire temporary AWS credentials. These credentials can be used to sign requests to services using SigV4 to authorize access.

Another common mechanism for authenticating east-west traffic is
TLS mutual authentication (mTLS). Many Internet of Things (IoT),
business-to-business applications, and microservices use mTLS to
validate the identity of both sides of a TLS communication through
the use of both client and server-side X.509 certificates. These
certificates can be issued by AWS Private Certificate Authority
(AWS Private CA). You can use services such as
[Amazon API Gateway](../../../apigateway/latest/developerguide/rest-api-mutual-tls.md "../../../apigateway/latest/developerguide/rest-api-mutual-tls.md") to provide mTLS authentication for inter- or
intra-workload communication.
[Application Load Balancer also supports mTLS](../../../elasticloadbalancing/latest/application/mutual-authentication.md "../../../elasticloadbalancing/latest/application/mutual-authentication.md") for internal or external
facing workloads. While mTLS provides authentication information
for both sides of a TLS communication, it does not provide a
mechanism for authorization.

Finally, OAuth 2.0 and OpenID Connect (OIDC) are two protocols typically used for controlling access to services by users, but are now becoming popular for service-to-service traffic as well. API Gateway provides a [JSON Web Token (JWT) authorizer](../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md "../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md"), allowing workloads to restrict access to API routes using JWTs issued from OIDC or OAuth 2.0 identity providers. OAuth2 scopes can be used as a source for basic authorization decisions, but the authorization checks still need to be implemented in the application layer, and OAuth2 scopes alone cannot support more complex authorization needs.

### Implementation steps

- **Define and document your workload network flows:** The first step in implementing a defense-in-depth strategy is defining your workload’s traffic flows.
  - Create a data flow diagram that clearly defines how data is transmitted between different services that comprise your workload. This diagram is the first step to enforcing those flows through authenticated network channels.
  - Instrument your workload in development and testing phases to validate that the data flow diagram accurately reflects the workload’s behavior at runtime.
  - A data flow diagram can also be useful when performing a threat modeling exercise, as described in [SEC01-BP07 Identify threats and prioritize mitigations using a threat model](sec_securely_operate_threat_model.md "sec_securely_operate_threat_model.md").

- **Establish network controls:** Consider AWS capabilities to establish network controls aligned to your data flows. While network boundaries should not be the only security control, they provide a layer in the defense-in-depth strategy to protect your workload.
  - Use [security groups](../../../vpc/latest/userguide/security-groups.md "../../../vpc/latest/userguide/security-groups.md") to establish define and restrict data flows between resources.
  - Consider using [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") to communicate with both AWS and third-party services that support AWS PrivateLink. Data sent through a AWS PrivateLink interface endpoint stays within the AWS network backbone and does not traverse the public Internet.

- **Implement authentication and authorization across services in your workload:** Choose the set of AWS services most appropriate to provide authenticated, encrypted traffic flows in your workload.
  - Consider [Amazon VPC Lattice](../../../vpc-lattice/latest/ug/what-is-vpc-lattice.md "../../../vpc-lattice/latest/ug/what-is-vpc-lattice.md") to secure service-to-service communication. VPC Lattice can use [SigV4 authentication combined with auth policies](../../../vpc-lattice/latest/ug/auth-policies.md "../../../vpc-lattice/latest/ug/auth-policies.md") to control service-to-service access.
  - For service-to-service communication using mTLS,
    consider
    [API Gateway](../../../apigateway/latest/developerguide/rest-api-mutual-tls.md "../../../apigateway/latest/developerguide/rest-api-mutual-tls.md"),
    [Application Load Balancer](../../../elasticloadbalancing/latest/application/mutual-authentication.md "../../../elasticloadbalancing/latest/application/mutual-authentication.md").
    [AWS Private CA](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md") can be used to establish a private CA
    hierarchy capable of issuing certificates for use with
    mTLS.
  - When integrating with services using OAuth 2.0 or OIDC, consider [API Gateway using the JWT authorizer](../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md "../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md").
  - For communication between your workload and IoT devices, consider [AWS IoT Core](../../../iot/latest/developerguide/client-authentication.md "../../../iot/latest/developerguide/client-authentication.md"), which provides several options for network traffic encryption and authentication.

- **Monitor for unauthorized access:** Continually monitor for unintended communication channels, unauthorized principals attempting to access protected resources, and other improper access patterns.
  - If using VPC Lattice to manage access to your services, consider enabling and monitoring [VPC Lattice access logs](../../../vpc-lattice/latest/ug/monitoring-access-logs.md "../../../vpc-lattice/latest/ug/monitoring-access-logs.md"). These access logs include information on the requesting entity, network information including source and destination VPC, and request metadata.
  - Consider enabling [VPC flow logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") to capture metadata on network flows and periodically review for anomalies.
  - Refer to the [AWS Security Incident Response Guide](../../../whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.md "../../../whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.md") and the [Incident Response section](incident-response.md "incident-response.md") of the AWS Well-Architected Framework security pillar for more guidance on planning, simulating, and responding to security incidents.

## Resources

**Related best practices:**

- [SEC03-BP07 Analyze public and cross-account access](sec_permissions_analyze_cross_account.md "sec_permissions_analyze_cross_account.md")
- [SEC02-BP02 Use temporary credentials](sec_identities_unique.md "sec_identities_unique.md")
- [SEC01-BP07 Identify threats and prioritize mitigations using a threat model](sec_securely_operate_threat_model.md "sec_securely_operate_threat_model.md")

**Related documents:**

- [Evaluating access control methods to secure Amazon API Gateway APIs](https://aws.amazon.com/blogs/compute/evaluating-access-control-methods-to-secure-amazon-api-gateway-apis/ "https://aws.amazon.com/blogs/compute/evaluating-access-control-methods-to-secure-amazon-api-gateway-apis/")
- [Configuring mutual TLS authentication for a REST API](../../../apigateway/latest/developerguide/rest-api-mutual-tls.md "../../../apigateway/latest/developerguide/rest-api-mutual-tls.md")
- [How to secure API Gateway HTTP endpoints with JWT authorizer](https://aws.amazon.com/blogs/security/how-to-secure-api-gateway-http-endpoints-with-jwt-authorizer/ "https://aws.amazon.com/blogs/security/how-to-secure-api-gateway-http-endpoints-with-jwt-authorizer/")
- [Authorizing direct calls to AWS services using AWS IoT Core credential provider](../../../iot/latest/developerguide/authorizing-direct-aws.md "../../../iot/latest/developerguide/authorizing-direct-aws.md")
- [AWS Security Incident Response Guide](../../../whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.md "../../../whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.md")

**Related videos:**

- [AWS re:invent 2022: Introducing VPC Lattice](https://www.youtube.com/watch?v=fRjD1JI0H5w "https://www.youtube.com/watch?v=fRjD1JI0H5w")
- [AWS re:invent 2020: Serverless API authentication for HTTP APIs on AWS](https://www.youtube.com/watch?v=AW4kvUkUKZ0 "https://www.youtube.com/watch?v=AW4kvUkUKZ0")

**Related examples:**

- [Amazon VPC Lattice Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/9e543f60-e409-43d4-b37f-78ff3e1a07f5/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/9e543f60-e409-43d4-b37f-78ff3e1a07f5/en-US")
- [Zero-Trust Episode 1 – The Phantom Service Perimeter workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dc413216-deab-4371-9e4a-879a4f14233d/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/dc413216-deab-4371-9e4a-879a4f14233d/en-US")
