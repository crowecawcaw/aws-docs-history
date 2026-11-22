

# Get the ARN of the current user in Connect Customer agent workspace

Returns the Amazon Resource Name (ARN) of the user that's currently logged in to the Connect Customer agent workspace. This operation belongs to the `UserClient`.

 **Signature** 

```typescript
async getUserArn(): Promise<string>
```

 **Usage** 

```typescript
const userArn: string = await userClient.getUserArn();
```

 **Permissions required:** 

```typescript
*
```