End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Tutorial: Query AWS IoT SiteWise data in AWS IoT Analytics

This tutorial demonstrates how to query AWS IoT SiteWise data in
AWS IoT Analytics. The tutorial uses data from a demo in AWS IoT SiteWise that provides a sample set of data for a
wind farm.

###### Important

You will be charged for the resources that this demo creates and consumes.

###### Topics

- [Prerequisites](#tutorial-prerequisites "#tutorial-prerequisites")
- [Load and verify data](tutorial-step1.md "tutorial-step1.md")
- [Data exploration](tutorial-step2.md "tutorial-step2.md")
- [Run statistical queries](tutorial-step3.md "tutorial-step3.md")
- [Cleaning up your tutorial resources](tutorial-step4.md "tutorial-step4.md")

## Prerequisites

For this tutorial, you need the following resources:

- You must have an AWS account to get started with AWS IoT SiteWise and AWS IoT Analytics. If you
  don't have one, follow the procedures in [To create an AWS
  account](quickstart.md#quickstart-console-signin "quickstart.md#quickstart-console-signin").
- A development computer running Windows, macOS, Linux, or Unix to access the
  AWS Management Console. For more information, see [Getting Started with the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").
- AWS IoT SiteWise data that defines AWS IoT SiteWise models and assets and streams data that
  represents data from wind farm equipment. To create your data, follow the steps
  in [Creating the AWS IoT SiteWise demo](../../../iot-sitewise/latest/userguide/getting-started-demo.md#create-getting-started-demo "../../../iot-sitewise/latest/userguide/getting-started-demo.md#create-getting-started-demo") in the
  _AWS IoT SiteWise User Guide_.
- Your AWS IoT SiteWise demo wind farm equipment data in an existing data store that you manage. For more information
  about how to create a data store for your AWS IoT SiteWise data, see [Configure storage
  settings](../../../iot-sitewise/latest/userguide/configure-storage.md "../../../iot-sitewise/latest/userguide/configure-storage.md") in the _AWS IoT SiteWise User Guide_.

###### Note

Your AWS IoT SiteWise metadata appears in your AWS IoT SiteWise data store soon after
creation; however, it can take up to six hours for your raw data to appear.
In the meantime, you can create an AWS IoT Analytics dataset and run queries on your
metadata.

### Next step

[Load and verify data](tutorial-step1.md "tutorial-step1.md")
