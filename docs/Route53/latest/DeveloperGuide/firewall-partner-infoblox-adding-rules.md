

# Adding Infoblox rules to DNS Firewall rule groups

After you subscribe, you can create one or more rules using Infoblox threat feeds within any DNS Firewall rule group.

**To add an Infoblox rule**  
Use the following procedure to add a rule.

1. Open the Amazon Virtual Private Cloud console and in the navigation pane, choose **DNS Firewall**, then choose **Rule groups**.

1. Select the target rule group.

1. Choose **Add rule**.

1. Under **Rule details**, enter a **Name** and select the **Advanced** plan pricing option.

1. Under **Rule configurations** > **Rule type**, select **Partner managed DNS threat protection**.

1. Under **Vendor**, confirm that **Infoblox** is selected.

1. Under **DNS security categories**, choose one or more threat list feeds from the dropdown. For more information about the available categories, see the following table.

1. Under **Action**, choose the action: **ALERT** (logs but allows) or **BLOCK** (blocks the query).

1. Choose **Add rule**. A success banner confirms rule creation.

**Available DNS security categories**  
The following table describes the DNS security categories available from Infoblox.


**Infoblox DNS security categories**  

| Category | Description | 
| --- | --- | 
| Infoblox - Informational | Domains that Infoblox lists at the informational threat level. These domains carry little known risk. Use them with the ALERT action to monitor DNS traffic. | 
| Infoblox - Low Risk | Domains that Infoblox rates at the low threat level. | 
| Infoblox - Medium Risk | Domains that Infoblox rates at the medium threat level. | 
| Infoblox - High Risk | Domains that Infoblox rates at the high threat level. | 
| Infoblox - Critical Risk | Domains that Infoblox rates at the critical threat level, the most severe level. | 

**Tip**  
Each selected security category creates a separate rule entry within the rule group. If you select 4 categories, 4 rules are created with sequential priorities.