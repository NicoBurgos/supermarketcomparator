'use client'

import { useSearchParams, usePathname, useRouter } from 'next/navigation'

export function Selector() {
	const searchParams = useSearchParams()
	const pathname = usePathname()
	const { replace } = useRouter()

	const handleSortChange = (value) => {
		const params = new URLSearchParams(searchParams)
		switch (value) {
			case 'precioAsc':
				params.set('order', 'precioAsc')
				break
			case 'precioDesc':
				params.set('order', 'precioDesc')
				break
			case 'nombreAsc':
				params.set('order', 'nombreAsc')
				break
			case 'nombreDesc':
				params.set('order', 'nombreDesc')
				break
			default:
		}

		replace(`${pathname}?${params.toString()}`)
	}

	//añadir al queryparams de laruta ?order=price
	return (
		<select
			name='ordenar'
			className='bg-gray-700 py-2 w-72 text-center mb-5'
			onChange={(e) => handleSortChange(e.target.value)}
			defaultValue={searchParams.get('order')?.toString() || 'none'}
		>
			<option value='none' disabled hidden>
				Ordenar Productos
			</option>
			<option value='precioAsc'>Menor Precio</option>
			<option value='precioDesc'>Mayor Precio</option>
			<option value='nombreAsc'>Alfabeticamente (Asc)</option>
			<option value='nombreDesc'>Alfabeticamente (Desc)</option>
		</select>
	)
}
