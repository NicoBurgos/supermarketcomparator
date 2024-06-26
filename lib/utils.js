export const generatePagination = (currentPage, totalPages) => {
	const array = []
	let startPage, endPage

	if (totalPages <= 5) {
		startPage = 1
		endPage = totalPages
	} else if (currentPage <= 3) {
		startPage = 1
		endPage = 5
	} else if (currentPage + 2 >= totalPages) {
		startPage = totalPages - 4
		endPage = totalPages
	} else {
		startPage = currentPage - 2
		endPage = currentPage + 2
	}

	for (let i = startPage; i <= endPage; i++) {
		array.push(i)
	}

	return array
}

export const sortProducts = (products, mode) => {
	switch (mode) {
		case 'precioAsc':
			return [...products].sort((a, b) => a.precio - b.precio)
		case 'precioDesc':
			return [...products].sort((a, b) => b.precio - a.precio)
		case 'nombreAsc':
			return [...products].sort((a, b) => a.nombre.localeCompare(b.nombre))
		case 'nombreDesc':
			return [...products].sort((a, b) => b.nombre.localeCompare(a.nombre))
		default:
			return [...products]
	}
}
