

# Supported authentication methods
<a name="qbiz-indexes-supported-authentication"></a>

The authentication methods supported depend on your implementation type:

## IDC Implementation
<a name="qbiz-indexes-auth-idc"></a>
+ Amazon Quick: AWS Identity Center authentication only
+ Amazon Q Business: `AWS_IAM_IDC`

## Non-IDC Implementation
<a name="qbiz-indexes-auth-qbiz"></a>
+ Amazon Quick:
  + Native identities (username/password)
  + AWS Managed Microsoft AD
  + IAM federation
+ Amazon Q Business: `AWS_QUICKSIGHT_IDP`