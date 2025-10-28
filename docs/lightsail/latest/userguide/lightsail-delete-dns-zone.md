# Delete a DNS zone in Lightsail

In some cases, you might want to completely remove a DNS zone that you've set up in
Amazon Lightsail to manage your domain's DNS records. Perhaps you want to transfer DNS
management to a different provider or back to your domain registrar. Deleting a DNS zone is a
straightforward process, but it's important to plan ahead to ensure your domain's traffic
continues to route correctly. Let's go over the steps to delete a DNS zone in
Lightsail.

###### Important

If you plan to continue routing traffic through your domain, prepare a different DNS
hosting provider before deleting your domain's DNS zone in Lightsail. Otherwise, all
traffic to your website stops when you delete the Lightsail DNS zone.

###### To delete a DNS zone

1. On the Lightsail console home page, In the left navigation pane, choose
   **Domains & DNS**.
2. Choose the name of the DNS zone you want to delete.
3. Choose the vertical ellipsis menu (⋮). Then, choose the
   **Delete** option.
4. Choose **Delete DNS zone** to confirm the deletion.

The DNS zone is deleted from Lightsail.
