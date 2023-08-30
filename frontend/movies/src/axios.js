// axios.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8081', 
});

instance.interceptors.request.use(config => {
  return config;
}, error => {
  return Promise.reject(error);
});

export default instance;