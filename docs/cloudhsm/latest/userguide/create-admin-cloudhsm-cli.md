

# Create an HSM user admin using CloudHSM CLI
<a name="create-admin-cloudhsm-cli"></a>

Follow these steps to create a hardware security module (HSM) admin user using the CloudHSM CLI.

1. Use the following command to start CloudHSM CLI interactive mode.

------
#### [ Linux ]

   ```
   $ /opt/cloudhsm/bin/cloudhsm-cli interactive
   ```

------
#### [ Windows ]

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive
   ```

------

1. Use the **login** command and log in to the cluster as the admin.

   ```
   aws-cloudhsm > login --username {{<username>}} --role admin
   ```

1. The system prompts you for your password. Enter the password, and the output shows that the command was successful.

   ```
   Enter password:
   {
     "error_code": 0,
     "data": {
       "username": "{{<username>}}",
       "role": "admin"
     }
   }
   ```

1. Enter the following command to create an admin:

   ```
   aws-cloudhsm > user create --username {{<username>}} --role admin
   ```

1. Enter the password for the new user.

1. Re-enter the password to confirm the password you entered is correct.