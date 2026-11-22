

# Allowed built-in functions

Elemental Inference allows the following built-in functions in both expressions. A call to any other built-in fails the evaluation. Elemental Inference rejects such a call when you save the function, except in the response expression of a model function, where it fails at run time. For more information, see [Writing function expressions](functions-expressions.md).

## Type conversion
<a name="functions-jsonata-allowed-type"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $string(value) | Converts a value to a string. Serializes an object or array. | $string(200) | "200" | 
| $number(value) | Converts a value to a number. | $number("42") | 42 | 
| $boolean(value) | Converts a value to a Boolean. | $boolean(1) | true | 

## Introspection
<a name="functions-jsonata-allowed-introspection"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $length(string) | Returns the length of a string. | $length("hello") | 5 | 
| $count(array) | Returns the number of elements in an array. | $count(media.frames) | 4 | 
| $exists(value) | Tests whether a value exists. | $exists(media.contextual.scene.summary) | true or false | 
| $keys(object) | Returns the key names of an object. | $keys(media.contextual) | ["shot", "scene"] | 

## String
<a name="functions-jsonata-allowed-string"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $uppercase(string) | Converts a string to uppercase. | $uppercase("hello") | "HELLO" | 
| $lowercase(string) | Converts a string to lowercase. | $lowercase("Hello") | "hello" | 
| $trim(string) | Removes leading and trailing whitespace. | $trim(" hi ") | "hi" | 
| $substring(string, start, length) | Extracts a substring. Positions start at zero. | $substring("abcdef", 2, 3) | "cde" | 
| $contains(string, pattern) | Tests whether a string contains a pattern. | $contains(media.transcript, "penalty") | true or false | 
| $match(string, pattern) | Matches a string against a regular expression. | $match("abc-123", /[0-9]\+/) | The match details | 
| $replace(string, pattern, replacement) | Replaces the matches of a pattern. | $replace("hello", "l", "r") | "herro" | 
| $split(string, separator) | Splits a string into an array. | $split("a,b,c", ",") | ["a", "b", "c"] | 
| $join(array, separator) | Joins an array into a string. | $join(media.contextual.shot.objects, ", ") | "ball, goal net" | 

**Note**  
Regular expressions use RE2 syntax, which doesn't support backreferences or lookaround.

## Numeric
<a name="functions-jsonata-allowed-numeric"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $sum(array) | Returns the sum of the values. | $sum([1, 2, 3]) | 6 | 
| $max(array) | Returns the largest value. | $max([10, 5, 20]) | 20 | 
| $min(array) | Returns the smallest value. | $min([10, 5, 20]) | 5 | 
| $average(array) | Returns the arithmetic mean. | $average([10, 20, 30]) | 20 | 
| $abs(number) | Returns the absolute value. | $abs(-7) | 7 | 
| $floor(number) | Rounds a number down. | $floor(3.9) | 3 | 
| $round(number, precision) | Rounds a number to a precision. | $round(3.456, 2) | 3.46 | 

## Array
<a name="functions-jsonata-allowed-array"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $append(array1, array2) | Concatenates two arrays. This is the usual way to put prompt text before mapped media. | $append([1, 2], [3, 4]) | [1, 2, 3, 4] | 
| $reverse(array) | Reverses the order of an array. | $reverse([1, 2, 3]) | [3, 2, 1] | 
| $sort(array) | Sorts an array. | $sort([3, 1, 2]) | [1, 2, 3] | 
| $distinct(array) | Removes duplicate values. | $distinct([1, 2, 2, 3]) | [1, 2, 3] | 
| $map(array, function) | Applies a function to each element. | $map([1,2,3], function($v){$v\*2}) | [2, 4, 6] | 
| $filter(array, function) | Keeps the elements for which the function returns true. | $filter([1,2,3,4], function($v){$v > 2}) | [3, 4] | 
| $reduce(array, function, init) | Reduces an array to one value. | $reduce([1,2,3], function($a,$b){$a\+$b}, 0) | 6 | 

## Object
<a name="functions-jsonata-allowed-object"></a>


| Function | Description | Example | Result | 
| --- | --- | --- | --- | 
| $merge(array) | Merges an array of objects into one object. | $merge([{"a":1}, {"b":2}]) | {"a":1,"b":2} | 
| $lookup(object, key) | Reads a value by key name. | $lookup(media.contextual.scene, "summary") | The value of summary | 
| $each(object, function) | Applies a function to each key-value pair. | $each({"a":1}, function($v,$k){$k & "=" & $v}) | ["a=1"] | 

## Boolean, encoding, date and time, and JSON
<a name="functions-jsonata-allowed-other"></a>


| Function | Description | Example | 
| --- | --- | --- | 
| $not(value) | Returns the logical NOT of a value. | $not($exists(media.transcript)) | 
| $random() | Returns a random number from 0 up to but not including 1. | $random() > 0.5 ? "a" : "b" | 
| $encodeUrl(string) | URL-encodes a string, preserving structural characters such as / and ?. | $encodeUrl("https://example.com/a b") | 
| $encodeUrlComponent(string) | URL-encodes one component, encoding all special characters. | $encodeUrlComponent("a&b=c") | 
| $decodeUrl(string) | Decodes a URL-encoded string. | $decodeUrl("a%20b") | 
| $decodeUrlComponent(string) | Decodes a URL-encoded component. | $decodeUrlComponent("a%26b") | 
| $base64encode(string) | Encodes a string to Base64. | $base64encode("hello") | 
| $base64decode(string) | Decodes a string from Base64. | $base64decode("aGVsbG8=") | 
| $now() | Returns the current time as an ISO 8601 string. | $now() | 
| $millis() | Returns the current time in milliseconds since the epoch. | $millis() | 
| $toMillis(string) | Converts an ISO 8601 string to milliseconds. | $toMillis("2026-01-15T12:00:00.000Z") | 
| $fromMillis(number) | Converts milliseconds to an ISO 8601 string. | $fromMillis(1768478400000) | 
| $parse(string) | Parses a JSON string into data. Use it in a response expression when you asked the model for JSON. | $parse(content[type = "text"][0].text) | 

**Note**  
`$random()` produces a new value each time it is evaluated. To use the same value in two places, bind it first: `($r := $random(); ...)`.

## Functions that are not allowed
<a name="functions-jsonata-not-allowed"></a>

Any built-in that isn't listed in the preceding tables is blocked, including `$pad()` and `$eval()`. `$pad()` can allocate an unbounded amount of memory inside a single call, and `$eval()` would let an expression build and run new code at run time.

The transform operator (`~> | {{location}} | {{update}} |`) is also unavailable, because it calls `$clone()`, which isn't allowed. Build the object you want with an object constructor or `$merge()` instead.