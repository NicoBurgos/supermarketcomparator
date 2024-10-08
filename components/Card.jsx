'use client'
import { useCartStore } from '@/store/cart-store'
import clsx from 'clsx'
import { Brand } from './Brand'

export function Card({ product }) {
	const darkMode = false
	const { addProduct, cart } = useCartStore()
	const productInCart = cart.find((item) => item.nombre === product.nombre)
	const handleClickAddCart = () => {
		addProduct(product)
	}
	return (
		<div
			className={clsx(
				'relative m-4 flex w-full max-w-xs flex-col overflow-hidden rounded-lg border shadow-md md:w-56 md:h-96',
				darkMode ? 'border-gray-700 bg-gray-800' : 'border-gray-100 bg-white'
			)}
		>
			<a
				className='relative mx-3 mt-3 flex h-60 overflow-hidden rounded-xl'
				href={product.enlace}
				target='_blank'
				rel='noopener noreferrer'
			>
				<img
					className='object-cover m-auto'
					src={`${product.imagen}`}
					alt='product image'
				/>
				<span className='absolute top-0 left-0 m-2'>
					<Brand brand={product.cadena} />
				</span>
				<div
					className={clsx(
						'absolute inset-0 flex items-center justify-center bg-black bg-opacity-50 text-white text-lg font-medium opacity-0 hover:opacity-100'
					)}
				>
					Ir al sitio web
				</div>
			</a>
			<div className='mt-4 px-5 pb-5'>
				<h5
					className={clsx(
						'text-xl tracking-tight',
						darkMode ? 'text-white' : 'text-slate-900'
					)}
				>
					{product.nombre}
				</h5>
				<div className='mt-2 mb-5 flex items-center justify-center'>
					<p>
						<span
							className={clsx(
								'text-3xl font-bold',
								darkMode ? 'text-white' : 'text-slate-900'
							)}
						>
							${product.precio}
						</span>
					</p>
				</div>
				<button
					onClick={handleClickAddCart}
					className={clsx(
						'flex items-center justify-center rounded-md px-5 py-2.5 text-center text-sm font-medium text-white focus:outline-none focus:ring-4 w-full',
						productInCart ? 'bg-red-800' : 'bg-green-800'
					)}
				>
					<svg
						xmlns='http://www.w3.org/2000/svg'
						className='mr-2 h-6 w-6'
						fill='none'
						viewBox='0 0 24 24'
						stroke='currentColor'
						strokeWidth='2'
					>
						<path
							strokeLinecap='round'
							strokeLinejoin='round'
							d='M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z'
						/>
					</svg>
					{productInCart ? 'Eliminar del Carrito' : 'Añadir al Carrito'}
				</button>
			</div>
		</div>
	)
}
