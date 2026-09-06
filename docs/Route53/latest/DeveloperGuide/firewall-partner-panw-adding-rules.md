

# Adding Palo Alto Networks rules to DNS Firewall rule groups
<a name="firewall-partner-panw-adding-rules"></a>

After you subscribe, you can create one or more rules using Palo Alto Networks threat feeds within any DNS Firewall rule group.

**To add a Palo Alto Networks rule**  
Use the following procedure to add a rule.

1. Open the Amazon Virtual Private Cloud console and in the navigation pane, choose **DNS Firewall**, then choose **Rule groups**.

1. Select the target rule group.

1. Choose **Add rule**.

1. Under **Rule details**, enter a **Name** and select the **Advanced** plan pricing option.

1. Under **Rule configurations** > **Rule type**, select **Partner managed DNS threat protection**.

1. Under **Vendor**, confirm **Palo Alto Networks** is selected.

1. Under **DNS security categories**, choose one or more threat list feeds from the dropdown. For more information about the available categories, see the following table.

1. Under **Action**, choose the action: **ALERT** (logs but allows) or **BLOCK** (blocks the query).

1. Choose **Add rule**. A success banner confirms rule creation.

**Available DNS security categories**  
The following table describes the DNS security categories available from Palo Alto Networks.


**DNS security categories**  

| Category | Description | 
| --- | --- | 
| Palo Alto Networks - Dynamic DNS Hosted Domains | Domains using dynamic DNS providers that allow rapid IP address changes, frequently abused by threat actors to evade IP-based blocking. | 
| Palo Alto Networks - Parked Domains | Domains displaying placeholder or "for sale" content. Attackers might acquire these to leverage residual reputation and redirect visitors to malicious content. | 
| Palo Alto Networks - Proxy Avoidance and Anonymizers | Domains providing services to bypass network security controls, including web proxies, VPN services, and anonymizing networks. | 
| Palo Alto Networks - Ad Tracking Domains | Domains used by advertising networks and third-party trackers to monitor user activity. These can serve as vectors for malvertising campaigns. | 
| Palo Alto Networks - Newly Registered Domains | Domains registered within the past 32 days. Attackers use fresh domains because they lack reputation history, making them harder to detect. | 
| Palo Alto Networks - Grayware Domains | Domains associated with applications that exhibit unwanted behavior such as excessive tracking, unsolicited advertising, or browser hijacking. | 
| Palo Alto Networks - Phishing Domains | Domains impersonating legitimate organizations to steal credentials or personal information through typosquatting, homograph attacks, or domain shadowing. | 
| Palo Alto Networks - Malware Domains | Domains that host or distribute malicious software, including exploit kits, ransomware droppers, and trojan delivery networks. | 
| Palo Alto Networks - Command and Control Domains | Domains used by malware to communicate with attacker-controlled infrastructure for instructions, data exfiltration, or payload delivery. | 

**Tip**  
Each selected security category creates a separate rule entry within the rule group. If you select 4 categories, 4 rules are created with sequential priorities.