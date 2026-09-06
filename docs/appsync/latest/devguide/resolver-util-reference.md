

# AWS AppSync resolver mapping template utility reference
<a name="resolver-util-reference"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html).

AWS AppSync defines a set of utilities that you can use within a GraphQL resolver to simplify interactions with data sources. Some of these utilities are for general use with any data source, such as generating IDs or timestamps. Others are specific to a type of data source. The following utilities are available:
+  [ Utility helpers in $util ](https://docs.aws.amazon.com/appsync/latest/devguide/utility-helpers-in-util.html) - The $util variable contains general utility methods to help you work with data. Unless otherwise specified, all utilities use the UTF-8 character set.
+ [ AppSync directives](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-directives.html) - AppSync exposes directives to facilitate developer productivity when writing in VTL.
+  [ Time helpers in $util.time ](https://docs.aws.amazon.com/appsync/latest/devguide/time-helpers-in-util-time.html) - The $util.time variable contains datetime methods to help generate timestamps, convert between datetime formats, and parse datetime strings. The syntax for datetime formats is based on [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html), which you can reference for further documentation.
+ [ List helpers in $util.list ](https://docs.aws.amazon.com/appsync/latest/devguide/list-helpers-in-util-list.html) - $util.list contains methods to help with common List operations such as removing or retaining items from a list for filtering use cases.
+  [ Map helpers in $util.map ](https://docs.aws.amazon.com/appsync/latest/devguide/utility-helpers-in-map.html) - $util.map contains methods to help with common Map operations such as removing or retaining items from a Map for filtering use cases.
+  [ DynamoDB helpers in $util.dynamodb ](https://docs.aws.amazon.com/appsync/latest/devguide/dynamodb-helpers-in-util-dynamodb.html) - $util.dynamodb contains helper methods that make it easier to write and read data to Amazon DynamoDB, such as automatic type mapping and formatting. 
+  [ Amazon RDS helpers in $util.rds ](https://docs.aws.amazon.com/appsync/latest/devguide/rds-helpers-in-util-rds.html) - $util.rds contains helper methods that format RDS operations by getting rid of extraneous data in result outputs.
+  [ HTTP helpers in $util.http ](https://docs.aws.amazon.com/appsync/latest/devguide/http-helpers-in-utils-http.html) - The $util.http utility provides helper methods that you can use to manage HTTP request parameters and to add response headers.
+  [ XML helpers in $util.xml ](https://docs.aws.amazon.com/appsync/latest/devguide/xml-helpers-in-utils-xml.html) - $util.xml contains helper methods that can make it easier to translate XML responses to JSON or a Dictionary.
+  [ Transformation helpers in $util.transform ](https://docs.aws.amazon.com/appsync/latest/devguide/transformation-helpers-in-utils-transform.html) - $util.transform contains helper methods that make it easier to perform complex operations against data sources, such as DynamoDB filter operations.
+  [ Math helpers in $util.math ](https://docs.aws.amazon.com/appsync/latest/devguide/math-helpers-in-util-math.html) - $util.math contains methods to help with common Math operations.
+  [ String helpers in $util.str ](https://docs.aws.amazon.com/appsync/latest/devguide/str-helpers-in-util-str.html) - $util.str contains methods to help with common String operations.
+  [ Extensions ](https://docs.aws.amazon.com/appsync/latest/devguide/extensions.html) - $extensions contains a set of methods to make additional actions within your resolvers.