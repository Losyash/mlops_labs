import { createApp } from 'vue'
import VueApp from './app.vue'
import VueAxios from '@/plugins/axios';

const app = createApp(VueApp);

app.use(VueAxios);
app.provide('aixos', app.config.globalProperties.axios);
app.mount('#app')