AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Troubleshooting parameter handling

issues

## Common parameter handling issues

**Environment variables not available during execution**

**Problem:** Commands fail because
environment variables
(`SSM_`parameter-name``) are
not found.

**Possible causes:**

- SSM Agent version doesn't support environment variable
  interpolation
- `interpolationType` is not set to
  `ENV_VAR`
- Parameter name doesn't match the expected environment variable
  name

**Solution:**

- Verify SSM Agent version is 3.3.2746.0 or later
- Add fallback logic for older agent versions:

```
if [ -z "${SSM_parameterName+x}" ]; then
    export SSM_parameterName="{{parameterName}}"
fi
```

**Parameter values containing special characters**

**Problem:** Commands fail when parameter
values contain spaces, quotes, or other special characters.

**Solution:**

- Use proper quoting when referencing environment
  variables:

```
# Correct
echo "$SSM_`parameter-name`"

# Incorrect
echo $SSM_`parameter-name`
```

- Add input validation using `allowedPattern` to
  restrict special characters

**Inconsistent behavior across platforms**

**Problem:** Parameter handling works
differently on Linux and Windows Server systems.

**Solution:**

- Use platform-specific environment variable syntax:

```
# PowerShell
$env:SSM_`parameter-name`

# Bash
$SSM_`parameter-name`
```

- Use platform-specific precondition checks in your
  document

**Parameter values not properly escaped**

**Problem:** Command injection
vulnerabilities despite using environment variable interpolation.

**Solution:**

- Always use proper escaping when including parameter values in
  commands:

```
# Correct
mysql_command="mysql -u \"$SSM_username\" -p\"$SSM_password\""

# Incorrect
mysql_command="mysql -u $SSM_username -p$SSM_password"
```

## Parameter validation tips

Use these techniques to validate your parameter handling:

1. Test environment variable availability:

```
#!/bin/bash
# Print all SSM_ environment variables
env | grep ^SSM_

# Test specific parameter
if [ -n "$SSM_parameter" ]; then
    echo "Parameter is available"
else
    echo "Parameter is not available"
fi
```

2. Verify parameter patterns:

```
parameters:
  myParameter:
    type: String
    allowedPattern: "^[a-zA-Z0-9_-]+$"
    description: "Test this pattern with sample inputs"
```

3. Include error handling:

```
if [[ ! "$SSM_parameter" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "Parameter validation failed"
    exit 1
fi
```
