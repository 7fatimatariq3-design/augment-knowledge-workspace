import axios from "axios";

const api = axios.create({
  baseURL: "/api",
});

// Milestone 2: attach auth token via interceptor once login is implemented
// api.interceptors.request.use((config) => {
//   const token = localStorage.getItem("token");
//   if (token) config.headers.Authorization = `Bearer ${token}`;
//   return config;
// });

export default api;
