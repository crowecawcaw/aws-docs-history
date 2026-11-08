

# Get the ARN of the current user in Connect Customer agent workspace
<a name="3P-apps-user-requests-getuserarn"></a>

Returns the Amazon Resource Name (ARN) of the user that's currently logged in to the Connect Customer agent workspace. This operation belongs to the `UserClient`.

 **Signature** 

```
async getUserArn(): Promise<string>
```

 **Usage** 

```
const userArn: string = await userClient.getUserArn();
```

 **Permissions required:** 

```
*
```