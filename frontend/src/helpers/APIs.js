import axios from 'axios'

const Apis = axios.create({
    baseURL: 'http://192.168.1.131:3001',
    timeout: 5000,
    headers: {
        "Content-type": "application/json"
    }
});

export {
   Apis
}
