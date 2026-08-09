# Troubleshooting

Find solutions to commonly seen errors when using AWS Security Agent.

## Access Denied: Incorrect GitHub account type selected or incorrect organization name specified

- You installed the AWS Security Agent application into your desired GitHub organization but incorrectly set the `GitHub Account Type` to `User` instead of `Organization`
- You installed the AWS Security Agent application into your desired GitHub organization and correctly set the `GitHub Account Type` to `Organization` but left the `Organization Name` field blank or entered an incorrect organization name that does not match the organization you installed the application into

**Solution:**

1. Go to GitHub and uninstall the app from the organization. For more information, see [Step 1: Uninstall the AWS Security Agent GitHub App from GitHub](remove-github.md#remove-github-step-1 "remove-github.md#remove-github-step-1").
2. Go back to the integrations page and restart the integration process by clicking on `Add Integrations`, install and authorize the app into your desired GitHub organization once again.
3. Select `Organization` from the dropdown of `GitHub account type`
4. Make sure the `Organization Name` you input is the EXACT same as the one you installed the application into.
5. Choose **Connect** to create your GitHub organization integration.

## Access Denied: Insufficient permissions to install GitHub App into organization

When you attempt to install the AWS Security Agent application into your desired GitHub organization, you will see two different messages on the button in the installation page.

- An organization `Member` will see `Authorize & Request`
- An organization `Owner` will see `Install & Authorize`

You can verify whether you are a `Member` or an `Owner` of the GitHub organization by following the below steps.

1. Go to [github.com](https://github.com "https://github.com")
2. Choose your profile on the website
3. Navigate to `Organizations` on the dropdown menu and choose it
4. Find the organization you wish to install AWS Security Agent into from the list of organizations, it will specify whether you are a `Member` or an `Owner` next to the organization name.

Possible solutions:

- Have an owner approve your installation request BEFORE you try to create the integration
- Have an owner update your role in the GitHub organization from a `Member` to an `Owner` and restart the integration process again

## Agent cannot connect to endpoint during a penetration test

If the penetration test agent is unable to make calls to the configured target URL or fails to successfully navigate the target endpoint:

- If your endpoint makes calls to domains outside the configured target URL, verify the additional domains are added as **Accessible URLs** in your penetration test configuration
- Penetration testing is currently only available for HTTP/HTTPS endpoints serving traffic on ports 80 or 443
- If you have a WAF configured, check that you WAF is not blocking penetration test traffic. You can allowlist penetration test traffic by `User-Agent` header, which will be set to `securityagent` by default

## Endpoint validation failed during a penetration test

A penetration test failing during endpoint validation indicates that your endpoint is not accessible from the penetration testing environment. The steps for debugging this issue will depend on if you have configured a VPC for your penetration test:

- For a non-VPC penetration test:

  - Ensure the target endpoint has a public DNS record that resolves to a publicly accessible IP address
  - Verify that your target endpoint can be reached without special networking requirements. Some common blockers are a specific VPN required to reach the endpoint or a WAF that blocks public internet traffic
  - Attempt to reach the target endpoint using `curl` or a browser and verify you receive a valid response

- For a VPC penetration test:

  - Ensure the selected VPC/subnet has proper routing to the target endpoint (e.g., via VPN tunnel or VPC peering), DNS resolution is correctly configured for the private domain (e.g., Route 53 Resolver or custom DNS), and security group rules allow outbound traffic to the target
  - To debug further, launch an EC2 instance in your account with the same VPC, subnet, and security group as your penetration test. Connect to the EC2 instance and verify that networking requests to your target endpoint succeed

## Getting additional help

If you continue to experience issues after trying these troubleshooting steps:

- Check the AWS Security Agent service status page
- Contact AWS Support for assistance with complex configuration issues
