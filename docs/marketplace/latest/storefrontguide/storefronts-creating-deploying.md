# Creating and deploying storefronts

Create, clone, deploy, and link storefronts to publish your catalog to buyers.

## Creating a storefront

You can create a new storefront to curate and publish a catalog of AWS Marketplace
products for your buyers. Each storefront is a dedicated, branded web page where buyers
browse, evaluate, and procure products through AWS Marketplace.

### Prerequisites

- An active AWS Marketplace Storefront organization
- At least one connected AWS Marketplace seller account
- Owner or Admin role at the organization level, plus Storefront Admin on the target storefront.

### To create a storefront

1. In the navigation pane, choose **Accounts &
   Storefronts**.
2. Choose **Create storefront**.
3. Enter a **Name** for the storefront.
4. (Optional) Turn on **Use GenAI to build
   storefront** to generate initial content automatically.
5. Choose **Create**.

The storefront is created in draft state. You can now configure design,
products, tags, and deployment settings.

### Next steps

After creating a storefront, you typically:

- Configure the design and layout
- Import products to your storefront catalog
- Set up tags and filters for navigation
- Configure Buy With AWS for procurement
- Deploy the storefront

### Related topics

- [Cloning a storefront](#cloning-a-storefront "#cloning-a-storefront")
- Layout types

## Cloning a storefront

You can clone an existing storefront to create a copy with the same design settings,
product selections, and configuration. Cloning is useful when you need to create a
similar storefront for a different audience or region without starting from
scratch.

### Prerequisites

- An existing storefront in your organization
- Storefront Admin role on the source storefront.

### To clone a storefront

1. In the navigation pane, choose **Accounts &
   Storefronts**.
2. Locate the storefront you want to clone.
3. Choose the actions menu on the storefront card, then choose
   **Clone**.

The actions menu on a storefront card contains Edit, Clone, and Delete. 4. Enter a **Name** for the cloned
storefront. 5. Choose **Clone**.

The new storefront is created in draft state with all settings copied from
the source storefront. You can modify any settings before deploying.

### What is cloned

The following settings are copied to the new storefront:

- Layout type and design configuration
- Color theme and branding
- Product selections
- Tag structure and filters
- BWA (Buy With AWS) configuration
- Vendor settings

### What is not cloned

- Deployment status (clone starts in draft)
- Analytics data
- Order history
- Storefront SSO configuration (must be reconfigured). For setup, see [Setting up single sign-on for a storefront](sso-storefront.md "sso-storefront.md").

### Related topics

- [Creating a storefront](#creating-a-storefront "#creating-a-storefront")
- Storefront templates

## Deployment

After configuring your storefront's design, products, and settings, you deploy it to
make it accessible to buyers. Deployment publishes the storefront at its configured
URL.

### Storefront states

| State    | Description                                                     |
| -------- | --------------------------------------------------------------- |
| Draft    | Storefront is being configured. Not accessible to buyers.       |
| Deployed | Storefront is live and accessible at its URL.                   |
| Disabled | Storefront was previously deployed but is now taken<br>offline. |

### To deploy a storefront

1. Open the storefront and choose the **Checkout &
   Deployment** tab.
2. Turn on the **Deploy your storefront**
   toggle, then choose **Save**.
3. The storefront becomes accessible at
   `https://<name>.storefront.marketplace.aws.com`.

### Storefront URL

By default, your storefront is accessible at:

```
https://<name>.storefront.marketplace.aws.com
```

The subdomain is derived from the storefront name.

Use the **Update domain** field to change the
subdomain for your storefront URL.

The following controls are available for the storefront URL:

- **Open link** – Opens the storefront URL
  in a new browser tab.
- **Copy link** – Copies the storefront URL
  to your clipboard.
- **Share link** – Generates a shareable
  link for distribution to buyers or stakeholders.

### Buy with AWS toggles

On the **Checkout & Deployment** tab, the
**Buy with AWS** toggle enables Buy with AWS for the
storefront. The **Buy with AWS banner** toggle controls
whether the Buy with AWS banner is displayed. Both toggles default to enabled.

### To disable a storefront

1. Open the storefront and choose the **Checkout &
   Deployment** tab.
2. Turn off the **Deploy your storefront**
   toggle, then choose **Save**.
3. The storefront is taken offline. Buyers who visit the URL see an
   unavailable message.

You can re-deploy a disabled storefront at any time without losing
configuration.

### Updating a live storefront

Changes made to a deployed storefront (design, products, tags) take effect
immediately after saving. There is no separate re-deploy step. Buyers see updates
as soon as you save them.

### Related topics

- [Creating a storefront](#creating-a-storefront "#creating-a-storefront")
- [Linking and embedding](#linking-and-embedding "#linking-and-embedding")
- [Setting up single sign-on for a storefront](sso-storefront.md "sso-storefront.md")

## Linking and embedding

You can manage listing relations for your storefront on the Linking tab.

### Managing listing relations

On the **Linking** tab, choose **Add new link** to manage relations between listings. The **Listings linked to main** list shows the linked
listings.

### Related topics

- [Deployment](#deployment "#deployment")
- Layout types
