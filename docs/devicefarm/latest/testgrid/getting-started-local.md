# Migrating to Device Farm desktop browser testing from local Selenium

WebDrivers

If you're testing browsers locally, you can use the desktop browser testing feature to test on Firefox, Edge,
and Chrome without setting up those browsers.

Traditional local testing with Selenium involves tests that start a WebDriver component, such as
`GeckoDriver` or `ChromeDriver`. These components directly interact with a browser
under test, without the use of an intermediary. This means that your browsers are running where your tests are
running:

![Diagram showing local computer components: Test Suites, browsers, and Web Application interconnected.](images/testgrid-localtests-shared.png)
A common solution is to add an intermediary, Selenium Server, that runs browsers remotely. Often, this
results in your tests being run on your CI server with a headless browser. Your infrastructure now looks like
this:

![Diagram showing test suites, Selenium Server, browsers, and web application interconnected.](images/testgrid-local-ci-shared.png)
When you use Selenium Server (or Selenium Grid), you create a `RemoteWebDriver` instance that acts
as a stand-in for your browser-specific `WebDriver`.

###### Important

We recommend that you follow the standard security advice of granting least privilege—that is, granting only the
permissions required to perform a task—when you configure the AWS SDK and AWS CLI with credentials. For more
information, see [AWS Security
Credentials](../../../general/latest/gr/aws-security-credentials.md "../../../general/latest/gr/aws-security-credentials.md") and [IAM Best
Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

###### To migrate

This procedure shows you how to configure your local `WebDriver` tests to use Selenium's
`RemoteWebDriver` with a URL from the `GetTestGridUrl` API call.

To perform these steps, you need an AWS account and a working set of tests.

1. To keep track of your sessions, you must create a project.

Console

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
Use the `create-test-grid-project` command to create a project:

```
aws devicefarm create-test-grid-project --name "`Peculiar Things`"
```

Make a note of the project ARN, which is used by your application:

```
{
    "testGridProject": {
        "arn": "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`",
        "name": "`Peculiar Things`"
    }
}
```

###### Note

To update your project configuration, see [Configuring your project to use Amazon VPC
endpoints](techref-vpc.md#techref-vpc-configure "techref-vpc.md#techref-vpc-configure"). 2. To use the desktop browser testing feature, you must install and configure the [AWS SDK](https://aws.amazon.com/getting-started/tools-sdks/#SDKs "https://aws.amazon.com/getting-started/tools-sdks/#SDKs") for the language appropriate for your
tests. 3. Modify your environment to include your AWS access and secret keys. The steps vary depending on your
configuration, but involve setting two environment variables:

###### Important

We recommend that you follow the standard security advice of granting least privilege—that is, granting only the
permissions required to perform a task—when you configure the AWS SDK and AWS CLI with credentials. For more
information, see [AWS Security
Credentials](../../../general/latest/gr/aws-security-credentials.md "../../../general/latest/gr/aws-security-credentials.md") and [IAM Best
Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

```
AWS_ACCESS_KEY_ID=`AKIAIOSFODNN7EXAMPLE`
AWS_SECRET_ACCESS_KEY=`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
```

4. ######

Instead of creating a `WebDriver` for your browser (for example, `GeckoDriver`)
create a `RemoteWebDriver` and get a URL from the desktop browser testing feature.

Java

###### Note

This example uses JUnit 5 and the AWS SDK for Java 2.x. For more information about the AWS SDK for Java 2.x, see
[AWS SDK for Java 2.x API Reference](../../../sdk-for-java/latest/reference.md "../../../sdk-for-java/latest/reference.md"). If you are using a different test framework, be aware that `@Before` and
`@After` are called before and after each test, respectively.

```
// Import the AWS SDK for Java 2.x Device Farm client:
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.devicefarm.*;
import software.amazon.awssdk.services.devicefarm.model.*;
import java.net.URL;

// in your tests ...
public class MyTests {
  // ... When you set up your test suite
  private static RemoteWebDriver driver;

  @Before
  void setUp() {
    String myProjectARN = "arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`";
    DeviceFarmClient client  = DeviceFarmClient.builder().region(Region.US_WEST_2).build();
    CreateTestGridUrlRequest request = CreateTestGridUrlRequest.builder()
      .expiresInSeconds(300)
      .projectArn(myProjectARN)
      .build();
    CreateTestGridUrlResponse response = client.createTestGridUrl(request);
    URL testGridUrl = new URL(response.url());
    // You can now pass this URL into RemoteWebDriver.
    WebDriver driver = new RemoteWebDriver(testGridUrl, DesiredCapabilities.firefox());
  }

  @After
  void tearDown() {
    // make sure to close your WebDriver:
    driver.quit();
  }

}
```

For more information, see [Migrating a Java test suite to Device Farm](testing-frameworks-java.md "testing-frameworks-java.md").

Python

###### Important

This example is written with the assumption you are using Python 3 with pytest. If you are using another
testing framework, see the documentation.

```

# Include boto3, the Python SDK's main package:
import boto3, pytest

# in your tests:
# Set up the Device Farm client, get a driver URL:
class myTestSuite:
  def setup_method(self, method):
    devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
    testgrid_url_response = devicefarm_client.create_test_grid_url(
      projectArn="arn:aws:devicefarm:us-west-2:`111122223333`:testgrid-project:`123e4567-e89b-12d3-a456-426655440000`",
      expiresInSeconds=300)
    self. driver = selenium.webdriver.Remote(testgrid_url_response["url"], `selenium.webdriver.DesiredCapabilities.FIREFOX`)

  # later, make sure to end your WebDriver session:
  def teardown_method(self, method):
    self.driver.quit()
```

For more information, see [Migrating Python tests to Device Farm desktop browser testing](testing-frameworks-python.md "testing-frameworks-python.md").

For a list of supported capabilities, see [Supported capabilities, browsers, and platforms in Device Farm desktop browser
testing](techref-support.md "techref-support.md") 5. Run your tests as you would normally.
