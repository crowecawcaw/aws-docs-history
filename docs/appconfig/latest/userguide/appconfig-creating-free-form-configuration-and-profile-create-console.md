# Creating an AWS AppConfig freeform configuration profile (console)

Use the following procedure to create an AWS AppConfig freeform configuration profile and
(optionally) a freeform-configuration by using the AWS Systems Manager console.

###### To create a freeform configuration profile

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/ "https://console.aws.amazon.com/systems-manager/appconfig/").
2. In the navigation pane, choose **Applications**, and then choose
   an application you created in [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md "appconfig-creating-namespace.md").
3. Choose the **Configuration profiles and feature flags** tab, and
   then choose **Create configuration**.
4. In the **Configuration options** section, choose
   **Freeform configuration**.
5. For **Configuration profile name**, enter a name for the
   configuration profile.
6. (Optional) Expand **Description** and enter a description.
7. (Optional) Expand **Additional options** and complete the
   following, as necessary.
   1. In the **Associate extensions** section, choose an extension
      from the list.
   2. In the **Tags** section, choose **Add new
      tag**, and then specify a key and optional value.

8. Choose **Next**.
9. On the **Specify configuration data** page, in the
   **Configuration definition** section, choose an option.
10. Complete the fields for the option you selected, as described in the following
    table.

| Option selected                        | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS AppConfig hosted configuration** | Choose either **Text**, **JSON**, or<br>**YAML**, and enter your configuration in the field. Go<br>to Step 12 in this procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Amazon S3 object**                   | Enter the object URI in the \*_S3 object source_<br>• field<br>and go to Step 11 in this procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **AWS CodePipeline**                   | Choose \*_Next_<br>• and go to Step 12 in this<br>procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Secrets Manager secret**             | Choose the secret from the list go to Step 11 in this procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **AWS Systems Manager parameter**      | Choose the parameter from the list and go to Step 11 in this<br>procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **AWS Systems Manager document**       | 1. Choose a document from the list or choose **Create new<br>document**.<br>2. If you choose **Create new document**, for<br>**Document name**, enter a name. Optionally, expand<br>**Version name\*<br>• and enter a name for the document<br>version.<br>3. For **Application configuration schema**, either<br>choose the JSON schema from the list or choose **Create<br>schema**. If you choose **Create schema**,<br>Systems Manager opens the **Create schema*<br>• page. Enter the<br>schema details, and then choose **Create application<br>configuration schema**.<br>4. In the \*\*Content*<br>• section, choose either<br>**YAML\*<br>• or **JSON\*<br>• and then enter<br>the configuration data in the field. |

11. In the **Service role** section, choose **New service
    role** to have AWS AppConfig create the IAM role that provides access to the
    configuration data. AWS AppConfig automatically populates the **Role name**
    field based on the name you entered earlier. Or, choose **Existing service
    role**. Choose the role by using the **Role ARN**
    list.
12. Optionally, on the **Add validators** page, choose either
    **JSON Schema** or **AWS Lambda**. If you choose
    **JSON Schema**, enter the JSON Schema in the field. If you choose
    **AWS Lambda**, choose the function Amazon Resource Name (ARN) and
    the version from the list.

###### Important

Configuration data stored in SSM documents must validate against an associated
JSON Schema before you can add the configuration to the system. SSM parameters do
not require a validation method, but we recommend that you create a validation check
for new or updated SSM parameter configurations by using AWS Lambda. 13. Choose **Next**. 14. On the **Review and save** page, choose **Save and
continue to deploy**.

###### Important

If you created a configuration profile for AWS CodePipeline, then you must create a
pipeline in CodePipeline that specifies AWS AppConfig as the _deploy provider_. You
don't need to perform [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md "deploying-feature-flags.md"). However, you must configure a client to
receive application configuration updates as described in [Retrieving configuration data without AWS AppConfig Agent](about-data-plane.md "about-data-plane.md"). For information about
creating a pipeline that specifies AWS AppConfig as the deploy provider, see [Tutorial: Create a Pipeline that Uses
AWS AppConfig as a Deployment Provider](../../../codepipeline/latest/userguide/tutorials-AppConfig.md "../../../codepipeline/latest/userguide/tutorials-AppConfig.md") in the _AWS CodePipeline User Guide_.

Proceed to [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md "deploying-feature-flags.md").
