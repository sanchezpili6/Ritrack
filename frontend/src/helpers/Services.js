import {Apis} from "@/helpers/APIs";

const get_user = async (email) => {
    const response = await Apis.get(`/get_user/${email}`);
    return response.data;
}
const add_user = async (user_data) => {
    const response = await Apis.post('/add_user', user_data);
    return response.data;
}
const login = async (data) => {
    const response = await Apis.post(`/login`, data);
    return response.data;
}
const logout = async (data) => {
    const response = await Apis.post(`/logout`, data);
    return response.data;
}
const get_pet = async (id) => {
    const response = await Apis.get(`/get_pet/${id}`);
    return response.data;
}
const add_pet = async (data) => {
    const response = await Apis.post(`/add_pet`, data);
    return response.data;
}
const edit_pet = async (data) => {
    const response = await Apis.put(`/edit_pet`, data);
    return response.data;
}

export {
    get_user,
    add_user,
    login,
    logout,
    get_pet,
    add_pet,
    edit_pet
}
