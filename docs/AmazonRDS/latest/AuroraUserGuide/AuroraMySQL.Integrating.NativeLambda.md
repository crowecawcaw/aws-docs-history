

# Invoking a Lambda function with an Aurora MySQL native function
<a name="AuroraMySQL.Integrating.NativeLambda"></a>

**Note**  
You can call the native functions `lambda_sync` and `lambda_async` when you use Aurora MySQL version 2, or Aurora MySQL version 3.01 and higher. For more information about Aurora MySQL versions, see [Database engine updates for Amazon Aurora MySQL](AuroraMySQL.Updates.md).

You can invoke an AWS Lambda function from an Aurora MySQL DB cluster by calling the native functions `lambda_sync` and `lambda_async`. This approach can be useful when you want to integrate your database running on Aurora MySQL with other AWS services. For example, you might want to send a notification using Amazon Simple Notification Service (Amazon SNS) whenever a row is inserted into a specific table in your database.

**Contents**
+ [Working with native functions to invoke a Lambda function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions)
  + [Granting the role in Aurora MySQL version 3 and version 8.4](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.v3)
  + [Granting the privilege in Aurora MySQL version 2](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.v2)
  + [Syntax for the lambda\_sync function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.Sync.Syntax)
  + [Parameters for the lambda\_sync function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.Sync.Parameters)
  + [Example for the lambda\_sync function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.Sync.Example)
  + [Syntax for the lambda\_async function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.Async.Syntax)
  + [Parameters for the lambda\_async function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.Async.Parameters)
  + [Example for the lambda\_async function](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.Async.Example)
  + [Invoking a Lambda function within a trigger](#AuroraMySQL.Integrating.NativeLambda.lambda_functions.trigger)

## Working with native functions to invoke a Lambda function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions"></a>

The `lambda_sync` and `lambda_async` functions are built-in, native functions that invoke a Lambda function synchronously or asynchronously. When you must know the result of the Lambda function before moving on to another action, use the synchronous function `lambda_sync`. When you don't need to know the result of the Lambda function before moving on to another action, use the asynchronous function `lambda_async`.

### Granting the role in Aurora MySQL version 3 and version 8.4
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.v3"></a>

In Aurora MySQL version 3 and version 8.4, the user invoking a native function must be granted the `AWS_LAMBDA_ACCESS` role. To grant this role to a user, connect to the DB instance as the administrative user, and run the following statement.

```
GRANT AWS_LAMBDA_ACCESS TO {{user}}@{{domain-or-ip-address}}
```

You can revoke this role by running the following statement.

```
REVOKE AWS_LAMBDA_ACCESS FROM {{user}}@{{domain-or-ip-address}}
```

**Tip**  
When you use the role technique in Aurora MySQL version 3, you can also activate the role by using the `SET ROLE {{role_name}}` or `SET ROLE ALL` statement. If you aren't familiar with the MySQL 8.0 role system, you can learn more in [Role-based privilege model](AuroraMySQL.Compare-80-v3.md#AuroraMySQL.privilege-model). For more details, see [Using roles](https://dev.mysql.com/doc/refman/8.0/en/roles.html) in the *MySQL Reference Manual*.  
This only applies to the current active session. When you reconnect, you must run the `SET ROLE` statement again to grant privileges. For more information, see [SET ROLE statement](https://dev.mysql.com/doc/refman/8.0/en/set-role.html) in the *MySQL Reference Manual*.  
You can use the `activate_all_roles_on_login` DB cluster parameter to automatically activate all roles when a user connects to a DB instance. When this parameter is set, you generally don't have to call the `SET ROLE` statement explicitly to activate a role. For more information, see [activate\_all\_roles\_on\_login](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_activate_all_roles_on_login) in the *MySQL Reference Manual*.  
However, you must call `SET ROLE ALL` explicitly at the beginning of a stored procedure to activate the role, when the stored procedure is called by a different user.

If you get an error such as the following when you try to invoke a Lambda function, then run a `SET ROLE` statement.

```
SQL Error [1227] [42000]: Access denied; you need (at least one of) the Invoke Lambda privilege(s) for this operation
```

Make sure that you're granting the role to the correct user, as shown in the `mysql.users` table entries. There might be multiple users with the same name, but on different hosts. Depending on which application or host is invoking the `lambda_sync` function, MySQL selects the user with the best match according to the `host` column entries.

### Granting the privilege in Aurora MySQL version 2
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.v2"></a>

In Aurora MySQL version 2, the user invoking a native function must be granted the `INVOKE LAMBDA` privilege. To grant this privilege to a user, connect to the DB instance as the administrative user, and run the following statement.

```
GRANT INVOKE LAMBDA ON *.* TO {{user}}@{{domain-or-ip-address}}
```

You can revoke this privilege by running the following statement.

```
REVOKE INVOKE LAMBDA ON *.* FROM {{user}}@{{domain-or-ip-address}}
```

### Syntax for the lambda\_sync function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.Sync.Syntax"></a>

You invoke the `lambda_sync` function synchronously with the `RequestResponse` invocation type. The function returns the result of the Lambda invocation in a JSON payload. The function has the following syntax.

```
lambda_sync (
  {{lambda_function_ARN}},
  {{JSON_payload}}
)
```

### Parameters for the lambda\_sync function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.Sync.Parameters"></a>

The `lambda_sync` function has the following parameters.

* lambda\_function\_ARN *  
The Amazon Resource Name (ARN) of the Lambda function to invoke.

* JSON\_payload *  
The payload for the invoked Lambda function, in JSON format.

**Note**  
Aurora MySQL version 3 supports the JSON parsing functions from MySQL 8.0. However, Aurora MySQL version 2 doesn't include those functions. JSON parsing isn't required when a Lambda function returns an atomic value, such as a number or a string.

### Example for the lambda\_sync function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.Sync.Example"></a>

The following query based on `lambda_sync` invokes the Lambda function `BasicTestLambda` synchronously using the function ARN. The payload for the function is `{"operation": "ping"}`.

```
SELECT lambda_sync(
    'arn:aws:lambda:us-east-1:123456789012:function:BasicTestLambda',
    '{"operation": "ping"}');
```

### Syntax for the lambda\_async function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.Async.Syntax"></a>

You invoke the `lambda_async` function asynchronously with the `Event` invocation type. The function returns the result of the Lambda invocation in a JSON payload. The function has the following syntax.

```
lambda_async (
  {{lambda_function_ARN}},
  {{JSON_payload}}
)
```

### Parameters for the lambda\_async function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.Async.Parameters"></a>

The `lambda_async` function has the following parameters.

* lambda\_function\_ARN *  
The Amazon Resource Name (ARN) of the Lambda function to invoke.

* JSON\_payload *  
The payload for the invoked Lambda function, in JSON format.

**Note**  
Aurora MySQL version 3 supports the JSON parsing functions from MySQL 8.0. However, Aurora MySQL version 2 doesn't include those functions. JSON parsing isn't required when a Lambda function returns an atomic value, such as a number or a string.

### Example for the lambda\_async function
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.Async.Example"></a>

The following query based on `lambda_async` invokes the Lambda function `BasicTestLambda` asynchronously using the function ARN. The payload for the function is `{"operation": "ping"}`.

```
SELECT lambda_async(
    'arn:aws:lambda:us-east-1:123456789012:function:BasicTestLambda',
    '{"operation": "ping"}');
```

### Invoking a Lambda function within a trigger
<a name="AuroraMySQL.Integrating.NativeLambda.lambda_functions.trigger"></a>

You can use triggers to call Lambda on data-modifying statements. The following example uses the `lambda_async` native function and stores the result in a variable.

```
mysql>SET @result=0;
mysql>DELIMITER //
mysql>CREATE TRIGGER myFirstTrigger
      AFTER INSERT
          ON Test_trigger FOR EACH ROW
      BEGIN
      SELECT lambda_async(
          'arn:aws:lambda:us-east-1:123456789012:function:BasicTestLambda',
          '{"operation": "ping"}')
          INTO @result;
      END; //
mysql>DELIMITER ;
```

**Note**  
Triggers aren't run once per SQL statement, but once per row modified, one row at a time. When a trigger runs, the process is synchronous. The data-modifying statement only returns when the trigger completes.  
Be careful when invoking an AWS Lambda function from triggers on tables that experience high write traffic. `INSERT`, `UPDATE`, and `DELETE` triggers are activated per row. A write-heavy workload on a table with `INSERT`, `UPDATE`, or `DELETE` triggers results in a large number of calls to your AWS Lambda function.