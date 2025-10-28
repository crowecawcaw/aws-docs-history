# Creating a Device Farm desktop browser testing project

You can use the Device Farm console or the AWS CLI to create a project.

Device Farm console

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. In the navigation pane, choose **Desktop Browser Testing**, and then
   choose **Projects**.
3. If you already have a project, under **Desktop browser testing
   projects**, choose the name of your project.

Otherwise, to create a new project, choose **New project**. Then, on the
**Create Project** page, do the following:

    1. Enter a **Project name**.
    2. (Optional) Enter a project **Description**.
    3. (Optional) Under **Virtual Private Cloud (VPC) Settings**, you can
     configure your project's VPC peering settings by choosing the **VPC**,
     its **Subnets**, and its **Security Groups**. For
     instructions on connecting Device Farm to a VPC, see [Working with
     Amazon Virtual Private Cloud across Regions](../developerguide/amazon-vpc-cross-region.md "../developerguide/amazon-vpc-cross-region.md") in the *Device Farm Developer Guide*.
    4. Choose **Create**.

4. In the project details, note the project's Amazon Resource Name (ARN). It looks like this:
   `arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000``.

###### Note

For instructions on updating your project configuration, see [Configuring your project to use Amazon VPC
endpoints](techref-vpc.md#techref-vpc-configure "techref-vpc.md#techref-vpc-configure").

AWS CLI
Use the `create-test-grid-project` command to create a
project:

```
aws devicefarm create-test-grid-project --name "My Web App"
```

The result contains the project that you just created:

```
{
    "testGridProject": {
        "arn": "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`",
        "name": "My Web App"
    }
}
```

###### Note

To update your project configuration, see [Configuring your project to use Amazon VPC
endpoints](techref-vpc.md#techref-vpc-configure "techref-vpc.md#techref-vpc-configure").
