For api overview and usages, check out [this page](overview.md).

[TOC]

# Authentication

## Login

```
POST /api/auth/login
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | email of the user. 
password | password of the user.

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

**Response**
```json

Status: 200 OK
{
    "auth_token": "eyJ0eXAiOiJKV1QiL",
    "email": "ak123@fueled.com",
    "id": "f9dceed1-0f19-49f4-a874-0c2e131abf79",
    "first_name": "",
    "last_name": ""
}
```

## Register

```
POST /api/auth/register
```

**Parameters**

Name     | Description
---------|-------------------------------------
email    | email of the user. Errors out if email already registered.
password | password of the user.

**Request**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```

**Response**
```json

Status: 201 Created
{
    "auth_token": "eyJ0eXAiOiJKV1QiLCJh",
    "email": "test@test.com",
    "id": "f9dceed1-0f19-49f4-a874-0c2e131abf79",
    "first_name": "",
    "last_name": ""
}
```

## Change password

```
POST /api/auth/password_change (requires authentication)
```

**Parameters**

Name             | Description
-----------------|-------------------------------------
current_password | Current password of the user.
new_password     | New password of the user.

**Request**
```json
{
    "current_password": "NotSoSafePassword",
    "new_password": "VerySafePassword0909"
}
```

**Response**
```
Status: 204 No-Content
```


## Confirm password reset

Confirm password reset for the user using the token sent in email.

```
POST /api/auth/password_reset_confirm
```

**Parameters**

Name          | Description
--------------|-------------------------------------
new_password  | New password of the user
token         | Token decoded from the url (verification link)


**Request**
```json
{
    "new_password": "new_pass",
    "token" : "IgotTHISfromTHEverificationLINKinEmail"
}
```

**Response**
```
Status: 204 No-Content
```

**Note**
- The verification link uses the format of key `password-confirm` in `FRONTEND_URLS` dict in settings/common.


# Current user actions

## Get profile of current logged-in user
```
GET /api/me (requires authentication)
```

__Response__

```json
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "first_name": "John",
    "last_name": "Hawley",
    "email": "john@localhost.com"
}
```

## Update profile of current logged-in user
```
PATCH /api/me (requires authentication)
```

__Example__
```json
{
    "first_name": "James",
    "last_name": "Warner"
}
```

__Response__

```json
{
    "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
    "first_name": "James",
    "last_name": "Warner",
    "email": "john@localhost.com",
}
```

# Tenant - Company

## Listing all the Companies
```
GET /api/company (require admin or is_staff authentication)
```

__Response__

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "13c01ee9-490a-42c6-9f11-b21f4694c1ad",
            "created_at": "2018-09-05T16:45:32.917423+05:30",
            "modified_at": "2018-09-05T16:45:32.917451+05:30",
            "name": "New",
            "admin": null,
            "tenant_aware_suffix": "new"
        },
        {
            "id": "92151529-d822-4656-9e02-5c4b6d99a092",
            "created_at": "2018-09-05T17:21:10.153887+05:30",
            "modified_at": "2018-09-05T17:25:44.030515+05:30",
            "name": "Old",
            "admin": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6",
            "tenant_aware_suffix": "old"
        }
    ]
}
```

## Adding a new Company
```
POST /api/company (require admin or is_staff authentication)
```

**Parameters**

Name                | Description
--------------------|-------------------------------------
name                | Name of the Company
tenant_aware_suffix | A 'Alphabetic' string which will be used to access the company api

__Example__
```json
{
    "name": "Old",
    "tenant_aware_suffix": "old"
}
```

__Response__

```json
{
    "id": "92151529-d822-4656-9e02-5c4b6d99a092",
    "created_at": "2018-09-05T17:21:10.153887+05:30",
    "modified_at": "2018-09-05T17:21:10.153911+05:30",
    "name": "Old",
    "admin": null,
    "tenant_aware_suffix": "old"
}
```

## Adding a user as Company Admin
```
PATCH /api/company/:id (require admin/is_staff authentication)
```

**Parameters**

Name          | Description
--------------|-------------------------------------
admin         | A registered User's id


__Example__
```json
{
    "admin": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6"
}
```

__Response__

```json
{
    "id": "92151529-d822-4656-9e02-5c4b6d99a092",
    "created_at": "2018-09-05T17:21:10.153887+05:30",
    "modified_at": "2018-09-05T17:25:44.030515+05:30",
    "name": "Old",
    "admin": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6",
    "tenant_aware_suffix": "old"
}
```

## Listing all Company Employee
```
GET /api/:tenant_aware_suffix (require admin/id_staff or Company Admin authentication)
```

__Response__
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6",
            "created_at": "2018-09-05T19:05:21.929355+05:30",
            "modified_at": "2018-09-05T19:05:21.929382+05:30",
            "first_name": "Shashank",
            "last_name": "Kumar",
            "email": "abc@shanky.xyz",
            "company": "Old"
        }
    ]
}
```

## Adding Employee to Company
```
POST /api/:tenant_aware_suffix (require admin/id_staff or Company Admin authentication)
```

**Parameters**

Name          | Description
--------------|-------------------------------------
id            | A registered User's id

__Example__
```json
{
    "id": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6"
}
```

__Response__
```json
{
    "id": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6",
    "created_at": "2018-09-05T19:05:21.929355+05:30",
    "modified_at": "2018-09-05T19:05:21.929382+05:30",
    "first_name": "Shashank",
    "last_name": "Kumar",
    "email": "abc@shanky.xyz",
    "company": "Old"
}
```

## Retrieving Employee Detail of the Company
```
GET /api/:tenant_aware_suffix/:id (require admin/id_staff or Company Admin or Employee authentication)
```

__Example__
```
GET localhost/api/old/8ce5d8f8-623c-40e0-8a1e-676eb80b09b6
```

__Response__
```json
{
    "id": "8ce5d8f8-623c-40e0-8a1e-676eb80b09b6",
    "created_at": "2018-09-05T19:05:21.929355+05:30",
    "modified_at": "2018-09-05T19:05:21.929382+05:30",
    "first_name": "Shashank",
    "last_name": "Kumar",
    "email": "abc@shanky.xyz",
    "company": "Old"
}
```

## Removing a Employee from the Company
```
DELETE /api/:tenant_aware_suffix/:id (require admin/id_staff or Company Admin or Employee authentication)
```

__Response__
```
204 No Content
```

