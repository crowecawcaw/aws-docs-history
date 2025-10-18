# HTTP 404 status code (Not Found)

CloudFront returns a 404 (Not Found) error when the client attempts to access a resource
 that doesn’t exist. If you receive this error with your CloudFront distribution, common
 causes include the following:


* Resource doesn't exist.
* URL is incorrect.
* Custom origin returning a 404.
* Custom error pages returning a 404. (Any error code might be translated to
 404.) For more information, see [How CloudFront processes errors when
 you have configured custom error pages](HTTPStatusCodes.md#HTTPStatusCodes-custom-error-pages "HTTPStatusCodes.md#HTTPStatusCodes-custom-error-pages").
* Custom error page accidentally deleted, resulting in a 404 because the
 request looks for the deleted custom error page. For more information, see
 [How CloudFront processes errors if
 you haven't configured custom error pages](HTTPStatusCodes.md#HTTPStatusCodes-no-custom-error-pages "HTTPStatusCodes.md#HTTPStatusCodes-no-custom-error-pages").
* Incorrect origin path. If the origin path is populated, its value is
 appended to the path of each request from the browser before the request is
 forwarded to the origin. For more information, see [Origin path](DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath "DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath").
