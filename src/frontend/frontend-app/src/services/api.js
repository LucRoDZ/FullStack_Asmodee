import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000',
});

export const getProducts = (category = '') =>
  API.get(`/products${category ? '?category=' + category : ''}`);

export const createOrder = (order) => API.post('/order', order);

export const getOrders = () => API.get('/orders');
