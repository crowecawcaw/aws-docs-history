

# SEC02-BP01 Identify principals and identity use-cases

 Every workload authenticates people, services, and devices, each with different risks and access needs. Before you choose authentication methods or providers, identify who and what interacts with your workload and what each interaction requires. This inventory shapes an identity design that scales as users and services grow. 

 **Desired outcome:** 
+  You have an inventory of every principal type that interacts with your workload, including workforce users, external users, federated users, service accounts, devices, and automated agents. 
+  You have mapped the identity use cases for each principal, covering registration, authentication, authorization, session management, and recovery. 
+  Your identity design accounts for tenancy, single sign-on, and cross-application session needs before implementation begins. 
+  Your chosen identity providers and authentication methods match the functional and non-functional requirements of each use case. 
+  Your identity architecture can absorb growth in users, services, and workload complexity without a redesign. 

 **Common anti-patterns:** 
+  Teams treat human users, service accounts, and system processes the same way, applying access controls that fit none of them well. 
+  Teams rely on single-factor authentication for sensitive operations instead of matching authentication strength to risk. 
+  Organizations skip identity lifecycle processes for onboarding, offboarding, and access review, which leaves orphaned accounts and stale permissions. 
+  Teams apply one identity approach to every use case rather than tailoring it to different audiences and risk levels. 
+  Teams design identity systems that couple tightly to a single provider, which makes later change expensive. 
+  Teams defer identity decisions until late in development, which forces rework when authentication and tenancy requirements surface. 

 **Benefits of establishing this best practice:** 
+  A complete principal inventory helps you avoid access control issues that appear when identity types are handled inconsistently. 
+  Matching authentication strength to each use case reduces exposure on sensitive operations without adding friction to routine ones. 
+  Early identity planning reduces costly rework during development and integration. 
+  A provider-agnostic design lets you adopt new services or change providers without rebuilding authentication. 
+  A design sized for growth supports more users, tenants, and services without a re-architecture. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A principal is any entity that can be authenticated (for example, a person, a service, a device, or an automated process). Workloads rarely serve only one kind of principal. A single application might authenticate employees through a corporate directory, customers through social sign-in, partner systems through machine credentials, and background jobs through service roles. Each authenticated principal has a different trust model, lifecycle, and tolerance for authentication friction. Grouping them under one scheme produces controls that are too weak for sensitive access and too heavy for routine access. 

 An identity use case describes what a principal needs to do and under what conditions. Self-registration implies account recovery and profile management. Multi-tenancy implies tenant identification and isolation in profiles and sessions. Service-to-service calls imply short-lived credentials and scoped authorization. Naming these use cases early identifies which identity provider capabilities you need and where standard protocols apply, such as OpenID Connect, OAuth 2.0, and SAML 2.0. 

 Customer identity and workforce identity have different design priorities. Customer-facing identity favors scale, self-service, and social or passwordless sign-in. Workforce identity favors central governance, federation with an existing directory, and consistent lifecycle control. Serving both from one directory usually undermines one of them. Decide the boundary between customer and workforce identity up front, because reversing it later means migrating live accounts and sessions. 

 Tight coupling to one identity provider makes it difficult to add new use cases. If you ignore non-functional requirements such as peak sign-in rates, data residency, and latency, you might only meet those requirements by accident if at all. Gaps in session management, token lifetimes, and audit trails cost more to close once traffic is live. Address these during design. 

 [Amazon Cognito](https://aws.amazon.com/cognito/) provides a managed user directory for customer-facing applications and can federate to external providers. [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) centralizes workforce access across accounts. [Amazon Verified Access](https://aws.amazon.com/verified-access/) fronts internal applications with your existing corporate identity provider. For multi-tenant products, [SaaS tenant isolation strategies](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html) describe how to carry tenant identity through profiles and sessions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory principal types:** List every entity that authenticates to your workload, such as internal workforce users, third-party and temporary workers, external customers, federated users, service accounts for microservices, devices, and bots. Record the role each principal plays and the sensitivity of the actions it performs. 

1.  **Classify identity use cases by application type:** Determine whether your workload is internal-only, external, a software as a service (SaaS) product, or a combination, then choose identity services that meet each use case. For internal applications, [Amazon Verified Access](https://aws.amazon.com/verified-access/) integrated with [your corporate identity provider](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-verified-access-integration-with-3rd-party-identity-providers/) fits well. For public customer-facing applications, [customer identity and access management](https://aws.amazon.com/identity/customer-identities/) with [Amazon Cognito](https://aws.amazon.com/cognito/) provides a scalable managed directory. 

1.  **Define tenancy and isolation attributes:** For multi-tenant workloads, define [tenant identification and isolation](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html) attributes and decide how they appear in user profiles and sessions. This makes tenant boundaries explicit in every authenticated request. 

1.  **Map identity scenarios and protocols:** Document the flows for each principal, including account creation, authentication factors, credential storage and recovery, profile management, and authorization to different areas of the workload. Record the protocols you will use, and prefer standard secure protocols such as OpenID Connect, OAuth 2.0, and SAML 2.0 to reduce the learning curve and reuse proven patterns. 

1.  **Define session management:** Specify how sessions, tokens, and temporary credentials are created, renewed, and ended for each principal type, including browser sessions and machine tokens. Consistent session rules prevent session fixation and indefinite-session vulnerabilities. 

1.  **Capture non-functional requirements:** Record scale, expected peaks, data residency, and response-time targets, because these constraints influence which identity services you can use. Size the design for growth rather than current volume alone. 

1.  **Perform a feature-gap analysis:** Map your identified use cases and requirements against the features of the identity services already used in your organization. Identify gaps and create a plan to close them through additional services or custom development. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 

 **Related documents:** 
+  [AWS Identity services](https://aws.amazon.com/identity/) 
+  [Customer identity and access management (CIAM)](https://aws.amazon.com/identity/customer-identities/) 
+  [Identity and access management resources in the Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/iam-resources.html) 

 **Related videos:** 
+  [AWS re:Inforce 2024 - Managing customer identities with Amazon Cognito (IAM221)](https://www.youtube.com/watch?v=ygZ1BTMW73U) 

 **Related services:** 
+  [Amazon Cognito](https://aws.amazon.com/cognito/) 
+  [Amazon Verified Access](https://aws.amazon.com/verified-access/) 
+  [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 