# Managing service quotas for your portal in Amazon WorkSpaces Secure Browser

When you create your AWS account, we automatically set default service quotas (also
referred to as limits) for resource usage with AWS services. Administrators must be aware of
two quotas that might need to be increased to support their use case. These two quotas are the
number of web portals you can create in each region, and the number of maximum concurrent
sessions you can support with each available instance type in each region. You can request an
increase for these from the Service Quotas page in the AWS Console.

The following table lists the default service quotas limits.

| Default quotas within an AWS Region by account    | Value |
| ------------------------------------------------- | ----- |
| Web portals                                       | 3     |
| Maximum concurrent sessions<br>• standard.regular | 25    |
| Maximum concurrent sessions<br>• standard.large   | 10    |
| Maximum concurrent sessions<br>• standard.xlarge  | 5     |

To view the service quotas allocated to your account for each region at any time, see the
[Service Quotas page](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/workspaces-web/quotas").

###### Important

Service quotas affect one AWS Region at a time. You must request service quota increases
in each AWS Region where you need more resources. For more information, [Amazon WorkSpaces Secure Browser endpoints and quotas](../../../general/latest/gr/workspacesweb.md "../../../general/latest/gr/workspacesweb.md").

###### Topics

- [Requesting a service quota increase in Amazon WorkSpaces Secure Browser](quota-increase.md "quota-increase.md")
- [Requesting a portal increase in Amazon WorkSpaces Secure Browser](request-portal-increase.md "request-portal-increase.md")
- [Requesting a maximum concurrent sessions
  increase in Amazon WorkSpaces Secure Browser](request-max-concurrent-session.md "request-max-concurrent-session.md")
- [Limit example for Amazon WorkSpaces Secure Browser](limit-example.md "limit-example.md")
- [Other service quotas in Amazon WorkSpaces Secure Browser](other-quotas.md "other-quotas.md")
