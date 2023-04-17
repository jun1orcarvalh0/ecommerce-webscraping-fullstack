import React, { useContext } from 'react';
import { useForm } from 'react-hook-form';

import { zodResolver } from '@hookform/resolvers/zod';
import { recoverBuscapeSearch, recoverMercadoLivreSearch } from 'api/fetchData';
import { Context } from 'context/Context';
import { z } from 'zod';

const schema = z.object({
  website: z.string().min(2, 'You must choose a website'),
  category: z.string().min(2, 'You must choose a category'),
  search: z.string().min(1, 'You must input a text')
});

type FormProps = z.infer<typeof schema>;

const SearchForm = () => {
  const { setScrapingData, setIsLoading } = useContext(Context);
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<FormProps>({
    mode: 'all',
    reValidateMode: 'onChange',
    resolver: zodResolver(schema)
  });

  const handleForm = async (data: FormProps) => {
    if (data.website === 'MercadoLivre') {
      setIsLoading(true);
      const result = await recoverMercadoLivreSearch(
        data.category,
        data.search
      );
      setScrapingData(result);
      setIsLoading(false);
    }
    if (data.website === 'Buscape') {
      setIsLoading(true);
      const result = await recoverBuscapeSearch(data.category, data.search);
      setScrapingData(result);
      setIsLoading(false);
    }
  };

  return (
    <div>
      <form
        onSubmit={handleSubmit(handleForm)}
        className="flex w-full justify-center"
      >
        <div className="flex flex-col p-8">
          <label className="text-xl font-medium">Select a website:</label>
          <select
            className='className="w-full border-2 border-gray-100 rounded-lg p-4 mt-1 mb-4 bg-transparent"'
            {...register('website')}
          >
            <option value="">Choose an option</option>
            <option value="MercadoLivre">MercadoLivre</option>
            <option value="Buscape">Buscape</option>
          </select>
          {errors.website?.message && (
            <p className="text-red-600">{errors.website.message}</p>
          )}
        </div>
        <div className="flex flex-col p-8">
          <label className="text-xl font-medium">Select a category:</label>
          <select
            className='className="w-full border-2 border-gray-100 rounded-lg p-4 mt-1 mb-4 bg-transparent"'
            {...register('category')}
          >
            <option value="">Select a category</option>
            <option value="geladeira">Geladeira</option>
            <option value="tv">TV</option>
            <option value="celular">Celular</option>
          </select>
          {errors.category?.message && (
            <p className="text-red-600">{errors.category.message}</p>
          )}
        </div>
        <div className="flex flex-col w-3/12 mt-7 p-8">
          <input
            className='className="w-full border-2 border-gray-100 rounded-lg p-4 mt-1 mb-4 bg-transparent"'
            {...register('search')}
            placeholder="Want to be more specific?"
          />
          {errors.search?.message && (
            <p className="text-red-600">{errors.search.message}</p>
          )}
        </div>
        <div className="flex flex-col justify-center w-1/12">
          <button
            type="submit"
            className={
              'py-3 rounded-lg bg-blue-600 text-white text-lg font-semibold hover:bg-blue-700'
            }
          >
            Search
          </button>
        </div>
      </form>
    </div>
  );
};

export default SearchForm;
