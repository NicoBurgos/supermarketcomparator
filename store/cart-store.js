import { create } from 'zustand'

export const useCartStore = create((set, get) => ({
	cart: [],

	addProduct: (product) =>
		set((state) => {
			const existingProduct = state.cart.find(
				(item) => item.nombre === product.nombre
			)
			if (existingProduct) {
				return {
					cart: state.cart.filter((item) => item.nombre !== product.nombre),
				}
			} else {
				return {
					cart: [...state.cart, { ...product, cantidad: 1 }],
				}
			}
		}),

	removeProduct: (productName) =>
		set((state) => ({
			cart: state.cart.filter((item) => item.nombre !== productName),
		})),

	updateProductQuantity: (productName, newQuantity) =>
		set((state) => ({
			cart: state.cart.map((item) =>
				item.nombre === productName
					? { ...item, cantidad: Math.max(newQuantity, 1) }
					: item
			),
		})),

	clearCart: () => set({ cart: [] }),

	calculateSubtotals: () => {
		return get().cart.reduce((acc, item) => {
			const subtotal = item.precio * item.cantidad
			if (acc[item.cadena]) {
				acc[item.cadena] += subtotal
			} else {
				acc[item.cadena] = subtotal
			}
			return acc
		}, {})
	},

	calculateTotal: () => {
		const cart = get().cart
		return cart.reduce((total, item) => total + item.precio * item.cantidad, 0)
	},

	cartCount: () => get().cart.length,
}))
