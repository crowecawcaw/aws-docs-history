The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Get the terms of an agreement using an AWS SDK

The following code example shows how to get the terms of an agreement.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code "https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code")
repository.

```
package com.example.awsmarketplace.agreementapi.seller;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementTermsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementTermsResponse;

public class GetAgreementTerms {

	public static void main(String[] args) {

		String agreementId = args.length > 0 ? args[0] : AGREEMENT_ID;

		GetAgreementTermsResponse getAgreementTermsResponse = getAgreementTermsResponse(agreementId);

		ReferenceCodesUtils.formatOutput(getAgreementTermsResponse);

	}

	public static GetAgreementTermsResponse getAgreementTermsResponse(String agreementId) {
		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

		GetAgreementTermsRequest getAgreementTermsRequest =
				GetAgreementTermsRequest.builder()
				.agreementId(agreementId)
				.build();

		GetAgreementTermsResponse getAgreementTermsResponse = marketplaceAgreementClient.getAgreementTerms(getAgreementTermsRequest);
		return getAgreementTermsResponse;
	}

}


```

- For API details, see
  [GetAgreementTerms](../../../goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementTerms.md "../../../goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementTerms.md")
  in _AWS SDK for Java 2.x API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
