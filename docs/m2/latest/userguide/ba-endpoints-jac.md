AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Manage JICS application console in AWS Blu Age

The JICS component is the AWS Blu Age support for modernization of the legacy CICS resources. The
JICS application console web application is dedicated to administrate JICS resources. The
following endpoints allow to perform the administration tasks without having to interact with the
JAC user interface. Whenever an endpoint requires authentication, the request will have to include
authentication details (username/password typically, as required by Basic Authentication).
Endpoints for the JICS application console web application use the root path
`/jac/`.

###### Topics

- [JICS resources management](#ba-endpoints-jac-resources "#ba-endpoints-jac-resources")
- [Other](#ba-endpoints-jac-other "#ba-endpoints-jac-other")
- [JAC users management endpoints](#ba-endpoints-jac-users "#ba-endpoints-jac-users")

## JICS resources management

All following endpoints are related to JICS resources management, allowing JICS
administrators to deal with resources on daily basis.

###### Topics

- [List JICS LISTS and GROUPS](#list-jics-lists-groups "#list-jics-lists-groups")
- [Retrieve JICS resources](#retrieve-jics-resources "#retrieve-jics-resources")
- [List JICS GROUPS](#list-jics-groups "#list-jics-groups")
- [List JICS GROUPS for a given LIST](#list-jics-groups-given-list "#list-jics-groups-given-list")
- [LIST JICS resources for a given GROUP](#list-jics-resources-given-group "#list-jics-resources-given-group")
- [LIST JICS resources for a given GROUP
  (alternative using a name)](#list-jics-resources-given-group-alt "#list-jics-resources-given-group-alt")
- [Editing the owned GROUPS of several LISTS](#edit-owned-groups-lists "#edit-owned-groups-lists")
- [Delete a LIST](#delete-list "#delete-list")
- [Delete a GROUP](#delete-group "#delete-group")
- [Delete a TRANSACTION](#delete-transaction "#delete-transaction")
- [Delete a PROGRAM](#delete-program "#delete-program")
- [Delete a FILE](#delete-file "#delete-file")
- [Delete a TDQUEUE](#delete-tdqueue "#delete-tdqueue")
- [Delete a TSMODEL](#delete-tsmodel "#delete-tsmodel")
- [Delete elements](#delete-elements "#delete-elements")
- [Create a LIST](#create-list "#create-list")
- [Create a GROUP](#create-group "#create-group")
- [Common RESOURCES creation considerations](#common-create-considerations "#common-create-considerations")
- [Create a TRANSACTION](#create-transaction "#create-transaction")
- [Create a PROGRAM](#create-program "#create-program")
- [Create a FILE](#create-file "#create-file")
- [Create a TDQUEUE](#create-tdqueue "#create-tdqueue")
- [Create a TSMODEL](#create-tsmodel "#create-tsmodel")
- [Create elements](#create-elements "#create-elements")
- [Update a LIST](#update-list "#update-list")
- [Update a GROUP](#update-group "#update-group")
- [Common RESOURCES update considerations](#common-update-considerations "#common-update-considerations")
- [Update a TRANSACTION](#update-transaction "#update-transaction")
- [Update a PROGRAM](#update-program "#update-program")
- [Update a FILE](#update-file "#update-file")
- [Update a TDQUEUE](#update-tdqueue "#update-tdqueue")
- [Update a TSMODEL](#update-tsmodel "#update-tsmodel")
- [Update elements](#update-elements "#update-elements")
- [Upsert elements](#upsert-elements "#upsert-elements")
- [Retrieve elements](#retrieve-elements "#retrieve-elements")
- [JICS CRUD operation](#jics-crud-operation "#jics-crud-operation")

### List JICS LISTS and GROUPS

The LIST and GROUPS are the main owning container resources within the JICS component. All
JICS resources must belong to a GROUP. Groups can belong to LISTS, but this is not mandatory.
LISTS might even not exist on a given JICS environment, but most of the time, LISTS are there to
give an extra layer of organization for resources. For more information about the CICS resources
organization, see [CICS resources](https://www.ibm.com/docs/en/cics-ts/6.1?topic=fundamentals-how-it-works-cics-resources "https://www.ibm.com/docs/en/cics-ts/6.1?topic=fundamentals-how-it-works-cics-resources").

- Supported method: GET
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/listJicsListsAndGroups`
- Arguments: None
- Returns: a list of serialized JicsContainer objects, both LISTS and GROUPS, as
  JSON.

Sample response:

```
[
    {
      "name": "Resources",
      "children": [
        {
          "jacType": "JACList",
          "name": "MURACHS",
          "isActive": true,
          "children": [
            {
              "jacType": "JACGroup",
              "name": "MURACHS",
              "isActive": true,
              "children": []
            }
          ]
        },
        {
          "jacType": "JACGroup",
          "name": "TEST",
          "isActive": true,
          "children": []
        }
      ],
      "isExpanded": true
    }
  ]
```

### Retrieve JICS resources

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/retrieveJicsResources`
- Arguments: A JSON payload that represents the JICS resources that you want to retrieve.
  This is the JSON serialization of a
  `com.netfective.bluage.jac.entities.request.RetrieveOperationRequest`
  object.
- Returns: A list of serialized JicsResource objects. The objects are returned in no
  particular order and are of different types, like PROGRAM, TRANSACTION, FILE, and so
  on.

### List JICS GROUPS

- Supported method: GET
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/listJicsGroups`
- Arguments: None
- Returns a list of serialized JicsContainer objects (GROUPS) as JSON. The GROUPS are
  returned without their owning LIST information.

Sample response:

```
[
    {
      "jacType": "JACGroup",
      "name": "MURACHS",
      "isActive": true,
      "children": []
    },
    {
      "jacType": "JACGroup",
      "name": "TEST",
      "isActive": true,
      "children": []
    }
  ]
```

### List JICS GROUPS for a given LIST

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/listGroupsForList`
- Arguments: a JSON payload, representing the JICS LIST whose GROUPS you're looking for.
  This is the JSON serialization of a `com.netfective.bluage.jac.entities.JACList`
  object.

Sample request:

```
{
    "jacType":"JACList",
    "name":"MURACHS",
    "isActive":true
  }
```

- Returns a list of serialized JicsContainer objects (GROUPS) as JSON, that are attached to
  the given LIST. The GROUPS are returned without their owning LIST information.

Sample response:

```
[
    {
      "jacType": "JACGroup",
      "name": "MURACHS",
      "isActive": true,
      "children": []
    }
  ]
```

### LIST JICS resources for a given GROUP

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/listResourcesForGroup`
- Arguments: a JSON payload, representing the JICS GROUP whose resources you're looking
  for. This is the JSON serialization of a
  `com.netfective.bluage.jac.entities.JACGroup` object. You do not need to specify
  all fields for the GROUP, but the name is mandatory.

Sample request:

```
{
    "jacType":"JACGroup",
    "name":"MURACHS",
    "isActive":true
  }
```

- Returns a list of serialized JicsResource objects, owned by the given GROUP. The objects
  are returned in no particular order and are of different types, like PROGRAM, TRANSACTION,
  FILE, and so on.

### LIST JICS resources for a given GROUP

(alternative using a name)

- Supported method: POST
- Requires authentication
- Path: `/api/services/rest/jicsservice/listResourcesForGroupName`
- Arguments: the name of the GROUP owning the resources you're looking for.
- Returns: a list of serialized JicsResource objects, owned by the given GROUP. The objects
  are being returned in no particular order and are of different types, like PROGRAM,
  TRANSACTION, FILE, and so on.

### Editing the owned GROUPS of several LISTS

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/editGroupsList`
- Arguments: a JSON representation of a collection of LISTS with children GROUPS;

Sample request:

```
[
  {
        "jacType": "JACList",
        "name": "MURACHS",
        "isActive": true,
        "children": [
          {
            "jacType": "JACGroup",
            "name": "MURACHS",
            "isActive": true,
            "children": []
          },
          {
            "jacType": "JACGroup",
            "name": "TEST",
            "isActive": true,
            "children": []
          }
        ]
  }
]
```

Prior to this editing, only the group named "MURACHS" belonged to the LIST named
"MURACHS". With this editing, you "add" the group named "TEST" to the LIST named
"MURACHS".

- Returns a boolean value. If the value is 'true', the LISTS modifications were
  successfully persisted to the underlying JICS storage.

### Delete a LIST

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteList`
- Arguments: a JSON payload, representing the JICS LIST to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACList` object.
- Returns a boolean value. If the value is 'true', the LIST deletion was successfully
  operated on the underlying JICS storage.

### Delete a GROUP

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteGroup`
- Arguments: a JSON payload, representing the JICS GROUP to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACGroup` object.
- Returns a boolean value. If the value is 'true', the GROUP deletion was successfully
  operated on the underlying JICS storage.

### Delete a TRANSACTION

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteTransaction`
- Arguments: a JSON payload, representing the JICS Transaction to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTransaction`
  object.
- Returns a boolean value. If the value is 'true', the TRANSACTION deletion was
  successfully operated on the underlying JICS storage.

### Delete a PROGRAM

- Supported method: POST
- Requires authentication and one the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteProgram`
- Arguments: a JSON payload, representing the JICS Program to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACProgram` object.
- Returns a boolean value. If the value is 'true', the PROGRAM deletion was successfully
  operated on the underlying JICS storage.

### Delete a FILE

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteFile`
- Arguments: a JSON payload, representing the JICS File to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACFile` object.
- Returns a boolean value. If the value is 'true', the FILE deletion was successfully
  operated on the underlying JICS storage.

### Delete a TDQUEUE

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteTDQueue`
- Arguments: a JSON payload, representing the JICS TDQUEUE to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTDQueue` object.
- Returns a boolean value. If the value is 'true', the TDQUEUE deletion was successfully
  operated on the underlying JICS storage.

### Delete a TSMODEL

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteTSModel`
- Arguments: a JSON payload, representing the JICS TSMODEL to delete. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTSModel` object.
- Returns a boolean value. If the value is 'true', the TSMODEL deletion was successfully
  operated on the underlying JICS storage.

### Delete elements

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/deleteElements`
- Arguments: A JSON payload that represents the JICS elements to delete.
- Returns a boolean value where `true` indicates that the deletion was
  successfully operated in the underlying JICS storage.

### Create a LIST

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createList`
- Arguments: a JSON payload, representing the JICS LIST to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACList` object.
- Returns a boolean value. If the value is 'true', the LIST was successfully created in the
  underlying JICS storage.

###### Note

The LIST will always be created empty. Attaching GROUPS to the LIST will require another
operation.

### Create a GROUP

- Supported method: POST
- Requires authentication and the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createGroup`
- Arguments: a JSON payload, representing the JICS GROUP to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACGroup` object.
- Returns a boolean value. If the value is 'true', the GROUP has been properly created in
  the underlying JICS storage.

###### Note

The GROUP will always be created empty. Attaching RESOURCES to the GROUP will require
additional operations (creating resources will automatically attach them to a given
GROUP.

### Common RESOURCES creation considerations

All the following endpoints are related to JICS RESOURCES creation and share some common
constraints: in the request payload to be sent to the endpoint, the `groupName` field
has to be valued.

GROUP ownership constraint:

No resource can be created without being attached to an existing group, and the endpoint
uses the groupName to retrieve the group to which this resource will be attached. The
`groupName` must point to the name of an existing GROUP. An error message with HTTP
STATUS 400 will be sent if the `groupName` is not pointing at an existing group in
the JICS underlying storage.

Unicity constraint within a GROUP:

A given resource with a given name must be unique within a given group. The check for
unicity will be performed by each resource creation endpoint. If the given payload does not
respect the unicity constraint, the endpoint will send a response with HTTP STATUS 400 (BAD
REQUEST) -- see the sample response below.

Sample payload: you try to create the transaction 'ARIT' in the 'TEST' group, but a
transaction with that name already exists in that group.

```
{
    "jacType":"JACTransaction",
    "name":"ARIT",
    "groupName":"TEST",
    "isActive":true
  }
```

You receive the following error response:

```
{
    "timestamp": 1686759054510,
    "status": 400,
    "error": "Bad Request",
    "path": "/jac/api/services/rest/jicsservice/createTransaction"
  }
```

Inspecting servers logs will confirm the origin of the issue:

```

2023-06-14 18:10:54 default         TRACE - o.s.w.m.HandlerMethod                    - Arguments: [java.lang.IllegalArgumentException: Transaction already present in the group, org.springframework.security.web.header.HeaderWriterFilter$HeaderWriterResponse@e34f6b8]
2023-06-14 18:10:54 default         ERROR - c.n.b.j.a.WebConfig                      - 400
java.lang.IllegalArgumentException: Transaction already present in the group
	at com.netfective.bluage.jac.server.services.rest.impl.JicsServiceImpl.createElement(JicsServiceImpl.java:1280)

```

### Create a TRANSACTION

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createTransaction`
- Arguments: a JSON payload, representing the JICS TRANSACTION to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTransaction`
  object.
- Returns a boolean value. If the value is 'true', the TRANSACTION was successfully created
  in the underlying JICS storage.

### Create a PROGRAM

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createProgram`
- Arguments: a JSON payload, representing the JICS PROGRAM to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACProgram` object.
- Returns a boolean value. If the value is 'true', the PROGRAM was successfully created in
  the underlying JICS storage.

### Create a FILE

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createFile`
- Arguments: a JSON payload, representing the JICS FILE to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACFile` object.
- Returns a boolean value. If the value is 'true', the FILE was successfully created in the
  underlying JICS storage.

### Create a TDQUEUE

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createTDQueue`
- Arguments: a JSON payload, representing the JICS TDQUEUE to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTDQueue` object.
- Returns a boolean value. If the value is 'true', the TDQUEUE was successfully created in
  the underlying JICS storage.

### Create a TSMODEL

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createTSModel`
- Arguments: a JSON payload, representing the JICS TSMODEL to create. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTSModel` object.
- Returns a boolean value where `true` indicates that the creation of elements
  was successfully operated in the underlying JICS storage.

### Create elements

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/createElements`
- Arguments: a JSON payload that represents the JICS elements to create.
- Returns a boolean value. If the value is 'true', the elements were successfully created
  in the underlying JICS storage.

### Update a LIST

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateList`
- Arguments: a JSON payload, representing the JICS LIST to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACList` object. There's no
  need to supply the children of the LIST; the LIST update mechanism won't take the children
  into account.
- Returns a boolean value. If the value is 'true', the LIST was successfully updated in the
  underlying JICS storage.

Updating the LIST 'isActive' flag will propagate to all owned elements of the LIST, that
is, all GROUPS owned by the LIST and all RESOURCES owned by those GROUPS. This is a convenient
way of deactivating a lot of resources with a single operation, over several GROUPS.

### Update a GROUP

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateGroup`
- Arguments: a JSON payload, representing the JICS GROUP to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACGroup` object. There's no
  need to supply the children of the GROUP, the GROUP update mechanism won't take this into
  account.
- Returns a boolean value. If the value is 'true', the GROUP was successfully updated in
  the underlying JICS storage.

###### Note

Updating the GROUP 'isActive' flag will propagate to all owned elements of the GROUP, that
is, all RESOURCES owned by the GROUP. This is a convenient way of deactivating a lot of
resources with a single operation within a given GROUP.

### Common RESOURCES update considerations

All following endpoints are about updating JICS RESOURCES. Using the `groupName`
field, you can change the owning GROUP of any JICS RESOURCE, provided the field value points to
an existing GROUP in the underlying JICS storage (otherwise, you will get a BAD REQUEST response
(HTTP STATUS 400) from the endpoint).

### Update a TRANSACTION

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateTransaction`
- Arguments: a JSON payload, representing the JICS TRANSACTION to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTransaction`
  object.
- Returns a boolean value. If the value is 'true', the TRANSACTION was successfully updated
  in the underlying JICS storage.

### Update a PROGRAM

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateProgram`
- Arguments: a JSON payload, representing the JICS PROGRAM to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACProgram` object.
- Returns a boolean value. If the value is 'true', the PROGRAM was successfully updated in
  the underlying JICS storage.

### Update a FILE

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateFile`
- Arguments: a JSON payload, representing the JICS FILE to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACFile` object.
- Returns a boolean value. If the value is 'true', the FILE was successfully updated in the
  underlying JICS storage.

### Update a TDQUEUE

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateTDQueue`
- Arguments: a JSON payload, representing the JICS TDQUEUE to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTDQueue` object.
- Returns a boolean value. If the value is 'true', the TDQueue was successfully updated in
  the underlying JICS storage.

### Update a TSMODEL

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateTSModel`
- Arguments: a JSON payload, representing the JICS TSMODEL to update. This is the JSON
  serialization of a `com.netfective.bluage.jac.entities.JACTSModel` object.
- Returns a boolean value. If the value is 'true', the TSMODEL was successfully updated in
  the underlying JICS storage.

### Update elements

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/updateElements`
- Arguments: A JSON payload that represents the elements to update.
- Returns a boolean value where `true` indicates that the elements update
  was successfully operated in the underlying JICS storage.

### Upsert elements

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/upsertElements`
- Arguments: A JSON payload that represents the elements to upsert.
- Returns a boolean value where `true` indicates that the elements upsert
  was successfully operated in the underlying JICS storage.

### Retrieve elements

- Supported method: GET
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/retrieveElements`
- Arguments: None
- Returns a list of all serialized JICS resources.

### JICS CRUD operation

- Supported method: POST
- Requires authentication and one of the following roles: ROLE_ADMIN, ROLE_SUPER_ADMIN,
  ROLE_USER
- Path: `/api/services/rest/jicsservice/jicsCrudOperation`
- Arguments: a JSON payload that represents the JICS resources you're looking for. This is
  the JSON serialization of a
  `com.netfective.bluage.jac.entities.request.JicsCrudOperationRequest`
  object.
- Returns a JSON payload that represents the response. This is the JSON serialization of a
  `com.netfective.bluage.jac.entities.request.JicsCrudOperationResponse`
  object.

## Other

###### Topics

- [JICS server health status](#jics-server-health "#jics-server-health")

### JICS server health status

- Supported method: GET
- Path: `/api/services/rest/jicsserver/serverIsUp`
- Arguments: None
- Returns: None. An HTTP STATUS 200 response indicates that the server is up and
  running.

## JAC users management endpoints

Use the following endpoints to manage user interactions.

###### Topics

- [Logging a user](#log-user "#log-user")
- [Testing if at least an user exists in the system](#test-user-exist "#test-user-exist")
- [Recording a new user](#record-new-user "#record-new-user")
- [User info](#user-info "#user-info")
- [Listing users](#list-users "#list-users")
- [Deleting a user](#delete-user "#delete-user")
- [Logout the current user](#logout-user "#logout-user")

### Logging a user

- Supported method: POST
- Path: `/api/services/security/servicelogin/login`
- Arguments: None
- Returns the JSON serialization of a
  `com.netfective.bluage.jac.entities.SignOn` object, representing the user whose
  credentials are provided in the current request. The password is hidden from the view in the
  returned object. The roles given to the used are being listed.

Sample response:

```
{
    "login": "some-admin",
    "password": null,
    "roles": [
      {
        "id": 0,
        "roleName": "ROLE_ADMIN"
      }
    ]
  }
```

### Testing if at least an user exists in the system

- Supported method: GET
- Path: `/api/services/security/servicelogin/hasAccount`
- Arguments: None
- Returns the boolean value `true` if at least one user other than the default
  super admin user has been created. Returns `false` otherwise.

### Recording a new user

- Supported method: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/security/servicelogin/recorduser`
- Arguments: the JSON serialization of a
  `com.netfective.bluage.jac.entities.SignOn` object, representing the user to be
  added to the storage. The Roles for the user should be defined, otherwise the user might not
  be able to use the JAC facility and endpoints.
- Returns the boolean value `true` if the user was successfully created. Returns
  `false` otherwise.

Sample request:

```
{
    "login": "simpleuser",
    "password": "simplepassword",
    "roles": [
      {
        "id": 2,
        "roleName": "ROLE_USER"
      }
    ]
  }
```

Only the following roles can be used when recording a new user:

- ROLE_ADMIN : can manage JICS resources and users.
- ROLE_USER : can manage JICS resources but not users.

### User info

- Supported method: GET
- Path: `/api/services/security/servicelogin/userInfo`
- Arguments: None
- Returns the username and roles of the currently connected user.

### Listing users

- Supported method: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/security/servicelogin/listusers`
- Arguments: None
- Returns a list of `com.netfective.bluage.jac.entities.SignOn`, serialized as
  JSON.

### Deleting a user

- Supported method: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/security/servicelogin/deleteuser`
- Arguments: the JSON serialization of a
  `com.netfective.bluage.jac.entities.SignOn` object that represents the user to be
  removed from the storage.
- Returns the boolean value `true` if the user was successfully removed.

###### Important

This action cannot be undone. The deleted user won't be able to connect to the JAC
application again.

### Logout the current user

- Supported method: GET
- Path: `/api/services/security/servicelogout/logout`
- Arguments: None
- Returns the JSON message `{"success":true}` if the current user was
  successfully logged out. The related HTTP session will be invalidated.
