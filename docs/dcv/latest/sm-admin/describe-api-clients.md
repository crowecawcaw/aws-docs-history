

# describe-api-clients
<a name="describe-api-clients"></a>

Lists the Session Manager clients that have been registered with the broker.

**Topics**
+ [Syntax](#sytnax)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker describe-api-clients
```

## Output
<a name="output"></a>

**`name`**  
The unique name of the Session Manager client.

**`id`**  
The unique ID of the Session Manager client.

**`active`**  
Indicates the status of the Session Manager client. If the client is active, the value is `true`; otherwise, it's `false`.

## Example
<a name="example"></a>

The following example lists the registered Session Manager clients.

**Command**

```
sudo -u root dcv-session-manager-broker describe-api-clients
```

**Output**

```
Api clients
[ {
"name" : "client-abc",
"id" : "f855b54b-40d4-4769-b792-b727bEXAMPLE",
"active" : false
}, {
"name" : "client-xyz",
"id" : "21cfe9cf-61d7-4c53-b1b6-cf248EXAMPLE",
"active" : true
}]
```