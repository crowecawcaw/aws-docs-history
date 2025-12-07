# Build lists of domains to block or allow

You can create your own domain lists to specify domain categories that you either don't find in the managed domain list offerings or that you prefer to handle on your own.

In addition to the procedures described in this section, in the console, you can create a domain list in the context of DNS Firewall rule management, when you create or update a rule.

Each domain specification in your domain list must satisfy the following requirements:

- It can optionally start with `*` (asterisk).
- With the exception of the optional starting asterisk and a period, as a delimiter between labels, it must only contain the following characters: `A-Z`, `a-z`, `0-9`, `-` (hyphen).
- It must be from 1-255 characters in length.
  **To create a domain list**

1. In the Route 53 Global Resolver console, navigate to your Global Resolver.
2. Choose the **Domain lists** tab.
3. Choose **Create domain list**.
4. Provide a name and optional description for your domain list, along with any tags, and select **Create domain list**.
5. Once created and operational, you can begin adding domains to your domain list by selecting **Add domains**.
6. If you choose to **Upload a list of domains from an Amazon S3 bucket**, enter the URI of the Amazon S3 bucket where you created a domain list. This domain list should have one domain name per line.
7. Otherwise, enter your domain specifications in the text box, one per line.
8. Choose **Add domains**.
   **To delete a domain list**

9. In the Route 53 Global Resolver console, navigate to your Global Resolver.
10. Choose the **Domain lists** tab.
11. Select the domain list that you want to delete, then choose **Delete**, and confirm the deletion.
