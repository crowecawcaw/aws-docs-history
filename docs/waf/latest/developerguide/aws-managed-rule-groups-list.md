**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS Managed Rules rule groups list

This section provides a list of available AWS Managed Rules rule groups.

This section describes the most recent versions of the AWS Managed Rules rule groups. You see these on the
console when you add a managed rule group to your protection pack (web ACL). Through the API, you
can retrieve this list along with the AWS Marketplace rule groups that you're
subscribed to by calling `ListAvailableManagedRuleGroups`.

###### Note

For information about retrieving an AWS Managed Rules rule group's versions, see [Retrieving the available versions for a managed rule
group](waf-using-managed-rule-groups-versions.md "waf-using-managed-rule-groups-versions.md").

All AWS Managed Rules rule groups support labeling, and the rule listings in this section include label
specifications. You can retrieve the labels for a managed rule group through the API by calling
`DescribeManagedRuleGroup`. The labels are listed in the
AvailableLabels property in the response. For information about
labeling, see [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").

Test and tune any changes to your AWS WAF protections before you use them for production traffic. For information,
see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

###### AWS Managed Rules rule groups

- [Baseline rule
  groups](aws-managed-rule-groups-baseline.md "aws-managed-rule-groups-baseline.md")
  - [Core rule set (CRS) managed rule group](aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-crs "aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-crs")
  - [Admin protection managed rule group](aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-admin "aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-admin")
  - [Known bad inputs managed rule group](aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-known-bad-inputs "aws-managed-rule-groups-baseline.md#aws-managed-rule-groups-baseline-known-bad-inputs")

- [Use-case specific rule
  groups](aws-managed-rule-groups-use-case.md "aws-managed-rule-groups-use-case.md")
  - [SQL database managed rule group](aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-sql-db "aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-sql-db")
  - [Linux operating system managed rule group](aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-linux-os "aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-linux-os")
  - [POSIX operating system managed rule group](aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-posix-os "aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-posix-os")
  - [Windows operating system managed rule group](aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-windows-os "aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-windows-os")
  - [PHP application managed rule group](aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-php-app "aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-php-app")
  - [WordPress application managed rule group](aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-wordpress-app "aws-managed-rule-groups-use-case.md#aws-managed-rule-groups-use-case-wordpress-app")

- [IP reputation rule
  groups](aws-managed-rule-groups-ip-rep.md "aws-managed-rule-groups-ip-rep.md")
  - [Amazon IP reputation list managed rule group](aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-amazon "aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-amazon")
  - [Anonymous IP list managed rule group](aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-anonymous "aws-managed-rule-groups-ip-rep.md#aws-managed-rule-groups-ip-rep-anonymous")

- [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md")
  - [Considerations for using this rule group](aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-using "aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-using")
  - [Labels added by this rule group](aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-labels "aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-labels")
    - [Token labels](aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-labels-token "aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-labels-token")
    - [ACFP labels](aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-labels-rg "aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-labels-rg")

  - [Account creation fraud prevention rules listing](aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-rules "aws-managed-rule-groups-acfp.md#aws-managed-rule-groups-acfp-rules")

- [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md")
  - [Considerations for using this rule group](aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-using "aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-using")
  - [Labels added by this rule group](aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-labels "aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-labels")
    - [Token labels](aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-labels-token "aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-labels-token")
    - [ATP labels](aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-labels-rg "aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-labels-rg")

  - [Account takeover prevention rules listing](aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-rules "aws-managed-rule-groups-atp.md#aws-managed-rule-groups-atp-rules")

- [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md")
  - [Protection levels](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-prot-levels "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-prot-levels")
  - [Considerations for using this rule group](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-using "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-using")
  - [Labels added by this rule group](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels")
    - [Token labels](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels-token "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels-token")
    - [Bot Control labels](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels-rg "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-labels-rg")

  - [Bot Control rules listing](aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules "aws-managed-rule-groups-bot.md#aws-managed-rule-groups-bot-rules")

- [AWS WAF Distributed Denial of Service (DDoS) prevention rule group](aws-managed-rule-groups-anti-ddos.md "aws-managed-rule-groups-anti-ddos.md")
  - [Considerations for using this rule group](aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-using "aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-using")
  - [Labels added by this rule group](aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-labels "aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-labels")
    - [Token labels](aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-labels-token "aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-labels-token")
    - [Anti-DDoS labels](aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-labels-rg "aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-labels-rg")

  - [Anti-DDoS rules listing](aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-rules "aws-managed-rule-groups-anti-ddos.md#aws-managed-rule-groups-anti-ddos-rules")
