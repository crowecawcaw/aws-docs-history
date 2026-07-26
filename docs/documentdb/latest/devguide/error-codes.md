# Error codes

When a command fails, you receive an error from Amazon DocumentDB (with MongoDB compatibility) that contains a numeric
error `code` and a descriptive message (`errmsg`). Use the following
table to identify the error codes that Amazon DocumentDB 8.0 might return to your client application.
Where an error code corresponds to a single condition, the description matches the message
text returned by the server. Codes that cover multiple conditions have a general description.

###### Important

Don't build application logic that depends on specific numeric error codes because
Amazon DocumentDB might change error codes between major versions.

| Error code | Description                                                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | Item not found                                                                                                                                                                    |
| 2          | A command argument, option, or field value is invalid or unsupported.                                                                                                             |
| 4          | A required field is missing or a configuration value is not correctly formatted.                                                                                                  |
| 5          | A view definition references itself, creating a cycle, or a filesystem error occurred.                                                                                            |
| 9          | A command, field, hint, or resume token could not be parsed or has an invalid format.                                                                                             |
| 10         | The target collection was not found or no collection was specified.                                                                                                               |
| 11         | A referenced user could not be found, or the target collection already exists.                                                                                                    |
| 13         | You are not authorized to run this command, or your authentication is invalid.                                                                                                    |
| 14         | A field or value has the wrong data type.                                                                                                                                         |
| 15         | A value overflowed its allowed range during evaluation.                                                                                                                           |
| 16         | The write batch is empty, malformed, or exceeds the allowed operation count.                                                                                                      |
| 17         | Not all objects have the same type                                                                                                                                                |
| 18         | Authentication failed because the credentials are invalid or the user does not exist.                                                                                             |
| 19         | Data processing primitive operation not found or primitive type not found                                                                                                         |
| 20         | The requested operation is not permitted in this context.                                                                                                                         |
| 26         | The target namespace or collection does not exist.                                                                                                                                |
| 27         | The requested index does not exist or no suitable index is available.                                                                                                             |
| 37         | A pipeline or aggregation stage argument is missing, empty, or invalid.                                                                                                           |
| 38         | Database name not found                                                                                                                                                           |
| 39         | The operation was canceled because it exceeded maxTimeMS, ran too long, or exceeded available memory.                                                                             |
| 40         | An update conflicts with another field, or writes are throttled or disabled by garbage collection.                                                                                |
| 41         | JavaScript error                                                                                                                                                                  |
| 43         | The specified cursor no longer exists or has expired.                                                                                                                             |
| 44         | Array index out of bounds                                                                                                                                                         |
| 48         | A collection, view, or namespace with that name already exists.                                                                                                                   |
| 51         | Illegal update operator                                                                                                                                                           |
| 52         | A field name uses a reserved '$' prefix that is not valid for storage.                                                                                                            |
| 53         | The \_id field has an invalid or unsupported type, such as an array or regex.                                                                                                     |
| 54         | cannot infer query fields to set                                                                                                                                                  |
| 55         | Transaction already committed                                                                                                                                                     |
| 56         | A field name in the request is empty, which is not allowed.                                                                                                                       |
| 57         | Transaction invalidated by other transaction                                                                                                                                      |
| 58         | Field value too long                                                                                                                                                              |
| 59         | The requested command is unknown or not supported.                                                                                                                                |
| 61         | Invalid collection                                                                                                                                                                |
| 62         | Cannot make changes to collection                                                                                                                                                 |
| 65         | batch op errors occurred                                                                                                                                                          |
| 66         | An update attempted to modify the immutable \_id field.                                                                                                                           |
| 67         | The index could not be created because of an invalid or unsupported specification.                                                                                                |
| 68         | An index with conflicting properties already exists.                                                                                                                              |
| 70         | field used with $snippet is not configured as snippet column                                                                                                                      |
| 71         | Index already exists with different options                                                                                                                                       |
| 72         | One or more options specified for the command or index are invalid.                                                                                                               |
| 73         | The namespace, database, or collection name is invalid or not allowed for this operation.                                                                                         |
| 74         | Collection does not have a text index defined.                                                                                                                                    |
| 75         | A text index is defined for this collection, but not for this field.                                                                                                              |
| 77         | Can't use snapshot with sort                                                                                                                                                      |
| 78         | Document not found                                                                                                                                                                |
| 80         | The query exceeds the maximum allowed size.                                                                                                                                       |
| 82         | Time frame has invalid formatting. Valid format: '1 m' or '3 y' '<number> h/d/w/s/m/y'                                                                                            |
| 85         | An index with that name already exists but with different options.                                                                                                                |
| 86         | The requested index conflicts with an existing index that has the same name.                                                                                                      |
| 87         | $sort key ordering must be 1 (for ascending) or -1 (for descending)                                                                                                               |
| 92         | Not enough space for operation                                                                                                                                                    |
| 93         | User already exists                                                                                                                                                               |
| 94         | The target collection, cluster, or resource privilege is invalid or unavailable.                                                                                                  |
| 95         | Database does not exist                                                                                                                                                           |
| 96         | 'writeConcern' parameter is invalid                                                                                                                                               |
| 97         | Password cannot be empty                                                                                                                                                          |
| 99         | Undefined role or privilege                                                                                                                                                       |
| 102        | Cannot add a role that is already built-in                                                                                                                                        |
| 103        | A valid role could not be extracted from the collection.                                                                                                                          |
| 105        | The user is invalid or the authorization library could not be initialized.                                                                                                        |
| 107        | Database cannot be granted roles from other database                                                                                                                              |
| 111        | \_id must be exactly specified when providing update document                                                                                                                     |
| 112        | Write Conflict                                                                                                                                                                    |
| 113        | The specified role does not exist.                                                                                                                                                |
| 114        | Role already exists                                                                                                                                                               |
| 115        | anyResource should be true when specified                                                                                                                                         |
| 116        | resources should have either db and collection set, cluster set or anyResource set                                                                                                |
| 117        | The operation conflicts with another in-progress operation, such as an active transaction.                                                                                        |
| 120        | 'showPrivileges' cannot be specified as we are showing all users                                                                                                                  |
| 121        | Document failed validation                                                                                                                                                        |
| 122        | Update error                                                                                                                                                                      |
| 124        | Error processing schema id                                                                                                                                                        |
| 125        | The command failed, often because of an ambiguous reference or missing session.                                                                                                   |
| 126        | Database already exists                                                                                                                                                           |
| 127        | Database name already exists in a difference case name                                                                                                                            |
| 128        | Too many fields                                                                                                                                                                   |
| 129        | Waiting for drop database                                                                                                                                                         |
| 130        | Bad parameter value                                                                                                                                                               |
| 136        | The cursor position was lost, or a required change stream feature is not enabled.                                                                                                 |
| 139        | JS Interpreter failure                                                                                                                                                            |
| 145        | Alias not defined in query                                                                                                                                                        |
| 147        | not master                                                                                                                                                                        |
| 148        | Insufficient resources to run query                                                                                                                                               |
| 149        | Alias already defined in query                                                                                                                                                    |
| 154        | An argument has an illegal value or an incorrect (non-numeric) type.                                                                                                              |
| 155        | NULL value encountered                                                                                                                                                            |
| 156        | UNDEFINED value encountered                                                                                                                                                       |
| 157        | NAN value encountered                                                                                                                                                             |
| 158        | Collection already in use for another purpose                                                                                                                                     |
| 159        | A duration value overflowed or a network operation failed.                                                                                                                        |
| 161        | The requested collation version is invalid or unavailable.                                                                                                                        |
| 163        | A field or name is not valid for storage.                                                                                                                                         |
| 164        | A query operator was nested in a way that is not allowed.                                                                                                                         |
| 165        | A view exceeds the maximum nesting depth of 20 or references itself in a cycle.                                                                                                   |
| 166        | The operation is not supported on a view, or too many positional elements were used.                                                                                              |
| 167        | The requested operation or stage is not supported on a view.                                                                                                                      |
| 168        | An expression or pipeline operator is unrecognized or has an invalid argument.                                                                                                    |
| 169        | BadValue $maxTimeMS has non-integral value                                                                                                                                        |
| 170        | BadValue $maxTimeMS is out of range                                                                                                                                               |
| 171        | An index cannot be built over multiple array fields.                                                                                                                              |
| 173        | Skip value must be positive                                                                                                                                                       |
| 174        | Expected log verbosity to be a number                                                                                                                                             |
| 181        | The key pattern matches multiple indexes; specify the index by name instead.                                                                                                      |
| 197        | The index specification contains an invalid or unsupported field.                                                                                                                 |
| 207        | uuid must be a 16-byte binary field with UUID (4) subtype                                                                                                                         |
| 224        | This query feature is not allowed in the current context.                                                                                                                         |
| 225        | A newer transaction has started on the session, so this older one cannot proceed.                                                                                                 |
| 241        | A value could not be converted to the requested type in $convert.                                                                                                                 |
| 250        | Invalid view                                                                                                                                                                      |
| 251        | The specified transaction number does not match any active transaction.                                                                                                           |
| 252        | Recursion limit reached                                                                                                                                                           |
| 253        | Could not insert entry into view                                                                                                                                                  |
| 254        | Could not delete entry from view                                                                                                                                                  |
| 256        | Document filtered by $having clause                                                                                                                                               |
| 257        | The total size of all operations in the transaction exceeds the allowed limit.                                                                                                    |
| 263        | This operation cannot be run inside a multi-document transaction.                                                                                                                 |
| 291        | unable to find index for $geoNear query                                                                                                                                           |
| 300        | Authentication failed because of a SASL handshake or session error.                                                                                                               |
| 301        | An authentication mechanism or requested operation is not supported.                                                                                                              |
| 302        | Authentication needs additional data to complete the SASL exchange.                                                                                                               |
| 303        | The requested stage, option, or role configuration is not supported.                                                                                                              |
| 304        | The requested aggregation stage is not supported.                                                                                                                                 |
| 305        | The aggregation projection operator is not supported.                                                                                                                             |
| 306        | The specified aggregation group accumulator operator is not supported.                                                                                                            |
| 502        | Column already exists                                                                                                                                                             |
| 505        | Insertion not allowed here                                                                                                                                                        |
| 601        | Coordinates are out of bounds                                                                                                                                                     |
| 602        | Index error                                                                                                                                                                       |
| 700        | Changes to this parameter is not allowed in live mode                                                                                                                             |
| 701        | Invalid value for this parameter                                                                                                                                                  |
| 703        | Illegal state transition for this parameter                                                                                                                                       |
| 999        | Bad transaction ID                                                                                                                                                                |
| 4570       | $lookup parameter expecting string value                                                                                                                                          |
| 4572       | $lookup is missing required fields                                                                                                                                                |
| 10065      | A parameter that must be an object (such as vars or $rand) was given a non-object value.                                                                                          |
| 10107      | not master                                                                                                                                                                        |
| 11000      | A duplicate key violates a unique index constraint.                                                                                                                               |
| 11601      | The operation was interrupted.                                                                                                                                                    |
| 11603      | Client request corrupted or illegal syntax                                                                                                                                        |
| 13103      | too many compound keys                                                                                                                                                            |
| 13297      | A database with the same name already exists but differs only in letter case.                                                                                                     |
| 13388      | Unrecognized pipeline stage name: $collStats                                                                                                                                      |
| 13435      | not master and slaveOk=false                                                                                                                                                      |
| 14031      | Not enough disk space                                                                                                                                                             |
| 15888      | must pass name of collection to create                                                                                                                                            |
| 15947      | a group's fields must be specified in an object                                                                                                                                   |
| 15950      | Group aggregate field name cannot be an operator                                                                                                                                  |
| 15952      | unknown $group operator                                                                                                                                                           |
| 15955      | Syntax error in group aggregation operator: the \_id field must be specified                                                                                                      |
| 15956      | The $skip argument is negative; it must be a non-negative number.                                                                                                                 |
| 15957      | the limit must be specified as a number                                                                                                                                           |
| 15958      | The $limit value must be a positive number.                                                                                                                                       |
| 15959      | the match filter must be an expression in an object                                                                                                                               |
| 15969      | Syntax error: the value of the $project operator must be a document.                                                                                                              |
| 15972      | Argument to $skip must be a number                                                                                                                                                |
| 15973      | the $sort key specification must be an object                                                                                                                                     |
| 15974      | $sort key ordering must be specified using a number                                                                                                                               |
| 15975      | $sort key ordering must be 1 (for ascending) or -1 (for descending)                                                                                                               |
| 15976      | $sort stage must have at least one sort key                                                                                                                                       |
| 15981      | query field is not a string                                                                                                                                                       |
| 15983      | An object representing an expression must have exactly one field.                                                                                                                 |
| 15992      | disallowed field type NULL in object expression                                                                                                                                   |
| 15998      | Field path names may not be empty strings.                                                                                                                                        |
| 16006      | A value could not be converted to a Date because it is not a valid date type.                                                                                                     |
| 16007      | A value cannot be converted to a string because a string was expected.                                                                                                            |
| 16020      | An expression operator was called with the wrong number of arguments.                                                                                                             |
| 16034      | $substrBytes starting index must be a numeric type.                                                                                                                               |
| 16035      | $substrBytes length argument must be a numeric type.                                                                                                                              |
| 16395      | $where is not allowed inside of a $match aggregation expression                                                                                                                   |
| 16400      | can't add an expression for a field because there is already an expression for that field or one of its sub-fields.                                                               |
| 16401      | can't add an expression for a subfield because there is already an expression that applies to the whole field                                                                     |
| 16404      | $ expressions are not allowed in this context                                                                                                                                     |
| 16406      | Cannot exclude fields other than \_id                                                                                                                                             |
| 16410      | A $project field name or path illegally starts with or contains '$'.                                                                                                              |
| 16411      | Field names cannot contain null character(s)                                                                                                                                      |
| 16419      | field path must not contain embedded null characters                                                                                                                              |
| 16424      | $near is not allowed inside of a $match aggregation expression                                                                                                                    |
| 16426      | $nearSphere/$near is not allowed inside of a $match aggregation expression                                                                                                        |
| 16435      | Pipeline component must contain one element                                                                                                                                       |
| 16493      | Tried to create string longer than 16MB                                                                                                                                           |
| 16554      | $add only supports numeric or date types.                                                                                                                                         |
| 16605      | $geoNear requires a valid 'near' field and correctly typed geoNear options.                                                                                                       |
| 16606      | $geoNear requires a 'distanceField' option as a String                                                                                                                            |
| 16607      | $geoNear requires the given option to be specified as a string.                                                                                                                   |
| 16608      | Divide by zero                                                                                                                                                                    |
| 16610      | $mod was given a divisor of zero.                                                                                                                                                 |
| 16611      | $mod only supports numeric types for both operands.                                                                                                                               |
| 16612      | only one date allowed in an $add expression                                                                                                                                       |
| 16613      | The operation attempted to subtract a non-numeric, non-date value from a date.                                                                                                    |
| 16702      | $concat only supports string arguments.                                                                                                                                           |
| 16730      | textIndexVersion is out of range                                                                                                                                                  |
| 16755      | can't index geometry with strict winding order                                                                                                                                    |
| 16800      | can't have 2 geo fields                                                                                                                                                           |
| 16801      | 2d has to be first in index                                                                                                                                                       |
| 16804      | location object expected, location array not in correct format                                                                                                                    |
| 16810      | $mod requires an array of exactly two values as its parameter.                                                                                                                    |
| 16837      | An update path cannot modify the same field more than once.                                                                                                                       |
| 16868      | Invalid variable name                                                                                                                                                             |
| 16869      | Invalid variable name                                                                                                                                                             |
| 16870      | Invalid variable name                                                                                                                                                             |
| 16872      | A field path is empty or '$' alone is used as a field path in $project.                                                                                                           |
| 16873      | Fieldpath does not start with $                                                                                                                                                   |
| 16874      | $let only supports an object as its argument                                                                                                                                      |
| 16875      | $let was given an unrecognized parameter.                                                                                                                                         |
| 16876      | Missing 'vars' parameter to $let                                                                                                                                                  |
| 16877      | Missing 'in' parameter to $let                                                                                                                                                    |
| 16878      | $map only supports an object as its argument                                                                                                                                      |
| 16879      | $map is given an unrecognized parameter.                                                                                                                                          |
| 16880      | $map is missing its required 'input' parameter.                                                                                                                                   |
| 16881      | Missing required field                                                                                                                                                            |
| 16882      | Missing 'in' parameter to $map                                                                                                                                                    |
| 16883      | The input to $map must be an array.                                                                                                                                               |
| 16898      | $minDistance must be non-negative                                                                                                                                                 |
| 16899      | $maxDistance must be a number                                                                                                                                                     |
| 16900      | $maxDistance must be non-negative                                                                                                                                                 |
| 16945      | Exceeded memory limit for $group or $lookup. Pass allowDiskUse:true to opt in.                                                                                                    |
| 16949      | Invalid aggregation option; allowDiskUse must be a boolean value.                                                                                                                 |
| 16990      | $out requires a string or object argument naming the output target.                                                                                                               |
| 16996      | insert for $out failed                                                                                                                                                            |
| 16997      | $out failed because the target collection's indexes changed during processing.                                                                                                    |
| 17040      | $allElementsTrue's argument must be an array.                                                                                                                                     |
| 17041      | $anyElementTrue's argument must be an array.                                                                                                                                      |
| 17042      | Both operands of $setIsSubset must be arrays.                                                                                                                                     |
| 17043      | All operands of $setUnion must be arrays.                                                                                                                                         |
| 17044      | An operand of $setEquals is not an array.                                                                                                                                         |
| 17045      | $setEquals requires at least two arguments.                                                                                                                                       |
| 17046      | Both operands of $setIsSubset must be arrays.                                                                                                                                     |
| 17047      | All operands of $setIntersection must be arrays.                                                                                                                                  |
| 17048      | Both operands of $setDifference must be arrays.                                                                                                                                   |
| 17049      | Both operands of $setDifference must be arrays.                                                                                                                                   |
| 17053      | $redact's expression should not return anything aside from the variables $$KEEP, $$DESCEND, and $$PRUNE                                                                           |
| 17080      | Missing 'if' parameter to cond                                                                                                                                                    |
| 17081      | Missing 'then' parameter to cond                                                                                                                                                  |
| 17082      | Missing 'else' parameter to cond                                                                                                                                                  |
| 17083      | Unrecognized parameter to $cond                                                                                                                                                   |
| 17124      | The argument to $size must be an array.                                                                                                                                           |
| 17275      | Can't redefine ROOT                                                                                                                                                               |
| 17276      | Variable not found                                                                                                                                                                |
| 17280      | The index key value is too large to index.                                                                                                                                        |
| 17287      | $merge cannot modify the same target row more than once.                                                                                                                          |
| 17293      | text index option 'textIndexVersion' must be a number                                                                                                                             |
| 17302      | This argument value must be greater than or equal to zero.                                                                                                                        |
| 17304      | $geoNear requires a valid 'near' point and geo query arguments.                                                                                                                   |
| 17308      | $meta is given an unsupported argument.                                                                                                                                           |
| 17310      | Both operands of $setIsSubset must be arrays.                                                                                                                                     |
| 17313      | $match with $text is only allowed as the first pipeline stage.                                                                                                                    |
| 17320      | createCollection cannot run on a namespace containing a reserved name.                                                                                                            |
| 17385      | Cannot $out to special collection                                                                                                                                                 |
| 17390      | $group does not support inclusion-style expressions                                                                                                                               |
| 17419      | The resulting document after update exceeds the maximum allowed size.                                                                                                             |
| 17420      | Document to upsert is larger than 16777216                                                                                                                                        |
| 18533      | Format field must be a string                                                                                                                                                     |
| 18534      | Unrecognized field to $dateToString                                                                                                                                               |
| 18535      | Date format string is invalid because of a trailing percent sign.                                                                                                                 |
| 18536      | Invalid $dateToString time format                                                                                                                                                 |
| 18537      | $dateToString cannot format a date component outside the range 0-9999.                                                                                                            |
| 18627      | Missing 'format' parameter to $dateToString                                                                                                                                       |
| 18628      | Missing 'date' parameter to $dateToString                                                                                                                                         |
| 18629      | incorrect argument type                                                                                                                                                           |
| 25278      | $geoNear requires a 'distanceField' argument                                                                                                                                      |
| 26823      | An operation ID cannot be represented within the available bits.                                                                                                                  |
| 28539      | The first argument to the distinct command must be a string                                                                                                                       |
| 28646      | $Filter expects an object as a parameter                                                                                                                                          |
| 28647      | Unexpected field to $filter                                                                                                                                                       |
| 28648      | $Filter requires an 'input' field                                                                                                                                                 |
| 28649      | $Filter requires an 'as' field                                                                                                                                                    |
| 28650      | $Filter requires a 'cond' field                                                                                                                                                   |
| 28651      | Array input required                                                                                                                                                              |
| 28656      | $substrBytes: Invalid range, starting index is a UTF-8 continuation byte.                                                                                                         |
| 28657      | $substrBytes: Invalid range, ending index is in the middle of a UTF-8 character.                                                                                                  |
| 28664      | $concatArrays only supports array inputs.                                                                                                                                         |
| 28667      | An expression such as $slice, $range, or $indexOfArray got the wrong number of arguments.                                                                                         |
| 28680      | $abs is applied to a value, like the minimum long, that cannot be negated.                                                                                                        |
| 28689      | An operator argument must be an array but a different type was given.                                                                                                             |
| 28690      | Second argument to arrayElemAt must be numeric                                                                                                                                    |
| 28691      | Second argument to arrayElemAt must be represented by a 32 bit integer                                                                                                            |
| 28714      | $sqrt's argument must be greater than or equal to 0                                                                                                                               |
| 28724      | The first argument to $slice must be an array.                                                                                                                                    |
| 28725      | The second argument to $slice must be a numeric value.                                                                                                                            |
| 28726      | The second argument to $slice must fit in a 32-bit integer.                                                                                                                       |
| 28727      | The third argument to $slice must be a number.                                                                                                                                    |
| 28728      | The third argument to $slice must be a 32-bit integer.                                                                                                                            |
| 28729      | $slice's third argument must be a positive 32-bit integer.                                                                                                                        |
| 28745      | the $sample stage specification must be an object                                                                                                                                 |
| 28746      | size argument to $sample must be a number                                                                                                                                         |
| 28747      | size argument to $sample must not be negative                                                                                                                                     |
| 28748      | $sample received an unrecognized option.                                                                                                                                          |
| 28749      | $sample stage must specify a size                                                                                                                                                 |
| 28756      | $log's argument must be numeric.                                                                                                                                                  |
| 28757      | $log requires its base argument to be a numeric value.                                                                                                                            |
| 28758      | The argument to $log must be a positive number.                                                                                                                                   |
| 28759      | $log's base must be a positive number not equal to 1.                                                                                                                             |
| 28761      | $log10's argument must be a positive number.                                                                                                                                      |
| 28762      | $pow's base must be a numeric value.                                                                                                                                              |
| 28763      | $pow's exponent must be numeric.                                                                                                                                                  |
| 28764      | $pow cannot take a base of 0 and a negative exponent                                                                                                                              |
| 28765      | $ceil, $exp, $floor, $ln, or $log10 receives a non-numeric type.                                                                                                                  |
| 28766      | $ln requires a positive number argument.                                                                                                                                          |
| 28812      | Fieldpath is empty                                                                                                                                                                |
| 28818      | Fieldpath does not start with a '$'                                                                                                                                               |
| 31022      | This operator requires an 'input' parameter to be specified.                                                                                                                      |
| 31023      | This operator requires a 'regex' parameter.                                                                                                                                       |
| 31024      | The operator is given an unknown argument.                                                                                                                                        |
| 31032      | A field name cannot contain an embedded null byte.                                                                                                                                |
| 31034      | A value falls outside the allowed range of [-32768, 32767].                                                                                                                       |
| 31095      | 'isoWeekYear' must evaluate to an integer between 1 and 9999.                                                                                                                     |
| 31138      | The $meta value used for sorting is not a valid metadata keyword.                                                                                                                 |
| 31170      | An empty object was expected but a non-empty value was provided.                                                                                                                  |
| 31249      | A projection path collides with another field in the projection.                                                                                                                  |
| 31254      | An inclusion cannot be specified within an exclusion projection.                                                                                                                  |
| 31393      | $bsonSize requires a document as input.                                                                                                                                           |
| 31394      | A positional projection operator cannot appear in the middle of a field path.                                                                                                     |
| 34413      | An invalid operator was used in a geo near query.                                                                                                                                 |
| 34435      | The argument to $reverseArray must be an array.                                                                                                                                   |
| 34443      | $range requires a numeric starting value.                                                                                                                                         |
| 34444      | $range requires a starting value representable as a 32-bit integer.                                                                                                               |
| 34445      | $range requires its ending value to be numeric.                                                                                                                                   |
| 34446      | $range ending value must fit in a 32-bit integer.                                                                                                                                 |
| 34447      | $range requires a numeric step value.                                                                                                                                             |
| 34448      | $range requires a step value representable as a 32-bit integer.                                                                                                                   |
| 34449      | $range requires a non-zero step value                                                                                                                                             |
| 34450      | $substrCP's starting index must be a numeric type.                                                                                                                                |
| 34451      | The $substrCP starting index cannot be represented as a 32-bit integer.                                                                                                           |
| 34452      | The length argument to $substrCP is not a numeric type.                                                                                                                           |
| 34453      | $substrCP length cannot be represented as a 32-bit integer.                                                                                                                       |
| 34454      | $substrCP: length must be a nonnegative integer.                                                                                                                                  |
| 34455      | $substrCP: the starting index must be nonnegative integer.                                                                                                                        |
| 34460      | $zip only supports an object as its argument.                                                                                                                                     |
| 34461      | $zip inputs must be an array of expressions.                                                                                                                                      |
| 34462      | The 'defaults' option must be an array of expressions.                                                                                                                            |
| 34463      | $zip's useLongestLength option must be a boolean.                                                                                                                                 |
| 34464      | $zip was given an unknown argument.                                                                                                                                               |
| 34465      | $zip requires at least one input array                                                                                                                                            |
| 34466      | cannot specify defaults unless useLongestLength is true                                                                                                                           |
| 34467      | defaults and inputs must have the same length                                                                                                                                     |
| 34468      | $zip receives a non-array expression in its input.                                                                                                                                |
| 34471      | $strLenCP requires a string argument.                                                                                                                                             |
| 34473      | $strLenBytes requires a string argument.                                                                                                                                          |
| 40060      | $switch requires an object as its argument.                                                                                                                                       |
| 40061      | $switch requires 'branches' to be an array.                                                                                                                                       |
| 40062      | $switch requires each branch to be an object.                                                                                                                                     |
| 40063      | $switch is given an unknown argument within a branch.                                                                                                                             |
| 40064      | $switch requires each branch have a 'case' expression.                                                                                                                            |
| 40065      | $switch requires each branch have a 'then' expression.                                                                                                                            |
| 40066      | $switch could not find a matching branch for an input, and no default was specified.                                                                                              |
| 40067      | The $switch expression contains an unknown argument.                                                                                                                              |
| 40068      | $switch requires at least one branch                                                                                                                                              |
| 40075      | $reduce requires object                                                                                                                                                           |
| 40076      | Unknown argument to $reduce                                                                                                                                                       |
| 40077      | $reduce requires 'input'                                                                                                                                                          |
| 40078      | $reduce requires 'initialValue'                                                                                                                                                   |
| 40079      | $reduce requires 'in'                                                                                                                                                             |
| 40080      | The input to $reduce must be an array.                                                                                                                                            |
| 40081      | The operator requires an array as its second argument.                                                                                                                            |
| 40085      | $split requires its first argument to evaluate to a string.                                                                                                                       |
| 40086      | $split's second argument must evaluate to a string.                                                                                                                               |
| 40087      | $split requires a non-empty separator                                                                                                                                             |
| 40090      | $indexOfArray requires an array as a first argument                                                                                                                               |
| 40091      | The first argument to $indexOfBytes is not a string.                                                                                                                              |
| 40092      | $indexOfBytes requires a string as its second argument.                                                                                                                           |
| 40093      | $indexOfCP requires a string as its first argument.                                                                                                                               |
| 40094      | $indexOfCP requires a string as its second argument.                                                                                                                              |
| 40096      | $indexOfArray requires integral starting and ending index values.                                                                                                                 |
| 40097      | $indexOfArray requires nonnegative numeric start and end indexes.                                                                                                                 |
| 40148      | the sortByCount field must be defined as a $-prefixed path or an expression inside an object                                                                                      |
| 40149      | the sortByCount field must be specified as a string or as an object                                                                                                               |
| 40156      | the count field must be a non-empty string                                                                                                                                        |
| 40157      | the count field must be a non-empty string                                                                                                                                        |
| 40158      | the count field cannot be a $-prefixed path                                                                                                                                       |
| 40159      | the count field cannot contain a null byte                                                                                                                                        |
| 40160      | the count field cannot contain '.'                                                                                                                                                |
| 40169      | the $facet specification must be a non-empty object                                                                                                                               |
| 40170      | arguments to $facet must be arrays                                                                                                                                                |
| 40171      | elements of arrays in $facet spec must be non-empty objects                                                                                                                       |
| 40172      | sub-pipeline in $facet stage cannot be empty                                                                                                                                      |
| 40176      | Conflicting fieldnames given                                                                                                                                                      |
| 40177      | $project and $addFields require at least one output field.                                                                                                                        |
| 40178      | Cannot exclude fields except '\_id' in an inclusion projection                                                                                                                    |
| 40179      | Cannot include fields or reset fields or add computed fields in an exclusion projection                                                                                           |
| 40180      | $project does not allow an empty object as a field value.                                                                                                                         |
| 40181      | Invalid $project :: caused by :: an expression specification must contain exactly one field.                                                                                      |
| 40183      | A dotted field name cannot be used inside a sub-object.                                                                                                                           |
| 40192      | The $bucket 'boundaries' field must have at least 2 values                                                                                                                        |
| 40193      | All values in the the 'boundaries' option to $bucket must have the same type                                                                                                      |
| 40194      | The 'boundaries' option to $bucket must be sorted, but elements are not in ascending order                                                                                        |
| 40195      | The $bucket 'default' field must be a constant expression                                                                                                                         |
| 40196      | The $bucket 'output' field must be an object                                                                                                                                      |
| 40197      | Unrecognized option to $bucket                                                                                                                                                    |
| 40198      | $bucket requires 'groupBy' and 'boundaries' to be specified                                                                                                                       |
| 40199      | The $bucket 'default' field must be less than the lowest boundary or greater than or equal to the highest boundary.                                                               |
| 40200      | The $bucket 'boundaries' field must be an array                                                                                                                                   |
| 40201      | Argument to $bucket stage must be an object                                                                                                                                       |
| 40202      | The $bucket 'groupBy' field must be defined as a $-prefixed path or an expression                                                                                                 |
| 40203      | The field must be an accumulator object                                                                                                                                           |
| 40204      | The field name cannot contain '.'                                                                                                                                                 |
| 40205      | The field name cannot be an operator name                                                                                                                                         |
| 40206      | The accumulator is a unary operator                                                                                                                                               |
| 40218      | query requires text score metadata, but it is not available                                                                                                                       |
| 40228      | $replaceRoot 'newRoot' expression must evaluate to an object.                                                                                                                     |
| 40229      | $replaceRoot requires an object as its specification.                                                                                                                             |
| 40230      | $replaceRoot only accepts the 'newRoot' option.                                                                                                                                   |
| 40234      | The $group field must be an accumulator object.                                                                                                                                   |
| 40235      | A field name cannot contain a '.' character.                                                                                                                                      |
| 40236      | Field names may not start with '$'                                                                                                                                                |
| 40237      | This accumulator is a unary operator and takes a single argument.                                                                                                                 |
| 40239      | The $bucketAuto 'groupBy' field must be defined as a $-prefixed path or an expression object                                                                                      |
| 40240      | The argument to $bucketAuto must be an object                                                                                                                                     |
| 40241      | The $bucketAuto 'buckets' field must be a numeric value                                                                                                                           |
| 40242      | The $bucketAuto 'buckets' field must be representable as a 32-bit integer                                                                                                         |
| 40243      | The $bucketAuto 'buckets' field must be greater than 0                                                                                                                            |
| 40244      | The $bucketAuto 'output' field must be an object                                                                                                                                  |
| 40245      | Unrecognized option to $bucketAuto                                                                                                                                                |
| 40246      | $bucketAuto requires 'groupBy' and 'buckets' to be specified                                                                                                                      |
| 40257      | Unknown rounding granularity                                                                                                                                                      |
| 40258      | $bucketAuto can specify a 'granularity' with numeric boundaries only                                                                                                              |
| 40260      | $bucketAuto can specify a 'granularity' with non-negative numbers only, but found a negative number                                                                               |
| 40261      | The $bucketAuto 'granularity' field must be a string                                                                                                                              |
| 40272      | The $addFields stage specification must be an object.                                                                                                                             |
| 40319      | the $lookup stage specification must be an object                                                                                                                                 |
| 40320      | missing 'from' option to $lookup stage specification                                                                                                                              |
| 40321      | 'from' option to $lookup must be a string                                                                                                                                         |
| 40322      | invalid $lookup namespace                                                                                                                                                         |
| 40323      | A pipeline stage specification object must contain exactly one field.                                                                                                             |
| 40324      | The pipeline contains an unrecognized stage name.                                                                                                                                 |
| 40331      | This aggregation stage is not allowed inside a $facet pipeline.                                                                                                                   |
| 40352      | $project field paths cannot be empty strings.                                                                                                                                     |
| 40353      | A field path must not end with a '.'.                                                                                                                                             |
| 40386      | $arrayToObject requires an array input.                                                                                                                                           |
| 40390      | $objectToArray requires a document as input.                                                                                                                                      |
| 40391      | $arrayToObject requires a consistent input format. Elements mustall be arrays or all be objects. Object was detected, now found: array                                            |
| 40392      | $arrayToObject requires objects with exactly the keys 'k' and 'v'.                                                                                                                |
| 40393      | $arrayToObject requires an object with keys 'k' and 'v'. Missing either or both keys                                                                                              |
| 40394      | $arrayToObject requires objects with string 'k' keys and 'v' values.                                                                                                              |
| 40395      | $arrayToObject requires key-value pairs whose keys are strings.                                                                                                                   |
| 40396      | $arrayToObject requires a consistent input format. Elements mustall be arrays or all be objects. Array was detected, now found: object                                            |
| 40397      | $arrayToObject requires an array of two-element arrays.                                                                                                                           |
| 40398      | $arrayToObject is given an input of an unrecognized type or format.                                                                                                               |
| 40400      | $mergeObjects requires all inputs to be objects.                                                                                                                                  |
| 40414      | A required command field is missing or failed validation.                                                                                                                         |
| 40415      | The command contains an unrecognized field.                                                                                                                                       |
| 40422      | A BSON array field name has an invalid value.                                                                                                                                     |
| 40485      | An unrecognized time zone identifier was supplied.                                                                                                                                |
| 40489      | $dateFromParts does not allow mixing regular calendar fields with ISO week date fields                                                                                            |
| 40515      | A $dateFromParts argument does not evaluate to an integer number.                                                                                                                 |
| 40516      | $dateFromParts requires either 'year' or 'isoWeekYear' to be present                                                                                                              |
| 40517      | The 'timezone' option must evaluate to a string for date operators.                                                                                                               |
| 40518      | $dateFromParts or $dateToParts got an unrecognized or wrongly typed parameter.                                                                                                    |
| 40519      | $dateFromParts only supports an object as its argument.                                                                                                                           |
| 40520      | $dateToParts was given an unrecognized parameter.                                                                                                                                 |
| 40522      | $dateToParts requires an object argument with a 'date' parameter.                                                                                                                 |
| 40523      | $dateFromParts 'year' must be an integer in the range 1 to 9999.                                                                                                                  |
| 40525      | $dateFromParts ISO week/day values are out of range or missing required fields.                                                                                                   |
| 40533      | The timezone argument must be a string.                                                                                                                                           |
| 40535      | An unrecognized option was supplied to the stage or expression.                                                                                                                   |
| 40536      | The expression accepts exactly one argument when given an array.                                                                                                                  |
| 40539      | The required 'date' argument to a date operator is missing.                                                                                                                       |
| 40540      | $dateFromString only supports an object as an argument                                                                                                                            |
| 40541      | $dateFromString received an unrecognized argument.                                                                                                                                |
| 40542      | Missing 'dateString' parameter to $dateFromString                                                                                                                                 |
| 40543      | $dateFromString requires that 'dateString' be a string.                                                                                                                           |
| 40545      | The date/time string is incomplete, with required elements missing.                                                                                                               |
| 40551      | you cannot pass in a date/time string with time zone information together with a timezone argument                                                                                |
| 40553      | $dateFromString cannot parse the given date string.                                                                                                                               |
| 40554      | you cannot pass in a date/time string with GMT offset together with a timezone argument                                                                                           |
| 40575      | $changeStream 'fullDocument' must be "default" or "updateLookup".                                                                                                                 |
| 40600      | $out cannot be used within a $facet stage.                                                                                                                                        |
| 40601      | $out and $merge can only be the final stage in the pipeline.                                                                                                                      |
| 40602      | A stage like $changeStream or $geoNear is not the first in the pipeline.                                                                                                          |
| 40603      | $geoNear was not the first stage in the pipeline after optimization. Is optimization disabled or inhibited?                                                                       |
| 40647      | The change stream resume token has a missing or wrong-typed \_data field.                                                                                                         |
| 40674      | Only one type of resume option is allowed, but multiple were found.                                                                                                               |
| 50001      | autoIndexId:false is not allowed for the specified collection.                                                                                                                    |
| 50694      | This operator was given an unknown argument.                                                                                                                                      |
| 50695      | This operator requires an 'input' field.                                                                                                                                          |
| 50696      | The operator only supports an object as its argument.                                                                                                                             |
| 50699      | This expression operator requires its input to be a string.                                                                                                                       |
| 50700      | The 'chars' argument must be a string.                                                                                                                                            |
| 50736      | getMore cannot run in a session on a cursor not created in a session.                                                                                                             |
| 50737      | Running getMore on a session-created cursor requires an lsid to be supplied.                                                                                                      |
| 50752      | The $substrBytes starting index is negative.                                                                                                                                      |
| 50808      | $changeStream stage expects a document as its argument.                                                                                                                           |
| 51024      | The collation 'strength' value must be 5 or less.                                                                                                                                 |
| 51047      | This operator or stage is not allowed within a $lookup sub-pipeline.                                                                                                              |
| 51075      | Cannot set options in both $regex and $options                                                                                                                                    |
| 51076      | Insufficient memory to build the vector index for the specified number of lists.                                                                                                  |
| 51078      | Could not find index name.                                                                                                                                                        |
| 51079      | Latency Stats are not supported                                                                                                                                                   |
| 51091      | A regular expression is invalid or badly formed.                                                                                                                                  |
| 51103      | The operator expects an object of named arguments but received another type.                                                                                                      |
| 51104      | The operator requires its 'input' argument to be a string.                                                                                                                        |
| 51105      | An operator's 'regex' argument is not a string or regex type.                                                                                                                     |
| 51106      | An operator requires its 'options' parameter to be a string.                                                                                                                      |
| 51107      | $regex options cannot be specified in both the 'regex' and 'options' fields.                                                                                                      |
| 51108      | Regular expression options contain an invalid flag or embedded null byte.                                                                                                         |
| 51109      | A regular expression cannot contain an embedded null byte.                                                                                                                        |
| 51110      | Regular expression options cannot contain an embedded null byte.                                                                                                                  |
| 51111      | The regular expression supplied to this operator is invalid.                                                                                                                      |
| 51151      | The size of buffer to store output exceeded the data type limit                                                                                                                   |
| 51156      | A regular expression failed to execute in $regex during evaluation.                                                                                                               |
| 51270      | An empty sub-projection object is not a valid projection value.                                                                                                                   |
| 51272      | Syntax error: $projection requires at least one output field.                                                                                                                     |
| 51744      | The operator requires 'replacement' to be a string.                                                                                                                               |
| 51745      | The operator requires its 'find' argument to be a string.                                                                                                                         |
| 51746      | An operator's 'input' argument is not a string.                                                                                                                                   |
| 51747      | An operator requires a 'replacement' parameter.                                                                                                                                   |
| 51748      | This operator requires a 'find' parameter.                                                                                                                                        |
| 51749      | This operator requires an 'input' parameter.                                                                                                                                      |
| 51750      | An aggregation operator received an unknown argument.                                                                                                                             |
| 100003     | Internal system error while processing the optimized query path                                                                                                                   |
| 100005     | A configured limit, such as collections, custom roles, or privileges, has been exceeded.                                                                                          |
| 100006     | The maximum number of allowed users has been exceeded.                                                                                                                            |
| 3040501    | $rand does not currently accept arguments                                                                                                                                         |
| 3041701    | $getField received an unknown argument in $project.                                                                                                                               |
| 3041702    | Invalid $project :: caused by :: $getField requires 'field' to be specified                                                                                                       |
| 3041703    | Invalid $project :: caused by :: $getField requires 'input' to be specified                                                                                                       |
| 3041704    | $getField requires the 'field' argument to evaluate to a string.                                                                                                                  |
| 4161100    | $setField and $unsetField only support an object as their argument.                                                                                                               |
| 4161101    | $setField or $unsetField was given an unknown argument.                                                                                                                           |
| 4161102    | $setField and $unsetField require a 'field' to be specified.                                                                                                                      |
| 4161103    | Invalid $project :: caused by :: $setField requires 'value' to be specified                                                                                                       |
| 4161105    | $setField or $unsetField requires 'input' to evaluate to an object.                                                                                                               |
| 4161106    | $setField and $unsetField require 'field' to evaluate to a constant.                                                                                                              |
| 4161107    | $setField or $unsetField requires 'field' to evaluate to a string.                                                                                                                |
| 4161108    | $project disallows a field path reference here; use {$literal: ...} instead.                                                                                                      |
| 4161109    | $setField and $unsetField require an 'input' field to be specified.                                                                                                               |
| 4662500    | The command contains an unrecognized field.                                                                                                                                       |
| 4862100    | The fully qualified namespace exceeds the maximum allowed length.                                                                                                                 |
| 5166301    | $dateDiff only supports an object as its argument                                                                                                                                 |
| 5166302    | $dateDiff was given an unrecognized argument.                                                                                                                                     |
| 5166303    | Missing 'startDate' parameter to $dateDiff                                                                                                                                        |
| 5166304    | Missing 'endDate' parameter to $dateDiff                                                                                                                                          |
| 5166305    | Missing 'unit' parameter to $dateDiff                                                                                                                                             |
| 5166307    | A $dateDiff argument is not a date.                                                                                                                                               |
| 5166308    | $dateDiff overflowed while computing the date difference.                                                                                                                         |
| 5166400    | $dateAdd and $dateSubtract require their argument to be an object.                                                                                                                |
| 5166401    | $dateAdd or $dateSubtract got an unrecognized argument.                                                                                                                           |
| 5166402    | $dateAdd or $dateSubtract require startDate, unit, and amount to be present.                                                                                                      |
| 5166403    | $dateAdd requires startDate to be convertible to a date                                                                                                                           |
| 5166404    | $dateAdd expects string defining the time unit                                                                                                                                    |
| 5166405    | $dateAdd expects integer amount of time units                                                                                                                                     |
| 5166406    | dateAdd overflowed                                                                                                                                                                |
| 5166503    | An unknown time unit value was provided.                                                                                                                                          |
| 5439002    | $dateTrunc overflowed while computing the truncated date.                                                                                                                         |
| 5439006    | dateTrunc unsupported binSize value                                                                                                                                               |
| 5439007    | $dateTrunc only supports an object as its argument                                                                                                                                |
| 5439008    | Unrecognized $dateTrunc argument; expected date, unit, binSize, timezone, startOfWeek.                                                                                            |
| 5439009    | Missing 'date' parameter to $dateTrunc                                                                                                                                            |
| 5439010    | Missing 'unit' parameter to $dateTrunc                                                                                                                                            |
| 5439012    | $dateTrunc requires 'date' to be a date.                                                                                                                                          |
| 5439013    | $dateDiff and $dateTrunc require 'unit' to be a string.                                                                                                                           |
| 5439014    | $dateDiff and $dateTrunc 'unit' value is not a recognized time unit.                                                                                                              |
| 5439015    | $dateDiff or $dateTrunc require 'startOfWeek' to be a string.                                                                                                                     |
| 5439016    | $dateDiff or $dateTrunc 'startOfWeek' value is not a valid day of the week.                                                                                                       |
| 5439017    | $dateTrunc requires 'binSize' to be a 64-bit integer.                                                                                                                             |
| 5439018    | $dateTrunc requires 'binSize' to be greater than 0.                                                                                                                               |
| 5447000    | The $collStats stage must be a nested object.                                                                                                                                     |
| 5626500    | $geoNear, $near, and $nearSphere are not allowed in this context, as these operators require sorting geospatial data. If you do not need sort, consider using $geoWithin instead. |
| 5654600    | $project does not allow a field path reference in this context.                                                                                                                   |
| 5654601    | Invalid $project :: caused by :: $getField requires 'field' to evaluate to a constant, but got a non-constant argument                                                            |
| 5654602    | $getField requires 'field' to evaluate to a string.                                                                                                                               |
| 5733415    | can't $mod by zero                                                                                                                                                                |
| 5860400    | $geoNear requires a 'near' argument                                                                                                                                               |
| 5887502    | All operands of $setEquals must be arrays.                                                                                                                                        |
| 5911200    | PlanExecutor error during aggregation :: caused by :: $mergeObjects only supports objects                                                                                         |
| 5976500    | $dateAdd was given an invalid 'amount' parameter value.                                                                                                                           |
| 6045000    | $dateSubtract was given an invalid 'amount' parameter value.                                                                                                                      |
| 7158303    | $switch found no matching branch for the input and no default was specified.                                                                                                      |
