# Active Directory sites and services

To reduce login latency, add the VPC CIDR range to your Active Directory sites and services (**Start ->
Administrative Tools -> Active Directory Sites and Services**). Add the VPC CIDR range to an Active Directory
Site that contains Domain Controllers that are closest to AWS.

Provide the AD site name of the site that you dedicated for AMS to your CSDM. AMS will rename the default site on the AMS side of AD to
match the provided name.
