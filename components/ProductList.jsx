import { Database } from '@/data/data.js'
import { Card } from '@/components/Card'
import { ProductsNotFound } from './ProductsNotFound'
export async function ProductList({ queryProduct, currentPage, queryOrder }) {
	const data = await Database.getProductsByName(
		queryProduct,
		currentPage,
		queryOrder
	)

	return (
		<div className='flex flex-col gap-5 justify-center text-center items-center w-72'>
			{data.length < 1 ? (
				<ProductsNotFound product={queryProduct} mode={'Search'} />
			) : (
				data.map((producto, index) => (
					<Card key={index} product={producto}></Card>
				))
			)}
		</div>
	)
}
