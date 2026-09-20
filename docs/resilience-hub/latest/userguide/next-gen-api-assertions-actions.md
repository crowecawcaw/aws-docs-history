

# Assertions
<a name="next-gen-api-assertions-actions"></a>


| Action | Method | Description | 
| --- | --- | --- | 
| CreateAssertion | POST | Create a user-created assertion for a service. Assertion text can be up to 1,000 characters. | 
| UpdateAssertion | POST | Update the text of an assertion. Updating an AI-generated assertion changes its source to USER. | 
| ListAssertions | GET | List assertions for a service, optionally filtered by source (AI\_GENERATED or USER). | 
| DeleteAssertion | POST | Delete an assertion. | 