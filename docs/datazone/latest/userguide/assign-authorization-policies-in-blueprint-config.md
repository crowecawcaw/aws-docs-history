# Assign authorization

policies within Amazon DataZone blueprint configurations

Another way to use the authorization mechanism in Amazon DataZone is to apply authorization
policies to projects and domain unit owners within Amazon DataZone blueprint configurations.

An Amazon DataZone blueprint configuration is an entity that encapsulates information
needed to create and configure resources used in publishing and subscribing user
workflows. This information includes AWS account number and region, CFN templates,
account level parameters such as VPCs and subnets, and can also contain database
connection information and credentials. To control costs and improve security, data
platform users require the ability to control who can use these blueprints and create
environments.

Within a specific blueprint configuration, you can assign the following authorization
policies to projects and domain unit owners:

- Create environment profiles using this blueprint - this policy can be assigned
  to Amazon DataZone projects and it authorizes them to create environment profiles
  using this blueprint.
- Grant permissions to create environment profiles using this blueprint - this
  policy can be assigned to domain unit owners and it authorizes them to grant
  permissions to projects to create environment profiles using this blueprint.

###### Assign the **Create environment profiles using this blueprint**

authorization policy to projects from a blueprint configuration via the Amazon DataZone
data portal

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the data portal, choose the domain that has the enabled blueprint that you
   want to work with, and then navigate to the **Blueprint
   configurations** tab.
3. In the **Blueprint configurations** tab, choose the enabled
   blueprint that you want to work with, then in this blueprint's details page,
   navigate to the **Authorization policies** tab, and then choose
   the **Create environment profiles using this blueprint**
   authorization policy.
4. In the **Create environment profiles using this blueprint**
   authorization policy details page, expand **Actions** and
   choose **Add projects**.
5. In the **Add projects** pop up window, you can do one of the
   following:
   - Choose the **All projects in a domain unit** option,
     then search for and specify the domain units that contain the projects
     that you want to authorize to create environment profiles with this
     blueprint, and then choose **Add projects**.
   - Choose the **Selected projects in a domain unit**
     option, then search for and specify the domain units that contain the
     projects to which you want to assign this policy, then seach for and
     choose the projects to which you want to assign this policy, and then
     choose **Add projects**.

###### Assign the \*\*Grant permissions to create environment profiles using this

blueprint\*\* authorization policy to domain unit owners from a blueprint
configuration via the Amazon DataZone management console

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. In the Amazon DataZone console, choose the domain that has the enabled blueprint
   that you want to work with, and then navigate to the **Blueprints** tab.
3. In the **Blueprints** tab, choose the enabled blueprint that
   you want to work with, and then in the blueprint's details page, navigate to the
   **Delegated permissions** tab.
4. In the **Delegated permissions** tab, search for and choose
   domain units to the owners of which you want to assign the **Grant
   permissions to create environment profiles using this blueprint**
   policy, and then choose **Add delegated permission**.
