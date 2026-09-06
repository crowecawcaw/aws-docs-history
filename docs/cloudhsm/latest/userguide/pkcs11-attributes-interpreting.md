

# PKCS \#11 library attributes tables for AWS CloudHSM Client SDK 5
<a name="pkcs11-attributes-interpreting"></a>

The PKCS \#11 library tables for AWS CloudHSM contain a list of attributes that differ by key types. It indicates whether a given attribute is supported for a particular key type when using a specific cryptographic function with AWS CloudHSM.

**Legend:**
+ ✔ indicates that CloudHSM supports the attribute for the specific key type.
+ ✖ indicates that CloudHSM does not support the attribute for the specific key type.
+ R indicates that the attribute value is set to read-only for the specific key type.
+ S indicates that the attribute cannot be read by the `GetAttributeValue` as it is sensitive.
+ An empty cell in the Default Value column indicates that there is no specific default value assigned to the attribute.

## GenerateKeyPair
<a name="generatekeypair"></a>


<table>
<thead>
  <tr><th>Attribute</th><th colspan="6">Key Type</th><th><b>Default Value</b></th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td><b>EC private</b></td><td><b>EC public</b></td><td><b>RSA private</b></td><td><b>RSA public</b></td><td><b>ML-DSA private</b></td><td><b>ML-DSA public</b></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CLASS</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_KEY_TYPE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LABEL</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_ID</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LOCAL</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_TOKEN</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE</code></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ENCRYPT</code></td><td>✖</td><td>✔<a href="#f10">3</a></td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DECRYPT</code></td><td>✔<a href="#f10">3</a></td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DERIVE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_MODIFIABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_DESTROYABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_SIGN</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_SIGN_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VERIFY</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_VERIFY_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_WRAP</code></td><td>✖</td><td>✔<a href="#f10">3</a></td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_WRAP_TEMPLATE</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_TRUSTED</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_WRAP_WITH_TRUSTED</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP</code></td><td>✔<a href="#f10">3</a></td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP_TEMPLATE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_SENSITIVE</code></td><td>✔<a href="#f8">1</a></td><td>✖</td><td>✔<a href="#f8">1</a></td><td>✖</td><td>✔</td><td>✖</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ALWAYS_SENSITIVE</code></td><td>R</td><td>✖</td><td>R</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXTRACTABLE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_NEVER_EXTRACTABLE</code></td><td>R</td><td>✖</td><td>R</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS_BITS</code></td><td>✖</td><td>✖</td><td>✖</td><td> ✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_1</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_2</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_COEFFICIENT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_1</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_2</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIVATE_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PUBLIC_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_PARAMS</code></td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_POINT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE_LEN</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_CHECK_VALUE</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_CLOUDHSM_PARAMETER_SET</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td></td><td></td></tr>
</tbody>
</table>


## GenerateKey
<a name="generatekey"></a>


<table>
<thead>
  <tr><th>Attribute</th><th colspan="3">Key Type</th><th><b>Default Value</b></th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td><b>AES</b></td><td><b>DES3</b></td><td><b>Generic Secret</b></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CLASS</code></td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_KEY_TYPE</code></td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LABEL</code></td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_ID</code></td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LOCAL</code></td><td>R </td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_TOKEN</code></td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE</code></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ENCRYPT</code></td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DECRYPT</code></td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DERIVE</code></td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_MODIFIABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_DESTROYABLE</code></td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_SIGN</code></td><td>✔ </td><td>✔</td><td>✔</td><td>True </td><td></td></tr>
  <tr><td><code>CKA_SIGN_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VERIFY</code></td><td>✔ </td><td>✔</td><td>✔</td><td>True </td><td></td></tr>
  <tr><td><code>CKA_VERIFY_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_WRAP</code></td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_WRAP_TEMPLATE</code></td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_TRUSTED</code></td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_WRAP_WITH_TRUSTED</code></td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP</code></td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP_TEMPLATE</code></td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_SENSITIVE</code></td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ALWAYS_SENSITIVE</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXTRACTABLE</code></td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_NEVER_EXTRACTABLE</code></td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS_BITS</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_1</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_2</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_COEFFICIENT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_1</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_2</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIVATE_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PUBLIC_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_PARAMS</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_POINT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE_LEN</code></td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✔<a href="#f9">2</a></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CHECK_VALUE</code></td><td>R </td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>


