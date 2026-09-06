

# Listing tags for a resource
<a name="sdk-listtagsforresource"></a>

The following example shows how to use the [ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html) function. This API supports all ACM resource types except the `certificate` resource type. For certificate resources, use [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html).

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListTagsForResourceRequest;
import com.amazonaws.services.certificatemanager.model.ListTagsForResourceResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create a request object.
        ListTagsForResourceRequest req = new ListTagsForResourceRequest()
            .withResourceArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123");

        // List the tags.
        ListTagsForResourceResult result = client.listTagsForResource(req);
        System.out.println(result);
    }
}
```