

# Rule states for Palo Alto Networks rules
<a name="firewall-partner-panw-rule-states"></a>

PANW rules in DNS Firewall can have different sync states that indicate their status.


**Rule sync states**  

| Sync state | Description | Recommended action | 
| --- | --- | --- | 
| CREATED | The rule has been successfully created and is being enforced normally. | No action needed. | 
| CREATING | The rule is currently being created, pending an entitlement check. If you are subscribed to the PANW product, the rule eventually transitions to CREATED. | No action needed. | 
| CREATION\_FAILED | The rule failed to create because you are not subscribed to the PANW product. | To retry rule creation after subscribing, you must delete the rule from the rule group and create the rule again. | 

To check rule status in the console, navigate to the DNS Firewall rule group and check the **Status** column in the rules table.