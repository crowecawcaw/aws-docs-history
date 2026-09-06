

# Retrieve attributes with the PKCS \#11 library for AWS CloudHSM Client SDK 5
<a name="pkcs11-attributes-retrieve"></a>

When your application reads attributes from a key or a certificate object, the PKCS \#11 library sends one request to your cluster for each `C_GetAttributeValue` call. The number of attributes in the template does not change the number of requests. One call that requests ten attributes sends one request. Ten calls that each request one attribute send ten requests.

Each call reads the object's attributes from your cluster in one request, and then copies the values that your template requests. The PKCS \#11 library does not cache the values, so every call sends a new request.

To reduce the number of requests that your application sends, follow these recommendations:
+ Request every attribute that you need in one template. Build a single template that contains all of the attributes that you want, and pass it to one `C_GetAttributeValue` call. The following example reads three attributes of a key with one call.

  ```
  CK_OBJECT_CLASS obj_class;
  CK_BYTE label[128];
  CK_BYTE id[128];
  
  CK_ATTRIBUTE attrs[] = {
          {CKA_CLASS, &obj_class, sizeof(obj_class)},
          {CKA_LABEL, label,       sizeof(label)},
          {CKA_ID,    id,          sizeof(id)},
  };
  
  rv = funcs->C_GetAttributeValue(session, object, attrs,
                                  sizeof(attrs) / sizeof(CK_ATTRIBUTE));
  ```

  For more information, see [List key attributes](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/attributes/) on the GitHub website.
+ Request only the attributes that your object supports and that you can read. When your template names an attribute that the object does not have, `C_GetAttributeValue` sets `ulValueLen` to `CK_UNAVAILABLE_INFORMATION` for that attribute and returns `CKR_ATTRIBUTE_TYPE_INVALID`. A sensitive attribute behaves the same way and returns `CKR_ATTRIBUTE_SENSITIVE`. In both cases, the other attributes in your template still receive their values. Check `ulValueLen` for each attribute instead of only the return value of the call. For the attributes that each object type supports, and for the attributes that are sensitive, see [PKCS \#11 library attributes tables for AWS CloudHSM Client SDK 5](pkcs11-attributes-interpreting.md).
+ Check how many calls your language binding makes. A PKCS \#11 binding for a language such as Python or Java decides how many `C_GetAttributeValue` calls it sends. Some bindings send one call for each attribute, and some send two. Use the interface that your binding provides for reading several attributes at once, and measure the calls that your application sends.
+ Cache attribute values in your application. Read the attributes of an object a single time, and store the values that your application needs. You can reuse a cached value until something changes the object. When other applications or users can modify your objects, refresh your cache after they do.
+ Allocate your buffers before you read an attribute. The PKCS \#11 standard describes a two-pass pattern for values of variable length. Your application calls `C_GetAttributeValue` with `pValue` set to `NULL_PTR` to learn the length, and then calls it again to read the value. Both calls send a request. When you know a buffer size that holds the values that you expect, allocate the buffers first and read the values with one call.

  A buffer that is too small returns `CKR_BUFFER_TOO_SMALL` for that attribute, and the call still sends a request. Choose buffer sizes that are generous enough for the values that you expect. Attributes that hold a template, such as `CKA_WRAP_TEMPLATE`, still need the two-pass pattern.

**Note**  
These recommendations apply to both key objects and certificate objects, and different limits apply to each. Certificate storage has a fixed read rate limit, and each `C_GetAttributeValue` call on a certificate object uses one read operation from it. For key objects, your HSMs throttle attribute reads when they reach capacity rather than at a fixed rate. The PKCS \#11 library retries those requests automatically. Sending fewer requests helps your application stay within both limits. For more information, see [Certificate storage limits](pkcs11-certificate-storage-limits.md) and [HSM throttling](troubleshoot-hsm-throttling.md).