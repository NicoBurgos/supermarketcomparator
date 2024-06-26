'use client'
import { useSearchParams, usePathname, useRouter } from 'next/navigation'
import { useDebouncedCallback } from 'use-debounce'

export function Search() {
	const searchParams = useSearchParams()
	const pathname = usePathname()
	const { replace } = useRouter()

	const handleSearch = useDebouncedCallback((product) => {
		const params = new URLSearchParams(searchParams)
		params.set('page', '1')
		if (product) {
			params.set('producto', product)
		} else {
			params.delete('producto')
		}
		replace(`${pathname}?${params.toString()}`)
	}, 300)
	return (
		<input
			placeholder='Inserte el producto a buscar'
			onChange={(e) =>
				handleSearch(e.target.value.replace(/[^a-zA-Z0-9\s]/g, ''))
			}
			defaultValue={searchParams.get('producto')?.toString() || ''}
			type='text'
			name='search'
			className='w-72 mb-8 text-black py-2 text-center'
		/>
	)
}
