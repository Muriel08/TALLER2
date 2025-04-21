// src/api.jsx
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000', // Asegurate que sea la URL de tu backend Flask
});

export default API;
