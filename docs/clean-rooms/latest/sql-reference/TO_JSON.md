# TO_JSON function

The TO_JSON function converts an input expression into a JSON string representation. The
function handles the conversion of different data types (such as numbers, strings, and
booleans) into their corresponding JSON representations.

The TO_JSON function is useful when you need to convert structured data (such as
database rows or JSON objects) into a more portable, self-describing format like JSON. This
can be particularly helpful when you need to interact with other systems or services that
expect JSON-formatted data.

## Syntax

```
to_json(expr[, options])
```

## Arguments

_expr_

The input expression that you want to convert to a JSON string. It can be a
value, a column, or any other valid SQL expression.

_options_

An optional set of configuration options that can be used to customize the
JSON conversion process. These options may include things like the handling of
null values, the representation of numeric values, and the treatment of special
characters..

## Returns

Returns a JSON string with a given struct value

## Examples

The following example converts a named struct (a type of structured data) into a JSON
string. The first argument `(named_struct('a', 1, 'b', 2)`) is the input
expression that is passed to the `to_json()` function. It creates a named
struct with two fields: "a" with a value of 1, and "b" with a value of 2. The to_json()
function takes the named struct as its argument and converts it into a JSON string
representation. The output is `{"a":1,"b":2}`, which is a valid JSON string
that represented the named struct.

```
SELECT to_json(named_struct('a', 1, 'b', 2));
 {"a":1,"b":2}
```

The following example converts a named struct that contains a timestamp value into a
JSON string, with a customized timestamp format. The first argument
(`named_struct('time', to_timestamp('2015-08-26', 'yyyy-MM-dd'))`) creates
a named struct with a single field 'time' that contains the timestamp value. The second
argument (`map('timestampFormat', 'dd/MM/yyyy')`) creates a map (key-value
dictionary) with a single key-value pair, where the key is 'timestampFormat' and the
value is 'dd/MM/yyyy'. This map is used to specify the desired format for the timestamp
value when converting it to JSON. The to_json() function converts the named struct into
a JSON string. The second argument, the map, is used to customize the timestamp format
to 'dd/MM/yyyy'. The output is `{"time":"26/08/2015"}`, which is a JSON
string with a single field 'time' that contains the timestamp value in the desired
'dd/MM/yyyy' format.

```
SELECT to_json(named_struct('time', to_timestamp('2015-08-26', 'yyyy-MM-dd')), map('timestampFormat', 'dd/MM/yyyy'));
 {"time":"26/08/2015"}
```
