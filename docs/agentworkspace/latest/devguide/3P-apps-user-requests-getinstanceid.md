

# Get the instance ID of the current Connect Customer instance in Connect Customer agent workspace
<a name="3P-apps-user-requests-getinstanceid"></a>

Returns the Connect Customer instance ID associated with the user that's currently logged in to the Connect Customer agent workspace. This operation belongs to the `UserClient`.

 **Signature** 

```
async getInstanceId(): Promise<string>
```

 **Usage** 

```
const instanceId: string = await userClient.getInstanceId();
```

 **Permissions required:** 

```
*
```