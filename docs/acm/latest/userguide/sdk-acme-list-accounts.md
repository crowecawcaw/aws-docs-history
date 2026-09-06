

# Listing ACME accounts
<a name="sdk-acme-list-accounts"></a>

The following example shows how to use the [ListAcmeAccounts](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeAccounts.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListAcmeAccountsRequest;
import com.amazonaws.services.certificatemanager.model.ListAcmeAccountsResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        ListAcmeAccountsRequest req = new ListAcmeAccountsRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withMaxResults(10);

        // List the ACME accounts.
        ListAcmeAccountsResult result = client.listAcmeAccounts(req);
        System.out.println(result);
    }
}
```