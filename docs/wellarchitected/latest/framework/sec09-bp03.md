

# SEC09-BP03 Authenticate network communications

 Authenticating network communications means each party verifies the other's identity before they exchange data, using protocols that support authentication. An attacker with unauthorized network access can move laterally and send requests that appear internal, so network location alone is insufficient evidence of identity. Apply it to internal service-to-service traffic as well as traffic from external users. 

 **Desired outcome:** 
+  You have documented traffic flows between the services that make up your workload. 
+  Your service-to-service communications use authenticated, encrypted protocols wherever technically feasible. 
+  Each of your services verifies the identity of the services it communicates with, rather than trusting network position. 
+  Your authentication decisions feed authorization and monitoring, so you can attribute requests to a verified identity. 

 **Common anti-patterns:** 
+  Traffic flows within the workload run unencrypted or unauthenticated. 
+  Teams reuse the same authentication credentials across multiple users or entities. 
+  Network controls serve as the only access control mechanism. 
+  Teams build a custom authentication mechanism instead of using industry-standard protocols. 
+  Traffic flows between service components are overly permissive. 

 **Benefits of establishing this best practice:** 
+  Unauthorized access to one component stays contained instead of spreading across the workload. 
+  Actions carry higher assurance, because only authenticated entities can perform them. 
+  Services decouple more cleanly, because communication interfaces are defined and enforced. 
+  Monitoring, logging, and incident response improve through request attribution to known identities. 
+  Network controls combined with authentication and authorization provide defense in depth. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 *North-south traffic* flows between your workload and its consumers, while *east-west traffic* flows between the services inside the workload. Encrypting and authenticating north-south traffic is common practice, but east-west traffic often goes unauthenticated because teams assume that a shared network boundary implies trust. Authenticate and authorize east-west communication even when both endpoints sit inside the same boundary. 

 Authentication and authorization are separate concerns. Authentication proves who is calling, and authorization decides what actions the caller can take. Some protocols verify identity but leave authorization to your application, so check which each mechanism covers and enforce the missing half yourself. 

 [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) signs API requests so the receiver can verify the caller's identity and detect tampering, regardless of the network path. AWS service APIs use SigV4, and you can apply it to your own east-west traffic with [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/access-management-overview.html) or [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html). For resources outside AWS, [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) issues temporary credentials for signing. SigV4 pairs identity with policies, so it covers both authentication and authorization. 

 In mutual TLS (mTLS), both sides of a connection present X.509 certificates so that client and server verify each other. Common uses include IoT fleets, business-to-business integrations, and microservices. Certificates can come from [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html), and services such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) and [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html) terminate mTLS for you. mTLS authenticates both parties but does not make authorization decisions, so enforce what each authenticated client may do in your application. 

 OAuth 2.0 and OpenID Connect (OIDC) issue tokens that a service presents to prove access, covering both user sign-in and service-to-service authorization. API Gateway can validate JSON Web Tokens (JWTs) from an [OIDC or OAuth 2.0 provider](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html) and restrict access to routes. OAuth 2.0 scopes support basic authorization, but complex decisions still belong in your application layer. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define and document your workload traffic flows:** Create a data flow diagram that shows how data moves between the services in your workload. Instrument the workload in development and test to confirm the diagram matches runtime behavior. The same diagram supports threat modeling. 

1.  **Establish network controls as one layer:** Use [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) to restrict which resources can exchange traffic. Where you communicate with AWS or third-party services that support it, use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) so traffic stays on the AWS network backbone and avoids the public internet. 

1.  **Implement authentication and authorization between services:** Select the mechanism that fits each flow. Use [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) with [auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) for SigV4-based service-to-service access, [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) or [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html) for mTLS, the [API Gateway JWT authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html) for OAuth 2.0 or OIDC, and [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/client-authentication.html) for device communication. 

1.  **Monitor for unauthorized access:** Enable [VPC Lattice access logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html) and [VPC flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to capture request and network metadata, then review them for unexpected flows or principals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC01-BP06 Identify threats and prioritize mitigations using a threat model](sec01-bp06.md) 

 **Related documents:** 
+  [Authorizing direct calls to AWS services using AWS IoT Core credential provider](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html) 
+  [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/) 
+  [Building zero trust access across multi-account AWS environments](https://aws.amazon.com/blogs/networking-and-content-delivery/building-zero-trust-access-across-multi-account-aws-environments/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Advanced VPC design and new capabilities (NET340)](https://www.youtube.com/watch?v=40QfxdvDGsw) 
+  [Authenticating clients with mutual TLS on Application Load Balancer (ALB)](https://www.youtube.com/watch?v=v8HXlRAHJUE) 
+  [AWS re:Inforce 2025 - Integrate Zero Trust into your cloud network (NIS304)](https://www.youtube.com/watch?v=AMSkou99Fus) 
+  [Zero Trust with AWS Application Networking](https://aws.amazon.com/video/watch/c224bdfd09a/) 

 **Related workshops:** 
+  [Amazon VPC Lattice Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/9e543f60-e409-43d4-b37f-78ff3e1a07f5/en-US) 