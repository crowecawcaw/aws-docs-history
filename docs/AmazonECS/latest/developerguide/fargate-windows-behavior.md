# Windows containers on Fargate container image pull behavior for Amazon ECS

Fargate Windows caches the most recent month's, and the previous month's, servercore
base image provided by Microsoft. These images match the KB/Build number patches updated
each Patch Tuesday. For example, on April 9, 2024, Microsoft released KB5036896 (17763.5696) for
Windows Server 2019. The previous month KB on March 12, 2024 was KB5035849 (17763.5576). So for
the platforms `WINDOWS_SERVER_2019_CORE` and
`WINDOWS_SERVER_2019_FULL` the following container images were cached::

- `mcr.microsoft.com/windows/servercore:ltsc2019`
- `mcr.microsoft.com/windows/servercore:10.0.17763.5696`
- `mcr.microsoft.com/windows/servercore:10.0.17763.5576`
  Additionally, on April 9, 2024, Microsoft released KB5036909 (20348.2402) for Windows Server

2022. The previous month KB on March 12, 2024 was KB5035857 (20348.2340). So for the platforms
      `WINDOWS_SERVER_2022_CORE` and `WINDOWS_SERVER_2022_FULL` the
      following container images were cached:

- `mcr.microsoft.com/windows/servercore:ltsc2022`
- `mcr.microsoft.com/windows/servercore:10.0.20348.2402`
- `mcr.microsoft.com/windows/servercore:10.0.20348.2340`
