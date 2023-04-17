import { ScriptProps } from 'next/script';
import { createContext, useState } from 'react';

type ContextType = {
  scrapingData: ScrapingData;
  setScrapingData: (data: ScrapingData) => void;
};

export type ScrapingData = {
  category: string;
  search: string;
  products: [];
};

export const Context = createContext({} as ContextType);

export function Provider({ children }: ScriptProps) {
  const [scrapingData, setScrapingData] = useState({} as ScrapingData);

  return (
    <Context.Provider value={{ setScrapingData, scrapingData }}>
      {children}
    </Context.Provider>
  );
}
