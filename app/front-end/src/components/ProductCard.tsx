import Link from 'next/link';
import React from 'react';

type ProductCardsProps = {
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
}: ProductCardsProps) => {
  return (
    <div className="card w-2/12 h-fit rounded-xl border-2 border-slate-700:1 py-6">
      <div className="flex justify-center img-area">
        <img src={picture} alt={title} className="object-contain rounded-lg" />
      </div>
      <div className="flex flex-col text-area mt-6 text-center">
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
