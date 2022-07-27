import axios from 'axios';

// this base url will be change based on
// if you need to point to production.
const BASE_URL = process.env.VUE_APP_API_SERVER
const ACCESS_TOKEN = 'token'

const tokenRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
})

const checkToken = (token) => {
  const loginBody = { token }
  return tokenRequest.post('/check-token', loginBody)
    .then((response) => {
      return Promise.resolve(response.data)
    }).catch((error) => {
      return Promise.reject(error)
    })
}

const loginUser = (username, password) => {
  const loginBody = { username, password }
  return tokenRequest.post('/login', loginBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.token)
      return Promise.resolve(response.data)
    }).catch((error) => {
      return Promise.reject(error)
    })
}

const logoutUser = (username)=> {
  const logoutBody = { username }  
  tokenRequest.post('/logout', logoutBody)
  window.localStorage.removeItem(ACCESS_TOKEN)
  authRequest.defaults.headers.Authorization = ''
  authRequestFile.defaults.headers.Authorization = ''
}

const authRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Token ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    'Content-Type': 'application/json',
  },
})

const authRequestFile = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Token ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    'content-type': 'multipart/form-data',
  },
})

const errorInterceptor = (error) => {
  console.log(error.response)
  return Promise.reject(error);
};

authRequest.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
);

authRequestFile.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
);


export {
  tokenRequest, checkToken, loginUser, logoutUser, authRequest, authRequestFile,
  errorInterceptor, BASE_URL, ACCESS_TOKEN
};
