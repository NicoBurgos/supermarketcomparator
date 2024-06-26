import clsx from 'clsx'

export function Brand({ brand }) {
	return (
		<span
			className={clsx(
				'rounded-full px-2 text-center text-lg font-semibold text-white py-1',
				{
					'bg-yellow-500': brand === 'Comodin',
					'bg-orange-500': brand === 'ChangoMas',
					'bg-green-500': brand === 'Vea',
					'bg-blue-500': brand === 'Carrefour',
					'bg-red-500': brand === 'Dia',
					'bg-black text-yellow-400': brand === 'Yaguar',
					'bg-black': ![
						'Comodin',
						'ChangoMas',
						'Vea',
						'Carrefour',
						'Yaguar',
						'Dia',
					].includes(brand),
				}
			)}
		>
			{brand}
		</span>
	)
}
