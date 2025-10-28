# Finding non-compliant resources for an

account with AWS Organizations

For each account, you can get information about non-compliant resources. You should
run this command from every Region in which the account has resources.

To find non-compliant resources for an account with a tag policy, run the following
command to save the results to a file:

```
`$` `aws resourcegroupstaggingapi get-resources --region us-east-1 \
 --include-compliance-details \
 --exclude-compliant-resources > `outputfile.txt``
```
