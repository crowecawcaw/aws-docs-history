End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Active Directory sites and services

To reduce login latency, add the VPC CIDR range to your Active Directory sites and services (**Start ->
Administrative Tools -> Active Directory Sites and Services**). Add the VPC CIDR range to an Active Directory
Site that contains Domain Controllers that are closest to AWS.

Provide the AD site name of the site that you dedicated for AMS to your CSDM. AMS will rename the default site on the AMS side of AD to
match the provided name.
