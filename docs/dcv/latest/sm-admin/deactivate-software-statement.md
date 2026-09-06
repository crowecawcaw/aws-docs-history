

# deactivate-software-statement
<a name="deactivate-software-statement"></a>

Deactivates a software statement. When you deactivate a software statement, it can no longer be used for agent registrations.

**Topics**
+ [Syntax](#sytnax)
+ [Options](#options)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker deactivate-software-statement --software-statement {{software_statement}}
```

## Options
<a name="options"></a>

**`--software-statement`**  
The software statement to deactivate.  
Type: String  
Required: Yes

## Example
<a name="example"></a>

The following example deactivates a software statement.

**Command**

```
sudo -u root dcv-session-manager-broker deactivate-software-statement --software-statement EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNEXAMPLEQiIDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlEXAMPLEiIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE
```

**Output**

```
Software statement EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNEXAMPLEQiIDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlEXAMPLEiIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE deactivated
```