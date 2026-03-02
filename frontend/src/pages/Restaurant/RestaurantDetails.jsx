// TODO: Implement Restaurant Details page
// - Display: name, cuisine, address, hours, contact, photos, avg rating, review count
// - Reviews list (rating, comment, date, author)
// - Add/edit/delete review form (logged-in users)
// - Favorite toggle button

import { useParams } from 'react-router-dom'

export default function RestaurantDetails() {
  const { id } = useParams()

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Restaurant Details</h1>
      <p className="text-gray-500">Details for restaurant ID: {id}</p>
    </div>
  )
}
