

# Amazon SNS subscription filter policy scope
<a name="sns-message-filtering-scope"></a>

The `FilterPolicyScope` subscription attribute allows you define the filtering scope by setting one of the following values:
+ `MessageAttributes` – Applies the filter policy to message attributes (default setting).
+ `MessageBody` – Applies the filter policy to the message body.

**Note**  
If no filter policy scope is defined for an existing filter policy, the scope defaults to `MessageAttributes`.