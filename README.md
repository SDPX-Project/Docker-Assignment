## Docker Assignment

### 📦 Installation

**1. Run Docker**

```bash
docker-compose up 
```

**or run in background**

```bash
docker compose up -d 
```

**2. Open Browser**

- **api dev**  
  - **api** [http://localhost:8000](http//localhost:8000)
  - **phpmyadmin** [http://localhost:5050](http://localhost:5050)

- **api test**
  - **api** [http://localhost:8001](http//localhost:8001)
  - **phpmyadmin** [http://localhost:5051](http://localhost:5051)


### CRUD API
| api          | body                                         | method   |
| ------------ | -------------------------------------------- | -------- |
| `/user`      | Get All User                                 | GET      |
| `/user/:id`  | Get User By id                               | GET      |
| `/user/add`  | Create User                                  | POST     |
| `/user/update` | Update User                                | PUT      |
| `/user/delete/:id`| Delete User                             | DELETE   |