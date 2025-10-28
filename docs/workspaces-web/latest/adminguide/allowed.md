# Allowed domains for Amazon WorkSpaces Secure Browser

For users to be able to access web portals from their local browser, you must add the
following domains to the allow list on the network the user is trying to access the
service from.

In the following table, replace `{region}` with the code of
the operating web portal's Region. For example,
s3.`{region}`.amazonaws.com should be
s3.eu-west-1.amazonaws.com for a web portal the Europe (Ireland) region.
For a list of Region codes, see [Amazon WorkSpaces Secure Browser endpoints and quotas](../../../general/latest/gr/workspacesweb.md "../../../general/latest/gr/workspacesweb.md").

| Category                                        | Domain or IP address                                                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WorkSpaces Secure Browser streaming assets      | s3.`{region}`.amazonaws.com s3.amazonaws.com appstream2.`{region}`.aws.amazon.com \*.amazonappstream.com \*.shortbread.aws.dev        |
| WorkSpaces Secure Browser static assets         | \*.workspaces-web.com di5ry4hb4263e.cloudfront.net                                                                                    |
| WorkSpaces Secure Browser authentication        | \*.auth.`{region}`.amazoncognito.com cognito-identity.`{region}`.amazonaws.com cognito-idp.`{region}`.amazonaws.com \*.cloudfront.net |
| WorkSpaces Secure Browser metrics and reporting | \*.execute-api.`{region}`.amazonaws.com unagi-na.amazon.com                                                                           | Depending on your configured identity provider, you might also need to allow list additional domains. Review your IdP’s documentation to identify which domains you need to allow list in order for WorkSpaces Secure Browser to use that provider. If you are using IAM Identity Center, see [IAM Identity Center prerequisites](../../../singlesignon/latest/userguide/prereqs.md "../../../singlesignon/latest/userguide/prereqs.md") for more information. |
