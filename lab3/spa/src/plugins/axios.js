import axios from 'axios';

export default {
  install(app, options) {
    const productHost = `${location.protocol}//${location.hostname}${location.port ? ':' + location.port: ''}`;
    const developHosts = ['localhost', '127.0.0.1', '::1'];
    const developPort = 8000;

    if (developHosts.includes(location.hostname)) {
      axios.defaults.baseURL = `${location.protocol}//${location.hostname}:${developPort}/api`;
      console.log(`API-URL = ${axios.defaults.baseURL}`);
    } else {
      axios.defaults.baseURL = `${productHost}/api`;
    };

    app.config.globalProperties.$axios = axios;
  }
};