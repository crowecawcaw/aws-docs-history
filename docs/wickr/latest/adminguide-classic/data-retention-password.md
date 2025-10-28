This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Password for data retention bot in

AWS Wickr

The first time you start the data retention bot, you specify the initial password
using one of the following options:

- The `WICKRIO_BOT_PASSWORD` environment variable. The data retention
  bot environment variables are outlined in the [Environment variables to configure
  data retention bot in AWS Wickr](data-retention-bot-env-variables.md "data-retention-bot-env-variables.md") section later in this
  guide.
- The **password** value in Secrets Manager identified by the
  `AWS_SECRET_NAME` environment variable. The Secrets Manager values for the
  data retention bot are outlined in the [Secrets Manager values for AWS Wickr](data-retention-aws-secret-values.md "data-retention-aws-secret-values.md") section later in this
  guide.
- Enter the password when prompted by the data retention bot. You will need to
  run the data retention bot with interactive TTY access using the
  `-ti`
  option.
  A new password will be generated when you configure the data retention bot for the
  first time. If you need to re-install the data retention bot, you use the generated
  password. The initial password is not valid after the initial installation of the data
  retention bot.

The new generated password will be displayed as shown in the following example.

###### Important

Save the password in a safe place. If you lose the password you will not be able
to re-install the data retention bot. Don't share this password. It provides the
ability to start data retention for your Wickr network.

```
********************************************************************
**** GENERATED PASSWORD
**** DO NOT LOSE THIS PASSWORD, YOU WILL NEED TO ENTER IT EVERY TIME
**** TO START THE BOT
 "HuEXAMPLERAW4lGgEXAMPLEn"
 ********************************************************************
```
