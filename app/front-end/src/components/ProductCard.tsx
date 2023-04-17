import Link from 'next/link';
import React from 'react';

export type ProductType = {
  category: string;
  picture: string;
  title: string;
  price: string;
  link: string;
};

const ProductCard = ({
  category,
  picture,
  title,
  price,
  link
}: ProductType) => {
  return (
    <div className="card w-3/12 h-fit rounded-xl border-2 border-slate-700:1 p-6 mb-4">
      <div className="flex h-48 max-h-full justify-center img-area">
        <img src={picture} alt={title} className="object-contain rounded-lg" />
      </div>
      <div className="flex flex-col h-44 text-area mt-6 text-center justify-around">
        <span className="text-lg text-gray-600 mt-3">{title}</span>
        <span className="text-lg text-gray-600 mt-3">
          Category: {category.toUpperCase()}
        </span>
        <span className="text-lg text-gray-600 font-semibold mt-6">
          R$ {price}
        </span>
      </div>
      <div className="flex justify-center text-center mt-6">
        <Link
          href={link}
          className="w-3/5 py-3 rounded-lg bg-blue-600 text-white text-lg font-semibold hover:bg-blue-700"
        >
          Link
        </Link>
      </div>
    </div>
  );
};

export default ProductCard;
