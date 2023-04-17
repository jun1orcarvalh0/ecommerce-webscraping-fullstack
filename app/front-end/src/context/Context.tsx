import { ScriptProps } from 'next/script';
import { createContext, useState } from 'react';

type ContextType = {
  scrapingData: ScrapingData;
  setScrapingData: (data: ScrapingData) => void;
  isLoading: boolean;
  setIsLoading: (bool: boolean) => void;
};

export type ScrapingData = {
  category: string;
  search: string;
  products: [];
};

export const Context = createContext({} as ContextType);

export function Provider({ children }: ScriptProps) {
  const [scrapingData, setScrapingData] = useState({} as ScrapingData);
  const [isLoading, setIsLoading] = useState(false);

  return (
    <Context.Provider
      value={{ setScrapingData, scrapingData, isLoading, setIsLoading }}
    >
      {children}
    </Context.Provider>
  );
}
