# Idempotency and Concurrency

## Idempotency Keys

AWS HealthLake supports idempotency keys for FHIR `POST` operations, providing a
robust mechanism to ensure data integrity during resource creation. By including a unique UUID
as an idempotency key in the request header, healthcare applications can guarantee that each
FHIR resource is created exactly once, even in scenarios involving network instability or
automatic retries.

This feature is particularly crucial for healthcare systems where duplicate medical
records could have serious consequences. When a request is received with the same idempotency
key as a previous request, HealthLake will return the original resource instead of creating a
duplicate. For example, this could occur during a retry loop or due to redundant request
pipelines. Using the idempotency key allows HealthLake to maintain data consistency while providing
a seamless experience for client applications handling intermittent connectivity
issues.

### Implementation

```
`POST` /<baseURL>/Patient
x-amz-fhir-idempotency-key: 123e4567-e89b-12d3-a456-426614174000
{
    "resourceType": "Patient",
    "name": [...]
}
```

### Response Scenarios

First Request (201 Created)

- New resource created successfully
- Response includes resource ID

Duplicate Request (409 Conflict)

- Same idempotency key detected
- Original resource returned
- No new resource created

Invalid Request (400 Bad Request)

- Malformed UUID
- Missing required fields

### Best Practices

- Generate unique UUID for each new resource creation
- Store idempotency keys for retry logic
- Use consistent key format: UUID v4 recommended
- Implement in client applications handling resource creation

###### Note

This feature is particularly valuable for healthcare systems requiring strict data
accuracy and preventing duplicate medical records.

## ETag in AWS HealthLake

AWS HealthLake uses ETags for optimistic concurrency control in FHIR resources, providing a
reliable mechanism to manage concurrent modifications and maintain data consistency. An ETag
is a unique identifier that represents a specific version of a resource, functioning as a
version control system through HTTP headers. When reading or modifying resources, applications
can use ETags to prevent unintended overwrites and ensure data integrity, particularly in
scenarios with potential concurrent updates.

### Implementation Example

```
// Initial Read
GET /fhir/Patient/123
Response:
ETag: W/"1"

// Update with If-Match
PUT /fhir/Patient/123
If-Match: W/"1"
{resource content}

// Create with If-None-Match
PUT /fhir/Patient/123
If-None-Match: *
{resource content}
// Succeeds only if resource doesn't exist
// Fails with 412 if resource exists
```

### Response Scenarios

Successful Operation (200 OK or 204 No Content)

- ETag matches current version
- Operation proceeds as intended

Version Conflict (412 Precondition Failed)

- ETag doesn't match current version
- Update rejected to prevent data loss

### Best Practices

- Include ETags in all update and delete operations
- Implement retry logic for handling version conflicts
- Use If-None-Match: \* for create-if-not-exists scenarios
- Always verify ETag freshness before modifications

This concurrency control system is essential for maintaining the integrity of healthcare
data, especially in environments with multiple users or systems accessing and modifying the
same resources.
