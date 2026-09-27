

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# How Parameter Store authorizes parameter retrieval
<a name="ps-retrieval-authorization"></a>

Four Parameter Store operations can return a parameter value, and each one is authorized against its own IAM action. Three of them authorize against the parameters named in the request. `GetParametersByPath` is the exception: it authorizes against the path in the request rather than against the parameters it returns.



| Operation | IAM action authorized | Resource authorized against | 
| --- | --- | --- | 
| [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html) | ssm:GetParameter | The requested parameter | 
| [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html) | ssm:GetParameters | Each requested parameter | 
| [GetParameterHistory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameterHistory.html) | ssm:GetParameterHistory | The requested parameter | 
| [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html) | ssm:GetParametersByPath | The path specified in the request, not the parameters returned | 

Two consequences of this model are important when you design restrictive policies.

**Each action is authorized independently**  
Parameter Store authorizes each retrieval operation against its own IAM action. Denying `ssm:GetParameter` has no effect on calls to `ssm:GetParameters`, `ssm:GetParametersByPath`, or `ssm:GetParameterHistory`. To restrict access to a parameter value, deny every action that can return it.

Because all four action names begin with `GetParameter`, the wildcard pattern `ssm:GetParameter*` covers them in a single statement. For examples, see [Denying permissions](parameter-store-setting-up.md#sysman-paramstore-deny-permissions).

**`GetParametersByPath` is authorized against the requested path**  
This means resource-level denies on an individual parameter don't limit what a path query returns. If you use parameter hierarchies to separate environments or application tiers, apply your controls to the paths themselves.

**Important**  
Parameter Store authorizes the `GetParametersByPath` operation against the path that you specify in the request, not against each parameter that the operation returns. A principal who is allowed to call `GetParametersByPath` for the path `/a` receives every parameter under that path, including `/a/b`. This is true even if the same policy explicitly denies access to `/a/b` for other actions.  
To prevent a parameter from being returned by `GetParametersByPath`, deny the `ssm:GetParametersByPath` action on every ancestor path that could include the parameter in its results. For example, to prevent `/a/b` from being returned, deny `ssm:GetParametersByPath` for both `/a` and `/`.

The same pattern applies to deletion. [DeleteParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameters.html) is authorized against `ssm:DeleteParameters`, not against `ssm:DeleteParameter`. To prevent a principal from deleting a parameter, deny both actions.

**Note**  
Parameter Store operations are recorded in AWS CloudTrail. If you want to review which operations have been used to retrieve a parameter in your account, see [Auditing and logging Parameter Store activity](parameter-store-logging-auditing.md).