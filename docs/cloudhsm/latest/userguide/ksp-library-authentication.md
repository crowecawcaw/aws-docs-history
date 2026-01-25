# Authenticate to the Key storage provider (KSP) for AWS CloudHSM

Client SDK 5

Before you use the Key storage provider (KSP) for AWS CloudHSM Client SDK 5, you must set the login credentials for
the HSM on your system. You have two options:

- Windows Credentials Manager (recommended for better security)
- System environment variables (simpler setup)

## Windows Credential Manager

You can set up credentials using either the `set_cloudhsm_credentials`
utility or the Windows Credentials Manager interface.

- **Using the `set_cloudhsm_credentials`
  utility**:

The Windows installer includes the `set_cloudhsm_credentials`
utility. You can use this utility to conveniently pass HSM login credentials to
Windows Credential Manager. If you want to compile this utility from source, you
can use the Python code included in the installer.

    1. Navigate to `C:\Program
     Files\Amazon\CloudHSM\tools\`.
    2. Run the following command:



    ```
    set_cloudhsm_credentials.exe --username `<CU USER>` --password `<CU PASSWORD>`
    ```

- **Using the Credential Manager
  interface**:
  1.  Open Credential Manager:
      - Enter `credential manager` in the taskbar search
        box
      - Select **Credential Manager**

  2.  Select **Windows Credentials** to manage Windows
      credentials.
  3.  Select **Add a generic credential**
  4.  Enter the following details:
      - **Internet or Network Address**:
        `CLOUDHSM_PIN`.
      - **Username**: `<CU
USER>`.
      - **Password**: `<CU
PASSWORD>`.

  5.  Choose **OK**

## System environment variables

You can set system environment variables to identify your HSM and [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU).

###### Warning

Setting credentials through system environment variables stores your password in plaintext on your system. For better security, use Windows Credential Manager instead.

You can set environment variables using:

- The [**setx**](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/setx "https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/setx").
- The Windows **System Properties** Control Panel (**Advanced** tab).
- set permanent system environment variables [Programmatic](<https://msdn.microsoft.com/en-us/library/system.environment.setenvironmentvariable(v=vs.110).aspx> "https://msdn.microsoft.com/en-us/library/system.environment.setenvironmentvariable(v=vs.110).aspx") methods.

To set the system environment variable:

**`CLOUDHSM_PIN=`<CU USERNAME>`:`<CU
 PASSWORD>``**

Identifies a [crypto user](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli") (CU) in the HSM and
provides all required login information. Your application authenticates and
runs as this CU. The application has the permissions of this CU and can view
and manage only the keys that the CU owns and shares. To create a new CU,
use the [user create](cloudhsm_cli-user-create.md "cloudhsm_cli-user-create.md") command
in CloudHSM CLI. To find existing CUs, use the [user list](cloudhsm_cli-user-list.md "cloudhsm_cli-user-list.md") command in
CloudHSM CLI.

For example:

```
setx /m CLOUDHSM_PIN test_user:password123
```

###### Note

When setting CLOUDHSM_PIN environment variables, you must escape any special characters that may be interpreted by your shell.
