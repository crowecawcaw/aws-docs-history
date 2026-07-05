# Listing tags for a resource

The following example shows how to use the [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") function. This API supports all ACM resource types
except the `certificate` resource type. For certificate resources, use
[ListTagsForCertificate](../APIReference/API_ListTagsForCertificate.md "../APIReference/API_ListTagsForCertificate.md").

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