## CreateObject
<a name="createobject"></a>

**ML-DSA and CreateObject**  
ML-DSA key import through `C_CreateObject` is not supported. To use ML-DSA keys, generate them directly on the HSM using `C_GenerateKeyPair`.


<table>
<thead>
  <tr><th>Attribute</th><th colspan="7">Key Type</th><th><b>Default Value</b></th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td><b>EC private</b></td><td><b>EC public</b></td><td><b>RSA private</b></td><td><b>RSA public</b></td><td><b>AES</b></td><td><b>DES3</b></td><td><b>Generic Secret</b></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CLASS</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td></td><td></td></tr>
  <tr><td><code>CKA_KEY_TYPE</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td></td><td></td></tr>
  <tr><td><code>CKA_LABEL</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_ID</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LOCAL</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_TOKEN</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE</code></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ENCRYPT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DECRYPT</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DERIVE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_MODIFIABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_DESTROYABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_SIGN</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_SIGN_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_VERIFY</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_VERIFY_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_WRAP</code></td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_WRAP_TEMPLATE</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_TRUSTED</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_WRAP_WITH_TRUSTED</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP_TEMPLATE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_SENSITIVE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ALWAYS_SENSITIVE</code></td><td>R</td><td>✖</td><td>R</td><td>✖</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXTRACTABLE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔ </td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_NEVER_EXTRACTABLE</code></td><td>R</td><td>✖</td><td>R</td><td>✖</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS</code></td><td>✖</td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS_BITS</code></td><td>✖</td><td>✖</td><td>✖</td><td> ✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_1</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_2</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_COEFFICIENT</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_1</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_2</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIVATE_EXPONENT</code></td><td>✖</td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PUBLIC_EXPONENT</code></td><td>✖</td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_PARAMS</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_POINT</code></td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE</code></td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✖</td><td>✖</td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE_LEN</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_CHECK_VALUE</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>


## UnwrapKey
<a name="unwrapkey"></a>


<table>
<thead>
  <tr><th>Attribute</th><th colspan="5">Key Type</th><th><b>Default Value</b></th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td><b>EC private</b></td><td><b>RSA private</b></td><td><b>AES</b></td><td><b>DES3</b></td><td><b>Generic Secret</b></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CLASS</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td></td><td></td></tr>
  <tr><td><code>CKA_KEY_TYPE</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td></td><td></td></tr>
  <tr><td><code>CKA_LABEL</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_ID</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LOCAL</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_TOKEN</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE</code></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ENCRYPT</code></td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DECRYPT</code></td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DERIVE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_MODIFIABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_DESTROYABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_SIGN</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_SIGN_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_VERIFY</code></td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_VERIFY_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_WRAP</code></td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP</code></td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_SENSITIVE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_EXTRACTABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_NEVER_EXTRACTABLE</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_ALWAYS_SENSITIVE</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS_BITS</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_1</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_2</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_COEFFICIENT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_1</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_2</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIVATE_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PUBLIC_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_PARAMS</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_POINT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE_LEN</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_CHECK_VALUE</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>


## DeriveKey
<a name="derivekey"></a>


