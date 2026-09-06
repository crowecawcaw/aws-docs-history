

# Removing tags from a resource
<a name="sdk-untagresource"></a>

The following example shows how to use the [UntagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_UntagResource.html) function. This API supports all ACM resource types except the `certificate` resource type. For certificate resources, use [RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html).

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.UntagResourceRequest;

import java.util.ArrayList;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Specify the tag keys to remove.
        ArrayList<String> tagKeys = new ArrayList<>();
        tagKeys.add("Environment");

        // Create a request object.
        UntagResourceRequest req = new UntagResourceRequest()
            .withResourceArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123")
            .withTagKeys(tagKeys);

        // Remove the tags.
        client.untagResource(req);
    }
}
```