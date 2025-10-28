# deactivate-software-statement

Deactivates a software statement. When you deactivate a software statement, it can no longer be used for agent registrations.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Options](#options "#options")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker deactivate-software-statement --software-statement `software_statement`
```

## Options

**`--software-statement`**

The software statement to deactivate.

Type: String

Required: Yes

## Example

The following example deactivates a software statement.

**Command**

```
`sudo -u root dcv-session-manager-broker deactivate-software-statement --software-statement EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNEXAMPLEQiIDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlEXAMPLEiIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE`
```

**Output**

```
Software statement EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNEXAMPLEQiIDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlEXAMPLEiIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE deactivated
```
