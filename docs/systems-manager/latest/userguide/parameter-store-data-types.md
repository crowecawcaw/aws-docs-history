

# Parameter data types in Parameter Store
<a name="parameter-store-data-types"></a>

When you create or update a parameter, you can specify a *data type* to tell Parameter Store how to validate the parameter value. For most data types, Parameter Store validates the value during the `PutParameter` operation and rejects values that don't conform. The exception is `aws:ec2:image`. For this data type, Parameter Store validates the value asynchronously. For more information, see [Using native parameter support in Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md).

The default data type is `text`, which performs no validation. You can change an existing parameter from one data type to another, such as from `text` to `integer` or from `integer` to `float`. The exceptions are `aws:ec2:image` and `aws:ssm:integration`. You can't change a parameter to or from either of these data types.

Validation applies to every supported parameter type for a given data type. Most data types support `String` and `SecureString`. Some data types also support `StringList`. For a `StringList` parameter, Parameter Store validates each item in the list. If any item is invalid, the whole request fails. For the parameter types that each data type supports, see [Supported data types](#parameter-store-data-types-table).

Parameter Store API operations that retrieve parameters always return the value as a string, regardless of data type. These operations include `GetParameter`, `GetParameters`, and `GetParametersByPath`. For example, if a parameter has the data type `integer` and the value `443`, `GetParameter` returns the value as the string `"443"`. Convert the value to the type that your application needs after you retrieve it.

**Note**  
You can use the `AllowedPattern` parameter constraint together with a predefined data type. If you specify both, the parameter value must pass the data type validation and match the allowed pattern.

## Supported data types
<a name="parameter-store-data-types-table"></a>

Data types listed as *Advanced only* in the following table require the parameter to be an advanced parameter:
+ If you create a standard parameter with one of these data types, the request fails.
+ If you use Intelligent-Tiering, Parameter Store creates the parameter as an advanced parameter.
+ If you change the data type of an existing standard parameter to one of these data types, you must also change the parameter to the advanced tier, or the request fails. If you use Intelligent-Tiering, Parameter Store upgrades the parameter to the advanced tier automatically. On the console, you must choose **Switch to advanced**. For more information, see [Default tier and individual parameter tier settings](parameter-store-advanced-parameters.md#parameter-store-tier-settings-overview).

The following table lists the data types that you can assign to parameters.


**Parameter data types**  

| Data type | Validation | Notes | 
| --- | --- | --- | 
| `text`<br />Parameter types: `String`, `StringList`, `SecureString`<br />Tier: Standard or Advanced | None (default) | The default data type. Use it for values that don't need validation. | 
| `aws:ec2:image`<br />Parameter types: `String`<br />Tier: Standard or Advanced | Valid Amazon Machine Image (AMI) ID format and AMI availability | Validated asynchronously. For more information, see [Using native parameter support in Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md). | 
| `aws:ssm:integration`<br />Parameter types: `SecureString`<br />Tier: Standard or Advanced | Valid Systems Manager integration definition | Used for Systems Manager Automation webhook integrations. For more information, see [Creating webhook integrations for Automation](creating-webhook-integrations.md). | 
| `aws:region`<br />Parameter types: `String`, `SecureString`<br />Tier: Standard or Advanced | Name of a launched AWS Region, including opt-in Regions | Example: `us-east-1` | 
| `aws:account:id`<br />Parameter types: `String`, `StringList`, `SecureString`<br />Tier: Standard or Advanced | AWS account ID format (12 digits) | Parameter Store checks only the format. It doesn't confirm that the account exists. The hyphenated form shown on the console (`1111-2222-3333`) isn't valid. Example: `111122223333` | 
| `boolean`<br />Parameter types: `String`, `SecureString`<br />Tier: Standard or Advanced | Boolean value: `true`, `True`, `TRUE`, `false`, `False`, `FALSE`, `0`, or `1` | Valid values are `0`, `1`, and `true` or `false` in all lowercase, all uppercase, or with only an initial capital letter. Other capitalizations, such as `tRue`, aren't valid. Examples: `true`, `FALSE`, `1` | 
| `integer`<br />Parameter types: `String`, `SecureString`<br />Tier: Standard or Advanced | Signed 32-bit integer (`-2147483648` to `2147483647`), with no leading zeros, plus sign, or decimal point | Values such as `007`, `+7`, `7.0`, and `5000000000` aren't valid. Examples: `443`, `-42` | 
| `float`<br />Parameter types: `String`, `SecureString`<br />Tier: Standard or Advanced | Floating-point value (negative values and exponent notation allowed) | The value must be representable as a 64-bit IEEE 754 floating-point number. `NaN`, `Infinity`, and values that overflow or round to zero (such as `1e-999`) aren't valid. Examples: `3.14`, `-0.5`, `1e5` | 
| `binary`<br />Parameter types: `String`, `SecureString`<br />Tier: Standard or Advanced | Binary value that contains only the digits `0` and `1` | The value can contain only the digits `0` and `1`. This data type doesn't accept base64-encoded data. There's no length limit beyond the parameter value size, and leading zeros are kept (`0011` is valid). Example: `101101` | 
| `hostname`<br />Parameter types: `String`, `SecureString`<br />Tier: Standard or Advanced | Valid host name (single-label names such as `myhost` are allowed) | Underscores aren't allowed, so DNS names such as `_dmarc.example.com` aren't valid. IP addresses aren't valid host names. Internationalized names must use punycode (`xn--`). Examples: `www.example.com`, `myhost` | 
| `email`<br />Parameter types: `String`, `StringList`, `SecureString`<br />Tier: Standard or Advanced | Valid email address | The value must be a bare address. Display names (`Mary <mary@example.com>`) and quoted local parts aren't accepted, and the domain must have at least two labels. Example: `mary_major@example.com` | 
| `ipv4-address`<br />Parameter types: `String`, `StringList`, `SecureString`<br />Tier: Standard or Advanced | Valid IPv4 address | The value must be a single address. CIDR prefixes (`10.0.0.0/16`) and ports aren't accepted. Leading zeros (`192.168.001.1`) aren't valid. Example: `192.0.2.1` | 
| `ipv6-address`<br />Parameter types: `String`, `StringList`, `SecureString`<br />Tier: Standard or Advanced | Valid IPv6 address (compressed form allowed) | The value must be a single address. CIDR prefixes and ports aren't accepted. Zone IDs and brackets aren't accepted, and the value isn't normalized. Examples: `2001:db8:0:0:0:0:0:1`, `2001:db8::1` | 
| `url`<br />Parameter types: `String`, `SecureString`<br />Tier: Advanced only | Valid URL format, including the scheme (protocol) and host | Any scheme is accepted, but the URL must include a host, so `mailto:` and `file:///` URLs aren't valid. URLs that contain a password (`user:password@host`) aren't valid. Example: `https://example.com` | 
| `json`<br />Parameter types: `String`, `SecureString`<br />Tier: Advanced only | Valid JSON. The top-level value must be an object or an array, and duplicate keys aren't allowed. The maximum nesting depth is 64. | Scalar values, such as `42` or `"abc"`, aren't valid. Example: `{"port": 443}` | 
| `jsonc`<br />Parameter types: `String`, `SecureString`<br />Tier: Advanced only | Valid JSON. The top-level value must be an object or an array, and duplicate keys aren't allowed. Line (`//`) and block (`/* */`) comments are allowed. The maximum nesting depth is 64. | Scalar values, such as `42` or `"abc"`, aren't valid. Trailing commas aren't allowed. Comments are stored and returned as written, so use a JSONC-aware parser to read the value. Example: `{"port": 443 /* HTTPS */}` | 

## Example: Creating a parameter with a data type
<a name="parameter-store-data-types-cli-example"></a>

The following AWS CLI example creates a `String` parameter with the data type `integer` and the value `443`.

------
#### [ Linux & macOS ]

```
aws ssm put-parameter \
    --name "/myapp/config/port" \
    --value "443" \
    --type String \
    --data-type "integer"
```

------
#### [ Windows ]

```
aws ssm put-parameter ^
    --name "/myapp/config/port" ^
    --value "443" ^
    --type String ^
    --data-type "integer"
```

------

If you specify a value that doesn't conform to the data type's rules, the command fails and returns an error. For example, the command fails if you specify `--data-type "integer"` with the value `"abc"`.