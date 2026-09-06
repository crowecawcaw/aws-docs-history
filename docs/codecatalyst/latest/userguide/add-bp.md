

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Adding a custom blueprint to a space blueprints catalog
<a name="add-bp"></a>

After you publish a custom blueprint to your space, it can be added to your space's blueprints catalog. If you add a custom blueprint to your CodeCatalyst space’s blueprints catalog, then the blueprint is available to all space members to use when creating a project or adding it to an existing project. Before adding a custom blueprint to the space’s blueprints catalog, the blueprint’s publishing permission must be enabled. If you opted in for workflow release generation, then publishing permissions are enabled by default. For more information, see [Setting publishing permissions for a custom blueprint](manage-permissions-bp.md) and [Publishing a custom blueprint to a space](publish-bp.md).

**Important**  
To add a custom blueprint to your CodeCatalyst space's blueprints catalog, you must be signed in with an account that has the **Space administrator** or **Power user** role in the space.

**To add a blueprint to the space's blueprints catalog**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. The blueprint can only be added from the default branch of the source repository. If you developed the blueprint on a feature branch, merge your feature branch with the changes to the default branch. Create a pull request to merge any changes to the default branch. For more information, see [Reviewing code with pull requests in Amazon CodeCatalyst](source-pull-requests.md).

1. In the CodeCatalyst console, navigate to the space dashboard with your custom blueprint.

1. On the space dashboard, choose the **Settings** tab, and then choose **Blueprints**.

1. Choose the blueprint name you want to add, and then choose **Add to catalog**. If you have more than one version, choose a version from the **Catalog version** dropdown menu

1. Choose **Save**.