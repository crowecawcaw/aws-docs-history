

# Get the AWS Region of the current user in Connect Customer agent workspace

Returns the AWS Region of the user that's currently logged in to the Connect Customer agent workspace, for example `us-west-2`. This operation belongs to the `UserClient`.

 **Signature** 

```typescript
async getUserRegion(): Promise<string>
```

 **Usage** 

```typescript
const region: string = await userClient.getUserRegion();
```

 **Permissions required:** 

```typescript
*
```