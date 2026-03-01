# AWS AppSync resolver mapping template programming guide

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

This is a cookbook-style tutorial of programming with the Apache Velocity Template
Language (VTL) in AWS AppSync. If you are familiar with other programming languages such as
JavaScript, C, or Java, it should be fairly straightforward.

AWS AppSync uses VTL to translate GraphQL requests from clients into a request to your data
source. Then it reverses the process to translate the data source response back into a
GraphQL response. VTL is a logical template language that gives you the power to manipulate
both the request and the response in the standard request/response flow of a web
application, using techniques such as:

- Default values for new items
- Input validation and formatting
- Transforming and shaping data
- Iterating over lists, maps, and arrays to pluck out or alter values
- Filter/change responses based on user identity
- Complex authorization checks
  For example, you might want to perform a phone number validation in the service on a
  GraphQL argument, or convert an input parameter to upper case before storing it in DynamoDB. Or
  maybe you want client systems to provide a code, as part of a GraphQL argument, JWT token
  claim, or HTTP header, and only respond with data if the code matches a specific string in a
  list. These are all logical checks you can perform with VTL in AWS AppSync.

VTL allows you to apply logic using programming techniques that might be familiar.
However, it is bounded to run within the standard request/response flow to ensure that your
GraphQL API is scalable as your user base grows. Because AWS AppSync also supports AWS Lambda
as a resolver, you can write Lambda functions in your programming language of choice (Node.js,
Python, Go, Java, etc.) if you need more flexibility.

## Setup

A common technique when learning a language is to print out results (for example,
`console.log(variable)` in JavaScript) to see what happens. In this
tutorial, we demonstrate this by creating a simple GraphQL schema and passing a map of
values to a Lambda function. The Lambda function prints out the values and then responds
with them. This will enable you to understand the request/response flow and see
different programming techniques.

Start by creating the following GraphQL schema:

```
type Query {
    get(id: ID, meta: String): Thing
}

type Thing {
    id: ID!
    title: String!
    meta: String
}

schema {
    query: Query
}
```

Now create the following AWS Lambda function, using Node.js as the language:

```
exports.handler = (event, context, callback) => {
    console.log('VTL details: ', event);
    callback(null, event);
};
```

In the **Data Sources** pane of the AWS AppSync console,
add this Lambda function as a new data source. Navigate back to the **Schema** page of the console and click the **ATTACH** button on the right, next to the
`get(...):Thing` query. For the request template, choose the existing
template from the **Invoke and forward arguments** menu.
For the response template, choose **Return Lambda
result**.

Open Amazon CloudWatch Logs for your Lambda function in one location, and from the **Queries** tab of the AWS AppSync console, run the following
GraphQL query:

```
query test {
  get(id:123 meta:"testing"){
    id
    meta
  }
}
```

The GraphQL response should contain `id:123` and `meta:testing`,
because the Lambda function is echoing them back. After a few seconds, you should see a
record in CloudWatch Logs with these details as well.

## Variables