<table>
<thead>
  <tr><th>Attribute</th><th colspan="3">Key Type</th><th><b>Default Value</b></th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td><b>AES</b></td><td><b>DES3</b></td><td><b>Generic Secret</b></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CLASS</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td></td><td></td></tr>
  <tr><td><code>CKA_KEY_TYPE</code></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td>✔<a href="#f9">2</a></td><td></td><td></td></tr>
  <tr><td><code>CKA_LABEL</code></td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_ID</code></td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td><code>CKA_LOCAL</code></td><td>R</td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_TOKEN</code></td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE</code></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>True</td><td></td></tr>
  <tr><td><code>CKA_ENCRYPT</code></td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DECRYPT</code></td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_DERIVE</code></td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_MODIFIABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_DESTROYABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_SIGN</code></td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_SIGN_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VERIFY</code></td><td>✔</td><td>✔</td><td>✔</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_VERIFY_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_WRAP</code></td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP</code></td><td>✔</td><td>✔</td><td>✖</td><td>False</td><td></td></tr>
  <tr><td><code>CKA_SENSITIVE</code></td><td>R</td><td>R</td><td>R</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_EXTRACTABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>True</td><td></td></tr>
  <tr><td><code>CKA_NEVER_EXTRACTABLE</code></td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_ALWAYS_SENSITIVE</code></td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_MODULUS_BITS</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_1</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIME_2</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_COEFFICIENT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_1</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_2</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PRIVATE_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_PUBLIC_EXPONENT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_PARAMS</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_EC_POINT</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE</code></td><td>✖</td><td>✖</td><td>✖</td><td> </td><td></td></tr>
  <tr><td><code>CKA_VALUE_LEN</code></td><td>✔<a href="#f9">2</a></td><td>✖</td><td>✔<a href="#f9">2</a></td><td> </td><td></td></tr>
  <tr><td><code>CKA_CHECK_VALUE</code></td><td>R</td><td>R</td><td>R</td><td> </td><td></td></tr>
</tbody>
</table>


## GetAttributeValue
<a name="getattributevalue"></a>


<table>
<thead>
  <tr><th>Attribute</th><th colspan="9">Key Type</th><th></th></tr>
</thead>
<tbody>
  <tr><td> </td><td><b>EC private</b></td><td><b>EC public</b></td><td><b>RSA private</b></td><td><b>RSA public</b></td><td><b>ML-DSA private</b></td><td><b>ML-DSA public</b></td><td><b>AES</b></td><td><b>DES3</b></td><td><b>Generic Secret</b></td><td></td></tr>
  <tr><td><code>CKA_CLASS</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_KEY_TYPE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_LABEL</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_ID</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_LOCAL</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>R</td><td>R</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_TOKEN</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE</code></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔</td><td>✔</td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td>✔<a href="#f8">1</a></td><td></td></tr>
  <tr><td><code>CKA_ENCRYPT</code></td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_DECRYPT</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_DERIVE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_MODIFIABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_DESTROYABLE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_SIGN</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_SIGN_RECOVER</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_VERIFY</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_VERIFY_RECOVER</code></td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_WRAP</code></td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_WRAP_TEMPLATE</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_TRUSTED</code></td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_WRAP_WITH_TRUSTED</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP</code></td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_UNWRAP_TEMPLATE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_SENSITIVE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_EXTRACTABLE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_NEVER_EXTRACTABLE</code></td><td>✔</td><td>✖</td><td>✔</td><td>✖</td><td>R</td><td>R</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_ALWAYS_SENSITIVE</code></td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td></td></tr>
  <tr><td><code>CKA_MODULUS</code></td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_MODULUS_BITS</code></td><td>✖</td><td>✖</td><td>✖</td><td> ✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_PRIME_1</code></td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_PRIME_2</code></td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_COEFFICIENT</code></td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_1</code></td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_EXPONENT_2</code></td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_PRIVATE_EXPONENT</code></td><td>✖</td><td>✖</td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_PUBLIC_EXPONENT</code></td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_EC_PARAMS</code></td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_EC_POINT</code></td><td>✖</td><td>✔</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_VALUE</code></td><td>S</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_VALUE_LEN</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>✔</td><td>✖</td><td>✔</td><td></td></tr>
  <tr><td><code>CKA_CHECK_VALUE</code></td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✖</td><td>✖</td><td>✔</td><td>✔</td><td>✖</td><td></td></tr>
  <tr><td><code>CKA_CLOUDHSM_PARAMETER_SET</code></td><td>✖</td><td>✖</td><td>✖</td><td>✖</td><td>R</td><td>R</td><td>✖</td><td>✖</td><td>✖</td><td></td></tr>
</tbody>
</table>


**Attribute annotations**
+ [1] This attribute is partially supported by the firmware and must be explicitly set only to the default value.
+ [2] Mandatory attribute.
+ [3] For Ed25519 keys (EC keys with ed25519 curve): CKA\_ENCRYPT, CKA\_DECRYPT, CKA\_WRAP, CKA\_UNWRAP, and CKA\_DERIVE are not functional. Ed25519 keys are signing-only and do not support encryption, wrapping, or key derivation operations.