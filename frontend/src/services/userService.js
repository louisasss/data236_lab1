import api from './api'

export const getProfile = () => api.get('/users/me')
export const updateProfile = (data) => api.put('/users/me', data)
export const uploadProfilePicture = (formData) =>
  api.post('/users/me/photo', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
export const getPreferences = () => api.get('/users/me/preferences')
export const updatePreferences = (data) => api.put('/users/me/preferences', data)
export const getFavorites = () => api.get('/users/me/favorites')
export const addFavorite = (restaurantId) => api.post(`/users/me/favorites/${restaurantId}`)
export const removeFavorite = (restaurantId) => api.delete(`/users/me/favorites/${restaurantId}`)
export const getHistory = () => api.get('/users/me/history')
