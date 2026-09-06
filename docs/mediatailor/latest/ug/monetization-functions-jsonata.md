

# JSONata expression reference for Functions
<a name="monetization-functions-jsonata"></a>

This page is a complete reference for the expression syntax, operators, and functions available in Functions. Use it when you write expressions for output blocks, URL fields, header values, body templates, and run conditions.

## Expression delimiters
<a name="monetization-functions-jsonata-delimiters"></a>

Every value you define in a function is either a constant or an expression — not a mix of both. MediaTailor distinguishes between the two based on delimiters.


| Syntax | Type | Evaluation | 
| --- | --- | --- | 
| https://ads.example.com/vast | Constant | Returned as-is with no evaluation. | 
| {%session.client\_ip%} | Expression | Evaluated at runtime. The result replaces the entire value. | 
| GET | Constant | Returned as-is. | 
| {%'https://ads.example.com/vast?ip=' & session.client\_ip%} | Expression | Evaluated at runtime. | 

**Important**  
A value is either entirely a constant or entirely an expression. You cannot mix the two in a single value. For example, `hello {%'world'%}` is not valid. To combine static text with dynamic values, use string concatenation inside the expression: `{%'hello ' & 'world'%}`.

## Language basics
<a name="monetization-functions-jsonata-basics"></a>

### Dot notation for path navigation
<a name="monetization-functions-jsonata-dot-notation"></a>

Use dot notation to traverse the input data. Each dot descends one level into the object hierarchy.

```
session.client_ip              → the viewer's IP address
response.body.envelope         → a field inside a parsed JSON response
player_params.campaign_id      → a player parameter
```

Missing fields return `null` without raising an error:

```
temp.nonExistent               → null
temp.nonExistent.deeply.nested → null
```

### String concatenation with `&`
<a name="monetization-functions-jsonata-concat"></a>

The `&` operator joins two string values. Non-string values are converted to strings automatically.

```
'https://ads.example.com/vast?ip=' & session.client_ip
→ "https://ads.example.com/vast?ip=192.0.2.1"

'duration=' & 30
→ "duration=30"
```

### Conditional (ternary) expressions
<a name="monetization-functions-jsonata-ternary"></a>

Use the ternary operator to return one of two values based on a condition.

```
condition ? value_if_true : value_if_false
```

Examples:

```
$exists(player_params.env) ? player_params.env : 'prod'
response.statusCode = 200 ? response.body.id : 'unknown'
$random() > 0.5 ? 'groupA' : 'groupB'
```

You can nest ternary expressions for multi-way branching:

```
$contains(session.user_agent, 'CTV') ? 'ctv'
  : $contains(session.user_agent, 'Mobile') ? 'mobile'
  : 'desktop'
```

### Variable binding with `:=`
<a name="monetization-functions-jsonata-binding"></a>

Use the `:=` operator inside parentheses to assign intermediate values within an expression. Bound variables are scoped to the enclosing parentheses and do not persist outside the expression.

```
(
  $base := 'https://ads.example.com';
  $base & '/vast?ip=' & session.client_ip
)
```

Semicolons separate statements inside parentheses. The last statement is the return value of the expression.

```
(
  $code := response.statusCode;
  $code != null and $code >= 200 and $code < 300
    ? response.body.value
    : 'fallback'
)
```

## Operators
<a name="monetization-functions-jsonata-operators"></a>

### Arithmetic
<a name="monetization-functions-jsonata-operators-arithmetic"></a>


| Operator | Description | Example | Result | 
| --- | --- | --- | --- | 
| \+ | Addition | 5 \+ 3 | 8 | 
| - | Subtraction | 10 - 4 | 6 | 
| \* | Multiplication | 6 \* 7 | 42 | 
| / | Division | 15 / 4 | 3.75 | 
| % | Modulo | 17 % 5 | 2 | 

**Important**  
Input values from player parameters and session data arrive as strings. Use `$number()` to convert them before numeric comparisons or arithmetic. Comparing a string to a number produces unexpected results.

### Comparison
<a name="monetization-functions-jsonata-operators-comparison"></a>


