'use client'
import { useState } from 'react'
import { Cart } from './Cart'
import { useCartStore } from '@/store/cart-store'

export function CartButton() {
	const [isCartOpen, setIsCartOpen] = useState(false)
	const cartCount = useCartStore((state) => state.cartCount())
	const handleToggleCart = () => {
		setIsCartOpen(!isCartOpen)
	}
	return (
		<aside
			className={`fixed bottom-0 left-0 right-0 w-full text-center bg-gray-700 transition-transform duration-300 ${
				isCartOpen ? 'h-screen' : 'h-12'
			}`}
		>
			<button
				onClick={handleToggleCart}
				className={`w-full h-full ${isCartOpen ? 'hidden' : 'block'}`}
			>
				{`Carrito (${cartCount} Productos)`}
			</button>
			{isCartOpen && (
				<div className='relative w-full h-full bg-white'>
					<button
						onClick={handleToggleCart}
						className='absolute px-2 top-2 right-2 text-black'
					>
						X
					</button>
					<div className='h-screen'>
						<Cart></Cart>
					</div>
				</div>
			)}
		</aside>
	)
}
