End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Managing applications in the AWS Panorama console

Use the AWS Panorama console to manage deployed applications.

###### Sections

- [Update or copy an application](#applications-manage-clone "#applications-manage-clone")
- [Delete versions and applications](#applications-manage-delete "#applications-manage-delete")

## Update or copy an application

To update an application, use the **Replace** option. When you replace an application, you
can update its code or models.

###### To update an application

1. Open the AWS Panorama console [Deployed applications page](https://console.aws.amazon.com/panorama/home#deployed-applications "https://console.aws.amazon.com/panorama/home#deployed-applications").
2. Choose an application.
3. Choose **Replace**.
4. Follow the instructions to create a new version or application.

There is also a **Clone** option that acts similar to **Replace**, but
doesn't remove the old version of the application. You can use this option to test changes to an application
without stopping the running version, or to redeploy a version that you've already deleted.

## Delete versions and applications

To clean up unused application versions, delete them from your appliances.

###### To delete an application

1. Open the AWS Panorama console [Deployed applications page](https://console.aws.amazon.com/panorama/home#deployed-applications "https://console.aws.amazon.com/panorama/home#deployed-applications").
2. Choose an application.
3. Choose **Delete from device**.
