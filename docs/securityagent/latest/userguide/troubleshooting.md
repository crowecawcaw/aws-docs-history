# Troubleshooting

Find solutions to commonly seen errors when using AWS Security Agent for code reviews.

## Access Denied: Incorrect GitHub account type selected or incorrect organization name specified

- You installed the AWS Security Agent application into your desired GitHub organization but incorrectly set the `GitHub Account Type` to `User` instead of `Organization`
- You installed the AWS Security Agent application into your desired GitHub organization and correctly set the `GitHub Account Type` to `Organization` but left the `Organization Name` field blank or entered an incorrect organization name that does not match the organization you installed the application into

**Solution:**

1. Go to GitHub and uninstall the app from the organization. For more information, see [Step 1: Uninstall the AWS Security Agent GitHub App from GitHub](remove-github.md#remove-github-step-1 "remove-github.md#remove-github-step-1").
2. Go back to the integrations page and restart the integration process by clicking on `Add Integrations`, install and authorize the app into your desired GitHub organization once again.
3. Select `Organization` from the dropdown of `GitHub account type`
4. Make sure the `Organization Name` you input is the EXACT same as the one you installed the application into.
5. Click the Connect button to create your GitHub organization integration.

## Access Denied: Insufficient permissions to install GitHub App into organization

When you attempt to install the AWS Security Agent application into your desired GitHub organization, you will see two different messages on the button in the installation page.

- An organization `Member` will see `Authorize & Request`
- An organization `Owner` will see `Install & Authorize`

You can verify whether you are a `Member` or an `Owner` of the GitHub organization by following the below steps.

1. Go to [github.com](https://github.com "https://github.com")
2. Click on your profile in the top right of the website
3. Navigate to `Organizations` on the dropdown menu and click it
4. Find the organization you wish to install AWS Security Agent into from the list of organizations, it will specify whether you are a `Member` or an `Owner` next to the organization name.

Possible solutions:

- Have an owner approve your installation request BEFORE you try to create the integration
- Have an owner update your role in the GitHub organization from a `Member` to an `Owner` and restart the integration process again

## Getting additional help

If you continue to experience issues after trying these troubleshooting steps:

- Check the AWS Security Agent service status page
- Contact AWS Support for assistance with complex configuration issues
