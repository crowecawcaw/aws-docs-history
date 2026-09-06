

# Errors and warnings from importing your API into API Gateway
<a name="api-gateway-import-api-errors-warnings"></a>

When you import your external definition file into API Gateway, API Gateway might generate warnings and errors. The following sections discuss the errors and warnings that might occur during import.

## Errors during import
<a name="api-gateway-import-api-errors"></a>

 During the import, errors can be generated for major issues like an invalid OpenAPI document. Errors are returned as exceptions (for example, `BadRequestException`) in an unsuccessful response. When an error occurs, the new API definition is discarded and no change is made to the existing API. 

## Warnings during import
<a name="api-gateway-import-api-warnings"></a>

 During the import, warnings can be generated for minor issues like a missing model reference. If a warning occurs, the operation will continue if the `failonwarnings=false` query expression is appended to the request URL. Otherwise, the updates will be rolled back. By default, `failonwarnings` is set to `false`. In such cases, warnings are returned as a field in the resulting [RestApi](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html) resource. Otherwise, warnings are returned as a message in the exception. 