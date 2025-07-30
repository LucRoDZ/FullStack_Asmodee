# Asmodee Fullstack Developer Assignment

This project is a simple fullstack application that allows customers to place orders from a list of products.

- Backend: **FastAPI** (Python)
- Frontend: **Vue 3** + **Vite**
- Order persistence: JSON file in `./backend`
- Features:
  - Product display
  - Category filtering
  - Order placement
  - Order history

- ChatGPT have been used as a copilot to learn .vue file structure.

---

## 📦 Prerequisites

### Backend

- Python **3.12+**
- Pre-installed `pip`

### Frontend

- Frontend is built with Vue 3 and Vite (created using `npm create vue@latest`)
- Node.js **20.19.0+** or **>=22.12.0** (⚠️ required by Vite 7)
- npm **10.8+**

---

## 🚀 Running the Project

### Backend (FastAPI)

1. Navigate to the backend folder:
   ```bash
   cd src/backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Contents of `requirements.txt`**:
   ```txt
   fastapi
   uvicorn
   pytest
   httpx
   ```

4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

   The backend will be available at [http://localhost:8000](http://localhost:8000)
   With the Swagger Docs and Simple use at [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Frontend (Vue 3 + Vite)

1. Navigate to the frontend folder:
   ```bash
   cd src/frontend/frontend-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at [http://localhost:5173](http://localhost:5173)

---

## API - Endpoints

| GET    | `/products`  | Lists products with optional category filter (`?category=electronics`)     |
| POST   | `/order`     | Creates an order: validates product existence and customer name            |
| GET    | `/orders`    | Lists all saved orders (persisted in a JSON file)                          |

- GET products available at [http://localhost:5173/products](http://localhost:5173/products)
- POST order available at [http://localhost:5173/order](http://localhost:5173/order)
- GET orders available at [http://localhost:5173/orders](http://localhost:5173/orders)
### Example Payload for POST `/order`

```json
{
  "customer_name": "John Doe",
  "product_ids": [1, 3]
}
```

---

## Run tests

- Navigate to src/backend :
   ```bash
   PYTHONPATH=. pytest tests/
   ```

---

## Implemented Bonus

- ✅ Order persistence in `orders.json`
- ✅ Add few Unit Tests with Pytest
- ✅ Error handling on the backend (invalid IDs, empty name, etc.)
- ✅ View routing with Vue Router (`/products`, `/orders`)
- ✅ Formatted price display (e.g., `$1,499.98`)

---

## 📁 Project Structure

```text
FullStack_Asmodee/
├── src/
│   ├── backend/       # FastAPI backend
│   └── frontend/      # Vue frontend
│       └── frontend-app/
```


## Author

Lucas ZIVAN (Asmodee Internship 2025)  
EPITA Engineering Student

📧 lucas.zivan@epita.fr | 📞 +33 7 83 66 55 75  
📍 Paris / Poitiers  
🔗 [linkedin.com/in/zivan-lucas-a057542a4](https://linkedin.com/in/zivan-lucas-a057542a4)
