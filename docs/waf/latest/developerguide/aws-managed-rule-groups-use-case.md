**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Use-case specific rule

groups

Use-case specific rule groups provide incremental protection for many
diverse AWS WAF use cases. Choose the rule groups that apply to your
application.

## SQL database managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesSQLiRuleSet`, WCU: 200

###### Note

This documentation covers the most recent static version release of this managed rule group. We report
version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md").
For information about other versions, use the API command
[DescribeManagedRuleGroup](../APIReference/API_DescribeManagedRuleGroup.md "../APIReference/API_DescribeManagedRuleGroup.md").

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The SQL database rule group contains rules to block request patterns
associated with exploitation of SQL databases, like SQL injection attacks.
This can help prevent remote injection of unauthorized queries. Evaluate
this rule group for use if your application interfaces with an SQL
database.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name                             | Description and label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SQLi_QUERYARGUMENTS`                 | Uses the built-in AWS WAF [SQL injection attack rule<br>statement](waf-rule-statement-type-sqli-match.md "waf-rule-statement-type-sqli-match.md"), with<br>sensitivity level set to Low, to<br>inspect the values of all query parameters for<br>patterns that match malicious SQL code.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:sql-database:SQLi_QueryArguments`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `SQLiExtendedPatterns_QUERYARGUMENTS` | Inspects the values of all query parameters for<br>patterns that match malicious SQL code. The patterns<br>this rule inspects for aren't covered by the<br>rule `SQLi_QUERYARGUMENTS`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:sql-database:SQLiExtendedPatterns_QueryArguments`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `SQLi_BODY`                           | Uses the built-in AWS WAF [SQL injection attack rule<br>statement](waf-rule-statement-type-sqli-match.md "waf-rule-statement-type-sqli-match.md"), with sensitivity level set to<br>Low, to inspect the request body for<br>patterns that match malicious SQL code.<br>WarningThis rule only inspects the request body up to the body size limit for the protection pack (web ACL) and resource type. For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. This rule uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:sql-database:SQLi_Body` |
| `SQLiExtendedPatterns_BODY`           | Inspects the request body for patterns that match<br>malicious SQL code. The patterns this rule inspects<br>for aren't covered by the rule<br>`SQLi_BODY`.<br>WarningThis rule only inspects the request body up to the body size limit for the protection pack (web ACL) and resource type. For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. This rule uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:sql-database:SQLiExtendedPatterns_Body`                                                                                          |
| `SQLi_COOKIE`                         | Uses the built-in AWS WAF [SQL injection attack rule<br>statement](waf-rule-statement-type-sqli-match.md "waf-rule-statement-type-sqli-match.md"), with sensitivity level set to<br>Low, to inspect the request cookie<br>headers for patterns that match malicious SQL code.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:sql-database:SQLi_Cookie`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `SQLi_URIPATH`                        | Uses the built-in AWS WAF [SQL injection attack rule<br>statement](waf-rule-statement-type-sqli-match.md "waf-rule-statement-type-sqli-match.md"), with sensitivity level set to<br>Low, to inspect the request cookie<br>headers for patterns that match malicious SQL code.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:sql-database:SQLi_URIPath`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Linux operating system managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesLinuxRuleSet`, WCU: 200

###### Note

This documentation covers the most recent static version release of this managed rule group. We report
version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md").
For information about other versions, use the API command
[DescribeManagedRuleGroup](../APIReference/API_DescribeManagedRuleGroup.md "../APIReference/API_DescribeManagedRuleGroup.md").

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The Linux operating system rule group contains rules that block request patterns
associated with the exploitation of vulnerabilities specific to Linux,
including Linux-specific Local File Inclusion (LFI) attacks. This can
help prevent attacks that expose file contents or run code for which the
attacker should not have had access. You should evaluate this rule group
if any part of your application runs on Linux. You should use this rule
group in conjunction with the
[POSIX operating system](#aws-managed-rule-groups-use-case-posix-os "#aws-managed-rule-groups-use-case-posix-os")
rule group.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name         | Description and label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LFI_URIPATH`     | Inspects the request path for attempts to exploit<br>Local File Inclusion (LFI) vulnerabilities in web<br>applications. Example patterns include files like<br>`/proc/version`, which could provide<br>operating system information to attackers.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:linux-os:LFI_URIPath`                                                                                                                                                                                                                                                                                                                                                           |
| `LFI_QUERYSTRING` | Inspects the values of querystring for attempts to<br>exploit Local File Inclusion (LFI) vulnerabilities<br>in web applications. Example patterns include files<br>like `/proc/version`, which could provide<br>operating system information to attackers.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:linux-os:LFI_QueryString`                                                                                                                                                                                                                                                                                                                                              |
| `LFI_HEADER`      | Inspects request headers for attempts to exploit Local File Inclusion<br>(LFI) vulnerabilities in web applications. Example<br>patterns include files like<br>`/proc/version`, which could provide<br>operating system information to attackers.<br>WarningThis rule only inspects the first 8 KB of the request headers or the first 200 headers, whichever limit is reached first, and it uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:linux-os:LFI_Header` |

## POSIX operating system managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesUnixRuleSet`, WCU: 100

