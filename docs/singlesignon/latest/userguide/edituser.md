# Edit Identity Center directory user properties

Use the following procedure to edit the properties of a user in your Identity Center
 directory. Alternatively, you can call the AWS API operation [UpdateUser](../IdentityStoreAPIReference/API_UpdateUser.md "../IdentityStoreAPIReference/API_UpdateUser.md") to update user properties.


Console
###### To edit user properties in IAM Identity Center

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Users**.
3. Choose the user that you want to edit.
4. On the user **Profile** page, next to **Profile
 details**, choose **Edit**.
5. On the **Edit profile details** page, update the
 properties as needed. Then, choose **Save changes**
 .


###### Note

(Optional) You can modify additional attributes such as **Employee
 number** and **Office 365 Immutable ID**
 to help map the user's identity in IAM Identity Center with certain business
 applications that users need to use. 


###### Note

The **Email address** attribute is an
 editable field and the value you provide must be unique.


AWS CLI
###### To edit user properties in IAM Identity Center


The following `update-user` command updates the user's
 nickname.



```
aws identitystore update-user \
    --identity-store-id d-1234567890 \
    --user-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --operations '{"AttributePath":"nickName","AttributeValue":"Johnny"}'
```
