// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify' 
import axios from 'axios';
import 'vuetify/dist/vuetify.min.css'
// Register components globally
const app = createApp(App);

// Mount the main app component
app.use(vuetify)
app.mount('#app');
