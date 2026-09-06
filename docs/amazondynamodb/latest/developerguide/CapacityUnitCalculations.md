

# DynamoDB item sizes and formats
<a name="CapacityUnitCalculations"></a>

DynamoDB tables are schemaless, except for the primary key, so the items in a table can all have different attributes, sizes, and data types.

The total size of an item is the sum of the lengths of its attribute names and values, plus any applicable overhead as described below. You can use the following guidelines to estimate attribute sizes:
+ Strings are Unicode with UTF-8 binary encoding. The size of a string is *(number of UTF-8-encoded bytes of attribute name) \+ (number of UTF-8-encoded bytes)*.
+ Numbers are variable length, with up to 38 significant digits. Leading and trailing zeroes are trimmed. The size of a number is approximately *(number of UTF-8-encoded bytes of attribute name) \+ (1 byte per two significant digits) \+ (1 byte)*.
+ A binary value must be encoded in base64 format before it can be sent to DynamoDB, but the value's raw byte length is used for calculating size. The size of a binary attribute is *(number of UTF-8-encoded bytes of attribute name) \+ (number of raw bytes).*
+ The size of a null attribute or a Boolean attribute is *(number of UTF-8-encoded bytes of attribute name) \+ (1 byte)*.
+ An attribute of type `List` or `Map` requires 3 bytes of overhead, regardless of its contents. The size of a `List` or `Map` is *(number of UTF-8-encoded bytes of attribute name) \+ sum (size of nested elements) \+ (3 bytes) *. The size of an empty `List` or `Map` is *(number of UTF-8-encoded bytes of attribute name) \+ (3 bytes)*.
+ Each `List` or `Map` element also requires 1 byte of overhead.
+ A set (string set, number set, or binary set) does not require any additional overhead beyond the sizes of its elements. The size of a set is *(number of UTF-8-encoded bytes of attribute name) \+ sum (size of each element value)*. Each element value is sized according to its type, using the same rules as the corresponding scalar type, but without an attribute name: a string element is *(number of UTF-8-encoded bytes)*, a number element is *(1 byte per two significant digits) \+ (1 byte)*, and a binary element is *(number of raw bytes)*.

**Note**  
We recommend that you choose shorter attribute names rather than long ones. This helps you reduce the amount of storage required, but also can lower the amount of RCU/WCUs you use.

For storage billing purposes, each item includes a per-item storage overhead that depends on the features you have enabled.
+ All items in DynamoDB require 100 bytes of storage overhead per item.
+ Some DynamoDB features (global tables, transactions, change data capture for Kinesis Data Streams with DynamoDB) require additional storage overhead to account for system-created attributes resulting from enabling those features. For example, global tables requires an additional 48 bytes of storage overhead.