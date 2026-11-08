

# Get the AWS Region of the current user in Connect Customer agent workspace
<a name="3P-apps-user-requests-getuserregion"></a>

Returns the AWS Region of the user that's currently logged in to the Connect Customer agent workspace, for example `us-west-2`. This operation belongs to the `UserClient`.

 **Signature** 

```
async getUserRegion(): Promise<string>
```

 **Usage** 

```
const region: string = await userClient.getUserRegion();
```

 **Permissions required:** 

```
*
```