###### Note

This documentation covers the most recent static version release of this managed rule group. We report
version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md").
For information about other versions, use the API command
[DescribeManagedRuleGroup](../APIReference/API_DescribeManagedRuleGroup.md "../APIReference/API_DescribeManagedRuleGroup.md").

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The POSIX operating system rule group contains rules that block request
patterns associated with the exploitation of vulnerabilities specific to
POSIX and POSIX-like operating systems, including Local File Inclusion (LFI)
attacks. This can help prevent attacks that expose file contents or run code
for which the attacker should not have had access. You should evaluate this
rule group if any part of your application runs on a POSIX or POSIX-like
operating system, including Linux, AIX, HP-UX, macOS, Solaris, FreeBSD, and
OpenBSD.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name                                | Description and label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `UNIXShellCommandsVariables_QUERYSTRING` | Inspects the values of the query string for<br>attempts to exploit command injection, LFI, and path<br>traversal vulnerabilities in web applications that<br>run on Unix systems. Examples include patterns like<br>`echo $HOME` and `echo<br>$PATH`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:posix-os:UNIXShellCommandsVariables_QueryString`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `UNIXShellCommandsVariables_BODY`        | Inspects the request body for attempts to exploit<br>command injection, LFI, and path traversal<br>vulnerabilities in web applications that run on Unix<br>systems. Examples include patterns like `echo<br>$HOME` and `echo $PATH`.<br>WarningThis rule only inspects the request body up to the body size limit for the protection pack (web ACL) and resource type. For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. This rule uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:posix-os:UNIXShellCommandsVariables_Body` |
| `UNIXShellCommandsVariables_HEADER`      | Inspects all request headers for attempts to exploit<br>command injection, LFI, and path traversal<br>vulnerabilities in web applications that run on Unix<br>systems. Examples include patterns like `echo<br>$HOME` and `echo $PATH`.<br>WarningThis rule only inspects the first 8 KB of the request headers or the first 200 headers, whichever limit is reached first, and it uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:posix-os:UNIXShellCommandsVariables_Header`                                                                                                                                                                                                                                                                             |

## Windows operating system managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesWindowsRuleSet`, WCU: 200

###### Note

This documentation covers the most recent static version release of this managed rule group. We report
version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md").
For information about other versions, use the API command
[DescribeManagedRuleGroup](../APIReference/API_DescribeManagedRuleGroup.md "../APIReference/API_DescribeManagedRuleGroup.md").

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The Windows operating system rule group contains rules that block request patterns
associated with the exploitation of vulnerabilities specific to Windows,
like remote execution of PowerShell commands. This can help prevent
exploitation of vulnerabilities that permit an attacker to run
unauthorized commands or run malicious code. Evaluate this rule group if
any part of your application runs on a Windows operating system.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name                             | Description and label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `WindowsShellCommands_COOKIE`         | Inspects the request cookie headers for WindowsShell command injection attempts in<br>web applications. The match patterns represent<br>WindowsShell commands. Example patterns include<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     | nslookup`and`;cmd`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:windows-os:WindowsShellCommands_Cookie`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `WindowsShellCommands_QUERYARGUMENTS` | Inspects the values of all query parameters for<br>WindowsShell command injection attempts in web<br>applications. The match patterns represent<br>WindowsShell commands. Example patterns include<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     | nslookup`and`;cmd`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:windows-os:WindowsShellCommands_QueryArguments`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `WindowsShellCommands_BODY`           | Inspects the request body for WindowsShell command<br>injection attempts in web applications. The match<br>patterns represent WindowsShell commands. Example<br>patterns include `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |     | nslookup` and<br>`;cmd`.<br>WarningThis rule only inspects the request body up to the body size limit for the protection pack (web ACL) and resource type. For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. This rule uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:windows-os:WindowsShellCommands_Body` |
| `PowerShellCommands_COOKIE`           | Inspects the request cookie headers for PowerShell command injection attempts in<br>web applications. The match patterns represent<br>PowerShell commands. For example,<br>`Invoke-Expression`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:windows-os:PowerShellCommands_Cookie`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `PowerShellCommands_QUERYARGUMENTS`   | Inspects the values of all query parameters for<br>PowerShell command injection attempts in web<br>applications. The match patterns represent<br>PowerShell commands. For example,<br>`Invoke-Expression`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:windows-os:PowerShellCommands_QueryArguments`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `PowerShellCommands_BODY`             | Inspects the request body for PowerShell command<br>injection attempts in web applications. The match<br>patterns represent PowerShell commands. For example,<br>`Invoke-Expression`.<br>WarningThis rule only inspects the request body up to the body size limit for the protection pack (web ACL) and resource type. For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. This rule uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:windows-os:PowerShellCommands_Body` |

