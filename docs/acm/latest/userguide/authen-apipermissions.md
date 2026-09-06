

# ACM API permissions: Actions and resources reference
<a name="authen-apipermissions"></a>

When you set up access control and write permissions policies that you can attach to an IAM user or role, you can use the following table as a reference. The first column in the table lists each AWS Certificate Manager API operation. You specify actions in a policy's `Action` element. The remaining columns provide the additional information: 

 You can use the IAM policy elements in your ACM policies to express conditions. For a complete list, see [Available Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*. 

**Note**  
 To specify an action, use the `acm:` prefix followed by the API operation name (for example, `acm:RequestCertificate`). 

Use the scroll bars to see the rest of the table.


**ACM API operations and permissions**  

| ACM API Operations | Required Permissions (API Operations) | Resources | 
| --- | --- | --- | 
| [AddTagsToCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_AddTagsToCertificate.html) | `acm:AddTagsToCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [DeleteCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html) | `acm:DeleteCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) | `acm:DescribeCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [ExportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExportCertificate.html) | `acm:ExportCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [GetAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAccountConfiguration.html) | `acm:GetAccountConfiguration` | `*` | 
| [GetCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetCertificate.html) | `acm:GetCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [ImportCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ImportCertificate.html) | `acm:ImportCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/*`<br />or<br />`*` | 
| [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html) | `acm:ListCertificates` | `*` | 
| [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html) | `acm:ListTagsForCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html) | `acm:ListTagsForResource` | `arn:aws:acm:{{region}}:{{account}}:{{resource-type}}/{{resource_ID}}` | 
| [PutAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_PutAccountConfiguration.html) | `acm:PutAccountConfiguration` | `*` | 
| [RemoveTagsFromCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RemoveTagsFromCertificate.html) | `acm:RemoveTagsFromCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 
| [RequestCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) | `acm:RequestCertificate` | `arn:aws:acm:{{region}}:{{account}}:certificate/*`<br />or<br />`*` | 
| [ResendValidationEmail](https://docs.aws.amazon.com/acm/latest/APIReference/API_ResendValidationEmail.html) | `acm:ResendValidationEmail` | arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate\_ID}} | 
| [SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html) | `acm:SearchCertificates` | `*` | 
| [TagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_TagResource.html) | `acm:TagResource` | `arn:aws:acm:{{region}}:{{account}}:{{resource-type}}/{{resource_ID}}` | 
| [UntagResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_UntagResource.html) | `acm:UntagResource` | `arn:aws:acm:{{region}}:{{account}}:{{resource-type}}/{{resource_ID}}` | 
| [UpdateCertificateOptions](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificateOptions.html) | `acm:UpdateCertificateOptions` | `arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}` | 