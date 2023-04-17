import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const api = axios.create({
  baseURL: process.env.API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

const recoverBuscapeSearch = async (category: string, search: string) => {
  try {
    const URL = `${API_URL}/products-from-buscape/${category}/${search}`;
    const result = await api.get(URL);
    return result.data;
  } catch (error: any) {
    return error.toJSON();
  }
};

const recoverMercadoLivreSearch = async (category: string, search: string) => {
  try {
    console.log(API_URL);
    const URL = `${API_URL}/products-from-ml/${category}/${search}`;
    const result = await api.get(URL);
    return result.data;
  } catch (error: any) {
    return error.toJSON();
  }
};

export { recoverMercadoLivreSearch, recoverBuscapeSearch };
