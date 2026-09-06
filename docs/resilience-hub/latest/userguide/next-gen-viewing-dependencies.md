

# Viewing discovered dependencies
<a name="next-gen-viewing-dependencies"></a>

After dependency discovery is enabled, you can view a table of discovered dependencies with the following columns:


| Column | Description | 
| --- | --- | 
| Dependency name | Identified name or domain name (for example, "LaunchDarkly" or "api.stripe.com") | 
| Type | AWS service, third-party, or internal | 
| Location | Where the dependency is hosted (for example, AWS us-east-1, Azure us-central, or RFC1918) | 
| Criticality | Hard or soft – user-assigned classification | 
| Query frequency | Visualization of query volume over time | 
| First seen | When the dependency was first discovered | 
| Last seen | Most recent query to this dependency | 

**Dependency timeline**

The dependency timeline shows when each dependency was first discovered and its activity over time. Select any dependency to view the underlying domain names and destination IP addresses. Usage frequency is available over the past 35 days, shown at hourly detail for single-day windows or daily detail for weekly windows.

**Compute resource attribution**

Next generation Resilience Hub attributes discovered dependencies to the specific compute resources – such as Amazon EC2 instances, Lambda functions, or containers – that make DNS queries to those dependencies. You can filter the dependency list by service (when viewing at the system level), criticality (hard, soft, or unclassified), type (AWS service, third-party, or internal), or location (AWS, third-party, or internal).