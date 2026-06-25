import axios from "axios";

const api = axios.create({
  baseURL: "https://plagiscan-ai.onrender.com/api",
});

export default api;