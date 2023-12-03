import { useState, useEffect } from "react";

function useCustomSearch(term) {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      fetch(
        `http://172.16.7.138:5000/result?q=${term}`
      )
        .then((response) => response.JSON.stringify.json())
        .then((result) => {
          setData(result);
        });
    };
    fetchData();
  }, [term]);

  return { data };
}

export default useCustomSearch;

