# POST with adobe flash (AWS signature
 version 2)

This section describes how to use `POST` with Adobe Flash.

## Adobe flash player security


By default, the Adobe Flash Player security model prohibits Adobe Flash Players
 from making network connections to servers outside the domain that serves the SWF
 file.


To override the default, you must upload a publicly readable crossdomain.xml file to
 the bucket that will accept POST uploads. The following is a sample crossdomain.xml
 file.



```
<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM
"http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
<allow-access-from domain="*" secure="false" />
</cross-domain-policy>
```

###### Note

For more information about the Adobe Flash security model, go to the Adobe
 website.

Adding the crossdomain.xml file to your bucket allows any Adobe Flash
 Player to connect to the crossdomain.xml file within your bucket; however, it
 does not grant access to the actual Amazon S3 bucket.


## Adobe flash considerations


 The FileReference API in Adobe Flash adds the `Filename`
 form field to the POST request. When you build Adobe Flash applications that upload
 to Amazon S3 by using the FileReference API action, include the following condition in your policy: 



```
['starts-with', '$Filename', '']
```

Some versions of the Adobe Flash Player do not properly handle HTTP responses that
 have an empty body. To configure POST to return a response that does not have an
 empty body, set `success_action_status` to 201. Amazon S3
 will then return an XML document with a 201 status code. For information about the content of
 the XML document, see [POST Object](RESTObjectPOST.md "RESTObjectPOST.md"). For information about form fields, see 
 [HTML form fields](HTTPPOSTForms.md#HTTPPOSTFormFields "HTTPPOSTForms.md#HTTPPOSTFormFields").
