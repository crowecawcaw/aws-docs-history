

# Search discoverable resources
<a name="feature-store-cross-account-discoverability-use"></a>

The resource owner account must grant permissions to resource consumer accounts to allow for discoverability or access (read-only, read-write, or admin) privileges with a shared resource. In the following sections, we provide instructions on how to accept an invitation to shared resources and examples showing how to search for discoverable feature groups.

**Accept an invitation to shared resources**

As the resource consumer account, you receive an invitation to join a resource share once the resource owner account has granted permission. To accept the invitation to any shared resources, open the [Shared with me: Resource shares](https://console.aws.amazon.com/ram/home#SharedResourceShares) page in the AWS RAM console to view and respond to invitations. Invitations are not sent in these cases:
+ If you are part of an organization in AWS Organizations and sharing in your organization is enabled, then principals in the organization automatically get access to the shared resources without invitations.
+ If you share with the AWS account that owns the resource, then the principals in that account automatically get access to the shared resources without invitations.

For more information about accepting and using a resource share in AWS RAM, see [Respond to the resource share invitation](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html).

## Search discoverable feature groups example
<a name="feature-store-cross-account-discoverability-use-search"></a>

Once resources are shared with a resource consumer account with the discoverability permission applied, the resource consumer account can search for and discover the shared resources in Amazon SageMaker Feature Store using the console UI and the Feature Store SDK. Note that you cannot search on tags for cross account resources. The maximum number of feature group catalogs viewable is 1000. For more information about granting discoverability permissions, see [Enabling cross account discoverability](feature-store-cross-account-discoverability.md).

For details about viewing shared feature groups in the console, see [Find feature groups in your Feature Store](feature-store-search-feature-group-metadata.md).

In the following example, the resource consumer account uses SageMaker AI search to search for resources made discoverable to them when `CrossAccountFilterOption` is set to `"CrossAccount"`:

```
from sagemaker.core.helper.session_helper import Session

sagemaker_session = Session(boto_session=boto_session)

sagemaker_session.search(
    resource="FeatureGroup",
    search_expression={
        "Filters": [
            {
                "Name": "FeatureGroupName",
                "Value": "MyFeatureGroup",
                "Operator": "Contains",
            }
        ],
        "Operator": "And",
    },
    sort_by="Name",
    sort_order="Ascending",
    next_token="token",
    max_results=50,
    CrossAccountFilterOption="CrossAccount"
)
```

For more information about SageMaker AI search and the request parameters, see [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) in the Amazon SageMaker API Reference.