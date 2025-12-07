# Managing DNS views with Route 53 Global Resolver

You can manage ongoing Route 53 Global Resolver operations including updating DNS views to control which client device groups can resolve to internal resources and what domains to filter.

## Managing DNS views

After creating DNS views, you can update their configuration, enable or disable them, and
manage their lifecycle.

### Creating DNS views for client device groups

A DNS view is a logical grouping defines security policies for a group of client devices, such as remote workers, branch office devices, or on-premises equipment. Each view has its own authentication requirements, filtering rules, and private hosted zone associations.

**To create a DNS view**

1. Open the console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/ "https://console.aws.amazon.com/route53globalresolver/").
2. Choose your global resolver from the list.
3. Choose the **DNS views** tab.
4. Choose **Create DNS view**.
5. In the **DNS view details** section:
   1. For **DNS view name**, enter a descriptive name for your
      DNS view (up to 128 characters).
   2. (Optional) For **Description**, enter a description for
      your DNS view (up to 255 characters).

6. In the **DNS query handling** section, configure the
   following settings:
   - **DNSSEC validation** - Choose **Enable** or **Disable**. DNSSEC validation enables
     the Global Resolver to verify the authenticity of DNS responses.
   - **Firewall rules fail open behavior** - Choose **Enable** to allow queries to proceed when DNS Firewall cannot evaluate
     them, or **Disable** to block such queries.
   - **EDNS0 client subnet** - Choose **Enable** to improve client location accuracy for traffic routing to nearby
     resources and efficient caching, or **Disable** to turn off
     this feature.

7. Choose **Create DNS view**.

After creating the DNS view, you can configure access controls, firewall rules, and private
hosted zone associations.

### Editing DNS views

You can modify DNS view settings after creation, including DNS query handling options and
associated resources.

**To edit a DNS view**

1. In the console, navigate to your global resolver.
2. Choose the **DNS views** tab.
3. Select the DNS view you want to edit and choose **Edit**.
4. Modify the DNS view settings as needed and choose **Save
   changes**.

### Enabling and disabling DNS views

You can temporarily disable a DNS view without deleting it. When disabled, the global
resolver stops serving requests for client devices associated with that DNS view.

###### Warning

Disabling a DNS view immediately stops DNS resolution for all client devices associated
with that view. Ensure you have alternative DNS resolution configured for affected client
devices.

### Deleting DNS views

Before you can delete a DNS view, you must first delete all associated resources,
including Access Source rules, access tokens, firewall rules, and private hosted zone
associations.

###### Warning

Deleting a DNS view is irreversible and will immediately stop DNS resolution for all
client devices associated with that view.

## Managing private hosted zone associations

You can view, update, and remove private hosted zone associations as needed to control
which client device groups have access to internal resources.

### Viewing associations

To view all private hosted zone associations for a DNS view, navigate to your DNS view and
check the **Private hosted zones** section to see all associated
zones with their status and association details.

### Updating associations

You can update the name of a private hosted zone association by selecting the association,
choosing **Edit**, updating the association name, and saving
changes.

### Removing associations

When you remove a private hosted zone association, Route 53 Global Resolver stops using that zone to
resolve DNS queries for the associated DNS view.

###### Warning

Removing a private hosted zone association immediately affects DNS resolution. Queries
for domains in the disassociated zone will be resolved using public DNS instead of the private
zone records.
