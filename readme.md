### Description
Simple Odoo module (addon) to make point of sales of foods

### CRUD
- Product
- Recipe
- Customer
- Order

### Additional Features
- PDF Report
- Record Tracking

### API

#### **Endpoint**
`localhost:{PORT}/api/product/`

##### **Method**
`GET`

##### **Auth**
`Public`

##### **Path Parameters**

| Parameter | Type | Description |
| - | -  | - |
| `{id}` |  Integer  |   ID of product  |

##### **Query Parameters**
Use this to filter your query. All of them are optional and make use of "AND" operator.

| Parameter | Type | Description |
| - | -  | - |
| `name`      |   String    |    Product's name    |
| `category`      |   String    |   Product's category    |
| `active`      |   Boolean    |    Is product archived (inactive) or not (active)?    |

##### **Success Response**
Data is found:
```json
{
    "code": 200,
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
    "code": 200,
    "found": false,
    "data": []
}
```

