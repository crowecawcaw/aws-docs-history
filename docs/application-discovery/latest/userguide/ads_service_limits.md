AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# AWS Application Discovery Service Quotas

The Service Quotas console provides information about AWS Application Discovery Service quotas. You can use the
Service Quotas console to view the default service quotas or to [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/discovery/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/discovery/quotas") for adjustable quotas.

Currently, the only quota that can be increased is **imported servers per
account**.

Application Discovery Service has the following default quotas:

- 1,000 applications per account.

If you reach this quota, and want to import new applications, you can delete
existing applications with the `DeleteApplications` API action. For more
information, see [DeleteApplications](../APIReference/API_DeleteApplications.md "../APIReference/API_DeleteApplications.md") in the
_Application Discovery Service API Reference_.

- Each import file can have a maximum file size of 10 MB.
- 25,000 imported server records per account.
- 25,000 deletions of import records per day.
- 10,000 imported servers per account (you can request to increase this quota).
- 1,000 active agents, which are collecting and sending data to Application Discovery Service.
- 10,000 inactive agents, which are responsive but not collecting data.
- 400 servers per application.
- 30 tags per server.
