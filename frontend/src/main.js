// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify' 
import router from './router';
import 'vuetify/dist/vuetify.min.css'
// Register components globally
const app = createApp(App);

// Mount the main app component
app.use(vuetify)
app.use(router)
app.mount('#app');
