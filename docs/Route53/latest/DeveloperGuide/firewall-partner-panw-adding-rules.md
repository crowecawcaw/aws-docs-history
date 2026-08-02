# Adding Palo Alto Networks rules to DNS Firewall rule groups

After you subscribe, you can create one or more rules using Palo Alto Networks threat
feeds within any DNS Firewall rule group.

###### To add a Palo Alto Networks rule

Use the following procedure to add a rule.

1. Open the Amazon Virtual Private Cloud console and in the navigation pane, choose
   **DNS Firewall**, then choose
   **Rule groups**.
2. Select the target rule group.
3. Choose **Add rule**.
4. Under **Rule details**, enter a
   **Name** and select the **Advanced**
   plan pricing option.
5. Under **Rule configurations** >
   **Rule type**, select **Partner managed DNS threat
   protection**.
6. Under **Vendor**, confirm **Palo Alto
   Networks** is selected.
7. Under **DNS security categories**, choose one or more
   threat list feeds from the dropdown. For more information about the
   available categories, see the following table.
8. Under **Action**, choose the action:
   **ALERT** (logs but allows) or
   **BLOCK** (blocks the query).
9. Choose **Add rule**. A success banner confirms rule
   creation.

###### Available DNS security categories

The following table describes the DNS security categories available from Palo Alto Networks.

DNS security categories| Category | Description |
| --- | --- |
| Palo Alto Networks<br>• Dynamic DNS Hosted Domains | Domains using dynamic DNS providers that allow rapid IP address<br>changes, frequently abused by threat actors to evade IP-based<br>blocking. |
| Palo Alto Networks<br>• Parked Domains | Domains displaying placeholder or "for sale" content. Attackers<br>might acquire these to leverage residual reputation and redirect<br>visitors to malicious content. |
| Palo Alto Networks<br>• Proxy Avoidance and Anonymizers | Domains providing services to bypass network security controls,<br>including web proxies, VPN services, and anonymizing<br>networks. |
| Palo Alto Networks<br>• Ad Tracking Domains | Domains used by advertising networks and third-party trackers to<br>monitor user activity. These can serve as vectors for malvertising<br>campaigns. |
| Palo Alto Networks<br>• Newly Registered Domains | Domains registered within the past 32 days. Attackers use fresh<br>domains because they lack reputation history, making them harder<br>to detect. |
| Palo Alto Networks<br>• Grayware Domains | Domains associated with applications that exhibit unwanted<br>behavior such as excessive tracking, unsolicited advertising, or<br>browser hijacking. |
| Palo Alto Networks<br>• Phishing Domains | Domains impersonating legitimate organizations to steal<br>credentials or personal information through typosquatting,<br>homograph attacks, or domain shadowing. |
| Palo Alto Networks<br>• Malware Domains | Domains that host or distribute malicious software, including<br>exploit kits, ransomware droppers, and trojan delivery<br>networks. |
| Palo Alto Networks<br>• Command and Control Domains | Domains used by malware to communicate with attacker-controlled<br>infrastructure for instructions, data exfiltration, or payload<br>delivery. |

###### Tip

Each selected security category creates a separate rule entry within the rule
group. If you select 4 categories, 4 rules are created with sequential
priorities.
