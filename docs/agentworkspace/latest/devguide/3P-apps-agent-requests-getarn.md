

# Get the ARN of the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getarn"></a>

Returns the Amazon Resource Name(ARN) of the user that's currently logged in to the Connect Customer agent workspace.

```
async getARN(): Promise<string>          
```

 **Permissions required:** 

```
User.Details.View                
```