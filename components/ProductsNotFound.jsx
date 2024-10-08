import { FaShoppingCart } from 'react-icons/fa'

export function ProductsNotFound({ product, mode }) {
	return (
		<div>
			<div className='mx-auto flex w-full flex-col items-center rounded-3xl border-4 bg-white px-6 py-8 text-center'>
				<div className='mb-6 text-5xl text-blue-600'>
					<FaShoppingCart />
				</div>
				<p className='mb-2 text-xl font-medium text-gray-600'>
					{mode === 'Search' ? (
						<>
							Producto <span className='font-bold'>{product}</span> No
							Encontrado
						</>
					) : (
						<span>Carrito Vacío</span>
					)}
				</p>
				<p className='text-gray-500'>
					{mode === 'Search' ? (
						<>No se han encontrado productos con ese nombre.</>
					) : (
						<>Agrega productos al carrito.</>
					)}
				</p>
			</div>
		</div>
	)
}
