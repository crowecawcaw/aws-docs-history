# ACM API permissions: Actions and resources reference

When you set up access control and write permissions policies that you can attach
to an IAM user or role, you can use the following table as a reference. The first
column in the table lists each AWS Certificate Manager API operation. You specify actions in a
policy's `Action` element. The remaining columns provide the additional
information:

You can use the IAM policy elements in your ACM policies to express
conditions. For a complete list, see [Available
Keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

###### Note

To specify an action, use the `acm:` prefix followed by the API
operation name (for example, `acm:RequestCertificate`).

Use the scroll bars to see the rest of the table.

| ACM API operations and permissions                                                                                               | ACM API Operations              | Required Permissions (API Operations)                         | Resources |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------- | --------- |
| [AddTagsToCertificate](../APIReference/API_AddTagsToCertificate.md "../APIReference/API_AddTagsToCertificate.md")                | `acm:AddTagsToCertificate`      | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [DeleteCertificate](../APIReference/API_DeleteCertificate.md "../APIReference/API_DeleteCertificate.md")                         | `acm:DeleteCertificate`         | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [DescribeCertificate](../APIReference/API_DescribeCertificate.md "../APIReference/API_DescribeCertificate.md")                   | `acm:DescribeCertificate`       | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [ExportCertificate](../APIReference/API_ExportCertificate.md "../APIReference/API_ExportCertificate.md")                         | `acm:ExportCertificate`         | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [GetAccountConfiguration](../APIReference/API_GetAccountConfiguration.md "../APIReference/API_GetAccountConfiguration.md")       | `acm:GetAccountConfiguration`   | `*`                                                           |
| [GetCertificate](../APIReference/API_GetCertificate.md "../APIReference/API_GetCertificate.md")                                  | `acm:GetCertificate`            | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [ImportCertificate](../APIReference/API_ImportCertificate.md "../APIReference/API_ImportCertificate.md")                         | `acm:ImportCertificate`         | `arn:aws:acm:`region`:`account`:certificate/*`<br>or<br>`*`   |
| [ListCertificates](../APIReference/API_ListCertificates.md "../APIReference/API_ListCertificates.md")                            | `acm:ListCertificates`          | `*`                                                           |
| [ListTagsForCertificate](../APIReference/API_ListTagsForCertificate.md "../APIReference/API_ListTagsForCertificate.md")          | `acm:ListTagsForCertificate`    | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [PutAccountConfiguration](../APIReference/API_PutAccountConfiguration.md "../APIReference/API_PutAccountConfiguration.md")       | `acm:PutAccountConfiguration`   | `*`                                                           |
| [RemoveTagsFromCertificate](../APIReference/API_RemoveTagsFromCertificate.md "../APIReference/API_RemoveTagsFromCertificate.md") | `acm:RemoveTagsFromCertificate` | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [RequestCertificate](../APIReference/API_RequestCertificate.md "../APIReference/API_RequestCertificate.md")                      | `acm:RequestCertificate`        | `arn:aws:acm:`region`:`account`:certificate/*`<br>or<br>`*`   |
| [ResendValidationEmail](../APIReference/API_ResendValidationEmail.md "../APIReference/API_ResendValidationEmail.md")             | `acm:ResendValidationEmail`     | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
| [UpdateCertificateOptions](../APIReference/API_UpdateCertificateOptions.md "../APIReference/API_UpdateCertificateOptions.md")    | `acm:UpdateCertificateOptions`  | `arn:aws:acm:`region`:`account`:certificate/`certificate_ID`` |
