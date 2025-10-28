# Use Infrastructure Composer with AWS SAM to delete a stack

This example shows you how to delete an AWS CloudFormation stack using the **sam delete** command.

Enter the command **sam delete** in the AWS SAM CLI and confirm whether you want to delete the stack and the template:

```
`$` `sam delete`
	Are you sure you want to delete the stack aws-app-composer-basic-api in the region us-west-2 ? [y/N]: `y`
	Do you want to delete the template file 30439348c0be6e1b85043b7a935b34ab.template in S3? [y/N]: `y`
	- Deleting S3 object with key eb226ca86d1bc4e9914ad85eb485fed8
	- Deleting S3 object with key 875e4bcf4b10a6a1144ad83158d84b6d
	- Deleting S3 object with key 20b869d98d61746dedd9aa33aa08a6fb
	- Deleting S3 object with key c513cedc4db6bc184ce30e94602741d6
	- Deleting S3 object with key c7a15d7d8d1c24b77a1eddf8caebc665
	- Deleting S3 object with key e8b8984f881c3732bfb34257cdd58f1e
	- Deleting S3 object with key 3185c59b550594ee7fca7f8c36686119.template
	- Deleting S3 object with key 30439348c0be6e1b85043b7a935b34ab.template
	- Deleting Cloudformation stack aws-app-composer-basic-api

Deleted successfully
```
