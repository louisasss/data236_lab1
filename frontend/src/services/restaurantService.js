import api from './api'

export const getRestaurants = (params) => api.get('/restaurants', { params })
export const getRestaurant = (id) => api.get(`/restaurants/${id}`)
export const createRestaurant = (data) => api.post('/restaurants', data)
export const updateRestaurant = (id, data) => api.put(`/restaurants/${id}`, data)
