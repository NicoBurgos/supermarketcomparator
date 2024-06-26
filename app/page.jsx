import { ProductList } from '@/components/ProductList'
import { Pagination } from '@/components/Pagination'
import { Search } from '@/components/Search'
import { Selector } from '@/components/Selector'
import { Database } from '@/data/data'
import { Suspense } from 'react'
import { Loader } from '@/components/Loader'

export default async function Home({ searchParams }) {
	const queryProduct = searchParams?.producto || ''
	const queryOrder = searchParams?.order || 'none'
	const currentPage = Number(searchParams?.page) || 1
	const totalPages = await Database.getTotalPages(queryProduct)

	return (
		<main className='flex flex-col items-center justify-between py-4'>
			<Search />
			{/*	AÑADIR UN SKELETON DE CARD*/}
			<Selector />
			{totalPages > 0 ? <Pagination totalPages={totalPages} /> : null}
			<Suspense key={queryProduct + currentPage} fallback={<Loader />}>
				<ProductList
					queryProduct={queryProduct}
					currentPage={currentPage}
					queryOrder={queryOrder}
				/>
			</Suspense>
			{totalPages > 0 ? <Pagination totalPages={totalPages} /> : null}
		</main>
	)
}
