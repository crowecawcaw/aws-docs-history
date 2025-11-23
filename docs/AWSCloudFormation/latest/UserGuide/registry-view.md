# View the available and activated extensions in the

CloudFormation registry

To view the available and activated extensions in the CloudFormation registry, you can use
the AWS Management Console or the AWS CLI.

###### To view the available and activated extensions (console)

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your
   AWS Region.
3. From the navigation pane, under **Registry**, choose what
   extension category you want to view:
   - **Public extensions** displays the public extensions
     available in your account.
     1. For **Filter**, **Extension
        type**, choose your extension type:
        **Resource types**,
        **Modules**, or
        **Hooks**.
     2. For **Filter**,
        **Publisher**, choose a publisher:
        **AWS** or **Third
        party**.

   - **Activated extensions** displays the public and
     private extensions activated in your account.
     1. Choose your extension type: **Resource
        types**, **Modules**, or
        **Hooks**.
     2. Use the **Filter** drop-down menu to further
        choose the extensions to view:
        - **AWS** – lists extensions
          published by AWS. Extensions published by AWS are
          activated by default.
        - **Third-party** – lists any
          public extensions from publishers other than AWS that
          you have activated in this account.
        - **Registered** – lists any
          private extensions you have activated in this
          account.

   - **Publisher** displays any public extensions that you
     have published using this account.

4. Search or choose the extension name to view extension details.

###### To view the available and activated extensions (AWS CLI)

Use the [list-types](../../../cli/latest/reference/cloudformation/list-types.md "../../../cli/latest/reference/cloudformation/list-types.md") command.
