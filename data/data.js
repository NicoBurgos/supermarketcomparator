import { sortProducts } from '@/lib/utils'
import productosCarrefour from './productosCarrefour.json'
import productosComodin from './productosComodin.json'
import productosVea from './productosVea.json'
import productosYaguar from './productosYaguar.json'
import productosDia from './productosDia.json'
import productosChangoMas from './productosChangoMas.json'

const allProducts = productosCarrefour.concat(
	productosComodin,
	productosVea,
	productosYaguar,
	productosDia,
	productosChangoMas
)
const PRODUCTS_PER_PAGE = 20

const getSupermarkets = () => {
	return ['Carrefour', 'ChangoMas', 'Comodin', 'Dia', 'Vea', 'Yaguar']
}

const getProductsBySupermarket = async (supermarket) => {
	switch (supermarket) {
		case 'Carrefour':
			return await productosCarrefour

		case 'ChangoMas':
			return await productosChangoMas

		case 'Comodin':
			return await productosComodin

		case 'Dia':
			return await productosDia

		case 'Vea':
			return await productosVea

		case 'Yaguar':
			return await productosYaguar
		default:
			return null
	}
}

const getAllProducts = async () => {
	return await allProducts
}

const getProductsByName = async (name, currentPage, mode) => {
	const orderedProducts = sortProducts(allProducts, mode)
	const offset = PRODUCTS_PER_PAGE * (currentPage - 1)
	const searchTerms = name.toLowerCase().split(' ')
	const products = await orderedProducts.filter((product) => {
		const productName = product.nombre.toLowerCase()

		return searchTerms.every((term) => productName.includes(term))
	})
	const productsLimited = products.slice(offset, offset + PRODUCTS_PER_PAGE)

	return productsLimited
}

const getTotalPages = async (name) => {
	const products = await allProducts.filter((product) =>
		product.nombre.toLowerCase().includes(name.toLowerCase())
	)
	const totalPages = Math.ceil(products.length / PRODUCTS_PER_PAGE)
	return totalPages
}

export const Database = {
	getProductsBySupermarket,
	getSupermarkets,
	getAllProducts,
	getProductsByName,
	getTotalPages,
}
