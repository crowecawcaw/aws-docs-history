# Understanding control parameters in Security Hub CSPM

Some controls in AWS Security Hub CSPM use parameters that affect how the control is evaluated. Typically, such controls are evaluated
against the default parameter values that Security Hub CSPM defines. However, for a subset of these controls, you can modify the parameter values. When you modify a control parameter value,
Security Hub CSPM starts evaluating the control against the value that you specify. If the resource underlying the control satisfies the custom value, Security Hub CSPM generates a `PASSED` finding.
If the resource doesn't satisfy the custom value, Security Hub CSPM generates a `FAILED` finding.

By customizing control parameters, you can refine the security best practices recommended and monitored by Security Hub CSPM
to align with your business requirements and security expectations. Instead of suppressing findings for a control, you can customize one or more of its
parameters to get findings that suit your security needs.

Here are some sample use cases for modifying control parameters and setting custom values:

- **[CloudWatch.16] – CloudWatch log groups should be retained for a specified time period**

You can specify the retention time period.

- **[IAM.7] – Password policies for IAM users should have strong configurations**

You can specify parameters related to password strength.

- **[EC2.18] – Security groups should only allow unrestricted incoming traffic for authorized ports**

You can specify which ports are authorized to permit unrestricted incoming traffic.

- **[Lambda.5] – VPC Lambda functions should operate in multiple Availability Zones**

You can specify the minimum number of Availability Zones that produces a passed finding.
This section covers things to consider when you modify control parameters.

## Effect of modifying control parameter values

When you change a parameter value, you also trigger a new security check that evaluates the control based on the
new value. Security Hub CSPM then generates new control findings based on the new value. During periodic updates to control findings,
Security Hub CSPM also uses the new parameter value. If you change parameter values for a control, but haven't enabled any standards that include the control, Security Hub CSPM doesn't conduct
any security checks using the new values. You have to enable at least one relevant standard for Security Hub CSPM to evaluate the control based
on the new parameter value.

A control can have one or more customizable parameters. Possible data types for each control parameter include the following:

- Boolean
- Double
- Enum
- EnumList
- Integer
- IntegerList
- String
- StringList

Custom parameter values apply across your enabled standards. You can't customize the parameters for a control that's
not supported in your current Region. For a list of Regional limits for individual controls, see [Regional limits on Security Hub CSPM controls](regions-controls.md "regions-controls.md").

For some controls, acceptable parameter values must fall into a
specified range to be valid. In these cases, Security Hub CSPM provides the acceptable range.

Security Hub CSPM chooses default parameter values and might occasionally update them. After you customize a control
parameter, its value continues to be the value that you specified for the parameter unless your change it. That is to say,
the parameter stops tracking updates to the default Security Hub CSPM value,
even if the custom value of the parameter matches the current, default value defined by Security Hub CSPM.
Here's an example for the control **[ACM.1] – Imported and ACM-issued certificates should be renewed
after a specified time period**:

```
{
    "SecurityControlId": "ACM.1",
    "Parameters": {
        "daysToExpiration": {
            "ValueType": "CUSTOM",
            "Value": {
                "Integer": 30
            }
        }
    }
}
```

In the preceding example, the `daysToExpiration` parameter has a custom value of `30`. The current
default value for this parameter is also `30`. If Security Hub CSPM changes the default value to `14`, the parameter in this
example won't track that change. It will retain a value of `30`.

If you want to track updates to the default Security Hub CSPM value for a parameter, set the `ValueType` field to `DEFAULT`
instead of `CUSTOM`. For more information, see
[Reverting to default control parameters in a single
account and Region](revert-default-parameter-values.md#revert-default-parameter-values-local-config "revert-default-parameter-values.md#revert-default-parameter-values-local-config").

## Controls that support custom parameters

For a list of security controls that support custom parameters, see the
**Controls** page of the Security Hub CSPM console or the [Control reference for Security Hub CSPM](securityhub-controls-reference.md "securityhub-controls-reference.md"). To retrieve this list programmatically, you can use the
[ListSecurityControlDefinitions](../../1.0/APIReference/API_ListSecurityControlDefinitions.md "../../1.0/APIReference/API_ListSecurityControlDefinitions.md") operation. In the response, the `CustomizableProperties` object indicates
which controls support customizable parameters.
