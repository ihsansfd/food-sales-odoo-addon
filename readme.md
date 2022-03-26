### Description
Simple module (addon) to make point of sales of foods

### CRUD
- Product
- Recipe
- Customer
- Order

### Additional Features
- PDF Report
- Record Tracking

### API

#### **Base URL**
`localhost:{PORT}/api/product/`

#### **Method**
`GET`

#### **Auth**
`Public`

#### **Request Type**
`http`


#### **Response Type**
`json/application`

#### **Path Parameters**

| Parameter | Type | Description |
| - | -  | - |
| `{id}` |  Integer  |   ID of product  |

#### **Query Parameters**
Use this to filter your query

| Parameter | Type | Description |
| - | -  | - |
| `name`      |   String    |    Product's name    |
| `category`      |   String    |   Product's category    |
| `Active`      |   Boolean    |    Is product archived (inactive) or not (active)?    |

#### **Success Response**
Data is found:
```json
{
    "code": 400,
    "found": true,
    "data": [
        {
            "id": 2,
            "name": "Plain Brownies",
            "price": 20000.0,
            "desc": "Ok",
            "category": "appetizer"
        }
    ]
}
```

Data is not found:
```json
{
    "code": 400,
    "found": false,
    "data": []
}
```

