# Other service quotas in Amazon WorkSpaces Secure Browser

You can view and request increases for other quotas listed on the [Service Quotas page](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas"). In practice, most customers will find it unnecessary to request
increases for these limits. These quotas are broadly grouped into two types:
_Number_ and _Rate_.

For Number quotas, when you submit a service quota increase for Number of web portals, you
will automatically receive an increase in the number of sub-resources required to create a
unique portal. This will be reflected on the [Service Quotas page](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas"). For example, if you request an increase in portals from 3 to 5,
you will automatically receive a service quota increase from 3 to 5 for both browser and user
settings. You have the option to re-use or create new sub-resources as desired.

On rare occasion, customers may find a use case for increasing the number or rate of other
resource quotas. For example, administrators may want to increase the number of browser settings
for testing additional portal configurations. These service quota requests will be reviewed and
fulfilled on a case-by-case basis.

For Rate quotas, the rate limits exposed in Service Quotas should not need to be adjusted,
regardless of the account portal limit.
