

# View the available and activated extensions in the CloudFormation registry
<a name="registry-view"></a>

To view the available and activated extensions in the CloudFormation registry, you can use the AWS Management Console or the AWS CLI.

**To view the available and activated extensions (console)**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose your AWS Region.

1. From the navigation pane, under **Registry**, choose what extension category you want to view:
   + **Public extensions** displays the public extensions available in your account.

     1. For **Filter**, **Extension type**, choose your extension type: **Resource types**, **Modules**, or **Hooks**.

     1. For **Filter**, **Publisher**, choose a publisher: **AWS** or **Third party**.
   + **Activated extensions** displays the public and private extensions activated in your account.

     1. Choose your extension type: **Resource types**, **Modules**, or **Hooks**.

     1. Use the **Filter** drop-down menu to further choose the extensions to view:
        + **AWS** – lists extensions published by AWS. Extensions published by AWS are activated by default.
        + **Third-party** – lists any public extensions from publishers other than AWS that you have activated in this account.
        + **Registered** – lists any private extensions you have activated in this account.
   + **Publisher** displays any public extensions that you have published using this account.

1. Search or choose the extension name to view extension details.

**To view the available and activated extensions (AWS CLI)**  
Use the [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) command.