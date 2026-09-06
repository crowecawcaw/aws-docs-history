

# How backend client certificate authentication works
<a name="rest-api-backend-auth-overview"></a>

With outbound mutual TLS (mTLS), API Gateway acts as a TLS client. It presents a client certificate to your backend server when it connects. Your backend checks this certificate to confirm that requests come from API Gateway.

Outbound mTLS is different from inbound mTLS. Inbound mTLS requires API clients to present certificates to API Gateway. Outbound mTLS secures the link between API Gateway and your backend.

## TLS handshake sequence
<a name="rest-api-backend-auth-overview-handshake"></a>

The following steps show how API Gateway sets up a mutual TLS connection with your backend:

1. API Gateway sends a ClientHello message to the backend.

1. The backend sends its server certificate to API Gateway.

1. API Gateway checks the server certificate.

1. The backend sends a CertificateRequest to API Gateway.

1. API Gateway sends the client certificate chain to the backend.

1. The backend checks the client certificate against its trust store.

1. The mutual TLS connection is ready. API Gateway forwards the API request.

If the backend does not request a client certificate in step 4, API Gateway finishes the TLS handshake without sending one. The connection uses standard one-way TLS.

## Compare certificate options
<a name="rest-api-backend-auth-overview-comparison"></a>

The following table compares the two approaches for configuring backend client certificates.


**ACM-managed compared with API Gateway-generated certificates**  

| Feature | ACM-managed certificates | API Gateway-generated certificates | 
| --- | --- | --- | 
| Certificate source | Your PKI or AWS Private Certificate Authority | API Gateway self-signed | 
| Configuration | Reference the certificate on the stage by its ACM ARN; manage the certificate lifecycle with ACM APIs. | Manage on the Client certificates page or with the API Gateway client certificate APIs. | 
| Renewal | Depends on how the certificate was issued. For certificates that ACM issues through AWS Private Certificate Authority, ACM renews them automatically and API Gateway propagates the update with no redeployment and no downtime. For certificates that you import into ACM, you must reimport them before expiration; API Gateway then propagates the reimport automatically. | Manual. Certificate expires after 365 days and must be rotated manually. | 
| Chain support | Full chain (up to 5 certificates) | Single self-signed certificate | 
| Backend trust model | Backend trusts your CA | Backend must pin the API Gateway certificate | 