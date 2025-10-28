# Update the AFT version

Sign in to the AWS Control Tower management account to initiate this AFT update.

You can update your deployed AFT version by pulling it in from the `main`
repository branch:

```
terraform get -update
```

After the pull is complete, you can re-run the Terraform plan or run apply to update
the AFT infrastructure with the latest changes.
