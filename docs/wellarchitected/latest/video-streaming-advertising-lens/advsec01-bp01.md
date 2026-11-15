

# ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content
<a name="advsec01-bp01"></a>

 Programmatic advertising platforms process authentication decisions for bid requests, creative uploads, and reporting interfaces. These decisions occur at high volume and within strict bid-response deadlines. Without authentication patterns designed for real-time bidding, unauthorized parties might access bid streams, campaign data, or audience segments. 

 **Desired outcome:** 
+  You have authentication controls that verify every supply-side platform (SSP) and demand-side platform (DSP) participant with industry-standard protocols before it submits or receives bid requests. 
+  You have an authentication system that handles peak request volume within the allocated bid-response latency budget. 
+  You have federated identity integration that provides single sign-on (SSO) for publishers and advertisers and maintains isolation between organizations. 

 **Common anti-patterns:** 
+  Using one shared API key for all programmatic partners instead of issuing unique credentials for each SSP or DSP relationship. 
+  Relying only on an IP address allowlist for partner authentication without cryptographically verifying the request origin. 
+  Applying the same authentication flow to human users and machine-to-machine traffic without accounting for latency constraints. 

 **Benefits of establishing this best practice:** 
+  Authentication controls reduce the risk of unauthorized access to bid streams that might lead to audience data theft or campaign manipulation. 
+  Partner-specific audit trails support compliance and dispute resolution for programmatic transactions. 
+  Isolated partner credentials limit how far a credential compromise can spread across the supply chain. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising platforms authenticate both human and machine traffic. Human users, including campaign managers, traffickers, and analysts, need interactive identity flows. Machine traffic, including bid requests, creative synchronization, and reporting APIs, must complete authentication within a defined portion of each exchange request's timeout. One shared pattern can increase programmatic latency or weaken administrative access. 

 For machine traffic, you choose between connection-level and request-level verification. Mutual TLS (mTLS) authenticates a connection when it starts and spreads that cost across later requests. This pattern suits persistent SSP-to-DSP connections with stable, high-volume traffic. Certificate rotation requires coordinated rollover windows. A failed rotation during a peak auction can stop all bid traffic for one partner. 

 OAuth 2.0 client credentials use short-lived tokens and support more granular revocation. Revocation isn't immediate for self-contained tokens. A token remains valid until it expires, and [Amazon Cognito](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TokenValidityUnitsType.html) doesn't issue access tokens with lifetimes shorter than five minutes. Faster cutoff requires live introspection at the resource server or a denylist at the enforcement point. Live introspection adds a network request to the request path. 

 Each exchange supplies its own timeout, often tens to low hundreds of milliseconds. The shortest partner timeout defines the upper bound for authentication. Authentication needs a separate sub-budget within that bound, measured independently from the full auction deadline. You then need to reuse long-lived connections. [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html) doesn't support TLS session resumption in either mutual TLS mode. Each new connection therefore incurs a full handshake without ticket-based resumption. mTLS requires client signature generation, server chain verification, and larger handshake messages. High connection churn can push 99th percentile (p99) authentication latency past the deadline during traffic spikes. These bid losses appear as lower revenue and produce no error alerts, so they are easy to miss. 

 Credential lifecycle work spans security, partnerships, and engineering. The organization needs clear ownership for partner offboarding, active sessions, and revocation propagation. Shared runbooks and service-level agreements (SLAs) record these decisions and their escalation paths. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish federated identity for human users:** Configure [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) for each organization type (publisher, advertiser, and agency). Integrate customer identity providers through [Security Assertion Markup Language 2.0 (SAML 2.0)](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html) or [OpenID Connect (OIDC)](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html) for SSO. Define attribute-based access control (ABAC) with custom claims that represent advertising roles. 

1.  **Implement mTLS for programmatic partner connections:** Issue X.509 certificates to each SSP or DSP partner. Configure [mutual TLS authentication for Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html) or [mutual TLS authentication for Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) on bid endpoints. Rotate certificates on a defined schedule, and maintain a certificate revocation list for offboarded partners. 

1.  **Define the certificate revocation runbook:** Document who executes revocation when you offboard a partner or suspect key compromise. Define the required propagation time. Revoke the certificate at the issuing certificate authority (CA), publish the updated revocation state to every enforcement point, and terminate the partner's established connections. 

1.  **Test certificate revocation:** Rehearse the runbook with a test partner certificate at least annually. Record the elapsed time from the revocation decision to enforced denial, and compare it with the required propagation time. 

1.  **Match revocation enforcement to each entry point:** An [Application Load Balancer trust store](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html) accepts a certificate revocation list and performs revocation checks in verify mode. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) doesn't verify a certificate's revocation status and replaces its truststore as a complete bundle. Removing a CA therefore revokes every partner whose certificate chains to that CA. To revoke individual partners behind API Gateway, use a dedicated CA for each partner or an [API Gateway Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) that checks a revocation list or denylist on each request. 

1.  **Configure short-lived token authentication for API access:** Use [Amazon Cognito machine-to-machine authorization](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html) with the client credentials grant for service-to-service calls that don't require persistent connections. Set token expiration to match the session requirements for bid operations and reporting APIs. 

1.  **Define IAM policies scoped to advertising functions:** Create [AWS Identity and Access Management (IAM) roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for distinct operational functions, such as bid processing, creative management, audience data, and reporting. Apply [permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) that set the maximum permissions for each function. Use [IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) to check policy syntax and AWS security best practices. Combine these results with [service last-accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html), policy tests, and owner review. Use [CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) or other configured event records as activity evidence. 

1.  **Implement authentication monitoring and anomaly detection:** Configure [Amazon Cognito events in AWS CloudTrail](https://docs.aws.amazon.com/cognito/latest/developerguide/understanding-amazon-cognito-entries.html) to record supported authentication and administrative API activity. Enable [Application Load Balancer connection logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-connection-logs.html) for mutual TLS outcomes. These logs, rather than CloudTrail, record client-certificate authentication results. Configure [Amazon API Gateway access logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html) for bid endpoints that terminate in API Gateway. Publish metrics for failed authentication spikes, unusual geographic access, and human sign-in attempts outside approved hours, and create [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) for those metrics. 

1.  **Enforce multi-factor authentication for privileged operations:** Require multi-factor authentication (MFA) for all human users who access campaign management, audience data, or financial reporting. [Amazon Cognito adaptive authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html) evaluates risk during supported sign-in flows, not for each business operation. To require step-up authentication for a budget change or an audience export, start a new authentication challenge for that operation. Before allowing it, verify the new token's [auth\_time claim](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.html) and the application's record that the required factor completed. For system administrators, use [FIDO2 security keys that support Web Authentication (WebAuthn)](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP04 Implement least privilege access to protect programmatic workloads](advsec01-bp04.md) 

 **Related documents:** 
+  [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) 
+  [SAML identity providers for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-saml-idp.html) 
+  [OIDC identity providers for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html) 
+  [Mutual TLS authentication for Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html) 
+  [IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) 