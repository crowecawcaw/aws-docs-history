AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Learning to craft effective

prompts to ask Amazon Q about your fleet

The better quality of the question, or the prompt, that you give to Amazon Q, the
better the result it provides you with.

###### Tips for query prompts

Keep in mind the following tips when querying Amazon Q about your fleet:

1. To help improve the accuracy of your results, use the terms "managed
   nodes" and "managed instances" in your prompts instead of just "nodes" and
   "instances".
2. To query for results across multiple accounts that are part of an
   _organization_, as configured in AWS Organizations, you must
   be logged into the delegated administrator account in the designated home
   Region.
3. In the delegated administrator account, use terms to help Amazon Q
   understand that you are asking about nodes and instances across the
   organization by specifically using terms such as "in my organization" or "in
   my account 123456789012".

###### Topics

- [Sample questions for Amazon Q](#sample-questions-Q "#sample-questions-Q")
- [Supported operating system names and
  versions for prompts](#supported-os-names-Q "#supported-os-names-Q")

## Sample questions for Amazon Q

In the following table, we provide sample questions demonstrate some ways you
can create queries of Amazon Q that lead to better results.

We also provide examples of the filters Amazon Q will apply when running the
[ListNodes](../APIReference/API_ListNodes.md "../APIReference/API_ListNodes.md") command, which are generated from the content of your
prompt.

| Sample natural language question                                                                                                             | Amazon Q applied filters                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Show me my Windows managed<br>nodes.`                                                                                                       | `<br>PlatformType = Windows<br>`                                                                                                                      |
| `List my managed instances in account<br>123456789012.`                                                                                      | `<br>AccountId = 123456789012<br>`                                                                                                                    |
| `Show me all managed nodes running Amazon Linux 2 across my<br>organization.`                                                                | `<br>PlatformName = Amazon Linux<br>PlatformVersion = 2<br>`                                                                                          |
| `Show me all managed instances running Microsoft<br>Windows Server 2019 Datacenter in my<br>organization.`                                   | `<br>PlatformName = Microsoft Windows Server 2019 Datacenter<br>`                                                                                     |
| `Can you show me all managed nodes with SSM Agent<br>version 3.3.1142.0?`                                                                    | `<br>AgentType = amazon-ssm-agent<br>AgentVersion = 3.3.1142.0<br>`                                                                                   |
| `List all Amazon Linux 2 managed instances in account<br>123456789012 that have SSM Agent version<br>3.3.1230.0.`                            | `<br>PlatformName = Amazon Linux<br>PlatformVersion = 2<br>AccountId = 123456789012<br>AgentType = amazon-ssm-agent<br>AgentVersion = 3.3.1230.0<br>` |
| `What Microsoft Windows Server 2012 R2 Enterprise managed<br>nodes are running in the eu-central-1 region across my<br>entire organization?` | `<br>PlatformName = Microsoft Windows Server 2012 R2 Enterprise<br>Region = eu-central-1<br>`                                                         |
| `Show me all managed instances running Red Hat<br>Linux 7 in ou-d6ty-gxdma6vm.`                                                              | `<br>PlatformName = RHEL Linux<br>PlatformVersion = 7<br>OrganizationalUnitId = ou-d6ty-gxdma6vm<br>`                                                 |
| `What Ubuntu managed instances are in account<br>123456789012?`                                                                              | `<br>PlatformName = Ubuntu<br>AccountId = 123456789012<br>`                                                                                           |
| `List my Linux managed<br>instances.`                                                                                                        | `<br>PlatformType = Linux<br>`                                                                                                                        |
| `Find my macOS managed nodes.`                                                                                                               | `<br>PlatformType = macOS<br>`                                                                                                                        |
| `Show me all versions of Amazon Linux managed nodes in my<br>org.`                                                                           | `<br>PlatformName = Amazon Linux<br>`                                                                                                                 |
| `List managed nodes running<br>Amazon Linux 2.`                                                                                              | `<br>PlatformName = Amazon Linux<br>PlatformVersion = 2<br>`                                                                                          |
| `List the managed nodes with Ubuntu 16.04 in<br>account 123456789012.`                                                                       | `<br>PlatformName = Ubuntu<br>PlatformVersion = 16.04<br>AccountId = 123456789012<br>`                                                                |
| `Find all managed nodes that have an SSM Agent<br>version that is not 3.3.987.0.`                                                            | `<br>AgentType = amazon-ssm-agent<br>AgentVersion != 3.3.987.0<br>`                                                                                   |
| `List all managed instances that are not running a<br>Linux operating system.`                                                               | `<br>PlatformType != Linux<br>`                                                                                                                       |

## Supported operating system names and

versions for prompts

When you are asking Amazon Q about the managed nodes in your account, it's
helpful to provide the name of an operating system as its labeled in Systems Manager. You
can also provide version numbers to further narrow down your results. For
example, as represented in the following tables, you could ask for results
specifically about `macOS 14.5`, `Microsoft
 Windows Server 2019 Datacenter`, and `AlmaLinux 9.2 through
 9.4`, to name just a few examples.

These lists might not be exhaustive and are offered as examples only.

| macOS | Platform name                              | Version numbers |
| ----- | ------------------------------------------ | --------------- |
| macOS | 13.2, 13.4, 13.7, 14.1, 14.5, 14.6.1, 15.0 |

| Windows                                     | Releases   | Version numbers |
| ------------------------------------------- | ---------- | --------------- |
| Microsoft Windows Server 2012 R2 Datacenter | 6.3.9600   |
| Microsoft Windows Server 2012 R2 Standard   | 6.3.9600   |
| Microsoft Windows Server 2012 Standard      | 6.2.9200   |
| Microsoft Windows Server 2016 Datacenter    | _N/A_      |
| Microsoft Windows Server 2016 Standard      | 10.0.14393 |
| Microsoft Windows Server 2019 Datacenter    | _N/A_      |
| Microsoft Windows Server 2019 Standard      | _N/A_      |
| Microsoft Windows Server 2022 Datacenter    | _N/A_      |
| Microsoft Windows Server 2022 Standard      | 10.0.20348 |

| Linux                           | Platform names                                                                                                                                | Version numbers |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| AlmaLinux                       | 8.10, 9.2, 9.3, 9.4                                                                                                                           |
| Amazon Linux 2                  | 2.0 and greater                                                                                                                               |
| Amazon Linux 2023               | 2023.0.20230315.0 and greater                                                                                                                 |
| BottleRocket                    | 1.14.3, 1.16.1, 1.18.0, 1.19.1, 1.19.2, 1.19.5, 1.20.0,<br>1.20.1, 1.20.2, 1.20.3, 1.20.5, 1.21.1, 1.23.0, 1.24.0, 1.24.1,<br>1.25.0, 1.26.1, |
| CentOS Stream                   | 9                                                                                                                                             |
| Debian GNU/Linux                | 11-12                                                                                                                                         |
| Oracle Linux Server             | 7.8, 8.2, 8.3, 8.8, 8.9, 8.10, 9.4                                                                                                            |
| Red Hat Enterprise Linux        | 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 8.10, 9.2, 9.3,<br>9.4                                                                                |
| Red Hat Enterprise Linux Server | 17.3, 7.6, 7.7, 7.8,7.9                                                                                                                       |
| Rocky Linux                     | 8.6, 8.7, 8.8, 8.9, 8.10, 9.1, 9.2, 9.3, 9.4                                                                                                  |
| Ubuntu Server                   | 16.04, 18.04, 20.04, 22.04, 24.04                                                                                                             |
