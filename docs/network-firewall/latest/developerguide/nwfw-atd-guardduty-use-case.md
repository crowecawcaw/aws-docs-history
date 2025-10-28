# Working with active threat defense indicators in Amazon GuardDuty

If you use Amazon GuardDuty, you can strengthen your security by using active threat defense managed rule group to automatically
block the threats that Amazon GuardDuty detects. Amazon GuardDuty can generate findings with the threat list
name `Amazon Active Threat Defense`. You can block these threats by implementing
the `AttackInfrastructure` active threat defense rule group in your Network Firewall firewall policy.

###### Note

The active threat defense managed rule group can block threats regardless of whether you use Amazon GuardDuty.
This information is relevant only if you already use Amazon GuardDuty for threat detection.

The following Amazon GuardDuty finding types may indicate threats that active threat defense managed rule group can block:

Command and control related findings

- Backdoor:EC2/C&CActivity.B
- Backdoor:EC2/C&CActivity.B!DNS
- Backdoor:Lambda/C&CActivity.B
- Backdoor:Runtime/C&CActivity.B
- Backdoor:Runtime/C&CActivity.B!DNS

Cryptocurrency related findings

- CryptoCurrency:EC2/BitcoinTool.B
- CryptoCurrency:EC2/BitcoinTool.B!DNS
- CryptoCurrency:Lambda/BitcoinTool.B
- CryptoCurrency:Runtime/BitcoinTool.B
- CryptoCurrency:Runtime/BitcoinTool.B!DNS
- Impact:EC2/BitcoinDomainRequest.Reputation

Other threat findings

- Trojan:EC2/BlackholeTraffic!DNS
- Trojan:Runtime/BlackholeTraffic!DNS
- UnauthorizedAccess:EC2/MaliciousIPCaller.Custom

For more information about Amazon GuardDuty finding types, see
[Active findings](../../../guardduty/latest/ug/guardduty_finding-types-active.md "../../../guardduty/latest/ug/guardduty_finding-types-active.md")
in the _Amazon GuardDuty User Guide_.
