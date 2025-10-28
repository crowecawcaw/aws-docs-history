# Enable or disable blueprints

You can complete the following procedure to enable or disable blueprints in the Amazon
SageMaker management console:

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Blueprints**
   tab.
4. In the **Blueprints** tab, use the radio buttons to select
   the blueprints that you want to enable or disable and then choose the
   **Enable** or **Disable** buttons to
   perform the action.

###### Important

When you enable a blueprint, by default, you are enabling it in the same region as
your domain. When you are enabling blueprints for a project profile that is created
and enabled in a different region from your domain, you must enable these blueprints
in same region where this project profile is enabled (in addition to enabling this
blueprint in the same region as your domain). You can do this via the
**Regions** tab in the blueprint details page. This applies to
all blueprints, including the Tooling blueprint.
