import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

const recoverBuscapeSearch = async (category: string, search: string) => {
  try {
    const URL = `${BASE_URL}/products-from-buscape/${category}/${search}`;
    console.log(URL);
    const result = await api.get(URL);
    console.log(result);
    return result;
  } catch (error: any) {
    return error.toJSON();
  }
};

const recoverMercadoLivreSearch = async (category: string, search: string) => {
  try {
    const URL = `${BASE_URL}/products-from-ml/${category}/${search}`;
    console.log(URL);
    const result = await api.get(URL);
    console.log(result);
    return result;
  } catch (error: any) {
    return error.toJSON();
  }
};

export { recoverMercadoLivreSearch, recoverBuscapeSearch };
