# Using fine-grained

authorization with a SMART on FHIR enabled HealthLake data store

[Scopes](reference-smart-on-fhir-oauth-scopes.md#smart-on-fhir-scopes-rest "reference-smart-on-fhir-oauth-scopes.md#smart-on-fhir-scopes-rest") alone do not provide you with the
necessary specificity about what data a requester is authorized to access in a data store.
Using fine-grained authorization enables a higher level of specificity when granting access
to a SMART on FHIR enabled HealthLake data store. To use fine-grained authorization, set
`FineGrainedAuthorizationEnabled` equal to `True` in the
`IdentityProviderConfiguration` parameter of your `CreateFHIRDatastore`
request.

If you enabled fine-grained authorization, your authorization server returns a
`fhirUser` scope in the `id_token` along with the access token.
This permits information about the User to be retrieved by client application. The client
application should treat the `fhirUser` claim as the URI of a FHIR resource
representing the current user. This can be `Patient`, `Practitioner`,
or `RelatedPerson`. The authorization server's response also includes a
`user/` scope that defines what data the user can access. This uses the
syntax defined for scopes related to FHIR resource specific scopes:

```
user/(fhir-resource | '*').('read' | 'write' | '*')
```

The following are examples of how fine-grained authorization can be used to further
specify data access related FHIR resource types.

- When `fhirUser` is a `Practitioner`, fine-grained
  authorization determines the collection of patients that the user can access. Access
  to `fhirUser` is allowed for only those patients where the Patient has
  reference to the `fhirUser` as a General Practitioner.

```
Patient.generalPractitioner : [{Reference(Practitioner)}]
```

- When `fhirUser` is a `Patient` or `RelatedPerson`
  and the patient referenced in the request is different from the
  `fhirUser`, fine-grained authorization determines access to
  `fhirUser` for the requested patient. Access is allowed when there is
  a relationship specified in requested `Patient` resource.

```
Patient.link.other : {Reference(Patient|RelatedPerson)}
```
