# I am not authorized to

perform an action in WorkSpaces Secure Browser

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `workspaces-web:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: workspaces-web:GetWidget on resource: my-example-widget
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`workspaces-web:`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.
