'use client'
import Link from 'next/link'
import clsx from 'clsx'
import { usePathname, useSearchParams } from 'next/navigation'
import { generatePagination } from '@/lib/utils'

export function Pagination({ totalPages }) {
	const darkMode = false
	const searchParams = useSearchParams()
	const pathname = usePathname()
	const currentPage = Number(searchParams?.get('page')) || 1
	const pages = generatePagination(currentPage, totalPages)

	const createPageURL = (page) => {
		const params = new URLSearchParams(searchParams)
		params.set('page', page.toString())
		return `${pathname}?${params.toString()}`
	}

	return (
		<nav
			aria-label='Page Navigation'
			className={clsx(
				'mx-auto my-10 flex max-w-md justify-between space-x-2 rounded-md py-2 text-gray-700',
				darkMode ? 'bg-gray-800 text-white' : 'bg-white text-gray-700'
			)}
		>
			{currentPage > 1 ? (
				<Link
					href={createPageURL(currentPage - 1)}
					aria-label='Previous Page'
					className={clsx(
						'flex items-center space-x-1 font-medium',
						darkMode ? 'hover:text-gray-300' : 'hover:text-blue-600'
					)}
				>
					<svg
						xmlns='http://www.w3.org/2000/svg'
						viewBox='0 0 24 24'
						fill='currentColor'
						className='h-4 w-4'
					>
						<path
							fillRule='evenodd'
							d='M7.72 12.53a.75.75 0 010-1.06l7.5-7.5a.75.75 0 111.06 1.06L9.31 12l6.97 6.97a.75.75 0 11-1.06 1.06l-7.5-7.5z'
							clipRule='evenodd'
						/>
					</svg>
				</Link>
			) : (
				<span
					className='flex items-center space-x-1 font-medium text-gray-400'
					aria-label='Previous Page'
					tabIndex='-1'
				>
					<svg
						xmlns='http://www.w3.org/2000/svg'
						viewBox='0 0 24 24'
						fill='currentColor'
						className='h-4 w-4'
					>
						<path
							fillRule='evenodd'
							d='M7.72 12.53a.75.75 0 010-1.06l7.5-7.5a.75.75 0 111.06 1.06L9.31 12l6.97 6.97a.75.75 0 11-1.06 1.06l-7.5-7.5z'
							clipRule='evenodd'
						/>
					</svg>
				</span>
			)}

			<ul className='flex'>
				{pages.map((page) => (
					<li key={page}>
						{page === '...' ? (
							<>
								<span className='text-gray-400' aria-hidden='true'>
									...
								</span>
								<span className='sr-only'>Skipping Pages</span>
							</>
						) : (
							<Link
								href={createPageURL(page)}
								className={clsx('px-2 text-lg font-medium sm:px-3', {
									'rounded-md bg-blue-600 text-white': page === currentPage,
									'hover:text-blue-600': !darkMode && page !== currentPage,
									'hover:text-gray-300': darkMode && page !== currentPage,
								})}
							>
								{page}
							</Link>
						)}
					</li>
				))}
			</ul>

			{currentPage < totalPages ? (
				<Link
					href={createPageURL(currentPage + 1)}
					aria-label='Next Page'
					className={clsx(
						'flex items-center space-x-1 font-medium',
						darkMode ? 'hover:text-gray-300' : 'hover:text-blue-600'
					)}
				>
					<svg
						xmlns='http://www.w3.org/2000/svg'
						viewBox='0 0 24 24'
						fill='currentColor'
						className='h-4 w-4'
					>
						<path
							fillRule='evenodd'
							d='M16.28 11.47a.75.75 0 010 1.06l-7.5 7.5a.75.75 0 01-1.06-1.06L14.69 12 7.72 5.03a.75.75 0 011.06-1.06l7.5 7.5z'
							clipRule='evenodd'
						/>
					</svg>
				</Link>
			) : (
				<span
					className='flex items-center space-x-1 font-medium text-gray-400'
					aria-label='Next Page'
					tabIndex='-1'
				>
					<svg
						xmlns='http://www.w3.org/2000/svg'
						viewBox='0 0 24 24'
						fill='currentColor'
						className='h-4 w-4'
					>
						<path
							fillRule='evenodd'
							d='M16.28 11.47a.75.75 0 010 1.06l-7.5 7.5a.75.75 0 01-1.06-1.06L14.69 12 7.72 5.03a.75.75 0 011.06-1.06l7.5 7.5z'
							clipRule='evenodd'
						/>
					</svg>
				</span>
			)}
		</nav>
	)
}
