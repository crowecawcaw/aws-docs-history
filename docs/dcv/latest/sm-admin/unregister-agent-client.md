

# unregister-agent-client
<a name="unregister-agent-client"></a>

Unregister an agent from the broker. 

**Topics**
+ [Syntax](#sytnax)
+ [Options](#options)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker unregister-agent-client --client-id {{client_id}}
```

## Options
<a name="options"></a>

**`--client-id`**  
The ID of the agent to unregister.  
Type: String  
Required: Yes

## Example
<a name="example"></a>

The following example unregisters an agent.

**Command**

```
sudo -u root dcv-session-manager-broker unregister-agent-client --client-id 3b0d7b1d-78c7-4e79-b2e1-b976dEXAMPLE
```

**Output**

```
agent client 3b0d7b1d-78c7-4e79-b2e1-b976dEXAMPLE unregistered
```