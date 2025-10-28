# Updates to shared services: Multi-Account Landing Zone

AMS applies data plane releases to managed accounts on a monthly basis, without prior notice.

AMS uses the core OU to provide shared services such as access, networking, EPS, log storage, alert aggregation
in your Multi-Account Landing Zone. AMS is responsible for addressing vulnerabilities, patching, and deployments of these shared services.
AMS regularly updates the resources used for providing these shared services so that users have access to latest
features, and security updates. The updates typically happen on a monthly basis. Resources that are part of these updates are:

- Accounts that are part of the core OU.

The management account, shared services account, network account, security account, and log archive account
have resources for RDP and SSH bastions, proxies, management hosts, and endpoint security (EPS), that are typically
updated every month. AMS uses immutable EC2 deployments as part of the shared services infrastructure.

- New AMS AMIs incorporating the latest updates.

###### Note

AMS operators utilize an internal alarm suppression change type (CT) when executing data plane changes
and the RFC for that CT appears in your RFC list.
This is because, as the data plane release is deployed, various infrastructure may be shut down, rebooted,
taken offline, or there may be CPU spikes or
other effects of the deployment that trigger alarms that, during the data plane deployment, are extraneous.
Once the deployment is complete, all infrastructure
is verified to be running properly and alarms are re-enabled.
