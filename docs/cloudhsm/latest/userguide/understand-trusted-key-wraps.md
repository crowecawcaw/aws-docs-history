# Understanding trusted keys in AWS CloudHSM

A *trusted key* is a key that is used to wrap other keys and that admins and cryptographic officers (COs) specifically
 identify as trusted using the attribute `CKA_TRUSTED`. Additionally, admins and cryptographic officers (COs) 
 use `CKA_UNWRAP_TEMPLATE` and related attributes to specify what actions data keys can do once they are unwrapped
 by a trusted key. Data keys that are unwrapped by the trusted key must also contain these attributes for the unwrap
 operation to succeed, which helps ensure that unwrapped data keys are only permitted for the use you intend.

Use the attribute `CKA_WRAP_WITH_TRUSTED` to identify all of the data keys you want to wrap with
 trusted keys. Doing this allows you to restrict data keys so applications can only use trusted
 keys to unwrap them. Once you set this attribute on the data keys, the attribute becomes read-only
 and you cannot change it. With these attributes in place, applications can only unwrap
 your data keys with the keys you trust, and unwraps always result in data keys with attributes that limit how these keys can be used.