## PHP application managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesPHPRuleSet`, WCU: 100

###### Note

This documentation covers the most recent static version release of this managed rule group. We report
version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md").
For information about other versions, use the API command
[DescribeManagedRuleGroup](../APIReference/API_DescribeManagedRuleGroup.md "../APIReference/API_DescribeManagedRuleGroup.md").

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The PHP application rule group contains rules that block request patterns associated with
the exploitation of vulnerabilities specific to the use of the PHP
programming language, including injection of unsafe PHP functions. This
can help prevent exploitation of vulnerabilities that permit an attacker
to remotely run code or commands for which they are not authorized.
Evaluate this rule group if PHP is installed on any server with which
your application interfaces.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name                                 | Description and label                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PHPHighRiskMethodsVariables_HEADER`      | Inspects all headers for<br>PHP script code injection attempts.<br>Example patterns<br>include functions like `fsockopen` and<br>the `$_GET` superglobal variable.<br>WarningThis rule only inspects the first 8 KB of the request headers or the first 200 headers, whichever limit is reached first, and it uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:php-app:PHPHighRiskMethodsVariables_Header`                                                                                                                                                                                                                                                                                                |
| `PHPHighRiskMethodsVariables_QUERYSTRING` | Inspects everything after the first<br>`?` in the request URL, looking for<br>PHP script code injection attempts.<br>Example patterns<br>include functions like `fsockopen` and<br>the `$_GET` superglobal variable.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:php-app:PHPHighRiskMethodsVariables_QueryString`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `PHPHighRiskMethodsVariables_BODY`        | Inspects the values of the request body for PHP<br>script code injection attempts. Example patterns<br>include functions like `fsockopen` and<br>the `$_GET` superglobal variable.<br>WarningThis rule only inspects the request body up to the body size limit for the protection pack (web ACL) and resource type. For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. This rule uses the `Continue` option for oversize content handling. For more information, see<br>[Oversize web request components<br>in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:php-app:PHPHighRiskMethodsVariables_Body` |

## WordPress application managed rule group

VendorName: `AWS`, Name:
`AWSManagedRulesWordPressRuleSet`, WCU: 100

###### Note

This documentation covers the most recent static version release of this managed rule group. We report
version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md").
For information about other versions, use the API command
[DescribeManagedRuleGroup](../APIReference/API_DescribeManagedRuleGroup.md "../APIReference/API_DescribeManagedRuleGroup.md").

The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you
with what you need to use the rules without giving
bad actors what they need to circumvent the rules.

If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The WordPress application rule group contains rules that block request
patterns associated with the exploitation of vulnerabilities specific to
WordPress sites. You should evaluate this rule group if you are running
WordPress. This rule group should be used in conjunction with the
[SQL database](#aws-managed-rule-groups-use-case-sql-db "#aws-managed-rule-groups-use-case-sql-db")
and [PHP application](#aws-managed-rule-groups-use-case-php-app "#aws-managed-rule-groups-use-case-php-app")
rule groups.

This managed rule group adds labels to the web requests that
it evaluates, which are available to rules that run after this rule group in your protection pack (web ACL). AWS WAF
also records the labels to Amazon CloudWatch metrics. For general information about labels and label metrics, see [Web request labeling](waf-labels.md "waf-labels.md")
and [Label metrics and dimensions](waf-metrics.md#waf-metrics-label "waf-metrics.md#waf-metrics-label").

| Rule name                                  | Description and label                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `WordPressExploitableCommands_QUERYSTRING` | Inspects the request query string for high risk<br>WordPress commands that can be exploited in<br>vulnerable installations or plugins. Examples<br>patterns include commands like<br>`do-reset-wordpress`.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:wordpress-app:WordPressExploitableCommands_QUERYSTRING` |
| `WordPressExploitablePaths_URIPATH`        | Inspects the request URI path for WordPress files<br>like `xmlrpc.php`, which are known to<br>have easily exploitable vulnerabilities.<br>Rule action: Block<br>Label:<br>`awswaf:managed:aws:wordpress-app:WordPressExploitablePaths_URIPATH`                                                                            |
