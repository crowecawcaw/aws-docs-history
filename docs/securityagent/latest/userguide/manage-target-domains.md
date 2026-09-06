

# Managed target domains used for penetration testing
<a name="manage-target-domains"></a>

In the AWS Management Console, you can add and manage target domains consumed by Agent Spaces for penetration testing. You must verify these target domains before you can use them in a penetration test. For more information about verifying target domains, see [Enable penetration test](enable-penetration-test.md) 

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:

1. Enabled penetration test (see [Enable penetration test](enable-penetration-test.md))

## Manage target domain resources
<a name="_manage_target_domain_resources"></a>
+ Navigate to the Target Domains overview page.
+ You should see all target domain resources associated with your account
  + If you don’t see any target domains associated with your account, follow the steps in [Enable penetration test](enable-penetration-test.md) to create and verify a target domain
+ Target domains can be reused between Agent Spaces and share verification status
  + To add an existing target domain to an Agent Space, navigate to the **Penetration test** tab of the Agent Space. Select **Add domain** and choose the desired domain under **Select from available previously registered domains** in the domain name field
  + Target domains must be associated with an Agent Space before they can be used in a penetration test
+ Removing a domain from an Agent Space does not delete the domain. The associated target domain can be permanently deleted from the Target Domains overview page

## Verify target domains
<a name="_verify_target_domains"></a>

In order for a target domain to be used in a penetration test, it must first be verified using one of the below methods:
+  **Route 53 domains (same AWS account)**: Choose **One-click verification**. AWS Security Agent automatically creates the DNS record and completes verification.
+  **DNS TXT (other DNS providers)**: Copy the verification token, add the TXT record with your DNS registrar, then select the domain and choose **Verify**.
+  **HTTP route**: Place the verification token at the required route path on your web server, then select the domain and choose **Verify**. For details, see [Enable an application domain for penetration testing](enable-test-domain.md).
+  **Private VPC**: Verifies the target domain’s IP falls within a private CIDR range (see [Connect agent to private VPC resources](connect-agent-vpc.md) for a list of private CIDR ranges). The penetration test target endpoint domain name must match the full domain name configured for verification. Only usable for private VPC penetration testing

**Note**  
For DNS TXT, HTTP route, and Route 53 verification, sub-domains of a verified domain are automatically covered and do not require separate verification. For Private VPC verification, each domain must be verified individually.