VTL uses [references](https://velocity.apache.org/engine/1.7/user-guide.html#references "https://velocity.apache.org/engine/1.7/user-guide.html#references"), which you can use to store or manipulate data. There are three
types of references in VTL: variables, properties, and methods. Variables have a
`$` sign in front of them and are created with the `#set`
directive:

```
#set($var = "a string")
```

Variables store similar types that you’re familiar with from other languages, such as
numbers, strings, arrays, lists, and maps. You might have noticed a JSON payload being
sent in the default request template for Lambda resolvers:

```
"payload": $util.toJson($context.arguments)
```

A couple of things to notice here - first, AWS AppSync provides several convenience
functions for common operations. In this example, `$util.toJson` converts a
variable to JSON. Second, the variable `$context.arguments` is automatically
populated from a GraphQL request as a map object. You can create a new map as
follows:

```
#set( $myMap = {
  "id": $context.arguments.id,
  "meta": "stuff",
  "upperMeta" : $context.arguments.meta.toUpperCase()
} )
```

You have now created a variable named `$myMap`, which has keys of
`id`, `meta`, and `upperMeta`. This also
demonstrates a few things:

- `id` is populated with a key from the GraphQL arguments. This is
  common in VTL to grab arguments from clients.
- `meta` is hardcoded with a value, showcasing default values.
- `upperMeta` is transforming the `meta` argument using a
  method `.toUpperCase()`.

Put the previous code at the top of your request template and change the
`payload` to use the new `$myMap` variable:

```
"payload": $util.toJson($myMap)
```

Run your Lambda function, and you can see the response change as well as this data in
CloudWatch logs. As you walk through the rest of this tutorial, we will keep populating
`$myMap` so you can run similar tests.

You can also set _properties\__ on your
variables. These could be simple strings, arrays, or JSON:

```
#set($myMap.myProperty = "ABC")
#set($myMap.arrProperty = ["Write", "Some", "GraphQL"])
#set($myMap.jsonProperty = {
    "AppSync" : "Offline and Realtime",
    "Cognito" : "AuthN and AuthZ"
})
```

### Quiet references

Because VTL is a templating language, by default, every reference you give it will
do a `.toString()`. If the reference is undefined, it prints the actual
reference representation, as a string. For example:

```
#set($myValue = 5)
##Prints '5'
$myValue

##Prints '$somethingelse'
$somethingelse
```

To address this, VTL has a _quiet reference_ or
_silent reference_ syntax, which tells the template engine to
suppress this behavior. The syntax for this is `$!{}`. For example, if we
changed the previous code slightly to use `$!{somethingelse}`, the
printing is suppressed:

```
#set($myValue = 5)
##Prints '5'
$myValue

##Nothing prints out
$!{somethingelse}
```

## Calling methods

In an earlier example, we showed you how to create a variable and simultaneously set
values. You can also do this in two steps by adding data to your map as shown
following:

```
#set ($myMap = {})
#set ($myList = [])

##Nothing prints out
$!{myMap.put("id", "first value")}
##Prints "first value"
$!{myMap.put("id", "another value")}
##Prints true
$!{myList.add("something")}
```

**HOWEVER** there is something to know about this behavior.
Although the quiet reference notation `$!{}` allows you to call methods, as
above, it won’t suppress the returned value of the executed method. This is why we noted
`##Prints "first value"` and `##Prints true` above. This can
cause errors when you’re iterating over maps or lists, such as inserting a value where a
key already exists, because the output adds unexpected strings to the template upon
evaluation.

The workaround to this is sometimes to call the methods using a `#set`
directive and ignore the variable. For example:

```
#set ($myMap = {})
#set($discard = $myMap.put("id", "first value"))
```

You might use this technique in your templates, as it prevents the unexpected strings
from being printed in the template. AWS AppSync provides an alternative convenience
function that offers the same behavior in a more succinct notation. This enables you to
not have to think about these implementation specifics. You can access this function
under `$util.quiet()` or its alias `$util.qr()`. For
example:

```
#set ($myMap = {})
#set ($myList = [])

##Nothing prints out
$util.quiet($myMap.put("id", "first value"))
##Nothing prints out
$util.qr($myList.add("something"))
```

## Strings

As with many programming languages, strings can be difficult to deal with, especially
when you want to build them from variables. There are some common things that come up
with VTL.

Suppose you are inserting data as a string to a data source like DynamoDB, but it is
populated from a variable, like a GraphQL argument. A string will have double quotation
marks, and to reference the variable in a string you just need `"${}"` (so no
`!` as in [quiet reference notation](https://velocity.apache.org/engine/1.7/user-guide.html#quiet-reference-notation "https://velocity.apache.org/engine/1.7/user-guide.html#quiet-reference-notation")). This is similar to a template literal in
JavaScript: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals")

```
#set($firstname = "Jeff")
$!{myMap.put("Firstname", "${firstname}")}
```

You can see this in DynamoDB request templates, like `"author": { "S" :
 "${context.arguments.author}"}` when using arguments from GraphQL clients, or
for automatic ID generation like `"id" : { "S" : "$util.autoId()"}`. This
means that you can reference a variable or the result of a method inside a string to
populate data.

You can also use public methods of the Java [String
class](https://docs.oracle.com/javase/6/docs/api/java/lang/String.html "https://docs.oracle.com/javase/6/docs/api/java/lang/String.html"), such as pulling out a substring:

```
#set($bigstring = "This is a long string, I want to pull out everything after the comma")
#set ($comma = $bigstring.indexOf(','))
#set ($comma = $comma +2)
#set ($substring = $bigstring.substring($comma))

$util.qr($myMap.put("substring", "${substring}"))
```

String concatenation is also a very common task. You can do this with variable
references alone or with static values:

```
#set($s1 = "Hello")
#set($s2 = " World")

$util.qr($myMap.put("concat","$s1$s2"))
$util.qr($myMap.put("concat2","Second $s1 World"))
```

## Loops

Now that you have created variables and called methods, you can add some logic to your
code. Unlike other languages, VTL allows only loops, where the number of iterations is
predetermined. There is no `do..while` in Velocity. This design ensures that
the evaluation process always terminates, and provides bounds for scalability when your
GraphQL operations execute.

Loops are created with a `#foreach` and require you to supply a **loop variable** and an **iterable
object** such as an array, list, map, or collection. A classic programming
example with a `#foreach` loop is to loop over the items in a collection and
print them out, so in our case we pluck them out and add them to the map:

```
#set($start = 0)
#set($end = 5)
#set($range = [$start..$end])

#foreach($i in $range)
   ##$util.qr($myMap.put($i, "abc"))
   ##$util.qr($myMap.put($i, $i.toString()+"foo")) ##Concat variable with string
   $util.qr($myMap.put($i, "${i}foo"))     ##Reference a variable in a string with "${varname}"
#end
```

This example shows a few things. The first is using variables with the range
`[..]` operator to create an iterable object. Then each item is
referenced by a variable `$i` that you can operate with. In the previous
example, you also see **Comments** that are denoted with a
double pound `##`. This also showcases using the loop variable in both the
keys or the values, as well as different methods of concatenation using strings.

Notice that `$i` is an integer, so you can call a `.toString()`
method. For GraphQL types of INT, this can be handy.

You can also use a range operator directly, for example:

```
#foreach($item in [1..5])
    ...
#end
```

## Arrays

You have been manipulating a map up to this point, but arrays are also common in VTL.
With arrays you also have access to some underlying methods such as
`.isEmpty()`, `.size()`, `.set()`,
`.get()`, and `.add()`, as shown below:

```
#set($array = [])
#set($idx = 0)

##adding elements
$util.qr($array.add("element in array"))
$util.qr($myMap.put("array", $array[$idx]))

##initialize array vals on create
#set($arr2 = [42, "a string", 21, "test"])

$util.qr($myMap.put("arr2", $arr2[$idx]))
$util.qr($myMap.put("isEmpty", $array.isEmpty()))  ##isEmpty == false
$util.qr($myMap.put("size", $array.size()))

##Get and set items in an array
$util.qr($myMap.put("set", $array.set(0, 'changing array value')))
$util.qr($myMap.put("get", $array.get(0)))
```

The previous example used array index notation to retrieve an element with
`arr2[$idx]`. You can look up by name from a Map/dictionary in a similar
way:

```
#set($result = {
    "Author" : "Nadia",
    "Topic" : "GraphQL"
})

$util.qr($myMap.put("Author", $result["Author"]))
```

This is very common when filtering results coming back from data sources in Response
Templates when using conditionals.

## Conditional checks

The earlier section with `#foreach` showcased some examples of using logic
to transform data with VTL. You can also apply conditional checks to evaluate data at
runtime:

```
#if(!$array.isEmpty())
    $util.qr($myMap.put("ifCheck", "Array not empty"))
#else
    $util.qr($myMap.put("ifCheck", "Your array is empty"))
#end
```

The above `#if()` check of a Boolean expression is nice, but you can also
use operators and `#elseif()` for branching:

```
#if ($arr2.size() == 0)
    $util.qr($myMap.put("elseIfCheck", "You forgot to put anything into this array!"))
#elseif ($arr2.size() == 1)
    $util.qr($myMap.put("elseIfCheck", "Good start but please add more stuff"))
#else
    $util.qr($myMap.put("elseIfCheck", "Good job!"))
#end
```

These two examples showed negation(!) and equality (==). We can also use ||,
&&, >, <, >=, <=, and !=.

```
#set($T = true)
#set($F = false)

#if ($T || $F)
  $util.qr($myMap.put("OR", "TRUE"))
#end

#if ($T && $F)
  $util.qr($myMap.put("AND", "TRUE"))
#end
```

**Note:** Only `Boolean.FALSE` and
`null` are considered false in conditionals. Zero (0) and empty strings
(“”) are not equivalent to false.

## Operators

No programming language would be complete without some operators to perform some
mathematical actions. Here are a few examples to get you started:

```
#set($x = 5)
#set($y = 7)
#set($z = $x + $y)
#set($x-y = $x - $y)
#set($xy = $x * $y)
#set($xDIVy = $x / $y)
#set($xMODy = $x % $y)

$util.qr($myMap.put("z", $z))
$util.qr($myMap.put("x-y", $x-y))
$util.qr($myMap.put("x*y", $xy))
$util.qr($myMap.put("x/y", $xDIVy))
$util.qr($myMap.put("x|y", $xMODy))
```

### Using loops and conditionals together

It is very common when transforming data in VTL, such as before writing or reading
from a data source, to loop over objects and then perform checks before performing
an action. Combining some of the tools from the previous sections gives you a lot of
functionality. One handy tool is knowing that `#foreach` automatically
provides you with a `.count` on each item:

```
#foreach ($item in $arr2)
  #set($idx = "item" + $foreach.count)
  $util.qr($myMap.put($idx, $item))
#end
```

For example, maybe you want to just pluck out values from a map if it is under a
certain size. Using the count along with conditionals and the `#break`
statement allows you to do this:

```
#set($hashmap = {
  "DynamoDB" : "https://aws.amazon.com/dynamodb/",
  "Amplify" : "https://github.com/aws/aws-amplify",
  "DynamoDB2" : "https://aws.amazon.com/dynamodb/",
  "Amplify2" : "https://github.com/aws/aws-amplify"
})

#foreach ($key in $hashmap.keySet())
    #if($foreach.count > 2)
    #break
  #end
    $util.qr($myMap.put($key, $hashmap.get($key)))
#end
```

The previous `#foreach` is iterated over with `.keySet()`,
which you can use on maps. This gives you access to get the `$key` and
reference the value with a `.get($key)`. GraphQL arguments from clients
in AWS AppSync are stored as a map. They can also be iterated through with
`.entrySet()`, which you can then access both keys and values as a
Set, and either populate other variables or perform complex conditional checks, such
as validation or transformation of input:

```
#foreach( $entry in $context.arguments.entrySet() )
#if ($entry.key == "XYZ" && $entry.value == "BAD")
    #set($myvar = "...")
  #else
    #break
  #end
#end
```

Other common examples are automatically populating default information, like the initial
object versions when synchronizing data (very important in conflict resolution) or
the default owner of an object for authorization checks - Mary created this blog
post, so:

```
#set($myMap.owner ="Mary")
#set($myMap.defaultOwners = ["Admins", "Editors"])
```

## Context

Now that you are more familiar with performing logical checks in AWS AppSync
resolvers with VTL, take a look at the context object:

```
$util.qr($myMap.put("context", $context))
```

This contains all of the information that you can access in your GraphQL request. For
a detailed explanation, see the [context
reference](resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference "resolver-context-reference.md#aws-appsync-resolver-mapping-template-context-reference").

## Filtering

So far in this tutorial all information from your Lambda function has been returned to
the GraphQL query with a very simple JSON transformation:

```
$util.toJson($context.result)
```

The VTL logic is just as powerful when you get responses from a data source,
especially when doing authorization checks on resources. Let’s walk through some
examples. First try changing your response template like so:

```
#set($data = {
    "id" : "456",
    "meta" : "Valid Response"
})

$util.toJson($data)
```

No matter what happens with your GraphQL operation, hardcoded values are returned back
to the client. Change this slightly so that the `meta` field is populated
from the Lambda response, set earlier in the tutorial in the `elseIfCheck`
value when learning about conditionals:

```
#set($data = {
    "id" : "456"
})

#foreach($item in $context.result.entrySet())
    #if($item.key == "elseIfCheck")
        $util.qr($data.put("meta", $item.value))
    #end
#end

$util.toJson($data)
```

`$context.result` is a map, so you can use `entrySet()` to perform
logic on either the keys or the values returned. Because `$context.identity`
contains information on the user that performed the GraphQL operation, if you return
authorization information from the data source, then you can decide to return all,
partial, or no data to a user based on your logic. Change your response template to look
like the following:

```
#if($context.result["id"] == 123)
    $util.toJson($context.result)
  #else
    $util.unauthorized()
#end
```

If you run your GraphQL query, the data will be returned as normal. However, if you
change the id argument to something other than 123 (`query test { get(id:456
 meta:"badrequest"){} }`), you will get an authorization failure
message.

You can find more examples of authorization scenarios in the [authorization use
cases](security-authorization-use-cases.md#aws-appsync-security-authorization-use-cases "security-authorization-use-cases.md#aws-appsync-security-authorization-use-cases") section.

### Template sample

If you followed along with the tutorial, you may have built out this template step
by step. In case you haven’t, we include it below to copy for testing.

**Request Template**

```
#set( $myMap = {
  "id": $context.arguments.id,
  "meta": "stuff",
  "upperMeta" : "$context.arguments.meta.toUpperCase()"
} )

##This is how you would do it in two steps with a "quiet reference" and you can use it for invoking methods, such as .put() to add items to a Map
#set ($myMap2 = {})
$util.qr($myMap2.put("id", "first value"))

## Properties are created with a dot notation
#set($myMap.myProperty = "ABC")
#set($myMap.arrProperty = ["Write", "Some", "GraphQL"])
#set($myMap.jsonProperty = {
    "AppSync" : "Offline and Realtime",
    "Cognito" : "AuthN and AuthZ"
})

##When you are inside a string and just have ${} without ! it means stuff inside curly braces are a reference
#set($firstname = "Jeff")
$util.qr($myMap.put("Firstname", "${firstname}"))

#set($bigstring = "This is a long string, I want to pull out everything after the comma")
#set ($comma = $bigstring.indexOf(','))
#set ($comma = $comma +2)
#set ($substring = $bigstring.substring($comma))
$util.qr($myMap.put("substring", "${substring}"))

##Classic for-each loop over N items:
#set($start = 0)
#set($end = 5)
#set($range = [$start..$end])
#foreach($i in $range)          ##Can also use range operator directly like #foreach($item in [1...5])
   ##$util.qr($myMap.put($i, "abc"))
   ##$util.qr($myMap.put($i, $i.toString()+"foo")) ##Concat variable with string
   $util.qr($myMap.put($i, "${i}foo"))     ##Reference a variable in a string with "${varname)"
#end

##Operators don't work
#set($x = 5)
#set($y = 7)
#set($z = $x + $y)
#set($x-y = $x - $y)
#set($xy = $x * $y)
#set($xDIVy = $x / $y)
#set($xMODy = $x % $y)
$util.qr($myMap.put("z", $z))
$util.qr($myMap.put("x-y", $x-y))
$util.qr($myMap.put("x*y", $xy))
$util.qr($myMap.put("x/y", $xDIVy))
$util.qr($myMap.put("x|y", $xMODy))

##arrays
#set($array = ["first"])
#set($idx = 0)
$util.qr($myMap.put("array", $array[$idx]))
##initialize array vals on create
#set($arr2 = [42, "a string", 21, "test"])
$util.qr($myMap.put("arr2", $arr2[$idx]))
$util.qr($myMap.put("isEmpty", $array.isEmpty()))  ##Returns false
$util.qr($myMap.put("size", $array.size()))
##Get and set items in an array
$util.qr($myMap.put("set", $array.set(0, 'changing array value')))
$util.qr($myMap.put("get", $array.get(0)))

##Lookup by name from a Map/dictionary in a similar way:
#set($result = {
    "Author" : "Nadia",
    "Topic" : "GraphQL"
})
$util.qr($myMap.put("Author", $result["Author"]))


##Conditional examples
#if(!$array.isEmpty())
$util.qr($myMap.put("ifCheck", "Array not empty"))
#else
$util.qr($myMap.put("ifCheck", "Your array is empty"))
#end

#if ($arr2.size() == 0)
$util.qr($myMap.put("elseIfCheck", "You forgot to put anything into this array!"))
#elseif ($arr2.size() == 1)
$util.qr($myMap.put("elseIfCheck", "Good start but please add more stuff"))
#else
$util.qr($myMap.put("elseIfCheck", "Good job!"))
#end

##Above showed negation(!) and equality (==), we can also use OR, AND, >, <, >=, <=, and !=
#set($T = true)
#set($F = false)
#if ($T || $F)
  $util.qr($myMap.put("OR", "TRUE"))
#end

#if ($T && $F)
  $util.qr($myMap.put("AND", "TRUE"))
#end

##Using the foreach loop counter - $foreach.count
#foreach ($item in $arr2)
  #set($idx = "item" + $foreach.count)
  $util.qr($myMap.put($idx, $item))
#end

##Using a Map and plucking out keys/vals
#set($hashmap = {
    "DynamoDB" : "https://aws.amazon.com/dynamodb/",
    "Amplify" : "https://github.com/aws/aws-amplify",
    "DynamoDB2" : "https://aws.amazon.com/dynamodb/",
    "Amplify2" : "https://github.com/aws/aws-amplify"
})

#foreach ($key in $hashmap.keySet())
    #if($foreach.count > 2)
        #break
    #end
    $util.qr($myMap.put($key, $hashmap.get($key)))
#end

##concatenate strings
#set($s1 = "Hello")
#set($s2 = " World")
$util.qr($myMap.put("concat","$s1$s2"))
$util.qr($myMap.put("concat2","Second $s1 World"))

$util.qr($myMap.put("context", $context))

{
    "version" : "2017-02-28",
    "operation": "Invoke",
    "payload": $util.toJson($myMap)
}
```

**Response Template**

```
#set($data = {
"id" : "456"
})
#foreach($item in $context.result.entrySet())   ##$context.result is a MAP so we use entrySet()
    #if($item.key == "ifCheck")
        $util.qr($data.put("meta", "$item.value"))
    #end
#end

##Uncomment this out if you want to test and remove the below #if check
##$util.toJson($data)

#if($context.result["id"] == 123)
    $util.toJson($context.result)
  #else
    $util.unauthorized()
#end
```