| Operator | Description | Example | Result | 
| --- | --- | --- | --- | 
| = | Equal to | response.statusCode = 200 | true | 
| \!= | Not equal to | player\_params.region \!= 'us-east-1' | true if not us-east-1 | 
| < | Less than | avail.index < 3 | true if below 3 | 
| > | Greater than | $number(player\_params.age) > 18 | true if over 18 | 
| <= | Less than or equal | $count(items) <= 10 | true if 10 or fewer | 
| >= | Greater than or equal | response.statusCode >= 400 | true if error status | 

### Boolean
<a name="monetization-functions-jsonata-operators-boolean"></a>


| Operator | Description | Example | 
| --- | --- | --- | 
| and | Logical AND | response.statusCode = 200 and $exists(response.body.id) | 
| or | Logical OR | player\_params.region = 'us-east-1' or player\_params.region = 'us-west-2' | 

Use parentheses for precedence:

```
score > 0.5 and (tier = 'premium' or tier = 'gold')
```

**Note**  
Use `$not()` for logical negation. There is no `not` keyword operator.

### Membership (`in`)
<a name="monetization-functions-jsonata-operators-membership"></a>

The `in` operator tests whether a value exists in an array.

```
'premium' in segments     → true if segments contains 'premium'
player_params.region in ['us-east-1', 'us-west-2']  → true
```

### Chaining (`~>`)
<a name="monetization-functions-jsonata-operators-chaining"></a>

The chaining operator passes the result of the left-hand expression as the first argument to the function on the right.

```
session.user_agent ~> $lowercase ~> $trim
→ equivalent to $trim($lowercase(session.user_agent))
```

## Allowed functions
<a name="monetization-functions-jsonata-allowed"></a>

MediaTailor supports the following built-in functions. Any function not listed here is blocked and causes a validation error when you create or update a function.

### Type conversion (3)
<a name="monetization-functions-jsonata-allowed-type"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $string(value) | Convert to string | $string(200) | "200" | 
| $number(value) | Convert to number | $number('42') | 42 | 
| $boolean(value) | Convert to boolean | $boolean(1) | true | 

### Introspection (4)
<a name="monetization-functions-jsonata-allowed-introspection"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $length(string) | String length | $length('hello') | 5 | 
| $count(array) | Array element count | $count([1, 2, 3]) | 3 | 
| $exists(value) | Check if value exists (not undefined) | $exists(temp.id) | true or false | 
| $keys(object) | Get object key names | $keys(response.body) | ["id", "name"] | 

### Numeric (7)
<a name="monetization-functions-jsonata-allowed-numeric"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $sum(array) | Sum of array | $sum([1, 2, 3]) | 6 | 
| $max(array) | Maximum value | $max([10, 5, 20]) | 20 | 
| $min(array) | Minimum value | $min([10, 5, 20]) | 5 | 
| $average(array) | Arithmetic mean | $average([10, 20, 30]) | 20 | 
| $abs(number) | Absolute value | $abs(-7) | 7 | 
| $floor(number) | Round down | $floor(3.9) | 3 | 
| $round(number, precision) | Round to precision | $round(3.456, 2) | 3.46 | 

### String (7)
<a name="monetization-functions-jsonata-allowed-string"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $uppercase(string) | To uppercase | $uppercase('hello') | "HELLO" | 
| $lowercase(string) | To lowercase | $lowercase('Hello') | "hello" | 
| $trim(string) | Remove leading/trailing whitespace | $trim(' hi ') | "hi" | 
| $substring(string, start, length) | Extract substring (zero-based) | $substring('abcdef', 2, 3) | "cde" | 
| $contains(string, pattern) | Check if string contains pattern | $contains(session.user\_agent, 'CTV') | true or false | 
| $match(string, pattern) | Match string against regex pattern | $match('abc-123', /[0-9]\+/) | {"match": "123", ...} | 
| $replace(string, pattern, replacement) | Replace matching pattern | $replace('hello', 'l', 'r') | "herro" | 

### Array (5)
<a name="monetization-functions-jsonata-allowed-array"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $append(arr1, arr2) | Concatenate arrays | $append([1, 2], [3, 4]) | [1, 2, 3, 4] | 
| $reverse(array) | Reverse order | $reverse([1, 2, 3]) | [3, 2, 1] | 
| $sort(array) | Sort array | $sort([3, 1, 2]) | [1, 2, 3] | 
| $distinct(array) | Remove duplicates | $distinct([1, 2, 2, 3]) | [1, 2, 3] | 
| $map(array, func) | Apply function to each element | $map([1,2,3], function($v){$v\*2}) | [2, 4, 6] | 

