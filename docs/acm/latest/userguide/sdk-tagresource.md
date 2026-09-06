

# Tagging a resource
<a name="sdk-tagresource"></a>

The following example shows how to use the [TagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_TagResource.html) function. This API supports all ACM resource types except the `certificate` resource type. For certificate resources, use [AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html).

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.TagResourceRequest;
import com.amazonaws.services.certificatemanager.model.Tag;

import java.util.ArrayList;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Specify the tags to add.
        Tag tag1 = new Tag()
            .withKey("Environment")
            .withValue("Production");

        ArrayList<Tag> tags = new ArrayList<>();
        tags.add(tag1);

        // Create a request object.
        TagResourceRequest req = new TagResourceRequest()
            .withResourceArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123")
            .withTags(tags);

        // Tag the resource.
        client.tagResource(req);
    }
}
```