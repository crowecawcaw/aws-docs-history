# Amazon Verified Permissions example template-linked policies

When you create a policy store in Verified Permissions using the **Sample policy store** method,
your policy store is created with predefined policies, policy templates, and a schema for the sample project
you chose. The following Verified Permissions template-linked policy examples can be used with the sample policy stores and their
respective policies, policy templates, and schemas.

## PhotoFlash

examples

The following example shows how you might create a template-linked policy that uses the policy template **Grant limited access to non-private shared
photos** with an individual user and photo.

###### Note

Cedar policy language considers an entity to be `in` itself. Therefore,
`principal in User::"Alice"` is equivalent to `principal ==
 User::"Alice"`.

```
permit (
 principal in PhotoFlash::User::"Alice",
 action in PhotoFlash::Action::"SharePhotoLimitedAccess",
 resource in PhotoFlash::Photo::"VacationPhoto94.jpg"
 );
```

The following example shows how you might create a template-linked policy that uses the policy template **Grant limited access to non-private shared
photos** with an individual user and album.

```
permit (
 principal in PhotoFlash::User::"Alice",
 action in PhotoFlash::Action::"SharePhotoLimitedAccess",
 resource in PhotoFlash::Album::"Italy2023"
 );
```

The following example shows how you might create a template-linked policy that uses the policy template **Grant limited access to non-private shared
photos** with a friend group and individual photo.

```
permit (
 principal in PhotoFlash::FriendGroup::"Jane::MySchoolFriends",
 action in PhotoFlash::Action::"SharePhotoLimitedAccess",
 resource in PhotoFlash::Photo::"VacationPhoto94.jpg"
 );
```

The following example shows how you might create a template-linked policy that uses the policy template **Grant limited access to non-private shared
photos** with a friend group and album.

```
permit (
 principal in PhotoFlash::FriendGroup::"Jane::MySchoolFriends",
 action in PhotoFlash::Action::"SharePhotoLimitedAccess",
 resource in PhotoFlash::Album::"Italy2023"
 );
```

The following example shows how you might create a template-linked policy that uses the policy template **Grant full access to non-private shared
photos** with a friend group and an individual photo.

```
permit (
 principal in PhotoFlash::UserGroup::"Jane::MySchoolFriends",
 action in PhotoFlash::Action::"SharePhotoFullAccess",
 resource in PhotoFlash::Photo::"VacationPhoto94.jpg"
 );
```

The following example shows how you might create a template-linked policy that uses the policy template **Block user from an
account**.

```
forbid(
 principal == PhotoFlash::User::"Bob",
 action,
 resource in PhotoFlash::Account::"Alice-account"
 );
```

## DigitalPetStore examples

The DigitalPetStore sample policy store does not include any policy templates. You can view the policies
included with the policy store by choosing **Policies** in the navigation pane
on the left after creating the **DigitalPetStore** sample policy store.

## TinyToDo

examples

The following example shows how you might create a template-linked policy that uses the policy template that gives viewer access for an individual user and
task list.

```
permit (
    principal == TinyTodo::User::"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_h2aKCU1ts|5ae0c4b1-6de8-4dff-b52e-158188686f31|bob",
    action in [TinyTodo::Action::"ReadList", TinyTodo::Action::"ListTasks"],
    resource == TinyTodo::List::"1"
);
```

The following example shows how you might create a template-linked policy that uses the policy template that gives editor access for an individual user and
task list.

```
permit (
    principal == TinyTodo::User::"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_h2aKCU1ts|5ae0c4b1-6de8-4dff-b52e-158188686f31|bob",
    action in [
        TinyTodo::Action::"ReadList",
        TinyTodo::Action::"UpdateList",
        TinyTodo::Action::"ListTasks",
        TinyTodo::Action::"CreateTask",
        TinyTodo::Action::"UpdateTask",
        TinyTodo::Action::"DeleteTask"
    ],
    resource == TinyTodo::List::"1"
);
```
