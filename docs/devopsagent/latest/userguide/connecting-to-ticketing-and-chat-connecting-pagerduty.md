# Connecting PagerDuty

PagerDuty integration enables AWS DevOps Agent to access and update incident data, on-call schedules, and service information from your PagerDuty account during incident investigations and automated response. This integration uses OAuth 2.0 for secure authentication.

###### Important

AWS DevOps Agent only supports the newer PagerDuty OAuth 2.0 (Scoped OAuth). Legacy PagerDuty OAuth with redirect uri is not supported.

## PagerDuty requirements

Before connecting PagerDuty, ensure you have:

- A PagerDuty account with your OAuth client ID and client secret
- Your PagerDuty account subdomain (for example, if your PagerDuty URL is `https://your-company.pagerduty.com`, the subdomain is `your-company`)

## Registering PagerDuty

PagerDuty is registered at the AWS account level and shared among all Agent Spaces in that account. Each registration corresponds to one PagerDuty account, identified by its region and subdomain. To register additional PagerDuty accounts, repeat this process for each one.

### Step 1: Configure access in PagerDuty

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console
3. Go to the **Capability Providers** page (accessible from the side navigation)
4. Find **PagerDuty** in the **Available** providers section under **Communication** and choose **Register**
5. Follow the guided setup on the **Configure access in PagerDuty** page:

**Check your service region and subdomain:**

- **Account scope** – Select your PagerDuty region (**US** or **EU**) and enter your PagerDuty subdomain. For example, if your PagerDuty URL is `https://your-company.pagerduty.com`, enter `your-company`.

**Create a new app in PagerDuty:**

- In a separate browser tab, log in to PagerDuty and navigate to **Integrations > App Registration**
- Create a new app using **OAuth 2.0 Scoped OAuth**
- Under **Permissions**, grant the following minimum required scopes: `incidents.read`, `incidents.write`, `services.read`, `webhook_subscriptions.read`, and `webhook_subscriptions.write`
- Enable **Events Integration** to allow bi-directional communication between AWS DevOps Agent and PagerDuty

**Configure OAuth credentials:**

- **Permission scope** – The minimum required scopes are: `incidents.read`, `incidents.write`, `services.read`, `webhook_subscriptions.read`, `webhook_subscriptions.write`
- **Client name** – Enter a descriptive name for your OAuth client
- **Client ID** – Enter the OAuth client ID from your PagerDuty app registration
- **Client secret** – Enter the OAuth client secret from your PagerDuty app registration

### Step 2: Review and submit PagerDuty registration

1. Review all the PagerDuty configuration details
2. Choose **Submit** to complete the registration
3. Upon successful registration, PagerDuty appears in the **Currently registered** section of the Capability Providers page

## Adding PagerDuty to an Agent Space

After registering PagerDuty at the account level, you can connect it to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Communications** section, choose **Add**
4. Choose the **PagerDuty** registration you want to connect to this Agent Space.
5. Choose **Save**

A single Agent Space can use more than one PagerDuty registration. To connect another registration, repeat these steps.

## Managing PagerDuty connections

- **Updating credentials** – If your OAuth credentials need to be updated, deregister PagerDuty from the Capability Providers page and re-register with the new credentials.
- **Viewing connections** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected communication integrations.
- **Removing PagerDuty** – To disconnect PagerDuty from an Agent Space, select it in the Communications section and choose **Remove**. To completely remove the registration, remove it from all Agent Spaces first, then deregister from the Capability Providers page.

## Webhook support

AWS DevOps Agent only supports PagerDuty V3 webhooks. Earlier webhook versions are not supported.

For more information about PagerDuty V3 webhook subscriptions, see [Webhooks Overview](https://developer.pagerduty.com/docs/webhooks-overview#webhook-subscriptions "https://developer.pagerduty.com/docs/webhooks-overview#webhook-subscriptions") in the PagerDuty developer documentation.
