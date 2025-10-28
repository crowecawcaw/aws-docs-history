# Updating a AWS Network Firewall logging configuration

To update your firewall's logging configuration through the Network Firewall AWS Management Console, use the
procedure in this section. For the API, see the Network Firewall API action,
`UpdateLoggingConfiguration`.

###### Note

Firewall logging is only available for traffic that you forward to
the stateful rules engine. You forward traffic to the stateful engine through stateless rule
actions and stateless default actions in the firewall policy. For information about these actions settings, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md "firewall-policy-settings.md") and [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

###### To update a firewall's logging configuration through the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, choose the name of the
   firewall that you want to edit. This takes you to the firewall's details
   page.
4. Choose the tab **Firewall details**, then in the
   **Logging** section, choose **Edit**.
5. Adjust the **Log type** selections as needed.
   To disable logging for a firewall, deselect all options.
   - **Flow** – Sends logs for all
     network traffic that the stateless engine forwards to the stateful
     rules engine.
   - **Alert** – Sends logs for
     traffic that matches any stateful rule whose action is set to
     `Alert`, `Drop`, or `Reject`. For more information
     about stateful rules and rule groups, see [Managing your own rule groups in AWS Network Firewall](rule-groups.md "rule-groups.md").
   - **TLS** – Sends logs for
     events related to TLS inspection. Network Firewall currently logs failures
     in certificate revocation checks for outbound traffic
     and TLS errors.

   These logs require the firewall to be configured
   for TLS inspection. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").

6. For each selected log type, choose the destination type, then provide the
   information for the logging destination that you prepared following the
   guidance in [Firewall logging destinations](firewall-logging-destinations.md "firewall-logging-destinations.md").

In order to change the destination for an existing **Log type**, you must first disable logging for the policy. Then, edit the policy and specify the new destination(s) for the **Log type**. 7. Choose **Save** to save your changes and return to the
firewall's detail page.
