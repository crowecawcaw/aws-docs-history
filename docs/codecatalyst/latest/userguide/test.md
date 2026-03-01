Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Skipping failed tests in an action

If your action has more than one test command, you might want to allow subsequent test
commands in the action to run even if a previous command fails. For example, in the following
commands, you may want `test2` to run always, even if `test1`
fails.

```
Steps:
- Run: npm install
- Run: npm run test1
- Run: npm run test2
```

Normally, when a step returns an error, Amazon CodeCatalyst stops the workflow action and marks it
as failed. You can allow the action steps to continue to run by redirecting the error output
to `null`. You can do this by adding `2>/dev/null` to the command. With
this modification, the preceding example would look like the following.

```
Steps:
- Run: npm install
- Run: npm run test1 2>/dev/null
- Run: npm run test2
```

In the second code snippet, the status of the `npm install` command will be
honored, but any error returned by the `npm run test1` command will be ignored. As
a result the `npm run test2` command is run. By doing this, you're able to view
both reports at once regardless of whether an error occurs.
