import { useCartStore } from '@/store/cart-store'
import { CartProduct } from './CartProduct'
import { ProductsNotFound } from './ProductsNotFound'
import { Brand } from './Brand'
import { useState } from 'react'
/* import {
	calculateBestRoute,
	getNearbySupermarkets,
} from '@/lib/calculateRoutes' */

export function Cart() {
	const [location, setLocation] = useState(null)
	const { cart, clearCart, calculateSubtotals, calculateTotal } = useCartStore()
	const subtotals = calculateSubtotals()
	const total = calculateTotal()
	const handleClearCart = () => {
		clearCart()
	}
	const handleBestRoute = () => {
		/* if (location) {
			const cadenas = [...new Set(cart.map((item) => item.cadena))]
			
			const supers = getNearbySupermarkets(
				[location.latitude, location.longitude],
				cadenas
			)
			console.log([location.latitude, location.longitude])
			console.log(supers)
		} else {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(
					(position) => {
						setLocation({
							latitude: position.coords.latitude,
							longitude: position.coords.longitude,
						})
					},
					(error) => {
						console.error('Error getting user location:', error)
					}
				)
			} else {
				console.error('Geolocation is not supported by this browser.')
			}
		} */
	}

	return (
		<section className='h-full bg-gray-100 py-6 sm:py-16 lg:py-20 '>
			<div className='h-full overflow-scroll mx-auto px-4 sm:px-6 lg:px-8'>
				<div className='flex items-center justify-center'>
					<h1 className='text-2xl font-semibold text-gray-900'>Tu Carrito</h1>
				</div>

				<div className='mx-auto mt-8 max-w-2xl md:mt-12'>
					<div className='bg-white shadow'>
						<div className='px-4 py-6 sm:px-8 sm:py-10'>
							<div className='flow-root'>
								{cart.length === 0 ? (
									<ProductsNotFound mode={'Cart'} />
								) : (
									<ul className='-my-8'>
										{cart.map((item, index) => (
											<CartProduct key={index} product={item} />
										))}
									</ul>
								)}
							</div>
							{cart.length === 0 ? null : (
								<div className='mt-6 border-t border-b py-2 text-black'>
									{Object.entries(subtotals).map(([cadena, subtotal]) => (
										<div
											key={cadena}
											className='flex items-center justify-between my-3'
										>
											<p className='text-lg text-black'>
												Subtotal <Brand brand={cadena} />
											</p>
											<p className='text-lg font-semibold text-gray-900'>
												$ {subtotal.toFixed(2)}
											</p>
										</div>
									))}
								</div>
							)}

							{cart.length === 0 ? null : (
								<div className='mt-6 flex items-center justify-between'>
									<p className='text-2xl font-semibold text-gray-900'>Total</p>
									<p className='text-2xl font-semibold text-gray-900'>
										$ {total.toFixed(2)}
									</p>
								</div>
							)}

							<div className='mt-6 text-center flex flex-col gap-2'>
								{cart.length > 0 && (
									<button
										onClick={() => handleBestRoute()}
										type='button'
										className='group inline-flex w-full items-center justify-center rounded-md bg-gray-900 px-6 py-4 text-lg font-semibold text-white transition-all duration-200 ease-in-out focus:shadow hover:bg-gray-800'
									>
										Calcular Ruta Óptima
									</button>
								)}
								<button
									onClick={() => handleClearCart()}
									type='button'
									className='group inline-flex w-full items-center justify-center rounded-md bg-gray-900 px-6 py-4 text-lg font-semibold text-white transition-all duration-200 ease-in-out focus:shadow hover:bg-gray-800'
								>
									Vaciar Carrito
									<svg
										xmlns='http://www.w3.org/2000/svg'
										className='group-hover:ml-8 ml-4 h-6 w-6 transition-all'
										fill='none'
										viewBox='0 0 24 24'
										stroke='currentColor'
										strokeWidth='2'
									>
										<path
											strokeLinecap='round'
											strokeLinejoin='round'
											d='M13 7l5 5m0 0l-5 5m5-5H6'
										/>
									</svg>
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	)
}
