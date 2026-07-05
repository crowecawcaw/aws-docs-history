# Listing ACME accounts

The following example shows how to use the [ListAcmeAccounts](../APIReference/API_ListAcmeAccounts.md "../APIReference/API_ListAcmeAccounts.md") function.

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