### Boolean (1)
<a name="monetization-functions-jsonata-allowed-boolean"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $not(value) | Logical NOT | $not(false) | true | 

### Random (1)
<a name="monetization-functions-jsonata-allowed-random"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $random() | Random number between 0 (inclusive) and 1 (exclusive) | $random() > 0.5 ? 'A' : 'B' | "A" or "B" | 

**Note**  
`$random()` generates a new value on each evaluation. If you need the same random value in multiple output keys, bind it to a variable first: `($r := $random(); ...)`.

### Date/time (4)
<a name="monetization-functions-jsonata-allowed-datetime"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $now() | Current timestamp as an ISO 8601 string | $now() | "2024-01-15T12:00:00.000Z" | 
| $millis() | Current timestamp as milliseconds since epoch | $millis() | 1705320000000 | 
| $toMillis(string) | Convert ISO 8601 string to milliseconds | $toMillis('2024-01-15T12:00:00.000Z') | 1705320000000 | 
| $fromMillis(number) | Convert milliseconds to ISO 8601 string | $fromMillis(1705320000000) | "2024-01-15T12:00:00.000Z" | 

### Encoding (6)
<a name="monetization-functions-jsonata-allowed-encoding"></a>


| Function | Description | Example | 
| --- | --- | --- | 
| $encodeUrl(string) | URL encode (preserves structural characters like /, ?, &) | $encodeUrl('https://example.com/path?q=hello world') | 
| $encodeUrlComponent(string) | URL encode a single component (encodes all special characters) | $encodeUrlComponent('a&b=c') → "a%26b%3Dc" | 
| $decodeUrl(string) | Decode a URL-encoded string | $decodeUrl('hello%20world') → "hello world" | 
| $decodeUrlComponent(string) | Decode a URL-encoded component | $decodeUrlComponent('a%26b') → "a&b" | 
| $base64encode(string) | Encode to Base64 | $base64encode('hello') → "aGVsbG8=" | 
| $base64decode(string) | Decode from Base64 | $base64decode('aGVsbG8=') → "hello" | 

**Tip**  
Use `$encodeUrlComponent()` for individual query parameter values. Use `$encodeUrl()` only when you need to encode a full URL while preserving its structure.

## Common patterns
<a name="monetization-functions-jsonata-patterns"></a>

### Fallback values
<a name="monetization-functions-jsonata-patterns-fallback"></a>

Provide a default when a value might not exist.

```
{%$exists(player_params.region) ? player_params.region : 'us-east-1'%}
```

### Dynamic URL construction
<a name="monetization-functions-jsonata-patterns-url"></a>

Build an ad decision server URL from multiple inputs.

```
{%'https://ads.example.com/v1/vast?ip=' & $encodeUrlComponent(session.client_ip) & '&ua=' & $encodeUrlComponent(session.user_agent) & '&sid=' & session.id%}
```

### Status code checks for HTTP\_REQUEST output
<a name="monetization-functions-jsonata-patterns-status"></a>

Guard output values against HTTP failures.

```
{%response.statusCode != null and response.statusCode = 200 ? response.body.envelope : 'default-envelope'%}
```

### Numeric conversion from player parameters
<a name="monetization-functions-jsonata-patterns-numeric"></a>

Player parameters arrive as strings. Convert them before arithmetic or numeric comparisons.

```
{%$number(player_params.max_duration) > 30 ? 'long' : 'short'%}
```

**Important**  
If `$number()` receives a non-numeric string, it returns `undefined`. Combine it with `$exists()` when the parameter might be missing or invalid: `($val := $number(player_params.max_duration); $exists($val) and $val > 30 ? 'long' : 'short')`.

### Random traffic split
<a name="monetization-functions-jsonata-patterns-random"></a>

Assign viewers to experiment groups using `$random()`.

```
{%$random() > 0.5 ? 'https://ads.example.com/v1/vast-a' : 'https://ads.example.com/v1/vast-b'%}
```

### Device type classification
<a name="monetization-functions-jsonata-patterns-device"></a>

Classify devices based on the user agent string.

```
{%$contains(session.user_agent, 'CTV') ? 'ctv' : $contains(session.user_agent, 'Mobile') ? 'mobile' : 'desktop'%}
```