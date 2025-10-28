# Limitations

The following are limitations for the Okta connector:

- For ‘Applications’ entity only one filter can be applied. If more than 1 filter is applied then 400 Bad Request is return with error summary –‘Invalid Search criteria’.
- Order by can be supported with search queries only. For example, `http://dev-15940405.okta.com/api/v1/groups?search=type e.q. "OKTA_GROUP"&sortBy=lastUpdated&sortOrder=asc`
