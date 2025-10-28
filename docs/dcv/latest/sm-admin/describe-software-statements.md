# describe-software-statements

Describes the existing software statements.

###### Topics

- [Syntax](#sytnax "#sytnax")
- [Output](#output "#output")
- [Example](#example "#example")

## Syntax

```
sudo -u root dcv-session-manager-broker describe-software-statements
```

## Output

**`software-statement`**

The software statement.

**`issued-at`**

The date and time the software was generated.

**`is-active`**

The current state of the software statement. `true` if the software statement
is active; otherwise it's `false`.

## Example

The following example generates a software statement.

**Command**

```
`sudo -u root dcv-session-manager-broker describe-software-statements`
```

**Output**

```
Software Statements
[ {
"software-statement" : "ewogICJpZCIgOiAiYmEEXAMPLEYtNzUwNy00YmFhLTliZWItYTA1MmJjZTE3NDJjIiwKICAiaXNzdWVkQXQiIDogMTU5NjY0MTkxMiEXAMPLEDAwMDAsCiAgImJyb2tlclZlcnNpb24iIDogIjEuMC4wIiwKICAiYWN0aXZlEXAMPLEydWUKfQ==",
"issued-at" : "2020.08.05 15:38:32 +0000",
"is-active" : "true"
}, {
"software-statement" : "EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNzdWEXAMPLEDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlcnNpb24iIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE",
"issued-at" : "2020.08.07 10:24:41 +0000",
"is-active" : "true"
} ]
```
