# Fullstack Developer Internship Assignment  

## Time Limit  
This is a **take-home assessment**. Focus on **functionality, code quality, and clarity** rather than advanced styling or over-engineering.  

---

## Tech Stack  
- **Backend:** Python (**FastAPI**) running on `http://localhost:8000`  
- **Frontend:** Vue.js with **Axios** running locally (e.g., `http://localhost:5173`)  

---

## Task Description  
You will build a small **product ordering application** with the following requirements:

---

### Backend (FastAPI)  
1. Create a **GET endpoint** `/products` that:  
   - Returns a list of products with fields: `id`, `name`, `price`, and `category`.  
   - Supports **query parameters** to filter by category (e.g., `/products?category=electronics`).  

2. Create a **POST endpoint** `/order` that:  
   - Accepts a JSON payload with:  
     ```json
     {
       "customer_name": "John Doe",
       "product_ids": [1, 3]
     }
     ```  
   - Validates that:  
     - All product IDs exist.  
     - `customer_name` is not empty.  
   - Returns an **order summary** containing:  
     - The ordered items (with full details).  
     - The total price.  
     - A generated **order ID** (e.g., a UUID).  

3. Add a **GET endpoint** `/orders` to fetch all previous orders made (in-memory is fine).  

---

### Frontend (Vue.js + Axios)  
1. Fetch and display the product list from `/products`.  
   - Include a **dropdown filter** to filter products by category using the query parameter.  

2. Build a form to:  
   - Enter a **customer name**.  
   - Select multiple products (checkboxes or multi-select).  

3. On submit:  
   - Send the form data (name + selected product IDs) to `/order`.  
   - Display the **order confirmation** (order ID, ordered items, and total price).  

4. Add a page or section that lists **all previous orders** using the `/orders` endpoint.  

---

## What We Expect to See  
- A running **FastAPI backend** (`http://localhost:8000`) with proper validation and clean routes.  
- A **Vue.js frontend** (`http://localhost:5173`) with clear Axios-based data fetching and updates.  
- Separation of concerns (components, services, etc.) in frontend code.  
- Clean, readable, and maintainable code.  
- Graceful handling of errors (e.g., invalid product IDs, empty name).  

---

## Bonus Points (Optional)  
- Persist data in a simple JSON file instead of memory (to simulate persistence).  
- Add unit tests for the backend endpoints.  
- Use Vue Router to separate product listing and order history views.  
- Format prices nicely (e.g., `$1,200.00`).  

---

## Deliverables  
- A GitHub repository (or zipped folder) containing both backend and frontend code.  
- A README with clear instructions to run both servers locally.  

---

**Good luck! We're looking for how you structure your solution, handle complexity, and write clean, functional code.**
