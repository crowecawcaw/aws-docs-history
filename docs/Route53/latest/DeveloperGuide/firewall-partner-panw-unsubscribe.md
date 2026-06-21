# Unsubscribe from Palo Alto Networks

###### Important

To stop subscription charges, you must remove all PANW rules from your DNS Firewall
rule groups in addition to unsubscribing from AWS Marketplace. If you unsubscribe
but leave the rules in your rule groups, charges continue until you remove
the rules.

###### Remove PANW rules from all rule groups

Use the following procedure to remove PANW rules.

1. Open the Amazon Virtual Private Cloud console.
2. In the navigation pane, choose **DNS Firewall**, then
   choose **Rule groups**.
3. For each rule group containing Palo Alto Networks rules, select the
   partner managed rules and choose **Delete**.
4. Confirm deletion.

###### Cancel the Marketplace subscription

Use the following procedure to cancel the subscription.

1. Open the AWS Marketplace console.
2. Choose **Manage subscriptions**.
3. Open the **Delivery method** list and choose
   **SaaS**.
4. Under **Agreement**, open the
   **Actions** list and choose **Cancel
   subscription** next to the Palo Alto Networks product.
5. In the **Cancel subscription** dialog box, enter
   `confirm`, then choose **Yes, cancel
   subscription**.

###### Note

If you unsubscribe but leave the rules in your rule groups, charges
continue until you remove the rules.
