import axios from 'axios';
import { useEffect, useState } from 'react';

const useFetch = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [hasError, setHasError] = useState(null);

  const apiUrl = "http://127.0.0.1:5000";
  

  const makeRequest = async (method, url, data = null) => {
    setIsLoading(true);
    setHasError(null);

    try {
      const response = await axios({
        method: method,
        url: `${apiUrl}${url}`,
        data: data,
      });

      setIsLoading(false);
      return response.data;
    } catch (error) {
      setHasError(error);
      setIsLoading(false);
      throw error;
    }
  };

  const get = async (url) => {
    return await makeRequest('GET', url);
  };

  const post = async (url, data) => {
    return await makeRequest('POST', url, data);
  };

  const put = async (url, data) => {
    return await makeRequest('PUT', url, data);
  };

  const del = async (url) => {
    return await makeRequest('DELETE', url);
  };

  useEffect(() => {
    console.log(apiUrl)
  }, [])
  
  return { get, post, put, delete: del, isLoading, hasError };

};

export default useFetch;
